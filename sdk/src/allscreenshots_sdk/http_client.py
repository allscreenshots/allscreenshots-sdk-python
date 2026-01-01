"""
HTTP client with retry logic and error handling.

This module provides a wrapper around httpx that handles authentication,
retries with exponential backoff, and error translation.
"""

import contextlib
import random
import time
from typing import Any

import httpx

from allscreenshots_sdk.exceptions import (
    ApiError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    TimeoutError,
    ValidationError,
)


class HttpClient:
    """
    HTTP client with retry logic and authentication.

    This client wraps httpx and provides:
    - Automatic API key authentication via X-API-Key header
    - Retry logic with exponential backoff for transient failures
    - Translation of HTTP errors to typed SDK exceptions
    """

    DEFAULT_BASE_URL = "https://api.allscreenshots.com"
    DEFAULT_TIMEOUT = 60.0
    DEFAULT_MAX_RETRIES = 3
    DEFAULT_RETRY_DELAY = 1.0
    DEFAULT_MAX_RETRY_DELAY = 30.0

    RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}

    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        retry_delay: float = DEFAULT_RETRY_DELAY,
        max_retry_delay: float = DEFAULT_MAX_RETRY_DELAY,
    ) -> None:
        """
        Initialize the HTTP client.

        Args:
            api_key: API key for authentication.
            base_url: Base URL for the API.
            timeout: Request timeout in seconds.
            max_retries: Maximum number of retry attempts.
            retry_delay: Initial delay between retries in seconds.
            max_retry_delay: Maximum delay between retries in seconds.
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.max_retry_delay = max_retry_delay

        self._client = httpx.Client(
            base_url=self.base_url,
            timeout=httpx.Timeout(timeout),
            headers={
                "X-API-Key": api_key,
                "User-Agent": "allscreenshots-sdk-python/1.0.0",
                "Accept": "application/json",
            },
        )

    def close(self) -> None:
        """Close the HTTP client and release resources."""
        self._client.close()

    def __enter__(self) -> "HttpClient":
        """Enter context manager."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Exit context manager and close client."""
        self.close()

    def _calculate_retry_delay(self, attempt: int, retry_after: int | None = None) -> float:
        """
        Calculate delay before next retry with exponential backoff and jitter.

        Args:
            attempt: Current attempt number (0-indexed).
            retry_after: Optional retry-after header value in seconds.

        Returns:
            Delay in seconds before next retry.
        """
        if retry_after is not None:
            return min(float(retry_after), self.max_retry_delay)

        # Exponential backoff with jitter
        delay = self.retry_delay * (2**attempt)
        jitter = random.uniform(0, delay * 0.1)
        return min(delay + jitter, self.max_retry_delay)

    def _should_retry(self, response: httpx.Response) -> bool:
        """
        Determine if request should be retried based on response.

        Args:
            response: The HTTP response.

        Returns:
            True if the request should be retried.
        """
        return response.status_code in self.RETRYABLE_STATUS_CODES

    def _handle_error_response(self, response: httpx.Response) -> None:
        """
        Translate HTTP error responses to SDK exceptions.

        Args:
            response: The HTTP response.

        Raises:
            ValidationError: For 400 responses.
            AuthenticationError: For 401 responses.
            NotFoundError: For 404 responses.
            RateLimitError: For 429 responses.
            ServerError: For 5xx responses.
            ApiError: For other error responses.
        """
        try:
            error_data = response.json()
            message = error_data.get("message") or error_data.get("error", "Unknown error")
            error_code = error_data.get("code") or error_data.get("errorCode")
            details = error_data
        except Exception:
            message = response.text or f"HTTP {response.status_code}"
            error_code = None
            details = {}

        status_code = response.status_code

        if status_code == 400:
            raise ValidationError(message, error_code, details)
        elif status_code == 401:
            raise AuthenticationError(message, error_code, details)
        elif status_code == 404:
            raise NotFoundError(message, error_code, details)
        elif status_code == 429:
            retry_after = None
            if "Retry-After" in response.headers:
                with contextlib.suppress(ValueError):
                    retry_after = int(response.headers["Retry-After"])
            raise RateLimitError(message, retry_after, error_code, details)
        elif 500 <= status_code < 600:
            raise ServerError(message, status_code, error_code, details)
        else:
            raise ApiError(message, status_code, error_code, details)

    def request(
        self,
        method: str,
        path: str,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """
        Make an HTTP request with retry logic.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.).
            path: API endpoint path.
            json: JSON body data.
            params: Query parameters.
            headers: Additional headers.

        Returns:
            The HTTP response.

        Raises:
            TimeoutError: If the request times out after all retries.
            ApiError: If the API returns an error after all retries.
        """
        # Filter out None values from params
        if params:
            params = {k: v for k, v in params.items() if v is not None}

        last_exception: Exception | None = None

        for attempt in range(self.max_retries + 1):
            try:
                response = self._client.request(
                    method=method,
                    url=path,
                    json=json,
                    params=params,
                    headers=headers,
                )

                if response.is_success:
                    return response

                if self._should_retry(response) and attempt < self.max_retries:
                    retry_after = None
                    if "Retry-After" in response.headers:
                        with contextlib.suppress(ValueError):
                            retry_after = int(response.headers["Retry-After"])
                    delay = self._calculate_retry_delay(attempt, retry_after)
                    time.sleep(delay)
                    continue

                self._handle_error_response(response)

            except httpx.TimeoutException as e:
                last_exception = e
                if attempt < self.max_retries:
                    delay = self._calculate_retry_delay(attempt)
                    time.sleep(delay)
                    continue
                raise TimeoutError(
                    f"Request timed out after {self.timeout} seconds",
                    timeout=self.timeout,
                ) from e

            except httpx.RequestError as e:
                last_exception = e
                if attempt < self.max_retries:
                    delay = self._calculate_retry_delay(attempt)
                    time.sleep(delay)
                    continue
                raise ApiError(
                    f"Request failed: {str(e)}",
                    status_code=0,
                    details={"original_error": str(e)},
                ) from e

        # Should not reach here, but just in case
        if last_exception:
            raise ApiError(f"Request failed after {self.max_retries} retries: {last_exception}", 0)
        raise ApiError("Request failed unexpectedly", 0)

    def get(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """
        Make a GET request.

        Args:
            path: API endpoint path.
            params: Query parameters.
            headers: Additional headers.

        Returns:
            The HTTP response.
        """
        return self.request("GET", path, params=params, headers=headers)

    def post(
        self,
        path: str,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """
        Make a POST request.

        Args:
            path: API endpoint path.
            json: JSON body data.
            params: Query parameters.
            headers: Additional headers.

        Returns:
            The HTTP response.
        """
        return self.request("POST", path, json=json, params=params, headers=headers)

    def put(
        self,
        path: str,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """
        Make a PUT request.

        Args:
            path: API endpoint path.
            json: JSON body data.
            params: Query parameters.
            headers: Additional headers.

        Returns:
            The HTTP response.
        """
        return self.request("PUT", path, json=json, params=params, headers=headers)

    def delete(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """
        Make a DELETE request.

        Args:
            path: API endpoint path.
            params: Query parameters.
            headers: Additional headers.

        Returns:
            The HTTP response.
        """
        return self.request("DELETE", path, params=params, headers=headers)


class AsyncHttpClient:
    """
    Async HTTP client with retry logic and authentication.

    This client wraps httpx.AsyncClient and provides:
    - Automatic API key authentication via X-API-Key header
    - Retry logic with exponential backoff for transient failures
    - Translation of HTTP errors to typed SDK exceptions
    """

    DEFAULT_BASE_URL = "https://api.allscreenshots.com"
    DEFAULT_TIMEOUT = 60.0
    DEFAULT_MAX_RETRIES = 3
    DEFAULT_RETRY_DELAY = 1.0
    DEFAULT_MAX_RETRY_DELAY = 30.0

    RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}

    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        retry_delay: float = DEFAULT_RETRY_DELAY,
        max_retry_delay: float = DEFAULT_MAX_RETRY_DELAY,
    ) -> None:
        """
        Initialize the async HTTP client.

        Args:
            api_key: API key for authentication.
            base_url: Base URL for the API.
            timeout: Request timeout in seconds.
            max_retries: Maximum number of retry attempts.
            retry_delay: Initial delay between retries in seconds.
            max_retry_delay: Maximum delay between retries in seconds.
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.max_retry_delay = max_retry_delay

        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=httpx.Timeout(timeout),
            headers={
                "X-API-Key": api_key,
                "User-Agent": "allscreenshots-sdk-python/1.0.0",
                "Accept": "application/json",
            },
        )

    async def close(self) -> None:
        """Close the HTTP client and release resources."""
        await self._client.aclose()

    async def __aenter__(self) -> "AsyncHttpClient":
        """Enter async context manager."""
        return self

    async def __aexit__(self, *args: Any) -> None:
        """Exit async context manager and close client."""
        await self.close()

    def _calculate_retry_delay(self, attempt: int, retry_after: int | None = None) -> float:
        """Calculate delay before next retry with exponential backoff and jitter."""
        if retry_after is not None:
            return min(float(retry_after), self.max_retry_delay)
        delay = self.retry_delay * (2**attempt)
        jitter = random.uniform(0, delay * 0.1)
        return min(delay + jitter, self.max_retry_delay)

    def _should_retry(self, response: httpx.Response) -> bool:
        """Determine if request should be retried based on response."""
        return response.status_code in self.RETRYABLE_STATUS_CODES

    def _handle_error_response(self, response: httpx.Response) -> None:
        """Translate HTTP error responses to SDK exceptions."""
        try:
            error_data = response.json()
            message = error_data.get("message") or error_data.get("error", "Unknown error")
            error_code = error_data.get("code") or error_data.get("errorCode")
            details = error_data
        except Exception:
            message = response.text or f"HTTP {response.status_code}"
            error_code = None
            details = {}

        status_code = response.status_code

        if status_code == 400:
            raise ValidationError(message, error_code, details)
        elif status_code == 401:
            raise AuthenticationError(message, error_code, details)
        elif status_code == 404:
            raise NotFoundError(message, error_code, details)
        elif status_code == 429:
            retry_after = None
            if "Retry-After" in response.headers:
                with contextlib.suppress(ValueError):
                    retry_after = int(response.headers["Retry-After"])
            raise RateLimitError(message, retry_after, error_code, details)
        elif 500 <= status_code < 600:
            raise ServerError(message, status_code, error_code, details)
        else:
            raise ApiError(message, status_code, error_code, details)

    async def request(
        self,
        method: str,
        path: str,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make an async HTTP request with retry logic."""
        import asyncio

        if params:
            params = {k: v for k, v in params.items() if v is not None}

        last_exception: Exception | None = None

        for attempt in range(self.max_retries + 1):
            try:
                response = await self._client.request(
                    method=method,
                    url=path,
                    json=json,
                    params=params,
                    headers=headers,
                )

                if response.is_success:
                    return response

                if self._should_retry(response) and attempt < self.max_retries:
                    retry_after = None
                    if "Retry-After" in response.headers:
                        with contextlib.suppress(ValueError):
                            retry_after = int(response.headers["Retry-After"])
                    delay = self._calculate_retry_delay(attempt, retry_after)
                    await asyncio.sleep(delay)
                    continue

                self._handle_error_response(response)

            except httpx.TimeoutException as e:
                last_exception = e
                if attempt < self.max_retries:
                    delay = self._calculate_retry_delay(attempt)
                    await asyncio.sleep(delay)
                    continue
                raise TimeoutError(
                    f"Request timed out after {self.timeout} seconds",
                    timeout=self.timeout,
                ) from e

            except httpx.RequestError as e:
                last_exception = e
                if attempt < self.max_retries:
                    delay = self._calculate_retry_delay(attempt)
                    await asyncio.sleep(delay)
                    continue
                raise ApiError(
                    f"Request failed: {str(e)}",
                    status_code=0,
                    details={"original_error": str(e)},
                ) from e

        if last_exception:
            raise ApiError(f"Request failed after {self.max_retries} retries: {last_exception}", 0)
        raise ApiError("Request failed unexpectedly", 0)

    async def get(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make an async GET request."""
        return await self.request("GET", path, params=params, headers=headers)

    async def post(
        self,
        path: str,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make an async POST request."""
        return await self.request("POST", path, json=json, params=params, headers=headers)

    async def put(
        self,
        path: str,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make an async PUT request."""
        return await self.request("PUT", path, json=json, params=params, headers=headers)

    async def delete(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make an async DELETE request."""
        return await self.request("DELETE", path, params=params, headers=headers)

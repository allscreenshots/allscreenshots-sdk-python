"""
Main client module for the Allscreenshots SDK.

This module provides the AllscreenshotsClient and its builder for creating
configured API clients.
"""

import os
from typing import Any

from allscreenshots_sdk.api.bulk import AsyncBulkApi, BulkApi
from allscreenshots_sdk.api.compose import AsyncComposeApi, ComposeApi
from allscreenshots_sdk.api.schedules import AsyncSchedulesApi, SchedulesApi
from allscreenshots_sdk.api.screenshots import AsyncScreenshotsApi, ScreenshotsApi
from allscreenshots_sdk.api.usage import AsyncUsageApi, UsageApi
from allscreenshots_sdk.http_client import AsyncHttpClient, HttpClient


class AllscreenshotsClientBuilder:
    """
    Builder for creating AllscreenshotsClient instances.

    Use the builder pattern to configure the client with your API key and
    optional settings like base URL and timeout.

    Example:
        >>> client = (
        ...     AllscreenshotsClient.builder()
        ...     .with_api_key("your-api-key")
        ...     .with_timeout(120.0)
        ...     .build()
        ... )
    """

    def __init__(self) -> None:
        """Initialize the builder with default values."""
        self._api_key: str | None = None
        self._base_url: str = HttpClient.DEFAULT_BASE_URL
        self._timeout: float = HttpClient.DEFAULT_TIMEOUT
        self._max_retries: int = HttpClient.DEFAULT_MAX_RETRIES
        self._retry_delay: float = HttpClient.DEFAULT_RETRY_DELAY
        self._max_retry_delay: float = HttpClient.DEFAULT_MAX_RETRY_DELAY

    def with_api_key(self, api_key: str) -> "AllscreenshotsClientBuilder":
        """
        Set the API key for authentication.

        Args:
            api_key: Your Allscreenshots API key.

        Returns:
            The builder instance for chaining.

        Example:
            >>> builder.with_api_key("sk_live_...")
        """
        self._api_key = api_key
        return self

    def with_base_url(self, base_url: str) -> "AllscreenshotsClientBuilder":
        """
        Set a custom base URL for the API.

        Args:
            base_url: The base URL (e.g., "https://api.allscreenshots.com").

        Returns:
            The builder instance for chaining.

        Example:
            >>> builder.with_base_url("https://staging-api.allscreenshots.com")
        """
        self._base_url = base_url
        return self

    def with_timeout(self, timeout: float) -> "AllscreenshotsClientBuilder":
        """
        Set the request timeout in seconds.

        Args:
            timeout: Timeout in seconds (default: 60.0).

        Returns:
            The builder instance for chaining.

        Example:
            >>> builder.with_timeout(120.0)  # 2 minutes
        """
        self._timeout = timeout
        return self

    def with_max_retries(self, max_retries: int) -> "AllscreenshotsClientBuilder":
        """
        Set the maximum number of retry attempts.

        Args:
            max_retries: Maximum retries (default: 3).

        Returns:
            The builder instance for chaining.

        Example:
            >>> builder.with_max_retries(5)
        """
        self._max_retries = max_retries
        return self

    def with_retry_delay(self, retry_delay: float) -> "AllscreenshotsClientBuilder":
        """
        Set the initial retry delay in seconds.

        Args:
            retry_delay: Initial delay between retries (default: 1.0).

        Returns:
            The builder instance for chaining.

        Example:
            >>> builder.with_retry_delay(2.0)
        """
        self._retry_delay = retry_delay
        return self

    def with_max_retry_delay(self, max_retry_delay: float) -> "AllscreenshotsClientBuilder":
        """
        Set the maximum retry delay in seconds.

        Args:
            max_retry_delay: Maximum delay between retries (default: 30.0).

        Returns:
            The builder instance for chaining.

        Example:
            >>> builder.with_max_retry_delay(60.0)
        """
        self._max_retry_delay = max_retry_delay
        return self

    def build(self) -> "AllscreenshotsClient":
        """
        Build and return a synchronous AllscreenshotsClient.

        The API key is resolved in this order:
        1. Explicitly set via with_api_key()
        2. ALLSCREENSHOTS_API_KEY environment variable

        Returns:
            A configured AllscreenshotsClient instance.

        Raises:
            ValueError: If no API key is provided or found in environment.

        Example:
            >>> client = AllscreenshotsClient.builder().with_api_key("key").build()
            >>> image = client.screenshots.capture("https://example.com")
        """
        api_key = self._api_key or os.environ.get("ALLSCREENSHOTS_API_KEY")
        if not api_key:
            raise ValueError(
                "API key is required. Set it via with_api_key() or "
                "ALLSCREENSHOTS_API_KEY environment variable."
            )

        http_client = HttpClient(
            api_key=api_key,
            base_url=self._base_url,
            timeout=self._timeout,
            max_retries=self._max_retries,
            retry_delay=self._retry_delay,
            max_retry_delay=self._max_retry_delay,
        )

        return AllscreenshotsClient(http_client)

    def build_async(self) -> "AsyncAllscreenshotsClient":
        """
        Build and return an asynchronous AllscreenshotsClient.

        The API key is resolved in this order:
        1. Explicitly set via with_api_key()
        2. ALLSCREENSHOTS_API_KEY environment variable

        Returns:
            A configured AsyncAllscreenshotsClient instance.

        Raises:
            ValueError: If no API key is provided or found in environment.

        Example:
            >>> async with AllscreenshotsClient.builder().with_api_key("key").build_async() as client:
            ...     image = await client.screenshots.capture("https://example.com")
        """
        api_key = self._api_key or os.environ.get("ALLSCREENSHOTS_API_KEY")
        if not api_key:
            raise ValueError(
                "API key is required. Set it via with_api_key() or "
                "ALLSCREENSHOTS_API_KEY environment variable."
            )

        http_client = AsyncHttpClient(
            api_key=api_key,
            base_url=self._base_url,
            timeout=self._timeout,
            max_retries=self._max_retries,
            retry_delay=self._retry_delay,
            max_retry_delay=self._max_retry_delay,
        )

        return AsyncAllscreenshotsClient(http_client)


class AllscreenshotsClient:
    """
    Synchronous client for the Allscreenshots API.

    Use the builder pattern to create instances:

    Example:
        >>> client = AllscreenshotsClient.builder().with_api_key("key").build()
        >>>
        >>> # Capture a screenshot
        >>> image = client.screenshots.capture("https://example.com")
        >>>
        >>> # Save to file
        >>> with open("screenshot.png", "wb") as f:
        ...     f.write(image)
        >>>
        >>> # Clean up when done
        >>> client.close()

    The client can also be used as a context manager:

        >>> with AllscreenshotsClient.builder().with_api_key("key").build() as client:
        ...     image = client.screenshots.capture("https://example.com")
    """

    def __init__(self, http_client: HttpClient) -> None:
        """
        Initialize the client with an HTTP client.

        Args:
            http_client: Configured HTTP client instance.
        """
        self._http = http_client
        self._screenshots = ScreenshotsApi(http_client)
        self._bulk = BulkApi(http_client)
        self._compose = ComposeApi(http_client)
        self._schedules = SchedulesApi(http_client)
        self._usage = UsageApi(http_client)

    @staticmethod
    def builder() -> AllscreenshotsClientBuilder:
        """
        Create a new client builder.

        Returns:
            A new AllscreenshotsClientBuilder instance.

        Example:
            >>> client = AllscreenshotsClient.builder().with_api_key("key").build()
        """
        return AllscreenshotsClientBuilder()

    @property
    def screenshots(self) -> ScreenshotsApi:
        """
        Access the Screenshots API.

        Returns:
            ScreenshotsApi instance for capturing screenshots.

        Example:
            >>> image = client.screenshots.capture("https://example.com")
        """
        return self._screenshots

    @property
    def bulk(self) -> BulkApi:
        """
        Access the Bulk Screenshots API.

        Returns:
            BulkApi instance for bulk operations.

        Example:
            >>> job = client.bulk.create(["https://a.com", "https://b.com"])
        """
        return self._bulk

    @property
    def compose(self) -> ComposeApi:
        """
        Access the Compose API.

        Returns:
            ComposeApi instance for composing multiple screenshots.

        Example:
            >>> result = client.compose.create([CaptureItem(url="https://example.com")])
        """
        return self._compose

    @property
    def schedules(self) -> SchedulesApi:
        """
        Access the Schedules API.

        Returns:
            SchedulesApi instance for managing scheduled captures.

        Example:
            >>> schedule = client.schedules.create(
            ...     name="Daily", url="https://example.com", schedule="0 9 * * *"
            ... )
        """
        return self._schedules

    @property
    def usage(self) -> UsageApi:
        """
        Access the Usage API.

        Returns:
            UsageApi instance for checking usage and quotas.

        Example:
            >>> usage = client.usage.get()
            >>> print(f"Screenshots used: {usage.current_period.screenshots_count}")
        """
        return self._usage

    def close(self) -> None:
        """
        Close the client and release resources.

        Call this method when you're done using the client to properly
        clean up HTTP connections.

        Example:
            >>> client = AllscreenshotsClient.builder().with_api_key("key").build()
            >>> try:
            ...     image = client.screenshots.capture("https://example.com")
            ... finally:
            ...     client.close()
        """
        self._http.close()

    def __enter__(self) -> "AllscreenshotsClient":
        """Enter context manager."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Exit context manager and close client."""
        self.close()


class AsyncAllscreenshotsClient:
    """
    Asynchronous client for the Allscreenshots API.

    Use the builder pattern to create instances:

    Example:
        >>> async with AllscreenshotsClient.builder().with_api_key("key").build_async() as client:
        ...     image = await client.screenshots.capture("https://example.com")
        ...     with open("screenshot.png", "wb") as f:
        ...         f.write(image)
    """

    def __init__(self, http_client: AsyncHttpClient) -> None:
        """
        Initialize the async client with an HTTP client.

        Args:
            http_client: Configured async HTTP client instance.
        """
        self._http = http_client
        self._screenshots = AsyncScreenshotsApi(http_client)
        self._bulk = AsyncBulkApi(http_client)
        self._compose = AsyncComposeApi(http_client)
        self._schedules = AsyncSchedulesApi(http_client)
        self._usage = AsyncUsageApi(http_client)

    @property
    def screenshots(self) -> AsyncScreenshotsApi:
        """Access the async Screenshots API."""
        return self._screenshots

    @property
    def bulk(self) -> AsyncBulkApi:
        """Access the async Bulk Screenshots API."""
        return self._bulk

    @property
    def compose(self) -> AsyncComposeApi:
        """Access the async Compose API."""
        return self._compose

    @property
    def schedules(self) -> AsyncSchedulesApi:
        """Access the async Schedules API."""
        return self._schedules

    @property
    def usage(self) -> AsyncUsageApi:
        """Access the async Usage API."""
        return self._usage

    async def close(self) -> None:
        """Close the client and release resources."""
        await self._http.close()

    async def __aenter__(self) -> "AsyncAllscreenshotsClient":
        """Enter async context manager."""
        return self

    async def __aexit__(self, *args: Any) -> None:
        """Exit async context manager and close client."""
        await self.close()

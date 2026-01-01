"""
Custom exceptions for the Allscreenshots SDK.

All exceptions inherit from AllscreenshotsError for easy catching of any SDK-related errors.

Example:
    >>> from allscreenshots_sdk import AllscreenshotsClient, AllscreenshotsError
    >>> try:
    ...     client.screenshots.capture("invalid-url")
    ... except AllscreenshotsError as e:
    ...     print(f"Error: {e}")
"""

from typing import Any


class AllscreenshotsError(Exception):
    """Base exception for all Allscreenshots SDK errors."""

    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None:
        """
        Initialize an AllscreenshotsError.

        Args:
            message: Human-readable error message.
            details: Optional dictionary with additional error details.
        """
        super().__init__(message)
        self.message = message
        self.details = details or {}


class ApiError(AllscreenshotsError):
    """Error returned from the Allscreenshots API."""

    def __init__(
        self,
        message: str,
        status_code: int,
        error_code: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """
        Initialize an ApiError.

        Args:
            message: Human-readable error message.
            status_code: HTTP status code from the API response.
            error_code: Optional error code from the API.
            details: Optional dictionary with additional error details.
        """
        super().__init__(message, details)
        self.status_code = status_code
        self.error_code = error_code

    def __str__(self) -> str:
        """Return a string representation of the error."""
        if self.error_code:
            return f"[{self.status_code}] {self.error_code}: {self.message}"
        return f"[{self.status_code}] {self.message}"


class ValidationError(ApiError):
    """Raised when request validation fails (HTTP 400)."""

    def __init__(
        self,
        message: str,
        error_code: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """
        Initialize a ValidationError.

        Args:
            message: Human-readable error message.
            error_code: Optional error code from the API.
            details: Optional dictionary with validation error details.
        """
        super().__init__(message, 400, error_code, details)


class AuthenticationError(ApiError):
    """Raised when authentication fails (HTTP 401)."""

    def __init__(
        self,
        message: str = "Invalid or missing API key",
        error_code: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """
        Initialize an AuthenticationError.

        Args:
            message: Human-readable error message.
            error_code: Optional error code from the API.
            details: Optional dictionary with additional error details.
        """
        super().__init__(message, 401, error_code, details)


class NotFoundError(ApiError):
    """Raised when a resource is not found (HTTP 404)."""

    def __init__(
        self,
        message: str = "Resource not found",
        error_code: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """
        Initialize a NotFoundError.

        Args:
            message: Human-readable error message.
            error_code: Optional error code from the API.
            details: Optional dictionary with additional error details.
        """
        super().__init__(message, 404, error_code, details)


class RateLimitError(ApiError):
    """Raised when rate limit is exceeded (HTTP 429)."""

    def __init__(
        self,
        message: str = "Rate limit exceeded",
        retry_after: int | None = None,
        error_code: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """
        Initialize a RateLimitError.

        Args:
            message: Human-readable error message.
            retry_after: Optional number of seconds to wait before retrying.
            error_code: Optional error code from the API.
            details: Optional dictionary with additional error details.
        """
        super().__init__(message, 429, error_code, details)
        self.retry_after = retry_after


class ServerError(ApiError):
    """Raised when the server returns an error (HTTP 5xx)."""

    def __init__(
        self,
        message: str = "Internal server error",
        status_code: int = 500,
        error_code: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """
        Initialize a ServerError.

        Args:
            message: Human-readable error message.
            status_code: HTTP status code (5xx).
            error_code: Optional error code from the API.
            details: Optional dictionary with additional error details.
        """
        super().__init__(message, status_code, error_code, details)


class TimeoutError(AllscreenshotsError):
    """Raised when a request times out."""

    def __init__(
        self,
        message: str = "Request timed out",
        timeout: float | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """
        Initialize a TimeoutError.

        Args:
            message: Human-readable error message.
            timeout: The timeout value in seconds that was exceeded.
            details: Optional dictionary with additional error details.
        """
        super().__init__(message, details)
        self.timeout = timeout

"""Unit tests for exception classes."""

from allscreenshots_sdk.exceptions import (
    AllscreenshotsError,
    ApiError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    TimeoutError,
    ValidationError,
)


class TestAllscreenshotsError:
    """Tests for base AllscreenshotsError."""

    def test_basic_error(self) -> None:
        """Test creating a basic error."""
        error = AllscreenshotsError("Something went wrong")
        assert str(error) == "Something went wrong"
        assert error.message == "Something went wrong"
        assert error.details == {}

    def test_error_with_details(self) -> None:
        """Test creating an error with details."""
        error = AllscreenshotsError("Error", details={"field": "url", "issue": "invalid"})
        assert error.details == {"field": "url", "issue": "invalid"}

    def test_error_inheritance(self) -> None:
        """Test that all errors inherit from AllscreenshotsError."""
        errors = [
            ApiError("msg", 400),
            ValidationError("msg"),
            AuthenticationError(),
            NotFoundError(),
            RateLimitError(),
            ServerError(),
            TimeoutError(),
        ]
        for error in errors:
            assert isinstance(error, AllscreenshotsError)


class TestApiError:
    """Tests for ApiError."""

    def test_api_error_creation(self) -> None:
        """Test creating an API error."""
        error = ApiError("Bad request", 400, "INVALID_URL", {"url": "not-valid"})
        assert error.message == "Bad request"
        assert error.status_code == 400
        assert error.error_code == "INVALID_URL"
        assert error.details == {"url": "not-valid"}

    def test_api_error_str_with_code(self) -> None:
        """Test string representation with error code."""
        error = ApiError("Bad request", 400, "INVALID_URL")
        assert str(error) == "[400] INVALID_URL: Bad request"

    def test_api_error_str_without_code(self) -> None:
        """Test string representation without error code."""
        error = ApiError("Bad request", 400)
        assert str(error) == "[400] Bad request"


class TestValidationError:
    """Tests for ValidationError."""

    def test_validation_error(self) -> None:
        """Test creating a validation error."""
        error = ValidationError("Invalid URL format", "INVALID_URL")
        assert error.status_code == 400
        assert error.error_code == "INVALID_URL"

    def test_validation_error_with_details(self) -> None:
        """Test validation error with field details."""
        error = ValidationError(
            "Validation failed",
            details={"errors": [{"field": "url", "message": "Invalid format"}]},
        )
        assert "errors" in error.details


class TestAuthenticationError:
    """Tests for AuthenticationError."""

    def test_default_message(self) -> None:
        """Test default authentication error message."""
        error = AuthenticationError()
        assert error.status_code == 401
        assert "API key" in error.message

    def test_custom_message(self) -> None:
        """Test custom authentication error message."""
        error = AuthenticationError("API key expired")
        assert error.message == "API key expired"


class TestNotFoundError:
    """Tests for NotFoundError."""

    def test_default_message(self) -> None:
        """Test default not found error message."""
        error = NotFoundError()
        assert error.status_code == 404
        assert "not found" in error.message.lower()

    def test_custom_message(self) -> None:
        """Test custom not found error message."""
        error = NotFoundError("Job job-123 not found")
        assert error.message == "Job job-123 not found"


class TestRateLimitError:
    """Tests for RateLimitError."""

    def test_default_message(self) -> None:
        """Test default rate limit error message."""
        error = RateLimitError()
        assert error.status_code == 429
        assert "rate limit" in error.message.lower()

    def test_with_retry_after(self) -> None:
        """Test rate limit error with retry-after."""
        error = RateLimitError("Too many requests", retry_after=30)
        assert error.retry_after == 30

    def test_without_retry_after(self) -> None:
        """Test rate limit error without retry-after."""
        error = RateLimitError()
        assert error.retry_after is None


class TestServerError:
    """Tests for ServerError."""

    def test_default_values(self) -> None:
        """Test default server error values."""
        error = ServerError()
        assert error.status_code == 500
        assert "internal" in error.message.lower() or "server" in error.message.lower()

    def test_custom_status_code(self) -> None:
        """Test server error with custom status code."""
        error = ServerError("Service unavailable", status_code=503)
        assert error.status_code == 503


class TestTimeoutError:
    """Tests for TimeoutError."""

    def test_default_message(self) -> None:
        """Test default timeout error message."""
        error = TimeoutError()
        assert "timed out" in error.message.lower()

    def test_with_timeout_value(self) -> None:
        """Test timeout error with timeout value."""
        error = TimeoutError("Request timed out", timeout=30.0)
        assert error.timeout == 30.0

    def test_not_api_error(self) -> None:
        """Test that TimeoutError is not an ApiError."""
        error = TimeoutError()
        assert not isinstance(error, ApiError)
        assert isinstance(error, AllscreenshotsError)

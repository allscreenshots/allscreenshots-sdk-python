"""Unit tests for HTTP client functionality."""

import pytest
from pytest_httpx import HTTPXMock

from allscreenshots_sdk.exceptions import (
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)
from allscreenshots_sdk.http_client import HttpClient


class TestHttpClient:
    """Tests for HttpClient."""

    def test_client_initialization(self) -> None:
        """Test client initialization with defaults."""
        client = HttpClient(api_key="test-key")
        try:
            assert client.api_key == "test-key"
            assert client.base_url == "https://api.allscreenshots.com"
            assert client.timeout == 60.0
            assert client.max_retries == 3
        finally:
            client.close()

    def test_client_custom_config(self) -> None:
        """Test client with custom configuration."""
        client = HttpClient(
            api_key="test-key",
            base_url="https://custom.api.com",
            timeout=120.0,
            max_retries=5,
        )
        try:
            assert client.base_url == "https://custom.api.com"
            assert client.timeout == 120.0
            assert client.max_retries == 5
        finally:
            client.close()

    def test_base_url_trailing_slash_removed(self) -> None:
        """Test that trailing slash is removed from base URL."""
        client = HttpClient(api_key="test-key", base_url="https://api.example.com/")
        try:
            assert client.base_url == "https://api.example.com"
        finally:
            client.close()

    def test_context_manager(self) -> None:
        """Test client as context manager."""
        with HttpClient(api_key="test-key") as client:
            assert client.api_key == "test-key"


class TestHttpClientRequests:
    """Tests for HTTP client requests."""

    def test_successful_get_request(self, httpx_mock: HTTPXMock) -> None:
        """Test successful GET request."""
        httpx_mock.add_response(
            method="GET",
            url="https://api.allscreenshots.com/v1/test",
            json={"status": "ok"},
        )

        with HttpClient(api_key="test-key") as client:
            response = client.get("/v1/test")
            assert response.json() == {"status": "ok"}

    def test_successful_post_request(self, httpx_mock: HTTPXMock) -> None:
        """Test successful POST request."""
        httpx_mock.add_response(
            method="POST",
            url="https://api.allscreenshots.com/v1/screenshots",
            content=b"image-data",
        )

        with HttpClient(api_key="test-key") as client:
            response = client.post("/v1/screenshots", json={"url": "https://example.com"})
            assert response.content == b"image-data"

    def test_api_key_header(self, httpx_mock: HTTPXMock) -> None:
        """Test that API key is sent in header."""
        httpx_mock.add_response(url="https://api.allscreenshots.com/v1/test")

        with HttpClient(api_key="my-api-key") as client:
            client.get("/v1/test")

        request = httpx_mock.get_request()
        assert request is not None
        assert request.headers["X-API-Key"] == "my-api-key"

    def test_user_agent_header(self, httpx_mock: HTTPXMock) -> None:
        """Test that User-Agent header is set."""
        httpx_mock.add_response(url="https://api.allscreenshots.com/v1/test")

        with HttpClient(api_key="test-key") as client:
            client.get("/v1/test")

        request = httpx_mock.get_request()
        assert request is not None
        assert "allscreenshots-sdk-python" in request.headers["User-Agent"]

    def test_query_params(self, httpx_mock: HTTPXMock) -> None:
        """Test that query params are properly passed."""
        httpx_mock.add_response(url="https://api.allscreenshots.com/v1/test?limit=10")

        with HttpClient(api_key="test-key") as client:
            client.get("/v1/test", params={"limit": 10})

        request = httpx_mock.get_request()
        assert request is not None
        assert "limit=10" in str(request.url)

    def test_none_params_filtered(self, httpx_mock: HTTPXMock) -> None:
        """Test that None values are filtered from params."""
        httpx_mock.add_response(url="https://api.allscreenshots.com/v1/test?limit=10")

        with HttpClient(api_key="test-key") as client:
            client.get("/v1/test", params={"limit": 10, "offset": None})

        request = httpx_mock.get_request()
        assert request is not None
        assert "offset" not in str(request.url)


class TestHttpClientErrorHandling:
    """Tests for HTTP client error handling."""

    def test_validation_error_400(self, httpx_mock: HTTPXMock) -> None:
        """Test that 400 raises ValidationError."""
        httpx_mock.add_response(
            status_code=400,
            json={"message": "Invalid URL", "code": "INVALID_URL"},
        )

        with HttpClient(api_key="test-key") as client:
            with pytest.raises(ValidationError) as exc_info:
                client.get("/v1/test")
            assert exc_info.value.status_code == 400
            assert exc_info.value.error_code == "INVALID_URL"

    def test_authentication_error_401(self, httpx_mock: HTTPXMock) -> None:
        """Test that 401 raises AuthenticationError."""
        httpx_mock.add_response(
            status_code=401,
            json={"message": "Invalid API key"},
        )

        with HttpClient(api_key="bad-key") as client:
            with pytest.raises(AuthenticationError) as exc_info:
                client.get("/v1/test")
            assert exc_info.value.status_code == 401

    def test_not_found_error_404(self, httpx_mock: HTTPXMock) -> None:
        """Test that 404 raises NotFoundError."""
        httpx_mock.add_response(
            status_code=404,
            json={"message": "Job not found"},
        )

        with HttpClient(api_key="test-key") as client:
            with pytest.raises(NotFoundError) as exc_info:
                client.get("/v1/jobs/nonexistent")
            assert exc_info.value.status_code == 404

    def test_rate_limit_error_429(self, httpx_mock: HTTPXMock) -> None:
        """Test that 429 raises RateLimitError."""
        httpx_mock.add_response(
            status_code=429,
            json={"message": "Rate limit exceeded"},
            headers={"Retry-After": "30"},
        )

        with HttpClient(api_key="test-key", max_retries=0) as client:
            with pytest.raises(RateLimitError) as exc_info:
                client.get("/v1/test")
            assert exc_info.value.status_code == 429
            assert exc_info.value.retry_after == 30

    def test_server_error_500(self, httpx_mock: HTTPXMock) -> None:
        """Test that 500 raises ServerError."""
        httpx_mock.add_response(
            status_code=500,
            json={"message": "Internal server error"},
        )

        with HttpClient(api_key="test-key", max_retries=0) as client:
            with pytest.raises(ServerError) as exc_info:
                client.get("/v1/test")
            assert exc_info.value.status_code == 500

    def test_server_error_503(self, httpx_mock: HTTPXMock) -> None:
        """Test that 503 raises ServerError."""
        httpx_mock.add_response(
            status_code=503,
            json={"message": "Service unavailable"},
        )

        with HttpClient(api_key="test-key", max_retries=0) as client:
            with pytest.raises(ServerError) as exc_info:
                client.get("/v1/test")
            assert exc_info.value.status_code == 503


class TestHttpClientRetry:
    """Tests for HTTP client retry logic."""

    def test_retry_on_500(self, httpx_mock: HTTPXMock) -> None:
        """Test that 500 errors are retried."""
        # First two requests fail, third succeeds
        httpx_mock.add_response(status_code=500)
        httpx_mock.add_response(status_code=500)
        httpx_mock.add_response(json={"status": "ok"})

        with HttpClient(api_key="test-key", retry_delay=0.01) as client:
            response = client.get("/v1/test")
            assert response.json() == {"status": "ok"}

        # Verify 3 requests were made
        requests = httpx_mock.get_requests()
        assert len(requests) == 3

    def test_retry_on_429(self, httpx_mock: HTTPXMock) -> None:
        """Test that 429 errors are retried."""
        httpx_mock.add_response(status_code=429)
        httpx_mock.add_response(json={"status": "ok"})

        with HttpClient(api_key="test-key", retry_delay=0.01) as client:
            response = client.get("/v1/test")
            assert response.json() == {"status": "ok"}

    def test_no_retry_on_400(self, httpx_mock: HTTPXMock) -> None:
        """Test that 400 errors are not retried."""
        httpx_mock.add_response(status_code=400, json={"message": "Bad request"})

        with HttpClient(api_key="test-key") as client, pytest.raises(ValidationError):
            client.get("/v1/test")

        # Only 1 request should be made
        requests = httpx_mock.get_requests()
        assert len(requests) == 1

    def test_no_retry_on_401(self, httpx_mock: HTTPXMock) -> None:
        """Test that 401 errors are not retried."""
        httpx_mock.add_response(status_code=401, json={"message": "Unauthorized"})

        with HttpClient(api_key="test-key") as client, pytest.raises(AuthenticationError):
            client.get("/v1/test")

        requests = httpx_mock.get_requests()
        assert len(requests) == 1

    def test_max_retries_exceeded(self, httpx_mock: HTTPXMock) -> None:
        """Test that error is raised after max retries."""
        # All requests fail
        for _ in range(4):  # 1 initial + 3 retries
            httpx_mock.add_response(status_code=500)

        with (
            HttpClient(api_key="test-key", max_retries=3, retry_delay=0.01) as client,
            pytest.raises(ServerError),
        ):
            client.get("/v1/test")

        requests = httpx_mock.get_requests()
        assert len(requests) == 4  # 1 initial + 3 retries


class TestHttpClientMethods:
    """Tests for HTTP client methods."""

    def test_put_method(self, httpx_mock: HTTPXMock) -> None:
        """Test PUT request."""
        httpx_mock.add_response(method="PUT", json={"updated": True})

        with HttpClient(api_key="test-key") as client:
            response = client.put("/v1/resource/1", json={"name": "new-name"})
            assert response.json() == {"updated": True}

    def test_delete_method(self, httpx_mock: HTTPXMock) -> None:
        """Test DELETE request."""
        httpx_mock.add_response(method="DELETE", status_code=204)

        with HttpClient(api_key="test-key") as client:
            response = client.delete("/v1/resource/1")
            assert response.status_code == 204

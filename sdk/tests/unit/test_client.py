"""Unit tests for the client and builder."""

import os
from unittest.mock import patch

import pytest

from allscreenshots_sdk import AllscreenshotsClient
from allscreenshots_sdk.client import AllscreenshotsClientBuilder


class TestAllscreenshotsClientBuilder:
    """Tests for AllscreenshotsClientBuilder."""

    def test_builder_creation(self) -> None:
        """Test creating a builder."""
        builder = AllscreenshotsClient.builder()
        assert isinstance(builder, AllscreenshotsClientBuilder)

    def test_with_api_key(self) -> None:
        """Test setting API key."""
        builder = AllscreenshotsClient.builder().with_api_key("test-key")
        assert builder._api_key == "test-key"

    def test_with_base_url(self) -> None:
        """Test setting base URL."""
        builder = AllscreenshotsClient.builder().with_base_url("https://custom.api.com")
        assert builder._base_url == "https://custom.api.com"

    def test_with_timeout(self) -> None:
        """Test setting timeout."""
        builder = AllscreenshotsClient.builder().with_timeout(120.0)
        assert builder._timeout == 120.0

    def test_with_max_retries(self) -> None:
        """Test setting max retries."""
        builder = AllscreenshotsClient.builder().with_max_retries(5)
        assert builder._max_retries == 5

    def test_with_retry_delay(self) -> None:
        """Test setting retry delay."""
        builder = AllscreenshotsClient.builder().with_retry_delay(2.0)
        assert builder._retry_delay == 2.0

    def test_with_max_retry_delay(self) -> None:
        """Test setting max retry delay."""
        builder = AllscreenshotsClient.builder().with_max_retry_delay(60.0)
        assert builder._max_retry_delay == 60.0

    def test_builder_chaining(self) -> None:
        """Test that builder methods can be chained."""
        builder = (
            AllscreenshotsClient.builder()
            .with_api_key("key")
            .with_base_url("https://api.example.com")
            .with_timeout(90.0)
            .with_max_retries(3)
        )
        assert builder._api_key == "key"
        assert builder._base_url == "https://api.example.com"
        assert builder._timeout == 90.0
        assert builder._max_retries == 3

    def test_build_with_api_key(self) -> None:
        """Test building client with explicit API key."""
        client = AllscreenshotsClient.builder().with_api_key("test-key").build()
        assert client is not None
        client.close()

    def test_build_with_env_api_key(self) -> None:
        """Test building client with API key from environment."""
        with patch.dict(os.environ, {"ALLSCREENSHOTS_API_KEY": "env-key"}):
            client = AllscreenshotsClient.builder().build()
            assert client is not None
            client.close()

    def test_build_without_api_key_raises(self) -> None:
        """Test that building without API key raises ValueError."""
        with patch.dict(os.environ, {}, clear=True):
            # Ensure env var is not set
            if "ALLSCREENSHOTS_API_KEY" in os.environ:
                del os.environ["ALLSCREENSHOTS_API_KEY"]

            with pytest.raises(ValueError) as exc_info:
                AllscreenshotsClient.builder().build()
            assert "API key is required" in str(exc_info.value)

    def test_build_async_client(self) -> None:
        """Test building async client."""
        client = AllscreenshotsClient.builder().with_api_key("test-key").build_async()
        assert client is not None
        # Use sync close for testing
        import asyncio

        asyncio.get_event_loop().run_until_complete(client.close())

    def test_build_async_without_api_key_raises(self) -> None:
        """Test that building async client without API key raises ValueError."""
        with patch.dict(os.environ, {}, clear=True):
            if "ALLSCREENSHOTS_API_KEY" in os.environ:
                del os.environ["ALLSCREENSHOTS_API_KEY"]

            with pytest.raises(ValueError) as exc_info:
                AllscreenshotsClient.builder().build_async()
            assert "API key is required" in str(exc_info.value)


class TestAllscreenshotsClient:
    """Tests for AllscreenshotsClient."""

    def test_client_has_all_apis(self) -> None:
        """Test that client exposes all API endpoints."""
        client = AllscreenshotsClient.builder().with_api_key("test-key").build()
        try:
            assert client.screenshots is not None
            assert client.bulk is not None
            assert client.compose is not None
            assert client.schedules is not None
            assert client.usage is not None
        finally:
            client.close()

    def test_client_context_manager(self) -> None:
        """Test using client as context manager."""
        with AllscreenshotsClient.builder().with_api_key("test-key").build() as client:
            assert client.screenshots is not None

    def test_builder_static_method(self) -> None:
        """Test that builder is a static method."""
        builder1 = AllscreenshotsClient.builder()
        builder2 = AllscreenshotsClient.builder()
        # They should be different instances
        assert builder1 is not builder2


class TestAsyncAllscreenshotsClient:
    """Tests for AsyncAllscreenshotsClient."""

    @pytest.mark.asyncio
    async def test_async_client_has_all_apis(self) -> None:
        """Test that async client exposes all API endpoints."""
        client = AllscreenshotsClient.builder().with_api_key("test-key").build_async()
        try:
            assert client.screenshots is not None
            assert client.bulk is not None
            assert client.compose is not None
            assert client.schedules is not None
            assert client.usage is not None
        finally:
            await client.close()

    @pytest.mark.asyncio
    async def test_async_client_context_manager(self) -> None:
        """Test using async client as context manager."""
        async with AllscreenshotsClient.builder().with_api_key("test-key").build_async() as client:
            assert client.screenshots is not None

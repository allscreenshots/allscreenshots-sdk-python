"""Unit tests for data models."""

import pytest
from pydantic import ValidationError

from allscreenshots_sdk.models import (
    BlockLevel,
    ImageFormat,
    JobResponse,
    JobStatus,
    ScreenshotRequest,
    ViewportConfig,
    WaitUntil,
)


class TestViewportConfig:
    """Tests for ViewportConfig model."""

    def test_valid_viewport(self) -> None:
        """Test creating a valid viewport configuration."""
        viewport = ViewportConfig(width=1920, height=1080, device_scale_factor=2)
        assert viewport.width == 1920
        assert viewport.height == 1080
        assert viewport.device_scale_factor == 2

    def test_viewport_serialization(self) -> None:
        """Test viewport serializes with correct field names."""
        viewport = ViewportConfig(width=1920, height=1080, device_scale_factor=2)
        data = viewport.model_dump(by_alias=True)
        assert data["width"] == 1920
        assert data["height"] == 1080
        assert data["deviceScaleFactor"] == 2

    def test_viewport_width_bounds(self) -> None:
        """Test viewport width validation bounds."""
        # Too small
        with pytest.raises(ValidationError):
            ViewportConfig(width=50)

        # Too large
        with pytest.raises(ValidationError):
            ViewportConfig(width=5000)

        # Valid bounds
        viewport = ViewportConfig(width=100)
        assert viewport.width == 100
        viewport = ViewportConfig(width=4096)
        assert viewport.width == 4096

    def test_viewport_height_bounds(self) -> None:
        """Test viewport height validation bounds."""
        with pytest.raises(ValidationError):
            ViewportConfig(height=50)
        with pytest.raises(ValidationError):
            ViewportConfig(height=5000)

    def test_device_scale_factor_bounds(self) -> None:
        """Test device scale factor validation bounds."""
        with pytest.raises(ValidationError):
            ViewportConfig(device_scale_factor=0)
        with pytest.raises(ValidationError):
            ViewportConfig(device_scale_factor=4)


class TestScreenshotRequest:
    """Tests for ScreenshotRequest model."""

    def test_minimal_request(self) -> None:
        """Test creating a minimal screenshot request."""
        request = ScreenshotRequest(url="https://example.com")
        assert request.url == "https://example.com"
        assert request.device is None
        assert request.full_page is None

    def test_full_request(self) -> None:
        """Test creating a full screenshot request with all options."""
        request = ScreenshotRequest(
            url="https://example.com",
            device="Desktop HD",
            full_page=True,
            format=ImageFormat.PNG,
            quality=80,
            delay=1000,
            wait_for=".main-content",
            wait_until=WaitUntil.NETWORKIDLE,
            timeout=30000,
            dark_mode=True,
            custom_css="body { background: red; }",
            hide_selectors=[".ad", ".popup"],
            selector=".main-content",
            block_ads=True,
            block_cookie_banners=True,
            block_level=BlockLevel.PRO,
            viewport=ViewportConfig(width=1920, height=1080),
        )
        assert request.device == "Desktop HD"
        assert request.full_page is True
        assert request.format == ImageFormat.PNG
        assert request.quality == 80

    def test_request_serialization(self) -> None:
        """Test request serializes with correct camelCase field names."""
        request = ScreenshotRequest(
            url="https://example.com",
            full_page=True,
            wait_for=".content",
            wait_until=WaitUntil.LOAD,
            dark_mode=True,
            custom_css="body {}",
            hide_selectors=[".ad"],
            block_ads=True,
            block_cookie_banners=True,
            block_level=BlockLevel.NORMAL,
            webhook_url="https://webhook.example.com",
            webhook_secret="secret123",
        )
        data = request.model_dump(by_alias=True, exclude_none=True)
        assert "fullPage" in data
        assert "waitFor" in data
        assert "waitUntil" in data
        assert "darkMode" in data
        assert "customCss" in data
        assert "hideSelectors" in data
        assert "blockAds" in data
        assert "blockCookieBanners" in data
        assert "blockLevel" in data
        assert "webhookUrl" in data
        assert "webhookSecret" in data

    def test_url_validation(self) -> None:
        """Test URL pattern validation."""
        # Valid URLs
        ScreenshotRequest(url="https://example.com")
        ScreenshotRequest(url="http://example.com")
        ScreenshotRequest(url="https://sub.example.com/path?query=1")

        # Invalid URLs
        with pytest.raises(ValidationError):
            ScreenshotRequest(url="not-a-url")
        with pytest.raises(ValidationError):
            ScreenshotRequest(url="ftp://example.com")
        with pytest.raises(ValidationError):
            ScreenshotRequest(url="example.com")

    def test_quality_bounds(self) -> None:
        """Test quality validation bounds."""
        with pytest.raises(ValidationError):
            ScreenshotRequest(url="https://example.com", quality=0)
        with pytest.raises(ValidationError):
            ScreenshotRequest(url="https://example.com", quality=101)

        request = ScreenshotRequest(url="https://example.com", quality=1)
        assert request.quality == 1
        request = ScreenshotRequest(url="https://example.com", quality=100)
        assert request.quality == 100

    def test_delay_bounds(self) -> None:
        """Test delay validation bounds."""
        with pytest.raises(ValidationError):
            ScreenshotRequest(url="https://example.com", delay=-1)
        with pytest.raises(ValidationError):
            ScreenshotRequest(url="https://example.com", delay=30001)

    def test_timeout_bounds(self) -> None:
        """Test timeout validation bounds."""
        with pytest.raises(ValidationError):
            ScreenshotRequest(url="https://example.com", timeout=999)
        with pytest.raises(ValidationError):
            ScreenshotRequest(url="https://example.com", timeout=60001)


class TestJobResponse:
    """Tests for JobResponse model."""

    def test_parse_job_response(self) -> None:
        """Test parsing a job response from JSON."""
        data = {
            "id": "job-123",
            "status": "COMPLETED",
            "url": "https://example.com",
            "resultUrl": "https://storage.example.com/result.png",
            "createdAt": "2024-01-15T10:30:00Z",
            "completedAt": "2024-01-15T10:30:05Z",
        }
        job = JobResponse.model_validate(data)
        assert job.id == "job-123"
        assert job.status == JobStatus.COMPLETED
        assert job.url == "https://example.com"
        assert job.result_url == "https://storage.example.com/result.png"

    def test_parse_failed_job(self) -> None:
        """Test parsing a failed job response."""
        data = {
            "id": "job-456",
            "status": "FAILED",
            "url": "https://example.com",
            "errorCode": "NAVIGATION_TIMEOUT",
            "errorMessage": "Page load timed out after 30 seconds",
        }
        job = JobResponse.model_validate(data)
        assert job.status == JobStatus.FAILED
        assert job.error_code == "NAVIGATION_TIMEOUT"
        assert job.error_message == "Page load timed out after 30 seconds"

    def test_job_status_enum(self) -> None:
        """Test all job status values."""
        for status in ["QUEUED", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED"]:
            data = {"id": "job-1", "status": status}
            job = JobResponse.model_validate(data)
            # use_enum_values=True means status is stored as string value
            assert job.status == status


class TestEnums:
    """Tests for enum models."""

    def test_image_format_values(self) -> None:
        """Test ImageFormat enum values."""
        assert ImageFormat.PNG.value == "png"
        assert ImageFormat.JPEG.value == "jpeg"
        assert ImageFormat.JPG.value == "jpg"
        assert ImageFormat.WEBP.value == "webp"
        assert ImageFormat.PDF.value == "pdf"

    def test_wait_until_values(self) -> None:
        """Test WaitUntil enum values."""
        assert WaitUntil.LOAD.value == "load"
        assert WaitUntil.DOMCONTENTLOADED.value == "domcontentloaded"
        assert WaitUntil.NETWORKIDLE.value == "networkidle"

    def test_block_level_values(self) -> None:
        """Test BlockLevel enum values."""
        assert BlockLevel.NONE.value == "none"
        assert BlockLevel.LIGHT.value == "light"
        assert BlockLevel.NORMAL.value == "normal"
        assert BlockLevel.PRO.value == "pro"
        assert BlockLevel.PRO_PLUS.value == "pro_plus"
        assert BlockLevel.ULTIMATE.value == "ultimate"

    def test_job_status_values(self) -> None:
        """Test JobStatus enum values."""
        assert JobStatus.QUEUED.value == "QUEUED"
        assert JobStatus.PROCESSING.value == "PROCESSING"
        assert JobStatus.COMPLETED.value == "COMPLETED"
        assert JobStatus.FAILED.value == "FAILED"
        assert JobStatus.CANCELLED.value == "CANCELLED"

"""
Screenshots API endpoints.

This module provides methods for capturing screenshots synchronously and asynchronously,
as well as managing screenshot jobs.
"""

from typing import TYPE_CHECKING

from allscreenshots_sdk.models import (
    AsyncJobCreatedResponse,
    JobResponse,
    ScreenshotRequest,
)

if TYPE_CHECKING:
    from allscreenshots_sdk.http_client import AsyncHttpClient, HttpClient


class ScreenshotsApi:
    """
    Synchronous API for screenshot operations.

    Example:
        >>> client = AllscreenshotsClient.builder().with_api_key("key").build()
        >>> # Capture a screenshot and get the image bytes
        >>> image_bytes = client.screenshots.capture("https://example.com")
        >>> with open("screenshot.png", "wb") as f:
        ...     f.write(image_bytes)
    """

    def __init__(self, http_client: "HttpClient") -> None:
        """
        Initialize the Screenshots API.

        Args:
            http_client: The HTTP client to use for requests.
        """
        self._http = http_client

    def capture(
        self,
        url: str,
        *,
        device: str | None = None,
        full_page: bool | None = None,
        format: str | None = None,
        quality: int | None = None,
        delay: int | None = None,
        wait_for: str | None = None,
        wait_until: str | None = None,
        timeout: int | None = None,
        dark_mode: bool | None = None,
        custom_css: str | None = None,
        hide_selectors: list[str] | None = None,
        selector: str | None = None,
        block_ads: bool | None = None,
        block_cookie_banners: bool | None = None,
        block_level: str | None = None,
        viewport_width: int | None = None,
        viewport_height: int | None = None,
        device_scale_factor: int | None = None,
    ) -> bytes:
        """
        Capture a screenshot synchronously and return the image bytes.

        Args:
            url: The URL to capture.
            device: Device preset name (e.g., 'Desktop HD', 'iPhone 14').
            full_page: Whether to capture the full page.
            format: Image format ('png', 'jpeg', 'webp', 'pdf').
            quality: Image quality (1-100, for jpeg/webp).
            delay: Delay before capture in milliseconds.
            wait_for: CSS selector to wait for before capture.
            wait_until: Page load condition ('load', 'domcontentloaded', 'networkidle').
            timeout: Request timeout in milliseconds.
            dark_mode: Whether to enable dark mode.
            custom_css: Custom CSS to inject.
            hide_selectors: List of CSS selectors to hide.
            selector: Specific element to capture.
            block_ads: Whether to block advertisements.
            block_cookie_banners: Whether to block cookie banners.
            block_level: Ad blocking level.
            viewport_width: Custom viewport width.
            viewport_height: Custom viewport height.
            device_scale_factor: Device scale factor (1-3).

        Returns:
            The screenshot image as bytes.

        Example:
            >>> image = client.screenshots.capture(
            ...     "https://github.com",
            ...     device="Desktop HD",
            ...     full_page=True,
            ... )
        """
        request = self._build_request(
            url=url,
            device=device,
            full_page=full_page,
            format=format,
            quality=quality,
            delay=delay,
            wait_for=wait_for,
            wait_until=wait_until,
            timeout=timeout,
            dark_mode=dark_mode,
            custom_css=custom_css,
            hide_selectors=hide_selectors,
            selector=selector,
            block_ads=block_ads,
            block_cookie_banners=block_cookie_banners,
            block_level=block_level,
            viewport_width=viewport_width,
            viewport_height=viewport_height,
            device_scale_factor=device_scale_factor,
        )

        response = self._http.post("/v1/screenshots", json=request.model_dump(by_alias=True, exclude_none=True))
        return response.content

    def capture_async(
        self,
        url: str,
        *,
        device: str | None = None,
        full_page: bool | None = None,
        format: str | None = None,
        quality: int | None = None,
        delay: int | None = None,
        wait_for: str | None = None,
        wait_until: str | None = None,
        timeout: int | None = None,
        dark_mode: bool | None = None,
        custom_css: str | None = None,
        hide_selectors: list[str] | None = None,
        selector: str | None = None,
        block_ads: bool | None = None,
        block_cookie_banners: bool | None = None,
        block_level: str | None = None,
        viewport_width: int | None = None,
        viewport_height: int | None = None,
        device_scale_factor: int | None = None,
        webhook_url: str | None = None,
        webhook_secret: str | None = None,
    ) -> AsyncJobCreatedResponse:
        """
        Start an async screenshot job.

        Args:
            url: The URL to capture.
            device: Device preset name.
            full_page: Whether to capture the full page.
            format: Image format.
            quality: Image quality (1-100).
            delay: Delay before capture in milliseconds.
            wait_for: CSS selector to wait for.
            wait_until: Page load condition.
            timeout: Request timeout in milliseconds.
            dark_mode: Whether to enable dark mode.
            custom_css: Custom CSS to inject.
            hide_selectors: Selectors to hide.
            selector: Element to capture.
            block_ads: Block advertisements.
            block_cookie_banners: Block cookie banners.
            block_level: Ad blocking level.
            viewport_width: Custom viewport width.
            viewport_height: Custom viewport height.
            device_scale_factor: Device scale factor.
            webhook_url: URL for webhook notification.
            webhook_secret: Secret for webhook verification.

        Returns:
            Job creation response with job ID and status URL.

        Example:
            >>> job = client.screenshots.capture_async("https://github.com")
            >>> print(f"Job ID: {job.id}")
        """
        request = self._build_request(
            url=url,
            device=device,
            full_page=full_page,
            format=format,
            quality=quality,
            delay=delay,
            wait_for=wait_for,
            wait_until=wait_until,
            timeout=timeout,
            dark_mode=dark_mode,
            custom_css=custom_css,
            hide_selectors=hide_selectors,
            selector=selector,
            block_ads=block_ads,
            block_cookie_banners=block_cookie_banners,
            block_level=block_level,
            viewport_width=viewport_width,
            viewport_height=viewport_height,
            device_scale_factor=device_scale_factor,
            webhook_url=webhook_url,
            webhook_secret=webhook_secret,
        )

        response = self._http.post(
            "/v1/screenshots/async",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )
        return AsyncJobCreatedResponse.model_validate(response.json())

    def list_jobs(self) -> list[JobResponse]:
        """
        List all screenshot jobs.

        Returns:
            List of job responses.

        Example:
            >>> jobs = client.screenshots.list_jobs()
            >>> for job in jobs:
            ...     print(f"{job.id}: {job.status}")
        """
        response = self._http.get("/v1/screenshots/jobs")
        return [JobResponse.model_validate(job) for job in response.json()]

    def get_job(self, job_id: str) -> JobResponse:
        """
        Get the status of a screenshot job.

        Args:
            job_id: The job ID.

        Returns:
            Job response with current status.

        Example:
            >>> job = client.screenshots.get_job("job-123")
            >>> if job.status == "COMPLETED":
            ...     result = client.screenshots.get_job_result("job-123")
        """
        response = self._http.get(f"/v1/screenshots/jobs/{job_id}")
        return JobResponse.model_validate(response.json())

    def get_job_result(self, job_id: str) -> bytes:
        """
        Download the result image of a completed job.

        Args:
            job_id: The job ID.

        Returns:
            The screenshot image as bytes.

        Example:
            >>> image = client.screenshots.get_job_result("job-123")
            >>> with open("result.png", "wb") as f:
            ...     f.write(image)
        """
        response = self._http.get(f"/v1/screenshots/jobs/{job_id}/result")
        return response.content

    def cancel_job(self, job_id: str) -> JobResponse:
        """
        Cancel a pending or processing job.

        Args:
            job_id: The job ID.

        Returns:
            Updated job response.

        Example:
            >>> job = client.screenshots.cancel_job("job-123")
            >>> print(f"Status: {job.status}")
        """
        response = self._http.post(f"/v1/screenshots/jobs/{job_id}/cancel")
        return JobResponse.model_validate(response.json())

    def _build_request(
        self,
        url: str,
        device: str | None = None,
        full_page: bool | None = None,
        format: str | None = None,
        quality: int | None = None,
        delay: int | None = None,
        wait_for: str | None = None,
        wait_until: str | None = None,
        timeout: int | None = None,
        dark_mode: bool | None = None,
        custom_css: str | None = None,
        hide_selectors: list[str] | None = None,
        selector: str | None = None,
        block_ads: bool | None = None,
        block_cookie_banners: bool | None = None,
        block_level: str | None = None,
        viewport_width: int | None = None,
        viewport_height: int | None = None,
        device_scale_factor: int | None = None,
        webhook_url: str | None = None,
        webhook_secret: str | None = None,
    ) -> ScreenshotRequest:
        """Build a ScreenshotRequest from individual parameters."""
        from allscreenshots_sdk.models import ViewportConfig

        viewport = None
        if viewport_width or viewport_height or device_scale_factor:
            viewport = ViewportConfig(
                width=viewport_width,
                height=viewport_height,
                device_scale_factor=device_scale_factor,
            )

        return ScreenshotRequest(
            url=url,
            device=device,
            full_page=full_page,
            format=format,
            quality=quality,
            delay=delay,
            wait_for=wait_for,
            wait_until=wait_until,
            timeout=timeout,
            dark_mode=dark_mode,
            custom_css=custom_css,
            hide_selectors=hide_selectors,
            selector=selector,
            block_ads=block_ads,
            block_cookie_banners=block_cookie_banners,
            block_level=block_level,
            viewport=viewport,
            webhook_url=webhook_url,
            webhook_secret=webhook_secret,
        )


class AsyncScreenshotsApi:
    """
    Asynchronous API for screenshot operations.

    Example:
        >>> async with AllscreenshotsClient.builder().with_api_key("key").build_async() as client:
        ...     image_bytes = await client.screenshots.capture("https://example.com")
    """

    def __init__(self, http_client: "AsyncHttpClient") -> None:
        """
        Initialize the async Screenshots API.

        Args:
            http_client: The async HTTP client to use for requests.
        """
        self._http = http_client

    async def capture(
        self,
        url: str,
        *,
        device: str | None = None,
        full_page: bool | None = None,
        format: str | None = None,
        quality: int | None = None,
        delay: int | None = None,
        wait_for: str | None = None,
        wait_until: str | None = None,
        timeout: int | None = None,
        dark_mode: bool | None = None,
        custom_css: str | None = None,
        hide_selectors: list[str] | None = None,
        selector: str | None = None,
        block_ads: bool | None = None,
        block_cookie_banners: bool | None = None,
        block_level: str | None = None,
        viewport_width: int | None = None,
        viewport_height: int | None = None,
        device_scale_factor: int | None = None,
    ) -> bytes:
        """Capture a screenshot asynchronously and return the image bytes."""
        request = self._build_request(
            url=url,
            device=device,
            full_page=full_page,
            format=format,
            quality=quality,
            delay=delay,
            wait_for=wait_for,
            wait_until=wait_until,
            timeout=timeout,
            dark_mode=dark_mode,
            custom_css=custom_css,
            hide_selectors=hide_selectors,
            selector=selector,
            block_ads=block_ads,
            block_cookie_banners=block_cookie_banners,
            block_level=block_level,
            viewport_width=viewport_width,
            viewport_height=viewport_height,
            device_scale_factor=device_scale_factor,
        )

        response = await self._http.post(
            "/v1/screenshots",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )
        return response.content

    async def capture_async(
        self,
        url: str,
        *,
        device: str | None = None,
        full_page: bool | None = None,
        format: str | None = None,
        quality: int | None = None,
        delay: int | None = None,
        wait_for: str | None = None,
        wait_until: str | None = None,
        timeout: int | None = None,
        dark_mode: bool | None = None,
        custom_css: str | None = None,
        hide_selectors: list[str] | None = None,
        selector: str | None = None,
        block_ads: bool | None = None,
        block_cookie_banners: bool | None = None,
        block_level: str | None = None,
        viewport_width: int | None = None,
        viewport_height: int | None = None,
        device_scale_factor: int | None = None,
        webhook_url: str | None = None,
        webhook_secret: str | None = None,
    ) -> AsyncJobCreatedResponse:
        """Start an async screenshot job."""
        request = self._build_request(
            url=url,
            device=device,
            full_page=full_page,
            format=format,
            quality=quality,
            delay=delay,
            wait_for=wait_for,
            wait_until=wait_until,
            timeout=timeout,
            dark_mode=dark_mode,
            custom_css=custom_css,
            hide_selectors=hide_selectors,
            selector=selector,
            block_ads=block_ads,
            block_cookie_banners=block_cookie_banners,
            block_level=block_level,
            viewport_width=viewport_width,
            viewport_height=viewport_height,
            device_scale_factor=device_scale_factor,
            webhook_url=webhook_url,
            webhook_secret=webhook_secret,
        )

        response = await self._http.post(
            "/v1/screenshots/async",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )
        return AsyncJobCreatedResponse.model_validate(response.json())

    async def list_jobs(self) -> list[JobResponse]:
        """List all screenshot jobs."""
        response = await self._http.get("/v1/screenshots/jobs")
        return [JobResponse.model_validate(job) for job in response.json()]

    async def get_job(self, job_id: str) -> JobResponse:
        """Get the status of a screenshot job."""
        response = await self._http.get(f"/v1/screenshots/jobs/{job_id}")
        return JobResponse.model_validate(response.json())

    async def get_job_result(self, job_id: str) -> bytes:
        """Download the result image of a completed job."""
        response = await self._http.get(f"/v1/screenshots/jobs/{job_id}/result")
        return response.content

    async def cancel_job(self, job_id: str) -> JobResponse:
        """Cancel a pending or processing job."""
        response = await self._http.post(f"/v1/screenshots/jobs/{job_id}/cancel")
        return JobResponse.model_validate(response.json())

    def _build_request(
        self,
        url: str,
        device: str | None = None,
        full_page: bool | None = None,
        format: str | None = None,
        quality: int | None = None,
        delay: int | None = None,
        wait_for: str | None = None,
        wait_until: str | None = None,
        timeout: int | None = None,
        dark_mode: bool | None = None,
        custom_css: str | None = None,
        hide_selectors: list[str] | None = None,
        selector: str | None = None,
        block_ads: bool | None = None,
        block_cookie_banners: bool | None = None,
        block_level: str | None = None,
        viewport_width: int | None = None,
        viewport_height: int | None = None,
        device_scale_factor: int | None = None,
        webhook_url: str | None = None,
        webhook_secret: str | None = None,
    ) -> ScreenshotRequest:
        """Build a ScreenshotRequest from individual parameters."""
        from allscreenshots_sdk.models import ViewportConfig

        viewport = None
        if viewport_width or viewport_height or device_scale_factor:
            viewport = ViewportConfig(
                width=viewport_width,
                height=viewport_height,
                device_scale_factor=device_scale_factor,
            )

        return ScreenshotRequest(
            url=url,
            device=device,
            full_page=full_page,
            format=format,
            quality=quality,
            delay=delay,
            wait_for=wait_for,
            wait_until=wait_until,
            timeout=timeout,
            dark_mode=dark_mode,
            custom_css=custom_css,
            hide_selectors=hide_selectors,
            selector=selector,
            block_ads=block_ads,
            block_cookie_banners=block_cookie_banners,
            block_level=block_level,
            viewport=viewport,
            webhook_url=webhook_url,
            webhook_secret=webhook_secret,
        )

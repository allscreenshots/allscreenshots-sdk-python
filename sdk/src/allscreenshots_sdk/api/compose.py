"""
Compose API endpoints.

This module provides methods for composing multiple screenshots into a single image.
"""

from typing import TYPE_CHECKING, Any

from allscreenshots_sdk.models import (
    CaptureDefaults,
    CaptureItem,
    ComposeJobStatusResponse,
    ComposeJobSummaryResponse,
    ComposeOutputConfig,
    ComposeRequest,
    ComposeResponse,
    LayoutPreviewResponse,
    VariantConfig,
)

if TYPE_CHECKING:
    from allscreenshots_sdk.http_client import AsyncHttpClient, HttpClient


class ComposeApi:
    """
    Synchronous API for compose operations.

    Compose allows you to capture multiple screenshots and combine them into a single
    image with various layout options.

    Example:
        >>> client = AllscreenshotsClient.builder().with_api_key("key").build()
        >>> result = client.compose.create([
        ...     CaptureItem(url="https://example.com"),
        ...     CaptureItem(url="https://github.com"),
        ... ])
        >>> print(f"Composed image: {result.url}")
    """

    def __init__(self, http_client: "HttpClient") -> None:
        """
        Initialize the Compose API.

        Args:
            http_client: The HTTP client to use for requests.
        """
        self._http = http_client

    def create(
        self,
        captures: list[CaptureItem] | None = None,
        *,
        url: str | None = None,
        variants: list[VariantConfig] | None = None,
        defaults: CaptureDefaults | None = None,
        output: ComposeOutputConfig | None = None,
        async_mode: bool = False,
        webhook_url: str | None = None,
        webhook_secret: str | None = None,
    ) -> ComposeResponse | ComposeJobStatusResponse:
        """
        Create a composed screenshot.

        You can either provide multiple URLs via `captures`, or a single URL with
        multiple `variants` (different device/viewport configurations).

        Args:
            captures: List of URLs to capture and compose.
            url: Single URL to capture with variants.
            variants: Different configurations for a single URL.
            defaults: Default capture options.
            output: Output configuration (layout, format, etc.).
            async_mode: Whether to run asynchronously.
            webhook_url: Webhook URL for notification.
            webhook_secret: Webhook secret for verification.

        Returns:
            ComposeResponse for sync mode, ComposeJobStatusResponse for async mode.

        Example:
            >>> # Multiple URLs
            >>> result = client.compose.create([
            ...     CaptureItem(url="https://example.com", label="Example"),
            ...     CaptureItem(url="https://github.com", label="GitHub"),
            ... ], output=ComposeOutputConfig(layout="GRID", columns=2))
            >>>
            >>> # Single URL with variants
            >>> result = client.compose.create(
            ...     url="https://example.com",
            ...     variants=[
            ...         VariantConfig(device="Desktop HD", label="Desktop"),
            ...         VariantConfig(device="iPhone 14", label="Mobile"),
            ...     ]
            ... )
        """
        request = ComposeRequest(
            captures=captures,
            url=url,
            variants=variants,
            defaults=defaults,
            output=output,
            async_=async_mode,
            webhook_url=webhook_url,
            webhook_secret=webhook_secret,
        )

        response = self._http.post(
            "/v1/screenshots/compose",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )

        data = response.json()
        if async_mode or "jobId" in data:
            return ComposeJobStatusResponse.model_validate(data)
        return ComposeResponse.model_validate(data)

    def preview_layout(
        self,
        layout: str,
        image_count: int,
        canvas_width: int | None = None,
        canvas_height: int | None = None,
        aspect_ratios: list[float] | None = None,
    ) -> LayoutPreviewResponse:
        """
        Preview how images will be placed in a layout.

        Args:
            layout: Layout type (GRID, HORIZONTAL, VERTICAL, etc.).
            image_count: Number of images.
            canvas_width: Canvas width in pixels.
            canvas_height: Canvas height in pixels.
            aspect_ratios: Aspect ratios of images.

        Returns:
            Layout preview with placement information.

        Example:
            >>> preview = client.compose.preview_layout(
            ...     layout="GRID",
            ...     image_count=4,
            ...     canvas_width=1920,
            ...     canvas_height=1080,
            ... )
            >>> for placement in preview.placements:
            ...     print(f"Image {placement.index}: ({placement.x}, {placement.y})")
        """
        params: dict[str, Any] = {
            "layout": layout,
            "image_count": image_count,
        }
        if canvas_width is not None:
            params["canvas_width"] = canvas_width
        if canvas_height is not None:
            params["canvas_height"] = canvas_height
        if aspect_ratios is not None:
            params["aspect_ratios"] = ",".join(str(r) for r in aspect_ratios)

        response = self._http.get("/v1/screenshots/compose/preview", params=params)
        return LayoutPreviewResponse.model_validate(response.json())

    def list_jobs(self) -> list[ComposeJobSummaryResponse]:
        """
        List all compose jobs.

        Returns:
            List of compose job summaries.

        Example:
            >>> jobs = client.compose.list_jobs()
            >>> for job in jobs:
            ...     print(f"{job.job_id}: {job.status}")
        """
        response = self._http.get("/v1/screenshots/compose/jobs")
        return [ComposeJobSummaryResponse.model_validate(job) for job in response.json()]

    def get_job(self, job_id: str) -> ComposeJobStatusResponse:
        """
        Get status of a compose job.

        Args:
            job_id: The compose job ID.

        Returns:
            Job status with result if completed.

        Example:
            >>> job = client.compose.get_job("compose-123")
            >>> if job.status == "COMPLETED":
            ...     print(f"Result: {job.result.url}")
        """
        response = self._http.get(f"/v1/screenshots/compose/jobs/{job_id}")
        return ComposeJobStatusResponse.model_validate(response.json())


class AsyncComposeApi:
    """
    Asynchronous API for compose operations.

    Example:
        >>> async with AllscreenshotsClient.builder().with_api_key("key").build_async() as client:
        ...     result = await client.compose.create([
        ...         CaptureItem(url="https://example.com"),
        ...     ])
    """

    def __init__(self, http_client: "AsyncHttpClient") -> None:
        """
        Initialize the async Compose API.

        Args:
            http_client: The async HTTP client to use for requests.
        """
        self._http = http_client

    async def create(
        self,
        captures: list[CaptureItem] | None = None,
        *,
        url: str | None = None,
        variants: list[VariantConfig] | None = None,
        defaults: CaptureDefaults | None = None,
        output: ComposeOutputConfig | None = None,
        async_mode: bool = False,
        webhook_url: str | None = None,
        webhook_secret: str | None = None,
    ) -> ComposeResponse | ComposeJobStatusResponse:
        """Create a composed screenshot."""
        request = ComposeRequest(
            captures=captures,
            url=url,
            variants=variants,
            defaults=defaults,
            output=output,
            async_=async_mode,
            webhook_url=webhook_url,
            webhook_secret=webhook_secret,
        )

        response = await self._http.post(
            "/v1/screenshots/compose",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )

        data = response.json()
        if async_mode or "jobId" in data:
            return ComposeJobStatusResponse.model_validate(data)
        return ComposeResponse.model_validate(data)

    async def preview_layout(
        self,
        layout: str,
        image_count: int,
        canvas_width: int | None = None,
        canvas_height: int | None = None,
        aspect_ratios: list[float] | None = None,
    ) -> LayoutPreviewResponse:
        """Preview how images will be placed in a layout."""
        params: dict[str, Any] = {
            "layout": layout,
            "image_count": image_count,
        }
        if canvas_width is not None:
            params["canvas_width"] = canvas_width
        if canvas_height is not None:
            params["canvas_height"] = canvas_height
        if aspect_ratios is not None:
            params["aspect_ratios"] = ",".join(str(r) for r in aspect_ratios)

        response = await self._http.get("/v1/screenshots/compose/preview", params=params)
        return LayoutPreviewResponse.model_validate(response.json())

    async def list_jobs(self) -> list[ComposeJobSummaryResponse]:
        """List all compose jobs."""
        response = await self._http.get("/v1/screenshots/compose/jobs")
        return [ComposeJobSummaryResponse.model_validate(job) for job in response.json()]

    async def get_job(self, job_id: str) -> ComposeJobStatusResponse:
        """Get status of a compose job."""
        response = await self._http.get(f"/v1/screenshots/compose/jobs/{job_id}")
        return ComposeJobStatusResponse.model_validate(response.json())

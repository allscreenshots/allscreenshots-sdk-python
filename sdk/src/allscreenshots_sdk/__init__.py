"""
Allscreenshots SDK - Python client for the Allscreenshots API.

This SDK provides a simple and intuitive interface for capturing screenshots
of web pages using the Allscreenshots service.

Example:
    >>> from allscreenshots_sdk import AllscreenshotsClient
    >>> client = AllscreenshotsClient.builder().with_api_key("your-api-key").build()
    >>> image_bytes = client.screenshots.capture("https://example.com")
"""

from allscreenshots_sdk.client import AllscreenshotsClient, AllscreenshotsClientBuilder
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
from allscreenshots_sdk.models import (
    AsyncJobCreatedResponse,
    BandwidthQuotaResponse,
    BulkDefaults,
    BulkJobDetailInfo,
    BulkJobSummary,
    BulkRequest,
    BulkResponse,
    BulkStatusResponse,
    BulkUrlOptions,
    BulkUrlRequest,
    CaptureDefaults,
    CaptureItem,
    ComposeJobStatusResponse,
    ComposeJobSummaryResponse,
    ComposeOutputConfig,
    ComposeRequest,
    ComposeResponse,
    CreateScheduleRequest,
    JobResponse,
    JobStatus,
    LayoutPreviewResponse,
    PeriodUsageResponse,
    PlacementPreview,
    QuotaDetailResponse,
    QuotaStatusResponse,
    ScheduleExecutionResponse,
    ScheduleHistoryResponse,
    ScheduleListResponse,
    ScheduleResponse,
    ScheduleScreenshotOptions,
    ScreenshotRequest,
    TotalsResponse,
    UpdateScheduleRequest,
    UsageResponse,
    VariantConfig,
    ViewportConfig,
)

__version__ = "1.0.0"

__all__ = [
    # Client
    "AllscreenshotsClient",
    "AllscreenshotsClientBuilder",
    # Exceptions
    "AllscreenshotsError",
    "ApiError",
    "AuthenticationError",
    "NotFoundError",
    "RateLimitError",
    "ServerError",
    "TimeoutError",
    "ValidationError",
    # Models
    "AsyncJobCreatedResponse",
    "BandwidthQuotaResponse",
    "BulkDefaults",
    "BulkJobDetailInfo",
    "BulkJobSummary",
    "BulkRequest",
    "BulkResponse",
    "BulkStatusResponse",
    "BulkUrlOptions",
    "BulkUrlRequest",
    "CaptureDefaults",
    "CaptureItem",
    "ComposeJobStatusResponse",
    "ComposeJobSummaryResponse",
    "ComposeOutputConfig",
    "ComposeRequest",
    "ComposeResponse",
    "CreateScheduleRequest",
    "JobResponse",
    "JobStatus",
    "LayoutPreviewResponse",
    "PeriodUsageResponse",
    "PlacementPreview",
    "QuotaDetailResponse",
    "QuotaStatusResponse",
    "ScheduleExecutionResponse",
    "ScheduleHistoryResponse",
    "ScheduleListResponse",
    "ScheduleResponse",
    "ScheduleScreenshotOptions",
    "ScreenshotRequest",
    "TotalsResponse",
    "UpdateScheduleRequest",
    "UsageResponse",
    "VariantConfig",
    "ViewportConfig",
]

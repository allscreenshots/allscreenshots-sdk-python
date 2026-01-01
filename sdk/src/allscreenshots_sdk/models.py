"""
Data models for the Allscreenshots API.

All models use Pydantic for validation and serialization. Field names match
the API specification exactly (camelCase for JSON serialization).
"""

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class JobStatus(str, Enum):
    """Status of a screenshot job."""

    QUEUED = "QUEUED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class ImageFormat(str, Enum):
    """Supported image formats."""

    PNG = "png"
    JPEG = "jpeg"
    JPG = "jpg"
    WEBP = "webp"
    PDF = "pdf"


class WaitUntil(str, Enum):
    """Page load wait conditions."""

    LOAD = "load"
    DOMCONTENTLOADED = "domcontentloaded"
    NETWORKIDLE = "networkidle"
    COMMIT = "commit"


class BlockLevel(str, Enum):
    """Ad blocking levels."""

    NONE = "none"
    LIGHT = "light"
    NORMAL = "normal"
    PRO = "pro"
    PRO_PLUS = "pro_plus"
    ULTIMATE = "ultimate"


class ResponseType(str, Enum):
    """Response type for screenshot requests."""

    BINARY = "BINARY"
    JSON = "JSON"


class Layout(str, Enum):
    """Layout options for compose requests."""

    GRID = "GRID"
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"
    MASONRY = "MASONRY"
    MONDRIAN = "MONDRIAN"
    PARTITIONING = "PARTITIONING"
    AUTO = "AUTO"


class Alignment(str, Enum):
    """Alignment options for compose layouts."""

    TOP = "top"
    CENTER = "center"
    BOTTOM = "bottom"


class BaseApiModel(BaseModel):
    """Base model with common configuration for API models."""

    model_config = ConfigDict(
        populate_by_name=True,
        use_enum_values=True,
    )


class ViewportConfig(BaseApiModel):
    """Viewport configuration for screenshots."""

    width: int | None = Field(None, ge=100, le=4096, description="Viewport width in pixels")
    height: int | None = Field(None, ge=100, le=4096, description="Viewport height in pixels")
    device_scale_factor: int | None = Field(
        None,
        ge=1,
        le=3,
        alias="deviceScaleFactor",
        description="Device scale factor (1-3)",
    )


class ScreenshotRequest(BaseApiModel):
    """Request parameters for taking a screenshot."""

    url: str = Field(..., pattern=r"^https?://.*", description="URL to capture")
    viewport: ViewportConfig | None = Field(None, description="Custom viewport configuration")
    device: str | None = Field(None, description="Device preset name (e.g., 'Desktop HD')")
    format: ImageFormat | None = Field(None, description="Output image format")
    full_page: bool | None = Field(None, alias="fullPage", description="Capture full page")
    quality: int | None = Field(None, ge=1, le=100, description="Image quality (1-100)")
    delay: int | None = Field(None, ge=0, le=30000, description="Delay before capture in ms")
    wait_for: str | None = Field(None, alias="waitFor", description="CSS selector to wait for")
    wait_until: WaitUntil | None = Field(
        None, alias="waitUntil", description="Page load condition"
    )
    timeout: int | None = Field(None, ge=1000, le=60000, description="Request timeout in ms")
    dark_mode: bool | None = Field(None, alias="darkMode", description="Enable dark mode")
    custom_css: str | None = Field(
        None, alias="customCss", max_length=10000, description="Custom CSS to inject"
    )
    hide_selectors: list[str] | None = Field(
        None, alias="hideSelectors", max_length=50, description="Selectors to hide"
    )
    selector: str | None = Field(
        None, max_length=500, description="Specific element to capture"
    )
    block_ads: bool | None = Field(None, alias="blockAds", description="Block advertisements")
    block_cookie_banners: bool | None = Field(
        None, alias="blockCookieBanners", description="Block cookie consent banners"
    )
    block_level: BlockLevel | None = Field(
        None, alias="blockLevel", description="Ad blocking level"
    )
    webhook_url: str | None = Field(
        None, alias="webhookUrl", pattern=r"^https?://.*", description="Webhook URL for callbacks"
    )
    webhook_secret: str | None = Field(
        None, alias="webhookSecret", max_length=255, description="Webhook secret for verification"
    )
    response_type: ResponseType | None = Field(
        None, alias="responseType", description="Response type (BINARY or JSON)"
    )


class JobResponse(BaseApiModel):
    """Response containing job status and details."""

    id: str = Field(..., description="Job ID")
    status: JobStatus = Field(..., description="Current job status")
    url: str | None = Field(None, description="Original URL")
    result_url: str | None = Field(None, alias="resultUrl", description="URL to download result")
    error_code: str | None = Field(None, alias="errorCode", description="Error code if failed")
    error_message: str | None = Field(
        None, alias="errorMessage", description="Error message if failed"
    )
    created_at: datetime | None = Field(None, alias="createdAt", description="Job creation time")
    started_at: datetime | None = Field(None, alias="startedAt", description="Job start time")
    completed_at: datetime | None = Field(
        None, alias="completedAt", description="Job completion time"
    )
    expires_at: datetime | None = Field(None, alias="expiresAt", description="Result expiration")
    metadata: dict[str, Any] | None = Field(None, description="Additional metadata")


class AsyncJobCreatedResponse(BaseApiModel):
    """Response when an async job is created."""

    id: str = Field(..., description="Job ID")
    status: JobStatus = Field(..., description="Initial job status")
    status_url: str | None = Field(None, alias="statusUrl", description="URL to check status")
    created_at: datetime | None = Field(None, alias="createdAt", description="Job creation time")


class BulkUrlOptions(BaseApiModel):
    """Options for individual URLs in a bulk request."""

    viewport: ViewportConfig | None = None
    device: str | None = None
    format: ImageFormat | None = None
    full_page: bool | None = Field(None, alias="fullPage")
    quality: int | None = Field(None, ge=1, le=100)
    delay: int | None = Field(None, ge=0, le=30000)
    wait_for: str | None = Field(None, alias="waitFor")
    wait_until: WaitUntil | None = Field(None, alias="waitUntil")
    timeout: int | None = Field(None, ge=1000, le=60000)
    dark_mode: bool | None = Field(None, alias="darkMode")
    custom_css: str | None = Field(None, alias="customCss")
    block_ads: bool | None = Field(None, alias="blockAds")
    block_cookie_banners: bool | None = Field(None, alias="blockCookieBanners")
    block_level: BlockLevel | None = Field(None, alias="blockLevel")


class BulkUrlRequest(BaseApiModel):
    """Individual URL request within a bulk operation."""

    url: str = Field(..., pattern=r"^https?://.*", description="URL to capture")
    options: BulkUrlOptions | None = Field(None, description="URL-specific options")


class BulkDefaults(BaseApiModel):
    """Default options applied to all URLs in a bulk request."""

    viewport: ViewportConfig | None = None
    device: str | None = None
    format: ImageFormat | None = None
    full_page: bool | None = Field(None, alias="fullPage")
    quality: int | None = Field(None, ge=1, le=100)
    delay: int | None = Field(None, ge=0, le=30000)
    wait_for: str | None = Field(None, alias="waitFor")
    wait_until: WaitUntil | None = Field(None, alias="waitUntil")
    timeout: int | None = Field(None, ge=1000, le=60000)
    dark_mode: bool | None = Field(None, alias="darkMode")
    custom_css: str | None = Field(None, alias="customCss")
    block_ads: bool | None = Field(None, alias="blockAds")
    block_cookie_banners: bool | None = Field(None, alias="blockCookieBanners")
    block_level: BlockLevel | None = Field(None, alias="blockLevel")


class BulkRequest(BaseApiModel):
    """Request for bulk screenshot operations."""

    urls: list[BulkUrlRequest] = Field(..., max_length=100, description="URLs to capture")
    defaults: BulkDefaults | None = Field(None, description="Default options for all URLs")
    webhook_url: str | None = Field(None, alias="webhookUrl", description="Webhook URL")
    webhook_secret: str | None = Field(None, alias="webhookSecret", description="Webhook secret")


class BulkJobInfo(BaseApiModel):
    """Basic job info within a bulk response."""

    id: str
    url: str
    status: str


class BulkResponse(BaseApiModel):
    """Response from creating a bulk screenshot job."""

    id: str = Field(..., description="Bulk job ID")
    status: str = Field(..., description="Overall status")
    total_jobs: int = Field(..., alias="totalJobs", description="Total number of jobs")
    completed_jobs: int = Field(0, alias="completedJobs", description="Completed jobs count")
    failed_jobs: int = Field(0, alias="failedJobs", description="Failed jobs count")
    progress: int = Field(0, ge=0, le=100, description="Progress percentage")
    jobs: list[BulkJobInfo] | None = Field(None, description="Individual job details")
    created_at: datetime | None = Field(None, alias="createdAt")
    completed_at: datetime | None = Field(None, alias="completedAt")


class BulkJobSummary(BaseApiModel):
    """Summary of a bulk job."""

    id: str
    status: str
    total_jobs: int = Field(..., alias="totalJobs")
    completed_jobs: int = Field(0, alias="completedJobs")
    failed_jobs: int = Field(0, alias="failedJobs")
    progress: int = Field(0)
    created_at: datetime | None = Field(None, alias="createdAt")
    completed_at: datetime | None = Field(None, alias="completedAt")


class BulkJobDetailInfo(BaseApiModel):
    """Detailed info for a job within a bulk operation."""

    id: str
    url: str
    status: str
    result_url: str | None = Field(None, alias="resultUrl")
    storage_url: str | None = Field(None, alias="storageUrl")
    format: str | None = None
    width: int | None = None
    height: int | None = None
    file_size: int | None = Field(None, alias="fileSize")
    render_time_ms: int | None = Field(None, alias="renderTimeMs")
    error_code: str | None = Field(None, alias="errorCode")
    error_message: str | None = Field(None, alias="errorMessage")
    created_at: datetime | None = Field(None, alias="createdAt")
    completed_at: datetime | None = Field(None, alias="completedAt")


class BulkStatusResponse(BaseApiModel):
    """Detailed status response for a bulk job."""

    id: str
    status: str
    total_jobs: int = Field(..., alias="totalJobs")
    completed_jobs: int = Field(0, alias="completedJobs")
    failed_jobs: int = Field(0, alias="failedJobs")
    progress: int = Field(0)
    jobs: list[BulkJobDetailInfo] | None = None
    created_at: datetime | None = Field(None, alias="createdAt")
    completed_at: datetime | None = Field(None, alias="completedAt")


class CaptureItem(BaseApiModel):
    """Individual capture item for compose requests."""

    url: str = Field(..., pattern=r"^https?://.*", description="URL to capture")
    id: str | None = Field(None, description="Optional identifier")
    label: str | None = Field(None, description="Label for the capture")
    viewport: ViewportConfig | None = None
    device: str | None = None
    full_page: bool | None = Field(None, alias="fullPage")
    dark_mode: bool | None = Field(None, alias="darkMode")
    delay: int | None = Field(None, ge=0, le=30000)


class VariantConfig(BaseApiModel):
    """Configuration for a variant in compose requests."""

    id: str | None = None
    label: str | None = None
    viewport: ViewportConfig | None = None
    device: str | None = None
    full_page: bool | None = Field(None, alias="fullPage")
    dark_mode: bool | None = Field(None, alias="darkMode")
    delay: int | None = Field(None, ge=0, le=30000)
    custom_css: str | None = Field(None, alias="customCss")


class CaptureDefaults(BaseApiModel):
    """Default capture settings for compose requests."""

    viewport: ViewportConfig | None = None
    device: str | None = None
    format: str | None = None
    full_page: bool | None = Field(None, alias="fullPage")
    quality: int | None = Field(None, ge=1, le=100)
    delay: int | None = Field(None, ge=0, le=30000)
    wait_for: str | None = Field(None, alias="waitFor")
    wait_until: str | None = Field(None, alias="waitUntil")
    timeout: int | None = Field(None, ge=1000, le=60000)
    dark_mode: bool | None = Field(None, alias="darkMode")
    custom_css: str | None = Field(None, alias="customCss")
    hide_selectors: list[str] | None = Field(None, alias="hideSelectors")
    block_ads: bool | None = Field(None, alias="blockAds")
    block_cookie_banners: bool | None = Field(None, alias="blockCookieBanners")
    block_level: str | None = Field(None, alias="blockLevel")


class LabelConfig(BaseApiModel):
    """Label configuration for compose output."""

    enabled: bool | None = None
    position: str | None = None
    font_size: int | None = Field(None, alias="fontSize")
    font_color: str | None = Field(None, alias="fontColor")
    background_color: str | None = Field(None, alias="backgroundColor")
    padding: int | None = None


class BorderConfig(BaseApiModel):
    """Border configuration for compose output."""

    enabled: bool | None = None
    width: int | None = None
    color: str | None = None
    radius: int | None = None


class ShadowConfig(BaseApiModel):
    """Shadow configuration for compose output."""

    enabled: bool | None = None
    color: str | None = None
    blur: int | None = None
    offset_x: int | None = Field(None, alias="offsetX")
    offset_y: int | None = Field(None, alias="offsetY")


class ComposeOutputConfig(BaseApiModel):
    """Output configuration for compose requests."""

    layout: Layout | None = None
    format: ImageFormat | None = None
    quality: int | None = Field(None, ge=1, le=100)
    columns: int | None = Field(None, ge=1, le=10)
    spacing: int | None = Field(None, ge=0, le=100)
    padding: int | None = Field(None, ge=0, le=100)
    background: str | None = None
    alignment: Alignment | None = None
    max_width: int | None = Field(None, alias="maxWidth", ge=100, le=10000)
    max_height: int | None = Field(None, alias="maxHeight", ge=100, le=10000)
    thumbnail_width: int | None = Field(None, alias="thumbnailWidth", ge=50, le=2000)
    labels: LabelConfig | None = None
    border: BorderConfig | None = None
    shadow: ShadowConfig | None = None


class ComposeRequest(BaseApiModel):
    """Request for composing multiple screenshots."""

    captures: list[CaptureItem] | None = Field(None, max_length=20, description="URLs to capture")
    url: str | None = Field(None, description="Single URL (use with variants)")
    variants: list[VariantConfig] | None = Field(
        None, max_length=20, description="Variants for single URL"
    )
    defaults: CaptureDefaults | None = None
    output: ComposeOutputConfig | None = None
    async_: bool | None = Field(None, alias="async", description="Run asynchronously")
    webhook_url: str | None = Field(None, alias="webhookUrl")
    webhook_secret: str | None = Field(None, alias="webhookSecret")
    captures_mode: bool | None = Field(None, alias="capturesMode")
    variants_mode: bool | None = Field(None, alias="variantsMode")


class ComposeMetadata(BaseApiModel):
    """Metadata for a compose response."""

    captures_count: int | None = Field(None, alias="capturesCount")
    layout_algorithm: str | None = Field(None, alias="layoutAlgorithm")


class ComposeResponse(BaseApiModel):
    """Response from a synchronous compose request."""

    url: str | None = None
    storage_url: str | None = Field(None, alias="storageUrl")
    expires_at: datetime | None = Field(None, alias="expiresAt")
    width: int | None = None
    height: int | None = None
    format: str | None = None
    file_size: int | None = Field(None, alias="fileSize")
    render_time_ms: int | None = Field(None, alias="renderTimeMs")
    layout: str | None = None
    metadata: ComposeMetadata | None = None


class ComposeJobStatusResponse(BaseApiModel):
    """Status response for an async compose job."""

    job_id: str = Field(..., alias="jobId")
    status: str
    progress: int | None = Field(None, ge=0, le=100)
    total_captures: int | None = Field(None, alias="totalCaptures")
    completed_captures: int | None = Field(None, alias="completedCaptures")
    result: ComposeResponse | None = None
    error_code: str | None = Field(None, alias="errorCode")
    error_message: str | None = Field(None, alias="errorMessage")
    created_at: datetime | None = Field(None, alias="createdAt")
    completed_at: datetime | None = Field(None, alias="completedAt")


class ComposeJobSummaryResponse(BaseApiModel):
    """Summary of a compose job."""

    job_id: str = Field(..., alias="jobId")
    status: str
    total_captures: int | None = Field(None, alias="totalCaptures")
    completed_captures: int | None = Field(None, alias="completedCaptures")
    failed_captures: int | None = Field(None, alias="failedCaptures")
    progress: int | None = Field(None, ge=0, le=100)
    layout_type: str | None = Field(None, alias="layoutType")
    created_at: datetime | None = Field(None, alias="createdAt")
    completed_at: datetime | None = Field(None, alias="completedAt")


class PlacementPreview(BaseApiModel):
    """Preview of where an image will be placed in a layout."""

    index: int
    x: int
    y: int
    width: int
    height: int
    label: str | None = None


class LayoutPreviewResponse(BaseApiModel):
    """Response from layout preview request."""

    layout: str
    resolved_layout: str | None = Field(None, alias="resolvedLayout")
    canvas_width: int = Field(..., alias="canvasWidth")
    canvas_height: int = Field(..., alias="canvasHeight")
    placements: list[PlacementPreview] | None = None
    metadata: dict[str, Any] | None = None


class ScheduleScreenshotOptions(BaseApiModel):
    """Screenshot options for scheduled captures."""

    viewport: ViewportConfig | None = None
    device: str | None = None
    format: ImageFormat | None = None
    full_page: bool | None = Field(None, alias="fullPage")
    quality: int | None = Field(None, ge=1, le=100)
    delay: int | None = Field(None, ge=0, le=30000)
    wait_for: str | None = Field(None, alias="waitFor")
    wait_until: WaitUntil | None = Field(None, alias="waitUntil")
    timeout: int | None = Field(None, ge=1000, le=60000)
    dark_mode: bool | None = Field(None, alias="darkMode")
    custom_css: str | None = Field(None, alias="customCss")
    hide_selectors: list[str] | None = Field(None, alias="hideSelectors")
    block_ads: bool | None = Field(None, alias="blockAds")
    block_cookie_banners: bool | None = Field(None, alias="blockCookieBanners")
    block_level: BlockLevel | None = Field(None, alias="blockLevel")


class CreateScheduleRequest(BaseApiModel):
    """Request to create a scheduled screenshot."""

    name: str = Field(..., max_length=255, description="Schedule name")
    url: str = Field(..., description="URL to capture")
    schedule: str = Field(..., description="Cron expression")
    timezone: str | None = Field(None, description="Timezone (e.g., 'America/New_York')")
    options: ScheduleScreenshotOptions | None = None
    webhook_url: str | None = Field(None, alias="webhookUrl")
    webhook_secret: str | None = Field(None, alias="webhookSecret")
    retention_days: int | None = Field(None, alias="retentionDays", ge=1, le=365)
    starts_at: datetime | None = Field(None, alias="startsAt")
    ends_at: datetime | None = Field(None, alias="endsAt")


class UpdateScheduleRequest(BaseApiModel):
    """Request to update a scheduled screenshot."""

    name: str | None = Field(None, max_length=255)
    url: str | None = None
    schedule: str | None = None
    timezone: str | None = None
    options: ScheduleScreenshotOptions | None = None
    webhook_url: str | None = Field(None, alias="webhookUrl")
    webhook_secret: str | None = Field(None, alias="webhookSecret")
    retention_days: int | None = Field(None, alias="retentionDays", ge=1, le=365)
    starts_at: datetime | None = Field(None, alias="startsAt")
    ends_at: datetime | None = Field(None, alias="endsAt")


class ScheduleResponse(BaseApiModel):
    """Response containing schedule details."""

    id: str
    name: str
    url: str
    schedule: str
    schedule_description: str | None = Field(None, alias="scheduleDescription")
    timezone: str | None = None
    status: str | None = None
    options: dict[str, Any] | None = None
    webhook_url: str | None = Field(None, alias="webhookUrl")
    retention_days: int | None = Field(None, alias="retentionDays")
    starts_at: datetime | None = Field(None, alias="startsAt")
    ends_at: datetime | None = Field(None, alias="endsAt")
    last_executed_at: datetime | None = Field(None, alias="lastExecutedAt")
    next_execution_at: datetime | None = Field(None, alias="nextExecutionAt")
    execution_count: int | None = Field(None, alias="executionCount")
    success_count: int | None = Field(None, alias="successCount")
    failure_count: int | None = Field(None, alias="failureCount")
    created_at: datetime | None = Field(None, alias="createdAt")
    updated_at: datetime | None = Field(None, alias="updatedAt")


class ScheduleListResponse(BaseApiModel):
    """Response containing a list of schedules."""

    schedules: list[ScheduleResponse]
    total: int


class ScheduleExecutionResponse(BaseApiModel):
    """Details of a schedule execution."""

    id: str
    executed_at: datetime | None = Field(None, alias="executedAt")
    status: str | None = None
    result_url: str | None = Field(None, alias="resultUrl")
    storage_url: str | None = Field(None, alias="storageUrl")
    file_size: int | None = Field(None, alias="fileSize")
    render_time_ms: int | None = Field(None, alias="renderTimeMs")
    error_code: str | None = Field(None, alias="errorCode")
    error_message: str | None = Field(None, alias="errorMessage")
    expires_at: datetime | None = Field(None, alias="expiresAt")


class ScheduleHistoryResponse(BaseApiModel):
    """Response containing schedule execution history."""

    schedule_id: str = Field(..., alias="scheduleId")
    total_executions: int = Field(..., alias="totalExecutions")
    executions: list[ScheduleExecutionResponse]


class QuotaDetailResponse(BaseApiModel):
    """Details about screenshot quota."""

    limit: int
    used: int
    remaining: int
    percent_used: int = Field(..., alias="percentUsed")


class BandwidthQuotaResponse(BaseApiModel):
    """Details about bandwidth quota."""

    limit_bytes: int = Field(..., alias="limitBytes")
    limit_formatted: str = Field(..., alias="limitFormatted")
    used_bytes: int = Field(..., alias="usedBytes")
    used_formatted: str = Field(..., alias="usedFormatted")
    remaining_bytes: int = Field(..., alias="remainingBytes")
    remaining_formatted: str = Field(..., alias="remainingFormatted")
    percent_used: int = Field(..., alias="percentUsed")


class QuotaStatusResponse(BaseApiModel):
    """Current quota status."""

    tier: str
    screenshots: QuotaDetailResponse
    bandwidth: BandwidthQuotaResponse
    period_ends: str = Field(..., alias="periodEnds")


class PeriodUsageResponse(BaseApiModel):
    """Usage for a specific period."""

    period_start: str = Field(..., alias="periodStart")
    period_end: str = Field(..., alias="periodEnd")
    screenshots_count: int = Field(..., alias="screenshotsCount")
    bandwidth_bytes: int = Field(..., alias="bandwidthBytes")
    bandwidth_formatted: str = Field(..., alias="bandwidthFormatted")


class QuotaResponse(BaseApiModel):
    """Quota information."""

    screenshots_limit: int = Field(..., alias="screenshotsLimit")
    bandwidth_limit_bytes: int = Field(..., alias="bandwidthLimitBytes")


class TotalsResponse(BaseApiModel):
    """Total usage across all periods."""

    screenshots_count: int = Field(..., alias="screenshotsCount")
    bandwidth_bytes: int = Field(..., alias="bandwidthBytes")
    bandwidth_formatted: str = Field(..., alias="bandwidthFormatted")


class UsageResponse(BaseApiModel):
    """Complete usage statistics."""

    tier: str
    current_period: PeriodUsageResponse = Field(..., alias="currentPeriod")
    quota: QuotaResponse
    history: list[PeriodUsageResponse] | None = None
    totals: TotalsResponse | None = None

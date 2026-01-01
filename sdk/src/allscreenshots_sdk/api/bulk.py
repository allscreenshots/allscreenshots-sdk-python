"""
Bulk Screenshots API endpoints.

This module provides methods for creating and managing bulk screenshot operations.
"""

from typing import TYPE_CHECKING

from allscreenshots_sdk.models import (
    BulkDefaults,
    BulkJobSummary,
    BulkRequest,
    BulkResponse,
    BulkStatusResponse,
    BulkUrlRequest,
)

if TYPE_CHECKING:
    from allscreenshots_sdk.http_client import AsyncHttpClient, HttpClient


class BulkApi:
    """
    Synchronous API for bulk screenshot operations.

    Example:
        >>> client = AllscreenshotsClient.builder().with_api_key("key").build()
        >>> bulk_job = client.bulk.create([
        ...     "https://example.com",
        ...     "https://github.com",
        ... ])
        >>> print(f"Bulk job ID: {bulk_job.id}")
    """

    def __init__(self, http_client: "HttpClient") -> None:
        """
        Initialize the Bulk API.

        Args:
            http_client: The HTTP client to use for requests.
        """
        self._http = http_client

    def create(
        self,
        urls: list[str] | list[BulkUrlRequest],
        *,
        defaults: BulkDefaults | None = None,
        webhook_url: str | None = None,
        webhook_secret: str | None = None,
    ) -> BulkResponse:
        """
        Create a bulk screenshot job.

        Args:
            urls: List of URLs to capture (strings or BulkUrlRequest objects).
            defaults: Default options to apply to all URLs.
            webhook_url: URL for webhook notification when complete.
            webhook_secret: Secret for webhook verification.

        Returns:
            BulkResponse with job ID and status.

        Example:
            >>> # Simple usage with URL strings
            >>> job = client.bulk.create([
            ...     "https://example.com",
            ...     "https://github.com",
            ... ])
            >>>
            >>> # Advanced usage with per-URL options
            >>> from allscreenshots_sdk import BulkUrlRequest, BulkUrlOptions
            >>> job = client.bulk.create([
            ...     BulkUrlRequest(url="https://example.com"),
            ...     BulkUrlRequest(
            ...         url="https://github.com",
            ...         options=BulkUrlOptions(full_page=True)
            ...     ),
            ... ])
        """
        # Convert string URLs to BulkUrlRequest objects
        url_requests = [
            BulkUrlRequest(url=u) if isinstance(u, str) else u
            for u in urls
        ]

        request = BulkRequest(
            urls=url_requests,
            defaults=defaults,
            webhook_url=webhook_url,
            webhook_secret=webhook_secret,
        )

        response = self._http.post(
            "/v1/screenshots/bulk",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkResponse.model_validate(response.json())

    def list_jobs(self) -> list[BulkJobSummary]:
        """
        List all bulk screenshot jobs.

        Returns:
            List of bulk job summaries.

        Example:
            >>> jobs = client.bulk.list_jobs()
            >>> for job in jobs:
            ...     print(f"{job.id}: {job.progress}%")
        """
        response = self._http.get("/v1/screenshots/bulk")
        return [BulkJobSummary.model_validate(job) for job in response.json()]

    def get_status(self, job_id: str) -> BulkStatusResponse:
        """
        Get detailed status of a bulk job.

        Args:
            job_id: The bulk job ID.

        Returns:
            Detailed status including individual job results.

        Example:
            >>> status = client.bulk.get_status("bulk-123")
            >>> print(f"Progress: {status.progress}%")
            >>> for job in status.jobs:
            ...     print(f"  {job.url}: {job.status}")
        """
        response = self._http.get(f"/v1/screenshots/bulk/{job_id}")
        return BulkStatusResponse.model_validate(response.json())

    def cancel(self, job_id: str) -> BulkJobSummary:
        """
        Cancel a bulk job.

        Args:
            job_id: The bulk job ID.

        Returns:
            Updated job summary.

        Example:
            >>> job = client.bulk.cancel("bulk-123")
            >>> print(f"Status: {job.status}")
        """
        response = self._http.post(f"/v1/screenshots/bulk/{job_id}/cancel")
        return BulkJobSummary.model_validate(response.json())


class AsyncBulkApi:
    """
    Asynchronous API for bulk screenshot operations.

    Example:
        >>> async with AllscreenshotsClient.builder().with_api_key("key").build_async() as client:
        ...     bulk_job = await client.bulk.create(["https://example.com"])
    """

    def __init__(self, http_client: "AsyncHttpClient") -> None:
        """
        Initialize the async Bulk API.

        Args:
            http_client: The async HTTP client to use for requests.
        """
        self._http = http_client

    async def create(
        self,
        urls: list[str] | list[BulkUrlRequest],
        *,
        defaults: BulkDefaults | None = None,
        webhook_url: str | None = None,
        webhook_secret: str | None = None,
    ) -> BulkResponse:
        """Create a bulk screenshot job."""
        url_requests = [
            BulkUrlRequest(url=u) if isinstance(u, str) else u
            for u in urls
        ]

        request = BulkRequest(
            urls=url_requests,
            defaults=defaults,
            webhook_url=webhook_url,
            webhook_secret=webhook_secret,
        )

        response = await self._http.post(
            "/v1/screenshots/bulk",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkResponse.model_validate(response.json())

    async def list_jobs(self) -> list[BulkJobSummary]:
        """List all bulk screenshot jobs."""
        response = await self._http.get("/v1/screenshots/bulk")
        return [BulkJobSummary.model_validate(job) for job in response.json()]

    async def get_status(self, job_id: str) -> BulkStatusResponse:
        """Get detailed status of a bulk job."""
        response = await self._http.get(f"/v1/screenshots/bulk/{job_id}")
        return BulkStatusResponse.model_validate(response.json())

    async def cancel(self, job_id: str) -> BulkJobSummary:
        """Cancel a bulk job."""
        response = await self._http.post(f"/v1/screenshots/bulk/{job_id}/cancel")
        return BulkJobSummary.model_validate(response.json())

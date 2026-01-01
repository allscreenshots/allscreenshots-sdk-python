"""
Schedules API endpoints.

This module provides methods for creating and managing scheduled screenshot captures.
"""

from typing import TYPE_CHECKING

from allscreenshots_sdk.models import (
    CreateScheduleRequest,
    ScheduleHistoryResponse,
    ScheduleListResponse,
    ScheduleResponse,
    ScheduleScreenshotOptions,
    UpdateScheduleRequest,
)

if TYPE_CHECKING:
    from datetime import datetime

    from allscreenshots_sdk.http_client import AsyncHttpClient, HttpClient


class SchedulesApi:
    """
    Synchronous API for schedule operations.

    Schedules allow you to automatically capture screenshots at specified intervals
    using cron expressions.

    Example:
        >>> client = AllscreenshotsClient.builder().with_api_key("key").build()
        >>> schedule = client.schedules.create(
        ...     name="Daily homepage",
        ...     url="https://example.com",
        ...     schedule="0 9 * * *",  # Every day at 9 AM
        ... )
        >>> print(f"Schedule ID: {schedule.id}")
    """

    def __init__(self, http_client: "HttpClient") -> None:
        """
        Initialize the Schedules API.

        Args:
            http_client: The HTTP client to use for requests.
        """
        self._http = http_client

    def create(
        self,
        name: str,
        url: str,
        schedule: str,
        *,
        timezone: str | None = None,
        options: ScheduleScreenshotOptions | None = None,
        webhook_url: str | None = None,
        webhook_secret: str | None = None,
        retention_days: int | None = None,
        starts_at: "datetime | None" = None,
        ends_at: "datetime | None" = None,
    ) -> ScheduleResponse:
        """
        Create a scheduled screenshot.

        Args:
            name: Name for the schedule.
            url: URL to capture.
            schedule: Cron expression (e.g., "0 9 * * *" for daily at 9 AM).
            timezone: Timezone for the schedule (e.g., "America/New_York").
            options: Screenshot capture options.
            webhook_url: Webhook URL for notifications.
            webhook_secret: Webhook secret for verification.
            retention_days: Number of days to retain screenshots (1-365).
            starts_at: When the schedule should start.
            ends_at: When the schedule should end.

        Returns:
            Created schedule response.

        Example:
            >>> schedule = client.schedules.create(
            ...     name="Weekly report",
            ...     url="https://dashboard.example.com/report",
            ...     schedule="0 8 * * 1",  # Every Monday at 8 AM
            ...     timezone="America/New_York",
            ...     options=ScheduleScreenshotOptions(
            ...         device="Desktop HD",
            ...         full_page=True,
            ...     ),
            ...     retention_days=30,
            ... )
        """
        request = CreateScheduleRequest(
            name=name,
            url=url,
            schedule=schedule,
            timezone=timezone,
            options=options,
            webhook_url=webhook_url,
            webhook_secret=webhook_secret,
            retention_days=retention_days,
            starts_at=starts_at,
            ends_at=ends_at,
        )

        response = self._http.post(
            "/v1/schedules",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )
        return ScheduleResponse.model_validate(response.json())

    def list(self) -> ScheduleListResponse:
        """
        List all schedules.

        Returns:
            List of schedules with total count.

        Example:
            >>> result = client.schedules.list()
            >>> print(f"Total schedules: {result.total}")
            >>> for schedule in result.schedules:
            ...     print(f"  {schedule.name}: {schedule.status}")
        """
        response = self._http.get("/v1/schedules")
        return ScheduleListResponse.model_validate(response.json())

    def get(self, schedule_id: str) -> ScheduleResponse:
        """
        Get a schedule by ID.

        Args:
            schedule_id: The schedule ID.

        Returns:
            Schedule details.

        Example:
            >>> schedule = client.schedules.get("schedule-123")
            >>> print(f"Next run: {schedule.next_execution_at}")
        """
        response = self._http.get(f"/v1/schedules/{schedule_id}")
        return ScheduleResponse.model_validate(response.json())

    def update(
        self,
        schedule_id: str,
        *,
        name: str | None = None,
        url: str | None = None,
        schedule: str | None = None,
        timezone: str | None = None,
        options: ScheduleScreenshotOptions | None = None,
        webhook_url: str | None = None,
        webhook_secret: str | None = None,
        retention_days: int | None = None,
        starts_at: "datetime | None" = None,
        ends_at: "datetime | None" = None,
    ) -> ScheduleResponse:
        """
        Update a schedule.

        Args:
            schedule_id: The schedule ID.
            name: New name.
            url: New URL.
            schedule: New cron expression.
            timezone: New timezone.
            options: New screenshot options.
            webhook_url: New webhook URL.
            webhook_secret: New webhook secret.
            retention_days: New retention period.
            starts_at: New start time.
            ends_at: New end time.

        Returns:
            Updated schedule.

        Example:
            >>> schedule = client.schedules.update(
            ...     "schedule-123",
            ...     name="Updated schedule name",
            ...     schedule="0 10 * * *",  # Changed to 10 AM
            ... )
        """
        request = UpdateScheduleRequest(
            name=name,
            url=url,
            schedule=schedule,
            timezone=timezone,
            options=options,
            webhook_url=webhook_url,
            webhook_secret=webhook_secret,
            retention_days=retention_days,
            starts_at=starts_at,
            ends_at=ends_at,
        )

        response = self._http.put(
            f"/v1/schedules/{schedule_id}",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )
        return ScheduleResponse.model_validate(response.json())

    def delete(self, schedule_id: str) -> None:
        """
        Delete a schedule.

        Args:
            schedule_id: The schedule ID.

        Example:
            >>> client.schedules.delete("schedule-123")
        """
        self._http.delete(f"/v1/schedules/{schedule_id}")

    def pause(self, schedule_id: str) -> ScheduleResponse:
        """
        Pause a schedule.

        Args:
            schedule_id: The schedule ID.

        Returns:
            Updated schedule.

        Example:
            >>> schedule = client.schedules.pause("schedule-123")
            >>> print(f"Status: {schedule.status}")  # "paused"
        """
        response = self._http.post(f"/v1/schedules/{schedule_id}/pause")
        return ScheduleResponse.model_validate(response.json())

    def resume(self, schedule_id: str) -> ScheduleResponse:
        """
        Resume a paused schedule.

        Args:
            schedule_id: The schedule ID.

        Returns:
            Updated schedule.

        Example:
            >>> schedule = client.schedules.resume("schedule-123")
            >>> print(f"Status: {schedule.status}")  # "active"
        """
        response = self._http.post(f"/v1/schedules/{schedule_id}/resume")
        return ScheduleResponse.model_validate(response.json())

    def trigger(self, schedule_id: str) -> ScheduleResponse:
        """
        Manually trigger a schedule execution.

        Args:
            schedule_id: The schedule ID.

        Returns:
            Updated schedule.

        Example:
            >>> schedule = client.schedules.trigger("schedule-123")
            >>> print(f"Last executed: {schedule.last_executed_at}")
        """
        response = self._http.post(f"/v1/schedules/{schedule_id}/trigger")
        return ScheduleResponse.model_validate(response.json())

    def get_history(self, schedule_id: str, *, limit: int | None = None) -> ScheduleHistoryResponse:
        """
        Get execution history for a schedule.

        Args:
            schedule_id: The schedule ID.
            limit: Maximum number of executions to return.

        Returns:
            Execution history.

        Example:
            >>> history = client.schedules.get_history("schedule-123", limit=10)
            >>> for execution in history.executions:
            ...     print(f"{execution.executed_at}: {execution.status}")
        """
        params = {"limit": limit} if limit else None
        response = self._http.get(f"/v1/schedules/{schedule_id}/history", params=params)
        return ScheduleHistoryResponse.model_validate(response.json())


class AsyncSchedulesApi:
    """
    Asynchronous API for schedule operations.

    Example:
        >>> async with AllscreenshotsClient.builder().with_api_key("key").build_async() as client:
        ...     schedule = await client.schedules.create(
        ...         name="Daily homepage",
        ...         url="https://example.com",
        ...         schedule="0 9 * * *",
        ...     )
    """

    def __init__(self, http_client: "AsyncHttpClient") -> None:
        """
        Initialize the async Schedules API.

        Args:
            http_client: The async HTTP client to use for requests.
        """
        self._http = http_client

    async def create(
        self,
        name: str,
        url: str,
        schedule: str,
        *,
        timezone: str | None = None,
        options: ScheduleScreenshotOptions | None = None,
        webhook_url: str | None = None,
        webhook_secret: str | None = None,
        retention_days: int | None = None,
        starts_at: "datetime | None" = None,
        ends_at: "datetime | None" = None,
    ) -> ScheduleResponse:
        """Create a scheduled screenshot."""
        request = CreateScheduleRequest(
            name=name,
            url=url,
            schedule=schedule,
            timezone=timezone,
            options=options,
            webhook_url=webhook_url,
            webhook_secret=webhook_secret,
            retention_days=retention_days,
            starts_at=starts_at,
            ends_at=ends_at,
        )

        response = await self._http.post(
            "/v1/schedules",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )
        return ScheduleResponse.model_validate(response.json())

    async def list(self) -> ScheduleListResponse:
        """List all schedules."""
        response = await self._http.get("/v1/schedules")
        return ScheduleListResponse.model_validate(response.json())

    async def get(self, schedule_id: str) -> ScheduleResponse:
        """Get a schedule by ID."""
        response = await self._http.get(f"/v1/schedules/{schedule_id}")
        return ScheduleResponse.model_validate(response.json())

    async def update(
        self,
        schedule_id: str,
        *,
        name: str | None = None,
        url: str | None = None,
        schedule: str | None = None,
        timezone: str | None = None,
        options: ScheduleScreenshotOptions | None = None,
        webhook_url: str | None = None,
        webhook_secret: str | None = None,
        retention_days: int | None = None,
        starts_at: "datetime | None" = None,
        ends_at: "datetime | None" = None,
    ) -> ScheduleResponse:
        """Update a schedule."""
        request = UpdateScheduleRequest(
            name=name,
            url=url,
            schedule=schedule,
            timezone=timezone,
            options=options,
            webhook_url=webhook_url,
            webhook_secret=webhook_secret,
            retention_days=retention_days,
            starts_at=starts_at,
            ends_at=ends_at,
        )

        response = await self._http.put(
            f"/v1/schedules/{schedule_id}",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )
        return ScheduleResponse.model_validate(response.json())

    async def delete(self, schedule_id: str) -> None:
        """Delete a schedule."""
        await self._http.delete(f"/v1/schedules/{schedule_id}")

    async def pause(self, schedule_id: str) -> ScheduleResponse:
        """Pause a schedule."""
        response = await self._http.post(f"/v1/schedules/{schedule_id}/pause")
        return ScheduleResponse.model_validate(response.json())

    async def resume(self, schedule_id: str) -> ScheduleResponse:
        """Resume a paused schedule."""
        response = await self._http.post(f"/v1/schedules/{schedule_id}/resume")
        return ScheduleResponse.model_validate(response.json())

    async def trigger(self, schedule_id: str) -> ScheduleResponse:
        """Manually trigger a schedule execution."""
        response = await self._http.post(f"/v1/schedules/{schedule_id}/trigger")
        return ScheduleResponse.model_validate(response.json())

    async def get_history(
        self, schedule_id: str, *, limit: int | None = None
    ) -> ScheduleHistoryResponse:
        """Get execution history for a schedule."""
        params = {"limit": limit} if limit else None
        response = await self._http.get(f"/v1/schedules/{schedule_id}/history", params=params)
        return ScheduleHistoryResponse.model_validate(response.json())

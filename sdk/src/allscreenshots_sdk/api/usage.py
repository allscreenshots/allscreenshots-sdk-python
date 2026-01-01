"""
Usage API endpoints.

This module provides methods for checking usage statistics and quota information.
"""

from typing import TYPE_CHECKING

from allscreenshots_sdk.models import QuotaStatusResponse, UsageResponse

if TYPE_CHECKING:
    from allscreenshots_sdk.http_client import AsyncHttpClient, HttpClient


class UsageApi:
    """
    Synchronous API for usage and quota operations.

    Example:
        >>> client = AllscreenshotsClient.builder().with_api_key("key").build()
        >>> usage = client.usage.get()
        >>> print(f"Screenshots this period: {usage.current_period.screenshots_count}")
    """

    def __init__(self, http_client: "HttpClient") -> None:
        """
        Initialize the Usage API.

        Args:
            http_client: The HTTP client to use for requests.
        """
        self._http = http_client

    def get(self) -> UsageResponse:
        """
        Get usage statistics.

        Returns:
            Usage response with current period, quota, and history.

        Example:
            >>> usage = client.usage.get()
            >>> print(f"Tier: {usage.tier}")
            >>> print(f"Screenshots: {usage.current_period.screenshots_count}")
            >>> print(f"Bandwidth: {usage.current_period.bandwidth_formatted}")
        """
        response = self._http.get("/v1/usage")
        return UsageResponse.model_validate(response.json())

    def get_quota(self) -> QuotaStatusResponse:
        """
        Get current quota status.

        Returns:
            Quota status with limits and usage.

        Example:
            >>> quota = client.usage.get_quota()
            >>> print(f"Screenshots: {quota.screenshots.used}/{quota.screenshots.limit}")
            >>> print(f"Bandwidth: {quota.bandwidth.used_formatted}/{quota.bandwidth.limit_formatted}")
            >>> if quota.screenshots.percent_used > 80:
            ...     print("Warning: Approaching screenshot limit!")
        """
        response = self._http.get("/v1/usage/quota")
        return QuotaStatusResponse.model_validate(response.json())


class AsyncUsageApi:
    """
    Asynchronous API for usage and quota operations.

    Example:
        >>> async with AllscreenshotsClient.builder().with_api_key("key").build_async() as client:
        ...     usage = await client.usage.get()
        ...     print(f"Screenshots: {usage.current_period.screenshots_count}")
    """

    def __init__(self, http_client: "AsyncHttpClient") -> None:
        """
        Initialize the async Usage API.

        Args:
            http_client: The async HTTP client to use for requests.
        """
        self._http = http_client

    async def get(self) -> UsageResponse:
        """Get usage statistics."""
        response = await self._http.get("/v1/usage")
        return UsageResponse.model_validate(response.json())

    async def get_quota(self) -> QuotaStatusResponse:
        """Get current quota status."""
        response = await self._http.get("/v1/usage/quota")
        return QuotaStatusResponse.model_validate(response.json())

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .requests import (
    RequestsResource,
    AsyncRequestsResource,
    RequestsResourceWithRawResponse,
    AsyncRequestsResourceWithRawResponse,
    RequestsResourceWithStreamingResponse,
    AsyncRequestsResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncOffsetPage, AsyncOffsetPage
from .....types.waap import WaapResolution
from ....._base_client import AsyncPaginator, make_request_options
from .....types.waap.domains import (
    analytics_list_ddos_info_params,
    analytics_list_ddos_attacks_params,
    analytics_list_event_traffic_params,
    analytics_get_event_statistics_params,
)
from .....types.waap.waap_ddos_info import WaapDDOSInfo
from .....types.waap.waap_resolution import WaapResolution
from .....types.waap.waap_ddos_attack import WaapDDOSAttack
from .....types.waap.waap_event_statistics import WaapEventStatistics
from .....types.waap.domains.analytics_list_event_traffic_response import AnalyticsListEventTrafficResponse

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    @cached_property
    def requests(self) -> RequestsResource:
        return RequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AnalyticsResourceWithStreamingResponse(self)

    def get_event_statistics(
        self,
        domain_id: int,
        *,
        start: Union[str, datetime],
        action: Optional[List[Literal["block", "captcha", "handshake", "monitor"]]] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ip: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reference_id: Optional[List[str]] | NotGiven = NOT_GIVEN,
        result: Optional[List[Literal["passed", "blocked", "monitored", "allowed"]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapEventStatistics:
        """
        Retrieve an domain's event statistics

        Args:
          domain_id: The domain ID

          start: Filter traffic starting from a specified date in ISO 8601 format

          action: A list of action names to filter on.

          end: Filter traffic up to a specified end date in ISO 8601 format. If not provided,
              defaults to the current date and time.

          ip: A list of IPs to filter event statistics.

          reference_id: A list of reference IDs to filter event statistics.

          result: A list of results to filter event statistics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/waap/v1/domains/{domain_id}/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start": start,
                        "action": action,
                        "end": end,
                        "ip": ip,
                        "reference_id": reference_id,
                        "result": result,
                    },
                    analytics_get_event_statistics_params.AnalyticsGetEventStatisticsParams,
                ),
            ),
            cast_to=WaapEventStatistics,
        )

    def list_ddos_attacks(
        self,
        domain_id: int,
        *,
        end_time: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        ordering: Literal["start_time", "-start_time", "end_time", "-end_time"] | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[WaapDDOSAttack]:
        """
        Retrieve a domain's DDoS attacks

        Args:
          domain_id: The domain ID

          end_time: Filter attacks up to a specified end date in ISO 8601 format

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Sort the response by given field.

          start_time: Filter attacks starting from a specified date in ISO 8601 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/ddos-attacks",
            page=SyncOffsetPage[WaapDDOSAttack],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "start_time": start_time,
                    },
                    analytics_list_ddos_attacks_params.AnalyticsListDDOSAttacksParams,
                ),
            ),
            model=WaapDDOSAttack,
        )

    def list_ddos_info(
        self,
        domain_id: int,
        *,
        group_by: Literal["URL", "User-Agent", "IP"],
        start: Union[str, datetime],
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[WaapDDOSInfo]:
        """
        Returns the top DDoS counts grouped by URL, User-Agent or IP

        Args:
          domain_id: The domain ID

          group_by: The identity of the requests to group by

          start: Filter traffic starting from a specified date in ISO 8601 format

          end: Filter traffic up to a specified end date in ISO 8601 format. If not provided,
              defaults to the current date and time.

          limit: Number of items to return

          offset: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/ddos-info",
            page=SyncOffsetPage[WaapDDOSInfo],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "group_by": group_by,
                        "start": start,
                        "end": end,
                        "limit": limit,
                        "offset": offset,
                    },
                    analytics_list_ddos_info_params.AnalyticsListDDOSInfoParams,
                ),
            ),
            model=WaapDDOSInfo,
        )

    def list_event_traffic(
        self,
        domain_id: int,
        *,
        resolution: WaapResolution,
        start: Union[str, datetime],
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyticsListEventTrafficResponse:
        """
        Retrieves a comprehensive report on a domain's traffic statistics based on
        Clickhouse. The report includes details such as API requests, blocked events,
        error counts, and many more traffic-related metrics.

        Args:
          domain_id: The domain ID

          resolution: Specifies the granularity of the result data.

          start: Filter traffic starting from a specified date in ISO 8601 format

          end: Filter traffic up to a specified end date in ISO 8601 format. If not provided,
              defaults to the current date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/waap/v1/domains/{domain_id}/traffic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resolution": resolution,
                        "start": start,
                        "end": end,
                    },
                    analytics_list_event_traffic_params.AnalyticsListEventTrafficParams,
                ),
            ),
            cast_to=AnalyticsListEventTrafficResponse,
        )


class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def requests(self) -> AsyncRequestsResource:
        return AsyncRequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAnalyticsResourceWithStreamingResponse(self)

    async def get_event_statistics(
        self,
        domain_id: int,
        *,
        start: Union[str, datetime],
        action: Optional[List[Literal["block", "captcha", "handshake", "monitor"]]] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ip: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reference_id: Optional[List[str]] | NotGiven = NOT_GIVEN,
        result: Optional[List[Literal["passed", "blocked", "monitored", "allowed"]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapEventStatistics:
        """
        Retrieve an domain's event statistics

        Args:
          domain_id: The domain ID

          start: Filter traffic starting from a specified date in ISO 8601 format

          action: A list of action names to filter on.

          end: Filter traffic up to a specified end date in ISO 8601 format. If not provided,
              defaults to the current date and time.

          ip: A list of IPs to filter event statistics.

          reference_id: A list of reference IDs to filter event statistics.

          result: A list of results to filter event statistics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/waap/v1/domains/{domain_id}/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start": start,
                        "action": action,
                        "end": end,
                        "ip": ip,
                        "reference_id": reference_id,
                        "result": result,
                    },
                    analytics_get_event_statistics_params.AnalyticsGetEventStatisticsParams,
                ),
            ),
            cast_to=WaapEventStatistics,
        )

    def list_ddos_attacks(
        self,
        domain_id: int,
        *,
        end_time: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        ordering: Literal["start_time", "-start_time", "end_time", "-end_time"] | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WaapDDOSAttack, AsyncOffsetPage[WaapDDOSAttack]]:
        """
        Retrieve a domain's DDoS attacks

        Args:
          domain_id: The domain ID

          end_time: Filter attacks up to a specified end date in ISO 8601 format

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Sort the response by given field.

          start_time: Filter attacks starting from a specified date in ISO 8601 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/ddos-attacks",
            page=AsyncOffsetPage[WaapDDOSAttack],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "start_time": start_time,
                    },
                    analytics_list_ddos_attacks_params.AnalyticsListDDOSAttacksParams,
                ),
            ),
            model=WaapDDOSAttack,
        )

    def list_ddos_info(
        self,
        domain_id: int,
        *,
        group_by: Literal["URL", "User-Agent", "IP"],
        start: Union[str, datetime],
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WaapDDOSInfo, AsyncOffsetPage[WaapDDOSInfo]]:
        """
        Returns the top DDoS counts grouped by URL, User-Agent or IP

        Args:
          domain_id: The domain ID

          group_by: The identity of the requests to group by

          start: Filter traffic starting from a specified date in ISO 8601 format

          end: Filter traffic up to a specified end date in ISO 8601 format. If not provided,
              defaults to the current date and time.

          limit: Number of items to return

          offset: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/ddos-info",
            page=AsyncOffsetPage[WaapDDOSInfo],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "group_by": group_by,
                        "start": start,
                        "end": end,
                        "limit": limit,
                        "offset": offset,
                    },
                    analytics_list_ddos_info_params.AnalyticsListDDOSInfoParams,
                ),
            ),
            model=WaapDDOSInfo,
        )

    async def list_event_traffic(
        self,
        domain_id: int,
        *,
        resolution: WaapResolution,
        start: Union[str, datetime],
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyticsListEventTrafficResponse:
        """
        Retrieves a comprehensive report on a domain's traffic statistics based on
        Clickhouse. The report includes details such as API requests, blocked events,
        error counts, and many more traffic-related metrics.

        Args:
          domain_id: The domain ID

          resolution: Specifies the granularity of the result data.

          start: Filter traffic starting from a specified date in ISO 8601 format

          end: Filter traffic up to a specified end date in ISO 8601 format. If not provided,
              defaults to the current date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/waap/v1/domains/{domain_id}/traffic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "resolution": resolution,
                        "start": start,
                        "end": end,
                    },
                    analytics_list_event_traffic_params.AnalyticsListEventTrafficParams,
                ),
            ),
            cast_to=AnalyticsListEventTrafficResponse,
        )


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get_event_statistics = to_raw_response_wrapper(
            analytics.get_event_statistics,
        )
        self.list_ddos_attacks = to_raw_response_wrapper(
            analytics.list_ddos_attacks,
        )
        self.list_ddos_info = to_raw_response_wrapper(
            analytics.list_ddos_info,
        )
        self.list_event_traffic = to_raw_response_wrapper(
            analytics.list_event_traffic,
        )

    @cached_property
    def requests(self) -> RequestsResourceWithRawResponse:
        return RequestsResourceWithRawResponse(self._analytics.requests)


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get_event_statistics = async_to_raw_response_wrapper(
            analytics.get_event_statistics,
        )
        self.list_ddos_attacks = async_to_raw_response_wrapper(
            analytics.list_ddos_attacks,
        )
        self.list_ddos_info = async_to_raw_response_wrapper(
            analytics.list_ddos_info,
        )
        self.list_event_traffic = async_to_raw_response_wrapper(
            analytics.list_event_traffic,
        )

    @cached_property
    def requests(self) -> AsyncRequestsResourceWithRawResponse:
        return AsyncRequestsResourceWithRawResponse(self._analytics.requests)


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get_event_statistics = to_streamed_response_wrapper(
            analytics.get_event_statistics,
        )
        self.list_ddos_attacks = to_streamed_response_wrapper(
            analytics.list_ddos_attacks,
        )
        self.list_ddos_info = to_streamed_response_wrapper(
            analytics.list_ddos_info,
        )
        self.list_event_traffic = to_streamed_response_wrapper(
            analytics.list_event_traffic,
        )

    @cached_property
    def requests(self) -> RequestsResourceWithStreamingResponse:
        return RequestsResourceWithStreamingResponse(self._analytics.requests)


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get_event_statistics = async_to_streamed_response_wrapper(
            analytics.get_event_statistics,
        )
        self.list_ddos_attacks = async_to_streamed_response_wrapper(
            analytics.list_ddos_attacks,
        )
        self.list_ddos_info = async_to_streamed_response_wrapper(
            analytics.list_ddos_info,
        )
        self.list_event_traffic = async_to_streamed_response_wrapper(
            analytics.list_event_traffic,
        )

    @cached_property
    def requests(self) -> AsyncRequestsResourceWithStreamingResponse:
        return AsyncRequestsResourceWithStreamingResponse(self._analytics.requests)

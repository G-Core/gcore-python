# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.waap.domains import (
    statistic_get_ddos_info_params,
    statistic_get_ddos_attacks_params,
    statistic_get_traffic_series_params,
    statistic_get_requests_series_params,
    statistic_get_events_aggregated_params,
)
from ....types.waap.domains.waap_ddos_info import WaapDDOSInfo
from ....types.waap.domains.waap_ddos_attack import WaapDDOSAttack
from ....types.waap.domains.waap_request_details import WaapRequestDetails
from ....types.waap.domains.waap_request_summary import WaapRequestSummary
from ....types.waap.domains.waap_event_statistics import WaapEventStatistics
from ....types.waap.domains.statistic_get_traffic_series_response import StatisticGetTrafficSeriesResponse

__all__ = ["StatisticsResource", "AsyncStatisticsResource"]


class StatisticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatisticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return StatisticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatisticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return StatisticsResourceWithStreamingResponse(self)

    def get_ddos_attacks(
        self,
        domain_id: int,
        *,
        end_time: Union[str, datetime, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal["start_time", "-start_time", "end_time", "-end_time"] | Omit = omit,
        start_time: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                    statistic_get_ddos_attacks_params.StatisticGetDDOSAttacksParams,
                ),
            ),
            model=WaapDDOSAttack,
        )

    def get_ddos_info(
        self,
        domain_id: int,
        *,
        group_by: Literal["URL", "User-Agent", "IP"],
        start: str,
        end: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapDDOSInfo]:
        """
        Returns the top DDoS counts grouped by URL, User-Agent or IP

        Args:
          domain_id: The domain ID

          group_by: The identity of the requests to group by

          start: Filter data items starting from a specified date in ISO 8601 format

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

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
                    statistic_get_ddos_info_params.StatisticGetDDOSInfoParams,
                ),
            ),
            model=WaapDDOSInfo,
        )

    def get_events_aggregated(
        self,
        domain_id: int,
        *,
        start: str,
        action: Optional[List[Literal["block", "captcha", "handshake", "monitor"]]] | Omit = omit,
        end: Optional[str] | Omit = omit,
        ip: Optional[SequenceNotStr[str]] | Omit = omit,
        reference_id: Optional[SequenceNotStr[str]] | Omit = omit,
        result: Optional[List[Literal["passed", "blocked", "monitored", "allowed"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapEventStatistics:
        """
        Retrieve an domain's event statistics

        Args:
          domain_id: The domain ID

          start: Filter data items starting from a specified date in ISO 8601 format

          action: A list of action names to filter on.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

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
                    statistic_get_events_aggregated_params.StatisticGetEventsAggregatedParams,
                ),
            ),
            cast_to=WaapEventStatistics,
        )

    def get_request_details(
        self,
        request_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapRequestDetails:
        """
        Retrieves all the available information for a request that matches a given
        request id

        Args:
          domain_id: The domain ID

          request_id: The request ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            f"/waap/v1/domains/{domain_id}/requests/{request_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapRequestDetails,
        )

    def get_requests_series(
        self,
        domain_id: int,
        *,
        start: str,
        actions: List[Literal["allow", "block", "captcha", "handshake"]] | Omit = omit,
        countries: SequenceNotStr[str] | Omit = omit,
        end: Optional[str] | Omit = omit,
        ip: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: str | Omit = omit,
        reference_id: str | Omit = omit,
        security_rule_name: str | Omit = omit,
        status_code: int | Omit = omit,
        traffic_types: List[
            Literal[
                "policy_allowed",
                "policy_blocked",
                "custom_rule_allowed",
                "custom_blocked",
                "legit_requests",
                "sanctioned",
                "dynamic",
                "api",
                "static",
                "ajax",
                "redirects",
                "monitor",
                "err_40x",
                "err_50x",
                "passed_to_origin",
                "timeout",
                "other",
                "ddos",
                "legit",
                "monitored",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapRequestSummary]:
        """
        Retrieve a domain's requests data.

        Args:
          domain_id: The domain ID

          start: Filter data items starting from a specified date in ISO 8601 format

          actions: Filter the response by actions.

          countries: Filter the response by country codes in ISO 3166-1 alpha-2 format.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          ip: Filter the response by IP.

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Sort the response by given field.

          reference_id: Filter the response by reference ID.

          security_rule_name: Filter the response by security rule name.

          status_code: Filter the response by response code.

          traffic_types: Filter the response by traffic types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/requests",
            page=SyncOffsetPage[WaapRequestSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start": start,
                        "actions": actions,
                        "countries": countries,
                        "end": end,
                        "ip": ip,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "reference_id": reference_id,
                        "security_rule_name": security_rule_name,
                        "status_code": status_code,
                        "traffic_types": traffic_types,
                    },
                    statistic_get_requests_series_params.StatisticGetRequestsSeriesParams,
                ),
            ),
            model=WaapRequestSummary,
        )

    def get_traffic_series(
        self,
        domain_id: int,
        *,
        resolution: Literal["daily", "hourly", "minutely"],
        start: str,
        end: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticGetTrafficSeriesResponse:
        """
        Retrieves a comprehensive report on a domain's traffic statistics based on
        Clickhouse. The report includes details such as API requests, blocked events,
        error counts, and many more traffic-related metrics.

        Args:
          domain_id: The domain ID

          resolution: Specifies the granularity of the result data.

          start: Filter data items starting from a specified date in ISO 8601 format

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

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
                    statistic_get_traffic_series_params.StatisticGetTrafficSeriesParams,
                ),
            ),
            cast_to=StatisticGetTrafficSeriesResponse,
        )


class AsyncStatisticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatisticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatisticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatisticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncStatisticsResourceWithStreamingResponse(self)

    def get_ddos_attacks(
        self,
        domain_id: int,
        *,
        end_time: Union[str, datetime, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal["start_time", "-start_time", "end_time", "-end_time"] | Omit = omit,
        start_time: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                    statistic_get_ddos_attacks_params.StatisticGetDDOSAttacksParams,
                ),
            ),
            model=WaapDDOSAttack,
        )

    def get_ddos_info(
        self,
        domain_id: int,
        *,
        group_by: Literal["URL", "User-Agent", "IP"],
        start: str,
        end: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapDDOSInfo, AsyncOffsetPage[WaapDDOSInfo]]:
        """
        Returns the top DDoS counts grouped by URL, User-Agent or IP

        Args:
          domain_id: The domain ID

          group_by: The identity of the requests to group by

          start: Filter data items starting from a specified date in ISO 8601 format

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

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
                    statistic_get_ddos_info_params.StatisticGetDDOSInfoParams,
                ),
            ),
            model=WaapDDOSInfo,
        )

    async def get_events_aggregated(
        self,
        domain_id: int,
        *,
        start: str,
        action: Optional[List[Literal["block", "captcha", "handshake", "monitor"]]] | Omit = omit,
        end: Optional[str] | Omit = omit,
        ip: Optional[SequenceNotStr[str]] | Omit = omit,
        reference_id: Optional[SequenceNotStr[str]] | Omit = omit,
        result: Optional[List[Literal["passed", "blocked", "monitored", "allowed"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapEventStatistics:
        """
        Retrieve an domain's event statistics

        Args:
          domain_id: The domain ID

          start: Filter data items starting from a specified date in ISO 8601 format

          action: A list of action names to filter on.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

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
                    statistic_get_events_aggregated_params.StatisticGetEventsAggregatedParams,
                ),
            ),
            cast_to=WaapEventStatistics,
        )

    async def get_request_details(
        self,
        request_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapRequestDetails:
        """
        Retrieves all the available information for a request that matches a given
        request id

        Args:
          domain_id: The domain ID

          request_id: The request ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            f"/waap/v1/domains/{domain_id}/requests/{request_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapRequestDetails,
        )

    def get_requests_series(
        self,
        domain_id: int,
        *,
        start: str,
        actions: List[Literal["allow", "block", "captcha", "handshake"]] | Omit = omit,
        countries: SequenceNotStr[str] | Omit = omit,
        end: Optional[str] | Omit = omit,
        ip: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: str | Omit = omit,
        reference_id: str | Omit = omit,
        security_rule_name: str | Omit = omit,
        status_code: int | Omit = omit,
        traffic_types: List[
            Literal[
                "policy_allowed",
                "policy_blocked",
                "custom_rule_allowed",
                "custom_blocked",
                "legit_requests",
                "sanctioned",
                "dynamic",
                "api",
                "static",
                "ajax",
                "redirects",
                "monitor",
                "err_40x",
                "err_50x",
                "passed_to_origin",
                "timeout",
                "other",
                "ddos",
                "legit",
                "monitored",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapRequestSummary, AsyncOffsetPage[WaapRequestSummary]]:
        """
        Retrieve a domain's requests data.

        Args:
          domain_id: The domain ID

          start: Filter data items starting from a specified date in ISO 8601 format

          actions: Filter the response by actions.

          countries: Filter the response by country codes in ISO 3166-1 alpha-2 format.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          ip: Filter the response by IP.

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Sort the response by given field.

          reference_id: Filter the response by reference ID.

          security_rule_name: Filter the response by security rule name.

          status_code: Filter the response by response code.

          traffic_types: Filter the response by traffic types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/requests",
            page=AsyncOffsetPage[WaapRequestSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start": start,
                        "actions": actions,
                        "countries": countries,
                        "end": end,
                        "ip": ip,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "reference_id": reference_id,
                        "security_rule_name": security_rule_name,
                        "status_code": status_code,
                        "traffic_types": traffic_types,
                    },
                    statistic_get_requests_series_params.StatisticGetRequestsSeriesParams,
                ),
            ),
            model=WaapRequestSummary,
        )

    async def get_traffic_series(
        self,
        domain_id: int,
        *,
        resolution: Literal["daily", "hourly", "minutely"],
        start: str,
        end: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticGetTrafficSeriesResponse:
        """
        Retrieves a comprehensive report on a domain's traffic statistics based on
        Clickhouse. The report includes details such as API requests, blocked events,
        error counts, and many more traffic-related metrics.

        Args:
          domain_id: The domain ID

          resolution: Specifies the granularity of the result data.

          start: Filter data items starting from a specified date in ISO 8601 format

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

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
                    statistic_get_traffic_series_params.StatisticGetTrafficSeriesParams,
                ),
            ),
            cast_to=StatisticGetTrafficSeriesResponse,
        )


class StatisticsResourceWithRawResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get_ddos_attacks = to_raw_response_wrapper(
            statistics.get_ddos_attacks,
        )
        self.get_ddos_info = to_raw_response_wrapper(
            statistics.get_ddos_info,
        )
        self.get_events_aggregated = to_raw_response_wrapper(
            statistics.get_events_aggregated,
        )
        self.get_request_details = to_raw_response_wrapper(
            statistics.get_request_details,
        )
        self.get_requests_series = to_raw_response_wrapper(
            statistics.get_requests_series,
        )
        self.get_traffic_series = to_raw_response_wrapper(
            statistics.get_traffic_series,
        )


class AsyncStatisticsResourceWithRawResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get_ddos_attacks = async_to_raw_response_wrapper(
            statistics.get_ddos_attacks,
        )
        self.get_ddos_info = async_to_raw_response_wrapper(
            statistics.get_ddos_info,
        )
        self.get_events_aggregated = async_to_raw_response_wrapper(
            statistics.get_events_aggregated,
        )
        self.get_request_details = async_to_raw_response_wrapper(
            statistics.get_request_details,
        )
        self.get_requests_series = async_to_raw_response_wrapper(
            statistics.get_requests_series,
        )
        self.get_traffic_series = async_to_raw_response_wrapper(
            statistics.get_traffic_series,
        )


class StatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get_ddos_attacks = to_streamed_response_wrapper(
            statistics.get_ddos_attacks,
        )
        self.get_ddos_info = to_streamed_response_wrapper(
            statistics.get_ddos_info,
        )
        self.get_events_aggregated = to_streamed_response_wrapper(
            statistics.get_events_aggregated,
        )
        self.get_request_details = to_streamed_response_wrapper(
            statistics.get_request_details,
        )
        self.get_requests_series = to_streamed_response_wrapper(
            statistics.get_requests_series,
        )
        self.get_traffic_series = to_streamed_response_wrapper(
            statistics.get_traffic_series,
        )


class AsyncStatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get_ddos_attacks = async_to_streamed_response_wrapper(
            statistics.get_ddos_attacks,
        )
        self.get_ddos_info = async_to_streamed_response_wrapper(
            statistics.get_ddos_info,
        )
        self.get_events_aggregated = async_to_streamed_response_wrapper(
            statistics.get_events_aggregated,
        )
        self.get_request_details = async_to_streamed_response_wrapper(
            statistics.get_request_details,
        )
        self.get_requests_series = async_to_streamed_response_wrapper(
            statistics.get_requests_series,
        )
        self.get_traffic_series = async_to_streamed_response_wrapper(
            statistics.get_traffic_series,
        )

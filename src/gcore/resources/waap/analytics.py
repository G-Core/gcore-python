# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.waap import (
    analytics_get_traffic_params,
    analytics_get_requests_params,
    analytics_get_event_statistics_params,
    analytics_get_traffic_filtered_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.waap.waap_request_summary import WaapRequestSummary
from ...types.waap.waap_simple_event_statistics import WaapSimpleEventStatistics
from ...types.waap.analytics_get_traffic_response import AnalyticsGetTrafficResponse
from ...types.waap.analytics_get_traffic_filtered_response import AnalyticsGetTrafficFilteredResponse

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
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
        dimension: Literal["country", "rule", "org", "ip", "useragent", "target"],
        *,
        start: str,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        ips: SequenceNotStr[str] | Omit = omit,
        security_rule_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapSimpleEventStatistics:
        """Retrieves event statistics per given dimension of a request characteristics.

        A
        WAAP _Event_ represents a request observed by the system. The report contains
        the total, blocked, suppressed, and allowed event counts for top ten points in
        the selected dimension.

        Args:
          dimension: A request characteristics dimension

          start: Filter data items starting from a specified date in ISO 8601 format

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          ips: Filter statistics by client IP addresses (max 10).

          security_rule_names: Filter data by name of a security rule matched the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            path_template("/waap/v1/analytics/stats/{dimension}", dimension=dimension),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start": start,
                        "domains": domains,
                        "end": end,
                        "ips": ips,
                        "security_rule_names": security_rule_names,
                    },
                    analytics_get_event_statistics_params.AnalyticsGetEventStatisticsParams,
                ),
            ),
            cast_to=WaapSimpleEventStatistics,
        )

    def get_requests(
        self,
        *,
        start: str,
        countries: SequenceNotStr[str] | Omit = omit,
        decision: List[Literal["blocked", "monitored", "allowed", "passed"]] | Omit = omit,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]] | Omit = omit,
        ips: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        optional_action: List[Literal["captcha", "challenge"]] | Omit = omit,
        ordering: str | Omit = omit,
        path: Optional[str] | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        request_ids: SequenceNotStr[str] | Omit = omit,
        security_rule_names: SequenceNotStr[str] | Omit = omit,
        session_ids: SequenceNotStr[str] | Omit = omit,
        status_codes: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapRequestSummary]:
        """Retrieve request log data over account's domains.

        The log records every request
        passing through WAAP towards the origin server.

        Args:
          start: Filter data items starting from a specified date in ISO 8601 format

          countries: Filter data by a country code of the originating IP address in ISO 3166-1
              alpha-2 format.

          decision: Filter data by decision.

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          http_methods: Filter by HTTP methods

          ips: Filter traffic data by client IP.

          limit: Number of items to return

          offset: Number of items to skip

          optional_action: Filter data by optional action.

          ordering: Sort data by given field.

          path: Filter by URL path with a glob-like pattern.

          reference_ids: Filter data by reference IDs.

          request_ids: Filter data by request IDs.

          security_rule_names: Filter data by name of a security rule matched the request.

          session_ids: Filter data by session IDs.

          status_codes: Filter data by HTTP response status code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v1/analytics/requests",
            page=SyncOffsetPage[WaapRequestSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start": start,
                        "countries": countries,
                        "decision": decision,
                        "domains": domains,
                        "end": end,
                        "http_methods": http_methods,
                        "ips": ips,
                        "limit": limit,
                        "offset": offset,
                        "optional_action": optional_action,
                        "ordering": ordering,
                        "path": path,
                        "reference_ids": reference_ids,
                        "request_ids": request_ids,
                        "security_rule_names": security_rule_names,
                        "session_ids": session_ids,
                        "status_codes": status_codes,
                    },
                    analytics_get_requests_params.AnalyticsGetRequestsParams,
                ),
            ),
            model=WaapRequestSummary,
        )

    def get_traffic(
        self,
        *,
        resolution: Literal["daily", "hourly", "minutely"],
        start: str,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetTrafficResponse:
        """Retrieves a comprehensive report on traffic statistics for a set of domains.

        The
        report includes details such as API requests, blocked events, error counts, and
        many more traffic-related metrics.

        Args:
          resolution: Specifies the granularity of the result data.

          start: Filter data items starting from a specified date in ISO 8601 format

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/waap/v1/analytics/traffic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resolution": resolution,
                        "start": start,
                        "domains": domains,
                        "end": end,
                    },
                    analytics_get_traffic_params.AnalyticsGetTrafficParams,
                ),
            ),
            cast_to=AnalyticsGetTrafficResponse,
        )

    def get_traffic_filtered(
        self,
        *,
        resolution: Literal["daily", "hourly", "minutely"],
        start: str,
        countries: SequenceNotStr[str] | Omit = omit,
        decision: List[Literal["blocked", "monitored", "allowed", "passed"]] | Omit = omit,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]] | Omit = omit,
        ips: SequenceNotStr[str] | Omit = omit,
        optional_action: List[Literal["captcha", "challenge"]] | Omit = omit,
        path: Optional[str] | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        request_ids: SequenceNotStr[str] | Omit = omit,
        security_rule_names: SequenceNotStr[str] | Omit = omit,
        session_ids: SequenceNotStr[str] | Omit = omit,
        status_codes: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetTrafficFilteredResponse:
        """Retrieves a traffic time series data over a set of domains.

        The response is
        suitable for plotting a time series chart. This method allows filtering the
        traffic data by various criteria.

        Args:
          resolution: Specifies the granularity of the result data.

          start: Filter data items starting from a specified date in ISO 8601 format

          countries: Filter data by a country code of the originating IP address in ISO 3166-1
              alpha-2 format.

          decision: Filter data by decision.

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          http_methods: Filter by HTTP methods

          ips: Filter traffic data by client IP.

          optional_action: Filter data by optional action.

          path: Filter by URL path with a glob-like pattern.

          reference_ids: Filter data by reference IDs.

          request_ids: Filter data by request IDs.

          security_rule_names: Filter data by name of a security rule matched the request.

          session_ids: Filter data by session IDs.

          status_codes: Filter data by HTTP response status code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/waap/v1/analytics/traffic-filtered",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resolution": resolution,
                        "start": start,
                        "countries": countries,
                        "decision": decision,
                        "domains": domains,
                        "end": end,
                        "http_methods": http_methods,
                        "ips": ips,
                        "optional_action": optional_action,
                        "path": path,
                        "reference_ids": reference_ids,
                        "request_ids": request_ids,
                        "security_rule_names": security_rule_names,
                        "session_ids": session_ids,
                        "status_codes": status_codes,
                    },
                    analytics_get_traffic_filtered_params.AnalyticsGetTrafficFilteredParams,
                ),
            ),
            cast_to=AnalyticsGetTrafficFilteredResponse,
        )


class AsyncAnalyticsResource(AsyncAPIResource):
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
        dimension: Literal["country", "rule", "org", "ip", "useragent", "target"],
        *,
        start: str,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        ips: SequenceNotStr[str] | Omit = omit,
        security_rule_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapSimpleEventStatistics:
        """Retrieves event statistics per given dimension of a request characteristics.

        A
        WAAP _Event_ represents a request observed by the system. The report contains
        the total, blocked, suppressed, and allowed event counts for top ten points in
        the selected dimension.

        Args:
          dimension: A request characteristics dimension

          start: Filter data items starting from a specified date in ISO 8601 format

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          ips: Filter statistics by client IP addresses (max 10).

          security_rule_names: Filter data by name of a security rule matched the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            path_template("/waap/v1/analytics/stats/{dimension}", dimension=dimension),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start": start,
                        "domains": domains,
                        "end": end,
                        "ips": ips,
                        "security_rule_names": security_rule_names,
                    },
                    analytics_get_event_statistics_params.AnalyticsGetEventStatisticsParams,
                ),
            ),
            cast_to=WaapSimpleEventStatistics,
        )

    def get_requests(
        self,
        *,
        start: str,
        countries: SequenceNotStr[str] | Omit = omit,
        decision: List[Literal["blocked", "monitored", "allowed", "passed"]] | Omit = omit,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]] | Omit = omit,
        ips: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        optional_action: List[Literal["captcha", "challenge"]] | Omit = omit,
        ordering: str | Omit = omit,
        path: Optional[str] | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        request_ids: SequenceNotStr[str] | Omit = omit,
        security_rule_names: SequenceNotStr[str] | Omit = omit,
        session_ids: SequenceNotStr[str] | Omit = omit,
        status_codes: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapRequestSummary, AsyncOffsetPage[WaapRequestSummary]]:
        """Retrieve request log data over account's domains.

        The log records every request
        passing through WAAP towards the origin server.

        Args:
          start: Filter data items starting from a specified date in ISO 8601 format

          countries: Filter data by a country code of the originating IP address in ISO 3166-1
              alpha-2 format.

          decision: Filter data by decision.

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          http_methods: Filter by HTTP methods

          ips: Filter traffic data by client IP.

          limit: Number of items to return

          offset: Number of items to skip

          optional_action: Filter data by optional action.

          ordering: Sort data by given field.

          path: Filter by URL path with a glob-like pattern.

          reference_ids: Filter data by reference IDs.

          request_ids: Filter data by request IDs.

          security_rule_names: Filter data by name of a security rule matched the request.

          session_ids: Filter data by session IDs.

          status_codes: Filter data by HTTP response status code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v1/analytics/requests",
            page=AsyncOffsetPage[WaapRequestSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start": start,
                        "countries": countries,
                        "decision": decision,
                        "domains": domains,
                        "end": end,
                        "http_methods": http_methods,
                        "ips": ips,
                        "limit": limit,
                        "offset": offset,
                        "optional_action": optional_action,
                        "ordering": ordering,
                        "path": path,
                        "reference_ids": reference_ids,
                        "request_ids": request_ids,
                        "security_rule_names": security_rule_names,
                        "session_ids": session_ids,
                        "status_codes": status_codes,
                    },
                    analytics_get_requests_params.AnalyticsGetRequestsParams,
                ),
            ),
            model=WaapRequestSummary,
        )

    async def get_traffic(
        self,
        *,
        resolution: Literal["daily", "hourly", "minutely"],
        start: str,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetTrafficResponse:
        """Retrieves a comprehensive report on traffic statistics for a set of domains.

        The
        report includes details such as API requests, blocked events, error counts, and
        many more traffic-related metrics.

        Args:
          resolution: Specifies the granularity of the result data.

          start: Filter data items starting from a specified date in ISO 8601 format

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/waap/v1/analytics/traffic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "resolution": resolution,
                        "start": start,
                        "domains": domains,
                        "end": end,
                    },
                    analytics_get_traffic_params.AnalyticsGetTrafficParams,
                ),
            ),
            cast_to=AnalyticsGetTrafficResponse,
        )

    async def get_traffic_filtered(
        self,
        *,
        resolution: Literal["daily", "hourly", "minutely"],
        start: str,
        countries: SequenceNotStr[str] | Omit = omit,
        decision: List[Literal["blocked", "monitored", "allowed", "passed"]] | Omit = omit,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]] | Omit = omit,
        ips: SequenceNotStr[str] | Omit = omit,
        optional_action: List[Literal["captcha", "challenge"]] | Omit = omit,
        path: Optional[str] | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        request_ids: SequenceNotStr[str] | Omit = omit,
        security_rule_names: SequenceNotStr[str] | Omit = omit,
        session_ids: SequenceNotStr[str] | Omit = omit,
        status_codes: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetTrafficFilteredResponse:
        """Retrieves a traffic time series data over a set of domains.

        The response is
        suitable for plotting a time series chart. This method allows filtering the
        traffic data by various criteria.

        Args:
          resolution: Specifies the granularity of the result data.

          start: Filter data items starting from a specified date in ISO 8601 format

          countries: Filter data by a country code of the originating IP address in ISO 3166-1
              alpha-2 format.

          decision: Filter data by decision.

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          http_methods: Filter by HTTP methods

          ips: Filter traffic data by client IP.

          optional_action: Filter data by optional action.

          path: Filter by URL path with a glob-like pattern.

          reference_ids: Filter data by reference IDs.

          request_ids: Filter data by request IDs.

          security_rule_names: Filter data by name of a security rule matched the request.

          session_ids: Filter data by session IDs.

          status_codes: Filter data by HTTP response status code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/waap/v1/analytics/traffic-filtered",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "resolution": resolution,
                        "start": start,
                        "countries": countries,
                        "decision": decision,
                        "domains": domains,
                        "end": end,
                        "http_methods": http_methods,
                        "ips": ips,
                        "optional_action": optional_action,
                        "path": path,
                        "reference_ids": reference_ids,
                        "request_ids": request_ids,
                        "security_rule_names": security_rule_names,
                        "session_ids": session_ids,
                        "status_codes": status_codes,
                    },
                    analytics_get_traffic_filtered_params.AnalyticsGetTrafficFilteredParams,
                ),
            ),
            cast_to=AnalyticsGetTrafficFilteredResponse,
        )


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get_event_statistics = to_raw_response_wrapper(
            analytics.get_event_statistics,
        )
        self.get_requests = to_raw_response_wrapper(
            analytics.get_requests,
        )
        self.get_traffic = to_raw_response_wrapper(
            analytics.get_traffic,
        )
        self.get_traffic_filtered = to_raw_response_wrapper(
            analytics.get_traffic_filtered,
        )


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get_event_statistics = async_to_raw_response_wrapper(
            analytics.get_event_statistics,
        )
        self.get_requests = async_to_raw_response_wrapper(
            analytics.get_requests,
        )
        self.get_traffic = async_to_raw_response_wrapper(
            analytics.get_traffic,
        )
        self.get_traffic_filtered = async_to_raw_response_wrapper(
            analytics.get_traffic_filtered,
        )


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get_event_statistics = to_streamed_response_wrapper(
            analytics.get_event_statistics,
        )
        self.get_requests = to_streamed_response_wrapper(
            analytics.get_requests,
        )
        self.get_traffic = to_streamed_response_wrapper(
            analytics.get_traffic,
        )
        self.get_traffic_filtered = to_streamed_response_wrapper(
            analytics.get_traffic_filtered,
        )


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get_event_statistics = async_to_streamed_response_wrapper(
            analytics.get_event_statistics,
        )
        self.get_requests = async_to_streamed_response_wrapper(
            analytics.get_requests,
        )
        self.get_traffic = async_to_streamed_response_wrapper(
            analytics.get_traffic,
        )
        self.get_traffic_filtered = async_to_streamed_response_wrapper(
            analytics.get_traffic_filtered,
        )

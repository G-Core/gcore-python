# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.storage import statistic_get_usage_series_params, statistic_get_usage_aggregated_params
from ...types.storage.usage_total import UsageTotal
from ...types.storage.statistic_get_usage_series_response import StatisticGetUsageSeriesResponse

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

    def get_usage_aggregated(
        self,
        *,
        from_: str | Omit = omit,
        locations: SequenceNotStr[str] | Omit = omit,
        storages: SequenceNotStr[str] | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageTotal:
        """
        Consumption statistics is updated in near real-time as a standard practice.
        However, the frequency of updates can vary, but they are typically available
        within a 60 minutes period. Exceptions, such as maintenance periods, may delay
        data beyond 60 minutes until servers resume and backfill missing statistics.

        Shows storage total usage data in filtered by storages, locations and interval.

        Args:
          from_: a From date filter

          locations: a Locations list of filter

          storages: a Storages list of filter

          to: a To date filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/storage/stats/v1/storage/usage/total",
            body=maybe_transform(
                {
                    "from_": from_,
                    "locations": locations,
                    "storages": storages,
                    "to": to,
                },
                statistic_get_usage_aggregated_params.StatisticGetUsageAggregatedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageTotal,
        )

    def get_usage_series(
        self,
        *,
        from_: str | Omit = omit,
        granularity: str | Omit = omit,
        locations: SequenceNotStr[str] | Omit = omit,
        source: int | Omit = omit,
        storages: SequenceNotStr[str] | Omit = omit,
        to: str | Omit = omit,
        ts_string: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticGetUsageSeriesResponse:
        """
        Consumption statistics is updated in near real-time as a standard practice.
        However, the frequency of updates can vary, but they are typically available
        within a 60 minutes period. Exceptions, such as maintenance periods, may delay
        data beyond 60 minutes until servers resume and backfill missing statistics.

        Shows storage usage data in series format filtered by clients, storages and
        interval.

        Args:
          from_: a From date filter

          granularity: a Granularity is period of time for grouping data Valid values are: 1h, 12h, 24h

          locations: a Locations list of filter

          source: a Source is deprecated parameter

          storages: a Storages list of filter

          to: a To date filter

          ts_string: a TsString is configurator of response time format switch response from unix
              time format to RFC3339 (2006-01-02T15:04:05Z07:00)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/storage/stats/v1/storage/usage/series",
            body=maybe_transform(
                {
                    "from_": from_,
                    "granularity": granularity,
                    "locations": locations,
                    "source": source,
                    "storages": storages,
                    "to": to,
                    "ts_string": ts_string,
                },
                statistic_get_usage_series_params.StatisticGetUsageSeriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatisticGetUsageSeriesResponse,
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

    async def get_usage_aggregated(
        self,
        *,
        from_: str | Omit = omit,
        locations: SequenceNotStr[str] | Omit = omit,
        storages: SequenceNotStr[str] | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageTotal:
        """
        Consumption statistics is updated in near real-time as a standard practice.
        However, the frequency of updates can vary, but they are typically available
        within a 60 minutes period. Exceptions, such as maintenance periods, may delay
        data beyond 60 minutes until servers resume and backfill missing statistics.

        Shows storage total usage data in filtered by storages, locations and interval.

        Args:
          from_: a From date filter

          locations: a Locations list of filter

          storages: a Storages list of filter

          to: a To date filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/storage/stats/v1/storage/usage/total",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "locations": locations,
                    "storages": storages,
                    "to": to,
                },
                statistic_get_usage_aggregated_params.StatisticGetUsageAggregatedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageTotal,
        )

    async def get_usage_series(
        self,
        *,
        from_: str | Omit = omit,
        granularity: str | Omit = omit,
        locations: SequenceNotStr[str] | Omit = omit,
        source: int | Omit = omit,
        storages: SequenceNotStr[str] | Omit = omit,
        to: str | Omit = omit,
        ts_string: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticGetUsageSeriesResponse:
        """
        Consumption statistics is updated in near real-time as a standard practice.
        However, the frequency of updates can vary, but they are typically available
        within a 60 minutes period. Exceptions, such as maintenance periods, may delay
        data beyond 60 minutes until servers resume and backfill missing statistics.

        Shows storage usage data in series format filtered by clients, storages and
        interval.

        Args:
          from_: a From date filter

          granularity: a Granularity is period of time for grouping data Valid values are: 1h, 12h, 24h

          locations: a Locations list of filter

          source: a Source is deprecated parameter

          storages: a Storages list of filter

          to: a To date filter

          ts_string: a TsString is configurator of response time format switch response from unix
              time format to RFC3339 (2006-01-02T15:04:05Z07:00)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/storage/stats/v1/storage/usage/series",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "granularity": granularity,
                    "locations": locations,
                    "source": source,
                    "storages": storages,
                    "to": to,
                    "ts_string": ts_string,
                },
                statistic_get_usage_series_params.StatisticGetUsageSeriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatisticGetUsageSeriesResponse,
        )


class StatisticsResourceWithRawResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get_usage_aggregated = to_raw_response_wrapper(
            statistics.get_usage_aggregated,
        )
        self.get_usage_series = to_raw_response_wrapper(
            statistics.get_usage_series,
        )


class AsyncStatisticsResourceWithRawResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get_usage_aggregated = async_to_raw_response_wrapper(
            statistics.get_usage_aggregated,
        )
        self.get_usage_series = async_to_raw_response_wrapper(
            statistics.get_usage_series,
        )


class StatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get_usage_aggregated = to_streamed_response_wrapper(
            statistics.get_usage_aggregated,
        )
        self.get_usage_series = to_streamed_response_wrapper(
            statistics.get_usage_series,
        )


class AsyncStatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get_usage_aggregated = async_to_streamed_response_wrapper(
            statistics.get_usage_aggregated,
        )
        self.get_usage_series = async_to_streamed_response_wrapper(
            statistics.get_usage_series,
        )

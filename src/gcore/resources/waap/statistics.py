# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.waap import statistic_get_usage_series_params
from ..._base_client import make_request_options
from ...types.waap.waap_statistics_series import WaapStatisticsSeries

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

    def get_usage_series(
        self,
        *,
        from_: Union[str, datetime],
        granularity: Literal["1h", "1d"],
        metrics: List[Literal["total_bytes", "total_requests"]],
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapStatisticsSeries:
        """Retrieve statistics data as a time series.

        The `from` and `to` parameters are
        rounded down and up according to the `granularity`. This means that if the
        `granularity` is set to `1h`, the `from` and `to` parameters will be rounded
        down and up to the nearest hour, respectively. If the `granularity` is set to
        `1d`, the `from` and `to` parameters will be rounded down and up to the nearest
        day, respectively. The response will include explicit 0 values for any missing
        data points.

        Args:
          from_: Beginning of the requested time period (ISO 8601 format, UTC)

          granularity: Duration of the time blocks into which the data will be divided.

          metrics: List of metric types to retrieve statistics for.

          to: End of the requested time period (ISO 8601 format, UTC)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/waap/v1/statistics/series",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "granularity": granularity,
                        "metrics": metrics,
                        "to": to,
                    },
                    statistic_get_usage_series_params.StatisticGetUsageSeriesParams,
                ),
            ),
            cast_to=WaapStatisticsSeries,
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

    async def get_usage_series(
        self,
        *,
        from_: Union[str, datetime],
        granularity: Literal["1h", "1d"],
        metrics: List[Literal["total_bytes", "total_requests"]],
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapStatisticsSeries:
        """Retrieve statistics data as a time series.

        The `from` and `to` parameters are
        rounded down and up according to the `granularity`. This means that if the
        `granularity` is set to `1h`, the `from` and `to` parameters will be rounded
        down and up to the nearest hour, respectively. If the `granularity` is set to
        `1d`, the `from` and `to` parameters will be rounded down and up to the nearest
        day, respectively. The response will include explicit 0 values for any missing
        data points.

        Args:
          from_: Beginning of the requested time period (ISO 8601 format, UTC)

          granularity: Duration of the time blocks into which the data will be divided.

          metrics: List of metric types to retrieve statistics for.

          to: End of the requested time period (ISO 8601 format, UTC)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/waap/v1/statistics/series",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "granularity": granularity,
                        "metrics": metrics,
                        "to": to,
                    },
                    statistic_get_usage_series_params.StatisticGetUsageSeriesParams,
                ),
            ),
            cast_to=WaapStatisticsSeries,
        )


class StatisticsResourceWithRawResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get_usage_series = to_raw_response_wrapper(
            statistics.get_usage_series,
        )


class AsyncStatisticsResourceWithRawResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get_usage_series = async_to_raw_response_wrapper(
            statistics.get_usage_series,
        )


class StatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get_usage_series = to_streamed_response_wrapper(
            statistics.get_usage_series,
        )


class AsyncStatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get_usage_series = async_to_streamed_response_wrapper(
            statistics.get_usage_series,
        )

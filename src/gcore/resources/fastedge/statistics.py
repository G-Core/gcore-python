# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

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
from ..._base_client import make_request_options
from ...types.fastedge import statistic_get_call_series_params, statistic_get_duration_series_params
from ...types.fastedge.statistic_get_call_series_response import StatisticGetCallSeriesResponse
from ...types.fastedge.statistic_get_duration_series_response import StatisticGetDurationSeriesResponse

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

    def get_call_series(
        self,
        *,
        from_: Union[str, datetime],
        step: int,
        to: Union[str, datetime],
        id: int | NotGiven = NOT_GIVEN,
        network: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatisticGetCallSeriesResponse:
        """
        Call statistics

        Args:
          from_: Reporting period start time, RFC3339 format

          step: Reporting granularity, in seconds

          to: Reporting period end time (not included into reporting period), RFC3339 format

          id: App ID

          network: Network name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fastedge/v1/stats/calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "step": step,
                        "to": to,
                        "id": id,
                        "network": network,
                    },
                    statistic_get_call_series_params.StatisticGetCallSeriesParams,
                ),
            ),
            cast_to=StatisticGetCallSeriesResponse,
        )

    def get_duration_series(
        self,
        *,
        from_: Union[str, datetime],
        step: int,
        to: Union[str, datetime],
        id: int | NotGiven = NOT_GIVEN,
        network: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatisticGetDurationSeriesResponse:
        """
        Execution duration statistics

        Args:
          from_: Reporting period start time, RFC3339 format

          step: Reporting granularity, in seconds

          to: Reporting period end time (not included into reporting period), RFC3339 format

          id: App ID

          network: Network name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fastedge/v1/stats/app_duration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "step": step,
                        "to": to,
                        "id": id,
                        "network": network,
                    },
                    statistic_get_duration_series_params.StatisticGetDurationSeriesParams,
                ),
            ),
            cast_to=StatisticGetDurationSeriesResponse,
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

    async def get_call_series(
        self,
        *,
        from_: Union[str, datetime],
        step: int,
        to: Union[str, datetime],
        id: int | NotGiven = NOT_GIVEN,
        network: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatisticGetCallSeriesResponse:
        """
        Call statistics

        Args:
          from_: Reporting period start time, RFC3339 format

          step: Reporting granularity, in seconds

          to: Reporting period end time (not included into reporting period), RFC3339 format

          id: App ID

          network: Network name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fastedge/v1/stats/calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "step": step,
                        "to": to,
                        "id": id,
                        "network": network,
                    },
                    statistic_get_call_series_params.StatisticGetCallSeriesParams,
                ),
            ),
            cast_to=StatisticGetCallSeriesResponse,
        )

    async def get_duration_series(
        self,
        *,
        from_: Union[str, datetime],
        step: int,
        to: Union[str, datetime],
        id: int | NotGiven = NOT_GIVEN,
        network: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatisticGetDurationSeriesResponse:
        """
        Execution duration statistics

        Args:
          from_: Reporting period start time, RFC3339 format

          step: Reporting granularity, in seconds

          to: Reporting period end time (not included into reporting period), RFC3339 format

          id: App ID

          network: Network name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fastedge/v1/stats/app_duration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "step": step,
                        "to": to,
                        "id": id,
                        "network": network,
                    },
                    statistic_get_duration_series_params.StatisticGetDurationSeriesParams,
                ),
            ),
            cast_to=StatisticGetDurationSeriesResponse,
        )


class StatisticsResourceWithRawResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get_call_series = to_raw_response_wrapper(
            statistics.get_call_series,
        )
        self.get_duration_series = to_raw_response_wrapper(
            statistics.get_duration_series,
        )


class AsyncStatisticsResourceWithRawResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get_call_series = async_to_raw_response_wrapper(
            statistics.get_call_series,
        )
        self.get_duration_series = async_to_raw_response_wrapper(
            statistics.get_duration_series,
        )


class StatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get_call_series = to_streamed_response_wrapper(
            statistics.get_call_series,
        )
        self.get_duration_series = to_streamed_response_wrapper(
            statistics.get_duration_series,
        )


class AsyncStatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get_call_series = async_to_streamed_response_wrapper(
            statistics.get_call_series,
        )
        self.get_duration_series = async_to_streamed_response_wrapper(
            statistics.get_duration_series,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ...types.cdn import metric_list_params
from ..._base_client import make_request_options
from ...types.cdn.cdn_metrics import CdnMetrics

__all__ = ["MetricsResource", "AsyncMetricsResource"]


class MetricsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return MetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return MetricsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        from_: str,
        metrics: SequenceNotStr[str],
        to: str,
        filter_by: Iterable[metric_list_params.FilterBy] | Omit = omit,
        granularity: str | Omit = omit,
        group_by: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnMetrics:
        """
        Get CDN metrics

        Args:
          from_: Beginning period to fetch metrics (ISO 8601/RFC 3339 format, UTC.)

              Examples:

              - 2021-06-14T00:00:00Z
              - 2021-06-14T00:00:00.000Z

              The total number of points, which is determined as the difference between "from"
              and "to" divided by "granularity", cannot exceed 1440. Exception: "speed"
              metrics are limited to 72 points.

          metrics:
              Possible values:

              - **`edge_bandwidth`** - Bandwidth from client to CDN (bit/s.)
              - **`edge_requests`** - Number of requests per interval (requests/s.)
              - **`edge_requests_total`** - Total number of requests per interval.
              - **`edge_status_1xx`** - Number of 1xx status codes from edge.
              - **`edge_status_200`** - Number of 200 status codes from edge.
              - **`edge_status_204`** - Number of 204 status codes from edge.
              - **`edge_status_206`** - Number of 206 status codes from edge.
              - **`edge_status_2xx`** - Number of 2xx status codes from edge.
              - **`edge_status_301`** - Number of 301 status codes from edge.
              - **`edge_status_302`** - Number of 302 status codes from edge.
              - **`edge_status_304`** - Number of 304 status codes from edge.
              - **`edge_status_3xx`** - Number of 3xx status codes from edge.
              - **`edge_status_400`** - Number of 400 status codes from edge.
              - **`edge_status_401`** - Number of 401 status codes from edge.
              - **`edge_status_403`** - Number of 403 status codes from edge.
              - **`edge_status_404`** - Number of 404 status codes from edge.
              - **`edge_status_416`** - Number of 416 status codes from edge.
              - **`edge_status_429`** - Number of 429 status codes from edge.
              - **`edge_status_4xx`** - Number of 4xx status codes from edge.
              - **`edge_status_500`** - Number of 500 status codes from edge.
              - **`edge_status_501`** - Number of 501 status codes from edge.
              - **`edge_status_502`** - Number of 502 status codes from edge.
              - **`edge_status_503`** - Number of 503 status codes from edge.
              - **`edge_status_504`** - Number of 504 status codes from edge.
              - **`edge_status_505`** - Number of 505 status codes from edge.
              - **`edge_status_5xx`** - Number of 5xx status codes from edge.
              - **`edge_hit_ratio`** - Percent of cache hits (0.0 - 1.0).
              - **`edge_hit_bytes`** - Number of bytes sent back when cache hits.
              - **`origin_bandwidth`** - Bandwidth from CDN to Origin (bit/s.)
              - **`origin_requests`** - Number of requests per interval (requests/s.)
              - **`origin_status_1xx`** - Number of 1xx status from origin.
              - **`origin_status_200`** - Number of 200 status from origin.
              - **`origin_status_204`** - Number of 204 status from origin.
              - **`origin_status_206`** - Number of 206 status from origin.
              - **`origin_status_2xx`** - Number of 2xx status from origin.
              - **`origin_status_301`** - Number of 301 status from origin.
              - **`origin_status_302`** - Number of 302 status from origin.
              - **`origin_status_304`** - Number of 304 status from origin.
              - **`origin_status_3xx`** - Number of 3xx status from origin.
              - **`origin_status_400`** - Number of 400 status from origin.
              - **`origin_status_401`** - Number of 401 status from origin.
              - **`origin_status_403`** - Number of 403 status from origin.
              - **`origin_status_404`** - Number of 404 status from origin.
              - **`origin_status_416`** - Number of 416 status from origin.
              - **`origin_status_429`** - Number of 426 status from origin.
              - **`origin_status_4xx`** - Number of 4xx status from origin.
              - **`origin_status_500`** - Number of 500 status from origin.
              - **`origin_status_501`** - Number of 501 status from origin.
              - **`origin_status_502`** - Number of 502 status from origin.
              - **`origin_status_503`** - Number of 503 status from origin.
              - **`origin_status_504`** - Number of 504 status from origin.
              - **`origin_status_505`** - Number of 505 status from origin.
              - **`origin_status_5xx`** - Number of 5xx status from origin.
              - **`edge_download_speed`** - Download speed from edge in KB/s (includes only
                requests that status was in the range [200, 300].)
              - **`origin_download_speed`** - Download speed from origin in KB/s (includes
                only requests that status was in the range [200, 300].)

          to: Specifies ending period to fetch metrics (ISO 8601/RFC 3339 format, UTC)

              Examples:

              - 2021-06-15T00:00:00Z
              - 2021-06-15T00:00:00.000Z

              The total number of points, which is determined as the difference between "from"
              and "to" divided by "granularity", cannot exceed 1440. Exception: "speed"
              metrics are limited to 72 points.

          filter_by: Each item represents one filter statement.

          granularity: Duration of the time blocks into which the data is divided. The value must
              correspond to the ISO 8601 period format.

              Examples:

              - P1D
              - PT5M

              Notes:

              - The total number of points, which is determined as the difference between
                "from" and "to" divided by "granularity", cannot exceed 1440. Exception:
                "speed" metrics are limited to 72 points.
              - For "speed" metrics the value must be a multiple of 5.

          group_by: Output data grouping.

              Possible values:

              - **resource** - Data is grouped by CDN resource.
              - **cname** - Data is grouped by common names.
              - **region** – Data is grouped by regions (continents.) Available for "speed"
                metrics only.
              - **isp** - Data is grouped by ISP names. Available for "speed" metrics only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cdn/advanced/v1/metrics",
            body=maybe_transform(
                {
                    "from_": from_,
                    "metrics": metrics,
                    "to": to,
                    "filter_by": filter_by,
                    "granularity": granularity,
                    "group_by": group_by,
                },
                metric_list_params.MetricListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnMetrics,
        )


class AsyncMetricsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncMetricsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        from_: str,
        metrics: SequenceNotStr[str],
        to: str,
        filter_by: Iterable[metric_list_params.FilterBy] | Omit = omit,
        granularity: str | Omit = omit,
        group_by: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnMetrics:
        """
        Get CDN metrics

        Args:
          from_: Beginning period to fetch metrics (ISO 8601/RFC 3339 format, UTC.)

              Examples:

              - 2021-06-14T00:00:00Z
              - 2021-06-14T00:00:00.000Z

              The total number of points, which is determined as the difference between "from"
              and "to" divided by "granularity", cannot exceed 1440. Exception: "speed"
              metrics are limited to 72 points.

          metrics:
              Possible values:

              - **`edge_bandwidth`** - Bandwidth from client to CDN (bit/s.)
              - **`edge_requests`** - Number of requests per interval (requests/s.)
              - **`edge_requests_total`** - Total number of requests per interval.
              - **`edge_status_1xx`** - Number of 1xx status codes from edge.
              - **`edge_status_200`** - Number of 200 status codes from edge.
              - **`edge_status_204`** - Number of 204 status codes from edge.
              - **`edge_status_206`** - Number of 206 status codes from edge.
              - **`edge_status_2xx`** - Number of 2xx status codes from edge.
              - **`edge_status_301`** - Number of 301 status codes from edge.
              - **`edge_status_302`** - Number of 302 status codes from edge.
              - **`edge_status_304`** - Number of 304 status codes from edge.
              - **`edge_status_3xx`** - Number of 3xx status codes from edge.
              - **`edge_status_400`** - Number of 400 status codes from edge.
              - **`edge_status_401`** - Number of 401 status codes from edge.
              - **`edge_status_403`** - Number of 403 status codes from edge.
              - **`edge_status_404`** - Number of 404 status codes from edge.
              - **`edge_status_416`** - Number of 416 status codes from edge.
              - **`edge_status_429`** - Number of 429 status codes from edge.
              - **`edge_status_4xx`** - Number of 4xx status codes from edge.
              - **`edge_status_500`** - Number of 500 status codes from edge.
              - **`edge_status_501`** - Number of 501 status codes from edge.
              - **`edge_status_502`** - Number of 502 status codes from edge.
              - **`edge_status_503`** - Number of 503 status codes from edge.
              - **`edge_status_504`** - Number of 504 status codes from edge.
              - **`edge_status_505`** - Number of 505 status codes from edge.
              - **`edge_status_5xx`** - Number of 5xx status codes from edge.
              - **`edge_hit_ratio`** - Percent of cache hits (0.0 - 1.0).
              - **`edge_hit_bytes`** - Number of bytes sent back when cache hits.
              - **`origin_bandwidth`** - Bandwidth from CDN to Origin (bit/s.)
              - **`origin_requests`** - Number of requests per interval (requests/s.)
              - **`origin_status_1xx`** - Number of 1xx status from origin.
              - **`origin_status_200`** - Number of 200 status from origin.
              - **`origin_status_204`** - Number of 204 status from origin.
              - **`origin_status_206`** - Number of 206 status from origin.
              - **`origin_status_2xx`** - Number of 2xx status from origin.
              - **`origin_status_301`** - Number of 301 status from origin.
              - **`origin_status_302`** - Number of 302 status from origin.
              - **`origin_status_304`** - Number of 304 status from origin.
              - **`origin_status_3xx`** - Number of 3xx status from origin.
              - **`origin_status_400`** - Number of 400 status from origin.
              - **`origin_status_401`** - Number of 401 status from origin.
              - **`origin_status_403`** - Number of 403 status from origin.
              - **`origin_status_404`** - Number of 404 status from origin.
              - **`origin_status_416`** - Number of 416 status from origin.
              - **`origin_status_429`** - Number of 426 status from origin.
              - **`origin_status_4xx`** - Number of 4xx status from origin.
              - **`origin_status_500`** - Number of 500 status from origin.
              - **`origin_status_501`** - Number of 501 status from origin.
              - **`origin_status_502`** - Number of 502 status from origin.
              - **`origin_status_503`** - Number of 503 status from origin.
              - **`origin_status_504`** - Number of 504 status from origin.
              - **`origin_status_505`** - Number of 505 status from origin.
              - **`origin_status_5xx`** - Number of 5xx status from origin.
              - **`edge_download_speed`** - Download speed from edge in KB/s (includes only
                requests that status was in the range [200, 300].)
              - **`origin_download_speed`** - Download speed from origin in KB/s (includes
                only requests that status was in the range [200, 300].)

          to: Specifies ending period to fetch metrics (ISO 8601/RFC 3339 format, UTC)

              Examples:

              - 2021-06-15T00:00:00Z
              - 2021-06-15T00:00:00.000Z

              The total number of points, which is determined as the difference between "from"
              and "to" divided by "granularity", cannot exceed 1440. Exception: "speed"
              metrics are limited to 72 points.

          filter_by: Each item represents one filter statement.

          granularity: Duration of the time blocks into which the data is divided. The value must
              correspond to the ISO 8601 period format.

              Examples:

              - P1D
              - PT5M

              Notes:

              - The total number of points, which is determined as the difference between
                "from" and "to" divided by "granularity", cannot exceed 1440. Exception:
                "speed" metrics are limited to 72 points.
              - For "speed" metrics the value must be a multiple of 5.

          group_by: Output data grouping.

              Possible values:

              - **resource** - Data is grouped by CDN resource.
              - **cname** - Data is grouped by common names.
              - **region** – Data is grouped by regions (continents.) Available for "speed"
                metrics only.
              - **isp** - Data is grouped by ISP names. Available for "speed" metrics only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cdn/advanced/v1/metrics",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "metrics": metrics,
                    "to": to,
                    "filter_by": filter_by,
                    "granularity": granularity,
                    "group_by": group_by,
                },
                metric_list_params.MetricListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnMetrics,
        )


class MetricsResourceWithRawResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.list = to_raw_response_wrapper(
            metrics.list,
        )


class AsyncMetricsResourceWithRawResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.list = async_to_raw_response_wrapper(
            metrics.list,
        )


class MetricsResourceWithStreamingResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.list = to_streamed_response_wrapper(
            metrics.list,
        )


class AsyncMetricsResourceWithStreamingResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.list = async_to_streamed_response_wrapper(
            metrics.list,
        )

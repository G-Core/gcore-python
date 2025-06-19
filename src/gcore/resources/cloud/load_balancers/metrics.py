# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.cloud import InstanceMetricsTimeUnit
from ...._base_client import make_request_options
from ....types.cloud.load_balancers import metric_list_params
from ....types.cloud.instance_metrics_time_unit import InstanceMetricsTimeUnit
from ....types.cloud.load_balancer_metrics_list import LoadBalancerMetricsList

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
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        time_interval: int,
        time_unit: InstanceMetricsTimeUnit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerMetricsList:
        """
        Get load balancer metrics, including cpu, memory and network

        Args:
          time_interval: Time interval

          time_unit: Time interval unit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not loadbalancer_id:
            raise ValueError(f"Expected a non-empty value for `loadbalancer_id` but received {loadbalancer_id!r}")
        return self._post(
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/metrics",
            body=maybe_transform(
                {
                    "time_interval": time_interval,
                    "time_unit": time_unit,
                },
                metric_list_params.MetricListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerMetricsList,
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
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        time_interval: int,
        time_unit: InstanceMetricsTimeUnit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerMetricsList:
        """
        Get load balancer metrics, including cpu, memory and network

        Args:
          time_interval: Time interval

          time_unit: Time interval unit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not loadbalancer_id:
            raise ValueError(f"Expected a non-empty value for `loadbalancer_id` but received {loadbalancer_id!r}")
        return await self._post(
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/metrics",
            body=await async_maybe_transform(
                {
                    "time_interval": time_interval,
                    "time_unit": time_unit,
                },
                metric_list_params.MetricListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerMetricsList,
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

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
from ...types.dns import metric_list_params
from ..._base_client import make_request_options

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
        client_ids: Iterable[int] | Omit = omit,
        zone_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Example of success response:

        ```
        # HELP healthcheck_state The `healthcheck_state` metric reflects the state of a specific monitor after conducting a health check
        # TYPE healthcheck_state gauge
        healthcheck_state{client_id="1",monitor_id="431",monitor_locations="us-east-1,us-west-1",monitor_name="test-monitor-1",monitor_type="http",rrset_name="rrset-name1",rrset_type="rrset-type1",zone_name="zone-name1"} 0
        healthcheck_state{client_id="1",monitor_id="4871",monitor_locations="fr-1,fr-2",monitor_name="test-monitor-2",monitor_type="tcp",rrset_name="rrset-name2",rrset_type="rrset-type2",zone_name="zone-name2"} 1
        healthcheck_state{client_id="2",monitor_id="7123",monitor_locations="ua-1,ua-2",monitor_name="test-monitor-3",monitor_type="icmp",rrset_name="rrset-name3",rrset_type="rrset-type3",zone_name="zone-name3"} 0
        ```

        Args:
          client_ids: Admin and technical user can specify `client_id` to get metrics for particular
              client. Ignored for client

          zone_names: Admin and technical user can specify `monitor_id` to get metrics for particular
              zone. Ignored for client

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "plain/text", **(extra_headers or {})}
        return self._get(
            "/dns/v2/monitor/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client_ids": client_ids,
                        "zone_names": zone_names,
                    },
                    metric_list_params.MetricListParams,
                ),
            ),
            cast_to=str,
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
        client_ids: Iterable[int] | Omit = omit,
        zone_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Example of success response:

        ```
        # HELP healthcheck_state The `healthcheck_state` metric reflects the state of a specific monitor after conducting a health check
        # TYPE healthcheck_state gauge
        healthcheck_state{client_id="1",monitor_id="431",monitor_locations="us-east-1,us-west-1",monitor_name="test-monitor-1",monitor_type="http",rrset_name="rrset-name1",rrset_type="rrset-type1",zone_name="zone-name1"} 0
        healthcheck_state{client_id="1",monitor_id="4871",monitor_locations="fr-1,fr-2",monitor_name="test-monitor-2",monitor_type="tcp",rrset_name="rrset-name2",rrset_type="rrset-type2",zone_name="zone-name2"} 1
        healthcheck_state{client_id="2",monitor_id="7123",monitor_locations="ua-1,ua-2",monitor_name="test-monitor-3",monitor_type="icmp",rrset_name="rrset-name3",rrset_type="rrset-type3",zone_name="zone-name3"} 0
        ```

        Args:
          client_ids: Admin and technical user can specify `client_id` to get metrics for particular
              client. Ignored for client

          zone_names: Admin and technical user can specify `monitor_id` to get metrics for particular
              zone. Ignored for client

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "plain/text", **(extra_headers or {})}
        return await self._get(
            "/dns/v2/monitor/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "client_ids": client_ids,
                        "zone_names": zone_names,
                    },
                    metric_list_params.MetricListParams,
                ),
            ),
            cast_to=str,
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

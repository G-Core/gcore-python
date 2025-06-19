# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....types.cloud import HTTPMethod, LbHealthMonitorType
from ....._base_client import make_request_options
from .....types.cloud.http_method import HTTPMethod
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.load_balancers.pools import health_monitor_create_params
from .....types.cloud.lb_health_monitor_type import LbHealthMonitorType

__all__ = ["HealthMonitorsResource", "AsyncHealthMonitorsResource"]


class HealthMonitorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HealthMonitorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return HealthMonitorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthMonitorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return HealthMonitorsResourceWithStreamingResponse(self)

    def create(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        delay: int,
        max_retries: int,
        api_timeout: int,
        type: LbHealthMonitorType,
        expected_codes: Optional[str] | NotGiven = NOT_GIVEN,
        http_method: Optional[HTTPMethod] | NotGiven = NOT_GIVEN,
        max_retries_down: Optional[int] | NotGiven = NOT_GIVEN,
        url_path: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer pool health monitor

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          delay: The time, in seconds, between sending probes to members

          max_retries: Number of successes before the member is switched to ONLINE state

          api_timeout: The maximum time to connect. Must be less than the delay value

          type: Health monitor type. Once health monitor is created, cannot be changed.

          expected_codes: Can only be used together with `HTTP` or `HTTPS` health monitor type.

          http_method: HTTP method. Can only be used together with `HTTP` or `HTTPS` health monitor
              type.

          max_retries_down: Number of failures before the member is switched to ERROR state.

          url_path: URL Path. Defaults to '/'. Can only be used together with `HTTP` or `HTTPS`
              health monitor type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._post(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor",
            body=maybe_transform(
                {
                    "delay": delay,
                    "max_retries": max_retries,
                    "api_timeout": api_timeout,
                    "type": type,
                    "expected_codes": expected_codes,
                    "http_method": http_method,
                    "max_retries_down": max_retries_down,
                    "url_path": url_path,
                },
                health_monitor_create_params.HealthMonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def delete(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete load balancer pool health monitor

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncHealthMonitorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHealthMonitorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHealthMonitorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthMonitorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncHealthMonitorsResourceWithStreamingResponse(self)

    async def create(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        delay: int,
        max_retries: int,
        api_timeout: int,
        type: LbHealthMonitorType,
        expected_codes: Optional[str] | NotGiven = NOT_GIVEN,
        http_method: Optional[HTTPMethod] | NotGiven = NOT_GIVEN,
        max_retries_down: Optional[int] | NotGiven = NOT_GIVEN,
        url_path: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer pool health monitor

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          delay: The time, in seconds, between sending probes to members

          max_retries: Number of successes before the member is switched to ONLINE state

          api_timeout: The maximum time to connect. Must be less than the delay value

          type: Health monitor type. Once health monitor is created, cannot be changed.

          expected_codes: Can only be used together with `HTTP` or `HTTPS` health monitor type.

          http_method: HTTP method. Can only be used together with `HTTP` or `HTTPS` health monitor
              type.

          max_retries_down: Number of failures before the member is switched to ERROR state.

          url_path: URL Path. Defaults to '/'. Can only be used together with `HTTP` or `HTTPS`
              health monitor type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._post(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor",
            body=await async_maybe_transform(
                {
                    "delay": delay,
                    "max_retries": max_retries,
                    "api_timeout": api_timeout,
                    "type": type,
                    "expected_codes": expected_codes,
                    "http_method": http_method,
                    "max_retries_down": max_retries_down,
                    "url_path": url_path,
                },
                health_monitor_create_params.HealthMonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def delete(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete load balancer pool health monitor

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class HealthMonitorsResourceWithRawResponse:
    def __init__(self, health_monitors: HealthMonitorsResource) -> None:
        self._health_monitors = health_monitors

        self.create = to_raw_response_wrapper(
            health_monitors.create,
        )
        self.delete = to_raw_response_wrapper(
            health_monitors.delete,
        )


class AsyncHealthMonitorsResourceWithRawResponse:
    def __init__(self, health_monitors: AsyncHealthMonitorsResource) -> None:
        self._health_monitors = health_monitors

        self.create = async_to_raw_response_wrapper(
            health_monitors.create,
        )
        self.delete = async_to_raw_response_wrapper(
            health_monitors.delete,
        )


class HealthMonitorsResourceWithStreamingResponse:
    def __init__(self, health_monitors: HealthMonitorsResource) -> None:
        self._health_monitors = health_monitors

        self.create = to_streamed_response_wrapper(
            health_monitors.create,
        )
        self.delete = to_streamed_response_wrapper(
            health_monitors.delete,
        )


class AsyncHealthMonitorsResourceWithStreamingResponse:
    def __init__(self, health_monitors: AsyncHealthMonitorsResource) -> None:
        self._health_monitors = health_monitors

        self.create = async_to_streamed_response_wrapper(
            health_monitors.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            health_monitors.delete,
        )

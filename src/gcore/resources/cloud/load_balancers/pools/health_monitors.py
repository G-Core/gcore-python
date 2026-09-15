# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
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
from .....types.cloud.health_monitor import HealthMonitor
from .....types.cloud.load_balancers.pools import health_monitor_create_params, health_monitor_update_params
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
        admin_state_up: bool | Omit = omit,
        domain_name: Optional[str] | Omit = omit,
        expected_codes: Optional[str] | Omit = omit,
        http_method: Optional[HTTPMethod] | Omit = omit,
        http_version: Optional[Literal["1.0", "1.1"]] | Omit = omit,
        max_retries_down: int | Omit = omit,
        url_path: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Creates a health monitor for a load balancer pool to automatically check the
        health status of pool members. The health monitor performs periodic checks on
        pool members and removes unhealthy members from rotation, ensuring only healthy
        servers receive traffic.

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          delay: The time, in seconds, between sending probes to members

          max_retries: Number of successes before the member is switched to ONLINE state

          api_timeout: The maximum time to connect. Must be less than the delay value

          type: Health monitor type. Once health monitor is created, cannot be changed.

          admin_state_up: Administrative state of the resource. When set to true, the resource is enabled
              and operational. When set to false, the resource is disabled and will not
              process traffic. Defaults to true.

          domain_name: Domain name for HTTP host header. Can only be used together with `HTTP` or
              `HTTPS` health monitor type.

          expected_codes: Expected HTTP response codes. Can be a single code, a comma-separated list of
              codes, or a single range of codes. Can only be used together with `HTTP` or
              `HTTPS` health monitor type. For example, 200, 200,202,401,403,404, or 200-204.
              If not specified, the default is 200.

          http_method: HTTP method. Can only be used together with `HTTP` or `HTTPS` health monitor
              type.

          http_version: HTTP version. Can only be used together with `HTTP` or `HTTPS` health monitor
              type. Supported values: 1.0, 1.1.

          max_retries_down: Number of failures before the member is switched to ERROR state.

          url_path: The HTTP path the health monitor requests on each member. Defaults to `/` if not
              set. Can only be used with `HTTP` or `HTTPS` health monitor type.

              Must start with `/` and contain only plain path segments. Query strings (`?`),
              fragments (`#`), percent-encoding (`%`), and consecutive slashes (`//`) are not
              allowed.

              Examples of valid paths:

              - `/` — check the root (most common, default)
              - `/healthz` — a dedicated health endpoint

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
            path_template(
                "/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor",
                project_id=project_id,
                region_id=region_id,
                pool_id=pool_id,
            ),
            body=maybe_transform(
                {
                    "delay": delay,
                    "max_retries": max_retries,
                    "api_timeout": api_timeout,
                    "type": type,
                    "admin_state_up": admin_state_up,
                    "domain_name": domain_name,
                    "expected_codes": expected_codes,
                    "http_method": http_method,
                    "http_version": http_version,
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

    def update(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        admin_state_up: bool | Omit = omit,
        delay: int | Omit = omit,
        domain_name: Optional[str] | Omit = omit,
        expected_codes: Optional[str] | Omit = omit,
        http_method: Optional[HTTPMethod] | Omit = omit,
        http_version: Optional[Literal["1.0", "1.1"]] | Omit = omit,
        max_retries: int | Omit = omit,
        max_retries_down: int | Omit = omit,
        api_timeout: int | Omit = omit,
        url_path: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Updates the health monitor of a load balancer pool, such as its check intervals,
        timeouts, and the thresholds used to mark pool members as healthy or unhealthy.
        Only the supplied fields are changed. Returns 404 if the pool has no health
        monitor attached. If a provided field already matches the current health monitor
        state it is skipped, and when no field changes anything no task is created and
        an empty task list is returned.

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          admin_state_up: Administrative state of the resource. Omit to leave unchanged; `false` disables
              the resource so it will not process traffic.

          delay: The time, in seconds, between sending probes to members. Omit to leave
              unchanged.

          domain_name: Domain name for HTTP host header. Can only be used together with `HTTP` or
              `HTTPS` health monitor type. Omit to leave unchanged. Set to `null` to clear the
              current value.

          expected_codes: Expected HTTP response codes. Can be a single code, a comma-separated list of
              codes, or a single range of codes. Can only be used together with `HTTP` or
              `HTTPS` health monitor type. For example, 200, 200,202,401,403,404, or 200-204.
              Omit to leave unchanged. Set to `null` to clear the current value.

          http_method: HTTP method. Can only be used together with `HTTP` or `HTTPS` health monitor
              type. Omit to leave unchanged. Set to `null` to clear the current value.

          http_version: HTTP version. Can only be used together with `HTTP` or `HTTPS` health monitor
              type. Supported values: 1.0, 1.1. Omit to leave unchanged. Set to `null` to
              clear the current value.

          max_retries: Number of successes before the member is switched to ONLINE state. Omit to leave
              unchanged.

          max_retries_down: Number of failures before the member is switched to ERROR state. Omit to leave
              unchanged.

          api_timeout: The maximum time to connect. Must be less than the delay value. Omit to leave
              unchanged.

          url_path: The HTTP path the health monitor requests on each member. Can only be used with
              `HTTP` or `HTTPS` health monitor type.

              Must start with `/` and contain only plain path segments. Query strings (`?`),
              fragments (`#`), percent-encoding (`%`), and consecutive slashes (`//`) are not
              allowed.

              Examples of valid paths:

              - `/` — check the root (most common)
              - `/healthz` — a dedicated health endpoint

              Omit to leave unchanged. Set to `null` to clear the current value.

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
        return self._patch(
            path_template(
                "/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor",
                project_id=project_id,
                region_id=region_id,
                pool_id=pool_id,
            ),
            body=maybe_transform(
                {
                    "admin_state_up": admin_state_up,
                    "delay": delay,
                    "domain_name": domain_name,
                    "expected_codes": expected_codes,
                    "http_method": http_method,
                    "http_version": http_version,
                    "max_retries": max_retries,
                    "max_retries_down": max_retries_down,
                    "api_timeout": api_timeout,
                    "url_path": url_path,
                },
                health_monitor_update_params.HealthMonitorUpdateParams,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes the health monitor from a load balancer pool.

        After deletion, the pool
        will no longer perform automatic health checks on its members, and all members
        will remain in rotation regardless of their actual health status.

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
            path_template(
                "/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor",
                project_id=project_id,
                region_id=region_id,
                pool_id=pool_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HealthMonitor:
        """
        Returns the health monitor configured for a load balancer pool, including its
        type, check intervals, timeouts, and the thresholds used to mark pool members as
        healthy or unhealthy. Returns 404 if the pool has no health monitor attached.

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
        return self._get(
            path_template(
                "/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor",
                project_id=project_id,
                region_id=region_id,
                pool_id=pool_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthMonitor,
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
        admin_state_up: bool | Omit = omit,
        domain_name: Optional[str] | Omit = omit,
        expected_codes: Optional[str] | Omit = omit,
        http_method: Optional[HTTPMethod] | Omit = omit,
        http_version: Optional[Literal["1.0", "1.1"]] | Omit = omit,
        max_retries_down: int | Omit = omit,
        url_path: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Creates a health monitor for a load balancer pool to automatically check the
        health status of pool members. The health monitor performs periodic checks on
        pool members and removes unhealthy members from rotation, ensuring only healthy
        servers receive traffic.

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          delay: The time, in seconds, between sending probes to members

          max_retries: Number of successes before the member is switched to ONLINE state

          api_timeout: The maximum time to connect. Must be less than the delay value

          type: Health monitor type. Once health monitor is created, cannot be changed.

          admin_state_up: Administrative state of the resource. When set to true, the resource is enabled
              and operational. When set to false, the resource is disabled and will not
              process traffic. Defaults to true.

          domain_name: Domain name for HTTP host header. Can only be used together with `HTTP` or
              `HTTPS` health monitor type.

          expected_codes: Expected HTTP response codes. Can be a single code, a comma-separated list of
              codes, or a single range of codes. Can only be used together with `HTTP` or
              `HTTPS` health monitor type. For example, 200, 200,202,401,403,404, or 200-204.
              If not specified, the default is 200.

          http_method: HTTP method. Can only be used together with `HTTP` or `HTTPS` health monitor
              type.

          http_version: HTTP version. Can only be used together with `HTTP` or `HTTPS` health monitor
              type. Supported values: 1.0, 1.1.

          max_retries_down: Number of failures before the member is switched to ERROR state.

          url_path: The HTTP path the health monitor requests on each member. Defaults to `/` if not
              set. Can only be used with `HTTP` or `HTTPS` health monitor type.

              Must start with `/` and contain only plain path segments. Query strings (`?`),
              fragments (`#`), percent-encoding (`%`), and consecutive slashes (`//`) are not
              allowed.

              Examples of valid paths:

              - `/` — check the root (most common, default)
              - `/healthz` — a dedicated health endpoint

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
            path_template(
                "/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor",
                project_id=project_id,
                region_id=region_id,
                pool_id=pool_id,
            ),
            body=await async_maybe_transform(
                {
                    "delay": delay,
                    "max_retries": max_retries,
                    "api_timeout": api_timeout,
                    "type": type,
                    "admin_state_up": admin_state_up,
                    "domain_name": domain_name,
                    "expected_codes": expected_codes,
                    "http_method": http_method,
                    "http_version": http_version,
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

    async def update(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        admin_state_up: bool | Omit = omit,
        delay: int | Omit = omit,
        domain_name: Optional[str] | Omit = omit,
        expected_codes: Optional[str] | Omit = omit,
        http_method: Optional[HTTPMethod] | Omit = omit,
        http_version: Optional[Literal["1.0", "1.1"]] | Omit = omit,
        max_retries: int | Omit = omit,
        max_retries_down: int | Omit = omit,
        api_timeout: int | Omit = omit,
        url_path: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Updates the health monitor of a load balancer pool, such as its check intervals,
        timeouts, and the thresholds used to mark pool members as healthy or unhealthy.
        Only the supplied fields are changed. Returns 404 if the pool has no health
        monitor attached. If a provided field already matches the current health monitor
        state it is skipped, and when no field changes anything no task is created and
        an empty task list is returned.

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          admin_state_up: Administrative state of the resource. Omit to leave unchanged; `false` disables
              the resource so it will not process traffic.

          delay: The time, in seconds, between sending probes to members. Omit to leave
              unchanged.

          domain_name: Domain name for HTTP host header. Can only be used together with `HTTP` or
              `HTTPS` health monitor type. Omit to leave unchanged. Set to `null` to clear the
              current value.

          expected_codes: Expected HTTP response codes. Can be a single code, a comma-separated list of
              codes, or a single range of codes. Can only be used together with `HTTP` or
              `HTTPS` health monitor type. For example, 200, 200,202,401,403,404, or 200-204.
              Omit to leave unchanged. Set to `null` to clear the current value.

          http_method: HTTP method. Can only be used together with `HTTP` or `HTTPS` health monitor
              type. Omit to leave unchanged. Set to `null` to clear the current value.

          http_version: HTTP version. Can only be used together with `HTTP` or `HTTPS` health monitor
              type. Supported values: 1.0, 1.1. Omit to leave unchanged. Set to `null` to
              clear the current value.

          max_retries: Number of successes before the member is switched to ONLINE state. Omit to leave
              unchanged.

          max_retries_down: Number of failures before the member is switched to ERROR state. Omit to leave
              unchanged.

          api_timeout: The maximum time to connect. Must be less than the delay value. Omit to leave
              unchanged.

          url_path: The HTTP path the health monitor requests on each member. Can only be used with
              `HTTP` or `HTTPS` health monitor type.

              Must start with `/` and contain only plain path segments. Query strings (`?`),
              fragments (`#`), percent-encoding (`%`), and consecutive slashes (`//`) are not
              allowed.

              Examples of valid paths:

              - `/` — check the root (most common)
              - `/healthz` — a dedicated health endpoint

              Omit to leave unchanged. Set to `null` to clear the current value.

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
        return await self._patch(
            path_template(
                "/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor",
                project_id=project_id,
                region_id=region_id,
                pool_id=pool_id,
            ),
            body=await async_maybe_transform(
                {
                    "admin_state_up": admin_state_up,
                    "delay": delay,
                    "domain_name": domain_name,
                    "expected_codes": expected_codes,
                    "http_method": http_method,
                    "http_version": http_version,
                    "max_retries": max_retries,
                    "max_retries_down": max_retries_down,
                    "api_timeout": api_timeout,
                    "url_path": url_path,
                },
                health_monitor_update_params.HealthMonitorUpdateParams,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes the health monitor from a load balancer pool.

        After deletion, the pool
        will no longer perform automatic health checks on its members, and all members
        will remain in rotation regardless of their actual health status.

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
            path_template(
                "/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor",
                project_id=project_id,
                region_id=region_id,
                pool_id=pool_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HealthMonitor:
        """
        Returns the health monitor configured for a load balancer pool, including its
        type, check intervals, timeouts, and the thresholds used to mark pool members as
        healthy or unhealthy. Returns 404 if the pool has no health monitor attached.

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
        return await self._get(
            path_template(
                "/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor",
                project_id=project_id,
                region_id=region_id,
                pool_id=pool_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthMonitor,
        )


class HealthMonitorsResourceWithRawResponse:
    def __init__(self, health_monitors: HealthMonitorsResource) -> None:
        self._health_monitors = health_monitors

        self.create = to_raw_response_wrapper(
            health_monitors.create,
        )
        self.update = to_raw_response_wrapper(
            health_monitors.update,
        )
        self.delete = to_raw_response_wrapper(
            health_monitors.delete,
        )
        self.get = to_raw_response_wrapper(
            health_monitors.get,
        )


class AsyncHealthMonitorsResourceWithRawResponse:
    def __init__(self, health_monitors: AsyncHealthMonitorsResource) -> None:
        self._health_monitors = health_monitors

        self.create = async_to_raw_response_wrapper(
            health_monitors.create,
        )
        self.update = async_to_raw_response_wrapper(
            health_monitors.update,
        )
        self.delete = async_to_raw_response_wrapper(
            health_monitors.delete,
        )
        self.get = async_to_raw_response_wrapper(
            health_monitors.get,
        )


class HealthMonitorsResourceWithStreamingResponse:
    def __init__(self, health_monitors: HealthMonitorsResource) -> None:
        self._health_monitors = health_monitors

        self.create = to_streamed_response_wrapper(
            health_monitors.create,
        )
        self.update = to_streamed_response_wrapper(
            health_monitors.update,
        )
        self.delete = to_streamed_response_wrapper(
            health_monitors.delete,
        )
        self.get = to_streamed_response_wrapper(
            health_monitors.get,
        )


class AsyncHealthMonitorsResourceWithStreamingResponse:
    def __init__(self, health_monitors: AsyncHealthMonitorsResource) -> None:
        self._health_monitors = health_monitors

        self.create = async_to_streamed_response_wrapper(
            health_monitors.create,
        )
        self.update = async_to_streamed_response_wrapper(
            health_monitors.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            health_monitors.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            health_monitors.get,
        )

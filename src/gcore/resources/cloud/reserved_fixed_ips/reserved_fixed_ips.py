# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, overload

import httpx

from .vip.vip import (
    VipResource,
    AsyncVipResource,
    VipResourceWithRawResponse,
    AsyncVipResourceWithRawResponse,
    VipResourceWithStreamingResponse,
    AsyncVipResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ....types.cloud import (
    InterfaceIPFamily,
    reserved_fixed_ip_list_params,
    reserved_fixed_ip_create_params,
    reserved_fixed_ip_update_params,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.reserved_fixed_ip import ReservedFixedIP
from ....types.cloud.interface_ip_family import InterfaceIPFamily

__all__ = ["ReservedFixedIPsResource", "AsyncReservedFixedIPsResource"]


class ReservedFixedIPsResource(SyncAPIResource):
    @cached_property
    def vip(self) -> VipResource:
        return VipResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReservedFixedIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ReservedFixedIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReservedFixedIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ReservedFixedIPsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        type: Literal["external"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new reserved fixed IP with the specified configuration.

        Args:
          type: Must be 'external'

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        type: Literal["subnet"],
        is_vip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new reserved fixed IP with the specified configuration.

        Args:
          subnet_id: Reserved fixed IP will be allocated in this subnet

          type: Must be 'subnet'.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        network_id: str,
        type: Literal["any_subnet"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new reserved fixed IP with the specified configuration.

        Args:
          network_id: Reserved fixed IP will be allocated in a subnet of this network

          type: Must be '`any_subnet`'.

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ip_address: str,
        network_id: str,
        type: Literal["ip_address"],
        is_vip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new reserved fixed IP with the specified configuration.

        Args:
          ip_address: Reserved fixed IP will be allocated the given IP address

          network_id: Reserved fixed IP will be allocated in a subnet of this network

          type: Must be '`ip_address`'.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        type: Literal["port"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new reserved fixed IP with the specified configuration.

        Args:
          port_id: Port ID to make a reserved fixed IP (for example, `vip_port_id` of the Load
              Balancer entity).

          type: Must be 'port'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["type"],
        ["subnet_id", "type"],
        ["network_id", "type"],
        ["ip_address", "network_id", "type"],
        ["port_id", "type"],
    )
    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        type: Literal["external"] | Literal["subnet"] | Literal["any_subnet"] | Literal["ip_address"] | Literal["port"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        subnet_id: str | Omit = omit,
        network_id: str | Omit = omit,
        ip_address: str | Omit = omit,
        port_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._post(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "type": type,
                    "ip_family": ip_family,
                    "is_vip": is_vip,
                    "subnet_id": subnet_id,
                    "network_id": network_id,
                    "ip_address": ip_address,
                    "port_id": port_id,
                },
                reserved_fixed_ip_create_params.ReservedFixedIPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        is_vip: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReservedFixedIP:
        """
        Update the VIP status of a reserved fixed IP.

        Args:
          is_vip: If reserved fixed IP should be a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return self._patch(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}",
            body=maybe_transform({"is_vip": is_vip}, reserved_fixed_ip_update_params.ReservedFixedIPUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservedFixedIP,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        available_only: bool | Omit = omit,
        device_id: str | Omit = omit,
        external_only: bool | Omit = omit,
        internal_only: bool | Omit = omit,
        ip_address: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        vip_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[ReservedFixedIP]:
        """
        List all reserved fixed IPs in the specified project and region.

        Args:
          available_only: Set to true if the response should only list IP addresses that are not attached
              to any instance

          device_id: Filter IPs by device ID it is attached to

          external_only: Set to true if the response should only list public IP addresses

          internal_only: Set to true if the response should only list private IP addresses

          ip_address: An IPv4 address to filter results by. Regular expression allowed

          limit: Limit the number of returned IPs

          offset: Offset value is used to exclude the first set of records from the result

          order_by: Ordering reserved fixed IP list result by name, status, `updated_at`,
              `created_at` or `fixed_ip_address` fields and directions (status.asc), default
              is "`fixed_ip_address`.asc"

          vip_only: Set to true if the response should only list VIPs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}",
            page=SyncOffsetPage[ReservedFixedIP],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "available_only": available_only,
                        "device_id": device_id,
                        "external_only": external_only,
                        "internal_only": internal_only,
                        "ip_address": ip_address,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "vip_only": vip_only,
                    },
                    reserved_fixed_ip_list_params.ReservedFixedIPListParams,
                ),
            ),
            model=ReservedFixedIP,
        )

    def delete(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete a specific reserved fixed IP and all its associated resources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return self._delete(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReservedFixedIP:
        """
        Get detailed information about a specific reserved fixed IP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return self._get(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservedFixedIP,
        )

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        type: Literal["external"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          type: Must be 'external'

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        type: Literal["subnet"],
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          subnet_id: Reserved fixed IP will be allocated in this subnet

          type: Must be 'subnet'.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        network_id: str,
        type: Literal["any_subnet"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          network_id: Reserved fixed IP will be allocated in a subnet of this network

          type: Must be '`any_subnet`'.

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ip_address: str,
        network_id: str,
        type: Literal["ip_address"],
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          ip_address: Reserved fixed IP will be allocated the given IP address

          network_id: Reserved fixed IP will be allocated in a subnet of this network

          type: Must be '`ip_address`'.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        type: Literal["port"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          port_id: Port ID to make a reserved fixed IP (for example, `vip_port_id` of the Load
              Balancer entity).

          type: Must be 'port'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["type"],
        ["subnet_id", "type"],
        ["network_id", "type"],
        ["ip_address", "network_id", "type"],
        ["port_id", "type"],
    )
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        type: Literal["external"] | Literal["subnet"] | Literal["any_subnet"] | Literal["ip_address"] | Literal["port"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        subnet_id: str | Omit = omit,
        network_id: str | Omit = omit,
        ip_address: str | Omit = omit,
        port_id: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response: TaskIDList = self.create(  # type: ignore
            project_id=project_id,
            region_id=region_id,
            type=type,
            ip_family=ip_family,
            is_vip=is_vip,
            subnet_id=subnet_id,
            network_id=network_id,
            ip_address=ip_address,
            port_id=port_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:  # type: ignore
            raise ValueError("Expected at least one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],  # type: ignore
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            task.created_resources is None
            or task.created_resources.ports is None
            or len(task.created_resources.ports) != 1
        ):
            raise ValueError("Task completed but created_resources or ports is missing or invalid")
        created_port_id = task.created_resources.ports[0]
        return self.get(
            port_id=created_port_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    def delete_and_poll(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete a specific reserved fixed IP and all its associated resources and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            port_id=port_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )


class AsyncReservedFixedIPsResource(AsyncAPIResource):
    @cached_property
    def vip(self) -> AsyncVipResource:
        return AsyncVipResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReservedFixedIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReservedFixedIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReservedFixedIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncReservedFixedIPsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        type: Literal["external"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new reserved fixed IP with the specified configuration.

        Args:
          type: Must be 'external'

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        type: Literal["subnet"],
        is_vip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new reserved fixed IP with the specified configuration.

        Args:
          subnet_id: Reserved fixed IP will be allocated in this subnet

          type: Must be 'subnet'.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        network_id: str,
        type: Literal["any_subnet"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new reserved fixed IP with the specified configuration.

        Args:
          network_id: Reserved fixed IP will be allocated in a subnet of this network

          type: Must be '`any_subnet`'.

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ip_address: str,
        network_id: str,
        type: Literal["ip_address"],
        is_vip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new reserved fixed IP with the specified configuration.

        Args:
          ip_address: Reserved fixed IP will be allocated the given IP address

          network_id: Reserved fixed IP will be allocated in a subnet of this network

          type: Must be '`ip_address`'.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        type: Literal["port"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new reserved fixed IP with the specified configuration.

        Args:
          port_id: Port ID to make a reserved fixed IP (for example, `vip_port_id` of the Load
              Balancer entity).

          type: Must be 'port'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["type"],
        ["subnet_id", "type"],
        ["network_id", "type"],
        ["ip_address", "network_id", "type"],
        ["port_id", "type"],
    )
    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        type: Literal["external"] | Literal["subnet"] | Literal["any_subnet"] | Literal["ip_address"] | Literal["port"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        subnet_id: str | Omit = omit,
        network_id: str | Omit = omit,
        ip_address: str | Omit = omit,
        port_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._post(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "ip_family": ip_family,
                    "is_vip": is_vip,
                    "subnet_id": subnet_id,
                    "network_id": network_id,
                    "ip_address": ip_address,
                    "port_id": port_id,
                },
                reserved_fixed_ip_create_params.ReservedFixedIPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        is_vip: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReservedFixedIP:
        """
        Update the VIP status of a reserved fixed IP.

        Args:
          is_vip: If reserved fixed IP should be a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return await self._patch(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}",
            body=await async_maybe_transform(
                {"is_vip": is_vip}, reserved_fixed_ip_update_params.ReservedFixedIPUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservedFixedIP,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        available_only: bool | Omit = omit,
        device_id: str | Omit = omit,
        external_only: bool | Omit = omit,
        internal_only: bool | Omit = omit,
        ip_address: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        vip_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ReservedFixedIP, AsyncOffsetPage[ReservedFixedIP]]:
        """
        List all reserved fixed IPs in the specified project and region.

        Args:
          available_only: Set to true if the response should only list IP addresses that are not attached
              to any instance

          device_id: Filter IPs by device ID it is attached to

          external_only: Set to true if the response should only list public IP addresses

          internal_only: Set to true if the response should only list private IP addresses

          ip_address: An IPv4 address to filter results by. Regular expression allowed

          limit: Limit the number of returned IPs

          offset: Offset value is used to exclude the first set of records from the result

          order_by: Ordering reserved fixed IP list result by name, status, `updated_at`,
              `created_at` or `fixed_ip_address` fields and directions (status.asc), default
              is "`fixed_ip_address`.asc"

          vip_only: Set to true if the response should only list VIPs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}",
            page=AsyncOffsetPage[ReservedFixedIP],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "available_only": available_only,
                        "device_id": device_id,
                        "external_only": external_only,
                        "internal_only": internal_only,
                        "ip_address": ip_address,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "vip_only": vip_only,
                    },
                    reserved_fixed_ip_list_params.ReservedFixedIPListParams,
                ),
            ),
            model=ReservedFixedIP,
        )

    async def delete(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete a specific reserved fixed IP and all its associated resources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return await self._delete(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReservedFixedIP:
        """
        Get detailed information about a specific reserved fixed IP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return await self._get(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservedFixedIP,
        )

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        type: Literal["external"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          type: Must be 'external'

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        type: Literal["subnet"],
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          subnet_id: Reserved fixed IP will be allocated in this subnet

          type: Must be 'subnet'.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        network_id: str,
        type: Literal["any_subnet"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          network_id: Reserved fixed IP will be allocated in a subnet of this network

          type: Must be '`any_subnet`'.

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ip_address: str,
        network_id: str,
        type: Literal["ip_address"],
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          ip_address: Reserved fixed IP will be allocated the given IP address

          network_id: Reserved fixed IP will be allocated in a subnet of this network

          type: Must be '`ip_address`'.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        type: Literal["port"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          port_id: Port ID to make a reserved fixed IP (for example, `vip_port_id` of the Load
              Balancer entity).

          type: Must be 'port'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["type"],
        ["subnet_id", "type"],
        ["network_id", "type"],
        ["ip_address", "network_id", "type"],
        ["port_id", "type"],
    )
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        type: Literal["external"] | Literal["subnet"] | Literal["any_subnet"] | Literal["ip_address"] | Literal["port"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        subnet_id: str | Omit = omit,
        network_id: str | Omit = omit,
        ip_address: str | Omit = omit,
        port_id: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response: TaskIDList = await self.create(  # type: ignore
            project_id=project_id,
            region_id=region_id,
            type=type,
            ip_family=ip_family,
            is_vip=is_vip,
            subnet_id=subnet_id,
            network_id=network_id,
            ip_address=ip_address,
            port_id=port_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:  # type: ignore
            raise ValueError("Expected at least one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],  # type: ignore
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            task.created_resources is None
            or task.created_resources.ports is None
            or len(task.created_resources.ports) != 1
        ):
            raise ValueError("Task completed but created_resources or ports is missing or invalid")
        created_port_id = task.created_resources.ports[0]
        return await self.get(
            port_id=created_port_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    async def delete_and_poll(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete a specific reserved fixed IP and all its associated resources and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            port_id=port_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )


class ReservedFixedIPsResourceWithRawResponse:
    def __init__(self, reserved_fixed_ips: ReservedFixedIPsResource) -> None:
        self._reserved_fixed_ips = reserved_fixed_ips

        self.create = to_raw_response_wrapper(
            reserved_fixed_ips.create,
        )
        self.update = to_raw_response_wrapper(
            reserved_fixed_ips.update,
        )
        self.list = to_raw_response_wrapper(
            reserved_fixed_ips.list,
        )
        self.delete = to_raw_response_wrapper(
            reserved_fixed_ips.delete,
        )
        self.get = to_raw_response_wrapper(
            reserved_fixed_ips.get,
        )
        self.create_and_poll = to_raw_response_wrapper(
            reserved_fixed_ips.create_and_poll,
        )
        self.delete_and_poll = to_raw_response_wrapper(
            reserved_fixed_ips.delete_and_poll,
        )

    @cached_property
    def vip(self) -> VipResourceWithRawResponse:
        return VipResourceWithRawResponse(self._reserved_fixed_ips.vip)


class AsyncReservedFixedIPsResourceWithRawResponse:
    def __init__(self, reserved_fixed_ips: AsyncReservedFixedIPsResource) -> None:
        self._reserved_fixed_ips = reserved_fixed_ips

        self.create = async_to_raw_response_wrapper(
            reserved_fixed_ips.create,
        )
        self.update = async_to_raw_response_wrapper(
            reserved_fixed_ips.update,
        )
        self.list = async_to_raw_response_wrapper(
            reserved_fixed_ips.list,
        )
        self.delete = async_to_raw_response_wrapper(
            reserved_fixed_ips.delete,
        )
        self.get = async_to_raw_response_wrapper(
            reserved_fixed_ips.get,
        )
        self.create_and_poll = async_to_raw_response_wrapper(
            reserved_fixed_ips.create_and_poll,
        )
        self.delete_and_poll = async_to_raw_response_wrapper(
            reserved_fixed_ips.delete_and_poll,
        )

    @cached_property
    def vip(self) -> AsyncVipResourceWithRawResponse:
        return AsyncVipResourceWithRawResponse(self._reserved_fixed_ips.vip)


class ReservedFixedIPsResourceWithStreamingResponse:
    def __init__(self, reserved_fixed_ips: ReservedFixedIPsResource) -> None:
        self._reserved_fixed_ips = reserved_fixed_ips

        self.create = to_streamed_response_wrapper(
            reserved_fixed_ips.create,
        )
        self.update = to_streamed_response_wrapper(
            reserved_fixed_ips.update,
        )
        self.list = to_streamed_response_wrapper(
            reserved_fixed_ips.list,
        )
        self.delete = to_streamed_response_wrapper(
            reserved_fixed_ips.delete,
        )
        self.get = to_streamed_response_wrapper(
            reserved_fixed_ips.get,
        )
        self.create_and_poll = to_streamed_response_wrapper(
            reserved_fixed_ips.create_and_poll,
        )
        self.delete_and_poll = to_streamed_response_wrapper(
            reserved_fixed_ips.delete_and_poll,
        )

    @cached_property
    def vip(self) -> VipResourceWithStreamingResponse:
        return VipResourceWithStreamingResponse(self._reserved_fixed_ips.vip)


class AsyncReservedFixedIPsResourceWithStreamingResponse:
    def __init__(self, reserved_fixed_ips: AsyncReservedFixedIPsResource) -> None:
        self._reserved_fixed_ips = reserved_fixed_ips

        self.create = async_to_streamed_response_wrapper(
            reserved_fixed_ips.create,
        )
        self.update = async_to_streamed_response_wrapper(
            reserved_fixed_ips.update,
        )
        self.list = async_to_streamed_response_wrapper(
            reserved_fixed_ips.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            reserved_fixed_ips.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            reserved_fixed_ips.get,
        )
        self.create_and_poll = async_to_streamed_response_wrapper(
            reserved_fixed_ips.create_and_poll,
        )
        self.delete_and_poll = async_to_streamed_response_wrapper(
            reserved_fixed_ips.delete_and_poll,
        )

    @cached_property
    def vip(self) -> AsyncVipResourceWithStreamingResponse:
        return AsyncVipResourceWithStreamingResponse(self._reserved_fixed_ips.vip)

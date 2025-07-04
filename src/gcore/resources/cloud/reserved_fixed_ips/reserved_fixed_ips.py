# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, overload

import httpx

from .vip import (
    VipResource,
    AsyncVipResource,
    VipResourceWithRawResponse,
    AsyncVipResourceWithRawResponse,
    VipResourceWithStreamingResponse,
    AsyncVipResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.cloud import InterfaceIPFamily, reserved_fixed_ip_list_params, reserved_fixed_ip_create_params
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
        ip_family: Optional[InterfaceIPFamily] | NotGiven = NOT_GIVEN,
        is_vip: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        is_vip: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        ip_family: Optional[InterfaceIPFamily] | NotGiven = NOT_GIVEN,
        is_vip: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        is_vip: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        ip_family: Optional[InterfaceIPFamily] | NotGiven = NOT_GIVEN,
        is_vip: bool | NotGiven = NOT_GIVEN,
        subnet_id: str | NotGiven = NOT_GIVEN,
        network_id: str | NotGiven = NOT_GIVEN,
        ip_address: str | NotGiven = NOT_GIVEN,
        port_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        available_only: bool | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        external_only: bool | NotGiven = NOT_GIVEN,
        internal_only: bool | NotGiven = NOT_GIVEN,
        ip_address: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        vip_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        ip_family: Optional[InterfaceIPFamily] | NotGiven = NOT_GIVEN,
        is_vip: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        is_vip: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        ip_family: Optional[InterfaceIPFamily] | NotGiven = NOT_GIVEN,
        is_vip: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        is_vip: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        ip_family: Optional[InterfaceIPFamily] | NotGiven = NOT_GIVEN,
        is_vip: bool | NotGiven = NOT_GIVEN,
        subnet_id: str | NotGiven = NOT_GIVEN,
        network_id: str | NotGiven = NOT_GIVEN,
        ip_address: str | NotGiven = NOT_GIVEN,
        port_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        available_only: bool | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        external_only: bool | NotGiven = NOT_GIVEN,
        internal_only: bool | NotGiven = NOT_GIVEN,
        ip_address: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        vip_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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


class ReservedFixedIPsResourceWithRawResponse:
    def __init__(self, reserved_fixed_ips: ReservedFixedIPsResource) -> None:
        self._reserved_fixed_ips = reserved_fixed_ips

        self.create = to_raw_response_wrapper(
            reserved_fixed_ips.create,
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

    @cached_property
    def vip(self) -> VipResourceWithRawResponse:
        return VipResourceWithRawResponse(self._reserved_fixed_ips.vip)


class AsyncReservedFixedIPsResourceWithRawResponse:
    def __init__(self, reserved_fixed_ips: AsyncReservedFixedIPsResource) -> None:
        self._reserved_fixed_ips = reserved_fixed_ips

        self.create = async_to_raw_response_wrapper(
            reserved_fixed_ips.create,
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

    @cached_property
    def vip(self) -> AsyncVipResourceWithRawResponse:
        return AsyncVipResourceWithRawResponse(self._reserved_fixed_ips.vip)


class ReservedFixedIPsResourceWithStreamingResponse:
    def __init__(self, reserved_fixed_ips: ReservedFixedIPsResource) -> None:
        self._reserved_fixed_ips = reserved_fixed_ips

        self.create = to_streamed_response_wrapper(
            reserved_fixed_ips.create,
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

    @cached_property
    def vip(self) -> VipResourceWithStreamingResponse:
        return VipResourceWithStreamingResponse(self._reserved_fixed_ips.vip)


class AsyncReservedFixedIPsResourceWithStreamingResponse:
    def __init__(self, reserved_fixed_ips: AsyncReservedFixedIPsResource) -> None:
        self._reserved_fixed_ips = reserved_fixed_ips

        self.create = async_to_streamed_response_wrapper(
            reserved_fixed_ips.create,
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

    @cached_property
    def vip(self) -> AsyncVipResourceWithStreamingResponse:
        return AsyncVipResourceWithStreamingResponse(self._reserved_fixed_ips.vip)

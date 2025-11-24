# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ....types.cloud import IPVersion
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.subnet import Subnet
from ....types.cloud.networks import subnet_list_params, subnet_create_params, subnet_update_params
from ....types.cloud.ip_version import IPVersion
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.tag_update_map_param import TagUpdateMapParam

__all__ = ["SubnetsResource", "AsyncSubnetsResource"]


class SubnetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubnetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return SubnetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubnetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return SubnetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cidr: str,
        name: str,
        network_id: str,
        connect_to_network_router: bool | Omit = omit,
        dns_nameservers: Optional[SequenceNotStr[str]] | Omit = omit,
        enable_dhcp: bool | Omit = omit,
        gateway_ip: Optional[str] | Omit = omit,
        host_routes: Optional[Iterable[subnet_create_params.HostRoute]] | Omit = omit,
        ip_version: IPVersion | Omit = omit,
        router_id_to_connect: Optional[str] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create subnet

        Args:
          project_id: Project ID

          region_id: Region ID

          cidr: CIDR

          name: Subnet name

          network_id: Network ID

          connect_to_network_router: True if the network's router should get a gateway in this subnet. Must be
              explicitly 'false' when `gateway_ip` is null.

          dns_nameservers: List IP addresses of DNS servers to advertise via DHCP.

          enable_dhcp: True if DHCP should be enabled

          gateway_ip: Default GW IPv4 address to advertise in DHCP routes in this subnet. Omit this
              field to let the cloud backend allocate it automatically. Set to null if no
              gateway must be advertised by this subnet's DHCP (useful when attaching
              instances to multiple subnets in order to prevent default route conflicts).

          host_routes: List of custom static routes to advertise via DHCP.

          ip_version: IP version

          router_id_to_connect: ID of the router to connect to. Requires `connect_to_network_router` set to
              true. If not specified, attempts to find a router created during network
              creation.

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._post(
            f"/cloud/v1/subnets/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "cidr": cidr,
                    "name": name,
                    "network_id": network_id,
                    "connect_to_network_router": connect_to_network_router,
                    "dns_nameservers": dns_nameservers,
                    "enable_dhcp": enable_dhcp,
                    "gateway_ip": gateway_ip,
                    "host_routes": host_routes,
                    "ip_version": ip_version,
                    "router_id_to_connect": router_id_to_connect,
                    "tags": tags,
                },
                subnet_create_params.SubnetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cidr: str,
        name: str,
        network_id: str,
        connect_to_network_router: bool | Omit = omit,
        dns_nameservers: Optional[SequenceNotStr[str]] | Omit = omit,
        enable_dhcp: bool | Omit = omit,
        gateway_ip: Optional[str] | Omit = omit,
        host_routes: Optional[Iterable[subnet_create_params.HostRoute]] | Omit = omit,
        ip_version: IPVersion | Omit = omit,
        router_id_to_connect: Optional[str] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subnet:
        """Create subnet and poll for the result."""
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            cidr=cidr,
            name=name,
            network_id=network_id,
            connect_to_network_router=connect_to_network_router,
            dns_nameservers=dns_nameservers,
            enable_dhcp=enable_dhcp,
            gateway_ip=gateway_ip,
            host_routes=host_routes,
            ip_version=ip_version,
            router_id_to_connect=router_id_to_connect,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError(f"Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.subnets or len(task.created_resources.subnets) != 1:
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return self.get(
            subnet_id=task.created_resources.subnets[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
        )

    def update(
        self,
        subnet_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        dns_nameservers: Optional[SequenceNotStr[str]] | Omit = omit,
        enable_dhcp: Optional[bool] | Omit = omit,
        gateway_ip: Optional[str] | Omit = omit,
        host_routes: Optional[Iterable[subnet_update_params.HostRoute]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subnet:
        """
        Update subnet

        Args:
          project_id: Project ID

          region_id: Region ID

          subnet_id: Subnet ID

          dns_nameservers: List IP addresses of DNS servers to advertise via DHCP.

          enable_dhcp: True if DHCP should be enabled

          gateway_ip: Default GW IPv4 address to advertise in DHCP routes in this subnet. Omit this
              field to let the cloud backend allocate it automatically. Set to null if no
              gateway must be advertised by this subnet's DHCP (useful when attaching
              instances to multiple subnets in order to prevent default route conflicts).

          host_routes: List of custom static routes to advertise via DHCP.

          name: Name

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
              key-value pairs to add or update tags. Set tag values to `null` to remove tags.
              Unspecified tags remain unchanged. Read-only tags are always preserved and
              cannot be modified.

              **Examples:**

              - **Add/update tags:**
                `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
                updates existing ones.

              - **Delete tags:** `{'tags': {'old_tag': null}}` removes specific tags.

              - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
                tags are preserved).

              - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
                specified tags.

              - **Mixed operations:**
                `{'tags': {'environment': 'production', 'cost_center': 'engineering', 'deprecated_tag': null}}`
                adds/updates 'environment' and '`cost_center`' while removing
                '`deprecated_tag`', preserving other existing tags.

              - **Replace all:** first delete existing tags with null values, then add new
                ones in the same request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        return self._patch(
            f"/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}",
            body=maybe_transform(
                {
                    "dns_nameservers": dns_nameservers,
                    "enable_dhcp": enable_dhcp,
                    "gateway_ip": gateway_ip,
                    "host_routes": host_routes,
                    "name": name,
                    "tags": tags,
                },
                subnet_update_params.SubnetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subnet,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        network_id: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal[
            "available_ips.asc",
            "available_ips.desc",
            "cidr.asc",
            "cidr.desc",
            "created_at.asc",
            "created_at.desc",
            "name.asc",
            "name.desc",
            "total_ips.asc",
            "total_ips.desc",
            "updated_at.asc",
            "updated_at.desc",
        ]
        | Omit = omit,
        tag_key: SequenceNotStr[str] | Omit = omit,
        tag_key_value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[Subnet]:
        """
        List subnets

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Optional. Limit the number of returned items

          network_id: Only list subnets of this network

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          order_by: Ordering subnets list result by `name`, `created_at`, `updated_at`,
              `available_ips`, `total_ips`, and `cidr` (default) fields of the subnet and
              directions (`name.asc`).

          tag_key: Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2

          tag_key_value: Optional. Filter by tag key-value pairs.

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
            f"/cloud/v1/subnets/{project_id}/{region_id}",
            page=SyncOffsetPage[Subnet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "network_id": network_id,
                        "offset": offset,
                        "order_by": order_by,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                    },
                    subnet_list_params.SubnetListParams,
                ),
            ),
            model=Subnet,
        )

    def delete(
        self,
        subnet_id: str,
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
        Delete subnet

        Args:
          project_id: Project ID

          region_id: Region ID

          subnet_id: Subnet ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        return self._delete(
            f"/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        subnet_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subnet:
        """
        Get subnet

        Args:
          project_id: Project ID

          region_id: Region ID

          subnet_id: Subnet ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        return self._get(
            f"/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subnet,
        )


class AsyncSubnetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubnetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubnetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubnetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncSubnetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cidr: str,
        name: str,
        network_id: str,
        connect_to_network_router: bool | Omit = omit,
        dns_nameservers: Optional[SequenceNotStr[str]] | Omit = omit,
        enable_dhcp: bool | Omit = omit,
        gateway_ip: Optional[str] | Omit = omit,
        host_routes: Optional[Iterable[subnet_create_params.HostRoute]] | Omit = omit,
        ip_version: IPVersion | Omit = omit,
        router_id_to_connect: Optional[str] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create subnet

        Args:
          project_id: Project ID

          region_id: Region ID

          cidr: CIDR

          name: Subnet name

          network_id: Network ID

          connect_to_network_router: True if the network's router should get a gateway in this subnet. Must be
              explicitly 'false' when `gateway_ip` is null.

          dns_nameservers: List IP addresses of DNS servers to advertise via DHCP.

          enable_dhcp: True if DHCP should be enabled

          gateway_ip: Default GW IPv4 address to advertise in DHCP routes in this subnet. Omit this
              field to let the cloud backend allocate it automatically. Set to null if no
              gateway must be advertised by this subnet's DHCP (useful when attaching
              instances to multiple subnets in order to prevent default route conflicts).

          host_routes: List of custom static routes to advertise via DHCP.

          ip_version: IP version

          router_id_to_connect: ID of the router to connect to. Requires `connect_to_network_router` set to
              true. If not specified, attempts to find a router created during network
              creation.

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._post(
            f"/cloud/v1/subnets/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "cidr": cidr,
                    "name": name,
                    "network_id": network_id,
                    "connect_to_network_router": connect_to_network_router,
                    "dns_nameservers": dns_nameservers,
                    "enable_dhcp": enable_dhcp,
                    "gateway_ip": gateway_ip,
                    "host_routes": host_routes,
                    "ip_version": ip_version,
                    "router_id_to_connect": router_id_to_connect,
                    "tags": tags,
                },
                subnet_create_params.SubnetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cidr: str,
        name: str,
        network_id: str,
        connect_to_network_router: bool | Omit = omit,
        dns_nameservers: Optional[SequenceNotStr[str]] | Omit = omit,
        enable_dhcp: bool | Omit = omit,
        gateway_ip: Optional[str] | Omit = omit,
        host_routes: Optional[Iterable[subnet_create_params.HostRoute]] | Omit = omit,
        ip_version: IPVersion | Omit = omit,
        router_id_to_connect: Optional[str] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subnet:
        """Create subnet and poll for the result."""
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            cidr=cidr,
            name=name,
            network_id=network_id,
            connect_to_network_router=connect_to_network_router,
            dns_nameservers=dns_nameservers,
            enable_dhcp=enable_dhcp,
            gateway_ip=gateway_ip,
            host_routes=host_routes,
            ip_version=ip_version,
            router_id_to_connect=router_id_to_connect,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError(f"Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.subnets or len(task.created_resources.subnets) != 1:
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return await self.get(
            subnet_id=task.created_resources.subnets[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
        )

    async def update(
        self,
        subnet_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        dns_nameservers: Optional[SequenceNotStr[str]] | Omit = omit,
        enable_dhcp: Optional[bool] | Omit = omit,
        gateway_ip: Optional[str] | Omit = omit,
        host_routes: Optional[Iterable[subnet_update_params.HostRoute]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subnet:
        """
        Update subnet

        Args:
          project_id: Project ID

          region_id: Region ID

          subnet_id: Subnet ID

          dns_nameservers: List IP addresses of DNS servers to advertise via DHCP.

          enable_dhcp: True if DHCP should be enabled

          gateway_ip: Default GW IPv4 address to advertise in DHCP routes in this subnet. Omit this
              field to let the cloud backend allocate it automatically. Set to null if no
              gateway must be advertised by this subnet's DHCP (useful when attaching
              instances to multiple subnets in order to prevent default route conflicts).

          host_routes: List of custom static routes to advertise via DHCP.

          name: Name

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
              key-value pairs to add or update tags. Set tag values to `null` to remove tags.
              Unspecified tags remain unchanged. Read-only tags are always preserved and
              cannot be modified.

              **Examples:**

              - **Add/update tags:**
                `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
                updates existing ones.

              - **Delete tags:** `{'tags': {'old_tag': null}}` removes specific tags.

              - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
                tags are preserved).

              - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
                specified tags.

              - **Mixed operations:**
                `{'tags': {'environment': 'production', 'cost_center': 'engineering', 'deprecated_tag': null}}`
                adds/updates 'environment' and '`cost_center`' while removing
                '`deprecated_tag`', preserving other existing tags.

              - **Replace all:** first delete existing tags with null values, then add new
                ones in the same request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        return await self._patch(
            f"/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}",
            body=await async_maybe_transform(
                {
                    "dns_nameservers": dns_nameservers,
                    "enable_dhcp": enable_dhcp,
                    "gateway_ip": gateway_ip,
                    "host_routes": host_routes,
                    "name": name,
                    "tags": tags,
                },
                subnet_update_params.SubnetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subnet,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        network_id: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal[
            "available_ips.asc",
            "available_ips.desc",
            "cidr.asc",
            "cidr.desc",
            "created_at.asc",
            "created_at.desc",
            "name.asc",
            "name.desc",
            "total_ips.asc",
            "total_ips.desc",
            "updated_at.asc",
            "updated_at.desc",
        ]
        | Omit = omit,
        tag_key: SequenceNotStr[str] | Omit = omit,
        tag_key_value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Subnet, AsyncOffsetPage[Subnet]]:
        """
        List subnets

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Optional. Limit the number of returned items

          network_id: Only list subnets of this network

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          order_by: Ordering subnets list result by `name`, `created_at`, `updated_at`,
              `available_ips`, `total_ips`, and `cidr` (default) fields of the subnet and
              directions (`name.asc`).

          tag_key: Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2

          tag_key_value: Optional. Filter by tag key-value pairs.

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
            f"/cloud/v1/subnets/{project_id}/{region_id}",
            page=AsyncOffsetPage[Subnet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "network_id": network_id,
                        "offset": offset,
                        "order_by": order_by,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                    },
                    subnet_list_params.SubnetListParams,
                ),
            ),
            model=Subnet,
        )

    async def delete(
        self,
        subnet_id: str,
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
        Delete subnet

        Args:
          project_id: Project ID

          region_id: Region ID

          subnet_id: Subnet ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        return await self._delete(
            f"/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        subnet_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subnet:
        """
        Get subnet

        Args:
          project_id: Project ID

          region_id: Region ID

          subnet_id: Subnet ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        return await self._get(
            f"/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subnet,
        )


class SubnetsResourceWithRawResponse:
    def __init__(self, subnets: SubnetsResource) -> None:
        self._subnets = subnets

        self.create = to_raw_response_wrapper(
            subnets.create,
        )
        self.create_and_poll = to_raw_response_wrapper(
            subnets.create_and_poll,
        )
        self.update = to_raw_response_wrapper(
            subnets.update,
        )
        self.list = to_raw_response_wrapper(
            subnets.list,
        )
        self.delete = to_raw_response_wrapper(
            subnets.delete,
        )
        self.get = to_raw_response_wrapper(
            subnets.get,
        )


class AsyncSubnetsResourceWithRawResponse:
    def __init__(self, subnets: AsyncSubnetsResource) -> None:
        self._subnets = subnets

        self.create = async_to_raw_response_wrapper(
            subnets.create,
        )
        self.create_and_poll = async_to_raw_response_wrapper(
            subnets.create_and_poll,
        )
        self.update = async_to_raw_response_wrapper(
            subnets.update,
        )
        self.list = async_to_raw_response_wrapper(
            subnets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            subnets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            subnets.get,
        )


class SubnetsResourceWithStreamingResponse:
    def __init__(self, subnets: SubnetsResource) -> None:
        self._subnets = subnets

        self.create = to_streamed_response_wrapper(
            subnets.create,
        )
        self.create_and_poll = to_streamed_response_wrapper(
            subnets.create_and_poll,
        )
        self.update = to_streamed_response_wrapper(
            subnets.update,
        )
        self.list = to_streamed_response_wrapper(
            subnets.list,
        )
        self.delete = to_streamed_response_wrapper(
            subnets.delete,
        )
        self.get = to_streamed_response_wrapper(
            subnets.get,
        )


class AsyncSubnetsResourceWithStreamingResponse:
    def __init__(self, subnets: AsyncSubnetsResource) -> None:
        self._subnets = subnets

        self.create = async_to_streamed_response_wrapper(
            subnets.create,
        )
        self.create_and_poll = async_to_streamed_response_wrapper(
            subnets.create_and_poll,
        )
        self.update = async_to_streamed_response_wrapper(
            subnets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            subnets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            subnets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            subnets.get,
        )

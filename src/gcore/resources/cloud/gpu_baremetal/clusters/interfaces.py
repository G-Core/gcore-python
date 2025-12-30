# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.gpu_baremetal.clusters import interface_attach_params, interface_detach_params
from .....types.cloud.network_interface_list import NetworkInterfaceList

__all__ = ["InterfacesResource", "AsyncInterfacesResource"]


class InterfacesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InterfacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return InterfacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InterfacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return InterfacesResourceWithStreamingResponse(self)

    def list(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkInterfaceList:
        """
        Retrieve a list of network interfaces attached to the GPU cluster servers.

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
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return self._get(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{cluster_id}/interfaces",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkInterfaceList,
        )

    @overload
    def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ddos_profile: interface_attach_params.NewInterfaceExternalExtendSchemaWithDDOSDDOSProfile | Omit = omit,
        interface_name: str | Omit = omit,
        ip_family: Literal["dual", "ipv4", "ipv6"] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Iterable[interface_attach_params.NewInterfaceExternalExtendSchemaWithDDOSSecurityGroup]
        | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to bare metal GPU cluster server

        Args:
          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          port_group: Each group will be added to the separate trunk.

          security_groups: List of security group IDs

          type: Must be 'external'. Union tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        ddos_profile: interface_attach_params.NewInterfaceSpecificSubnetSchemaDDOSProfile | Omit = omit,
        interface_name: str | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Iterable[interface_attach_params.NewInterfaceSpecificSubnetSchemaSecurityGroup] | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to bare metal GPU cluster server

        Args:
          subnet_id: Port will get an IP address from this subnet

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name

          port_group: Each group will be added to the separate trunk.

          security_groups: List of security group IDs

          type: Must be 'subnet'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        network_id: str,
        ddos_profile: interface_attach_params.NewInterfaceAnySubnetSchemaDDOSProfile | Omit = omit,
        interface_name: str | Omit = omit,
        ip_family: Literal["dual", "ipv4", "ipv6"] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Iterable[interface_attach_params.NewInterfaceAnySubnetSchemaSecurityGroup] | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to bare metal GPU cluster server

        Args:
          network_id: Port will get an IP address in this network subnet

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          port_group: Each group will be added to the separate trunk.

          security_groups: List of security group IDs

          type: Must be '`any_subnet`'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        ddos_profile: interface_attach_params.NewInterfaceReservedFixedIPSchemaDDOSProfile | Omit = omit,
        interface_name: str | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Iterable[interface_attach_params.NewInterfaceReservedFixedIPSchemaSecurityGroup] | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to bare metal GPU cluster server

        Args:
          port_id: Port ID

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name

          port_group: Each group will be added to the separate trunk.

          security_groups: List of security group IDs

          type: Must be '`reserved_fixed_ip`'. Union tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ddos_profile: interface_attach_params.NewInterfaceExternalExtendSchemaWithDDOSDDOSProfile
        | interface_attach_params.NewInterfaceSpecificSubnetSchemaDDOSProfile
        | interface_attach_params.NewInterfaceAnySubnetSchemaDDOSProfile
        | interface_attach_params.NewInterfaceReservedFixedIPSchemaDDOSProfile
        | Omit = omit,
        interface_name: str | Omit = omit,
        ip_family: Literal["dual", "ipv4", "ipv6"] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Iterable[interface_attach_params.NewInterfaceExternalExtendSchemaWithDDOSSecurityGroup]
        | Iterable[interface_attach_params.NewInterfaceSpecificSubnetSchemaSecurityGroup]
        | Iterable[interface_attach_params.NewInterfaceAnySubnetSchemaSecurityGroup]
        | Iterable[interface_attach_params.NewInterfaceReservedFixedIPSchemaSecurityGroup]
        | Omit = omit,
        type: str | Omit = omit,
        subnet_id: str | Omit = omit,
        network_id: str | Omit = omit,
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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface",
            body=maybe_transform(
                {
                    "ddos_profile": ddos_profile,
                    "interface_name": interface_name,
                    "ip_family": ip_family,
                    "port_group": port_group,
                    "security_groups": security_groups,
                    "type": type,
                    "subnet_id": subnet_id,
                    "network_id": network_id,
                    "port_id": port_id,
                },
                interface_attach_params.InterfaceAttachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def detach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ip_address: str,
        port_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Detach interface from bare metal GPU cluster server

        Args:
          ip_address: IP address

          port_id: ID of the port

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/detach_interface",
            body=maybe_transform(
                {
                    "ip_address": ip_address,
                    "port_id": port_id,
                },
                interface_detach_params.InterfaceDetachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class AsyncInterfacesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInterfacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInterfacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInterfacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncInterfacesResourceWithStreamingResponse(self)

    async def list(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkInterfaceList:
        """
        Retrieve a list of network interfaces attached to the GPU cluster servers.

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
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return await self._get(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{cluster_id}/interfaces",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkInterfaceList,
        )

    @overload
    async def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ddos_profile: interface_attach_params.NewInterfaceExternalExtendSchemaWithDDOSDDOSProfile | Omit = omit,
        interface_name: str | Omit = omit,
        ip_family: Literal["dual", "ipv4", "ipv6"] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Iterable[interface_attach_params.NewInterfaceExternalExtendSchemaWithDDOSSecurityGroup]
        | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to bare metal GPU cluster server

        Args:
          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          port_group: Each group will be added to the separate trunk.

          security_groups: List of security group IDs

          type: Must be 'external'. Union tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        ddos_profile: interface_attach_params.NewInterfaceSpecificSubnetSchemaDDOSProfile | Omit = omit,
        interface_name: str | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Iterable[interface_attach_params.NewInterfaceSpecificSubnetSchemaSecurityGroup] | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to bare metal GPU cluster server

        Args:
          subnet_id: Port will get an IP address from this subnet

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name

          port_group: Each group will be added to the separate trunk.

          security_groups: List of security group IDs

          type: Must be 'subnet'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        network_id: str,
        ddos_profile: interface_attach_params.NewInterfaceAnySubnetSchemaDDOSProfile | Omit = omit,
        interface_name: str | Omit = omit,
        ip_family: Literal["dual", "ipv4", "ipv6"] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Iterable[interface_attach_params.NewInterfaceAnySubnetSchemaSecurityGroup] | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to bare metal GPU cluster server

        Args:
          network_id: Port will get an IP address in this network subnet

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          port_group: Each group will be added to the separate trunk.

          security_groups: List of security group IDs

          type: Must be '`any_subnet`'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        ddos_profile: interface_attach_params.NewInterfaceReservedFixedIPSchemaDDOSProfile | Omit = omit,
        interface_name: str | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Iterable[interface_attach_params.NewInterfaceReservedFixedIPSchemaSecurityGroup] | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to bare metal GPU cluster server

        Args:
          port_id: Port ID

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name

          port_group: Each group will be added to the separate trunk.

          security_groups: List of security group IDs

          type: Must be '`reserved_fixed_ip`'. Union tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ddos_profile: interface_attach_params.NewInterfaceExternalExtendSchemaWithDDOSDDOSProfile
        | interface_attach_params.NewInterfaceSpecificSubnetSchemaDDOSProfile
        | interface_attach_params.NewInterfaceAnySubnetSchemaDDOSProfile
        | interface_attach_params.NewInterfaceReservedFixedIPSchemaDDOSProfile
        | Omit = omit,
        interface_name: str | Omit = omit,
        ip_family: Literal["dual", "ipv4", "ipv6"] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Iterable[interface_attach_params.NewInterfaceExternalExtendSchemaWithDDOSSecurityGroup]
        | Iterable[interface_attach_params.NewInterfaceSpecificSubnetSchemaSecurityGroup]
        | Iterable[interface_attach_params.NewInterfaceAnySubnetSchemaSecurityGroup]
        | Iterable[interface_attach_params.NewInterfaceReservedFixedIPSchemaSecurityGroup]
        | Omit = omit,
        type: str | Omit = omit,
        subnet_id: str | Omit = omit,
        network_id: str | Omit = omit,
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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface",
            body=await async_maybe_transform(
                {
                    "ddos_profile": ddos_profile,
                    "interface_name": interface_name,
                    "ip_family": ip_family,
                    "port_group": port_group,
                    "security_groups": security_groups,
                    "type": type,
                    "subnet_id": subnet_id,
                    "network_id": network_id,
                    "port_id": port_id,
                },
                interface_attach_params.InterfaceAttachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def detach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ip_address: str,
        port_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Detach interface from bare metal GPU cluster server

        Args:
          ip_address: IP address

          port_id: ID of the port

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/detach_interface",
            body=await async_maybe_transform(
                {
                    "ip_address": ip_address,
                    "port_id": port_id,
                },
                interface_detach_params.InterfaceDetachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class InterfacesResourceWithRawResponse:
    def __init__(self, interfaces: InterfacesResource) -> None:
        self._interfaces = interfaces

        self.list = to_raw_response_wrapper(
            interfaces.list,
        )
        self.attach = to_raw_response_wrapper(
            interfaces.attach,
        )
        self.detach = to_raw_response_wrapper(
            interfaces.detach,
        )


class AsyncInterfacesResourceWithRawResponse:
    def __init__(self, interfaces: AsyncInterfacesResource) -> None:
        self._interfaces = interfaces

        self.list = async_to_raw_response_wrapper(
            interfaces.list,
        )
        self.attach = async_to_raw_response_wrapper(
            interfaces.attach,
        )
        self.detach = async_to_raw_response_wrapper(
            interfaces.detach,
        )


class InterfacesResourceWithStreamingResponse:
    def __init__(self, interfaces: InterfacesResource) -> None:
        self._interfaces = interfaces

        self.list = to_streamed_response_wrapper(
            interfaces.list,
        )
        self.attach = to_streamed_response_wrapper(
            interfaces.attach,
        )
        self.detach = to_streamed_response_wrapper(
            interfaces.detach,
        )


class AsyncInterfacesResourceWithStreamingResponse:
    def __init__(self, interfaces: AsyncInterfacesResource) -> None:
        self._interfaces = interfaces

        self.list = async_to_streamed_response_wrapper(
            interfaces.list,
        )
        self.attach = async_to_streamed_response_wrapper(
            interfaces.attach,
        )
        self.detach = async_to_streamed_response_wrapper(
            interfaces.detach,
        )

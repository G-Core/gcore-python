# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

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
from ...._base_client import make_request_options
from ....types.cloud.console import Console
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.gpu_baremetal_clusters import (
    server_delete_params,
    server_attach_interface_params,
    server_detach_interface_params,
)
from ....types.cloud.gpu_baremetal_cluster_server import GPUBaremetalClusterServer

__all__ = ["ServersResource", "AsyncServersResource"]


class ServersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ServersResourceWithStreamingResponse(self)

    def delete(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        delete_floatings: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Delete a specific node from a GPU cluster.

        The node must be in a state that
        allows deletion.

        Args:
          delete_floatings: Set False if you do not want to delete assigned floating IPs. By default, it's
              True.

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._delete(
            f"/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"delete_floatings": delete_floatings}, server_delete_params.ServerDeleteParams),
            ),
            cast_to=TaskIDList,
        )

    def delete_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        delete_floatings: bool | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a bare metal GPU server from cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            cluster_id=cluster_id,
            delete_floatings=delete_floatings,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
        )

    @overload
    def attach_interface(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ddos_profile: server_attach_interface_params.NewInterfaceExternalExtendSchemaWithDDOSDDOSProfile
        | NotGiven = NOT_GIVEN,
        interface_name: str | NotGiven = NOT_GIVEN,
        ip_family: Literal["dual", "ipv4", "ipv6"] | NotGiven = NOT_GIVEN,
        port_group: int | NotGiven = NOT_GIVEN,
        security_groups: Iterable[server_attach_interface_params.NewInterfaceExternalExtendSchemaWithDDOSSecurityGroup]
        | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
    def attach_interface(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        ddos_profile: server_attach_interface_params.NewInterfaceSpecificSubnetSchemaDDOSProfile | NotGiven = NOT_GIVEN,
        interface_name: str | NotGiven = NOT_GIVEN,
        port_group: int | NotGiven = NOT_GIVEN,
        security_groups: Iterable[server_attach_interface_params.NewInterfaceSpecificSubnetSchemaSecurityGroup]
        | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
    def attach_interface(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        network_id: str,
        ddos_profile: server_attach_interface_params.NewInterfaceAnySubnetSchemaDDOSProfile | NotGiven = NOT_GIVEN,
        interface_name: str | NotGiven = NOT_GIVEN,
        ip_family: Literal["dual", "ipv4", "ipv6"] | NotGiven = NOT_GIVEN,
        port_group: int | NotGiven = NOT_GIVEN,
        security_groups: Iterable[server_attach_interface_params.NewInterfaceAnySubnetSchemaSecurityGroup]
        | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
    def attach_interface(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        ddos_profile: server_attach_interface_params.NewInterfaceReservedFixedIPSchemaDDOSProfile
        | NotGiven = NOT_GIVEN,
        interface_name: str | NotGiven = NOT_GIVEN,
        port_group: int | NotGiven = NOT_GIVEN,
        security_groups: Iterable[server_attach_interface_params.NewInterfaceReservedFixedIPSchemaSecurityGroup]
        | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def attach_interface(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ddos_profile: server_attach_interface_params.NewInterfaceExternalExtendSchemaWithDDOSDDOSProfile
        | NotGiven = NOT_GIVEN,
        interface_name: str | NotGiven = NOT_GIVEN,
        ip_family: Literal["dual", "ipv4", "ipv6"] | NotGiven = NOT_GIVEN,
        port_group: int | NotGiven = NOT_GIVEN,
        security_groups: Iterable[server_attach_interface_params.NewInterfaceExternalExtendSchemaWithDDOSSecurityGroup]
        | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        subnet_id: str | NotGiven = NOT_GIVEN,
        network_id: str | NotGiven = NOT_GIVEN,
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
                server_attach_interface_params.ServerAttachInterfaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def detach_interface(
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                server_detach_interface_params.ServerDetachInterfaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get_console(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Console:
        """
        Get bare metal GPU cluster server console URL

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/get_console",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Console,
        )

    def powercycle(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUBaremetalClusterServer:
        """
        Stops and then starts the server, effectively performing a hard reboot.

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/powercycle",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalClusterServer,
        )

    def reboot(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUBaremetalClusterServer:
        """
        Reboot one bare metal GPU cluster server

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/reboot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalClusterServer,
        )


class AsyncServersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncServersResourceWithStreamingResponse(self)

    async def delete(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        delete_floatings: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Delete a specific node from a GPU cluster.

        The node must be in a state that
        allows deletion.

        Args:
          delete_floatings: Set False if you do not want to delete assigned floating IPs. By default, it's
              True.

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._delete(
            f"/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"delete_floatings": delete_floatings}, server_delete_params.ServerDeleteParams
                ),
            ),
            cast_to=TaskIDList,
        )

    async def delete_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        delete_floatings: bool | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a bare metal GPU server from cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            cluster_id=cluster_id,
            delete_floatings=delete_floatings,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
        )

    @overload
    async def attach_interface(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ddos_profile: server_attach_interface_params.NewInterfaceExternalExtendSchemaWithDDOSDDOSProfile
        | NotGiven = NOT_GIVEN,
        interface_name: str | NotGiven = NOT_GIVEN,
        ip_family: Literal["dual", "ipv4", "ipv6"] | NotGiven = NOT_GIVEN,
        port_group: int | NotGiven = NOT_GIVEN,
        security_groups: Iterable[server_attach_interface_params.NewInterfaceExternalExtendSchemaWithDDOSSecurityGroup]
        | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
    async def attach_interface(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        ddos_profile: server_attach_interface_params.NewInterfaceSpecificSubnetSchemaDDOSProfile | NotGiven = NOT_GIVEN,
        interface_name: str | NotGiven = NOT_GIVEN,
        port_group: int | NotGiven = NOT_GIVEN,
        security_groups: Iterable[server_attach_interface_params.NewInterfaceSpecificSubnetSchemaSecurityGroup]
        | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
    async def attach_interface(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        network_id: str,
        ddos_profile: server_attach_interface_params.NewInterfaceAnySubnetSchemaDDOSProfile | NotGiven = NOT_GIVEN,
        interface_name: str | NotGiven = NOT_GIVEN,
        ip_family: Literal["dual", "ipv4", "ipv6"] | NotGiven = NOT_GIVEN,
        port_group: int | NotGiven = NOT_GIVEN,
        security_groups: Iterable[server_attach_interface_params.NewInterfaceAnySubnetSchemaSecurityGroup]
        | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
    async def attach_interface(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        ddos_profile: server_attach_interface_params.NewInterfaceReservedFixedIPSchemaDDOSProfile
        | NotGiven = NOT_GIVEN,
        interface_name: str | NotGiven = NOT_GIVEN,
        port_group: int | NotGiven = NOT_GIVEN,
        security_groups: Iterable[server_attach_interface_params.NewInterfaceReservedFixedIPSchemaSecurityGroup]
        | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def attach_interface(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ddos_profile: server_attach_interface_params.NewInterfaceExternalExtendSchemaWithDDOSDDOSProfile
        | NotGiven = NOT_GIVEN,
        interface_name: str | NotGiven = NOT_GIVEN,
        ip_family: Literal["dual", "ipv4", "ipv6"] | NotGiven = NOT_GIVEN,
        port_group: int | NotGiven = NOT_GIVEN,
        security_groups: Iterable[server_attach_interface_params.NewInterfaceExternalExtendSchemaWithDDOSSecurityGroup]
        | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        subnet_id: str | NotGiven = NOT_GIVEN,
        network_id: str | NotGiven = NOT_GIVEN,
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
                server_attach_interface_params.ServerAttachInterfaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def detach_interface(
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                server_detach_interface_params.ServerDetachInterfaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get_console(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Console:
        """
        Get bare metal GPU cluster server console URL

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/get_console",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Console,
        )

    async def powercycle(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUBaremetalClusterServer:
        """
        Stops and then starts the server, effectively performing a hard reboot.

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/powercycle",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalClusterServer,
        )

    async def reboot(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUBaremetalClusterServer:
        """
        Reboot one bare metal GPU cluster server

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/reboot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalClusterServer,
        )


class ServersResourceWithRawResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.delete = to_raw_response_wrapper(
            servers.delete,
        )
        self.attach_interface = to_raw_response_wrapper(
            servers.attach_interface,
        )
        self.detach_interface = to_raw_response_wrapper(
            servers.detach_interface,
        )
        self.get_console = to_raw_response_wrapper(
            servers.get_console,
        )
        self.powercycle = to_raw_response_wrapper(
            servers.powercycle,
        )
        self.reboot = to_raw_response_wrapper(
            servers.reboot,
        )


class AsyncServersResourceWithRawResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.delete = async_to_raw_response_wrapper(
            servers.delete,
        )
        self.attach_interface = async_to_raw_response_wrapper(
            servers.attach_interface,
        )
        self.detach_interface = async_to_raw_response_wrapper(
            servers.detach_interface,
        )
        self.get_console = async_to_raw_response_wrapper(
            servers.get_console,
        )
        self.powercycle = async_to_raw_response_wrapper(
            servers.powercycle,
        )
        self.reboot = async_to_raw_response_wrapper(
            servers.reboot,
        )


class ServersResourceWithStreamingResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.delete = to_streamed_response_wrapper(
            servers.delete,
        )
        self.attach_interface = to_streamed_response_wrapper(
            servers.attach_interface,
        )
        self.detach_interface = to_streamed_response_wrapper(
            servers.detach_interface,
        )
        self.get_console = to_streamed_response_wrapper(
            servers.get_console,
        )
        self.powercycle = to_streamed_response_wrapper(
            servers.powercycle,
        )
        self.reboot = to_streamed_response_wrapper(
            servers.reboot,
        )


class AsyncServersResourceWithStreamingResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.delete = async_to_streamed_response_wrapper(
            servers.delete,
        )
        self.attach_interface = async_to_streamed_response_wrapper(
            servers.attach_interface,
        )
        self.detach_interface = async_to_streamed_response_wrapper(
            servers.detach_interface,
        )
        self.get_console = async_to_streamed_response_wrapper(
            servers.get_console,
        )
        self.powercycle = async_to_streamed_response_wrapper(
            servers.powercycle,
        )
        self.reboot = async_to_streamed_response_wrapper(
            servers.reboot,
        )

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
from ....types.cloud.gpu_cluster_server import GPUClusterServer
from ....types.cloud.gpu_baremetal_clusters import (
    server_delete_params,
    server_attach_interface_params,
    server_detach_interface_params,
)

__all__ = ["ServersResource", "AsyncServersResource"]


class ServersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
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
        """
        Remove single node from GPU cluster.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[2].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/3/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[3].schema"

          delete_floatings: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/4'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[4]"

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
        Attach interface to GPU cluster node

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[2].schema"

          ddos_profile: '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/ddos_profile/allOf/0'
              "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.ddos_profile.allOf[0]"

          interface_name: '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/interface_name'
              "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.interface_name"

          ip_family: '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/ip_family'
              "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.ip_family"

          port_group: '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/port_group'
              "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.port_group"

          security_groups: '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/security_groups'
              "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.security_groups"

          type: '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/type'
              "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.type"

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
        Attach interface to GPU cluster node

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[2].schema"

          subnet_id: '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/subnet_id'
              "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.subnet_id"

          ddos_profile: '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/ddos_profile/allOf/0'
              "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.ddos_profile.allOf[0]"

          interface_name: '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/interface_name'
              "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.interface_name"

          port_group: '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/port_group'
              "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.port_group"

          security_groups: '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/security_groups'
              "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.security_groups"

          type: '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/type'
              "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.type"

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
        Attach interface to GPU cluster node

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[2].schema"

          network_id: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/network_id'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.network_id"

          ddos_profile: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/ddos_profile/allOf/0'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.ddos_profile.allOf[0]"

          interface_name: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/interface_name'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.interface_name"

          ip_family: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/ip_family'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.ip_family"

          port_group: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/port_group'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.port_group"

          security_groups: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/security_groups'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.security_groups"

          type: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/type'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.type"

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
        Attach interface to GPU cluster node

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[2].schema"

          port_id: '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/port_id'
              "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.port_id"

          ddos_profile: '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/ddos_profile/allOf/0'
              "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.ddos_profile.allOf[0]"

          interface_name: '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/interface_name'
              "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.interface_name"

          port_group: '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/port_group'
              "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.port_group"

          security_groups: '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/security_groups'
              "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.security_groups"

          type: '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/type'
              "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.type"

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
        Detach interface from GPU cluster node

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdetach_interface/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/detach_interface'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdetach_interface/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/detach_interface'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdetach_interface/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/detach_interface'].post.parameters[2].schema"

          ip_address: '#/components/schemas/PortIdWithIpSchema/properties/ip_address'
              "$.components.schemas.PortIdWithIpSchema.properties.ip_address"

          port_id: '#/components/schemas/PortIdWithIpSchema/properties/port_id'
              "$.components.schemas.PortIdWithIpSchema.properties.port_id"

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
        Get GPU cluster node console URL

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[2].schema"

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
    ) -> GPUClusterServer:
        """
        Powercycle (stop and start) one GPU cluster node, aka hard reboot

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fpowercycle/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/powercycle'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fpowercycle/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/powercycle'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fpowercycle/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/powercycle'].post.parameters[2].schema"

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
            cast_to=GPUClusterServer,
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
    ) -> GPUClusterServer:
        """
        Reboot one GPU cluster node

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Freboot/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/reboot'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Freboot/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/reboot'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Freboot/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/reboot'].post.parameters[2].schema"

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
            cast_to=GPUClusterServer,
        )


class AsyncServersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
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
        """
        Remove single node from GPU cluster.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[2].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/3/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[3].schema"

          delete_floatings: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/4'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[4]"

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
        Attach interface to GPU cluster node

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[2].schema"

          ddos_profile: '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/ddos_profile/allOf/0'
              "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.ddos_profile.allOf[0]"

          interface_name: '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/interface_name'
              "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.interface_name"

          ip_family: '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/ip_family'
              "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.ip_family"

          port_group: '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/port_group'
              "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.port_group"

          security_groups: '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/security_groups'
              "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.security_groups"

          type: '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/type'
              "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.type"

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
        Attach interface to GPU cluster node

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[2].schema"

          subnet_id: '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/subnet_id'
              "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.subnet_id"

          ddos_profile: '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/ddos_profile/allOf/0'
              "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.ddos_profile.allOf[0]"

          interface_name: '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/interface_name'
              "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.interface_name"

          port_group: '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/port_group'
              "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.port_group"

          security_groups: '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/security_groups'
              "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.security_groups"

          type: '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/type'
              "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.type"

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
        Attach interface to GPU cluster node

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[2].schema"

          network_id: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/network_id'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.network_id"

          ddos_profile: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/ddos_profile/allOf/0'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.ddos_profile.allOf[0]"

          interface_name: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/interface_name'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.interface_name"

          ip_family: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/ip_family'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.ip_family"

          port_group: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/port_group'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.port_group"

          security_groups: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/security_groups'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.security_groups"

          type: '#/components/schemas/NewInterfaceAnySubnetSchema/properties/type'
              "$.components.schemas.NewInterfaceAnySubnetSchema.properties.type"

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
        Attach interface to GPU cluster node

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[2].schema"

          port_id: '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/port_id'
              "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.port_id"

          ddos_profile: '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/ddos_profile/allOf/0'
              "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.ddos_profile.allOf[0]"

          interface_name: '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/interface_name'
              "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.interface_name"

          port_group: '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/port_group'
              "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.port_group"

          security_groups: '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/security_groups'
              "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.security_groups"

          type: '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/type'
              "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.type"

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
        Detach interface from GPU cluster node

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdetach_interface/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/detach_interface'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdetach_interface/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/detach_interface'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdetach_interface/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/detach_interface'].post.parameters[2].schema"

          ip_address: '#/components/schemas/PortIdWithIpSchema/properties/ip_address'
              "$.components.schemas.PortIdWithIpSchema.properties.ip_address"

          port_id: '#/components/schemas/PortIdWithIpSchema/properties/port_id'
              "$.components.schemas.PortIdWithIpSchema.properties.port_id"

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
        Get GPU cluster node console URL

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[2].schema"

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
    ) -> GPUClusterServer:
        """
        Powercycle (stop and start) one GPU cluster node, aka hard reboot

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fpowercycle/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/powercycle'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fpowercycle/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/powercycle'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fpowercycle/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/powercycle'].post.parameters[2].schema"

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
            cast_to=GPUClusterServer,
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
    ) -> GPUClusterServer:
        """
        Reboot one GPU cluster node

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Freboot/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/reboot'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Freboot/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/reboot'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Freboot/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/reboot'].post.parameters[2].schema"

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
            cast_to=GPUClusterServer,
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

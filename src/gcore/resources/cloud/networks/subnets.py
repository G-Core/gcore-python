# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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

__all__ = ["SubnetsResource", "AsyncSubnetsResource"]


class SubnetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubnetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return SubnetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubnetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
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
        connect_to_network_router: bool | NotGiven = NOT_GIVEN,
        dns_nameservers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_dhcp: bool | NotGiven = NOT_GIVEN,
        gateway_ip: Optional[str] | NotGiven = NOT_GIVEN,
        host_routes: Optional[Iterable[subnet_create_params.HostRoute]] | NotGiven = NOT_GIVEN,
        ip_version: IPVersion | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        router_id_to_connect: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create subnet

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].post.parameters[1].schema"

          cidr: '#/components/schemas/CreateSubnetSerializer/properties/cidr'
              "$.components.schemas.CreateSubnetSerializer.properties.cidr"

          name: '#/components/schemas/CreateSubnetSerializer/properties/name'
              "$.components.schemas.CreateSubnetSerializer.properties.name"

          network_id: '#/components/schemas/CreateSubnetSerializer/properties/network_id'
              "$.components.schemas.CreateSubnetSerializer.properties.network_id"

          connect_to_network_router: '#/components/schemas/CreateSubnetSerializer/properties/connect_to_network_router'
              "$.components.schemas.CreateSubnetSerializer.properties.connect_to_network_router"

          dns_nameservers: '#/components/schemas/CreateSubnetSerializer/properties/dns_nameservers/anyOf/0'
              "$.components.schemas.CreateSubnetSerializer.properties.dns_nameservers.anyOf[0]"

          enable_dhcp: '#/components/schemas/CreateSubnetSerializer/properties/enable_dhcp'
              "$.components.schemas.CreateSubnetSerializer.properties.enable_dhcp"

          gateway_ip: '#/components/schemas/CreateSubnetSerializer/properties/gateway_ip/anyOf/0'
              "$.components.schemas.CreateSubnetSerializer.properties.gateway_ip.anyOf[0]"

          host_routes: '#/components/schemas/CreateSubnetSerializer/properties/host_routes/anyOf/0'
              "$.components.schemas.CreateSubnetSerializer.properties.host_routes.anyOf[0]"

          ip_version: '#/components/schemas/CreateSubnetSerializer/properties/ip_version'
              "$.components.schemas.CreateSubnetSerializer.properties.ip_version"

          metadata: '#/components/schemas/CreateSubnetSerializer/properties/metadata/anyOf/0'
              "$.components.schemas.CreateSubnetSerializer.properties.metadata.anyOf[0]"

          router_id_to_connect: '#/components/schemas/CreateSubnetSerializer/properties/router_id_to_connect/anyOf/0'
              "$.components.schemas.CreateSubnetSerializer.properties.router_id_to_connect.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
                    "metadata": metadata,
                    "router_id_to_connect": router_id_to_connect,
                },
                subnet_create_params.SubnetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        subnet_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        dns_nameservers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_dhcp: Optional[bool] | NotGiven = NOT_GIVEN,
        gateway_ip: Optional[str] | NotGiven = NOT_GIVEN,
        host_routes: Optional[Iterable[subnet_update_params.HostRoute]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subnet:
        """
        Change subnet properties

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].patch.parameters[1].schema"

          subnet_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].patch.parameters[2].schema"

          dns_nameservers: '#/components/schemas/PatchSubnetSerializer/properties/dns_nameservers/anyOf/0'
              "$.components.schemas.PatchSubnetSerializer.properties.dns_nameservers.anyOf[0]"

          enable_dhcp: '#/components/schemas/PatchSubnetSerializer/properties/enable_dhcp/anyOf/0'
              "$.components.schemas.PatchSubnetSerializer.properties.enable_dhcp.anyOf[0]"

          gateway_ip: '#/components/schemas/PatchSubnetSerializer/properties/gateway_ip/anyOf/0'
              "$.components.schemas.PatchSubnetSerializer.properties.gateway_ip.anyOf[0]"

          host_routes: '#/components/schemas/PatchSubnetSerializer/properties/host_routes/anyOf/0'
              "$.components.schemas.PatchSubnetSerializer.properties.host_routes.anyOf[0]"

          name: '#/components/schemas/PatchSubnetSerializer/properties/name/anyOf/0'
              "$.components.schemas.PatchSubnetSerializer.properties.name.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
        limit: int | NotGiven = NOT_GIVEN,
        metadata_k: List[str] | NotGiven = NOT_GIVEN,
        metadata_kv: str | NotGiven = NOT_GIVEN,
        network_id: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[Subnet]:
        """
        List subnets

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[1].schema"

          limit: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[2]"

          metadata_k: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[3]"

          metadata_kv: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[4]"

          network_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[5]"

          offset: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[6]"

          order_by: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[7]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
                        "metadata_k": metadata_k,
                        "metadata_kv": metadata_kv,
                        "network_id": network_id,
                        "offset": offset,
                        "order_by": order_by,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete subnet

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}']['delete'].parameters[1].schema"

          subnet_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}']['delete'].parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subnet:
        """
        Get subnet

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].get.parameters[1].schema"

          subnet_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].get.parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubnetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubnetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
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
        connect_to_network_router: bool | NotGiven = NOT_GIVEN,
        dns_nameservers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_dhcp: bool | NotGiven = NOT_GIVEN,
        gateway_ip: Optional[str] | NotGiven = NOT_GIVEN,
        host_routes: Optional[Iterable[subnet_create_params.HostRoute]] | NotGiven = NOT_GIVEN,
        ip_version: IPVersion | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        router_id_to_connect: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create subnet

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].post.parameters[1].schema"

          cidr: '#/components/schemas/CreateSubnetSerializer/properties/cidr'
              "$.components.schemas.CreateSubnetSerializer.properties.cidr"

          name: '#/components/schemas/CreateSubnetSerializer/properties/name'
              "$.components.schemas.CreateSubnetSerializer.properties.name"

          network_id: '#/components/schemas/CreateSubnetSerializer/properties/network_id'
              "$.components.schemas.CreateSubnetSerializer.properties.network_id"

          connect_to_network_router: '#/components/schemas/CreateSubnetSerializer/properties/connect_to_network_router'
              "$.components.schemas.CreateSubnetSerializer.properties.connect_to_network_router"

          dns_nameservers: '#/components/schemas/CreateSubnetSerializer/properties/dns_nameservers/anyOf/0'
              "$.components.schemas.CreateSubnetSerializer.properties.dns_nameservers.anyOf[0]"

          enable_dhcp: '#/components/schemas/CreateSubnetSerializer/properties/enable_dhcp'
              "$.components.schemas.CreateSubnetSerializer.properties.enable_dhcp"

          gateway_ip: '#/components/schemas/CreateSubnetSerializer/properties/gateway_ip/anyOf/0'
              "$.components.schemas.CreateSubnetSerializer.properties.gateway_ip.anyOf[0]"

          host_routes: '#/components/schemas/CreateSubnetSerializer/properties/host_routes/anyOf/0'
              "$.components.schemas.CreateSubnetSerializer.properties.host_routes.anyOf[0]"

          ip_version: '#/components/schemas/CreateSubnetSerializer/properties/ip_version'
              "$.components.schemas.CreateSubnetSerializer.properties.ip_version"

          metadata: '#/components/schemas/CreateSubnetSerializer/properties/metadata/anyOf/0'
              "$.components.schemas.CreateSubnetSerializer.properties.metadata.anyOf[0]"

          router_id_to_connect: '#/components/schemas/CreateSubnetSerializer/properties/router_id_to_connect/anyOf/0'
              "$.components.schemas.CreateSubnetSerializer.properties.router_id_to_connect.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
                    "metadata": metadata,
                    "router_id_to_connect": router_id_to_connect,
                },
                subnet_create_params.SubnetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        subnet_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        dns_nameservers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_dhcp: Optional[bool] | NotGiven = NOT_GIVEN,
        gateway_ip: Optional[str] | NotGiven = NOT_GIVEN,
        host_routes: Optional[Iterable[subnet_update_params.HostRoute]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subnet:
        """
        Change subnet properties

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].patch.parameters[1].schema"

          subnet_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].patch.parameters[2].schema"

          dns_nameservers: '#/components/schemas/PatchSubnetSerializer/properties/dns_nameservers/anyOf/0'
              "$.components.schemas.PatchSubnetSerializer.properties.dns_nameservers.anyOf[0]"

          enable_dhcp: '#/components/schemas/PatchSubnetSerializer/properties/enable_dhcp/anyOf/0'
              "$.components.schemas.PatchSubnetSerializer.properties.enable_dhcp.anyOf[0]"

          gateway_ip: '#/components/schemas/PatchSubnetSerializer/properties/gateway_ip/anyOf/0'
              "$.components.schemas.PatchSubnetSerializer.properties.gateway_ip.anyOf[0]"

          host_routes: '#/components/schemas/PatchSubnetSerializer/properties/host_routes/anyOf/0'
              "$.components.schemas.PatchSubnetSerializer.properties.host_routes.anyOf[0]"

          name: '#/components/schemas/PatchSubnetSerializer/properties/name/anyOf/0'
              "$.components.schemas.PatchSubnetSerializer.properties.name.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
        limit: int | NotGiven = NOT_GIVEN,
        metadata_k: List[str] | NotGiven = NOT_GIVEN,
        metadata_kv: str | NotGiven = NOT_GIVEN,
        network_id: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Subnet, AsyncOffsetPage[Subnet]]:
        """
        List subnets

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[1].schema"

          limit: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[2]"

          metadata_k: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[3]"

          metadata_kv: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[4]"

          network_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[5]"

          offset: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[6]"

          order_by: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[7]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
                        "metadata_k": metadata_k,
                        "metadata_kv": metadata_kv,
                        "network_id": network_id,
                        "offset": offset,
                        "order_by": order_by,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete subnet

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}']['delete'].parameters[1].schema"

          subnet_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}']['delete'].parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subnet:
        """
        Get subnet

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].get.parameters[1].schema"

          subnet_id: '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].get.parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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

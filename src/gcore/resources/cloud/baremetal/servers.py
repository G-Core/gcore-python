# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

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
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.baremetal import server_list_params, server_create_params, server_rebuild_params
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.baremetal.baremetal_server import BaremetalServer

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

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        interfaces: Iterable[server_create_params.Interface],
        app_config: Optional[object] | NotGiven = NOT_GIVEN,
        apptemplate_id: str | NotGiven = NOT_GIVEN,
        ddos_profile: server_create_params.DDOSProfile | NotGiven = NOT_GIVEN,
        image_id: str | NotGiven = NOT_GIVEN,
        keypair_name: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name_templates: List[str] | NotGiven = NOT_GIVEN,
        names: List[str] | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create a new bare metal server or multiple servers

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].post.parameters[1].schema"

          flavor: '#/components/schemas/CreateBareMetalServerSerializer/properties/flavor'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.flavor"

          interfaces: '#/components/schemas/CreateBareMetalServerSerializer/properties/interfaces'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.interfaces"

          app_config: '#/components/schemas/CreateBareMetalServerSerializer/properties/app_config/anyOf/0'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.app_config.anyOf[0]"

          apptemplate_id: '#/components/schemas/CreateBareMetalServerSerializer/properties/apptemplate_id'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.apptemplate_id"

          ddos_profile: '#/components/schemas/CreateBareMetalServerSerializer/properties/ddos_profile'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.ddos_profile"

          image_id: '#/components/schemas/CreateBareMetalServerSerializer/properties/image_id'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.image_id"

          keypair_name: '#/components/schemas/CreateBareMetalServerSerializer/properties/keypair_name/anyOf/0'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.keypair_name.anyOf[0]"

          metadata: '#/components/schemas/CreateBareMetalServerSerializer/properties/metadata'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.metadata"

          name_templates: '#/components/schemas/CreateBareMetalServerSerializer/properties/name_templates'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.name_templates"

          names: '#/components/schemas/CreateBareMetalServerSerializer/properties/names'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.names"

          password: '#/components/schemas/CreateBareMetalServerSerializer/properties/password'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.password"

          user_data: '#/components/schemas/CreateBareMetalServerSerializer/properties/user_data'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.user_data"

          username: '#/components/schemas/CreateBareMetalServerSerializer/properties/username'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.username"

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
            f"/cloud/v1/bminstances/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "flavor": flavor,
                    "interfaces": interfaces,
                    "app_config": app_config,
                    "apptemplate_id": apptemplate_id,
                    "ddos_profile": ddos_profile,
                    "image_id": image_id,
                    "keypair_name": keypair_name,
                    "metadata": metadata,
                    "name_templates": name_templates,
                    "names": names,
                    "password": password,
                    "user_data": user_data,
                    "username": username,
                },
                server_create_params.ServerCreateParams,
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
        changes_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        changes_since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        flavor_id: str | NotGiven = NOT_GIVEN,
        flavor_prefix: str | NotGiven = NOT_GIVEN,
        include_k8s: bool | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_kv: str | NotGiven = NOT_GIVEN,
        metadata_v: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        only_isolated: bool | NotGiven = NOT_GIVEN,
        only_with_fixed_external_ip: bool | NotGiven = NOT_GIVEN,
        order_by: Literal["created.asc", "created.desc", "name.asc", "name.desc", "status.asc", "status.desc"]
        | NotGiven = NOT_GIVEN,
        profile_name: str | NotGiven = NOT_GIVEN,
        protection_status: Literal["Active", "Queued", "Error"] | NotGiven = NOT_GIVEN,
        status: Literal[
            "ACTIVE", "BUILD", "ERROR", "HARD_REBOOT", "REBOOT", "REBUILD", "RESCUE", "SHUTOFF", "SUSPENDED"
        ]
        | NotGiven = NOT_GIVEN,
        type_ddos_profile: Literal["basic", "advanced"] | NotGiven = NOT_GIVEN,
        uuid: str | NotGiven = NOT_GIVEN,
        with_ddos: bool | NotGiven = NOT_GIVEN,
        with_interfaces_name: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[BaremetalServer]:
        """
        List bare metal servers

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[1].schema"

          changes_before: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[2]"

          changes_since: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[3]"

          flavor_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[4]"

          flavor_prefix: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[5]"

          include_k8s: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[6]"

          ip: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[7]"

          limit: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/8'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[8]"

          metadata_kv: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/9'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[9]"

          metadata_v: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/10'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[10]"

          name: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/11'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[11]"

          offset: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/12'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[12]"

          only_isolated: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/13'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[13]"

          only_with_fixed_external_ip: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/14'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[14]"

          order_by: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/15'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[15]"

          profile_name: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/16'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[16]"

          protection_status: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/17'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[17]"

          status: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/18'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[18]"

          type_ddos_profile: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/19'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[19]"

          uuid: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/20'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[20]"

          with_ddos: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/21'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[21]"

          with_interfaces_name: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/22'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[22]"

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
            f"/cloud/v1/bminstances/{project_id}/{region_id}",
            page=SyncOffsetPage[BaremetalServer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "changes_before": changes_before,
                        "changes_since": changes_since,
                        "flavor_id": flavor_id,
                        "flavor_prefix": flavor_prefix,
                        "include_k8s": include_k8s,
                        "ip": ip,
                        "limit": limit,
                        "metadata_kv": metadata_kv,
                        "metadata_v": metadata_v,
                        "name": name,
                        "offset": offset,
                        "only_isolated": only_isolated,
                        "only_with_fixed_external_ip": only_with_fixed_external_ip,
                        "order_by": order_by,
                        "profile_name": profile_name,
                        "protection_status": protection_status,
                        "status": status,
                        "type_ddos_profile": type_ddos_profile,
                        "uuid": uuid,
                        "with_ddos": with_ddos,
                        "with_interfaces_name": with_interfaces_name,
                    },
                    server_list_params.ServerListParams,
                ),
            ),
            model=BaremetalServer,
        )

    def rebuild(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Rebuild bare metal server

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bserver_id%7D%2Frebuild/post/parameters/0/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bserver_id%7D%2Frebuild/post/parameters/1/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild'].post.parameters[1].schema"

          server_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bserver_id%7D%2Frebuild/post/parameters/2/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild'].post.parameters[2].schema"

          image_id: '#/components/schemas/RebuildBaremetalSchema/properties/image_id'
              "$.components.schemas.RebuildBaremetalSchema.properties.image_id"

          user_data: '#/components/schemas/RebuildBaremetalSchema/properties/user_data'
              "$.components.schemas.RebuildBaremetalSchema.properties.user_data"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._post(
            f"/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild",
            body=maybe_transform(
                {
                    "image_id": image_id,
                    "user_data": user_data,
                },
                server_rebuild_params.ServerRebuildParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
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

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        interfaces: Iterable[server_create_params.Interface],
        app_config: Optional[object] | NotGiven = NOT_GIVEN,
        apptemplate_id: str | NotGiven = NOT_GIVEN,
        ddos_profile: server_create_params.DDOSProfile | NotGiven = NOT_GIVEN,
        image_id: str | NotGiven = NOT_GIVEN,
        keypair_name: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name_templates: List[str] | NotGiven = NOT_GIVEN,
        names: List[str] | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create a new bare metal server or multiple servers

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].post.parameters[1].schema"

          flavor: '#/components/schemas/CreateBareMetalServerSerializer/properties/flavor'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.flavor"

          interfaces: '#/components/schemas/CreateBareMetalServerSerializer/properties/interfaces'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.interfaces"

          app_config: '#/components/schemas/CreateBareMetalServerSerializer/properties/app_config/anyOf/0'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.app_config.anyOf[0]"

          apptemplate_id: '#/components/schemas/CreateBareMetalServerSerializer/properties/apptemplate_id'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.apptemplate_id"

          ddos_profile: '#/components/schemas/CreateBareMetalServerSerializer/properties/ddos_profile'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.ddos_profile"

          image_id: '#/components/schemas/CreateBareMetalServerSerializer/properties/image_id'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.image_id"

          keypair_name: '#/components/schemas/CreateBareMetalServerSerializer/properties/keypair_name/anyOf/0'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.keypair_name.anyOf[0]"

          metadata: '#/components/schemas/CreateBareMetalServerSerializer/properties/metadata'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.metadata"

          name_templates: '#/components/schemas/CreateBareMetalServerSerializer/properties/name_templates'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.name_templates"

          names: '#/components/schemas/CreateBareMetalServerSerializer/properties/names'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.names"

          password: '#/components/schemas/CreateBareMetalServerSerializer/properties/password'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.password"

          user_data: '#/components/schemas/CreateBareMetalServerSerializer/properties/user_data'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.user_data"

          username: '#/components/schemas/CreateBareMetalServerSerializer/properties/username'
              "$.components.schemas.CreateBareMetalServerSerializer.properties.username"

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
            f"/cloud/v1/bminstances/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "flavor": flavor,
                    "interfaces": interfaces,
                    "app_config": app_config,
                    "apptemplate_id": apptemplate_id,
                    "ddos_profile": ddos_profile,
                    "image_id": image_id,
                    "keypair_name": keypair_name,
                    "metadata": metadata,
                    "name_templates": name_templates,
                    "names": names,
                    "password": password,
                    "user_data": user_data,
                    "username": username,
                },
                server_create_params.ServerCreateParams,
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
        changes_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        changes_since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        flavor_id: str | NotGiven = NOT_GIVEN,
        flavor_prefix: str | NotGiven = NOT_GIVEN,
        include_k8s: bool | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_kv: str | NotGiven = NOT_GIVEN,
        metadata_v: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        only_isolated: bool | NotGiven = NOT_GIVEN,
        only_with_fixed_external_ip: bool | NotGiven = NOT_GIVEN,
        order_by: Literal["created.asc", "created.desc", "name.asc", "name.desc", "status.asc", "status.desc"]
        | NotGiven = NOT_GIVEN,
        profile_name: str | NotGiven = NOT_GIVEN,
        protection_status: Literal["Active", "Queued", "Error"] | NotGiven = NOT_GIVEN,
        status: Literal[
            "ACTIVE", "BUILD", "ERROR", "HARD_REBOOT", "REBOOT", "REBUILD", "RESCUE", "SHUTOFF", "SUSPENDED"
        ]
        | NotGiven = NOT_GIVEN,
        type_ddos_profile: Literal["basic", "advanced"] | NotGiven = NOT_GIVEN,
        uuid: str | NotGiven = NOT_GIVEN,
        with_ddos: bool | NotGiven = NOT_GIVEN,
        with_interfaces_name: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BaremetalServer, AsyncOffsetPage[BaremetalServer]]:
        """
        List bare metal servers

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[1].schema"

          changes_before: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[2]"

          changes_since: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[3]"

          flavor_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[4]"

          flavor_prefix: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[5]"

          include_k8s: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[6]"

          ip: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[7]"

          limit: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/8'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[8]"

          metadata_kv: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/9'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[9]"

          metadata_v: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/10'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[10]"

          name: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/11'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[11]"

          offset: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/12'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[12]"

          only_isolated: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/13'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[13]"

          only_with_fixed_external_ip: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/14'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[14]"

          order_by: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/15'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[15]"

          profile_name: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/16'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[16]"

          protection_status: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/17'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[17]"

          status: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/18'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[18]"

          type_ddos_profile: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/19'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[19]"

          uuid: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/20'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[20]"

          with_ddos: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/21'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[21]"

          with_interfaces_name: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/22'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[22]"

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
            f"/cloud/v1/bminstances/{project_id}/{region_id}",
            page=AsyncOffsetPage[BaremetalServer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "changes_before": changes_before,
                        "changes_since": changes_since,
                        "flavor_id": flavor_id,
                        "flavor_prefix": flavor_prefix,
                        "include_k8s": include_k8s,
                        "ip": ip,
                        "limit": limit,
                        "metadata_kv": metadata_kv,
                        "metadata_v": metadata_v,
                        "name": name,
                        "offset": offset,
                        "only_isolated": only_isolated,
                        "only_with_fixed_external_ip": only_with_fixed_external_ip,
                        "order_by": order_by,
                        "profile_name": profile_name,
                        "protection_status": protection_status,
                        "status": status,
                        "type_ddos_profile": type_ddos_profile,
                        "uuid": uuid,
                        "with_ddos": with_ddos,
                        "with_interfaces_name": with_interfaces_name,
                    },
                    server_list_params.ServerListParams,
                ),
            ),
            model=BaremetalServer,
        )

    async def rebuild(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Rebuild bare metal server

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bserver_id%7D%2Frebuild/post/parameters/0/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bserver_id%7D%2Frebuild/post/parameters/1/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild'].post.parameters[1].schema"

          server_id: '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bserver_id%7D%2Frebuild/post/parameters/2/schema'
              "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild'].post.parameters[2].schema"

          image_id: '#/components/schemas/RebuildBaremetalSchema/properties/image_id'
              "$.components.schemas.RebuildBaremetalSchema.properties.image_id"

          user_data: '#/components/schemas/RebuildBaremetalSchema/properties/user_data'
              "$.components.schemas.RebuildBaremetalSchema.properties.user_data"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._post(
            f"/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild",
            body=await async_maybe_transform(
                {
                    "image_id": image_id,
                    "user_data": user_data,
                },
                server_rebuild_params.ServerRebuildParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class ServersResourceWithRawResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.create = to_raw_response_wrapper(
            servers.create,
        )
        self.list = to_raw_response_wrapper(
            servers.list,
        )
        self.rebuild = to_raw_response_wrapper(
            servers.rebuild,
        )


class AsyncServersResourceWithRawResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.create = async_to_raw_response_wrapper(
            servers.create,
        )
        self.list = async_to_raw_response_wrapper(
            servers.list,
        )
        self.rebuild = async_to_raw_response_wrapper(
            servers.rebuild,
        )


class ServersResourceWithStreamingResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.create = to_streamed_response_wrapper(
            servers.create,
        )
        self.list = to_streamed_response_wrapper(
            servers.list,
        )
        self.rebuild = to_streamed_response_wrapper(
            servers.rebuild,
        )


class AsyncServersResourceWithStreamingResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.create = async_to_streamed_response_wrapper(
            servers.create,
        )
        self.list = async_to_streamed_response_wrapper(
            servers.list,
        )
        self.rebuild = async_to_streamed_response_wrapper(
            servers.rebuild,
        )

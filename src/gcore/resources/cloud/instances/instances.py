# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from .images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from .flavors import (
    FlavorsResource,
    AsyncFlavorsResource,
    FlavorsResourceWithRawResponse,
    AsyncFlavorsResourceWithRawResponse,
    FlavorsResourceWithStreamingResponse,
    AsyncFlavorsResourceWithStreamingResponse,
)
from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .interfaces import (
    InterfacesResource,
    AsyncInterfacesResource,
    InterfacesResourceWithRawResponse,
    AsyncInterfacesResourceWithRawResponse,
    InterfacesResourceWithStreamingResponse,
    AsyncInterfacesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ....types.cloud import (
    instance_list_params,
    instance_action_params,
    instance_create_params,
    instance_delete_params,
    instance_resize_params,
    instance_update_params,
    instance_get_console_params,
    instance_assign_security_group_params,
    instance_add_to_placement_group_params,
    instance_unassign_security_group_params,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.console import Console
from ....types.cloud.instance import Instance
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.instance_interface import InstanceInterface
from ....types.cloud.tag_update_list_param import TagUpdateListParam

__all__ = ["InstancesResource", "AsyncInstancesResource"]


class InstancesResource(SyncAPIResource):
    @cached_property
    def flavors(self) -> FlavorsResource:
        return FlavorsResource(self._client)

    @cached_property
    def interfaces(self) -> InterfacesResource:
        return InterfacesResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def with_raw_response(self) -> InstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return InstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return InstancesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        interfaces: Iterable[instance_create_params.Interface],
        volumes: Iterable[instance_create_params.Volume],
        allow_app_ports: bool | NotGiven = NOT_GIVEN,
        configuration: Optional[object] | NotGiven = NOT_GIVEN,
        name_templates: List[str] | NotGiven = NOT_GIVEN,
        names: List[str] | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        security_groups: Iterable[instance_create_params.SecurityGroup] | NotGiven = NOT_GIVEN,
        servergroup_id: str | NotGiven = NOT_GIVEN,
        ssh_key_name: Optional[str] | NotGiven = NOT_GIVEN,
        tags: TagUpdateListParam | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create one or many instances or basic VMs.

        For Linux instances, use the
        'username' and 'password' to create a new user. When only 'password' is
        provided, it is set as the password for the default user of the image. The
        'user_data' is ignored when the 'password' is specified. Use the 'user_data'
        field to provide a cloud-init script in base64 to apply configurations to the
        instance. For Windows instances, the 'username' cannot be specified in the
        request. Use the 'password' field to set the password for the 'Admin' user on
        Windows. Use the 'user_data' field to provide a cloudbase-init script in base64
        to create new users on Windows. The password of the Admin user cannot be updated
        via 'user_data'.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}'].post.parameters[1].schema"

          flavor: '#/components/schemas/CreateInstanceSerializerV2/properties/flavor'
              "$.components.schemas.CreateInstanceSerializerV2.properties.flavor"

          interfaces: '#/components/schemas/CreateInstanceSerializerV2/properties/interfaces'
              "$.components.schemas.CreateInstanceSerializerV2.properties.interfaces"

          volumes: '#/components/schemas/CreateInstanceSerializerV2/properties/volumes'
              "$.components.schemas.CreateInstanceSerializerV2.properties.volumes"

          allow_app_ports: '#/components/schemas/CreateInstanceSerializerV2/properties/allow_app_ports'
              "$.components.schemas.CreateInstanceSerializerV2.properties.allow_app_ports"

          configuration: '#/components/schemas/CreateInstanceSerializerV2/properties/configuration/anyOf/0'
              "$.components.schemas.CreateInstanceSerializerV2.properties.configuration.anyOf[0]"

          name_templates: '#/components/schemas/CreateInstanceSerializerV2/properties/name_templates'
              "$.components.schemas.CreateInstanceSerializerV2.properties.name_templates"

          names: '#/components/schemas/CreateInstanceSerializerV2/properties/names'
              "$.components.schemas.CreateInstanceSerializerV2.properties.names"

          password: '#/components/schemas/CreateInstanceSerializerV2/properties/password'
              "$.components.schemas.CreateInstanceSerializerV2.properties.password"

          security_groups: '#/components/schemas/CreateInstanceSerializerV2/properties/security_groups'
              "$.components.schemas.CreateInstanceSerializerV2.properties.security_groups"

          servergroup_id: '#/components/schemas/CreateInstanceSerializerV2/properties/servergroup_id'
              "$.components.schemas.CreateInstanceSerializerV2.properties.servergroup_id"

          ssh_key_name: '#/components/schemas/CreateInstanceSerializerV2/properties/ssh_key_name/anyOf/0'
              "$.components.schemas.CreateInstanceSerializerV2.properties.ssh_key_name.anyOf[0]"

          tags: '#/components/schemas/CreateInstanceSerializerV2/properties/tags'
              "$.components.schemas.CreateInstanceSerializerV2.properties.tags"

          user_data: '#/components/schemas/CreateInstanceSerializerV2/properties/user_data'
              "$.components.schemas.CreateInstanceSerializerV2.properties.user_data"

          username: '#/components/schemas/CreateInstanceSerializerV2/properties/username'
              "$.components.schemas.CreateInstanceSerializerV2.properties.username"

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
            f"/cloud/v2/instances/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "flavor": flavor,
                    "interfaces": interfaces,
                    "volumes": volumes,
                    "allow_app_ports": allow_app_ports,
                    "configuration": configuration,
                    "name_templates": name_templates,
                    "names": names,
                    "password": password,
                    "security_groups": security_groups,
                    "servergroup_id": servergroup_id,
                    "ssh_key_name": ssh_key_name,
                    "tags": tags,
                    "user_data": user_data,
                    "username": username,
                },
                instance_create_params.InstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        Rename instance

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}'].patch.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}'].patch.parameters[2].schema"

          name: '#/components/schemas/NameSerializer/properties/name'
              "$.components.schemas.NameSerializer.properties.name"

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
        return self._patch(
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}",
            body=maybe_transform({"name": name}, instance_update_params.InstanceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        available_floating: bool | NotGiven = NOT_GIVEN,
        changes_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        changes_since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        exclude_flavor_prefix: str | NotGiven = NOT_GIVEN,
        exclude_secgroup: str | NotGiven = NOT_GIVEN,
        flavor_id: str | NotGiven = NOT_GIVEN,
        flavor_prefix: str | NotGiven = NOT_GIVEN,
        include_ai: bool | NotGiven = NOT_GIVEN,
        include_baremetal: bool | NotGiven = NOT_GIVEN,
        include_k8s: bool | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        only_isolated: bool | NotGiven = NOT_GIVEN,
        only_with_fixed_external_ip: bool | NotGiven = NOT_GIVEN,
        order_by: Literal["created.asc", "created.desc", "name.asc", "name.desc"] | NotGiven = NOT_GIVEN,
        profile_name: str | NotGiven = NOT_GIVEN,
        protection_status: Literal["Active", "Queued", "Error"] | NotGiven = NOT_GIVEN,
        status: Literal[
            "ACTIVE",
            "BUILD",
            "ERROR",
            "HARD_REBOOT",
            "MIGRATING",
            "PAUSED",
            "REBOOT",
            "REBUILD",
            "RESIZE",
            "REVERT_RESIZE",
            "SHELVED",
            "SHELVED_OFFLOADED",
            "SHUTOFF",
            "SOFT_DELETED",
            "SUSPENDED",
            "VERIFY_RESIZE",
        ]
        | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        tag_value: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> SyncOffsetPage[Instance]:
        """
        List instances

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[1].schema"

          available_floating: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[2]"

          changes_before: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[3]"

          changes_since: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[4]"

          exclude_flavor_prefix: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[5]"

          exclude_secgroup: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[6]"

          flavor_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[7]"

          flavor_prefix: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/8'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[8]"

          include_ai: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/9'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[9]"

          include_baremetal: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/10'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[10]"

          include_k8s: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/11'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[11]"

          ip: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/12'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[12]"

          limit: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/13'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[13]"

          name: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/14'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[14]"

          offset: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/15'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[15]"

          only_isolated: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/16'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[16]"

          only_with_fixed_external_ip: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/17'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[17]"

          order_by: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/18'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[18]"

          profile_name: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/19'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[19]"

          protection_status: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/20'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[20]"

          status: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/21'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[21]"

          tag_key_value: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/22'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[22]"

          tag_value: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/23'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[23]"

          type_ddos_profile: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/24'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[24]"

          uuid: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/25'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[25]"

          with_ddos: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/26'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[26]"

          with_interfaces_name: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/27'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[27]"

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
            f"/cloud/v1/instances/{project_id}/{region_id}",
            page=SyncOffsetPage[Instance],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "available_floating": available_floating,
                        "changes_before": changes_before,
                        "changes_since": changes_since,
                        "exclude_flavor_prefix": exclude_flavor_prefix,
                        "exclude_secgroup": exclude_secgroup,
                        "flavor_id": flavor_id,
                        "flavor_prefix": flavor_prefix,
                        "include_ai": include_ai,
                        "include_baremetal": include_baremetal,
                        "include_k8s": include_k8s,
                        "ip": ip,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "only_isolated": only_isolated,
                        "only_with_fixed_external_ip": only_with_fixed_external_ip,
                        "order_by": order_by,
                        "profile_name": profile_name,
                        "protection_status": protection_status,
                        "status": status,
                        "tag_key_value": tag_key_value,
                        "tag_value": tag_value,
                        "type_ddos_profile": type_ddos_profile,
                        "uuid": uuid,
                        "with_ddos": with_ddos,
                        "with_interfaces_name": with_interfaces_name,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            model=Instance,
        )

    def delete(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        delete_floatings: bool | NotGiven = NOT_GIVEN,
        floatings: str | NotGiven = NOT_GIVEN,
        reserved_fixed_ips: str | NotGiven = NOT_GIVEN,
        volumes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete instance

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[2].schema"

          delete_floatings: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/3'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[3]"

          floatings: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/4'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[4]"

          reserved_fixed_ips: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/5'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[5]"

          volumes: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/6'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[6]"

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
        return self._delete(
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "delete_floatings": delete_floatings,
                        "floatings": floatings,
                        "reserved_fixed_ips": reserved_fixed_ips,
                        "volumes": volumes,
                    },
                    instance_delete_params.InstanceDeleteParams,
                ),
            ),
            cast_to=TaskIDList,
        )

    @overload
    def action(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"],
        activate_profile: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        The action can be one of: start, stop, reboot, powercycle, suspend or resume.
        Suspend and resume are not available for baremetal instances.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/0/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/1/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/2/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[2].schema"

          action: '#/components/schemas/StartActionInstanceSerializer/properties/action'
              "$.components.schemas.StartActionInstanceSerializer.properties.action"

          activate_profile: '#/components/schemas/StartActionInstanceSerializer/properties/activate_profile/anyOf/0'
              "$.components.schemas.StartActionInstanceSerializer.properties.activate_profile.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def action(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["reboot", "reboot_hard", "resume", "stop", "suspend"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        The action can be one of: start, stop, reboot, powercycle, suspend or resume.
        Suspend and resume are not available for baremetal instances.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/0/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/1/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/2/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[2].schema"

          action: '#/components/schemas/BasicActionInstanceSerializer/properties/action'
              "$.components.schemas.BasicActionInstanceSerializer.properties.action"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["action"])
    def action(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"] | Literal["reboot", "reboot_hard", "resume", "stop", "suspend"],
        activate_profile: Optional[bool] | NotGiven = NOT_GIVEN,
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
            f"/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action",
            body=maybe_transform(
                {
                    "action": action,
                    "activate_profile": activate_profile,
                },
                instance_action_params.InstanceActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def add_to_placement_group(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        servergroup_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Put instance into the server group

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fput_into_servergroup/post/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/put_into_servergroup'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fput_into_servergroup/post/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/put_into_servergroup'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fput_into_servergroup/post/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/put_into_servergroup'].post.parameters[2].schema"

          servergroup_id: '#/components/schemas/InstancePutServerGroupSchema/properties/servergroup_id'
              "$.components.schemas.InstancePutServerGroupSchema.properties.servergroup_id"

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
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/put_into_servergroup",
            body=maybe_transform(
                {"servergroup_id": servergroup_id},
                instance_add_to_placement_group_params.InstanceAddToPlacementGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def assign_security_group(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | NotGiven = NOT_GIVEN,
        ports_security_group_names: Iterable[instance_assign_security_group_params.PortsSecurityGroupName]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Assign the security group to the server.

        To assign multiple security groups to
        all ports, use the NULL value for the port_id field

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faddsecuritygroup/post/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/addsecuritygroup'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faddsecuritygroup/post/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/addsecuritygroup'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faddsecuritygroup/post/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/addsecuritygroup'].post.parameters[2].schema"

          name: '#/components/schemas/InstancePortsSecurityGroupsSchema/properties/name'
              "$.components.schemas.InstancePortsSecurityGroupsSchema.properties.name"

          ports_security_group_names: '#/components/schemas/InstancePortsSecurityGroupsSchema/properties/ports_security_group_names'
              "$.components.schemas.InstancePortsSecurityGroupsSchema.properties.ports_security_group_names"

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/addsecuritygroup",
            body=maybe_transform(
                {
                    "name": name,
                    "ports_security_group_names": ports_security_group_names,
                },
                instance_assign_security_group_params.InstanceAssignSecurityGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def disable_port_security(
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
    ) -> InstanceInterface:
        """
        Disable port security for instance interface

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fports%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fdisable_port_security/post/parameters/0/schema'
              "$.paths['/cloud/v1/ports/{project_id}/{region_id}/{port_id}/disable_port_security'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fports%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fdisable_port_security/post/parameters/1/schema'
              "$.paths['/cloud/v1/ports/{project_id}/{region_id}/{port_id}/disable_port_security'].post.parameters[1].schema"

          port_id: '#/paths/%2Fcloud%2Fv1%2Fports%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fdisable_port_security/post/parameters/2/schema'
              "$.paths['/cloud/v1/ports/{project_id}/{region_id}/{port_id}/disable_port_security'].post.parameters[2].schema"

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
        return self._post(
            f"/cloud/v1/ports/{project_id}/{region_id}/{port_id}/disable_port_security",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceInterface,
        )

    def enable_port_security(
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
    ) -> InstanceInterface:
        """
        Enable port security for instance interface

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fports%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fenable_port_security/post/parameters/0/schema'
              "$.paths['/cloud/v1/ports/{project_id}/{region_id}/{port_id}/enable_port_security'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fports%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fenable_port_security/post/parameters/1/schema'
              "$.paths['/cloud/v1/ports/{project_id}/{region_id}/{port_id}/enable_port_security'].post.parameters[1].schema"

          port_id: '#/paths/%2Fcloud%2Fv1%2Fports%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fenable_port_security/post/parameters/2/schema'
              "$.paths['/cloud/v1/ports/{project_id}/{region_id}/{port_id}/enable_port_security'].post.parameters[2].schema"

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
        return self._post(
            f"/cloud/v1/ports/{project_id}/{region_id}/{port_id}/enable_port_security",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceInterface,
        )

    def get(
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
    ) -> Instance:
        """
        **Cookie Parameters**:

        - `language` (str, optional): Language for the response content. Affects the
          `ddos_profile` field. Supported values:
          - `'en'` (default)
          - `'de'`
          - `'ru'`

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}'].get.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}'].get.parameters[2].schema"

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
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def get_console(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        console_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Console:
        """
        Get instance console URL

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[2].schema"

          console_type: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/3'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[3]"

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
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/get_console",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"console_type": console_type}, instance_get_console_params.InstanceGetConsoleParams
                ),
            ),
            cast_to=Console,
        )

    def remove_from_placement_group(
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
    ) -> TaskIDList:
        """
        Remove instance from the server group

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fremove_from_servergroup/post/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/remove_from_servergroup'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fremove_from_servergroup/post/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/remove_from_servergroup'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fremove_from_servergroup/post/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/remove_from_servergroup'].post.parameters[2].schema"

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
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/remove_from_servergroup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def resize(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Change flavor of the instance

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fchangeflavor/post/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/changeflavor'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fchangeflavor/post/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/changeflavor'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fchangeflavor/post/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/changeflavor'].post.parameters[2].schema"

          flavor_id: '#/components/schemas/FlavorIdSchema/properties/flavor_id'
              "$.components.schemas.FlavorIdSchema.properties.flavor_id"

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
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/changeflavor",
            body=maybe_transform({"flavor_id": flavor_id}, instance_resize_params.InstanceResizeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def unassign_security_group(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | NotGiven = NOT_GIVEN,
        ports_security_group_names: Iterable[instance_unassign_security_group_params.PortsSecurityGroupName]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Un-assign the security group to the server.

        To un-assign multiple security
        groups to all ports, use the NULL value for the port_id field

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdelsecuritygroup/post/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/delsecuritygroup'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdelsecuritygroup/post/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/delsecuritygroup'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdelsecuritygroup/post/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/delsecuritygroup'].post.parameters[2].schema"

          name: '#/components/schemas/InstancePortsSecurityGroupsSchema/properties/name'
              "$.components.schemas.InstancePortsSecurityGroupsSchema.properties.name"

          ports_security_group_names: '#/components/schemas/InstancePortsSecurityGroupsSchema/properties/ports_security_group_names'
              "$.components.schemas.InstancePortsSecurityGroupsSchema.properties.ports_security_group_names"

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/delsecuritygroup",
            body=maybe_transform(
                {
                    "name": name,
                    "ports_security_group_names": ports_security_group_names,
                },
                instance_unassign_security_group_params.InstanceUnassignSecurityGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncInstancesResource(AsyncAPIResource):
    @cached_property
    def flavors(self) -> AsyncFlavorsResource:
        return AsyncFlavorsResource(self._client)

    @cached_property
    def interfaces(self) -> AsyncInterfacesResource:
        return AsyncInterfacesResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncInstancesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        interfaces: Iterable[instance_create_params.Interface],
        volumes: Iterable[instance_create_params.Volume],
        allow_app_ports: bool | NotGiven = NOT_GIVEN,
        configuration: Optional[object] | NotGiven = NOT_GIVEN,
        name_templates: List[str] | NotGiven = NOT_GIVEN,
        names: List[str] | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        security_groups: Iterable[instance_create_params.SecurityGroup] | NotGiven = NOT_GIVEN,
        servergroup_id: str | NotGiven = NOT_GIVEN,
        ssh_key_name: Optional[str] | NotGiven = NOT_GIVEN,
        tags: TagUpdateListParam | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create one or many instances or basic VMs.

        For Linux instances, use the
        'username' and 'password' to create a new user. When only 'password' is
        provided, it is set as the password for the default user of the image. The
        'user_data' is ignored when the 'password' is specified. Use the 'user_data'
        field to provide a cloud-init script in base64 to apply configurations to the
        instance. For Windows instances, the 'username' cannot be specified in the
        request. Use the 'password' field to set the password for the 'Admin' user on
        Windows. Use the 'user_data' field to provide a cloudbase-init script in base64
        to create new users on Windows. The password of the Admin user cannot be updated
        via 'user_data'.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}'].post.parameters[1].schema"

          flavor: '#/components/schemas/CreateInstanceSerializerV2/properties/flavor'
              "$.components.schemas.CreateInstanceSerializerV2.properties.flavor"

          interfaces: '#/components/schemas/CreateInstanceSerializerV2/properties/interfaces'
              "$.components.schemas.CreateInstanceSerializerV2.properties.interfaces"

          volumes: '#/components/schemas/CreateInstanceSerializerV2/properties/volumes'
              "$.components.schemas.CreateInstanceSerializerV2.properties.volumes"

          allow_app_ports: '#/components/schemas/CreateInstanceSerializerV2/properties/allow_app_ports'
              "$.components.schemas.CreateInstanceSerializerV2.properties.allow_app_ports"

          configuration: '#/components/schemas/CreateInstanceSerializerV2/properties/configuration/anyOf/0'
              "$.components.schemas.CreateInstanceSerializerV2.properties.configuration.anyOf[0]"

          name_templates: '#/components/schemas/CreateInstanceSerializerV2/properties/name_templates'
              "$.components.schemas.CreateInstanceSerializerV2.properties.name_templates"

          names: '#/components/schemas/CreateInstanceSerializerV2/properties/names'
              "$.components.schemas.CreateInstanceSerializerV2.properties.names"

          password: '#/components/schemas/CreateInstanceSerializerV2/properties/password'
              "$.components.schemas.CreateInstanceSerializerV2.properties.password"

          security_groups: '#/components/schemas/CreateInstanceSerializerV2/properties/security_groups'
              "$.components.schemas.CreateInstanceSerializerV2.properties.security_groups"

          servergroup_id: '#/components/schemas/CreateInstanceSerializerV2/properties/servergroup_id'
              "$.components.schemas.CreateInstanceSerializerV2.properties.servergroup_id"

          ssh_key_name: '#/components/schemas/CreateInstanceSerializerV2/properties/ssh_key_name/anyOf/0'
              "$.components.schemas.CreateInstanceSerializerV2.properties.ssh_key_name.anyOf[0]"

          tags: '#/components/schemas/CreateInstanceSerializerV2/properties/tags'
              "$.components.schemas.CreateInstanceSerializerV2.properties.tags"

          user_data: '#/components/schemas/CreateInstanceSerializerV2/properties/user_data'
              "$.components.schemas.CreateInstanceSerializerV2.properties.user_data"

          username: '#/components/schemas/CreateInstanceSerializerV2/properties/username'
              "$.components.schemas.CreateInstanceSerializerV2.properties.username"

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
            f"/cloud/v2/instances/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "flavor": flavor,
                    "interfaces": interfaces,
                    "volumes": volumes,
                    "allow_app_ports": allow_app_ports,
                    "configuration": configuration,
                    "name_templates": name_templates,
                    "names": names,
                    "password": password,
                    "security_groups": security_groups,
                    "servergroup_id": servergroup_id,
                    "ssh_key_name": ssh_key_name,
                    "tags": tags,
                    "user_data": user_data,
                    "username": username,
                },
                instance_create_params.InstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        Rename instance

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}'].patch.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}'].patch.parameters[2].schema"

          name: '#/components/schemas/NameSerializer/properties/name'
              "$.components.schemas.NameSerializer.properties.name"

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
        return await self._patch(
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}",
            body=await async_maybe_transform({"name": name}, instance_update_params.InstanceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        available_floating: bool | NotGiven = NOT_GIVEN,
        changes_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        changes_since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        exclude_flavor_prefix: str | NotGiven = NOT_GIVEN,
        exclude_secgroup: str | NotGiven = NOT_GIVEN,
        flavor_id: str | NotGiven = NOT_GIVEN,
        flavor_prefix: str | NotGiven = NOT_GIVEN,
        include_ai: bool | NotGiven = NOT_GIVEN,
        include_baremetal: bool | NotGiven = NOT_GIVEN,
        include_k8s: bool | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        only_isolated: bool | NotGiven = NOT_GIVEN,
        only_with_fixed_external_ip: bool | NotGiven = NOT_GIVEN,
        order_by: Literal["created.asc", "created.desc", "name.asc", "name.desc"] | NotGiven = NOT_GIVEN,
        profile_name: str | NotGiven = NOT_GIVEN,
        protection_status: Literal["Active", "Queued", "Error"] | NotGiven = NOT_GIVEN,
        status: Literal[
            "ACTIVE",
            "BUILD",
            "ERROR",
            "HARD_REBOOT",
            "MIGRATING",
            "PAUSED",
            "REBOOT",
            "REBUILD",
            "RESIZE",
            "REVERT_RESIZE",
            "SHELVED",
            "SHELVED_OFFLOADED",
            "SHUTOFF",
            "SOFT_DELETED",
            "SUSPENDED",
            "VERIFY_RESIZE",
        ]
        | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        tag_value: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[Instance, AsyncOffsetPage[Instance]]:
        """
        List instances

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[1].schema"

          available_floating: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[2]"

          changes_before: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[3]"

          changes_since: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[4]"

          exclude_flavor_prefix: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[5]"

          exclude_secgroup: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[6]"

          flavor_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[7]"

          flavor_prefix: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/8'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[8]"

          include_ai: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/9'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[9]"

          include_baremetal: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/10'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[10]"

          include_k8s: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/11'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[11]"

          ip: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/12'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[12]"

          limit: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/13'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[13]"

          name: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/14'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[14]"

          offset: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/15'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[15]"

          only_isolated: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/16'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[16]"

          only_with_fixed_external_ip: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/17'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[17]"

          order_by: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/18'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[18]"

          profile_name: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/19'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[19]"

          protection_status: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/20'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[20]"

          status: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/21'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[21]"

          tag_key_value: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/22'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[22]"

          tag_value: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/23'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[23]"

          type_ddos_profile: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/24'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[24]"

          uuid: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/25'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[25]"

          with_ddos: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/26'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[26]"

          with_interfaces_name: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/27'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}'].get.parameters[27]"

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
            f"/cloud/v1/instances/{project_id}/{region_id}",
            page=AsyncOffsetPage[Instance],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "available_floating": available_floating,
                        "changes_before": changes_before,
                        "changes_since": changes_since,
                        "exclude_flavor_prefix": exclude_flavor_prefix,
                        "exclude_secgroup": exclude_secgroup,
                        "flavor_id": flavor_id,
                        "flavor_prefix": flavor_prefix,
                        "include_ai": include_ai,
                        "include_baremetal": include_baremetal,
                        "include_k8s": include_k8s,
                        "ip": ip,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "only_isolated": only_isolated,
                        "only_with_fixed_external_ip": only_with_fixed_external_ip,
                        "order_by": order_by,
                        "profile_name": profile_name,
                        "protection_status": protection_status,
                        "status": status,
                        "tag_key_value": tag_key_value,
                        "tag_value": tag_value,
                        "type_ddos_profile": type_ddos_profile,
                        "uuid": uuid,
                        "with_ddos": with_ddos,
                        "with_interfaces_name": with_interfaces_name,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            model=Instance,
        )

    async def delete(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        delete_floatings: bool | NotGiven = NOT_GIVEN,
        floatings: str | NotGiven = NOT_GIVEN,
        reserved_fixed_ips: str | NotGiven = NOT_GIVEN,
        volumes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete instance

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[2].schema"

          delete_floatings: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/3'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[3]"

          floatings: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/4'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[4]"

          reserved_fixed_ips: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/5'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[5]"

          volumes: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/delete/parameters/6'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}']['delete'].parameters[6]"

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
        return await self._delete(
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "delete_floatings": delete_floatings,
                        "floatings": floatings,
                        "reserved_fixed_ips": reserved_fixed_ips,
                        "volumes": volumes,
                    },
                    instance_delete_params.InstanceDeleteParams,
                ),
            ),
            cast_to=TaskIDList,
        )

    @overload
    async def action(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"],
        activate_profile: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        The action can be one of: start, stop, reboot, powercycle, suspend or resume.
        Suspend and resume are not available for baremetal instances.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/0/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/1/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/2/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[2].schema"

          action: '#/components/schemas/StartActionInstanceSerializer/properties/action'
              "$.components.schemas.StartActionInstanceSerializer.properties.action"

          activate_profile: '#/components/schemas/StartActionInstanceSerializer/properties/activate_profile/anyOf/0'
              "$.components.schemas.StartActionInstanceSerializer.properties.activate_profile.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def action(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["reboot", "reboot_hard", "resume", "stop", "suspend"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        The action can be one of: start, stop, reboot, powercycle, suspend or resume.
        Suspend and resume are not available for baremetal instances.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/0/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/1/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/2/schema'
              "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[2].schema"

          action: '#/components/schemas/BasicActionInstanceSerializer/properties/action'
              "$.components.schemas.BasicActionInstanceSerializer.properties.action"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["action"])
    async def action(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"] | Literal["reboot", "reboot_hard", "resume", "stop", "suspend"],
        activate_profile: Optional[bool] | NotGiven = NOT_GIVEN,
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
            f"/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "activate_profile": activate_profile,
                },
                instance_action_params.InstanceActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def add_to_placement_group(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        servergroup_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Put instance into the server group

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fput_into_servergroup/post/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/put_into_servergroup'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fput_into_servergroup/post/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/put_into_servergroup'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fput_into_servergroup/post/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/put_into_servergroup'].post.parameters[2].schema"

          servergroup_id: '#/components/schemas/InstancePutServerGroupSchema/properties/servergroup_id'
              "$.components.schemas.InstancePutServerGroupSchema.properties.servergroup_id"

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
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/put_into_servergroup",
            body=await async_maybe_transform(
                {"servergroup_id": servergroup_id},
                instance_add_to_placement_group_params.InstanceAddToPlacementGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def assign_security_group(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | NotGiven = NOT_GIVEN,
        ports_security_group_names: Iterable[instance_assign_security_group_params.PortsSecurityGroupName]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Assign the security group to the server.

        To assign multiple security groups to
        all ports, use the NULL value for the port_id field

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faddsecuritygroup/post/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/addsecuritygroup'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faddsecuritygroup/post/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/addsecuritygroup'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faddsecuritygroup/post/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/addsecuritygroup'].post.parameters[2].schema"

          name: '#/components/schemas/InstancePortsSecurityGroupsSchema/properties/name'
              "$.components.schemas.InstancePortsSecurityGroupsSchema.properties.name"

          ports_security_group_names: '#/components/schemas/InstancePortsSecurityGroupsSchema/properties/ports_security_group_names'
              "$.components.schemas.InstancePortsSecurityGroupsSchema.properties.ports_security_group_names"

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/addsecuritygroup",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "ports_security_group_names": ports_security_group_names,
                },
                instance_assign_security_group_params.InstanceAssignSecurityGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def disable_port_security(
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
    ) -> InstanceInterface:
        """
        Disable port security for instance interface

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fports%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fdisable_port_security/post/parameters/0/schema'
              "$.paths['/cloud/v1/ports/{project_id}/{region_id}/{port_id}/disable_port_security'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fports%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fdisable_port_security/post/parameters/1/schema'
              "$.paths['/cloud/v1/ports/{project_id}/{region_id}/{port_id}/disable_port_security'].post.parameters[1].schema"

          port_id: '#/paths/%2Fcloud%2Fv1%2Fports%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fdisable_port_security/post/parameters/2/schema'
              "$.paths['/cloud/v1/ports/{project_id}/{region_id}/{port_id}/disable_port_security'].post.parameters[2].schema"

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
        return await self._post(
            f"/cloud/v1/ports/{project_id}/{region_id}/{port_id}/disable_port_security",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceInterface,
        )

    async def enable_port_security(
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
    ) -> InstanceInterface:
        """
        Enable port security for instance interface

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fports%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fenable_port_security/post/parameters/0/schema'
              "$.paths['/cloud/v1/ports/{project_id}/{region_id}/{port_id}/enable_port_security'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fports%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fenable_port_security/post/parameters/1/schema'
              "$.paths['/cloud/v1/ports/{project_id}/{region_id}/{port_id}/enable_port_security'].post.parameters[1].schema"

          port_id: '#/paths/%2Fcloud%2Fv1%2Fports%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fenable_port_security/post/parameters/2/schema'
              "$.paths['/cloud/v1/ports/{project_id}/{region_id}/{port_id}/enable_port_security'].post.parameters[2].schema"

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
        return await self._post(
            f"/cloud/v1/ports/{project_id}/{region_id}/{port_id}/enable_port_security",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceInterface,
        )

    async def get(
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
    ) -> Instance:
        """
        **Cookie Parameters**:

        - `language` (str, optional): Language for the response content. Affects the
          `ddos_profile` field. Supported values:
          - `'en'` (default)
          - `'de'`
          - `'ru'`

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}'].get.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}'].get.parameters[2].schema"

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
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    async def get_console(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        console_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Console:
        """
        Get instance console URL

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[2].schema"

          console_type: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fget_console/get/parameters/3'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/get_console'].get.parameters[3]"

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
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/get_console",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"console_type": console_type}, instance_get_console_params.InstanceGetConsoleParams
                ),
            ),
            cast_to=Console,
        )

    async def remove_from_placement_group(
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
    ) -> TaskIDList:
        """
        Remove instance from the server group

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fremove_from_servergroup/post/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/remove_from_servergroup'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fremove_from_servergroup/post/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/remove_from_servergroup'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fremove_from_servergroup/post/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/remove_from_servergroup'].post.parameters[2].schema"

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
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/remove_from_servergroup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def resize(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Change flavor of the instance

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fchangeflavor/post/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/changeflavor'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fchangeflavor/post/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/changeflavor'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fchangeflavor/post/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/changeflavor'].post.parameters[2].schema"

          flavor_id: '#/components/schemas/FlavorIdSchema/properties/flavor_id'
              "$.components.schemas.FlavorIdSchema.properties.flavor_id"

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
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/changeflavor",
            body=await async_maybe_transform({"flavor_id": flavor_id}, instance_resize_params.InstanceResizeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def unassign_security_group(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | NotGiven = NOT_GIVEN,
        ports_security_group_names: Iterable[instance_unassign_security_group_params.PortsSecurityGroupName]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Un-assign the security group to the server.

        To un-assign multiple security
        groups to all ports, use the NULL value for the port_id field

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdelsecuritygroup/post/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/delsecuritygroup'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdelsecuritygroup/post/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/delsecuritygroup'].post.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdelsecuritygroup/post/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/delsecuritygroup'].post.parameters[2].schema"

          name: '#/components/schemas/InstancePortsSecurityGroupsSchema/properties/name'
              "$.components.schemas.InstancePortsSecurityGroupsSchema.properties.name"

          ports_security_group_names: '#/components/schemas/InstancePortsSecurityGroupsSchema/properties/ports_security_group_names'
              "$.components.schemas.InstancePortsSecurityGroupsSchema.properties.ports_security_group_names"

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/delsecuritygroup",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "ports_security_group_names": ports_security_group_names,
                },
                instance_unassign_security_group_params.InstanceUnassignSecurityGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class InstancesResourceWithRawResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.create = to_raw_response_wrapper(
            instances.create,
        )
        self.update = to_raw_response_wrapper(
            instances.update,
        )
        self.list = to_raw_response_wrapper(
            instances.list,
        )
        self.delete = to_raw_response_wrapper(
            instances.delete,
        )
        self.action = to_raw_response_wrapper(
            instances.action,
        )
        self.add_to_placement_group = to_raw_response_wrapper(
            instances.add_to_placement_group,
        )
        self.assign_security_group = to_raw_response_wrapper(
            instances.assign_security_group,
        )
        self.disable_port_security = to_raw_response_wrapper(
            instances.disable_port_security,
        )
        self.enable_port_security = to_raw_response_wrapper(
            instances.enable_port_security,
        )
        self.get = to_raw_response_wrapper(
            instances.get,
        )
        self.get_console = to_raw_response_wrapper(
            instances.get_console,
        )
        self.remove_from_placement_group = to_raw_response_wrapper(
            instances.remove_from_placement_group,
        )
        self.resize = to_raw_response_wrapper(
            instances.resize,
        )
        self.unassign_security_group = to_raw_response_wrapper(
            instances.unassign_security_group,
        )

    @cached_property
    def flavors(self) -> FlavorsResourceWithRawResponse:
        return FlavorsResourceWithRawResponse(self._instances.flavors)

    @cached_property
    def interfaces(self) -> InterfacesResourceWithRawResponse:
        return InterfacesResourceWithRawResponse(self._instances.interfaces)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._instances.images)

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._instances.metrics)


class AsyncInstancesResourceWithRawResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.create = async_to_raw_response_wrapper(
            instances.create,
        )
        self.update = async_to_raw_response_wrapper(
            instances.update,
        )
        self.list = async_to_raw_response_wrapper(
            instances.list,
        )
        self.delete = async_to_raw_response_wrapper(
            instances.delete,
        )
        self.action = async_to_raw_response_wrapper(
            instances.action,
        )
        self.add_to_placement_group = async_to_raw_response_wrapper(
            instances.add_to_placement_group,
        )
        self.assign_security_group = async_to_raw_response_wrapper(
            instances.assign_security_group,
        )
        self.disable_port_security = async_to_raw_response_wrapper(
            instances.disable_port_security,
        )
        self.enable_port_security = async_to_raw_response_wrapper(
            instances.enable_port_security,
        )
        self.get = async_to_raw_response_wrapper(
            instances.get,
        )
        self.get_console = async_to_raw_response_wrapper(
            instances.get_console,
        )
        self.remove_from_placement_group = async_to_raw_response_wrapper(
            instances.remove_from_placement_group,
        )
        self.resize = async_to_raw_response_wrapper(
            instances.resize,
        )
        self.unassign_security_group = async_to_raw_response_wrapper(
            instances.unassign_security_group,
        )

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithRawResponse:
        return AsyncFlavorsResourceWithRawResponse(self._instances.flavors)

    @cached_property
    def interfaces(self) -> AsyncInterfacesResourceWithRawResponse:
        return AsyncInterfacesResourceWithRawResponse(self._instances.interfaces)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._instances.images)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._instances.metrics)


class InstancesResourceWithStreamingResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.create = to_streamed_response_wrapper(
            instances.create,
        )
        self.update = to_streamed_response_wrapper(
            instances.update,
        )
        self.list = to_streamed_response_wrapper(
            instances.list,
        )
        self.delete = to_streamed_response_wrapper(
            instances.delete,
        )
        self.action = to_streamed_response_wrapper(
            instances.action,
        )
        self.add_to_placement_group = to_streamed_response_wrapper(
            instances.add_to_placement_group,
        )
        self.assign_security_group = to_streamed_response_wrapper(
            instances.assign_security_group,
        )
        self.disable_port_security = to_streamed_response_wrapper(
            instances.disable_port_security,
        )
        self.enable_port_security = to_streamed_response_wrapper(
            instances.enable_port_security,
        )
        self.get = to_streamed_response_wrapper(
            instances.get,
        )
        self.get_console = to_streamed_response_wrapper(
            instances.get_console,
        )
        self.remove_from_placement_group = to_streamed_response_wrapper(
            instances.remove_from_placement_group,
        )
        self.resize = to_streamed_response_wrapper(
            instances.resize,
        )
        self.unassign_security_group = to_streamed_response_wrapper(
            instances.unassign_security_group,
        )

    @cached_property
    def flavors(self) -> FlavorsResourceWithStreamingResponse:
        return FlavorsResourceWithStreamingResponse(self._instances.flavors)

    @cached_property
    def interfaces(self) -> InterfacesResourceWithStreamingResponse:
        return InterfacesResourceWithStreamingResponse(self._instances.interfaces)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._instances.images)

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._instances.metrics)


class AsyncInstancesResourceWithStreamingResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.create = async_to_streamed_response_wrapper(
            instances.create,
        )
        self.update = async_to_streamed_response_wrapper(
            instances.update,
        )
        self.list = async_to_streamed_response_wrapper(
            instances.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            instances.delete,
        )
        self.action = async_to_streamed_response_wrapper(
            instances.action,
        )
        self.add_to_placement_group = async_to_streamed_response_wrapper(
            instances.add_to_placement_group,
        )
        self.assign_security_group = async_to_streamed_response_wrapper(
            instances.assign_security_group,
        )
        self.disable_port_security = async_to_streamed_response_wrapper(
            instances.disable_port_security,
        )
        self.enable_port_security = async_to_streamed_response_wrapper(
            instances.enable_port_security,
        )
        self.get = async_to_streamed_response_wrapper(
            instances.get,
        )
        self.get_console = async_to_streamed_response_wrapper(
            instances.get_console,
        )
        self.remove_from_placement_group = async_to_streamed_response_wrapper(
            instances.remove_from_placement_group,
        )
        self.resize = async_to_streamed_response_wrapper(
            instances.resize,
        )
        self.unassign_security_group = async_to_streamed_response_wrapper(
            instances.unassign_security_group,
        )

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithStreamingResponse:
        return AsyncFlavorsResourceWithStreamingResponse(self._instances.flavors)

    @cached_property
    def interfaces(self) -> AsyncInterfacesResourceWithStreamingResponse:
        return AsyncInterfacesResourceWithStreamingResponse(self._instances.interfaces)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._instances.images)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._instances.metrics)

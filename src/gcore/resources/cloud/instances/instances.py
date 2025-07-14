# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
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

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return InstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
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
        name: str | NotGiven = NOT_GIVEN,
        name_template: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        security_groups: Iterable[instance_create_params.SecurityGroup] | NotGiven = NOT_GIVEN,
        servergroup_id: str | NotGiven = NOT_GIVEN,
        ssh_key_name: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create an instance with specified configuration.

        How to get access: For Linux,

        - Use the `user_data` field to provide a
          [cloud-init script](https://cloudinit.readthedocs.io/en/latest/reference/examples.html)
          in base64 to apply configurations to the instance.
        - Specify the `username` and `password` to create a new user.
        - When only `password` is provided, it is set as the password for the default
          user of the image.
        - The `user_data` is ignored when the `password` is specified. For Windows,
        - Use the `user_data` field to provide a
          [cloudbase-init script](https://cloudbase-init.readthedocs.io/en/latest/userdata.html#cloud-config)
          in base64 to create new users on Windows.
        - Use the `password` field to set the password for the 'Admin' user on Windows.
        - The password of the Admin user cannot be updated via `user_data`.
        - The `username` cannot be specified in the request.

        Args:
          project_id: Project ID

          region_id: Region ID

          flavor: The flavor of the instance.

          interfaces: A list of network interfaces for the instance. You can create one or more
              interfaces - private, public, or both.

          volumes: List of volumes that will be attached to the instance.

          allow_app_ports: Set to `true` if creating the instance from an `apptemplate`. This allows
              application ports in the security group for instances created from a marketplace
              application template.

          configuration: Parameters for the application template if creating the instance from an
              `apptemplate`.

          name: Instance name.

          name_template: If you want the instance name to be automatically generated based on IP
              addresses, you can provide a name template instead of specifying the name
              manually. The template should include a placeholder that will be replaced during
              provisioning. Supported placeholders are: `{`ip_octets`}` (last 3 octets of the
              IP), `{`two_ip_octets`}`, and `{`one_ip_octet`}`.

          password: For Linux instances, 'username' and 'password' are used to create a new user.
              When only 'password' is provided, it is set as the password for the default user
              of the image. For Windows instances, 'username' cannot be specified. Use the
              'password' field to set the password for the 'Admin' user on Windows. Use the
              '`user_data`' field to provide a script to create new users on Windows. The
              password of the Admin user cannot be updated via '`user_data`'.

          security_groups: Specifies security group UUIDs to be applied to all instance network interfaces.

          servergroup_id:
              Placement group ID for instance placement policy. Supported group types:

              - `anti-affinity`: Ensures instances are placed on different hosts for high
                availability.
              - `affinity`: Places instances on the same host for low-latency communication.
              - `soft-anti-affinity`: Tries to place instances on different hosts but allows
                sharing if needed.

          ssh_key_name: Specifies the name of the SSH keypair, created via the
              [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          user_data: String in base64 format. For Linux instances, '`user_data`' is ignored when
              'password' field is provided. For Windows instances, Admin user password is set
              by 'password' field and cannot be updated via '`user_data`'. Examples of the
              `user_data`: https://cloudinit.readthedocs.io/en/latest/topics/examples.html

          username: For Linux instances, 'username' and 'password' are used to create a new user.
              For Windows instances, 'username' cannot be specified. Use 'password' field to
              set the password for the 'Admin' user on Windows.

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
                    "name": name,
                    "name_template": name_template,
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

    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        interfaces: Iterable[instance_create_params.Interface],
        volumes: Iterable[instance_create_params.Volume],
        allow_app_ports: bool | NotGiven = NOT_GIVEN,
        configuration: Optional[object] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        name_template: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        security_groups: Iterable[instance_create_params.SecurityGroup] | NotGiven = NOT_GIVEN,
        servergroup_id: str | NotGiven = NOT_GIVEN,
        ssh_key_name: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """Create one or many instances or basic VMs and poll for the result."""
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            interfaces=interfaces,
            volumes=volumes,
            allow_app_ports=allow_app_ports,
            configuration=configuration,
            name_template=name_template,
            name=name,
            password=password,
            security_groups=security_groups,
            servergroup_id=servergroup_id,
            ssh_key_name=ssh_key_name,
            tags=tags,
            user_data=user_data,
            username=username,
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
        )
        if (
            not task.created_resources
            or not task.created_resources.instances
            or len(task.created_resources.instances) != 1
        ):
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return self.get(
            instance_id=task.created_resources.instances[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
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
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          name: Name.

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
        """List all instances in the specified project and region.

        Results can be filtered
        by various parameters like name, status, and IP address.

        Args:
          project_id: Project ID

          region_id: Region ID

          available_floating: Only show instances which are able to handle floating address

          changes_before: Filters the instances by a date and time stamp when the instances last changed.

          changes_since: Filters the instances by a date and time stamp when the instances last changed
              status.

          exclude_flavor_prefix: Exclude instances with specified flavor prefix

          exclude_secgroup: Exclude instances with specified security group name

          flavor_id: Filter out instances by `flavor_id`. Flavor id must match exactly.

          flavor_prefix: Filter out instances by `flavor_prefix`.

          include_ai: Include GPU clusters' servers

          include_baremetal: Include bare metal servers. Please, use `GET /v1/bminstances/` instead

          include_k8s: Include managed k8s worker nodes

          ip: An IPv4 address to filter results by. Note: partial matches are allowed. For
              example, searching for 192.168.0.1 will return 192.168.0.1, 192.168.0.10,
              192.168.0.110, and so on.

          limit: Optional. Limit the number of returned items

          name: Filter instances by name. You can provide a full or partial name, instances with
              matching names will be returned. For example, entering 'test' will return all
              instances that contain 'test' in their name.

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          only_isolated: Include only isolated instances

          only_with_fixed_external_ip: Return bare metals only with external fixed IP addresses.

          order_by: Order by field and direction.

          profile_name: Filter result by ddos protection profile name. Effective only with `with_ddos`
              set to true.

          protection_status: Filter result by DDoS `protection_status`. if parameter is provided. Effective
              only with `with_ddos` set to true. (Active, Queued or Error)

          status: Filters instances by status.

          tag_key_value: Optional. Filter by tag key-value pairs.

          tag_value: Optional. Filter by tag values. ?`tag_value`=value1&`tag_value`=value2

          type_ddos_profile: Return bare metals either only with advanced or only basic DDoS protection.
              Effective only with `with_ddos` set to true. (advanced or basic)

          uuid: Filter the server list result by the UUID of the server. Allowed UUID part

          with_ddos: Include DDoS profile information in the response when set to `true`. Otherwise,
              the `ddos_profile` field in the response is `null` by default.

          with_interfaces_name: Include `interface_name` in the addresses

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
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          delete_floatings: True if it is required to delete floating IPs assigned to the instance. Can't be
              used with `floatings`.

          floatings: Comma separated list of floating ids that should be deleted. Can't be used with
              `delete_floatings`.

          reserved_fixed_ips: Comma separated list of port IDs to be deleted with the instance

          volumes: Comma separated list of volume IDs to be deleted with the instance

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

    def delete_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        delete_floatings: bool | NotGiven = NOT_GIVEN,
        floatings: str | NotGiven = NOT_GIVEN,
        reserved_fixed_ips: str | NotGiven = NOT_GIVEN,
        volumes: str | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            delete_floatings=delete_floatings,
            floatings=floatings,
            reserved_fixed_ips=reserved_fixed_ips,
            volumes=volumes,
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
        Suspend and resume are not available for bare metal instances.

        Args:
          action: Instance action name

          activate_profile: Used on start instance to activate Advanced DDoS profile

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
        Suspend and resume are not available for bare metal instances.

        Args:
          action: Instance action name

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
        """Add an instance to a server group.

        The instance must not already be in a server
        group. Bare metal servers do not support server groups.

        Args:
          servergroup_id: Anti-affinity or affinity or soft-anti-affinity server group ID.

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

    def add_to_placement_group_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        servergroup_id: str,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        Put instance into the server group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.add_to_placement_group(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            servergroup_id=servergroup_id,
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
        )
        return self.get(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
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
        all ports, use the NULL value for the `port_id` field

        Args:
          name: Security group name, applies to all ports

          ports_security_group_names: Port security groups mapping

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
        """Retrieve detailed information about a specific instance.

        The response content
        language for `ddos_profile` can be controlled via the 'language' cookie
        parameter. **Cookie Parameters**:

        - `language` (str, optional): Language for the response content. Affects the
          `ddos_profile` field. Supported values:
        - `'en'` (default)
        - `'de'`
        - `'ru'`

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

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
          console_type: Console type

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
        """Remove an instance from its current server group.

        The instance must be in a
        server group to be removed. Bare metal servers do not support server groups.

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
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/remove_from_servergroup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def remove_from_placement_group_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        Remove instance from the server group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.remove_from_placement_group(
            instance_id=instance_id,
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
        )
        return self.get(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
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
          flavor_id: Flavor ID

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

    def resize_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor_id: str,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        Change flavor of the instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.resize(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            flavor_id=flavor_id,
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
        )
        return self.get(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
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
        groups to all ports, use the NULL value for the `port_id` field

        Args:
          name: Security group name, applies to all ports

          ports_security_group_names: Port security groups mapping

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

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
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
        name: str | NotGiven = NOT_GIVEN,
        name_template: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        security_groups: Iterable[instance_create_params.SecurityGroup] | NotGiven = NOT_GIVEN,
        servergroup_id: str | NotGiven = NOT_GIVEN,
        ssh_key_name: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create an instance with specified configuration.

        How to get access: For Linux,

        - Use the `user_data` field to provide a
          [cloud-init script](https://cloudinit.readthedocs.io/en/latest/reference/examples.html)
          in base64 to apply configurations to the instance.
        - Specify the `username` and `password` to create a new user.
        - When only `password` is provided, it is set as the password for the default
          user of the image.
        - The `user_data` is ignored when the `password` is specified. For Windows,
        - Use the `user_data` field to provide a
          [cloudbase-init script](https://cloudbase-init.readthedocs.io/en/latest/userdata.html#cloud-config)
          in base64 to create new users on Windows.
        - Use the `password` field to set the password for the 'Admin' user on Windows.
        - The password of the Admin user cannot be updated via `user_data`.
        - The `username` cannot be specified in the request.

        Args:
          project_id: Project ID

          region_id: Region ID

          flavor: The flavor of the instance.

          interfaces: A list of network interfaces for the instance. You can create one or more
              interfaces - private, public, or both.

          volumes: List of volumes that will be attached to the instance.

          allow_app_ports: Set to `true` if creating the instance from an `apptemplate`. This allows
              application ports in the security group for instances created from a marketplace
              application template.

          configuration: Parameters for the application template if creating the instance from an
              `apptemplate`.

          name: Instance name.

          name_template: If you want the instance name to be automatically generated based on IP
              addresses, you can provide a name template instead of specifying the name
              manually. The template should include a placeholder that will be replaced during
              provisioning. Supported placeholders are: `{`ip_octets`}` (last 3 octets of the
              IP), `{`two_ip_octets`}`, and `{`one_ip_octet`}`.

          password: For Linux instances, 'username' and 'password' are used to create a new user.
              When only 'password' is provided, it is set as the password for the default user
              of the image. For Windows instances, 'username' cannot be specified. Use the
              'password' field to set the password for the 'Admin' user on Windows. Use the
              '`user_data`' field to provide a script to create new users on Windows. The
              password of the Admin user cannot be updated via '`user_data`'.

          security_groups: Specifies security group UUIDs to be applied to all instance network interfaces.

          servergroup_id:
              Placement group ID for instance placement policy. Supported group types:

              - `anti-affinity`: Ensures instances are placed on different hosts for high
                availability.
              - `affinity`: Places instances on the same host for low-latency communication.
              - `soft-anti-affinity`: Tries to place instances on different hosts but allows
                sharing if needed.

          ssh_key_name: Specifies the name of the SSH keypair, created via the
              [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          user_data: String in base64 format. For Linux instances, '`user_data`' is ignored when
              'password' field is provided. For Windows instances, Admin user password is set
              by 'password' field and cannot be updated via '`user_data`'. Examples of the
              `user_data`: https://cloudinit.readthedocs.io/en/latest/topics/examples.html

          username: For Linux instances, 'username' and 'password' are used to create a new user.
              For Windows instances, 'username' cannot be specified. Use 'password' field to
              set the password for the 'Admin' user on Windows.

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
                    "name": name,
                    "name_template": name_template,
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

    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        interfaces: Iterable[instance_create_params.Interface],
        volumes: Iterable[instance_create_params.Volume],
        allow_app_ports: bool | NotGiven = NOT_GIVEN,
        configuration: Optional[object] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        name_template: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        security_groups: Iterable[instance_create_params.SecurityGroup] | NotGiven = NOT_GIVEN,
        servergroup_id: str | NotGiven = NOT_GIVEN,
        ssh_key_name: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """Create one or many instances or basic VMs and poll for the result."""
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            interfaces=interfaces,
            volumes=volumes,
            allow_app_ports=allow_app_ports,
            configuration=configuration,
            name_template=name_template,
            name=name,
            password=password,
            security_groups=security_groups,
            servergroup_id=servergroup_id,
            ssh_key_name=ssh_key_name,
            tags=tags,
            user_data=user_data,
            username=username,
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
        )
        if (
            not task.created_resources
            or not task.created_resources.instances
            or len(task.created_resources.instances) != 1
        ):
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return await self.get(
            instance_id=task.created_resources.instances[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
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
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          name: Name.

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
        """List all instances in the specified project and region.

        Results can be filtered
        by various parameters like name, status, and IP address.

        Args:
          project_id: Project ID

          region_id: Region ID

          available_floating: Only show instances which are able to handle floating address

          changes_before: Filters the instances by a date and time stamp when the instances last changed.

          changes_since: Filters the instances by a date and time stamp when the instances last changed
              status.

          exclude_flavor_prefix: Exclude instances with specified flavor prefix

          exclude_secgroup: Exclude instances with specified security group name

          flavor_id: Filter out instances by `flavor_id`. Flavor id must match exactly.

          flavor_prefix: Filter out instances by `flavor_prefix`.

          include_ai: Include GPU clusters' servers

          include_baremetal: Include bare metal servers. Please, use `GET /v1/bminstances/` instead

          include_k8s: Include managed k8s worker nodes

          ip: An IPv4 address to filter results by. Note: partial matches are allowed. For
              example, searching for 192.168.0.1 will return 192.168.0.1, 192.168.0.10,
              192.168.0.110, and so on.

          limit: Optional. Limit the number of returned items

          name: Filter instances by name. You can provide a full or partial name, instances with
              matching names will be returned. For example, entering 'test' will return all
              instances that contain 'test' in their name.

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          only_isolated: Include only isolated instances

          only_with_fixed_external_ip: Return bare metals only with external fixed IP addresses.

          order_by: Order by field and direction.

          profile_name: Filter result by ddos protection profile name. Effective only with `with_ddos`
              set to true.

          protection_status: Filter result by DDoS `protection_status`. if parameter is provided. Effective
              only with `with_ddos` set to true. (Active, Queued or Error)

          status: Filters instances by status.

          tag_key_value: Optional. Filter by tag key-value pairs.

          tag_value: Optional. Filter by tag values. ?`tag_value`=value1&`tag_value`=value2

          type_ddos_profile: Return bare metals either only with advanced or only basic DDoS protection.
              Effective only with `with_ddos` set to true. (advanced or basic)

          uuid: Filter the server list result by the UUID of the server. Allowed UUID part

          with_ddos: Include DDoS profile information in the response when set to `true`. Otherwise,
              the `ddos_profile` field in the response is `null` by default.

          with_interfaces_name: Include `interface_name` in the addresses

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
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          delete_floatings: True if it is required to delete floating IPs assigned to the instance. Can't be
              used with `floatings`.

          floatings: Comma separated list of floating ids that should be deleted. Can't be used with
              `delete_floatings`.

          reserved_fixed_ips: Comma separated list of port IDs to be deleted with the instance

          volumes: Comma separated list of volume IDs to be deleted with the instance

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

    async def delete_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        delete_floatings: bool | NotGiven = NOT_GIVEN,
        floatings: str | NotGiven = NOT_GIVEN,
        reserved_fixed_ips: str | NotGiven = NOT_GIVEN,
        volumes: str | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            delete_floatings=delete_floatings,
            floatings=floatings,
            reserved_fixed_ips=reserved_fixed_ips,
            volumes=volumes,
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
        Suspend and resume are not available for bare metal instances.

        Args:
          action: Instance action name

          activate_profile: Used on start instance to activate Advanced DDoS profile

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
        Suspend and resume are not available for bare metal instances.

        Args:
          action: Instance action name

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
        """Add an instance to a server group.

        The instance must not already be in a server
        group. Bare metal servers do not support server groups.

        Args:
          servergroup_id: Anti-affinity or affinity or soft-anti-affinity server group ID.

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

    async def add_to_placement_group_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        servergroup_id: str,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        Put instance into the server group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.add_to_placement_group(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            servergroup_id=servergroup_id,
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
        )
        return await self.get(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
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
        all ports, use the NULL value for the `port_id` field

        Args:
          name: Security group name, applies to all ports

          ports_security_group_names: Port security groups mapping

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
        """Retrieve detailed information about a specific instance.

        The response content
        language for `ddos_profile` can be controlled via the 'language' cookie
        parameter. **Cookie Parameters**:

        - `language` (str, optional): Language for the response content. Affects the
          `ddos_profile` field. Supported values:
        - `'en'` (default)
        - `'de'`
        - `'ru'`

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

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
          console_type: Console type

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
        """Remove an instance from its current server group.

        The instance must be in a
        server group to be removed. Bare metal servers do not support server groups.

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
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/remove_from_servergroup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def remove_from_placement_group_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        Remove instance from the server group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.remove_from_placement_group(
            instance_id=instance_id,
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
        )
        return await self.get(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
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
          flavor_id: Flavor ID

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

    async def resize_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor_id: str,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        Change flavor of the instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.resize(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            flavor_id=flavor_id,
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
        )
        return await self.get(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
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
        groups to all ports, use the NULL value for the `port_id` field

        Args:
          name: Security group name, applies to all ports

          ports_security_group_names: Port security groups mapping

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

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal

import httpx

from .images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from .console import (
    ConsoleResource,
    AsyncConsoleResource,
    ConsoleResourceWithRawResponse,
    AsyncConsoleResourceWithRawResponse,
    ConsoleResourceWithStreamingResponse,
    AsyncConsoleResourceWithStreamingResponse,
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
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
    instance_list_params,
    instance_action_params,
    instance_create_params,
    instance_delete_params,
    instance_update_params,
    instance_rebuild_params,
)
from .resize_flavors import (
    ResizeFlavorsResource,
    AsyncResizeFlavorsResource,
    ResizeFlavorsResourceWithRawResponse,
    AsyncResizeFlavorsResourceWithRawResponse,
    ResizeFlavorsResourceWithStreamingResponse,
    AsyncResizeFlavorsResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from .instances_custom import InstancesResourceCustomMixin, AsyncInstancesResourceCustomMixin
from ....types.cloud.instance import Instance
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.tag_update_map_param import TagUpdateMapParam
from ....types.cloud.instance_delete_response import InstanceDeleteResponse

__all__ = ["InstancesResource", "AsyncInstancesResource"]


class InstancesResource(InstancesResourceCustomMixin, SyncAPIResource):
    """
    Instances are cloud virtual machines that boot from a volume and connect to networks through ports, in any region of the project.
    """

    @cached_property
    def console(self) -> ConsoleResource:
        return ConsoleResource(self._client)

    @cached_property
    def resize_flavors(self) -> ResizeFlavorsResource:
        return ResizeFlavorsResource(self._client)

    @cached_property
    def flavors(self) -> FlavorsResource:
        """
        Instance flavors define the CPU, memory, and OS type of an instance, in all regions of the project.
        """
        return FlavorsResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        """
        Instance images are operating system images (public, private, or shared) used to boot cloud instances.
        """
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
        boot_volume_id: str,
        flavor_name: str,
        interfaces: Iterable[instance_create_params.Interface],
        region_id: int,
        dry_run: bool | Omit = omit,
        data_volume_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        password: str | Omit = omit,
        placement_group_id: str | Omit = omit,
        ssh_key_id: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        user_data: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Create a virtual instance that boots from a volume.

        The instance uses a volume
        and ports that you create first, in the region of the instance.

        To create one:

        1. Pick an image with [List images](#operation/ImagesViewSet.get).
        2. [Create a volume](#operation/VolumeViewSet.post) from the image. Wait until
           its status is `available`.
        3. Pick a flavor with
           [List instance flavors](#operation/GlobalInstanceFlavorListView.get). Send
           `compatible_with_boot_volume_id` to get only the flavors that can boot the
           volume.
        4. [Create a port](#operation/GlobalPortListView.post). A body with only
           `region_id` gives one public IPv4 address.

        You can also attach more volumes, put the instance in a
        [placement group](#operation/GlobalPlacementGroupListView.post), and add an
        [SSH key](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).

        The response holds the IDs of the tasks that create the instance.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real create.

        Args:
          project_id: Project ID.

          boot_volume_id: Pre-created boot volume UUID.

          flavor_name: Name of an instance flavor with no GPU. Use
              `GET /v1/projects/{project_id}/instances/flavors` to list them.

          interfaces: Pre-created ports to attach, in NIC/boot order.

          region_id: Region to provision the instance in.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          data_volume_ids: Pre-created data volume UUIDs to attach.

          name: Instance name. If you omit it, the name template of the account gives the name.
              Without a template, the name is generated. The account can forbid custom names.
              Then the name must be equal to the name that the template gives.

          password: Password of the default user. No response returns it. A Windows image needs a
              password. For a Windows image, the create checks these rules: the password has a
              minimum of 6 characters, it contains no word 'admin', and it contains 3 of these
              character types: digits, lowercase letters, uppercase letters, other characters.
              For a Linux image, the password enables SSH login with a password. Send
              `password` or `user_data`, not both.

          placement_group_id: Pre-created placement group UUID for affinity/anti-affinity.

          ssh_key_id: ID of the SSH key to add to the default user.

          tags: Customer-owned key-value tags.

          user_data: cloud-init user data, raw or base64. Up to 65535 bytes once decoded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._post(
            path_template("/cloud/v1/projects/{project_id}/instances", project_id=project_id),
            body=maybe_transform(
                {
                    "boot_volume_id": boot_volume_id,
                    "flavor_name": flavor_name,
                    "interfaces": interfaces,
                    "region_id": region_id,
                    "data_volume_ids": data_volume_ids,
                    "name": name,
                    "password": password,
                    "placement_group_id": placement_group_id,
                    "ssh_key_id": ssh_key_id,
                    "tags": tags,
                    "user_data": user_data,
                },
                instance_create_params.InstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dry_run": dry_run}, instance_create_params.InstanceCreateParams),
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        dry_run: bool | Omit = omit,
        data_volume_ids: SequenceNotStr[str] | Omit = omit,
        flavor_name: str | Omit = omit,
        interfaces: Iterable[instance_update_params.Interface] | Omit = omit,
        name: str | Omit = omit,
        placement_group_id: Optional[str] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Send only the fields to change.

        One task makes all the changes. A field with the
        current value changes nothing.

        - Rename: send `name`.
        - Resize: send `flavor_name`. Pick it with
          [List instance resize flavors](#operation/GlobalInstanceResizeFlavorListView.get).
          A resize restarts the instance.
        - Add a port: [create a port](#operation/GlobalPortListView.post). Then send
          `interfaces` with the current ports in their current order and the new port at
          the end.
        - Remove a port: send `interfaces` without that port. The port stays and you can
          use it again. For a port change, the instance `status` must be `active` or
          `stopped`. Resume a suspended instance first.
        - Attach or detach a data volume: send the full list in `data_volume_ids`. A new
          volume must be `available`.
        - Move to a [placement group](#operation/GlobalPlacementGroupListView.post):
          send `placement_group_id`. Send `null` to remove the instance from its group.
          The instance `status` must be `active`. The instance can move to another host.
        - Change tags: send `tags` as a JSON Merge Patch.

        To change the security groups,
        [update the ports](#operation/GlobalPortDetailView.patch). You cannot change
        `boot_volume_id` or `ssh_key_id`. To change them, create a new instance.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real update. If a resize exceeds a quota, the error names every quota that
        it exceeds.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          data_volume_ids: Full list of the data volumes of the instance. Volumes that are not in the list
              are detached. New volumes are attached.

          flavor_name: Name of the new flavor. The instance is resized to this flavor.

          interfaces: Full list of the ports of the instance. Ports that are not in the list are
              detached. New ports are attached. Keep the current ports in their current order.

          name: Instance name.

          placement_group_id: ID of the placement group. Send null to remove the instance from its placement
              group.

          tags: Tags as JSON Merge Patch. A key with the value null removes that tag. The value
              null removes all tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._patch(
            path_template(
                "/cloud/v1/projects/{project_id}/instances/{instance_id}",
                project_id=project_id,
                instance_id=instance_id,
            ),
            body=maybe_transform(
                {
                    "data_volume_ids": data_volume_ids,
                    "flavor_name": flavor_name,
                    "interfaces": interfaces,
                    "name": name,
                    "placement_group_id": placement_group_id,
                    "tags": tags,
                },
                instance_update_params.InstanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dry_run": dry_run}, instance_update_params.InstanceUpdateParams),
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        created_at: instance_list_params.CreatedAt | Omit = omit,
        flavor_name: instance_list_params.FlavorName | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        ip_address: instance_list_params.IPAddress | Omit = omit,
        limit: int | Omit = omit,
        managed: bool | Omit = omit,
        managed_by: Literal["k8s_cluster"] | Omit = omit,
        managed_by_resource_ids: SequenceNotStr[str] | Omit = omit,
        managed_by_resource_names: SequenceNotStr[str] | Omit = omit,
        name: instance_list_params.Name | Omit = omit,
        network_ids: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal[
            "created_at.asc",
            "created_at.desc",
            "name.asc",
            "name.desc",
            "region_id.asc",
            "region_id.desc",
            "status.asc",
            "status.desc",
        ]
        | Omit = omit,
        region_ids: Iterable[int] | Omit = omit,
        security_group_ids: SequenceNotStr[str] | Omit = omit,
        statuses: List[
            Literal[
                "active",
                "deleted",
                "deleting",
                "error",
                "provisioning",
                "rebooting",
                "rebuilding",
                "resizing",
                "stopped",
                "unknown",
                "updating",
            ]
        ]
        | Omit = omit,
        subnet_ids: SequenceNotStr[str] | Omit = omit,
        tag_key: instance_list_params.TagKey | Omit = omit,
        tag_value: instance_list_params.TagValue | Omit = omit,
        tags: Dict[str, SequenceNotStr[str]] | Omit = omit,
        updated_at: instance_list_params.UpdatedAt | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[Instance]:
        """
        List a project's instances across all regions.

        Args:
          project_id: Project ID.

          created_at: Range filter on creation time.

          flavor_name: Operator flavor name filter.

          ids: Filter by instance UUID(s).

          ip_address: Filter by an IP address of a port of the instance. The filter compares the fixed
              IPs and the floating IPs of the port.

          limit: Max items to return.

          managed: Filter by managed status. true = managed by a service, false =
              customer-operated.

          managed_by: Filter by manager type, e.g. `k8s_cluster`.

          managed_by_resource_ids: Filter by managing resource ID(s).

          managed_by_resource_names: Filter by managing resource name(s).

          name: Operator name filter, e.g. name[contains]=web.

          network_ids: Filter by network ID(s) the instance has a port on.

          offset: Items to skip.

          order_by: Sort field and direction.

          region_ids: Filter by region ID(s). Omit = all regions.

          security_group_ids: Filter by security group ID(s).

          statuses: Filter by lifecycle status(es).

          subnet_ids: Filter by subnet ID(s).

          tag_key: Filter by tag key regardless of value, e.g. `tag_key[contains]=team`.

          tag_value: Filter by tag value regardless of key, e.g. `tag_value[prefix]=prod`.

          tags: Filter by exact tag key-value pairs, e.g. `tags[env]=prod&tags[team]=core`.
              Repeat a key to match any of several values for it, e.g.
              `tags[env]=prod&tags[env]=dev`. Values for one key are ORed, different keys are
              ANDed; values match case-insensitively.

          updated_at: Range filter on last-update time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            path_template("/cloud/v1/projects/{project_id}/instances", project_id=project_id),
            page=SyncOffsetPage[Instance],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "flavor_name": flavor_name,
                        "ids": ids,
                        "ip_address": ip_address,
                        "limit": limit,
                        "managed": managed,
                        "managed_by": managed_by,
                        "managed_by_resource_ids": managed_by_resource_ids,
                        "managed_by_resource_names": managed_by_resource_names,
                        "name": name,
                        "network_ids": network_ids,
                        "offset": offset,
                        "order_by": order_by,
                        "region_ids": region_ids,
                        "security_group_ids": security_group_ids,
                        "statuses": statuses,
                        "subnet_ids": subnet_ids,
                        "tag_key": tag_key,
                        "tag_value": tag_value,
                        "tags": tags,
                        "updated_at": updated_at,
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
        all_floating_ips: bool | Omit = omit,
        all_ports: bool | Omit = omit,
        all_volumes: bool | Omit = omit,
        dry_run: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        port_ids: SequenceNotStr[str] | Omit = omit,
        volume_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceDeleteResponse:
        """Cascade-delete volumes, ports, floating IPs based on preservation params.

        By
        default, all are preserved (detached/disassociated).

        `resources_to_delete` holds:

        - the instance itself;
        - the volumes that `volume_ids` names, or every volume if `all_volumes` is
          `true`, and the snapshots of these volumes;
        - the ports that `port_ids` names, or every port if `all_ports` is `true`, and
          the sub-ports of their trunks;
        - the floating IPs that `floating_ip_ids` names, or every floating IP if
          `all_floating_ips` is `true`.

        `resources_to_preserve` holds every other volume, port, sub-port and floating IP
        of the instance. A floating IP on a deleted port stays, with no port.

        [`DELETE /v1/instances/{project_id}/{region_id}/{instance_id}`](#operation/InstanceInstanceViewSet.delete)
        is different. It deletes every port, except the reserved fixed IPs that
        `reserved_fixed_ips` does not name.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array and the same two lists. A failed check
        returns the same error as the real delete.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          all_floating_ips: Delete all associated floating IPs (default: preserve).

          all_ports: Delete all attached ports (default: preserve).

          all_volumes: Delete all attached volumes (default: preserve).

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          floating_ip_ids: Delete only these floating IP IDs (mutually exclusive with `all_floating_ips`).

          port_ids: Delete only these port IDs (mutually exclusive with `all_ports`).

          volume_ids: Delete only these volume IDs (mutually exclusive with `all_volumes`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._delete(
            path_template(
                "/cloud/v1/projects/{project_id}/instances/{instance_id}",
                project_id=project_id,
                instance_id=instance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "all_floating_ips": all_floating_ips,
                        "all_ports": all_ports,
                        "all_volumes": all_volumes,
                        "dry_run": dry_run,
                        "floating_ip_ids": floating_ip_ids,
                        "port_ids": port_ids,
                        "volume_ids": volume_ids,
                    },
                    instance_delete_params.InstanceDeleteParams,
                ),
            ),
            cast_to=InstanceDeleteResponse,
        )

    def action(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        action: Literal["reboot", "reboot_hard", "resume", "start", "stop", "suspend"],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Change the power state of an instance.

        The action is one of: `start`, `stop`,
        `reboot`, `reboot_hard`, `suspend` or `resume`. The action does not change the
        Advanced DDoS profile of the instance. Use the DDoS profile resource to activate
        or to deactivate protection. Returns the ID of the task that runs the action.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real action.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          action: Power action to run on the instance. `reboot_hard` replaces the legacy
              `powercycle` action.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            path_template(
                "/cloud/v1/projects/{project_id}/instances/{instance_id}/action",
                project_id=project_id,
                instance_id=instance_id,
            ),
            body=maybe_transform({"action": action}, instance_action_params.InstanceActionParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dry_run": dry_run}, instance_action_params.InstanceActionParams),
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Returns a single instance by ID, resolved across all regions.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template(
                "/cloud/v1/projects/{project_id}/instances/{instance_id}",
                project_id=project_id,
                instance_id=instance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def rebuild(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | Omit = omit,
        ssh_key_name: Optional[str] | Omit = omit,
        user_data: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Rebuild instance with a new image while preserving its configuration.

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          image_id: Image ID. If you omit it, the instance keeps the current image.

          ssh_key_name: Specifies the name of the SSH keypair, created via the
              [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).
              Use null to remove the SSH key from the instance. If you omit it, the instance
              keeps the current SSH key.

          user_data:
              String in base64 format. Examples of the `user_data`:
              https://cloudinit.readthedocs.io/en/latest/topics/examples.html. If you omit it,
              the instance keeps the current user data.

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
            path_template(
                "/cloud/v3/instances/{project_id}/{region_id}/{instance_id}/rebuild",
                project_id=project_id,
                region_id=region_id,
                instance_id=instance_id,
            ),
            body=maybe_transform(
                {
                    "image_id": image_id,
                    "ssh_key_name": ssh_key_name,
                    "user_data": user_data,
                },
                instance_rebuild_params.InstanceRebuildParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class AsyncInstancesResource(AsyncInstancesResourceCustomMixin, AsyncAPIResource):
    """
    Instances are cloud virtual machines that boot from a volume and connect to networks through ports, in any region of the project.
    """

    @cached_property
    def console(self) -> AsyncConsoleResource:
        return AsyncConsoleResource(self._client)

    @cached_property
    def resize_flavors(self) -> AsyncResizeFlavorsResource:
        return AsyncResizeFlavorsResource(self._client)

    @cached_property
    def flavors(self) -> AsyncFlavorsResource:
        """
        Instance flavors define the CPU, memory, and OS type of an instance, in all regions of the project.
        """
        return AsyncFlavorsResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        """
        Instance images are operating system images (public, private, or shared) used to boot cloud instances.
        """
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
        boot_volume_id: str,
        flavor_name: str,
        interfaces: Iterable[instance_create_params.Interface],
        region_id: int,
        dry_run: bool | Omit = omit,
        data_volume_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        password: str | Omit = omit,
        placement_group_id: str | Omit = omit,
        ssh_key_id: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        user_data: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Create a virtual instance that boots from a volume.

        The instance uses a volume
        and ports that you create first, in the region of the instance.

        To create one:

        1. Pick an image with [List images](#operation/ImagesViewSet.get).
        2. [Create a volume](#operation/VolumeViewSet.post) from the image. Wait until
           its status is `available`.
        3. Pick a flavor with
           [List instance flavors](#operation/GlobalInstanceFlavorListView.get). Send
           `compatible_with_boot_volume_id` to get only the flavors that can boot the
           volume.
        4. [Create a port](#operation/GlobalPortListView.post). A body with only
           `region_id` gives one public IPv4 address.

        You can also attach more volumes, put the instance in a
        [placement group](#operation/GlobalPlacementGroupListView.post), and add an
        [SSH key](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).

        The response holds the IDs of the tasks that create the instance.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real create.

        Args:
          project_id: Project ID.

          boot_volume_id: Pre-created boot volume UUID.

          flavor_name: Name of an instance flavor with no GPU. Use
              `GET /v1/projects/{project_id}/instances/flavors` to list them.

          interfaces: Pre-created ports to attach, in NIC/boot order.

          region_id: Region to provision the instance in.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          data_volume_ids: Pre-created data volume UUIDs to attach.

          name: Instance name. If you omit it, the name template of the account gives the name.
              Without a template, the name is generated. The account can forbid custom names.
              Then the name must be equal to the name that the template gives.

          password: Password of the default user. No response returns it. A Windows image needs a
              password. For a Windows image, the create checks these rules: the password has a
              minimum of 6 characters, it contains no word 'admin', and it contains 3 of these
              character types: digits, lowercase letters, uppercase letters, other characters.
              For a Linux image, the password enables SSH login with a password. Send
              `password` or `user_data`, not both.

          placement_group_id: Pre-created placement group UUID for affinity/anti-affinity.

          ssh_key_id: ID of the SSH key to add to the default user.

          tags: Customer-owned key-value tags.

          user_data: cloud-init user data, raw or base64. Up to 65535 bytes once decoded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return await self._post(
            path_template("/cloud/v1/projects/{project_id}/instances", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "boot_volume_id": boot_volume_id,
                    "flavor_name": flavor_name,
                    "interfaces": interfaces,
                    "region_id": region_id,
                    "data_volume_ids": data_volume_ids,
                    "name": name,
                    "password": password,
                    "placement_group_id": placement_group_id,
                    "ssh_key_id": ssh_key_id,
                    "tags": tags,
                    "user_data": user_data,
                },
                instance_create_params.InstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dry_run": dry_run}, instance_create_params.InstanceCreateParams),
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        dry_run: bool | Omit = omit,
        data_volume_ids: SequenceNotStr[str] | Omit = omit,
        flavor_name: str | Omit = omit,
        interfaces: Iterable[instance_update_params.Interface] | Omit = omit,
        name: str | Omit = omit,
        placement_group_id: Optional[str] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Send only the fields to change.

        One task makes all the changes. A field with the
        current value changes nothing.

        - Rename: send `name`.
        - Resize: send `flavor_name`. Pick it with
          [List instance resize flavors](#operation/GlobalInstanceResizeFlavorListView.get).
          A resize restarts the instance.
        - Add a port: [create a port](#operation/GlobalPortListView.post). Then send
          `interfaces` with the current ports in their current order and the new port at
          the end.
        - Remove a port: send `interfaces` without that port. The port stays and you can
          use it again. For a port change, the instance `status` must be `active` or
          `stopped`. Resume a suspended instance first.
        - Attach or detach a data volume: send the full list in `data_volume_ids`. A new
          volume must be `available`.
        - Move to a [placement group](#operation/GlobalPlacementGroupListView.post):
          send `placement_group_id`. Send `null` to remove the instance from its group.
          The instance `status` must be `active`. The instance can move to another host.
        - Change tags: send `tags` as a JSON Merge Patch.

        To change the security groups,
        [update the ports](#operation/GlobalPortDetailView.patch). You cannot change
        `boot_volume_id` or `ssh_key_id`. To change them, create a new instance.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real update. If a resize exceeds a quota, the error names every quota that
        it exceeds.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          data_volume_ids: Full list of the data volumes of the instance. Volumes that are not in the list
              are detached. New volumes are attached.

          flavor_name: Name of the new flavor. The instance is resized to this flavor.

          interfaces: Full list of the ports of the instance. Ports that are not in the list are
              detached. New ports are attached. Keep the current ports in their current order.

          name: Instance name.

          placement_group_id: ID of the placement group. Send null to remove the instance from its placement
              group.

          tags: Tags as JSON Merge Patch. A key with the value null removes that tag. The value
              null removes all tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._patch(
            path_template(
                "/cloud/v1/projects/{project_id}/instances/{instance_id}",
                project_id=project_id,
                instance_id=instance_id,
            ),
            body=await async_maybe_transform(
                {
                    "data_volume_ids": data_volume_ids,
                    "flavor_name": flavor_name,
                    "interfaces": interfaces,
                    "name": name,
                    "placement_group_id": placement_group_id,
                    "tags": tags,
                },
                instance_update_params.InstanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dry_run": dry_run}, instance_update_params.InstanceUpdateParams),
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        created_at: instance_list_params.CreatedAt | Omit = omit,
        flavor_name: instance_list_params.FlavorName | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        ip_address: instance_list_params.IPAddress | Omit = omit,
        limit: int | Omit = omit,
        managed: bool | Omit = omit,
        managed_by: Literal["k8s_cluster"] | Omit = omit,
        managed_by_resource_ids: SequenceNotStr[str] | Omit = omit,
        managed_by_resource_names: SequenceNotStr[str] | Omit = omit,
        name: instance_list_params.Name | Omit = omit,
        network_ids: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal[
            "created_at.asc",
            "created_at.desc",
            "name.asc",
            "name.desc",
            "region_id.asc",
            "region_id.desc",
            "status.asc",
            "status.desc",
        ]
        | Omit = omit,
        region_ids: Iterable[int] | Omit = omit,
        security_group_ids: SequenceNotStr[str] | Omit = omit,
        statuses: List[
            Literal[
                "active",
                "deleted",
                "deleting",
                "error",
                "provisioning",
                "rebooting",
                "rebuilding",
                "resizing",
                "stopped",
                "unknown",
                "updating",
            ]
        ]
        | Omit = omit,
        subnet_ids: SequenceNotStr[str] | Omit = omit,
        tag_key: instance_list_params.TagKey | Omit = omit,
        tag_value: instance_list_params.TagValue | Omit = omit,
        tags: Dict[str, SequenceNotStr[str]] | Omit = omit,
        updated_at: instance_list_params.UpdatedAt | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Instance, AsyncOffsetPage[Instance]]:
        """
        List a project's instances across all regions.

        Args:
          project_id: Project ID.

          created_at: Range filter on creation time.

          flavor_name: Operator flavor name filter.

          ids: Filter by instance UUID(s).

          ip_address: Filter by an IP address of a port of the instance. The filter compares the fixed
              IPs and the floating IPs of the port.

          limit: Max items to return.

          managed: Filter by managed status. true = managed by a service, false =
              customer-operated.

          managed_by: Filter by manager type, e.g. `k8s_cluster`.

          managed_by_resource_ids: Filter by managing resource ID(s).

          managed_by_resource_names: Filter by managing resource name(s).

          name: Operator name filter, e.g. name[contains]=web.

          network_ids: Filter by network ID(s) the instance has a port on.

          offset: Items to skip.

          order_by: Sort field and direction.

          region_ids: Filter by region ID(s). Omit = all regions.

          security_group_ids: Filter by security group ID(s).

          statuses: Filter by lifecycle status(es).

          subnet_ids: Filter by subnet ID(s).

          tag_key: Filter by tag key regardless of value, e.g. `tag_key[contains]=team`.

          tag_value: Filter by tag value regardless of key, e.g. `tag_value[prefix]=prod`.

          tags: Filter by exact tag key-value pairs, e.g. `tags[env]=prod&tags[team]=core`.
              Repeat a key to match any of several values for it, e.g.
              `tags[env]=prod&tags[env]=dev`. Values for one key are ORed, different keys are
              ANDed; values match case-insensitively.

          updated_at: Range filter on last-update time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            path_template("/cloud/v1/projects/{project_id}/instances", project_id=project_id),
            page=AsyncOffsetPage[Instance],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "flavor_name": flavor_name,
                        "ids": ids,
                        "ip_address": ip_address,
                        "limit": limit,
                        "managed": managed,
                        "managed_by": managed_by,
                        "managed_by_resource_ids": managed_by_resource_ids,
                        "managed_by_resource_names": managed_by_resource_names,
                        "name": name,
                        "network_ids": network_ids,
                        "offset": offset,
                        "order_by": order_by,
                        "region_ids": region_ids,
                        "security_group_ids": security_group_ids,
                        "statuses": statuses,
                        "subnet_ids": subnet_ids,
                        "tag_key": tag_key,
                        "tag_value": tag_value,
                        "tags": tags,
                        "updated_at": updated_at,
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
        all_floating_ips: bool | Omit = omit,
        all_ports: bool | Omit = omit,
        all_volumes: bool | Omit = omit,
        dry_run: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        port_ids: SequenceNotStr[str] | Omit = omit,
        volume_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceDeleteResponse:
        """Cascade-delete volumes, ports, floating IPs based on preservation params.

        By
        default, all are preserved (detached/disassociated).

        `resources_to_delete` holds:

        - the instance itself;
        - the volumes that `volume_ids` names, or every volume if `all_volumes` is
          `true`, and the snapshots of these volumes;
        - the ports that `port_ids` names, or every port if `all_ports` is `true`, and
          the sub-ports of their trunks;
        - the floating IPs that `floating_ip_ids` names, or every floating IP if
          `all_floating_ips` is `true`.

        `resources_to_preserve` holds every other volume, port, sub-port and floating IP
        of the instance. A floating IP on a deleted port stays, with no port.

        [`DELETE /v1/instances/{project_id}/{region_id}/{instance_id}`](#operation/InstanceInstanceViewSet.delete)
        is different. It deletes every port, except the reserved fixed IPs that
        `reserved_fixed_ips` does not name.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array and the same two lists. A failed check
        returns the same error as the real delete.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          all_floating_ips: Delete all associated floating IPs (default: preserve).

          all_ports: Delete all attached ports (default: preserve).

          all_volumes: Delete all attached volumes (default: preserve).

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          floating_ip_ids: Delete only these floating IP IDs (mutually exclusive with `all_floating_ips`).

          port_ids: Delete only these port IDs (mutually exclusive with `all_ports`).

          volume_ids: Delete only these volume IDs (mutually exclusive with `all_volumes`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._delete(
            path_template(
                "/cloud/v1/projects/{project_id}/instances/{instance_id}",
                project_id=project_id,
                instance_id=instance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "all_floating_ips": all_floating_ips,
                        "all_ports": all_ports,
                        "all_volumes": all_volumes,
                        "dry_run": dry_run,
                        "floating_ip_ids": floating_ip_ids,
                        "port_ids": port_ids,
                        "volume_ids": volume_ids,
                    },
                    instance_delete_params.InstanceDeleteParams,
                ),
            ),
            cast_to=InstanceDeleteResponse,
        )

    async def action(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        action: Literal["reboot", "reboot_hard", "resume", "start", "stop", "suspend"],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Change the power state of an instance.

        The action is one of: `start`, `stop`,
        `reboot`, `reboot_hard`, `suspend` or `resume`. The action does not change the
        Advanced DDoS profile of the instance. Use the DDoS profile resource to activate
        or to deactivate protection. Returns the ID of the task that runs the action.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real action.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          action: Power action to run on the instance. `reboot_hard` replaces the legacy
              `powercycle` action.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            path_template(
                "/cloud/v1/projects/{project_id}/instances/{instance_id}/action",
                project_id=project_id,
                instance_id=instance_id,
            ),
            body=await async_maybe_transform({"action": action}, instance_action_params.InstanceActionParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dry_run": dry_run}, instance_action_params.InstanceActionParams),
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Returns a single instance by ID, resolved across all regions.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template(
                "/cloud/v1/projects/{project_id}/instances/{instance_id}",
                project_id=project_id,
                instance_id=instance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    async def rebuild(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | Omit = omit,
        ssh_key_name: Optional[str] | Omit = omit,
        user_data: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Rebuild instance with a new image while preserving its configuration.

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          image_id: Image ID. If you omit it, the instance keeps the current image.

          ssh_key_name: Specifies the name of the SSH keypair, created via the
              [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).
              Use null to remove the SSH key from the instance. If you omit it, the instance
              keeps the current SSH key.

          user_data:
              String in base64 format. Examples of the `user_data`:
              https://cloudinit.readthedocs.io/en/latest/topics/examples.html. If you omit it,
              the instance keeps the current user data.

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
            path_template(
                "/cloud/v3/instances/{project_id}/{region_id}/{instance_id}/rebuild",
                project_id=project_id,
                region_id=region_id,
                instance_id=instance_id,
            ),
            body=await async_maybe_transform(
                {
                    "image_id": image_id,
                    "ssh_key_name": ssh_key_name,
                    "user_data": user_data,
                },
                instance_rebuild_params.InstanceRebuildParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
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
        self.get = to_raw_response_wrapper(
            instances.get,
        )
        self.rebuild = to_raw_response_wrapper(
            instances.rebuild,
        )

    @cached_property
    def console(self) -> ConsoleResourceWithRawResponse:
        return ConsoleResourceWithRawResponse(self._instances.console)

    @cached_property
    def resize_flavors(self) -> ResizeFlavorsResourceWithRawResponse:
        return ResizeFlavorsResourceWithRawResponse(self._instances.resize_flavors)

    @cached_property
    def flavors(self) -> FlavorsResourceWithRawResponse:
        """
        Instance flavors define the CPU, memory, and OS type of an instance, in all regions of the project.
        """
        return FlavorsResourceWithRawResponse(self._instances.flavors)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        """
        Instance images are operating system images (public, private, or shared) used to boot cloud instances.
        """
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
        self.get = async_to_raw_response_wrapper(
            instances.get,
        )
        self.rebuild = async_to_raw_response_wrapper(
            instances.rebuild,
        )

    @cached_property
    def console(self) -> AsyncConsoleResourceWithRawResponse:
        return AsyncConsoleResourceWithRawResponse(self._instances.console)

    @cached_property
    def resize_flavors(self) -> AsyncResizeFlavorsResourceWithRawResponse:
        return AsyncResizeFlavorsResourceWithRawResponse(self._instances.resize_flavors)

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithRawResponse:
        """
        Instance flavors define the CPU, memory, and OS type of an instance, in all regions of the project.
        """
        return AsyncFlavorsResourceWithRawResponse(self._instances.flavors)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        """
        Instance images are operating system images (public, private, or shared) used to boot cloud instances.
        """
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
        self.get = to_streamed_response_wrapper(
            instances.get,
        )
        self.rebuild = to_streamed_response_wrapper(
            instances.rebuild,
        )

    @cached_property
    def console(self) -> ConsoleResourceWithStreamingResponse:
        return ConsoleResourceWithStreamingResponse(self._instances.console)

    @cached_property
    def resize_flavors(self) -> ResizeFlavorsResourceWithStreamingResponse:
        return ResizeFlavorsResourceWithStreamingResponse(self._instances.resize_flavors)

    @cached_property
    def flavors(self) -> FlavorsResourceWithStreamingResponse:
        """
        Instance flavors define the CPU, memory, and OS type of an instance, in all regions of the project.
        """
        return FlavorsResourceWithStreamingResponse(self._instances.flavors)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        """
        Instance images are operating system images (public, private, or shared) used to boot cloud instances.
        """
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
        self.get = async_to_streamed_response_wrapper(
            instances.get,
        )
        self.rebuild = async_to_streamed_response_wrapper(
            instances.rebuild,
        )

    @cached_property
    def console(self) -> AsyncConsoleResourceWithStreamingResponse:
        return AsyncConsoleResourceWithStreamingResponse(self._instances.console)

    @cached_property
    def resize_flavors(self) -> AsyncResizeFlavorsResourceWithStreamingResponse:
        return AsyncResizeFlavorsResourceWithStreamingResponse(self._instances.resize_flavors)

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithStreamingResponse:
        """
        Instance flavors define the CPU, memory, and OS type of an instance, in all regions of the project.
        """
        return AsyncFlavorsResourceWithStreamingResponse(self._instances.flavors)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        """
        Instance images are operating system images (public, private, or shared) used to boot cloud instances.
        """
        return AsyncImagesResourceWithStreamingResponse(self._instances.images)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._instances.metrics)

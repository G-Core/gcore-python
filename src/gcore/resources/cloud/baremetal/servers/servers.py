# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal

import httpx

from .console import (
    ConsoleResource,
    AsyncConsoleResource,
    ConsoleResourceWithRawResponse,
    AsyncConsoleResourceWithRawResponse,
    ConsoleResourceWithStreamingResponse,
    AsyncConsoleResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncOffsetPage, AsyncOffsetPage
from ..servers_custom import ServersResourceCustomMixin, AsyncServersResourceCustomMixin
from ....._base_client import AsyncPaginator, make_request_options
from .....types.cloud.baremetal import (
    server_list_params,
    server_action_params,
    server_create_params,
    server_delete_params,
    server_update_params,
    server_rebuild_params,
)
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.tag_update_map_param import TagUpdateMapParam
from .....types.cloud.baremetal.baremetal_server import BaremetalServer
from .....types.cloud.baremetal.server_delete_response import ServerDeleteResponse

__all__ = ["ServersResource", "AsyncServersResource"]


class ServersResource(ServersResourceCustomMixin, SyncAPIResource):
    """
    Bare metal servers are dedicated physical machines that boot an OS image from a local disk and connect to networks through ports, in any region of the project.
    """

    @cached_property
    def console(self) -> ConsoleResource:
        return ConsoleResource(self._client)

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

    def create(
        self,
        *,
        project_id: int | None = None,
        flavor_name: str,
        image_id: str,
        interfaces: Iterable[server_create_params.Interface],
        region_id: int,
        dry_run: bool | Omit = omit,
        name: str | Omit = omit,
        password: str | Omit = omit,
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
        """Create a bare metal server.

        The server writes an OS image to its local disk and
        boots from it. The server uses ports that you create first, in the region of the
        server.

        To create one:

        1. Pick an image with [List bare metal images](#operation/BmImagesViewSet.get).
        2. Pick a flavor with
           [List bare metal flavors](#operation/GlobalBaremetalFlavorListView.get). Send
           `compatible_with_image_id` to get only the flavors that can boot the image.
           The `networking_capabilities` of the flavor tell which port settings it
           accepts.
        3. [Create a port](#operation/GlobalPortListView.post) for each interface. A
           body with only `region_id` gives one public IPv4 address.

        The order of `interfaces` is the NIC order and the boot order. Omit `port_group`
        to put all interfaces in the first bond. You can also add an
        [SSH key](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).

        The response holds the IDs of the tasks that create the server.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real create.

        Args:
          project_id: Project ID.

          flavor_name: Name of a bare metal flavor. The flavor sets the CPU, the memory, the disks and
              the network cards of the server.
              `GET /v1/projects/{project_id}/baremetal/flavors` lists the flavors.

          image_id: OS image to write to the server's local disk.

          interfaces: Pre-created ports to attach, in NIC/boot order.

          region_id: Region to provision the server in.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          name: Server name. Auto-generated if omitted.

          password: Password of the default user. No response returns it. A Windows image needs a
              password. For a Windows image, the create checks these rules: the password has a
              minimum of 6 characters, it contains no word 'admin', and it contains 3 of these
              character types: digits, lowercase letters, uppercase letters, other characters.
              For a Linux image, the password enables SSH login with a password. Send
              `password` or `user_data`, not both.

          ssh_key_id: ID of the SSH key to add to the default user.

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Tag keys and values cannot contain characters from
              U+0080 to U+00FF. Some tags are read-only and cannot be modified by the user.
              Tags are also integrated with cost reports, allowing cost data to be filtered
              based on tag keys or values.

          user_data: cloud-init user data (raw or base64). Windows: may be combined with password
              (password sets the Administrator account). Linux: mutually exclusive with
              password.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._post(
            path_template("/cloud/v1/projects/{project_id}/baremetal/servers", project_id=project_id),
            body=maybe_transform(
                {
                    "flavor_name": flavor_name,
                    "image_id": image_id,
                    "interfaces": interfaces,
                    "region_id": region_id,
                    "name": name,
                    "password": password,
                    "ssh_key_id": ssh_key_id,
                    "tags": tags,
                    "user_data": user_data,
                },
                server_create_params.ServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dry_run": dry_run}, server_create_params.ServerCreateParams),
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        dry_run: bool | Omit = omit,
        interfaces: Iterable[server_update_params.Interface] | Omit = omit,
        name: str | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Send only the fields to change.

        The response holds the IDs of the tasks that
        make the changes.

        - Rename: send `name`.
        - Add an interface: [create a port](#operation/GlobalPortListView.post). Then
          send `interfaces` with the current interfaces in their current order and the
          new port at the end.
        - Remove an interface: send `interfaces` without it. The port stays and you can
          use it again. The server keeps at least one interface.
        - Change tags: send `tags` as a JSON Merge Patch.

        To change the security groups,
        [update the ports](#operation/GlobalPortDetailView.patch). The update does not
        change the flavor or the image.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real update.

        Args:
          project_id: Project ID.

          server_id: Bare metal server ID.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          interfaces: Full list of the interfaces of the server. Interfaces that are not in the list
              are detached. Keep the current interfaces in their current order. Add new
              interfaces at the end of the list. Send at least one interface.

          name: Server name.

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7396). Provide
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
                adds/updates 'environment' and 'cost_center' while removing 'deprecated_tag',
                preserving other existing tags.
              - **Replace all:** first delete existing tags with null values, then add new
                ones in the same request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._patch(
            path_template(
                "/cloud/v1/projects/{project_id}/baremetal/servers/{server_id}",
                project_id=project_id,
                server_id=server_id,
            ),
            body=maybe_transform(
                {
                    "interfaces": interfaces,
                    "name": name,
                    "tags": tags,
                },
                server_update_params.ServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dry_run": dry_run}, server_update_params.ServerUpdateParams),
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        created_at: server_list_params.CreatedAt | Omit = omit,
        flavor_name: server_list_params.FlavorName | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        ip_address: server_list_params.IPAddress | Omit = omit,
        limit: int | Omit = omit,
        managed: bool | Omit = omit,
        managed_by: Literal["k8s_cluster"] | Omit = omit,
        managed_by_resource_ids: SequenceNotStr[str] | Omit = omit,
        managed_by_resource_names: SequenceNotStr[str] | Omit = omit,
        name: server_list_params.Name | Omit = omit,
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
        tag_key: server_list_params.TagKey | Omit = omit,
        tag_value: server_list_params.TagValue | Omit = omit,
        tags: Dict[str, SequenceNotStr[str]] | Omit = omit,
        updated_at: server_list_params.UpdatedAt | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[BaremetalServer]:
        """
        List a project's bare metal servers across all regions.

        Args:
          project_id: Project ID.

          created_at: Range filter on creation time.

          flavor_name: Operator flavor name filter.

          ids: Filter by baremetal server UUID(s).

          ip_address: Exact IP filter on a fixed IP.

          limit: Max items to return.

          managed: Filter by managed status. true = managed by a service, false =
              customer-operated.

          managed_by: Filter by manager type, e.g. `k8s_cluster`.

          managed_by_resource_ids: Filter by managing resource ID(s).

          managed_by_resource_names: Filter by managing resource name(s).

          name: Operator name filter, e.g. name[contains]=web.

          network_ids: Filter by network ID(s) the server has a port on.

          offset: Items to skip.

          order_by: Sort field and direction.

          region_ids: Filter by region ID(s). Omit = all regions.

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
            path_template("/cloud/v1/projects/{project_id}/baremetal/servers", project_id=project_id),
            page=SyncOffsetPage[BaremetalServer],
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
                        "statuses": statuses,
                        "subnet_ids": subnet_ids,
                        "tag_key": tag_key,
                        "tag_value": tag_value,
                        "tags": tags,
                        "updated_at": updated_at,
                    },
                    server_list_params.ServerListParams,
                ),
            ),
            model=BaremetalServer,
        )

    def delete(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        all_floating_ips: bool | Omit = omit,
        all_ports: bool | Omit = omit,
        dry_run: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        port_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerDeleteResponse:
        """Delete a bare metal server.

        Ports and floating IPs are preserved by default:
        ports are detached (the trunk is dissolved, each port survives standalone) and
        floating IPs are disassociated. Asynchronous - returns the ID of the task
        performing the deletion.

        `resources_to_delete` holds:

        - the server itself;
        - the ports and sub-ports that `port_ids` names, or every port if `all_ports` is
          `true`;
        - the floating IPs that `floating_ip_ids` names, or every floating IP if
          `all_floating_ips` is `true`.

        `resources_to_preserve` holds every other port, sub-port and floating IP of the
        server. A floating IP on a deleted port stays, with no port.

        [`DELETE /v1/bminstances/{project_id}/{region_id}/{server_id}`](#operation/BMInstancesViewSet.delete)
        is different. It deletes every port, except the reserved fixed IPs that
        `reserved_fixed_ip_ids` and `all_reserved_fixed_ips` do not select.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array and the same two lists. A failed check
        returns the same error as the real delete.

        Args:
          project_id: Project ID.

          server_id: Bare metal server ID.

          all_floating_ips: Delete all floating IPs associated with the server's ports. Default preserves
              them (disassociate only). Mutually exclusive with `floating_ip_ids`.

          all_ports: Delete all ports attached to the bare metal server. Default preserves them
              (detach only; the trunk is dissolved but every port survives, reusable
              elsewhere). Mutually exclusive with `port_ids`.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          floating_ip_ids: Floating IP IDs to delete; the rest are preserved. Mutually exclusive with
              `all_floating_ips`.

          port_ids: Port IDs to delete; the rest are preserved. Mutually exclusive with `all_ports`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._delete(
            path_template(
                "/cloud/v1/projects/{project_id}/baremetal/servers/{server_id}",
                project_id=project_id,
                server_id=server_id,
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
                        "dry_run": dry_run,
                        "floating_ip_ids": floating_ip_ids,
                        "port_ids": port_ids,
                    },
                    server_delete_params.ServerDeleteParams,
                ),
            ),
            cast_to=ServerDeleteResponse,
        )

    def action(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        action: Literal["reboot", "reboot_hard", "start", "stop"],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Change the power state of a bare metal server.

        The action is one of: `start`,
        `stop`, `reboot` or `reboot_hard`. The action does not change the Advanced DDoS
        profile of the server. Use the DDoS profile resource to activate or to
        deactivate protection. Returns the ID of the task that runs the action.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real action.

        Args:
          project_id: Project ID.

          server_id: Bare metal server ID.

          action: Power action to run on the bare metal server.

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
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._post(
            path_template(
                "/cloud/v1/projects/{project_id}/baremetal/servers/{server_id}/action",
                project_id=project_id,
                server_id=server_id,
            ),
            body=maybe_transform({"action": action}, server_action_params.ServerActionParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dry_run": dry_run}, server_action_params.ServerActionParams),
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaremetalServer:
        """
        Returns a single bare metal server by ID, resolved across all regions.

        Args:
          project_id: Project ID.

          server_id: Bare metal server ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._get(
            path_template(
                "/cloud/v1/projects/{project_id}/baremetal/servers/{server_id}",
                project_id=project_id,
                server_id=server_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaremetalServer,
        )

    def rebuild(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | Omit = omit,
        user_data: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Rebuild a bare metal server with a new image while preserving its configuration.

        Args:
          project_id: Project ID

          region_id: Region ID

          server_id: Server ID

          image_id: Image ID

          user_data: String in base64 format. Must not be passed together with 'username' or
              'password'. Examples of the `user_data`:
              https://cloudinit.readthedocs.io/en/latest/topics/examples.html

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
            path_template(
                "/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild",
                project_id=project_id,
                region_id=region_id,
                server_id=server_id,
            ),
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


class AsyncServersResource(AsyncServersResourceCustomMixin, AsyncAPIResource):
    """
    Bare metal servers are dedicated physical machines that boot an OS image from a local disk and connect to networks through ports, in any region of the project.
    """

    @cached_property
    def console(self) -> AsyncConsoleResource:
        return AsyncConsoleResource(self._client)

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

    async def create(
        self,
        *,
        project_id: int | None = None,
        flavor_name: str,
        image_id: str,
        interfaces: Iterable[server_create_params.Interface],
        region_id: int,
        dry_run: bool | Omit = omit,
        name: str | Omit = omit,
        password: str | Omit = omit,
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
        """Create a bare metal server.

        The server writes an OS image to its local disk and
        boots from it. The server uses ports that you create first, in the region of the
        server.

        To create one:

        1. Pick an image with [List bare metal images](#operation/BmImagesViewSet.get).
        2. Pick a flavor with
           [List bare metal flavors](#operation/GlobalBaremetalFlavorListView.get). Send
           `compatible_with_image_id` to get only the flavors that can boot the image.
           The `networking_capabilities` of the flavor tell which port settings it
           accepts.
        3. [Create a port](#operation/GlobalPortListView.post) for each interface. A
           body with only `region_id` gives one public IPv4 address.

        The order of `interfaces` is the NIC order and the boot order. Omit `port_group`
        to put all interfaces in the first bond. You can also add an
        [SSH key](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).

        The response holds the IDs of the tasks that create the server.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real create.

        Args:
          project_id: Project ID.

          flavor_name: Name of a bare metal flavor. The flavor sets the CPU, the memory, the disks and
              the network cards of the server.
              `GET /v1/projects/{project_id}/baremetal/flavors` lists the flavors.

          image_id: OS image to write to the server's local disk.

          interfaces: Pre-created ports to attach, in NIC/boot order.

          region_id: Region to provision the server in.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          name: Server name. Auto-generated if omitted.

          password: Password of the default user. No response returns it. A Windows image needs a
              password. For a Windows image, the create checks these rules: the password has a
              minimum of 6 characters, it contains no word 'admin', and it contains 3 of these
              character types: digits, lowercase letters, uppercase letters, other characters.
              For a Linux image, the password enables SSH login with a password. Send
              `password` or `user_data`, not both.

          ssh_key_id: ID of the SSH key to add to the default user.

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Tag keys and values cannot contain characters from
              U+0080 to U+00FF. Some tags are read-only and cannot be modified by the user.
              Tags are also integrated with cost reports, allowing cost data to be filtered
              based on tag keys or values.

          user_data: cloud-init user data (raw or base64). Windows: may be combined with password
              (password sets the Administrator account). Linux: mutually exclusive with
              password.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return await self._post(
            path_template("/cloud/v1/projects/{project_id}/baremetal/servers", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "flavor_name": flavor_name,
                    "image_id": image_id,
                    "interfaces": interfaces,
                    "region_id": region_id,
                    "name": name,
                    "password": password,
                    "ssh_key_id": ssh_key_id,
                    "tags": tags,
                    "user_data": user_data,
                },
                server_create_params.ServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dry_run": dry_run}, server_create_params.ServerCreateParams),
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        dry_run: bool | Omit = omit,
        interfaces: Iterable[server_update_params.Interface] | Omit = omit,
        name: str | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Send only the fields to change.

        The response holds the IDs of the tasks that
        make the changes.

        - Rename: send `name`.
        - Add an interface: [create a port](#operation/GlobalPortListView.post). Then
          send `interfaces` with the current interfaces in their current order and the
          new port at the end.
        - Remove an interface: send `interfaces` without it. The port stays and you can
          use it again. The server keeps at least one interface.
        - Change tags: send `tags` as a JSON Merge Patch.

        To change the security groups,
        [update the ports](#operation/GlobalPortDetailView.patch). The update does not
        change the flavor or the image.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real update.

        Args:
          project_id: Project ID.

          server_id: Bare metal server ID.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          interfaces: Full list of the interfaces of the server. Interfaces that are not in the list
              are detached. Keep the current interfaces in their current order. Add new
              interfaces at the end of the list. Send at least one interface.

          name: Server name.

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7396). Provide
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
                adds/updates 'environment' and 'cost_center' while removing 'deprecated_tag',
                preserving other existing tags.
              - **Replace all:** first delete existing tags with null values, then add new
                ones in the same request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._patch(
            path_template(
                "/cloud/v1/projects/{project_id}/baremetal/servers/{server_id}",
                project_id=project_id,
                server_id=server_id,
            ),
            body=await async_maybe_transform(
                {
                    "interfaces": interfaces,
                    "name": name,
                    "tags": tags,
                },
                server_update_params.ServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dry_run": dry_run}, server_update_params.ServerUpdateParams),
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        created_at: server_list_params.CreatedAt | Omit = omit,
        flavor_name: server_list_params.FlavorName | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        ip_address: server_list_params.IPAddress | Omit = omit,
        limit: int | Omit = omit,
        managed: bool | Omit = omit,
        managed_by: Literal["k8s_cluster"] | Omit = omit,
        managed_by_resource_ids: SequenceNotStr[str] | Omit = omit,
        managed_by_resource_names: SequenceNotStr[str] | Omit = omit,
        name: server_list_params.Name | Omit = omit,
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
        tag_key: server_list_params.TagKey | Omit = omit,
        tag_value: server_list_params.TagValue | Omit = omit,
        tags: Dict[str, SequenceNotStr[str]] | Omit = omit,
        updated_at: server_list_params.UpdatedAt | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BaremetalServer, AsyncOffsetPage[BaremetalServer]]:
        """
        List a project's bare metal servers across all regions.

        Args:
          project_id: Project ID.

          created_at: Range filter on creation time.

          flavor_name: Operator flavor name filter.

          ids: Filter by baremetal server UUID(s).

          ip_address: Exact IP filter on a fixed IP.

          limit: Max items to return.

          managed: Filter by managed status. true = managed by a service, false =
              customer-operated.

          managed_by: Filter by manager type, e.g. `k8s_cluster`.

          managed_by_resource_ids: Filter by managing resource ID(s).

          managed_by_resource_names: Filter by managing resource name(s).

          name: Operator name filter, e.g. name[contains]=web.

          network_ids: Filter by network ID(s) the server has a port on.

          offset: Items to skip.

          order_by: Sort field and direction.

          region_ids: Filter by region ID(s). Omit = all regions.

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
            path_template("/cloud/v1/projects/{project_id}/baremetal/servers", project_id=project_id),
            page=AsyncOffsetPage[BaremetalServer],
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
                        "statuses": statuses,
                        "subnet_ids": subnet_ids,
                        "tag_key": tag_key,
                        "tag_value": tag_value,
                        "tags": tags,
                        "updated_at": updated_at,
                    },
                    server_list_params.ServerListParams,
                ),
            ),
            model=BaremetalServer,
        )

    async def delete(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        all_floating_ips: bool | Omit = omit,
        all_ports: bool | Omit = omit,
        dry_run: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        port_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerDeleteResponse:
        """Delete a bare metal server.

        Ports and floating IPs are preserved by default:
        ports are detached (the trunk is dissolved, each port survives standalone) and
        floating IPs are disassociated. Asynchronous - returns the ID of the task
        performing the deletion.

        `resources_to_delete` holds:

        - the server itself;
        - the ports and sub-ports that `port_ids` names, or every port if `all_ports` is
          `true`;
        - the floating IPs that `floating_ip_ids` names, or every floating IP if
          `all_floating_ips` is `true`.

        `resources_to_preserve` holds every other port, sub-port and floating IP of the
        server. A floating IP on a deleted port stays, with no port.

        [`DELETE /v1/bminstances/{project_id}/{region_id}/{server_id}`](#operation/BMInstancesViewSet.delete)
        is different. It deletes every port, except the reserved fixed IPs that
        `reserved_fixed_ip_ids` and `all_reserved_fixed_ips` do not select.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array and the same two lists. A failed check
        returns the same error as the real delete.

        Args:
          project_id: Project ID.

          server_id: Bare metal server ID.

          all_floating_ips: Delete all floating IPs associated with the server's ports. Default preserves
              them (disassociate only). Mutually exclusive with `floating_ip_ids`.

          all_ports: Delete all ports attached to the bare metal server. Default preserves them
              (detach only; the trunk is dissolved but every port survives, reusable
              elsewhere). Mutually exclusive with `port_ids`.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          floating_ip_ids: Floating IP IDs to delete; the rest are preserved. Mutually exclusive with
              `all_floating_ips`.

          port_ids: Port IDs to delete; the rest are preserved. Mutually exclusive with `all_ports`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._delete(
            path_template(
                "/cloud/v1/projects/{project_id}/baremetal/servers/{server_id}",
                project_id=project_id,
                server_id=server_id,
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
                        "dry_run": dry_run,
                        "floating_ip_ids": floating_ip_ids,
                        "port_ids": port_ids,
                    },
                    server_delete_params.ServerDeleteParams,
                ),
            ),
            cast_to=ServerDeleteResponse,
        )

    async def action(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        action: Literal["reboot", "reboot_hard", "start", "stop"],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Change the power state of a bare metal server.

        The action is one of: `start`,
        `stop`, `reboot` or `reboot_hard`. The action does not change the Advanced DDoS
        profile of the server. Use the DDoS profile resource to activate or to
        deactivate protection. Returns the ID of the task that runs the action.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real action.

        Args:
          project_id: Project ID.

          server_id: Bare metal server ID.

          action: Power action to run on the bare metal server.

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
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._post(
            path_template(
                "/cloud/v1/projects/{project_id}/baremetal/servers/{server_id}/action",
                project_id=project_id,
                server_id=server_id,
            ),
            body=await async_maybe_transform({"action": action}, server_action_params.ServerActionParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dry_run": dry_run}, server_action_params.ServerActionParams),
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaremetalServer:
        """
        Returns a single bare metal server by ID, resolved across all regions.

        Args:
          project_id: Project ID.

          server_id: Bare metal server ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._get(
            path_template(
                "/cloud/v1/projects/{project_id}/baremetal/servers/{server_id}",
                project_id=project_id,
                server_id=server_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaremetalServer,
        )

    async def rebuild(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | Omit = omit,
        user_data: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Rebuild a bare metal server with a new image while preserving its configuration.

        Args:
          project_id: Project ID

          region_id: Region ID

          server_id: Server ID

          image_id: Image ID

          user_data: String in base64 format. Must not be passed together with 'username' or
              'password'. Examples of the `user_data`:
              https://cloudinit.readthedocs.io/en/latest/topics/examples.html

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
            path_template(
                "/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild",
                project_id=project_id,
                region_id=region_id,
                server_id=server_id,
            ),
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
        self.update = to_raw_response_wrapper(
            servers.update,
        )
        self.list = to_raw_response_wrapper(
            servers.list,
        )
        self.delete = to_raw_response_wrapper(
            servers.delete,
        )
        self.action = to_raw_response_wrapper(
            servers.action,
        )
        self.get = to_raw_response_wrapper(
            servers.get,
        )
        self.rebuild = to_raw_response_wrapper(
            servers.rebuild,
        )

    @cached_property
    def console(self) -> ConsoleResourceWithRawResponse:
        return ConsoleResourceWithRawResponse(self._servers.console)


class AsyncServersResourceWithRawResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.create = async_to_raw_response_wrapper(
            servers.create,
        )
        self.update = async_to_raw_response_wrapper(
            servers.update,
        )
        self.list = async_to_raw_response_wrapper(
            servers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            servers.delete,
        )
        self.action = async_to_raw_response_wrapper(
            servers.action,
        )
        self.get = async_to_raw_response_wrapper(
            servers.get,
        )
        self.rebuild = async_to_raw_response_wrapper(
            servers.rebuild,
        )

    @cached_property
    def console(self) -> AsyncConsoleResourceWithRawResponse:
        return AsyncConsoleResourceWithRawResponse(self._servers.console)


class ServersResourceWithStreamingResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.create = to_streamed_response_wrapper(
            servers.create,
        )
        self.update = to_streamed_response_wrapper(
            servers.update,
        )
        self.list = to_streamed_response_wrapper(
            servers.list,
        )
        self.delete = to_streamed_response_wrapper(
            servers.delete,
        )
        self.action = to_streamed_response_wrapper(
            servers.action,
        )
        self.get = to_streamed_response_wrapper(
            servers.get,
        )
        self.rebuild = to_streamed_response_wrapper(
            servers.rebuild,
        )

    @cached_property
    def console(self) -> ConsoleResourceWithStreamingResponse:
        return ConsoleResourceWithStreamingResponse(self._servers.console)


class AsyncServersResourceWithStreamingResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.create = async_to_streamed_response_wrapper(
            servers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            servers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            servers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            servers.delete,
        )
        self.action = async_to_streamed_response_wrapper(
            servers.action,
        )
        self.get = async_to_streamed_response_wrapper(
            servers.get,
        )
        self.rebuild = async_to_streamed_response_wrapper(
            servers.rebuild,
        )

    @cached_property
    def console(self) -> AsyncConsoleResourceWithStreamingResponse:
        return AsyncConsoleResourceWithStreamingResponse(self._servers.console)

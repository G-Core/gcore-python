# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from .ports_custom import PortsResourceCustomMixin, AsyncPortsResourceCustomMixin
from ...types.cloud import port_list_params, port_create_params, port_update_params, port_convert_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cloud.port import Port
from ...types.cloud.task_id_list import TaskIDList
from ...types.cloud.tag_update_map_param import TagUpdateMapParam
from ...types.cloud.ip_assignment_request_param import IPAssignmentRequestParam

__all__ = ["PortsResource", "AsyncPortsResource"]


class PortsResource(PortsResourceCustomMixin, SyncAPIResource):
    """
    Ports reserve IP addresses on a network and act as network interfaces of compute resources, with their own security groups and allowed address pairs.
    """

    @cached_property
    def with_raw_response(self) -> PortsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PortsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PortsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int,
        dry_run: bool | Omit = omit,
        allowed_address_pairs: Iterable[port_create_params.AllowedAddressPair] | Omit = omit,
        ip_assignments: Iterable[IPAssignmentRequestParam] | Omit = omit,
        network_id: str | Omit = omit,
        port_security_enabled: bool | Omit = omit,
        security_group_ids: SequenceNotStr[str] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """A port reserves addresses on a network.

        The port can exist on its own. A compute
        resource claims the port and then uses it as a network interface. Port with one
        public address Send only the region. The port gets one IPv4 address from the
        region's public network.

        ```json
        { "region_id": 1 }
        ```

        Port in your own network Name only the network. The port gets one IPv4 address
        from any IPv4 subnet of that network.

        ```json
        { "region_id": 1, "network_id": "<network_id>" }
        ```

        Port in a chosen subnet Name the subnet in `ip_assignments`. An IPv6-only
        network always needs this form. Without `network_id`, the port goes to the
        network of the subnet.

        ```json
        {
          "region_id": 1,
          "network_id": "<network_id>",
          "ip_assignments": [{ "subnet_id": "<subnet_id>" }]
        }
        ```

        Port with IPv4 and IPv6 Name one IPv4 subnet and one IPv6 subnet of the same
        network.

        ```json
        {
          "region_id": 1,
          "network_id": "<network_id>",
          "ip_assignments": [
            { "subnet_id": "<ipv4_subnet_id>" },
            { "subnet_id": "<ipv6_subnet_id>" }
          ]
        }
        ```

        Port with a chosen address Add `ip_address` to the assignment. The address must
        be free and inside the subnet.

        ```json
        {
          "region_id": 1,
          "network_id": "<network_id>",
          "ip_assignments": [
            { "subnet_id": "<subnet_id>", "ip_address": "192.168.123.20" }
          ]
        }
        ```

        Port that holds a failover address Put the shared address in
        `allowed_address_pairs`. Every port that can hold the address needs this. Create
        the port that owns the address first.

        ```json
        {
          "region_id": 1,
          "network_id": "<network_id>",
          "allowed_address_pairs": [{ "ip_address": "192.168.123.100" }]
        }
        ```

        Rules

        - `network_id` defaults to the region's public network. The subnets in
          `ip_assignments` do not change it.
        - Every subnet in `ip_assignments` must belong to `network_id`.
        - Without `ip_assignments` the network must have an IPv4 subnet.
        - One entry in `ip_assignments` gives one address. Repeat a subnet to get more
          addresses from it.
        - Each `allowed_address_pairs` address must already belong to a port in the same
          network.
        - A port in the region's public network refuses `port_security_enabled`.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real create.

        Args:
          project_id: Project ID

          region_id: Region ID where the port is created

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          allowed_address_pairs: A set of zero or more allowed port address pair and/or subnet masks.

          ip_assignments: IP addresses to assign. All subnets must belong to the same network. Repeat a
              subnet to get several addresses from it. Omit the field to get one address from
              an IPv4 subnet.

          network_id: Network to create the port in. When omitted, it is the network of the subnets in
              `ip_assignments`, or the region's public network if `ip_assignments` is omitted.
              Every subnet in `ip_assignments` must belong to it.

          port_security_enabled: When true, the network driver enforces port security on this port (anti-spoofing
              checks and security-group filtering apply). Defaults to the network's setting.

          security_group_ids: List of security group IDs to attach to the port.

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Tag keys and values cannot contain characters from
              U+0080 to U+00FF. Some tags are read-only and cannot be modified by the user.
              Tags are also integrated with cost reports, allowing cost data to be filtered
              based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._post(
            path_template("/cloud/v1/projects/{project_id}/ports", project_id=project_id),
            body=maybe_transform(
                {
                    "region_id": region_id,
                    "allowed_address_pairs": allowed_address_pairs,
                    "ip_assignments": ip_assignments,
                    "network_id": network_id,
                    "port_security_enabled": port_security_enabled,
                    "security_group_ids": security_group_ids,
                    "tags": tags,
                },
                port_create_params.PortCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dry_run": dry_run}, port_create_params.PortCreateParams),
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        allowed_address_pairs: Iterable[port_update_params.AllowedAddressPair] | Omit = omit,
        ip_assignments: Iterable[IPAssignmentRequestParam] | Omit = omit,
        port_security_enabled: bool | Omit = omit,
        security_group_ids: SequenceNotStr[str] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Updates port security, security groups, allowed address pairs, tags and IP
        assignments.

        **Behavior:**

        - Undefined fields remain unchanged; list fields replace the whole set, so send
          the full desired list (`[]` to clear, `ip_assignments` must keep at least one
          entry)
        - Tags are merged per key; a `null` value removes the key, and `tags: null`
          removes all user tags
        - If no changes are detected, no task is created and an empty task list is
          returned

        **Supported ports:** all compute types (instances, basic VMs, bare metal
        servers, GPU virtual servers, GPU bare metal servers), as long as the port
        `capabilities` report `true` for the field being changed. Ports that the
        platform manages (DHCP, router, load balancer) are rejected. You can update a
        port that is not attached to a server. The server checks the settings when you
        attach the port.

        **Typical uses:**

        - Per-port firewall: `security_group_ids` applies to this port only, so ports on
          the same server can differ. While port security is enabled, an empty list
          permits no traffic
        - VIP failover (VRRP/keepalived): add the VIP address to `allowed_address_pairs`
          of every port allowed to claim it, all on the VIP's network
        - Routing and NAT appliances: `port_security_enabled: false` permits forwarding
          traffic with foreign source addresses; clear security groups and allowed
          address pairs in the same request
        - Additional addresses: `ip_assignments` adds or releases IPs (dual-stack, extra
          service IPs) without detaching the port; the guest OS must be configured for
          the extra ones. Send an entry with only `subnet_id` to get any free address of
          that subnet, which is the only option on a shared subnet whose free addresses
          the caller does not know. Such an entry keeps an address the port already has
          in that subnet, in the order the port reports them, so a shorter list releases
          the addresses at the end of that order. A request can replace all current
          addresses. A port an instance holds takes its addresses from one subnet per IP
          version, because the guest reaches one address range per version

        **Public network:** port security and allowed address pairs cannot be changed on
        ports in the region's public network. IP assignments can. To add an address
        there, send an entry with only `subnet_id`. A new entry with `ip_address` is not
        allowed. An entry can still specify an address that the port already holds. Each
        IPv4 address there counts against the external IP quota, so a request that
        allocates one fails when the limit is full, and a request that releases one
        gives the quota back. IPv6 addresses in that network are not counted.

        **Network that other clients share:** a network of another project can hold
        ports of other clients. On such a network, port security stays enabled. Each
        allowed address pair must name one address and the MAC address of a port of the
        same project, and a range is not allowed. A network that no other client uses
        keeps the rules of an own network.

        Args:
          project_id: Project ID

          port_id: Port ID

          allowed_address_pairs: A set of zero or more allowed port address pair and/or subnet masks. Replaces
              the full set of allowed address pairs. Send `[]` to clear; omit the field to
              leave existing pairs unchanged.

          ip_assignments: IP assignments on the port. Replaces the full set. Subnets must belong to the
              port's network, and a port an instance holds supports one subnet per IP version.
              An entry without `ip_address` keeps an address the port already has in that
              subnet, in the order the port reports them, or takes a free one when the port
              has none. Addresses that no entry keeps are released.

          port_security_enabled: When true, the network driver enforces port security on this port (anti-spoofing
              checks and security-group filtering apply). When false, all traffic is allowed
              and security groups are not applied.

          security_group_ids: List of security group IDs. Replaces the full set of security groups attached to
              the port. Send `[]` to detach all groups; omit the field to leave existing
              groups unchanged.

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
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return self._patch(
            path_template("/cloud/v1/projects/{project_id}/ports/{port_id}", project_id=project_id, port_id=port_id),
            body=maybe_transform(
                {
                    "allowed_address_pairs": allowed_address_pairs,
                    "ip_assignments": ip_assignments,
                    "port_security_enabled": port_security_enabled,
                    "security_group_ids": security_group_ids,
                    "tags": tags,
                },
                port_update_params.PortUpdateParams,
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
        attached: bool | Omit = omit,
        attached_to_resource_ids: SequenceNotStr[str] | Omit = omit,
        attached_to_resource_types: List[
            Literal[
                "baremetal_server",
                "basic_vm",
                "dhcp",
                "gpu_baremetal_server",
                "gpu_virtual_server",
                "instance",
                "load_balancer",
                "router",
            ]
        ]
        | Omit = omit,
        created_at: port_list_params.CreatedAt | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        ip_address: port_list_params.IPAddress | Omit = omit,
        limit: int | Omit = omit,
        managed: bool | Omit = omit,
        managed_by: Literal[
            "file_share",
            "gpu_baremetal_cluster",
            "gpu_virtual_cluster",
            "k8s_cluster",
            "load_balancer",
            "network",
            "router",
            "system",
        ]
        | Omit = omit,
        managed_by_resource_ids: SequenceNotStr[str] | Omit = omit,
        managed_by_resource_names: SequenceNotStr[str] | Omit = omit,
        network_ids: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal[
            "created_at.asc",
            "created_at.desc",
            "network_grouping.asc",
            "region_id.asc",
            "region_id.desc",
            "updated_at.asc",
            "updated_at.desc",
        ]
        | Omit = omit,
        public: bool | Omit = omit,
        region_ids: Iterable[int] | Omit = omit,
        security_group_ids: SequenceNotStr[str] | Omit = omit,
        subnet_ids: SequenceNotStr[str] | Omit = omit,
        tag_key: port_list_params.TagKey | Omit = omit,
        tag_value: port_list_params.TagValue | Omit = omit,
        tags: Dict[str, SequenceNotStr[str]] | Omit = omit,
        updated_at: port_list_params.UpdatedAt | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[Port]:
        """
        List a project's ports across all regions.

        Args:
          project_id: Project ID

          attached: Filter attached (true) or standalone (false) ports.

          attached_to_resource_ids: Filter by attached resource ID(s). Matches ports attached to any of the given
              resources.

          attached_to_resource_types: Filter by attachment resource type(s). A port matches if its type is any of the
              given values.

          created_at: Range filter on creation time.

          ids: Filter by port UUID(s).

          ip_address: Filter by fixed IP address.

          limit: Max items to return.

          managed: Filter by managed status. true = managed by a service, false =
              customer-operated. A port with a manager type that this API version does not
              know counts as managed, but its `managed_by` is null. Cannot be combined with
              `managed_by` when false.

          managed_by: Filter by manager type, e.g. system or `k8s_cluster`.

          managed_by_resource_ids: Filter by managing resource ID(s).

          managed_by_resource_names: Filter by managing resource name(s).

          network_ids: Filter by network ID(s).

          offset: Items to skip.

          order_by: Sort field and direction. `network_grouping.asc` keeps the ports of one network
              together. In each region, the networks shared with the project come first, in
              the order of the share. If no shared network is public, the default public
              network of the region comes next. Then come other public networks, then all
              other networks.

          public: Filter ports on networks that give publicly routed address space (true) or not
              (false).

          region_ids: Filter by region ID(s). Omit = all regions.

          security_group_ids: Filter by security group ID(s). A port matches if it has any of the given
              security groups.

          subnet_ids: Filter by subnet ID(s). A port matches if it has a fixed IP in any of the given
              subnets.

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
            path_template("/cloud/v1/projects/{project_id}/ports", project_id=project_id),
            page=SyncOffsetPage[Port],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "attached": attached,
                        "attached_to_resource_ids": attached_to_resource_ids,
                        "attached_to_resource_types": attached_to_resource_types,
                        "created_at": created_at,
                        "ids": ids,
                        "ip_address": ip_address,
                        "limit": limit,
                        "managed": managed,
                        "managed_by": managed_by,
                        "managed_by_resource_ids": managed_by_resource_ids,
                        "managed_by_resource_names": managed_by_resource_names,
                        "network_ids": network_ids,
                        "offset": offset,
                        "order_by": order_by,
                        "public": public,
                        "region_ids": region_ids,
                        "security_group_ids": security_group_ids,
                        "subnet_ids": subnet_ids,
                        "tag_key": tag_key,
                        "tag_value": tag_value,
                        "tags": tags,
                        "updated_at": updated_at,
                    },
                    port_list_params.PortListParams,
                ),
            ),
            model=Port,
        )

    def delete(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Delete a port that no compute resource uses.

        The request returns a task. The
        task deletes the port. Effects

        - A floating IP of the port stays in the project. The task removes it from the
          port.
        - Each IPv4 address on the region's public network goes back to the external IP
          quota. Rules
        - The port must not be attached. Detach it from the compute resource first.
        - The platform manages ports of routers, load balancers and DHCP. You cannot
          delete these ports.
        - A port that an attach or detach operation holds cannot be deleted. Try again
          when the operation ends.
        - An address of the port must not be in `allowed_address_pairs` of other ports.
          Remove these entries first.

        Args:
          project_id: Project ID

          port_id: Port ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return self._delete(
            path_template("/cloud/v1/projects/{project_id}/ports/{port_id}", project_id=project_id, port_id=port_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def convert(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        target_type: Literal["floating_ip"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Converts a port to a floating IP with the same address.

        The task deletes the
        port and creates the floating IP. The port must be unattached, be on a public
        network and have exactly one IPv4 address.

        The external IP quota decreases by one and the floating IP quota increases by
        one.

        If the floating IP create fails, the task creates the port again with the same
        address. The new port gets a new ID. It keeps only the network, name,
        description, security groups, port security, allowed address pairs and tags.
        Other attributes get their default values.

        A concurrent network operation can cause the conversion to fail. In rare cases
        the address is then lost, and you must create a new one.

        Args:
          project_id: Project ID

          port_id: Port ID

          target_type: Resource type to convert the port to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return self._post(
            path_template(
                "/cloud/v1/projects/{project_id}/ports/{port_id}/convert", project_id=project_id, port_id=port_id
            ),
            body=maybe_transform({"target_type": target_type}, port_convert_params.PortConvertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Port:
        """
        Get port

        Args:
          project_id: Project ID

          port_id: Port ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return self._get(
            path_template("/cloud/v1/projects/{project_id}/ports/{port_id}", project_id=project_id, port_id=port_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Port,
        )


class AsyncPortsResource(AsyncPortsResourceCustomMixin, AsyncAPIResource):
    """
    Ports reserve IP addresses on a network and act as network interfaces of compute resources, with their own security groups and allowed address pairs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPortsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPortsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int,
        dry_run: bool | Omit = omit,
        allowed_address_pairs: Iterable[port_create_params.AllowedAddressPair] | Omit = omit,
        ip_assignments: Iterable[IPAssignmentRequestParam] | Omit = omit,
        network_id: str | Omit = omit,
        port_security_enabled: bool | Omit = omit,
        security_group_ids: SequenceNotStr[str] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """A port reserves addresses on a network.

        The port can exist on its own. A compute
        resource claims the port and then uses it as a network interface. Port with one
        public address Send only the region. The port gets one IPv4 address from the
        region's public network.

        ```json
        { "region_id": 1 }
        ```

        Port in your own network Name only the network. The port gets one IPv4 address
        from any IPv4 subnet of that network.

        ```json
        { "region_id": 1, "network_id": "<network_id>" }
        ```

        Port in a chosen subnet Name the subnet in `ip_assignments`. An IPv6-only
        network always needs this form. Without `network_id`, the port goes to the
        network of the subnet.

        ```json
        {
          "region_id": 1,
          "network_id": "<network_id>",
          "ip_assignments": [{ "subnet_id": "<subnet_id>" }]
        }
        ```

        Port with IPv4 and IPv6 Name one IPv4 subnet and one IPv6 subnet of the same
        network.

        ```json
        {
          "region_id": 1,
          "network_id": "<network_id>",
          "ip_assignments": [
            { "subnet_id": "<ipv4_subnet_id>" },
            { "subnet_id": "<ipv6_subnet_id>" }
          ]
        }
        ```

        Port with a chosen address Add `ip_address` to the assignment. The address must
        be free and inside the subnet.

        ```json
        {
          "region_id": 1,
          "network_id": "<network_id>",
          "ip_assignments": [
            { "subnet_id": "<subnet_id>", "ip_address": "192.168.123.20" }
          ]
        }
        ```

        Port that holds a failover address Put the shared address in
        `allowed_address_pairs`. Every port that can hold the address needs this. Create
        the port that owns the address first.

        ```json
        {
          "region_id": 1,
          "network_id": "<network_id>",
          "allowed_address_pairs": [{ "ip_address": "192.168.123.100" }]
        }
        ```

        Rules

        - `network_id` defaults to the region's public network. The subnets in
          `ip_assignments` do not change it.
        - Every subnet in `ip_assignments` must belong to `network_id`.
        - Without `ip_assignments` the network must have an IPv4 subnet.
        - One entry in `ip_assignments` gives one address. Repeat a subnet to get more
          addresses from it.
        - Each `allowed_address_pairs` address must already belong to a port in the same
          network.
        - A port in the region's public network refuses `port_security_enabled`.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real create.

        Args:
          project_id: Project ID

          region_id: Region ID where the port is created

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          allowed_address_pairs: A set of zero or more allowed port address pair and/or subnet masks.

          ip_assignments: IP addresses to assign. All subnets must belong to the same network. Repeat a
              subnet to get several addresses from it. Omit the field to get one address from
              an IPv4 subnet.

          network_id: Network to create the port in. When omitted, it is the network of the subnets in
              `ip_assignments`, or the region's public network if `ip_assignments` is omitted.
              Every subnet in `ip_assignments` must belong to it.

          port_security_enabled: When true, the network driver enforces port security on this port (anti-spoofing
              checks and security-group filtering apply). Defaults to the network's setting.

          security_group_ids: List of security group IDs to attach to the port.

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Tag keys and values cannot contain characters from
              U+0080 to U+00FF. Some tags are read-only and cannot be modified by the user.
              Tags are also integrated with cost reports, allowing cost data to be filtered
              based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return await self._post(
            path_template("/cloud/v1/projects/{project_id}/ports", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "region_id": region_id,
                    "allowed_address_pairs": allowed_address_pairs,
                    "ip_assignments": ip_assignments,
                    "network_id": network_id,
                    "port_security_enabled": port_security_enabled,
                    "security_group_ids": security_group_ids,
                    "tags": tags,
                },
                port_create_params.PortCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dry_run": dry_run}, port_create_params.PortCreateParams),
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        allowed_address_pairs: Iterable[port_update_params.AllowedAddressPair] | Omit = omit,
        ip_assignments: Iterable[IPAssignmentRequestParam] | Omit = omit,
        port_security_enabled: bool | Omit = omit,
        security_group_ids: SequenceNotStr[str] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Updates port security, security groups, allowed address pairs, tags and IP
        assignments.

        **Behavior:**

        - Undefined fields remain unchanged; list fields replace the whole set, so send
          the full desired list (`[]` to clear, `ip_assignments` must keep at least one
          entry)
        - Tags are merged per key; a `null` value removes the key, and `tags: null`
          removes all user tags
        - If no changes are detected, no task is created and an empty task list is
          returned

        **Supported ports:** all compute types (instances, basic VMs, bare metal
        servers, GPU virtual servers, GPU bare metal servers), as long as the port
        `capabilities` report `true` for the field being changed. Ports that the
        platform manages (DHCP, router, load balancer) are rejected. You can update a
        port that is not attached to a server. The server checks the settings when you
        attach the port.

        **Typical uses:**

        - Per-port firewall: `security_group_ids` applies to this port only, so ports on
          the same server can differ. While port security is enabled, an empty list
          permits no traffic
        - VIP failover (VRRP/keepalived): add the VIP address to `allowed_address_pairs`
          of every port allowed to claim it, all on the VIP's network
        - Routing and NAT appliances: `port_security_enabled: false` permits forwarding
          traffic with foreign source addresses; clear security groups and allowed
          address pairs in the same request
        - Additional addresses: `ip_assignments` adds or releases IPs (dual-stack, extra
          service IPs) without detaching the port; the guest OS must be configured for
          the extra ones. Send an entry with only `subnet_id` to get any free address of
          that subnet, which is the only option on a shared subnet whose free addresses
          the caller does not know. Such an entry keeps an address the port already has
          in that subnet, in the order the port reports them, so a shorter list releases
          the addresses at the end of that order. A request can replace all current
          addresses. A port an instance holds takes its addresses from one subnet per IP
          version, because the guest reaches one address range per version

        **Public network:** port security and allowed address pairs cannot be changed on
        ports in the region's public network. IP assignments can. To add an address
        there, send an entry with only `subnet_id`. A new entry with `ip_address` is not
        allowed. An entry can still specify an address that the port already holds. Each
        IPv4 address there counts against the external IP quota, so a request that
        allocates one fails when the limit is full, and a request that releases one
        gives the quota back. IPv6 addresses in that network are not counted.

        **Network that other clients share:** a network of another project can hold
        ports of other clients. On such a network, port security stays enabled. Each
        allowed address pair must name one address and the MAC address of a port of the
        same project, and a range is not allowed. A network that no other client uses
        keeps the rules of an own network.

        Args:
          project_id: Project ID

          port_id: Port ID

          allowed_address_pairs: A set of zero or more allowed port address pair and/or subnet masks. Replaces
              the full set of allowed address pairs. Send `[]` to clear; omit the field to
              leave existing pairs unchanged.

          ip_assignments: IP assignments on the port. Replaces the full set. Subnets must belong to the
              port's network, and a port an instance holds supports one subnet per IP version.
              An entry without `ip_address` keeps an address the port already has in that
              subnet, in the order the port reports them, or takes a free one when the port
              has none. Addresses that no entry keeps are released.

          port_security_enabled: When true, the network driver enforces port security on this port (anti-spoofing
              checks and security-group filtering apply). When false, all traffic is allowed
              and security groups are not applied.

          security_group_ids: List of security group IDs. Replaces the full set of security groups attached to
              the port. Send `[]` to detach all groups; omit the field to leave existing
              groups unchanged.

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
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return await self._patch(
            path_template("/cloud/v1/projects/{project_id}/ports/{port_id}", project_id=project_id, port_id=port_id),
            body=await async_maybe_transform(
                {
                    "allowed_address_pairs": allowed_address_pairs,
                    "ip_assignments": ip_assignments,
                    "port_security_enabled": port_security_enabled,
                    "security_group_ids": security_group_ids,
                    "tags": tags,
                },
                port_update_params.PortUpdateParams,
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
        attached: bool | Omit = omit,
        attached_to_resource_ids: SequenceNotStr[str] | Omit = omit,
        attached_to_resource_types: List[
            Literal[
                "baremetal_server",
                "basic_vm",
                "dhcp",
                "gpu_baremetal_server",
                "gpu_virtual_server",
                "instance",
                "load_balancer",
                "router",
            ]
        ]
        | Omit = omit,
        created_at: port_list_params.CreatedAt | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        ip_address: port_list_params.IPAddress | Omit = omit,
        limit: int | Omit = omit,
        managed: bool | Omit = omit,
        managed_by: Literal[
            "file_share",
            "gpu_baremetal_cluster",
            "gpu_virtual_cluster",
            "k8s_cluster",
            "load_balancer",
            "network",
            "router",
            "system",
        ]
        | Omit = omit,
        managed_by_resource_ids: SequenceNotStr[str] | Omit = omit,
        managed_by_resource_names: SequenceNotStr[str] | Omit = omit,
        network_ids: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal[
            "created_at.asc",
            "created_at.desc",
            "network_grouping.asc",
            "region_id.asc",
            "region_id.desc",
            "updated_at.asc",
            "updated_at.desc",
        ]
        | Omit = omit,
        public: bool | Omit = omit,
        region_ids: Iterable[int] | Omit = omit,
        security_group_ids: SequenceNotStr[str] | Omit = omit,
        subnet_ids: SequenceNotStr[str] | Omit = omit,
        tag_key: port_list_params.TagKey | Omit = omit,
        tag_value: port_list_params.TagValue | Omit = omit,
        tags: Dict[str, SequenceNotStr[str]] | Omit = omit,
        updated_at: port_list_params.UpdatedAt | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Port, AsyncOffsetPage[Port]]:
        """
        List a project's ports across all regions.

        Args:
          project_id: Project ID

          attached: Filter attached (true) or standalone (false) ports.

          attached_to_resource_ids: Filter by attached resource ID(s). Matches ports attached to any of the given
              resources.

          attached_to_resource_types: Filter by attachment resource type(s). A port matches if its type is any of the
              given values.

          created_at: Range filter on creation time.

          ids: Filter by port UUID(s).

          ip_address: Filter by fixed IP address.

          limit: Max items to return.

          managed: Filter by managed status. true = managed by a service, false =
              customer-operated. A port with a manager type that this API version does not
              know counts as managed, but its `managed_by` is null. Cannot be combined with
              `managed_by` when false.

          managed_by: Filter by manager type, e.g. system or `k8s_cluster`.

          managed_by_resource_ids: Filter by managing resource ID(s).

          managed_by_resource_names: Filter by managing resource name(s).

          network_ids: Filter by network ID(s).

          offset: Items to skip.

          order_by: Sort field and direction. `network_grouping.asc` keeps the ports of one network
              together. In each region, the networks shared with the project come first, in
              the order of the share. If no shared network is public, the default public
              network of the region comes next. Then come other public networks, then all
              other networks.

          public: Filter ports on networks that give publicly routed address space (true) or not
              (false).

          region_ids: Filter by region ID(s). Omit = all regions.

          security_group_ids: Filter by security group ID(s). A port matches if it has any of the given
              security groups.

          subnet_ids: Filter by subnet ID(s). A port matches if it has a fixed IP in any of the given
              subnets.

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
            path_template("/cloud/v1/projects/{project_id}/ports", project_id=project_id),
            page=AsyncOffsetPage[Port],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "attached": attached,
                        "attached_to_resource_ids": attached_to_resource_ids,
                        "attached_to_resource_types": attached_to_resource_types,
                        "created_at": created_at,
                        "ids": ids,
                        "ip_address": ip_address,
                        "limit": limit,
                        "managed": managed,
                        "managed_by": managed_by,
                        "managed_by_resource_ids": managed_by_resource_ids,
                        "managed_by_resource_names": managed_by_resource_names,
                        "network_ids": network_ids,
                        "offset": offset,
                        "order_by": order_by,
                        "public": public,
                        "region_ids": region_ids,
                        "security_group_ids": security_group_ids,
                        "subnet_ids": subnet_ids,
                        "tag_key": tag_key,
                        "tag_value": tag_value,
                        "tags": tags,
                        "updated_at": updated_at,
                    },
                    port_list_params.PortListParams,
                ),
            ),
            model=Port,
        )

    async def delete(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Delete a port that no compute resource uses.

        The request returns a task. The
        task deletes the port. Effects

        - A floating IP of the port stays in the project. The task removes it from the
          port.
        - Each IPv4 address on the region's public network goes back to the external IP
          quota. Rules
        - The port must not be attached. Detach it from the compute resource first.
        - The platform manages ports of routers, load balancers and DHCP. You cannot
          delete these ports.
        - A port that an attach or detach operation holds cannot be deleted. Try again
          when the operation ends.
        - An address of the port must not be in `allowed_address_pairs` of other ports.
          Remove these entries first.

        Args:
          project_id: Project ID

          port_id: Port ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return await self._delete(
            path_template("/cloud/v1/projects/{project_id}/ports/{port_id}", project_id=project_id, port_id=port_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def convert(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        target_type: Literal["floating_ip"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Converts a port to a floating IP with the same address.

        The task deletes the
        port and creates the floating IP. The port must be unattached, be on a public
        network and have exactly one IPv4 address.

        The external IP quota decreases by one and the floating IP quota increases by
        one.

        If the floating IP create fails, the task creates the port again with the same
        address. The new port gets a new ID. It keeps only the network, name,
        description, security groups, port security, allowed address pairs and tags.
        Other attributes get their default values.

        A concurrent network operation can cause the conversion to fail. In rare cases
        the address is then lost, and you must create a new one.

        Args:
          project_id: Project ID

          port_id: Port ID

          target_type: Resource type to convert the port to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return await self._post(
            path_template(
                "/cloud/v1/projects/{project_id}/ports/{port_id}/convert", project_id=project_id, port_id=port_id
            ),
            body=await async_maybe_transform({"target_type": target_type}, port_convert_params.PortConvertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Port:
        """
        Get port

        Args:
          project_id: Project ID

          port_id: Port ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return await self._get(
            path_template("/cloud/v1/projects/{project_id}/ports/{port_id}", project_id=project_id, port_id=port_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Port,
        )


class PortsResourceWithRawResponse:
    def __init__(self, ports: PortsResource) -> None:
        self._ports = ports

        self.create = to_raw_response_wrapper(
            ports.create,
        )
        self.update = to_raw_response_wrapper(
            ports.update,
        )
        self.list = to_raw_response_wrapper(
            ports.list,
        )
        self.delete = to_raw_response_wrapper(
            ports.delete,
        )
        self.convert = to_raw_response_wrapper(
            ports.convert,
        )
        self.get = to_raw_response_wrapper(
            ports.get,
        )


class AsyncPortsResourceWithRawResponse:
    def __init__(self, ports: AsyncPortsResource) -> None:
        self._ports = ports

        self.create = async_to_raw_response_wrapper(
            ports.create,
        )
        self.update = async_to_raw_response_wrapper(
            ports.update,
        )
        self.list = async_to_raw_response_wrapper(
            ports.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ports.delete,
        )
        self.convert = async_to_raw_response_wrapper(
            ports.convert,
        )
        self.get = async_to_raw_response_wrapper(
            ports.get,
        )


class PortsResourceWithStreamingResponse:
    def __init__(self, ports: PortsResource) -> None:
        self._ports = ports

        self.create = to_streamed_response_wrapper(
            ports.create,
        )
        self.update = to_streamed_response_wrapper(
            ports.update,
        )
        self.list = to_streamed_response_wrapper(
            ports.list,
        )
        self.delete = to_streamed_response_wrapper(
            ports.delete,
        )
        self.convert = to_streamed_response_wrapper(
            ports.convert,
        )
        self.get = to_streamed_response_wrapper(
            ports.get,
        )


class AsyncPortsResourceWithStreamingResponse:
    def __init__(self, ports: AsyncPortsResource) -> None:
        self._ports = ports

        self.create = async_to_streamed_response_wrapper(
            ports.create,
        )
        self.update = async_to_streamed_response_wrapper(
            ports.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ports.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ports.delete,
        )
        self.convert = async_to_streamed_response_wrapper(
            ports.convert,
        )
        self.get = async_to_streamed_response_wrapper(
            ports.get,
        )

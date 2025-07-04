# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional

import httpx

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
from .statuses import (
    StatusesResource,
    AsyncStatusesResource,
    StatusesResourceWithRawResponse,
    AsyncStatusesResourceWithRawResponse,
    StatusesResourceWithStreamingResponse,
    AsyncStatusesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from .listeners import (
    ListenersResource,
    AsyncListenersResource,
    ListenersResourceWithRawResponse,
    AsyncListenersResourceWithRawResponse,
    ListenersResourceWithStreamingResponse,
    AsyncListenersResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .pools.pools import (
    PoolsResource,
    AsyncPoolsResource,
    PoolsResourceWithRawResponse,
    AsyncPoolsResourceWithRawResponse,
    PoolsResourceWithStreamingResponse,
    AsyncPoolsResourceWithStreamingResponse,
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
    InterfaceIPFamily,
    LoadBalancerMemberConnectivity,
    load_balancer_get_params,
    load_balancer_list_params,
    load_balancer_create_params,
    load_balancer_resize_params,
    load_balancer_update_params,
    load_balancer_failover_params,
)
from ...._base_client import AsyncPaginator, make_request_options
from .l7_policies.l7_policies import (
    L7PoliciesResource,
    AsyncL7PoliciesResource,
    L7PoliciesResourceWithRawResponse,
    AsyncL7PoliciesResourceWithRawResponse,
    L7PoliciesResourceWithStreamingResponse,
    AsyncL7PoliciesResourceWithStreamingResponse,
)
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.load_balancer import LoadBalancer
from ....types.cloud.interface_ip_family import InterfaceIPFamily
from ....types.cloud.tag_update_map_param import TagUpdateMapParam
from ....types.cloud.load_balancer_member_connectivity import LoadBalancerMemberConnectivity

__all__ = ["LoadBalancersResource", "AsyncLoadBalancersResource"]


class LoadBalancersResource(SyncAPIResource):
    @cached_property
    def l7_policies(self) -> L7PoliciesResource:
        return L7PoliciesResource(self._client)

    @cached_property
    def flavors(self) -> FlavorsResource:
        return FlavorsResource(self._client)

    @cached_property
    def listeners(self) -> ListenersResource:
        return ListenersResource(self._client)

    @cached_property
    def pools(self) -> PoolsResource:
        return PoolsResource(self._client)

    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def statuses(self) -> StatusesResource:
        return StatusesResource(self._client)

    @cached_property
    def with_raw_response(self) -> LoadBalancersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return LoadBalancersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoadBalancersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return LoadBalancersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str | NotGiven = NOT_GIVEN,
        floating_ip: load_balancer_create_params.FloatingIP | NotGiven = NOT_GIVEN,
        listeners: Iterable[load_balancer_create_params.Listener] | NotGiven = NOT_GIVEN,
        logging: load_balancer_create_params.Logging | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        name_template: str | NotGiven = NOT_GIVEN,
        preferred_connectivity: LoadBalancerMemberConnectivity | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        vip_ip_family: InterfaceIPFamily | NotGiven = NOT_GIVEN,
        vip_network_id: str | NotGiven = NOT_GIVEN,
        vip_port_id: str | NotGiven = NOT_GIVEN,
        vip_subnet_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer

        Args:
          flavor: Load balancer flavor name

          floating_ip: Floating IP configuration for assignment

          listeners: Load balancer listeners. Maximum 50 per LB (excluding Prometheus endpoint
              listener).

          logging: Logging configuration

          name: Load balancer name

          name_template: Load balancer name which will be changed by template.

          preferred_connectivity: Preferred option to establish connectivity between load balancer and its pools
              members. L2 provides best performance, L3 provides less IPs usage. It is taking
              effect only if `instance_id` + `ip_address` is provided, not `subnet_id` +
              `ip_address`, because we're considering this as intentional `subnet_id`
              specification.

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          vip_ip_family: IP family for load balancer subnet auto-selection if `vip_network_id` is
              specified

          vip_network_id: Network ID for load balancer. If not specified, default external network will be
              used. Mutually exclusive with `vip_port_id`

          vip_port_id: Existing Reserved Fixed IP port ID for load balancer. Mutually exclusive with
              `vip_network_id`

          vip_subnet_id: Subnet ID for load balancer. If not specified, any subnet from `vip_network_id`
              will be selected. Ignored when `vip_network_id` is not specified.

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
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "flavor": flavor,
                    "floating_ip": floating_ip,
                    "listeners": listeners,
                    "logging": logging,
                    "name": name,
                    "name_template": name_template,
                    "preferred_connectivity": preferred_connectivity,
                    "tags": tags,
                    "vip_ip_family": vip_ip_family,
                    "vip_network_id": vip_network_id,
                    "vip_port_id": vip_port_id,
                    "vip_subnet_id": vip_subnet_id,
                },
                load_balancer_create_params.LoadBalancerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        logging: load_balancer_update_params.Logging | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        preferred_connectivity: LoadBalancerMemberConnectivity | NotGiven = NOT_GIVEN,
        tags: Optional[TagUpdateMapParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Rename load balancer, activate/deactivate logging, update preferred connectivity
        type and/or modify load balancer tags. The request will only process the fields
        that are provided in the request body. Any fields that are not included will
        remain unchanged.

        Args:
          logging: Logging configuration

          name: Name.

          preferred_connectivity: Preferred option to establish connectivity between load balancer and its pools
              members

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
              key-value pairs to add or update tags. Set tag values to `null` to remove tags.
              Unspecified tags remain unchanged. Read-only tags are always preserved and
              cannot be modified. **Examples:**

              - **Add/update tags:**
                `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
                updates existing ones.
              - **Delete tags:** `{'tags': {'`old_tag`': null}}` removes specific tags.
              - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
                tags are preserved).
              - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
                specified tags.
              - **Mixed operations:**
                `{'tags': {'environment': 'production', '`cost_center`': 'engineering', '`deprecated_tag`': null}}`
                adds/updates 'environment' and '`cost_center`' while removing
                '`deprecated_tag`', preserving other existing tags.
              - **Replace all:** first delete existing tags with null values, then add new
                ones in the same request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not loadbalancer_id:
            raise ValueError(f"Expected a non-empty value for `loadbalancer_id` but received {loadbalancer_id!r}")
        return self._patch(
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}",
            body=maybe_transform(
                {
                    "logging": logging,
                    "name": name,
                    "preferred_connectivity": preferred_connectivity,
                    "tags": tags,
                },
                load_balancer_update_params.LoadBalancerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancer,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        assigned_floating: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        logging_enabled: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        show_stats: bool | NotGiven = NOT_GIVEN,
        tag_key: List[str] | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        with_ddos: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[LoadBalancer]:
        """
        List load balancers

        Args:
          assigned_floating: With or without assigned floating IP

          limit: Limit the number of returned limit request entities.

          logging_enabled: With or without logging

          name: Filter by name

          offset: Offset value is used to exclude the first set of records from the result.

          order_by: Ordering Load Balancer list result by name, `created_at`, `updated_at`,
              `operating_status`, `provisioning_status`, `vip_address`, `vip_ip_family` and
              flavor fields of the load balancer and directions (name.asc), default is
              "`created_at`.asc"

          show_stats: Show statistics

          tag_key: Filter by tag keys.

          tag_key_value: Filter by tag key-value pairs. Must be a valid JSON string.

          with_ddos: Show Advanced DDoS protection profile, if exists

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
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}",
            page=SyncOffsetPage[LoadBalancer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "assigned_floating": assigned_floating,
                        "limit": limit,
                        "logging_enabled": logging_enabled,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "show_stats": show_stats,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                        "with_ddos": with_ddos,
                    },
                    load_balancer_list_params.LoadBalancerListParams,
                ),
            ),
            model=LoadBalancer,
        )

    def delete(
        self,
        loadbalancer_id: str,
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
        Delete load balancer

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
        if not loadbalancer_id:
            raise ValueError(f"Expected a non-empty value for `loadbalancer_id` but received {loadbalancer_id!r}")
        return self._delete(
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def failover(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Failover load balancer

        Args:
          force: Validate current load balancer status before failover or not.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not loadbalancer_id:
            raise ValueError(f"Expected a non-empty value for `loadbalancer_id` but received {loadbalancer_id!r}")
        return self._post(
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/failover",
            body=maybe_transform({"force": force}, load_balancer_failover_params.LoadBalancerFailoverParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        show_stats: bool | NotGiven = NOT_GIVEN,
        with_ddos: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Get load balancer

        Args:
          show_stats: Show statistics

          with_ddos: Show DDoS profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not loadbalancer_id:
            raise ValueError(f"Expected a non-empty value for `loadbalancer_id` but received {loadbalancer_id!r}")
        return self._get(
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "show_stats": show_stats,
                        "with_ddos": with_ddos,
                    },
                    load_balancer_get_params.LoadBalancerGetParams,
                ),
            ),
            cast_to=LoadBalancer,
        )

    def resize(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Resize load balancer

        Args:
          flavor: Name of the desired flavor to resize to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not loadbalancer_id:
            raise ValueError(f"Expected a non-empty value for `loadbalancer_id` but received {loadbalancer_id!r}")
        return self._post(
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/resize",
            body=maybe_transform({"flavor": flavor}, load_balancer_resize_params.LoadBalancerResizeParams),
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
        flavor: str | NotGiven = NOT_GIVEN,
        floating_ip: load_balancer_create_params.FloatingIP | NotGiven = NOT_GIVEN,
        listeners: Iterable[load_balancer_create_params.Listener] | NotGiven = NOT_GIVEN,
        logging: load_balancer_create_params.Logging | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        name_template: str | NotGiven = NOT_GIVEN,
        preferred_connectivity: LoadBalancerMemberConnectivity | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        vip_ip_family: InterfaceIPFamily | NotGiven = NOT_GIVEN,
        vip_network_id: str | NotGiven = NOT_GIVEN,
        vip_port_id: str | NotGiven = NOT_GIVEN,
        vip_subnet_id: str | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancer:
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            floating_ip=floating_ip,
            listeners=listeners,
            logging=logging,
            name=name,
            name_template=name_template,
            preferred_connectivity=preferred_connectivity,
            tags=tags,
            vip_ip_family=vip_ip_family,
            vip_network_id=vip_network_id,
            vip_port_id=vip_port_id,
            vip_subnet_id=vip_subnet_id,
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
            or not task.created_resources.loadbalancers
            or len(task.created_resources.loadbalancers) != 1
        ):
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return self.get(
            loadbalancer_id=task.created_resources.loadbalancers[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    def delete_and_poll(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete load balancer and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            loadbalancer_id=loadbalancer_id,
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

    def failover_and_poll(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        force: bool | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancer:
        """
        Failover load balancer and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.failover(
            loadbalancer_id=loadbalancer_id,
            project_id=project_id,
            region_id=region_id,
            force=force,
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
            loadbalancer_id=loadbalancer_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    def resize_and_poll(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancer:
        """
        Resize load balancer and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.resize(
            loadbalancer_id=loadbalancer_id,
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
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
            loadbalancer_id=loadbalancer_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )


class AsyncLoadBalancersResource(AsyncAPIResource):
    @cached_property
    def l7_policies(self) -> AsyncL7PoliciesResource:
        return AsyncL7PoliciesResource(self._client)

    @cached_property
    def flavors(self) -> AsyncFlavorsResource:
        return AsyncFlavorsResource(self._client)

    @cached_property
    def listeners(self) -> AsyncListenersResource:
        return AsyncListenersResource(self._client)

    @cached_property
    def pools(self) -> AsyncPoolsResource:
        return AsyncPoolsResource(self._client)

    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def statuses(self) -> AsyncStatusesResource:
        return AsyncStatusesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLoadBalancersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoadBalancersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoadBalancersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncLoadBalancersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str | NotGiven = NOT_GIVEN,
        floating_ip: load_balancer_create_params.FloatingIP | NotGiven = NOT_GIVEN,
        listeners: Iterable[load_balancer_create_params.Listener] | NotGiven = NOT_GIVEN,
        logging: load_balancer_create_params.Logging | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        name_template: str | NotGiven = NOT_GIVEN,
        preferred_connectivity: LoadBalancerMemberConnectivity | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        vip_ip_family: InterfaceIPFamily | NotGiven = NOT_GIVEN,
        vip_network_id: str | NotGiven = NOT_GIVEN,
        vip_port_id: str | NotGiven = NOT_GIVEN,
        vip_subnet_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer

        Args:
          flavor: Load balancer flavor name

          floating_ip: Floating IP configuration for assignment

          listeners: Load balancer listeners. Maximum 50 per LB (excluding Prometheus endpoint
              listener).

          logging: Logging configuration

          name: Load balancer name

          name_template: Load balancer name which will be changed by template.

          preferred_connectivity: Preferred option to establish connectivity between load balancer and its pools
              members. L2 provides best performance, L3 provides less IPs usage. It is taking
              effect only if `instance_id` + `ip_address` is provided, not `subnet_id` +
              `ip_address`, because we're considering this as intentional `subnet_id`
              specification.

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          vip_ip_family: IP family for load balancer subnet auto-selection if `vip_network_id` is
              specified

          vip_network_id: Network ID for load balancer. If not specified, default external network will be
              used. Mutually exclusive with `vip_port_id`

          vip_port_id: Existing Reserved Fixed IP port ID for load balancer. Mutually exclusive with
              `vip_network_id`

          vip_subnet_id: Subnet ID for load balancer. If not specified, any subnet from `vip_network_id`
              will be selected. Ignored when `vip_network_id` is not specified.

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
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "flavor": flavor,
                    "floating_ip": floating_ip,
                    "listeners": listeners,
                    "logging": logging,
                    "name": name,
                    "name_template": name_template,
                    "preferred_connectivity": preferred_connectivity,
                    "tags": tags,
                    "vip_ip_family": vip_ip_family,
                    "vip_network_id": vip_network_id,
                    "vip_port_id": vip_port_id,
                    "vip_subnet_id": vip_subnet_id,
                },
                load_balancer_create_params.LoadBalancerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        logging: load_balancer_update_params.Logging | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        preferred_connectivity: LoadBalancerMemberConnectivity | NotGiven = NOT_GIVEN,
        tags: Optional[TagUpdateMapParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Rename load balancer, activate/deactivate logging, update preferred connectivity
        type and/or modify load balancer tags. The request will only process the fields
        that are provided in the request body. Any fields that are not included will
        remain unchanged.

        Args:
          logging: Logging configuration

          name: Name.

          preferred_connectivity: Preferred option to establish connectivity between load balancer and its pools
              members

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
              key-value pairs to add or update tags. Set tag values to `null` to remove tags.
              Unspecified tags remain unchanged. Read-only tags are always preserved and
              cannot be modified. **Examples:**

              - **Add/update tags:**
                `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
                updates existing ones.
              - **Delete tags:** `{'tags': {'`old_tag`': null}}` removes specific tags.
              - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
                tags are preserved).
              - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
                specified tags.
              - **Mixed operations:**
                `{'tags': {'environment': 'production', '`cost_center`': 'engineering', '`deprecated_tag`': null}}`
                adds/updates 'environment' and '`cost_center`' while removing
                '`deprecated_tag`', preserving other existing tags.
              - **Replace all:** first delete existing tags with null values, then add new
                ones in the same request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not loadbalancer_id:
            raise ValueError(f"Expected a non-empty value for `loadbalancer_id` but received {loadbalancer_id!r}")
        return await self._patch(
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}",
            body=await async_maybe_transform(
                {
                    "logging": logging,
                    "name": name,
                    "preferred_connectivity": preferred_connectivity,
                    "tags": tags,
                },
                load_balancer_update_params.LoadBalancerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancer,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        assigned_floating: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        logging_enabled: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        show_stats: bool | NotGiven = NOT_GIVEN,
        tag_key: List[str] | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        with_ddos: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LoadBalancer, AsyncOffsetPage[LoadBalancer]]:
        """
        List load balancers

        Args:
          assigned_floating: With or without assigned floating IP

          limit: Limit the number of returned limit request entities.

          logging_enabled: With or without logging

          name: Filter by name

          offset: Offset value is used to exclude the first set of records from the result.

          order_by: Ordering Load Balancer list result by name, `created_at`, `updated_at`,
              `operating_status`, `provisioning_status`, `vip_address`, `vip_ip_family` and
              flavor fields of the load balancer and directions (name.asc), default is
              "`created_at`.asc"

          show_stats: Show statistics

          tag_key: Filter by tag keys.

          tag_key_value: Filter by tag key-value pairs. Must be a valid JSON string.

          with_ddos: Show Advanced DDoS protection profile, if exists

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
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}",
            page=AsyncOffsetPage[LoadBalancer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "assigned_floating": assigned_floating,
                        "limit": limit,
                        "logging_enabled": logging_enabled,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "show_stats": show_stats,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                        "with_ddos": with_ddos,
                    },
                    load_balancer_list_params.LoadBalancerListParams,
                ),
            ),
            model=LoadBalancer,
        )

    async def delete(
        self,
        loadbalancer_id: str,
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
        Delete load balancer

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
        if not loadbalancer_id:
            raise ValueError(f"Expected a non-empty value for `loadbalancer_id` but received {loadbalancer_id!r}")
        return await self._delete(
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def failover(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Failover load balancer

        Args:
          force: Validate current load balancer status before failover or not.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not loadbalancer_id:
            raise ValueError(f"Expected a non-empty value for `loadbalancer_id` but received {loadbalancer_id!r}")
        return await self._post(
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/failover",
            body=await async_maybe_transform(
                {"force": force}, load_balancer_failover_params.LoadBalancerFailoverParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        show_stats: bool | NotGiven = NOT_GIVEN,
        with_ddos: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Get load balancer

        Args:
          show_stats: Show statistics

          with_ddos: Show DDoS profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not loadbalancer_id:
            raise ValueError(f"Expected a non-empty value for `loadbalancer_id` but received {loadbalancer_id!r}")
        return await self._get(
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "show_stats": show_stats,
                        "with_ddos": with_ddos,
                    },
                    load_balancer_get_params.LoadBalancerGetParams,
                ),
            ),
            cast_to=LoadBalancer,
        )

    async def resize(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Resize load balancer

        Args:
          flavor: Name of the desired flavor to resize to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not loadbalancer_id:
            raise ValueError(f"Expected a non-empty value for `loadbalancer_id` but received {loadbalancer_id!r}")
        return await self._post(
            f"/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/resize",
            body=await async_maybe_transform({"flavor": flavor}, load_balancer_resize_params.LoadBalancerResizeParams),
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
        flavor: str | NotGiven = NOT_GIVEN,
        floating_ip: load_balancer_create_params.FloatingIP | NotGiven = NOT_GIVEN,
        listeners: Iterable[load_balancer_create_params.Listener] | NotGiven = NOT_GIVEN,
        logging: load_balancer_create_params.Logging | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        name_template: str | NotGiven = NOT_GIVEN,
        preferred_connectivity: LoadBalancerMemberConnectivity | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        vip_ip_family: InterfaceIPFamily | NotGiven = NOT_GIVEN,
        vip_network_id: str | NotGiven = NOT_GIVEN,
        vip_port_id: str | NotGiven = NOT_GIVEN,
        vip_subnet_id: str | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancer:
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            floating_ip=floating_ip,
            listeners=listeners,
            logging=logging,
            name=name,
            name_template=name_template,
            preferred_connectivity=preferred_connectivity,
            tags=tags,
            vip_ip_family=vip_ip_family,
            vip_network_id=vip_network_id,
            vip_port_id=vip_port_id,
            vip_subnet_id=vip_subnet_id,
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
            or not task.created_resources.loadbalancers
            or len(task.created_resources.loadbalancers) != 1
        ):
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return await self.get(
            loadbalancer_id=task.created_resources.loadbalancers[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    async def delete_and_poll(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete load balancer and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            loadbalancer_id=loadbalancer_id,
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

    async def failover_and_poll(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        force: bool | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancer:
        """
        Failover load balancer and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.failover(
            loadbalancer_id=loadbalancer_id,
            project_id=project_id,
            region_id=region_id,
            force=force,
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
            loadbalancer_id=loadbalancer_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    async def resize_and_poll(
        self,
        loadbalancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancer:
        """
        Resize load balancer and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.resize(
            loadbalancer_id=loadbalancer_id,
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
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
            loadbalancer_id=loadbalancer_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )


class LoadBalancersResourceWithRawResponse:
    def __init__(self, load_balancers: LoadBalancersResource) -> None:
        self._load_balancers = load_balancers

        self.create = to_raw_response_wrapper(
            load_balancers.create,
        )
        self.update = to_raw_response_wrapper(
            load_balancers.update,
        )
        self.list = to_raw_response_wrapper(
            load_balancers.list,
        )
        self.delete = to_raw_response_wrapper(
            load_balancers.delete,
        )
        self.failover = to_raw_response_wrapper(
            load_balancers.failover,
        )
        self.get = to_raw_response_wrapper(
            load_balancers.get,
        )
        self.resize = to_raw_response_wrapper(
            load_balancers.resize,
        )

    @cached_property
    def l7_policies(self) -> L7PoliciesResourceWithRawResponse:
        return L7PoliciesResourceWithRawResponse(self._load_balancers.l7_policies)

    @cached_property
    def flavors(self) -> FlavorsResourceWithRawResponse:
        return FlavorsResourceWithRawResponse(self._load_balancers.flavors)

    @cached_property
    def listeners(self) -> ListenersResourceWithRawResponse:
        return ListenersResourceWithRawResponse(self._load_balancers.listeners)

    @cached_property
    def pools(self) -> PoolsResourceWithRawResponse:
        return PoolsResourceWithRawResponse(self._load_balancers.pools)

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._load_balancers.metrics)

    @cached_property
    def statuses(self) -> StatusesResourceWithRawResponse:
        return StatusesResourceWithRawResponse(self._load_balancers.statuses)


class AsyncLoadBalancersResourceWithRawResponse:
    def __init__(self, load_balancers: AsyncLoadBalancersResource) -> None:
        self._load_balancers = load_balancers

        self.create = async_to_raw_response_wrapper(
            load_balancers.create,
        )
        self.update = async_to_raw_response_wrapper(
            load_balancers.update,
        )
        self.list = async_to_raw_response_wrapper(
            load_balancers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            load_balancers.delete,
        )
        self.failover = async_to_raw_response_wrapper(
            load_balancers.failover,
        )
        self.get = async_to_raw_response_wrapper(
            load_balancers.get,
        )
        self.resize = async_to_raw_response_wrapper(
            load_balancers.resize,
        )

    @cached_property
    def l7_policies(self) -> AsyncL7PoliciesResourceWithRawResponse:
        return AsyncL7PoliciesResourceWithRawResponse(self._load_balancers.l7_policies)

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithRawResponse:
        return AsyncFlavorsResourceWithRawResponse(self._load_balancers.flavors)

    @cached_property
    def listeners(self) -> AsyncListenersResourceWithRawResponse:
        return AsyncListenersResourceWithRawResponse(self._load_balancers.listeners)

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithRawResponse:
        return AsyncPoolsResourceWithRawResponse(self._load_balancers.pools)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._load_balancers.metrics)

    @cached_property
    def statuses(self) -> AsyncStatusesResourceWithRawResponse:
        return AsyncStatusesResourceWithRawResponse(self._load_balancers.statuses)


class LoadBalancersResourceWithStreamingResponse:
    def __init__(self, load_balancers: LoadBalancersResource) -> None:
        self._load_balancers = load_balancers

        self.create = to_streamed_response_wrapper(
            load_balancers.create,
        )
        self.update = to_streamed_response_wrapper(
            load_balancers.update,
        )
        self.list = to_streamed_response_wrapper(
            load_balancers.list,
        )
        self.delete = to_streamed_response_wrapper(
            load_balancers.delete,
        )
        self.failover = to_streamed_response_wrapper(
            load_balancers.failover,
        )
        self.get = to_streamed_response_wrapper(
            load_balancers.get,
        )
        self.resize = to_streamed_response_wrapper(
            load_balancers.resize,
        )

    @cached_property
    def l7_policies(self) -> L7PoliciesResourceWithStreamingResponse:
        return L7PoliciesResourceWithStreamingResponse(self._load_balancers.l7_policies)

    @cached_property
    def flavors(self) -> FlavorsResourceWithStreamingResponse:
        return FlavorsResourceWithStreamingResponse(self._load_balancers.flavors)

    @cached_property
    def listeners(self) -> ListenersResourceWithStreamingResponse:
        return ListenersResourceWithStreamingResponse(self._load_balancers.listeners)

    @cached_property
    def pools(self) -> PoolsResourceWithStreamingResponse:
        return PoolsResourceWithStreamingResponse(self._load_balancers.pools)

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._load_balancers.metrics)

    @cached_property
    def statuses(self) -> StatusesResourceWithStreamingResponse:
        return StatusesResourceWithStreamingResponse(self._load_balancers.statuses)


class AsyncLoadBalancersResourceWithStreamingResponse:
    def __init__(self, load_balancers: AsyncLoadBalancersResource) -> None:
        self._load_balancers = load_balancers

        self.create = async_to_streamed_response_wrapper(
            load_balancers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            load_balancers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            load_balancers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            load_balancers.delete,
        )
        self.failover = async_to_streamed_response_wrapper(
            load_balancers.failover,
        )
        self.get = async_to_streamed_response_wrapper(
            load_balancers.get,
        )
        self.resize = async_to_streamed_response_wrapper(
            load_balancers.resize,
        )

    @cached_property
    def l7_policies(self) -> AsyncL7PoliciesResourceWithStreamingResponse:
        return AsyncL7PoliciesResourceWithStreamingResponse(self._load_balancers.l7_policies)

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithStreamingResponse:
        return AsyncFlavorsResourceWithStreamingResponse(self._load_balancers.flavors)

    @cached_property
    def listeners(self) -> AsyncListenersResourceWithStreamingResponse:
        return AsyncListenersResourceWithStreamingResponse(self._load_balancers.listeners)

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithStreamingResponse:
        return AsyncPoolsResourceWithStreamingResponse(self._load_balancers.pools)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._load_balancers.metrics)

    @cached_property
    def statuses(self) -> AsyncStatusesResourceWithStreamingResponse:
        return AsyncStatusesResourceWithStreamingResponse(self._load_balancers.statuses)

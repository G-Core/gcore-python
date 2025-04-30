# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

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
from ....types.cloud.tag_update_list_param import TagUpdateListParam
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

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return LoadBalancersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoadBalancersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
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
        tags: TagUpdateListParam | NotGiven = NOT_GIVEN,
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
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].post.parameters[1].schema"

          flavor: '#/components/schemas/CreateLoadbalancerSerializer/properties/flavor'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.flavor"

          floating_ip: '#/components/schemas/CreateLoadbalancerSerializer/properties/floating_ip'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.floating_ip"

          listeners: '#/components/schemas/CreateLoadbalancerSerializer/properties/listeners'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.listeners"

          logging: '#/components/schemas/CreateLoadbalancerSerializer/properties/logging'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.logging"

          name: '#/components/schemas/CreateLoadbalancerSerializer/properties/name'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.name"

          name_template: '#/components/schemas/CreateLoadbalancerSerializer/properties/name_template'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.name_template"

          preferred_connectivity: '#/components/schemas/CreateLoadbalancerSerializer/properties/preferred_connectivity'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.preferred_connectivity"

          tags: '#/components/schemas/CreateLoadbalancerSerializer/properties/tags'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.tags"

          vip_ip_family: '#/components/schemas/CreateLoadbalancerSerializer/properties/vip_ip_family'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.vip_ip_family"

          vip_network_id: '#/components/schemas/CreateLoadbalancerSerializer/properties/vip_network_id'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.vip_network_id"

          vip_port_id: '#/components/schemas/CreateLoadbalancerSerializer/properties/vip_port_id'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.vip_port_id"

          vip_subnet_id: '#/components/schemas/CreateLoadbalancerSerializer/properties/vip_subnet_id'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.vip_subnet_id"

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Rename load balancer, activate/deactivate logs or update preferred connectivity
        for load balancer

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].patch.parameters[1].schema"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].patch.parameters[2].schema"

          logging: '#/components/schemas/LoadBalancerPatchSerializer/properties/logging'
              "$.components.schemas.LoadBalancerPatchSerializer.properties.logging"

          name: '#/components/schemas/LoadBalancerPatchSerializer/properties/name'
              "$.components.schemas.LoadBalancerPatchSerializer.properties.name"

          preferred_connectivity: '#/components/schemas/LoadBalancerPatchSerializer/properties/preferred_connectivity'
              "$.components.schemas.LoadBalancerPatchSerializer.properties.preferred_connectivity"

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
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[1].schema"

          assigned_floating: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[2]"

          limit: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[3]"

          logging_enabled: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[4]"

          name: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[5]"

          offset: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[6]"

          order_by: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[7]"

          show_stats: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/8'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[8]"

          tag_key: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/9'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[9]"

          tag_key_value: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/10'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[10]"

          with_ddos: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/11'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[11]"

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
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}']['delete'].parameters[1].schema"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}']['delete'].parameters[2].schema"

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
        Failover loadbalancer

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Ffailover/post/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/failover'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Ffailover/post/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/failover'].post.parameters[1].schema"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Ffailover/post/parameters/2/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/failover'].post.parameters[2].schema"

          force: '#/components/schemas/FailoverLoadBalancer/properties/force'
              "$.components.schemas.FailoverLoadBalancer.properties.force"

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
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].get.parameters[1].schema"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].get.parameters[2].schema"

          show_stats: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].get.parameters[3]"

          with_ddos: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].get.parameters[4]"

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
        Resize loadbalancer

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Fresize/post/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/resize'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Fresize/post/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/resize'].post.parameters[1].schema"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Fresize/post/parameters/2/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/resize'].post.parameters[2].schema"

          flavor: '#/components/schemas/ResizeLoadBalancer/properties/flavor'
              "$.components.schemas.ResizeLoadBalancer.properties.flavor"

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

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoadBalancersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoadBalancersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
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
        tags: TagUpdateListParam | NotGiven = NOT_GIVEN,
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
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].post.parameters[1].schema"

          flavor: '#/components/schemas/CreateLoadbalancerSerializer/properties/flavor'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.flavor"

          floating_ip: '#/components/schemas/CreateLoadbalancerSerializer/properties/floating_ip'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.floating_ip"

          listeners: '#/components/schemas/CreateLoadbalancerSerializer/properties/listeners'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.listeners"

          logging: '#/components/schemas/CreateLoadbalancerSerializer/properties/logging'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.logging"

          name: '#/components/schemas/CreateLoadbalancerSerializer/properties/name'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.name"

          name_template: '#/components/schemas/CreateLoadbalancerSerializer/properties/name_template'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.name_template"

          preferred_connectivity: '#/components/schemas/CreateLoadbalancerSerializer/properties/preferred_connectivity'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.preferred_connectivity"

          tags: '#/components/schemas/CreateLoadbalancerSerializer/properties/tags'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.tags"

          vip_ip_family: '#/components/schemas/CreateLoadbalancerSerializer/properties/vip_ip_family'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.vip_ip_family"

          vip_network_id: '#/components/schemas/CreateLoadbalancerSerializer/properties/vip_network_id'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.vip_network_id"

          vip_port_id: '#/components/schemas/CreateLoadbalancerSerializer/properties/vip_port_id'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.vip_port_id"

          vip_subnet_id: '#/components/schemas/CreateLoadbalancerSerializer/properties/vip_subnet_id'
              "$.components.schemas.CreateLoadbalancerSerializer.properties.vip_subnet_id"

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Rename load balancer, activate/deactivate logs or update preferred connectivity
        for load balancer

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].patch.parameters[1].schema"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].patch.parameters[2].schema"

          logging: '#/components/schemas/LoadBalancerPatchSerializer/properties/logging'
              "$.components.schemas.LoadBalancerPatchSerializer.properties.logging"

          name: '#/components/schemas/LoadBalancerPatchSerializer/properties/name'
              "$.components.schemas.LoadBalancerPatchSerializer.properties.name"

          preferred_connectivity: '#/components/schemas/LoadBalancerPatchSerializer/properties/preferred_connectivity'
              "$.components.schemas.LoadBalancerPatchSerializer.properties.preferred_connectivity"

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
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[1].schema"

          assigned_floating: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[2]"

          limit: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[3]"

          logging_enabled: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[4]"

          name: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[5]"

          offset: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[6]"

          order_by: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[7]"

          show_stats: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/8'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[8]"

          tag_key: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/9'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[9]"

          tag_key_value: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/10'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[10]"

          with_ddos: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/11'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[11]"

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
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}']['delete'].parameters[1].schema"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}']['delete'].parameters[2].schema"

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
        Failover loadbalancer

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Ffailover/post/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/failover'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Ffailover/post/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/failover'].post.parameters[1].schema"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Ffailover/post/parameters/2/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/failover'].post.parameters[2].schema"

          force: '#/components/schemas/FailoverLoadBalancer/properties/force'
              "$.components.schemas.FailoverLoadBalancer.properties.force"

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
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].get.parameters[1].schema"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].get.parameters[2].schema"

          show_stats: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].get.parameters[3]"

          with_ddos: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].get.parameters[4]"

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
        Resize loadbalancer

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Fresize/post/parameters/0/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/resize'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Fresize/post/parameters/1/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/resize'].post.parameters[1].schema"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Fresize/post/parameters/2/schema'
              "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/resize'].post.parameters[2].schema"

          flavor: '#/components/schemas/ResizeLoadBalancer/properties/flavor'
              "$.components.schemas.ResizeLoadBalancer.properties.flavor"

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

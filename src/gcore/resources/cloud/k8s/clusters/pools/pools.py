# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from .nodes import (
    NodesResource,
    AsyncNodesResource,
    NodesResourceWithRawResponse,
    AsyncNodesResourceWithRawResponse,
    NodesResourceWithStreamingResponse,
    AsyncNodesResourceWithStreamingResponse,
)
from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.cloud.k8s.clusters import (
    pool_create_params,
    pool_resize_params,
    pool_update_params,
    pool_check_quota_params,
)
from ......types.cloud.task_id_list import TaskIDList
from ......types.cloud.k8s.clusters.k8s_cluster_pool import K8SClusterPool
from ......types.cloud.k8s.clusters.k8s_cluster_pool_list import K8SClusterPoolList
from ......types.cloud.k8s.clusters.k8s_cluster_pool_quota import K8SClusterPoolQuota

__all__ = ["PoolsResource", "AsyncPoolsResource"]


class PoolsResource(SyncAPIResource):
    @cached_property
    def nodes(self) -> NodesResource:
        return NodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PoolsResourceWithStreamingResponse(self)

    def create(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor_id: str,
        min_node_count: int,
        name: str,
        auto_healing_enabled: Optional[bool] | Omit = omit,
        boot_volume_size: Optional[int] | Omit = omit,
        boot_volume_type: Optional[Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]]
        | Omit = omit,
        crio_config: Optional[Dict[str, str]] | Omit = omit,
        is_public_ipv4: Optional[bool] | Omit = omit,
        kubelet_config: Optional[Dict[str, str]] | Omit = omit,
        labels: Optional[Dict[str, str]] | Omit = omit,
        max_node_count: Optional[int] | Omit = omit,
        servergroup_policy: Optional[Literal["affinity", "anti-affinity", "soft-anti-affinity"]] | Omit = omit,
        taints: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create k8s cluster pool

        Args:
          flavor_id: Flavor ID

          min_node_count: Minimum node count

          name: Pool's name

          auto_healing_enabled: Enable auto healing

          boot_volume_size: Boot volume size

          boot_volume_type: Boot volume type

          crio_config: Cri-o configuration for pool nodes

          is_public_ipv4: Enable public v4 address

          kubelet_config: Kubelet configuration for pool nodes

          labels: Labels applied to the cluster pool

          max_node_count: Maximum node count

          servergroup_policy: Server group policy: anti-affinity, soft-anti-affinity or affinity

          taints: Taints applied to the cluster pool

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        return self._post(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools",
            body=maybe_transform(
                {
                    "flavor_id": flavor_id,
                    "min_node_count": min_node_count,
                    "name": name,
                    "auto_healing_enabled": auto_healing_enabled,
                    "boot_volume_size": boot_volume_size,
                    "boot_volume_type": boot_volume_type,
                    "crio_config": crio_config,
                    "is_public_ipv4": is_public_ipv4,
                    "kubelet_config": kubelet_config,
                    "labels": labels,
                    "max_node_count": max_node_count,
                    "servergroup_policy": servergroup_policy,
                    "taints": taints,
                },
                pool_create_params.PoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        pool_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        auto_healing_enabled: Optional[bool] | Omit = omit,
        labels: Optional[Dict[str, str]] | Omit = omit,
        max_node_count: Optional[int] | Omit = omit,
        min_node_count: Optional[int] | Omit = omit,
        node_count: Optional[int] | Omit = omit,
        taints: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterPool:
        """
        Update k8s cluster pool

        Args:
          auto_healing_enabled: Enable/disable auto healing

          labels: Labels applied to the cluster pool

          max_node_count: Maximum node count

          min_node_count: Minimum node count

          node_count: This field is deprecated. Please use the cluster pool resize handler instead.

          taints: Taints applied to the cluster pool

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        if not pool_name:
            raise ValueError(f"Expected a non-empty value for `pool_name` but received {pool_name!r}")
        return self._patch(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}",
            body=maybe_transform(
                {
                    "auto_healing_enabled": auto_healing_enabled,
                    "labels": labels,
                    "max_node_count": max_node_count,
                    "min_node_count": min_node_count,
                    "node_count": node_count,
                    "taints": taints,
                },
                pool_update_params.PoolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterPool,
        )

    def list(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterPoolList:
        """
        List k8s cluster pools

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
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        return self._get(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterPoolList,
        )

    def delete(
        self,
        pool_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete k8s cluster pool

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
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        if not pool_name:
            raise ValueError(f"Expected a non-empty value for `pool_name` but received {pool_name!r}")
        return self._delete(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def check_quota(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor_id: str,
        boot_volume_size: Optional[int] | Omit = omit,
        max_node_count: Optional[int] | Omit = omit,
        min_node_count: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        node_count: Optional[int] | Omit = omit,
        servergroup_policy: Optional[Literal["affinity", "anti-affinity", "soft-anti-affinity"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterPoolQuota:
        """Calculate quota requirements for a new cluster pool before creation.

        Returns
        exceeded quotas if regional limits would be violated. Use before pool creation
        to validate resource availability. Checks: CPU, RAM, volumes, VMs, GPUs, and
        baremetal quotas depending on flavor type.

        Args:
          project_id: Project ID

          region_id: Region ID

          flavor_id: Flavor ID

          boot_volume_size: Boot volume size

          max_node_count: Maximum node count

          min_node_count: Minimum node count

          name: Name of the cluster pool

          node_count: Maximum node count

          servergroup_policy: Server group policy: anti-affinity, soft-anti-affinity or affinity

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/pools/check_limits",
            body=maybe_transform(
                {
                    "flavor_id": flavor_id,
                    "boot_volume_size": boot_volume_size,
                    "max_node_count": max_node_count,
                    "min_node_count": min_node_count,
                    "name": name,
                    "node_count": node_count,
                    "servergroup_policy": servergroup_policy,
                },
                pool_check_quota_params.PoolCheckQuotaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterPoolQuota,
        )

    def get(
        self,
        pool_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterPool:
        """
        Get k8s cluster pool

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
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        if not pool_name:
            raise ValueError(f"Expected a non-empty value for `pool_name` but received {pool_name!r}")
        return self._get(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterPool,
        )

    def resize(
        self,
        pool_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        node_count: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Resize k8s cluster pool

        Args:
          node_count: Target node count

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        if not pool_name:
            raise ValueError(f"Expected a non-empty value for `pool_name` but received {pool_name!r}")
        return self._post(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}/resize",
            body=maybe_transform({"node_count": node_count}, pool_resize_params.PoolResizeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class AsyncPoolsResource(AsyncAPIResource):
    @cached_property
    def nodes(self) -> AsyncNodesResource:
        return AsyncNodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPoolsResourceWithStreamingResponse(self)

    async def create(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor_id: str,
        min_node_count: int,
        name: str,
        auto_healing_enabled: Optional[bool] | Omit = omit,
        boot_volume_size: Optional[int] | Omit = omit,
        boot_volume_type: Optional[Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]]
        | Omit = omit,
        crio_config: Optional[Dict[str, str]] | Omit = omit,
        is_public_ipv4: Optional[bool] | Omit = omit,
        kubelet_config: Optional[Dict[str, str]] | Omit = omit,
        labels: Optional[Dict[str, str]] | Omit = omit,
        max_node_count: Optional[int] | Omit = omit,
        servergroup_policy: Optional[Literal["affinity", "anti-affinity", "soft-anti-affinity"]] | Omit = omit,
        taints: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create k8s cluster pool

        Args:
          flavor_id: Flavor ID

          min_node_count: Minimum node count

          name: Pool's name

          auto_healing_enabled: Enable auto healing

          boot_volume_size: Boot volume size

          boot_volume_type: Boot volume type

          crio_config: Cri-o configuration for pool nodes

          is_public_ipv4: Enable public v4 address

          kubelet_config: Kubelet configuration for pool nodes

          labels: Labels applied to the cluster pool

          max_node_count: Maximum node count

          servergroup_policy: Server group policy: anti-affinity, soft-anti-affinity or affinity

          taints: Taints applied to the cluster pool

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        return await self._post(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools",
            body=await async_maybe_transform(
                {
                    "flavor_id": flavor_id,
                    "min_node_count": min_node_count,
                    "name": name,
                    "auto_healing_enabled": auto_healing_enabled,
                    "boot_volume_size": boot_volume_size,
                    "boot_volume_type": boot_volume_type,
                    "crio_config": crio_config,
                    "is_public_ipv4": is_public_ipv4,
                    "kubelet_config": kubelet_config,
                    "labels": labels,
                    "max_node_count": max_node_count,
                    "servergroup_policy": servergroup_policy,
                    "taints": taints,
                },
                pool_create_params.PoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        pool_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        auto_healing_enabled: Optional[bool] | Omit = omit,
        labels: Optional[Dict[str, str]] | Omit = omit,
        max_node_count: Optional[int] | Omit = omit,
        min_node_count: Optional[int] | Omit = omit,
        node_count: Optional[int] | Omit = omit,
        taints: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterPool:
        """
        Update k8s cluster pool

        Args:
          auto_healing_enabled: Enable/disable auto healing

          labels: Labels applied to the cluster pool

          max_node_count: Maximum node count

          min_node_count: Minimum node count

          node_count: This field is deprecated. Please use the cluster pool resize handler instead.

          taints: Taints applied to the cluster pool

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        if not pool_name:
            raise ValueError(f"Expected a non-empty value for `pool_name` but received {pool_name!r}")
        return await self._patch(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}",
            body=await async_maybe_transform(
                {
                    "auto_healing_enabled": auto_healing_enabled,
                    "labels": labels,
                    "max_node_count": max_node_count,
                    "min_node_count": min_node_count,
                    "node_count": node_count,
                    "taints": taints,
                },
                pool_update_params.PoolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterPool,
        )

    async def list(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterPoolList:
        """
        List k8s cluster pools

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
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        return await self._get(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterPoolList,
        )

    async def delete(
        self,
        pool_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete k8s cluster pool

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
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        if not pool_name:
            raise ValueError(f"Expected a non-empty value for `pool_name` but received {pool_name!r}")
        return await self._delete(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def check_quota(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor_id: str,
        boot_volume_size: Optional[int] | Omit = omit,
        max_node_count: Optional[int] | Omit = omit,
        min_node_count: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        node_count: Optional[int] | Omit = omit,
        servergroup_policy: Optional[Literal["affinity", "anti-affinity", "soft-anti-affinity"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterPoolQuota:
        """Calculate quota requirements for a new cluster pool before creation.

        Returns
        exceeded quotas if regional limits would be violated. Use before pool creation
        to validate resource availability. Checks: CPU, RAM, volumes, VMs, GPUs, and
        baremetal quotas depending on flavor type.

        Args:
          project_id: Project ID

          region_id: Region ID

          flavor_id: Flavor ID

          boot_volume_size: Boot volume size

          max_node_count: Maximum node count

          min_node_count: Minimum node count

          name: Name of the cluster pool

          node_count: Maximum node count

          servergroup_policy: Server group policy: anti-affinity, soft-anti-affinity or affinity

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/pools/check_limits",
            body=await async_maybe_transform(
                {
                    "flavor_id": flavor_id,
                    "boot_volume_size": boot_volume_size,
                    "max_node_count": max_node_count,
                    "min_node_count": min_node_count,
                    "name": name,
                    "node_count": node_count,
                    "servergroup_policy": servergroup_policy,
                },
                pool_check_quota_params.PoolCheckQuotaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterPoolQuota,
        )

    async def get(
        self,
        pool_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterPool:
        """
        Get k8s cluster pool

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
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        if not pool_name:
            raise ValueError(f"Expected a non-empty value for `pool_name` but received {pool_name!r}")
        return await self._get(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterPool,
        )

    async def resize(
        self,
        pool_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        node_count: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Resize k8s cluster pool

        Args:
          node_count: Target node count

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        if not pool_name:
            raise ValueError(f"Expected a non-empty value for `pool_name` but received {pool_name!r}")
        return await self._post(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}/resize",
            body=await async_maybe_transform({"node_count": node_count}, pool_resize_params.PoolResizeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class PoolsResourceWithRawResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

        self.create = to_raw_response_wrapper(
            pools.create,
        )
        self.update = to_raw_response_wrapper(
            pools.update,
        )
        self.list = to_raw_response_wrapper(
            pools.list,
        )
        self.delete = to_raw_response_wrapper(
            pools.delete,
        )
        self.check_quota = to_raw_response_wrapper(
            pools.check_quota,
        )
        self.get = to_raw_response_wrapper(
            pools.get,
        )
        self.resize = to_raw_response_wrapper(
            pools.resize,
        )

    @cached_property
    def nodes(self) -> NodesResourceWithRawResponse:
        return NodesResourceWithRawResponse(self._pools.nodes)


class AsyncPoolsResourceWithRawResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

        self.create = async_to_raw_response_wrapper(
            pools.create,
        )
        self.update = async_to_raw_response_wrapper(
            pools.update,
        )
        self.list = async_to_raw_response_wrapper(
            pools.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pools.delete,
        )
        self.check_quota = async_to_raw_response_wrapper(
            pools.check_quota,
        )
        self.get = async_to_raw_response_wrapper(
            pools.get,
        )
        self.resize = async_to_raw_response_wrapper(
            pools.resize,
        )

    @cached_property
    def nodes(self) -> AsyncNodesResourceWithRawResponse:
        return AsyncNodesResourceWithRawResponse(self._pools.nodes)


class PoolsResourceWithStreamingResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

        self.create = to_streamed_response_wrapper(
            pools.create,
        )
        self.update = to_streamed_response_wrapper(
            pools.update,
        )
        self.list = to_streamed_response_wrapper(
            pools.list,
        )
        self.delete = to_streamed_response_wrapper(
            pools.delete,
        )
        self.check_quota = to_streamed_response_wrapper(
            pools.check_quota,
        )
        self.get = to_streamed_response_wrapper(
            pools.get,
        )
        self.resize = to_streamed_response_wrapper(
            pools.resize,
        )

    @cached_property
    def nodes(self) -> NodesResourceWithStreamingResponse:
        return NodesResourceWithStreamingResponse(self._pools.nodes)


class AsyncPoolsResourceWithStreamingResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

        self.create = async_to_streamed_response_wrapper(
            pools.create,
        )
        self.update = async_to_streamed_response_wrapper(
            pools.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pools.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pools.delete,
        )
        self.check_quota = async_to_streamed_response_wrapper(
            pools.check_quota,
        )
        self.get = async_to_streamed_response_wrapper(
            pools.get,
        )
        self.resize = async_to_streamed_response_wrapper(
            pools.resize,
        )

    @cached_property
    def nodes(self) -> AsyncNodesResourceWithStreamingResponse:
        return AsyncNodesResourceWithStreamingResponse(self._pools.nodes)

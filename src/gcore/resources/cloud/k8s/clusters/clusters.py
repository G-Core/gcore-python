# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from .nodes import (
    NodesResource,
    AsyncNodesResource,
    NodesResourceWithRawResponse,
    AsyncNodesResourceWithRawResponse,
    NodesResourceWithStreamingResponse,
    AsyncNodesResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from .pools.pools import (
    PoolsResource,
    AsyncPoolsResource,
    PoolsResourceWithRawResponse,
    AsyncPoolsResourceWithRawResponse,
    PoolsResourceWithStreamingResponse,
    AsyncPoolsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloud.k8s import (
    cluster_create_params,
    cluster_delete_params,
    cluster_update_params,
    cluster_upgrade_params,
)
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.k8s.k8s_cluster import K8SCluster
from .....types.cloud.k8s.k8s_cluster_list import K8SClusterList
from .....types.cloud.k8s_cluster_version_list import K8SClusterVersionList
from .....types.cloud.k8s.k8s_cluster_kubeconfig import K8SClusterKubeconfig
from .....types.cloud.k8s.k8s_cluster_certificate import K8SClusterCertificate

__all__ = ["ClustersResource", "AsyncClustersResource"]


class ClustersResource(SyncAPIResource):
    @cached_property
    def nodes(self) -> NodesResource:
        return NodesResource(self._client)

    @cached_property
    def pools(self) -> PoolsResource:
        return PoolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ClustersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        keypair: str,
        name: str,
        pools: Iterable[cluster_create_params.Pool],
        version: str,
        add_ons: cluster_create_params.AddOns | Omit = omit,
        authentication: Optional[cluster_create_params.Authentication] | Omit = omit,
        autoscaler_config: Optional[Dict[str, str]] | Omit = omit,
        cni: Optional[cluster_create_params.Cni] | Omit = omit,
        csi: cluster_create_params.Csi | Omit = omit,
        ddos_profile: Optional[cluster_create_params.DDOSProfile] | Omit = omit,
        fixed_network: Optional[str] | Omit = omit,
        fixed_subnet: Optional[str] | Omit = omit,
        is_ipv6: Optional[bool] | Omit = omit,
        logging: Optional[cluster_create_params.Logging] | Omit = omit,
        pods_ip_pool: Optional[str] | Omit = omit,
        pods_ipv6_pool: Optional[str] | Omit = omit,
        services_ip_pool: Optional[str] | Omit = omit,
        services_ipv6_pool: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create k8s cluster

        Args:
          keypair: The keypair of the cluster

          name: The name of the cluster

          pools: The pools of the cluster

          version: The version of the k8s cluster

          add_ons: Cluster add-ons configuration

          authentication: Authentication settings

          autoscaler_config: Cluster autoscaler configuration.

              It allows you to override the default cluster-autoscaler parameters provided by
              the platform with your preferred values.

              Supported parameters (in alphabetical order):

              - balance-similar-node-groups (boolean: true/false) - Detect similar node groups
                and balance the number of nodes between them.
              - expander (string: random, most-pods, least-waste, price, priority, grpc) -
                Type of node group expander to be used in scale up. Specifying multiple values
                separated by commas will call the expanders in succession until there is only
                one option remaining.
              - expendable-pods-priority-cutoff (float) - Pods with priority below cutoff will
                be expendable. They can be killed without any consideration during scale down
                and they don't cause scale up. Pods with null priority (PodPriority disabled)
                are non expendable.
              - ignore-daemonsets-utilization (boolean: true/false) - Should CA ignore
                DaemonSet pods when calculating resource utilization for scaling down.
              - max-empty-bulk-delete (integer) - Maximum number of empty nodes that can be
                deleted at the same time.
              - max-graceful-termination-sec (integer) - Maximum number of seconds CA waits
                for pod termination when trying to scale down a node.
              - max-node-provision-time (duration: e.g., '15m') - The default maximum time CA
                waits for node to be provisioned - the value can be overridden per node group.
              - max-total-unready-percentage (float) - Maximum percentage of unready nodes in
                the cluster. After this is exceeded, CA halts operations.
              - new-pod-scale-up-delay (duration: e.g., '10s') - Pods less than this old will
                not be considered for scale-up. Can be increased for individual pods through
                annotation.
              - ok-total-unready-count (integer) - Number of allowed unready nodes,
                irrespective of max-total-unready-percentage.
              - scale-down-delay-after-add (duration: e.g., '10m') - How long after scale up
                that scale down evaluation resumes.
              - scale-down-delay-after-delete (duration: e.g., '10s') - How long after node
                deletion that scale down evaluation resumes.
              - scale-down-delay-after-failure (duration: e.g., '3m') - How long after scale
                down failure that scale down evaluation resumes.
              - scale-down-enabled (boolean: true/false) - Should CA scale down the cluster.
              - scale-down-unneeded-time (duration: e.g., '10m') - How long a node should be
                unneeded before it is eligible for scale down.
              - scale-down-unready-time (duration: e.g., '20m') - How long an unready node
                should be unneeded before it is eligible for scale down.
              - scale-down-utilization-threshold (float) - The maximum value between the sum
                of cpu requests and sum of memory requests of all pods running on the node
                divided by node's corresponding allocatable resource, below which a node can
                be considered for scale down.
              - scan-interval (duration: e.g., '10s') - How often cluster is reevaluated for
                scale up or down.
              - skip-nodes-with-custom-controller-pods (boolean: true/false) - If true cluster
                autoscaler will never delete nodes with pods owned by custom controllers.
              - skip-nodes-with-local-storage (boolean: true/false) - If true cluster
                autoscaler will never delete nodes with pods with local storage, e.g. EmptyDir
                or HostPath.
              - skip-nodes-with-system-pods (boolean: true/false) - If true cluster autoscaler
                will never delete nodes with pods from kube-system (except for DaemonSet or
                mirror pods).

          cni: Cluster CNI settings

          csi: Container Storage Interface (CSI) driver settings

          ddos_profile: Advanced DDoS Protection profile

          fixed_network: The network of the cluster

          fixed_subnet: The subnet of the cluster

          is_ipv6: Enable public v6 address

          logging: Logging configuration

          pods_ip_pool: The IP pool for the pods

          pods_ipv6_pool: The IPv6 pool for the pods

          services_ip_pool: The IP pool for the services

          services_ipv6_pool: The IPv6 pool for the services

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "keypair": keypair,
                    "name": name,
                    "pools": pools,
                    "version": version,
                    "add_ons": add_ons,
                    "authentication": authentication,
                    "autoscaler_config": autoscaler_config,
                    "cni": cni,
                    "csi": csi,
                    "ddos_profile": ddos_profile,
                    "fixed_network": fixed_network,
                    "fixed_subnet": fixed_subnet,
                    "is_ipv6": is_ipv6,
                    "logging": logging,
                    "pods_ip_pool": pods_ip_pool,
                    "pods_ipv6_pool": pods_ipv6_pool,
                    "services_ip_pool": services_ip_pool,
                    "services_ipv6_pool": services_ipv6_pool,
                },
                cluster_create_params.ClusterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        add_ons: cluster_update_params.AddOns | Omit = omit,
        authentication: Optional[cluster_update_params.Authentication] | Omit = omit,
        autoscaler_config: Optional[Dict[str, str]] | Omit = omit,
        cni: Optional[cluster_update_params.Cni] | Omit = omit,
        ddos_profile: Optional[cluster_update_params.DDOSProfile] | Omit = omit,
        logging: Optional[cluster_update_params.Logging] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Update k8s cluster

        Args:
          add_ons: Cluster add-ons configuration

          authentication: Authentication settings

          autoscaler_config: Cluster autoscaler configuration.

              It allows you to override the default cluster-autoscaler parameters provided by
              the platform with your preferred values.

              Supported parameters (in alphabetical order):

              - balance-similar-node-groups (boolean: true/false) - Detect similar node groups
                and balance the number of nodes between them.
              - expander (string: random, most-pods, least-waste, price, priority, grpc) -
                Type of node group expander to be used in scale up. Specifying multiple values
                separated by commas will call the expanders in succession until there is only
                one option remaining.
              - expendable-pods-priority-cutoff (float) - Pods with priority below cutoff will
                be expendable. They can be killed without any consideration during scale down
                and they don't cause scale up. Pods with null priority (PodPriority disabled)
                are non expendable.
              - ignore-daemonsets-utilization (boolean: true/false) - Should CA ignore
                DaemonSet pods when calculating resource utilization for scaling down.
              - max-empty-bulk-delete (integer) - Maximum number of empty nodes that can be
                deleted at the same time.
              - max-graceful-termination-sec (integer) - Maximum number of seconds CA waits
                for pod termination when trying to scale down a node.
              - max-node-provision-time (duration: e.g., '15m') - The default maximum time CA
                waits for node to be provisioned - the value can be overridden per node group.
              - max-total-unready-percentage (float) - Maximum percentage of unready nodes in
                the cluster. After this is exceeded, CA halts operations.
              - new-pod-scale-up-delay (duration: e.g., '10s') - Pods less than this old will
                not be considered for scale-up. Can be increased for individual pods through
                annotation.
              - ok-total-unready-count (integer) - Number of allowed unready nodes,
                irrespective of max-total-unready-percentage.
              - scale-down-delay-after-add (duration: e.g., '10m') - How long after scale up
                that scale down evaluation resumes.
              - scale-down-delay-after-delete (duration: e.g., '10s') - How long after node
                deletion that scale down evaluation resumes.
              - scale-down-delay-after-failure (duration: e.g., '3m') - How long after scale
                down failure that scale down evaluation resumes.
              - scale-down-enabled (boolean: true/false) - Should CA scale down the cluster.
              - scale-down-unneeded-time (duration: e.g., '10m') - How long a node should be
                unneeded before it is eligible for scale down.
              - scale-down-unready-time (duration: e.g., '20m') - How long an unready node
                should be unneeded before it is eligible for scale down.
              - scale-down-utilization-threshold (float) - The maximum value between the sum
                of cpu requests and sum of memory requests of all pods running on the node
                divided by node's corresponding allocatable resource, below which a node can
                be considered for scale down.
              - scan-interval (duration: e.g., '10s') - How often cluster is reevaluated for
                scale up or down.
              - skip-nodes-with-custom-controller-pods (boolean: true/false) - If true cluster
                autoscaler will never delete nodes with pods owned by custom controllers.
              - skip-nodes-with-local-storage (boolean: true/false) - If true cluster
                autoscaler will never delete nodes with pods with local storage, e.g. EmptyDir
                or HostPath.
              - skip-nodes-with-system-pods (boolean: true/false) - If true cluster autoscaler
                will never delete nodes with pods from kube-system (except for DaemonSet or
                mirror pods).

          cni: Cluster CNI settings

          ddos_profile: Advanced DDoS Protection profile

          logging: Logging configuration

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
        return self._patch(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}",
            body=maybe_transform(
                {
                    "add_ons": add_ons,
                    "authentication": authentication,
                    "autoscaler_config": autoscaler_config,
                    "cni": cni,
                    "ddos_profile": ddos_profile,
                    "logging": logging,
                },
                cluster_update_params.ClusterUpdateParams,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterList:
        """
        List k8s clusters

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
        return self._get(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterList,
        )

    def delete(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        volumes: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete k8s cluster

        Args:
          volumes: Comma separated list of volume IDs to be deleted with the cluster

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
        return self._delete(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"volumes": volumes}, cluster_delete_params.ClusterDeleteParams),
            ),
            cast_to=TaskIDList,
        )

    def get(
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
    ) -> K8SCluster:
        """
        Get k8s cluster

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SCluster,
        )

    def get_certificate(
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
    ) -> K8SClusterCertificate:
        """
        Get k8s cluster CA certificate

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/certificates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterCertificate,
        )

    def get_kubeconfig(
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
    ) -> K8SClusterKubeconfig:
        """
        Get k8s cluster kubeconfig

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterKubeconfig,
        )

    def list_versions_for_upgrade(
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
    ) -> K8SClusterVersionList:
        """
        List available k8s cluster versions for upgrade

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/upgrade_versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterVersionList,
        )

    def upgrade(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Upgrade k8s cluster

        Args:
          version: Target k8s cluster version

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/upgrade",
            body=maybe_transform({"version": version}, cluster_upgrade_params.ClusterUpgradeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class AsyncClustersResource(AsyncAPIResource):
    @cached_property
    def nodes(self) -> AsyncNodesResource:
        return AsyncNodesResource(self._client)

    @cached_property
    def pools(self) -> AsyncPoolsResource:
        return AsyncPoolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncClustersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        keypair: str,
        name: str,
        pools: Iterable[cluster_create_params.Pool],
        version: str,
        add_ons: cluster_create_params.AddOns | Omit = omit,
        authentication: Optional[cluster_create_params.Authentication] | Omit = omit,
        autoscaler_config: Optional[Dict[str, str]] | Omit = omit,
        cni: Optional[cluster_create_params.Cni] | Omit = omit,
        csi: cluster_create_params.Csi | Omit = omit,
        ddos_profile: Optional[cluster_create_params.DDOSProfile] | Omit = omit,
        fixed_network: Optional[str] | Omit = omit,
        fixed_subnet: Optional[str] | Omit = omit,
        is_ipv6: Optional[bool] | Omit = omit,
        logging: Optional[cluster_create_params.Logging] | Omit = omit,
        pods_ip_pool: Optional[str] | Omit = omit,
        pods_ipv6_pool: Optional[str] | Omit = omit,
        services_ip_pool: Optional[str] | Omit = omit,
        services_ipv6_pool: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create k8s cluster

        Args:
          keypair: The keypair of the cluster

          name: The name of the cluster

          pools: The pools of the cluster

          version: The version of the k8s cluster

          add_ons: Cluster add-ons configuration

          authentication: Authentication settings

          autoscaler_config: Cluster autoscaler configuration.

              It allows you to override the default cluster-autoscaler parameters provided by
              the platform with your preferred values.

              Supported parameters (in alphabetical order):

              - balance-similar-node-groups (boolean: true/false) - Detect similar node groups
                and balance the number of nodes between them.
              - expander (string: random, most-pods, least-waste, price, priority, grpc) -
                Type of node group expander to be used in scale up. Specifying multiple values
                separated by commas will call the expanders in succession until there is only
                one option remaining.
              - expendable-pods-priority-cutoff (float) - Pods with priority below cutoff will
                be expendable. They can be killed without any consideration during scale down
                and they don't cause scale up. Pods with null priority (PodPriority disabled)
                are non expendable.
              - ignore-daemonsets-utilization (boolean: true/false) - Should CA ignore
                DaemonSet pods when calculating resource utilization for scaling down.
              - max-empty-bulk-delete (integer) - Maximum number of empty nodes that can be
                deleted at the same time.
              - max-graceful-termination-sec (integer) - Maximum number of seconds CA waits
                for pod termination when trying to scale down a node.
              - max-node-provision-time (duration: e.g., '15m') - The default maximum time CA
                waits for node to be provisioned - the value can be overridden per node group.
              - max-total-unready-percentage (float) - Maximum percentage of unready nodes in
                the cluster. After this is exceeded, CA halts operations.
              - new-pod-scale-up-delay (duration: e.g., '10s') - Pods less than this old will
                not be considered for scale-up. Can be increased for individual pods through
                annotation.
              - ok-total-unready-count (integer) - Number of allowed unready nodes,
                irrespective of max-total-unready-percentage.
              - scale-down-delay-after-add (duration: e.g., '10m') - How long after scale up
                that scale down evaluation resumes.
              - scale-down-delay-after-delete (duration: e.g., '10s') - How long after node
                deletion that scale down evaluation resumes.
              - scale-down-delay-after-failure (duration: e.g., '3m') - How long after scale
                down failure that scale down evaluation resumes.
              - scale-down-enabled (boolean: true/false) - Should CA scale down the cluster.
              - scale-down-unneeded-time (duration: e.g., '10m') - How long a node should be
                unneeded before it is eligible for scale down.
              - scale-down-unready-time (duration: e.g., '20m') - How long an unready node
                should be unneeded before it is eligible for scale down.
              - scale-down-utilization-threshold (float) - The maximum value between the sum
                of cpu requests and sum of memory requests of all pods running on the node
                divided by node's corresponding allocatable resource, below which a node can
                be considered for scale down.
              - scan-interval (duration: e.g., '10s') - How often cluster is reevaluated for
                scale up or down.
              - skip-nodes-with-custom-controller-pods (boolean: true/false) - If true cluster
                autoscaler will never delete nodes with pods owned by custom controllers.
              - skip-nodes-with-local-storage (boolean: true/false) - If true cluster
                autoscaler will never delete nodes with pods with local storage, e.g. EmptyDir
                or HostPath.
              - skip-nodes-with-system-pods (boolean: true/false) - If true cluster autoscaler
                will never delete nodes with pods from kube-system (except for DaemonSet or
                mirror pods).

          cni: Cluster CNI settings

          csi: Container Storage Interface (CSI) driver settings

          ddos_profile: Advanced DDoS Protection profile

          fixed_network: The network of the cluster

          fixed_subnet: The subnet of the cluster

          is_ipv6: Enable public v6 address

          logging: Logging configuration

          pods_ip_pool: The IP pool for the pods

          pods_ipv6_pool: The IPv6 pool for the pods

          services_ip_pool: The IP pool for the services

          services_ipv6_pool: The IPv6 pool for the services

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "keypair": keypair,
                    "name": name,
                    "pools": pools,
                    "version": version,
                    "add_ons": add_ons,
                    "authentication": authentication,
                    "autoscaler_config": autoscaler_config,
                    "cni": cni,
                    "csi": csi,
                    "ddos_profile": ddos_profile,
                    "fixed_network": fixed_network,
                    "fixed_subnet": fixed_subnet,
                    "is_ipv6": is_ipv6,
                    "logging": logging,
                    "pods_ip_pool": pods_ip_pool,
                    "pods_ipv6_pool": pods_ipv6_pool,
                    "services_ip_pool": services_ip_pool,
                    "services_ipv6_pool": services_ipv6_pool,
                },
                cluster_create_params.ClusterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        add_ons: cluster_update_params.AddOns | Omit = omit,
        authentication: Optional[cluster_update_params.Authentication] | Omit = omit,
        autoscaler_config: Optional[Dict[str, str]] | Omit = omit,
        cni: Optional[cluster_update_params.Cni] | Omit = omit,
        ddos_profile: Optional[cluster_update_params.DDOSProfile] | Omit = omit,
        logging: Optional[cluster_update_params.Logging] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Update k8s cluster

        Args:
          add_ons: Cluster add-ons configuration

          authentication: Authentication settings

          autoscaler_config: Cluster autoscaler configuration.

              It allows you to override the default cluster-autoscaler parameters provided by
              the platform with your preferred values.

              Supported parameters (in alphabetical order):

              - balance-similar-node-groups (boolean: true/false) - Detect similar node groups
                and balance the number of nodes between them.
              - expander (string: random, most-pods, least-waste, price, priority, grpc) -
                Type of node group expander to be used in scale up. Specifying multiple values
                separated by commas will call the expanders in succession until there is only
                one option remaining.
              - expendable-pods-priority-cutoff (float) - Pods with priority below cutoff will
                be expendable. They can be killed without any consideration during scale down
                and they don't cause scale up. Pods with null priority (PodPriority disabled)
                are non expendable.
              - ignore-daemonsets-utilization (boolean: true/false) - Should CA ignore
                DaemonSet pods when calculating resource utilization for scaling down.
              - max-empty-bulk-delete (integer) - Maximum number of empty nodes that can be
                deleted at the same time.
              - max-graceful-termination-sec (integer) - Maximum number of seconds CA waits
                for pod termination when trying to scale down a node.
              - max-node-provision-time (duration: e.g., '15m') - The default maximum time CA
                waits for node to be provisioned - the value can be overridden per node group.
              - max-total-unready-percentage (float) - Maximum percentage of unready nodes in
                the cluster. After this is exceeded, CA halts operations.
              - new-pod-scale-up-delay (duration: e.g., '10s') - Pods less than this old will
                not be considered for scale-up. Can be increased for individual pods through
                annotation.
              - ok-total-unready-count (integer) - Number of allowed unready nodes,
                irrespective of max-total-unready-percentage.
              - scale-down-delay-after-add (duration: e.g., '10m') - How long after scale up
                that scale down evaluation resumes.
              - scale-down-delay-after-delete (duration: e.g., '10s') - How long after node
                deletion that scale down evaluation resumes.
              - scale-down-delay-after-failure (duration: e.g., '3m') - How long after scale
                down failure that scale down evaluation resumes.
              - scale-down-enabled (boolean: true/false) - Should CA scale down the cluster.
              - scale-down-unneeded-time (duration: e.g., '10m') - How long a node should be
                unneeded before it is eligible for scale down.
              - scale-down-unready-time (duration: e.g., '20m') - How long an unready node
                should be unneeded before it is eligible for scale down.
              - scale-down-utilization-threshold (float) - The maximum value between the sum
                of cpu requests and sum of memory requests of all pods running on the node
                divided by node's corresponding allocatable resource, below which a node can
                be considered for scale down.
              - scan-interval (duration: e.g., '10s') - How often cluster is reevaluated for
                scale up or down.
              - skip-nodes-with-custom-controller-pods (boolean: true/false) - If true cluster
                autoscaler will never delete nodes with pods owned by custom controllers.
              - skip-nodes-with-local-storage (boolean: true/false) - If true cluster
                autoscaler will never delete nodes with pods with local storage, e.g. EmptyDir
                or HostPath.
              - skip-nodes-with-system-pods (boolean: true/false) - If true cluster autoscaler
                will never delete nodes with pods from kube-system (except for DaemonSet or
                mirror pods).

          cni: Cluster CNI settings

          ddos_profile: Advanced DDoS Protection profile

          logging: Logging configuration

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
        return await self._patch(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}",
            body=await async_maybe_transform(
                {
                    "add_ons": add_ons,
                    "authentication": authentication,
                    "autoscaler_config": autoscaler_config,
                    "cni": cni,
                    "ddos_profile": ddos_profile,
                    "logging": logging,
                },
                cluster_update_params.ClusterUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterList:
        """
        List k8s clusters

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
        return await self._get(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterList,
        )

    async def delete(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        volumes: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete k8s cluster

        Args:
          volumes: Comma separated list of volume IDs to be deleted with the cluster

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
        return await self._delete(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"volumes": volumes}, cluster_delete_params.ClusterDeleteParams),
            ),
            cast_to=TaskIDList,
        )

    async def get(
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
    ) -> K8SCluster:
        """
        Get k8s cluster

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SCluster,
        )

    async def get_certificate(
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
    ) -> K8SClusterCertificate:
        """
        Get k8s cluster CA certificate

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/certificates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterCertificate,
        )

    async def get_kubeconfig(
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
    ) -> K8SClusterKubeconfig:
        """
        Get k8s cluster kubeconfig

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterKubeconfig,
        )

    async def list_versions_for_upgrade(
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
    ) -> K8SClusterVersionList:
        """
        List available k8s cluster versions for upgrade

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/upgrade_versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterVersionList,
        )

    async def upgrade(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Upgrade k8s cluster

        Args:
          version: Target k8s cluster version

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
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/upgrade",
            body=await async_maybe_transform({"version": version}, cluster_upgrade_params.ClusterUpgradeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class ClustersResourceWithRawResponse:
    def __init__(self, clusters: ClustersResource) -> None:
        self._clusters = clusters

        self.create = to_raw_response_wrapper(
            clusters.create,
        )
        self.update = to_raw_response_wrapper(
            clusters.update,
        )
        self.list = to_raw_response_wrapper(
            clusters.list,
        )
        self.delete = to_raw_response_wrapper(
            clusters.delete,
        )
        self.get = to_raw_response_wrapper(
            clusters.get,
        )
        self.get_certificate = to_raw_response_wrapper(
            clusters.get_certificate,
        )
        self.get_kubeconfig = to_raw_response_wrapper(
            clusters.get_kubeconfig,
        )
        self.list_versions_for_upgrade = to_raw_response_wrapper(
            clusters.list_versions_for_upgrade,
        )
        self.upgrade = to_raw_response_wrapper(
            clusters.upgrade,
        )

    @cached_property
    def nodes(self) -> NodesResourceWithRawResponse:
        return NodesResourceWithRawResponse(self._clusters.nodes)

    @cached_property
    def pools(self) -> PoolsResourceWithRawResponse:
        return PoolsResourceWithRawResponse(self._clusters.pools)


class AsyncClustersResourceWithRawResponse:
    def __init__(self, clusters: AsyncClustersResource) -> None:
        self._clusters = clusters

        self.create = async_to_raw_response_wrapper(
            clusters.create,
        )
        self.update = async_to_raw_response_wrapper(
            clusters.update,
        )
        self.list = async_to_raw_response_wrapper(
            clusters.list,
        )
        self.delete = async_to_raw_response_wrapper(
            clusters.delete,
        )
        self.get = async_to_raw_response_wrapper(
            clusters.get,
        )
        self.get_certificate = async_to_raw_response_wrapper(
            clusters.get_certificate,
        )
        self.get_kubeconfig = async_to_raw_response_wrapper(
            clusters.get_kubeconfig,
        )
        self.list_versions_for_upgrade = async_to_raw_response_wrapper(
            clusters.list_versions_for_upgrade,
        )
        self.upgrade = async_to_raw_response_wrapper(
            clusters.upgrade,
        )

    @cached_property
    def nodes(self) -> AsyncNodesResourceWithRawResponse:
        return AsyncNodesResourceWithRawResponse(self._clusters.nodes)

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithRawResponse:
        return AsyncPoolsResourceWithRawResponse(self._clusters.pools)


class ClustersResourceWithStreamingResponse:
    def __init__(self, clusters: ClustersResource) -> None:
        self._clusters = clusters

        self.create = to_streamed_response_wrapper(
            clusters.create,
        )
        self.update = to_streamed_response_wrapper(
            clusters.update,
        )
        self.list = to_streamed_response_wrapper(
            clusters.list,
        )
        self.delete = to_streamed_response_wrapper(
            clusters.delete,
        )
        self.get = to_streamed_response_wrapper(
            clusters.get,
        )
        self.get_certificate = to_streamed_response_wrapper(
            clusters.get_certificate,
        )
        self.get_kubeconfig = to_streamed_response_wrapper(
            clusters.get_kubeconfig,
        )
        self.list_versions_for_upgrade = to_streamed_response_wrapper(
            clusters.list_versions_for_upgrade,
        )
        self.upgrade = to_streamed_response_wrapper(
            clusters.upgrade,
        )

    @cached_property
    def nodes(self) -> NodesResourceWithStreamingResponse:
        return NodesResourceWithStreamingResponse(self._clusters.nodes)

    @cached_property
    def pools(self) -> PoolsResourceWithStreamingResponse:
        return PoolsResourceWithStreamingResponse(self._clusters.pools)


class AsyncClustersResourceWithStreamingResponse:
    def __init__(self, clusters: AsyncClustersResource) -> None:
        self._clusters = clusters

        self.create = async_to_streamed_response_wrapper(
            clusters.create,
        )
        self.update = async_to_streamed_response_wrapper(
            clusters.update,
        )
        self.list = async_to_streamed_response_wrapper(
            clusters.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            clusters.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            clusters.get,
        )
        self.get_certificate = async_to_streamed_response_wrapper(
            clusters.get_certificate,
        )
        self.get_kubeconfig = async_to_streamed_response_wrapper(
            clusters.get_kubeconfig,
        )
        self.list_versions_for_upgrade = async_to_streamed_response_wrapper(
            clusters.list_versions_for_upgrade,
        )
        self.upgrade = async_to_streamed_response_wrapper(
            clusters.upgrade,
        )

    @cached_property
    def nodes(self) -> AsyncNodesResourceWithStreamingResponse:
        return AsyncNodesResourceWithStreamingResponse(self._clusters.nodes)

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithStreamingResponse:
        return AsyncPoolsResourceWithStreamingResponse(self._clusters.pools)

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
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
from .flavors import (
    FlavorsResource,
    AsyncFlavorsResource,
    FlavorsResourceWithRawResponse,
    AsyncFlavorsResourceWithRawResponse,
    FlavorsResourceWithStreamingResponse,
    AsyncFlavorsResourceWithStreamingResponse,
)
from .servers import (
    ServersResource,
    AsyncServersResource,
    ServersResourceWithRawResponse,
    AsyncServersResourceWithRawResponse,
    ServersResourceWithStreamingResponse,
    AsyncServersResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
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
    gpu_baremetal_cluster_list_params,
    gpu_baremetal_cluster_create_params,
    gpu_baremetal_cluster_delete_params,
    gpu_baremetal_cluster_resize_params,
    gpu_baremetal_cluster_rebuild_params,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.gpu_baremetal_cluster import GPUBaremetalCluster
from ....types.cloud.gpu_baremetal_clusters.gpu_baremetal_cluster_server_v1_list import GPUBaremetalClusterServerV1List

__all__ = ["GPUBaremetalClustersResource", "AsyncGPUBaremetalClustersResource"]


class GPUBaremetalClustersResource(SyncAPIResource):
    @cached_property
    def interfaces(self) -> InterfacesResource:
        return InterfacesResource(self._client)

    @cached_property
    def servers(self) -> ServersResource:
        return ServersResource(self._client)

    @cached_property
    def flavors(self) -> FlavorsResource:
        return FlavorsResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> GPUBaremetalClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return GPUBaremetalClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GPUBaremetalClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return GPUBaremetalClustersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        image_id: str,
        name: str,
        servers_count: int,
        servers_settings: gpu_baremetal_cluster_create_params.ServersSettings,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new bare metal GPU cluster with the specified configuration.

        Args:
          project_id: Project ID

          region_id: Region ID

          flavor: Cluster flavor ID

          image_id: System image ID

          name: Cluster name

          servers_count: Number of servers in the cluster

          servers_settings: Configuration settings for the servers in the cluster

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters",
            body=maybe_transform(
                {
                    "flavor": flavor,
                    "image_id": image_id,
                    "name": name,
                    "servers_count": servers_count,
                    "servers_settings": servers_settings,
                    "tags": tags,
                },
                gpu_baremetal_cluster_create_params.GPUBaremetalClusterCreateParams,
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
        limit: int | Omit = omit,
        managed_by: List[Literal["k8s", "user"]] | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[GPUBaremetalCluster]:
        """
        List all bare metal GPU clusters in the specified project and region.

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Limit of items on a single page

          managed_by: Specifies the entity responsible for managing the resource.

              - `user`: The resource (cluster) is created and maintained directly by the user.
              - `k8s`: The resource is created and maintained automatically by Managed
                Kubernetes service

          offset: Offset in results list

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters",
            page=SyncOffsetPage[GPUBaremetalCluster],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "managed_by": managed_by,
                        "offset": offset,
                    },
                    gpu_baremetal_cluster_list_params.GPUBaremetalClusterListParams,
                ),
            ),
            model=GPUBaremetalCluster,
        )

    def delete(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        all_floating_ips: bool | Omit = omit,
        all_reserved_fixed_ips: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        reserved_fixed_ip_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete a bare metal GPU cluster and all its associated resources.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          all_floating_ips: Flag indicating whether the floating ips associated with server / cluster are
              deleted

          all_reserved_fixed_ips: Flag indicating whether the reserved fixed ips associated with server / cluster
              are deleted

          floating_ip_ids: Optional list of floating ips to be deleted

          reserved_fixed_ip_ids: Optional list of reserved fixed ips to be deleted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return self._delete(
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters/{cluster_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "all_floating_ips": all_floating_ips,
                        "all_reserved_fixed_ips": all_reserved_fixed_ips,
                        "floating_ip_ids": floating_ip_ids,
                        "reserved_fixed_ip_ids": reserved_fixed_ip_ids,
                    },
                    gpu_baremetal_cluster_delete_params.GPUBaremetalClusterDeleteParams,
                ),
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalCluster:
        """
        Get detailed information about a specific bare metal GPU cluster.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return self._get(
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters/{cluster_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalCluster,
        )

    def powercycle_all_servers(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalClusterServerV1List:
        """
        Stops and then starts all cluster servers, effectively performing a hard reboot.

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
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return self._post(
            f"/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/powercycle",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalClusterServerV1List,
        )

    def reboot_all_servers(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalClusterServerV1List:
        """
        Reboot all bare metal GPU cluster servers

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
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return self._post(
            f"/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/reboot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalClusterServerV1List,
        )

    def rebuild(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        nodes: SequenceNotStr[str],
        image_id: Optional[str] | Omit = omit,
        user_data: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Rebuild one or more nodes in a GPU cluster.

        All cluster nodes must be specified
        to update the cluster image.

        Args:
          nodes: List of nodes uuids to be rebuild

          image_id: AI GPU image ID

          user_data:
              String in base64 format.Examples of the `user_data`:
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
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return self._post(
            f"/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/rebuild",
            body=maybe_transform(
                {
                    "nodes": nodes,
                    "image_id": image_id,
                    "user_data": user_data,
                },
                gpu_baremetal_cluster_rebuild_params.GPUBaremetalClusterRebuildParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def resize(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        instances_count: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Change the number of nodes in a GPU cluster.

        The cluster can be scaled up or
        down.

        Args:
          instances_count: Resized (total) number of instances

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return self._post(
            f"/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/resize",
            body=maybe_transform(
                {"instances_count": instances_count},
                gpu_baremetal_cluster_resize_params.GPUBaremetalClusterResizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class AsyncGPUBaremetalClustersResource(AsyncAPIResource):
    @cached_property
    def interfaces(self) -> AsyncInterfacesResource:
        return AsyncInterfacesResource(self._client)

    @cached_property
    def servers(self) -> AsyncServersResource:
        return AsyncServersResource(self._client)

    @cached_property
    def flavors(self) -> AsyncFlavorsResource:
        return AsyncFlavorsResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGPUBaremetalClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGPUBaremetalClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGPUBaremetalClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncGPUBaremetalClustersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        image_id: str,
        name: str,
        servers_count: int,
        servers_settings: gpu_baremetal_cluster_create_params.ServersSettings,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new bare metal GPU cluster with the specified configuration.

        Args:
          project_id: Project ID

          region_id: Region ID

          flavor: Cluster flavor ID

          image_id: System image ID

          name: Cluster name

          servers_count: Number of servers in the cluster

          servers_settings: Configuration settings for the servers in the cluster

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters",
            body=await async_maybe_transform(
                {
                    "flavor": flavor,
                    "image_id": image_id,
                    "name": name,
                    "servers_count": servers_count,
                    "servers_settings": servers_settings,
                    "tags": tags,
                },
                gpu_baremetal_cluster_create_params.GPUBaremetalClusterCreateParams,
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
        limit: int | Omit = omit,
        managed_by: List[Literal["k8s", "user"]] | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[GPUBaremetalCluster, AsyncOffsetPage[GPUBaremetalCluster]]:
        """
        List all bare metal GPU clusters in the specified project and region.

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Limit of items on a single page

          managed_by: Specifies the entity responsible for managing the resource.

              - `user`: The resource (cluster) is created and maintained directly by the user.
              - `k8s`: The resource is created and maintained automatically by Managed
                Kubernetes service

          offset: Offset in results list

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters",
            page=AsyncOffsetPage[GPUBaremetalCluster],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "managed_by": managed_by,
                        "offset": offset,
                    },
                    gpu_baremetal_cluster_list_params.GPUBaremetalClusterListParams,
                ),
            ),
            model=GPUBaremetalCluster,
        )

    async def delete(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        all_floating_ips: bool | Omit = omit,
        all_reserved_fixed_ips: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        reserved_fixed_ip_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete a bare metal GPU cluster and all its associated resources.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          all_floating_ips: Flag indicating whether the floating ips associated with server / cluster are
              deleted

          all_reserved_fixed_ips: Flag indicating whether the reserved fixed ips associated with server / cluster
              are deleted

          floating_ip_ids: Optional list of floating ips to be deleted

          reserved_fixed_ip_ids: Optional list of reserved fixed ips to be deleted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return await self._delete(
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters/{cluster_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "all_floating_ips": all_floating_ips,
                        "all_reserved_fixed_ips": all_reserved_fixed_ips,
                        "floating_ip_ids": floating_ip_ids,
                        "reserved_fixed_ip_ids": reserved_fixed_ip_ids,
                    },
                    gpu_baremetal_cluster_delete_params.GPUBaremetalClusterDeleteParams,
                ),
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalCluster:
        """
        Get detailed information about a specific bare metal GPU cluster.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return await self._get(
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters/{cluster_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalCluster,
        )

    async def powercycle_all_servers(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalClusterServerV1List:
        """
        Stops and then starts all cluster servers, effectively performing a hard reboot.

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
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return await self._post(
            f"/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/powercycle",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalClusterServerV1List,
        )

    async def reboot_all_servers(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalClusterServerV1List:
        """
        Reboot all bare metal GPU cluster servers

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
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return await self._post(
            f"/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/reboot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalClusterServerV1List,
        )

    async def rebuild(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        nodes: SequenceNotStr[str],
        image_id: Optional[str] | Omit = omit,
        user_data: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Rebuild one or more nodes in a GPU cluster.

        All cluster nodes must be specified
        to update the cluster image.

        Args:
          nodes: List of nodes uuids to be rebuild

          image_id: AI GPU image ID

          user_data:
              String in base64 format.Examples of the `user_data`:
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
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return await self._post(
            f"/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/rebuild",
            body=await async_maybe_transform(
                {
                    "nodes": nodes,
                    "image_id": image_id,
                    "user_data": user_data,
                },
                gpu_baremetal_cluster_rebuild_params.GPUBaremetalClusterRebuildParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def resize(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        instances_count: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Change the number of nodes in a GPU cluster.

        The cluster can be scaled up or
        down.

        Args:
          instances_count: Resized (total) number of instances

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return await self._post(
            f"/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/resize",
            body=await async_maybe_transform(
                {"instances_count": instances_count},
                gpu_baremetal_cluster_resize_params.GPUBaremetalClusterResizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class GPUBaremetalClustersResourceWithRawResponse:
    def __init__(self, gpu_baremetal_clusters: GPUBaremetalClustersResource) -> None:
        self._gpu_baremetal_clusters = gpu_baremetal_clusters

        self.create = to_raw_response_wrapper(
            gpu_baremetal_clusters.create,
        )
        self.list = to_raw_response_wrapper(
            gpu_baremetal_clusters.list,
        )
        self.delete = to_raw_response_wrapper(
            gpu_baremetal_clusters.delete,
        )
        self.get = to_raw_response_wrapper(
            gpu_baremetal_clusters.get,
        )
        self.powercycle_all_servers = to_raw_response_wrapper(
            gpu_baremetal_clusters.powercycle_all_servers,
        )
        self.reboot_all_servers = to_raw_response_wrapper(
            gpu_baremetal_clusters.reboot_all_servers,
        )
        self.rebuild = to_raw_response_wrapper(
            gpu_baremetal_clusters.rebuild,
        )
        self.resize = to_raw_response_wrapper(
            gpu_baremetal_clusters.resize,
        )

    @cached_property
    def interfaces(self) -> InterfacesResourceWithRawResponse:
        return InterfacesResourceWithRawResponse(self._gpu_baremetal_clusters.interfaces)

    @cached_property
    def servers(self) -> ServersResourceWithRawResponse:
        return ServersResourceWithRawResponse(self._gpu_baremetal_clusters.servers)

    @cached_property
    def flavors(self) -> FlavorsResourceWithRawResponse:
        return FlavorsResourceWithRawResponse(self._gpu_baremetal_clusters.flavors)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._gpu_baremetal_clusters.images)


class AsyncGPUBaremetalClustersResourceWithRawResponse:
    def __init__(self, gpu_baremetal_clusters: AsyncGPUBaremetalClustersResource) -> None:
        self._gpu_baremetal_clusters = gpu_baremetal_clusters

        self.create = async_to_raw_response_wrapper(
            gpu_baremetal_clusters.create,
        )
        self.list = async_to_raw_response_wrapper(
            gpu_baremetal_clusters.list,
        )
        self.delete = async_to_raw_response_wrapper(
            gpu_baremetal_clusters.delete,
        )
        self.get = async_to_raw_response_wrapper(
            gpu_baremetal_clusters.get,
        )
        self.powercycle_all_servers = async_to_raw_response_wrapper(
            gpu_baremetal_clusters.powercycle_all_servers,
        )
        self.reboot_all_servers = async_to_raw_response_wrapper(
            gpu_baremetal_clusters.reboot_all_servers,
        )
        self.rebuild = async_to_raw_response_wrapper(
            gpu_baremetal_clusters.rebuild,
        )
        self.resize = async_to_raw_response_wrapper(
            gpu_baremetal_clusters.resize,
        )

    @cached_property
    def interfaces(self) -> AsyncInterfacesResourceWithRawResponse:
        return AsyncInterfacesResourceWithRawResponse(self._gpu_baremetal_clusters.interfaces)

    @cached_property
    def servers(self) -> AsyncServersResourceWithRawResponse:
        return AsyncServersResourceWithRawResponse(self._gpu_baremetal_clusters.servers)

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithRawResponse:
        return AsyncFlavorsResourceWithRawResponse(self._gpu_baremetal_clusters.flavors)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._gpu_baremetal_clusters.images)


class GPUBaremetalClustersResourceWithStreamingResponse:
    def __init__(self, gpu_baremetal_clusters: GPUBaremetalClustersResource) -> None:
        self._gpu_baremetal_clusters = gpu_baremetal_clusters

        self.create = to_streamed_response_wrapper(
            gpu_baremetal_clusters.create,
        )
        self.list = to_streamed_response_wrapper(
            gpu_baremetal_clusters.list,
        )
        self.delete = to_streamed_response_wrapper(
            gpu_baremetal_clusters.delete,
        )
        self.get = to_streamed_response_wrapper(
            gpu_baremetal_clusters.get,
        )
        self.powercycle_all_servers = to_streamed_response_wrapper(
            gpu_baremetal_clusters.powercycle_all_servers,
        )
        self.reboot_all_servers = to_streamed_response_wrapper(
            gpu_baremetal_clusters.reboot_all_servers,
        )
        self.rebuild = to_streamed_response_wrapper(
            gpu_baremetal_clusters.rebuild,
        )
        self.resize = to_streamed_response_wrapper(
            gpu_baremetal_clusters.resize,
        )

    @cached_property
    def interfaces(self) -> InterfacesResourceWithStreamingResponse:
        return InterfacesResourceWithStreamingResponse(self._gpu_baremetal_clusters.interfaces)

    @cached_property
    def servers(self) -> ServersResourceWithStreamingResponse:
        return ServersResourceWithStreamingResponse(self._gpu_baremetal_clusters.servers)

    @cached_property
    def flavors(self) -> FlavorsResourceWithStreamingResponse:
        return FlavorsResourceWithStreamingResponse(self._gpu_baremetal_clusters.flavors)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._gpu_baremetal_clusters.images)


class AsyncGPUBaremetalClustersResourceWithStreamingResponse:
    def __init__(self, gpu_baremetal_clusters: AsyncGPUBaremetalClustersResource) -> None:
        self._gpu_baremetal_clusters = gpu_baremetal_clusters

        self.create = async_to_streamed_response_wrapper(
            gpu_baremetal_clusters.create,
        )
        self.list = async_to_streamed_response_wrapper(
            gpu_baremetal_clusters.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            gpu_baremetal_clusters.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            gpu_baremetal_clusters.get,
        )
        self.powercycle_all_servers = async_to_streamed_response_wrapper(
            gpu_baremetal_clusters.powercycle_all_servers,
        )
        self.reboot_all_servers = async_to_streamed_response_wrapper(
            gpu_baremetal_clusters.reboot_all_servers,
        )
        self.rebuild = async_to_streamed_response_wrapper(
            gpu_baremetal_clusters.rebuild,
        )
        self.resize = async_to_streamed_response_wrapper(
            gpu_baremetal_clusters.resize,
        )

    @cached_property
    def interfaces(self) -> AsyncInterfacesResourceWithStreamingResponse:
        return AsyncInterfacesResourceWithStreamingResponse(self._gpu_baremetal_clusters.interfaces)

    @cached_property
    def servers(self) -> AsyncServersResourceWithStreamingResponse:
        return AsyncServersResourceWithStreamingResponse(self._gpu_baremetal_clusters.servers)

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithStreamingResponse:
        return AsyncFlavorsResourceWithStreamingResponse(self._gpu_baremetal_clusters.flavors)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._gpu_baremetal_clusters.images)

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

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
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.cloud.tag_update_list_param import TagUpdateListParam
from ....types.cloud.gpu_cluster_server_list import GPUClusterServerList

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

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return GPUBaremetalClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GPUBaremetalClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return GPUBaremetalClustersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        image_id: str,
        interfaces: Iterable[gpu_baremetal_cluster_create_params.Interface],
        name: str,
        instances_count: int | NotGiven = NOT_GIVEN,
        keypair_name: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
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
        """
        Create a new GPU cluster.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}'].post.parameters[1].schema"

          flavor: '#/components/schemas/CreateAIClusterGPUSerializer/properties/flavor'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.flavor"

          image_id: '#/components/schemas/CreateAIClusterGPUSerializer/properties/image_id'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.image_id"

          interfaces: '#/components/schemas/CreateAIClusterGPUSerializer/properties/interfaces'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.interfaces"

          name: '#/components/schemas/CreateAIClusterGPUSerializer/properties/name'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.name"

          instances_count: '#/components/schemas/CreateAIClusterGPUSerializer/properties/instances_count'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.instances_count"

          keypair_name: '#/components/schemas/CreateAIClusterGPUSerializer/properties/keypair_name'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.keypair_name"

          password: '#/components/schemas/CreateAIClusterGPUSerializer/properties/password'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.password"

          tags: '#/components/schemas/CreateAIClusterGPUSerializer/properties/tags'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.tags"

          user_data: '#/components/schemas/CreateAIClusterGPUSerializer/properties/user_data'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.user_data"

          username: '#/components/schemas/CreateAIClusterGPUSerializer/properties/username'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.username"

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
            f"/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "flavor": flavor,
                    "image_id": image_id,
                    "interfaces": interfaces,
                    "name": name,
                    "instances_count": instances_count,
                    "keypair_name": keypair_name,
                    "password": password,
                    "tags": tags,
                    "user_data": user_data,
                    "username": username,
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
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[GPUBaremetalCluster]:
        """
        List GPU clusters

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}'].get.parameters[1].schema"

          limit: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}'].get.parameters[2]"

          offset: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}'].get.parameters[3]"

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
            f"/cloud/v2/ai/clusters/{project_id}/{region_id}",
            page=SyncOffsetPage[GPUBaremetalCluster],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
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
        delete_floatings: bool | NotGiven = NOT_GIVEN,
        floatings: str | NotGiven = NOT_GIVEN,
        reserved_fixed_ips: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete GPU cluster

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[2].schema"

          delete_floatings: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/3'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[3]"

          floatings: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/4'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[4]"

          reserved_fixed_ips: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/5'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[5]"

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
            f"/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUBaremetalCluster:
        """
        Get GPU cluster

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}'].get.parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}'].get.parameters[2].schema"

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
            f"/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUClusterServerList:
        """
        Powercycle (stop and start) all GPU cluster nodes, aka hard reboot

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fpowercycle/post/parameters/0/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/powercycle'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fpowercycle/post/parameters/1/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/powercycle'].post.parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fpowercycle/post/parameters/2/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/powercycle'].post.parameters[2].schema"

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
            cast_to=GPUClusterServerList,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUClusterServerList:
        """
        Reboot all GPU cluster nodes

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Freboot/post/parameters/0/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/reboot'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Freboot/post/parameters/1/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/reboot'].post.parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Freboot/post/parameters/2/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/reboot'].post.parameters[2].schema"

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
            cast_to=GPUClusterServerList,
        )

    def rebuild(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        nodes: List[str],
        image_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_data: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Rebuild one or many nodes from GPU cluster.

        All cluster nodes need to be
        provided to change the cluster image.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Frebuild/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/rebuild'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Frebuild/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/rebuild'].post.parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Frebuild/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/rebuild'].post.parameters[2].schema"

          nodes: '#/components/schemas/RebuildClusterSerializer/properties/nodes'
              "$.components.schemas.RebuildClusterSerializer.properties.nodes"

          image_id: '#/components/schemas/RebuildClusterSerializer/properties/image_id/anyOf/0'
              "$.components.schemas.RebuildClusterSerializer.properties.image_id.anyOf[0]"

          user_data: '#/components/schemas/RebuildClusterSerializer/properties/user_data/anyOf/0'
              "$.components.schemas.RebuildClusterSerializer.properties.user_data.anyOf[0]"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Resize an existing AI GPU cluster.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fresize/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/resize'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fresize/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/resize'].post.parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fresize/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/resize'].post.parameters[2].schema"

          instances_count: '#/components/schemas/ResizeAIClusterGPUSerializerV1/properties/instances_count'
              "$.components.schemas.ResizeAIClusterGPUSerializerV1.properties.instances_count"

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

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGPUBaremetalClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGPUBaremetalClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncGPUBaremetalClustersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        image_id: str,
        interfaces: Iterable[gpu_baremetal_cluster_create_params.Interface],
        name: str,
        instances_count: int | NotGiven = NOT_GIVEN,
        keypair_name: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
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
        """
        Create a new GPU cluster.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}'].post.parameters[1].schema"

          flavor: '#/components/schemas/CreateAIClusterGPUSerializer/properties/flavor'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.flavor"

          image_id: '#/components/schemas/CreateAIClusterGPUSerializer/properties/image_id'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.image_id"

          interfaces: '#/components/schemas/CreateAIClusterGPUSerializer/properties/interfaces'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.interfaces"

          name: '#/components/schemas/CreateAIClusterGPUSerializer/properties/name'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.name"

          instances_count: '#/components/schemas/CreateAIClusterGPUSerializer/properties/instances_count'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.instances_count"

          keypair_name: '#/components/schemas/CreateAIClusterGPUSerializer/properties/keypair_name'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.keypair_name"

          password: '#/components/schemas/CreateAIClusterGPUSerializer/properties/password'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.password"

          tags: '#/components/schemas/CreateAIClusterGPUSerializer/properties/tags'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.tags"

          user_data: '#/components/schemas/CreateAIClusterGPUSerializer/properties/user_data'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.user_data"

          username: '#/components/schemas/CreateAIClusterGPUSerializer/properties/username'
              "$.components.schemas.CreateAIClusterGPUSerializer.properties.username"

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
            f"/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "flavor": flavor,
                    "image_id": image_id,
                    "interfaces": interfaces,
                    "name": name,
                    "instances_count": instances_count,
                    "keypair_name": keypair_name,
                    "password": password,
                    "tags": tags,
                    "user_data": user_data,
                    "username": username,
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
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[GPUBaremetalCluster, AsyncOffsetPage[GPUBaremetalCluster]]:
        """
        List GPU clusters

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}'].get.parameters[1].schema"

          limit: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}'].get.parameters[2]"

          offset: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}'].get.parameters[3]"

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
            f"/cloud/v2/ai/clusters/{project_id}/{region_id}",
            page=AsyncOffsetPage[GPUBaremetalCluster],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
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
        delete_floatings: bool | NotGiven = NOT_GIVEN,
        floatings: str | NotGiven = NOT_GIVEN,
        reserved_fixed_ips: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete GPU cluster

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[2].schema"

          delete_floatings: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/3'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[3]"

          floatings: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/4'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[4]"

          reserved_fixed_ips: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/5'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[5]"

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
            f"/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUBaremetalCluster:
        """
        Get GPU cluster

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}'].get.parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}'].get.parameters[2].schema"

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
            f"/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUClusterServerList:
        """
        Powercycle (stop and start) all GPU cluster nodes, aka hard reboot

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fpowercycle/post/parameters/0/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/powercycle'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fpowercycle/post/parameters/1/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/powercycle'].post.parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fpowercycle/post/parameters/2/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/powercycle'].post.parameters[2].schema"

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
            cast_to=GPUClusterServerList,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUClusterServerList:
        """
        Reboot all GPU cluster nodes

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Freboot/post/parameters/0/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/reboot'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Freboot/post/parameters/1/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/reboot'].post.parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Freboot/post/parameters/2/schema'
              "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/reboot'].post.parameters[2].schema"

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
            cast_to=GPUClusterServerList,
        )

    async def rebuild(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        nodes: List[str],
        image_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_data: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Rebuild one or many nodes from GPU cluster.

        All cluster nodes need to be
        provided to change the cluster image.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Frebuild/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/rebuild'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Frebuild/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/rebuild'].post.parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Frebuild/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/rebuild'].post.parameters[2].schema"

          nodes: '#/components/schemas/RebuildClusterSerializer/properties/nodes'
              "$.components.schemas.RebuildClusterSerializer.properties.nodes"

          image_id: '#/components/schemas/RebuildClusterSerializer/properties/image_id/anyOf/0'
              "$.components.schemas.RebuildClusterSerializer.properties.image_id.anyOf[0]"

          user_data: '#/components/schemas/RebuildClusterSerializer/properties/user_data/anyOf/0'
              "$.components.schemas.RebuildClusterSerializer.properties.user_data.anyOf[0]"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Resize an existing AI GPU cluster.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fresize/post/parameters/0/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/resize'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fresize/post/parameters/1/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/resize'].post.parameters[1].schema"

          cluster_id: '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fresize/post/parameters/2/schema'
              "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/resize'].post.parameters[2].schema"

          instances_count: '#/components/schemas/ResizeAIClusterGPUSerializerV1/properties/instances_count'
              "$.components.schemas.ResizeAIClusterGPUSerializerV1.properties.instances_count"

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

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional

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
from ....types.cloud.gpu_baremetal_cluster_server_list import GPUBaremetalClusterServerList

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
        interfaces: Iterable[gpu_baremetal_cluster_create_params.Interface],
        name: str,
        instances_count: int | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        ssh_key_name: str | NotGiven = NOT_GIVEN,
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
        """Create a new GPU cluster with specified configuration.

        The cluster can be
        created with one or more nodes.

        Args:
          flavor: Flavor name

          image_id: Image ID

          interfaces: A list of network interfaces for the server. You can create one or more
              interfaces - private, public, or both.

          name: GPU Cluster name

          instances_count: Number of servers to create

          password: A password for a bare metal server. This parameter is used to set a password for
              the "Admin" user on a Windows instance, a default user or a new user on a Linux
              instance

          ssh_key_name: Specifies the name of the SSH keypair, created via the
              [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          user_data: String in base64 format. Must not be passed together with 'username' or
              'password'. Examples of the `user_data`:
              https://cloudinit.readthedocs.io/en/latest/topics/examples.html

          username: A name of a new user in the Linux instance. It may be passed with a 'password'
              parameter

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
                    "password": password,
                    "ssh_key_name": ssh_key_name,
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
        List bare metal GPU clusters

        Args:
          limit: Limit the number of returned clusters

          offset: Offset value is used to exclude the first set of records from the result

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
        Delete bare metal GPU cluster

        Args:
          delete_floatings: True if it is required to delete floating IPs assigned to the servers. Can't be
              used with floatings.

          floatings: Comma separated list of floating ids that should be deleted. Can't be used with
              `delete_floatings`.

          reserved_fixed_ips: Comma separated list of port IDs to be deleted with the servers

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
        Get bare metal GPU cluster

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
    ) -> GPUBaremetalClusterServerList:
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
            cast_to=GPUBaremetalClusterServerList,
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
    ) -> GPUBaremetalClusterServerList:
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
            cast_to=GPUBaremetalClusterServerList,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        image_id: str,
        interfaces: Iterable[gpu_baremetal_cluster_create_params.Interface],
        name: str,
        instances_count: int | NotGiven = NOT_GIVEN,
        ssh_key_name: str | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUBaremetalCluster:
        """
        Create a bare metal GPU cluster and wait for it to be ready.
        """
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            image_id=image_id,
            interfaces=interfaces,
            name=name,
            instances_count=instances_count,
            ssh_key_name=ssh_key_name,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError(f"Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.ai_clusters:
            raise ValueError("No cluster was created")
        cluster_id = task.created_resources.ai_clusters[0]
        return self.get(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    def rebuild_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        nodes: List[str],
        image_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_data: Optional[str] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUBaremetalCluster:
        """
        Rebuild a bare metal GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.rebuild(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            nodes=nodes,
            image_id=image_id,
            user_data=user_data,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
        )
        return self.get(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    def resize_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        instances_count: int,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUBaremetalCluster:
        """
        Resize a bare metal GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.resize(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            instances_count=instances_count,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
        )
        return self.get(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
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
        interfaces: Iterable[gpu_baremetal_cluster_create_params.Interface],
        name: str,
        instances_count: int | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        ssh_key_name: str | NotGiven = NOT_GIVEN,
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
        """Create a new GPU cluster with specified configuration.

        The cluster can be
        created with one or more nodes.

        Args:
          flavor: Flavor name

          image_id: Image ID

          interfaces: A list of network interfaces for the server. You can create one or more
              interfaces - private, public, or both.

          name: GPU Cluster name

          instances_count: Number of servers to create

          password: A password for a bare metal server. This parameter is used to set a password for
              the "Admin" user on a Windows instance, a default user or a new user on a Linux
              instance

          ssh_key_name: Specifies the name of the SSH keypair, created via the
              [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          user_data: String in base64 format. Must not be passed together with 'username' or
              'password'. Examples of the `user_data`:
              https://cloudinit.readthedocs.io/en/latest/topics/examples.html

          username: A name of a new user in the Linux instance. It may be passed with a 'password'
              parameter

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
                    "password": password,
                    "ssh_key_name": ssh_key_name,
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
        List bare metal GPU clusters

        Args:
          limit: Limit the number of returned clusters

          offset: Offset value is used to exclude the first set of records from the result

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
        Delete bare metal GPU cluster

        Args:
          delete_floatings: True if it is required to delete floating IPs assigned to the servers. Can't be
              used with floatings.

          floatings: Comma separated list of floating ids that should be deleted. Can't be used with
              `delete_floatings`.

          reserved_fixed_ips: Comma separated list of port IDs to be deleted with the servers

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
        Get bare metal GPU cluster

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
    ) -> GPUBaremetalClusterServerList:
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
            cast_to=GPUBaremetalClusterServerList,
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
    ) -> GPUBaremetalClusterServerList:
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
            cast_to=GPUBaremetalClusterServerList,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        image_id: str,
        interfaces: Iterable[gpu_baremetal_cluster_create_params.Interface],
        name: str,
        instances_count: int | NotGiven = NOT_GIVEN,
        ssh_key_name: str | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUBaremetalCluster:
        """
        Create a bare metal GPU cluster and wait for it to be ready.
        """
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            image_id=image_id,
            interfaces=interfaces,
            name=name,
            instances_count=instances_count,
            ssh_key_name=ssh_key_name,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError(f"Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.ai_clusters:
            raise ValueError("No cluster was created")
        cluster_id = task.created_resources.ai_clusters[0]
        return await self.get(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    async def rebuild_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        nodes: List[str],
        image_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_data: Optional[str] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUBaremetalCluster:
        """
        Rebuild a bare metal GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.rebuild(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            nodes=nodes,
            image_id=image_id,
            user_data=user_data,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
        )
        return await self.get(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    async def resize_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        instances_count: int,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUBaremetalCluster:
        """
        Resize a bare metal GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.resize(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            instances_count=instances_count,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
        )
        return await self.get(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
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

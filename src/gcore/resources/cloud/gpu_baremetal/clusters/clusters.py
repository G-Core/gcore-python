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
from ....._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from .interfaces import (
    InterfacesResource,
    AsyncInterfacesResource,
    InterfacesResourceWithRawResponse,
    AsyncInterfacesResourceWithRawResponse,
    InterfacesResourceWithStreamingResponse,
    AsyncInterfacesResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncOffsetPage, AsyncOffsetPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.gpu_baremetal import (
    cluster_list_params,
    cluster_action_params,
    cluster_create_params,
    cluster_delete_params,
    cluster_resize_params,
    cluster_rebuild_params,
)
from .....types.cloud.tag_update_map_param import TagUpdateMapParam
from .....types.cloud.gpu_baremetal.gpu_baremetal_cluster import GPUBaremetalCluster
from .....types.cloud.gpu_baremetal.clusters.gpu_baremetal_cluster_server_v1_list import GPUBaremetalClusterServerV1List

__all__ = ["ClustersResource", "AsyncClustersResource"]


class ClustersResource(SyncAPIResource):
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
        flavor: str,
        image_id: str,
        name: str,
        servers_count: int,
        servers_settings: cluster_create_params.ServersSettings,
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
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

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
                cluster_create_params.ClusterCreateParams,
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
                    cluster_list_params.ClusterListParams,
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
                    cluster_delete_params.ClusterDeleteParams,
                ),
            ),
            cast_to=TaskIDList,
        )

    def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["update_tags"],
        tags: Optional[TagUpdateMapParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Perform a specific action on a baremetal GPU cluster.

        Available actions: update
        tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          action: Action name

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
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
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return self._post(
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters/{cluster_id}/action",
            body=maybe_transform(
                {
                    "action": action,
                    "tags": tags,
                },
                cluster_action_params.ClusterActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
                cluster_rebuild_params.ClusterRebuildParams,
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
            body=maybe_transform({"instances_count": instances_count}, cluster_resize_params.ClusterResizeParams),
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
        name: str,
        servers_count: int,
        servers_settings: cluster_create_params.ServersSettings,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
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
            name=name,
            servers_count=servers_count,
            servers_settings=servers_settings,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.ai_clusters:
            raise ValueError("No cluster was created")
        cluster_id = task.created_resources.ai_clusters[0]
        return self.get(  # pyright: ignore[reportDeprecated]
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
        image_id: Optional[str] | Omit = omit,
        user_data: Optional[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return self.get(  # pyright: ignore[reportDeprecated]
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
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return self.get(  # pyright: ignore[reportDeprecated]
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )


class AsyncClustersResource(AsyncAPIResource):
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
        flavor: str,
        image_id: str,
        name: str,
        servers_count: int,
        servers_settings: cluster_create_params.ServersSettings,
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
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

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
                cluster_create_params.ClusterCreateParams,
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
                    cluster_list_params.ClusterListParams,
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
                    cluster_delete_params.ClusterDeleteParams,
                ),
            ),
            cast_to=TaskIDList,
        )

    async def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["update_tags"],
        tags: Optional[TagUpdateMapParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Perform a specific action on a baremetal GPU cluster.

        Available actions: update
        tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          action: Action name

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
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
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return await self._post(
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters/{cluster_id}/action",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "tags": tags,
                },
                cluster_action_params.ClusterActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
                cluster_rebuild_params.ClusterRebuildParams,
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
                {"instances_count": instances_count}, cluster_resize_params.ClusterResizeParams
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
        name: str,
        servers_count: int,
        servers_settings: cluster_create_params.ServersSettings,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
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
            name=name,
            servers_count=servers_count,
            servers_settings=servers_settings,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.ai_clusters:
            raise ValueError("No cluster was created")
        cluster_id = task.created_resources.ai_clusters[0]
        return await self.get(  # pyright: ignore[reportDeprecated]
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
        image_id: Optional[str] | Omit = omit,
        user_data: Optional[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return await self.get(  # pyright: ignore[reportDeprecated]
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
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return await self.get(  # pyright: ignore[reportDeprecated]
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )


class ClustersResourceWithRawResponse:
    def __init__(self, clusters: ClustersResource) -> None:
        self._clusters = clusters

        self.create = to_raw_response_wrapper(
            clusters.create,
        )
        self.list = to_raw_response_wrapper(
            clusters.list,
        )
        self.delete = to_raw_response_wrapper(
            clusters.delete,
        )
        self.action = to_raw_response_wrapper(
            clusters.action,
        )
        self.get = to_raw_response_wrapper(
            clusters.get,
        )
        self.powercycle_all_servers = to_raw_response_wrapper(
            clusters.powercycle_all_servers,
        )
        self.reboot_all_servers = to_raw_response_wrapper(
            clusters.reboot_all_servers,
        )
        self.rebuild = to_raw_response_wrapper(
            clusters.rebuild,
        )
        self.resize = to_raw_response_wrapper(
            clusters.resize,
        )
        self.create_and_poll = to_raw_response_wrapper(
            clusters.create_and_poll,
        )
        self.rebuild_and_poll = to_raw_response_wrapper(
            clusters.rebuild_and_poll,
        )
        self.resize_and_poll = to_raw_response_wrapper(
            clusters.resize_and_poll,
        )

    @cached_property
    def interfaces(self) -> InterfacesResourceWithRawResponse:
        return InterfacesResourceWithRawResponse(self._clusters.interfaces)

    @cached_property
    def servers(self) -> ServersResourceWithRawResponse:
        return ServersResourceWithRawResponse(self._clusters.servers)

    @cached_property
    def flavors(self) -> FlavorsResourceWithRawResponse:
        return FlavorsResourceWithRawResponse(self._clusters.flavors)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._clusters.images)


class AsyncClustersResourceWithRawResponse:
    def __init__(self, clusters: AsyncClustersResource) -> None:
        self._clusters = clusters

        self.create = async_to_raw_response_wrapper(
            clusters.create,
        )
        self.list = async_to_raw_response_wrapper(
            clusters.list,
        )
        self.delete = async_to_raw_response_wrapper(
            clusters.delete,
        )
        self.action = async_to_raw_response_wrapper(
            clusters.action,
        )
        self.get = async_to_raw_response_wrapper(
            clusters.get,
        )
        self.powercycle_all_servers = async_to_raw_response_wrapper(
            clusters.powercycle_all_servers,
        )
        self.reboot_all_servers = async_to_raw_response_wrapper(
            clusters.reboot_all_servers,
        )
        self.rebuild = async_to_raw_response_wrapper(
            clusters.rebuild,
        )
        self.resize = async_to_raw_response_wrapper(
            clusters.resize,
        )
        self.create_and_poll = async_to_raw_response_wrapper(
            clusters.create_and_poll,
        )
        self.rebuild_and_poll = async_to_raw_response_wrapper(
            clusters.rebuild_and_poll,
        )
        self.resize_and_poll = async_to_raw_response_wrapper(
            clusters.resize_and_poll,
        )

    @cached_property
    def interfaces(self) -> AsyncInterfacesResourceWithRawResponse:
        return AsyncInterfacesResourceWithRawResponse(self._clusters.interfaces)

    @cached_property
    def servers(self) -> AsyncServersResourceWithRawResponse:
        return AsyncServersResourceWithRawResponse(self._clusters.servers)

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithRawResponse:
        return AsyncFlavorsResourceWithRawResponse(self._clusters.flavors)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._clusters.images)


class ClustersResourceWithStreamingResponse:
    def __init__(self, clusters: ClustersResource) -> None:
        self._clusters = clusters

        self.create = to_streamed_response_wrapper(
            clusters.create,
        )
        self.list = to_streamed_response_wrapper(
            clusters.list,
        )
        self.delete = to_streamed_response_wrapper(
            clusters.delete,
        )
        self.action = to_streamed_response_wrapper(
            clusters.action,
        )
        self.get = to_streamed_response_wrapper(
            clusters.get,
        )
        self.powercycle_all_servers = to_streamed_response_wrapper(
            clusters.powercycle_all_servers,
        )
        self.reboot_all_servers = to_streamed_response_wrapper(
            clusters.reboot_all_servers,
        )
        self.rebuild = to_streamed_response_wrapper(
            clusters.rebuild,
        )
        self.resize = to_streamed_response_wrapper(
            clusters.resize,
        )
        self.create_and_poll = to_streamed_response_wrapper(
            clusters.create_and_poll,
        )
        self.rebuild_and_poll = to_streamed_response_wrapper(
            clusters.rebuild_and_poll,
        )
        self.resize_and_poll = to_streamed_response_wrapper(
            clusters.resize_and_poll,
        )

    @cached_property
    def interfaces(self) -> InterfacesResourceWithStreamingResponse:
        return InterfacesResourceWithStreamingResponse(self._clusters.interfaces)

    @cached_property
    def servers(self) -> ServersResourceWithStreamingResponse:
        return ServersResourceWithStreamingResponse(self._clusters.servers)

    @cached_property
    def flavors(self) -> FlavorsResourceWithStreamingResponse:
        return FlavorsResourceWithStreamingResponse(self._clusters.flavors)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._clusters.images)


class AsyncClustersResourceWithStreamingResponse:
    def __init__(self, clusters: AsyncClustersResource) -> None:
        self._clusters = clusters

        self.create = async_to_streamed_response_wrapper(
            clusters.create,
        )
        self.list = async_to_streamed_response_wrapper(
            clusters.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            clusters.delete,
        )
        self.action = async_to_streamed_response_wrapper(
            clusters.action,
        )
        self.get = async_to_streamed_response_wrapper(
            clusters.get,
        )
        self.powercycle_all_servers = async_to_streamed_response_wrapper(
            clusters.powercycle_all_servers,
        )
        self.reboot_all_servers = async_to_streamed_response_wrapper(
            clusters.reboot_all_servers,
        )
        self.rebuild = async_to_streamed_response_wrapper(
            clusters.rebuild,
        )
        self.resize = async_to_streamed_response_wrapper(
            clusters.resize,
        )
        self.create_and_poll = async_to_streamed_response_wrapper(
            clusters.create_and_poll,
        )
        self.rebuild_and_poll = async_to_streamed_response_wrapper(
            clusters.rebuild_and_poll,
        )
        self.resize_and_poll = async_to_streamed_response_wrapper(
            clusters.resize_and_poll,
        )

    @cached_property
    def interfaces(self) -> AsyncInterfacesResourceWithStreamingResponse:
        return AsyncInterfacesResourceWithStreamingResponse(self._clusters.interfaces)

    @cached_property
    def servers(self) -> AsyncServersResourceWithStreamingResponse:
        return AsyncServersResourceWithStreamingResponse(self._clusters.servers)

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithStreamingResponse:
        return AsyncFlavorsResourceWithStreamingResponse(self._clusters.flavors)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._clusters.images)

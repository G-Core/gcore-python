# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, overload

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
from .volumes import (
    VolumesResource,
    AsyncVolumesResource,
    VolumesResourceWithRawResponse,
    AsyncVolumesResourceWithRawResponse,
    VolumesResourceWithStreamingResponse,
    AsyncVolumesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
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
    gpu_virtual_cluster_list_params,
    gpu_virtual_cluster_action_params,
    gpu_virtual_cluster_create_params,
    gpu_virtual_cluster_delete_params,
    gpu_virtual_cluster_update_params,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.gpu_virtual_cluster import GPUVirtualCluster
from ....types.cloud.tag_update_map_param import TagUpdateMapParam

__all__ = ["GPUVirtualClustersResource", "AsyncGPUVirtualClustersResource"]


class GPUVirtualClustersResource(SyncAPIResource):
    @cached_property
    def servers(self) -> ServersResource:
        return ServersResource(self._client)

    @cached_property
    def volumes(self) -> VolumesResource:
        return VolumesResource(self._client)

    @cached_property
    def interfaces(self) -> InterfacesResource:
        return InterfacesResource(self._client)

    @cached_property
    def flavors(self) -> FlavorsResource:
        return FlavorsResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> GPUVirtualClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return GPUVirtualClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GPUVirtualClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return GPUVirtualClustersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        name: str,
        servers_count: int,
        servers_settings: gpu_virtual_cluster_create_params.ServersSettings,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new virtual GPU cluster with the specified configuration.

        Args:
          project_id: Project ID

          region_id: Region ID

          flavor: Cluster flavor ID

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
            f"/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters",
            body=maybe_transform(
                {
                    "flavor": flavor,
                    "name": name,
                    "servers_count": servers_count,
                    "servers_settings": servers_settings,
                    "tags": tags,
                },
                gpu_virtual_cluster_create_params.GPUVirtualClusterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """
        Update the name of an existing virtual GPU cluster.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          name: Cluster name

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
        return self._patch(
            f"/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}",
            body=maybe_transform({"name": name}, gpu_virtual_cluster_update_params.GPUVirtualClusterUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUVirtualCluster,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[GPUVirtualCluster]:
        """
        List all virtual GPU clusters in the specified project and region.

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Limit of items on a single page

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
            f"/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters",
            page=SyncOffsetPage[GPUVirtualCluster],
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
                    gpu_virtual_cluster_list_params.GPUVirtualClusterListParams,
                ),
            ),
            model=GPUVirtualCluster,
        )

    def delete(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        all_floating_ips: bool | Omit = omit,
        all_reserved_fixed_ips: bool | Omit = omit,
        all_volumes: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        reserved_fixed_ip_ids: SequenceNotStr[str] | Omit = omit,
        volume_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete a virtual GPU cluster and all its associated resources.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          all_floating_ips: Flag indicating whether the floating ips associated with server / cluster are
              deleted

          all_reserved_fixed_ips: Flag indicating whether the reserved fixed ips associated with server / cluster
              are deleted

          all_volumes: Flag indicating whether all attached volumes are deleted

          floating_ip_ids: Optional list of floating ips to be deleted

          reserved_fixed_ip_ids: Optional list of reserved fixed ips to be deleted

          volume_ids: Optional list of volumes to be deleted

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
            f"/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "all_floating_ips": all_floating_ips,
                        "all_reserved_fixed_ips": all_reserved_fixed_ips,
                        "all_volumes": all_volumes,
                        "floating_ip_ids": floating_ip_ids,
                        "reserved_fixed_ip_ids": reserved_fixed_ip_ids,
                        "volume_ids": volume_ids,
                    },
                    gpu_virtual_cluster_delete_params.GPUVirtualClusterDeleteParams,
                ),
            ),
            cast_to=TaskIDList,
        )

    @overload
    def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Perform a specific action on a virtual GPU cluster.

        Available actions: start,
        stop, soft reboot, hard reboot, resize, update tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          action: Action name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["stop"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Perform a specific action on a virtual GPU cluster.

        Available actions: start,
        stop, soft reboot, hard reboot, resize, update tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          action: Action name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["soft_reboot"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Perform a specific action on a virtual GPU cluster.

        Available actions: start,
        stop, soft reboot, hard reboot, resize, update tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          action: Action name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["hard_reboot"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Perform a specific action on a virtual GPU cluster.

        Available actions: start,
        stop, soft reboot, hard reboot, resize, update tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          action: Action name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
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
        """Perform a specific action on a virtual GPU cluster.

        Available actions: start,
        stop, soft reboot, hard reboot, resize, update tags.

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
        ...

    @overload
    def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["resize"],
        servers_count: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Perform a specific action on a virtual GPU cluster.

        Available actions: start,
        stop, soft reboot, hard reboot, resize, update tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          action: Action name

          servers_count: Requested servers count

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["action"], ["action", "tags"], ["action", "servers_count"])
    def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"]
        | Literal["stop"]
        | Literal["soft_reboot"]
        | Literal["hard_reboot"]
        | Literal["update_tags"]
        | Literal["resize"],
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        servers_count: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return self._post(
            f"/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}/action",
            body=maybe_transform(
                {
                    "action": action,
                    "tags": tags,
                    "servers_count": servers_count,
                },
                gpu_virtual_cluster_action_params.GPUVirtualClusterActionParams,
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
    ) -> GPUVirtualCluster:
        """
        Get detailed information about a specific virtual GPU cluster.

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
            f"/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUVirtualCluster,
        )


class AsyncGPUVirtualClustersResource(AsyncAPIResource):
    @cached_property
    def servers(self) -> AsyncServersResource:
        return AsyncServersResource(self._client)

    @cached_property
    def volumes(self) -> AsyncVolumesResource:
        return AsyncVolumesResource(self._client)

    @cached_property
    def interfaces(self) -> AsyncInterfacesResource:
        return AsyncInterfacesResource(self._client)

    @cached_property
    def flavors(self) -> AsyncFlavorsResource:
        return AsyncFlavorsResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGPUVirtualClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGPUVirtualClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGPUVirtualClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncGPUVirtualClustersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        name: str,
        servers_count: int,
        servers_settings: gpu_virtual_cluster_create_params.ServersSettings,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new virtual GPU cluster with the specified configuration.

        Args:
          project_id: Project ID

          region_id: Region ID

          flavor: Cluster flavor ID

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
            f"/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters",
            body=await async_maybe_transform(
                {
                    "flavor": flavor,
                    "name": name,
                    "servers_count": servers_count,
                    "servers_settings": servers_settings,
                    "tags": tags,
                },
                gpu_virtual_cluster_create_params.GPUVirtualClusterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """
        Update the name of an existing virtual GPU cluster.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          name: Cluster name

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
        return await self._patch(
            f"/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}",
            body=await async_maybe_transform(
                {"name": name}, gpu_virtual_cluster_update_params.GPUVirtualClusterUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUVirtualCluster,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[GPUVirtualCluster, AsyncOffsetPage[GPUVirtualCluster]]:
        """
        List all virtual GPU clusters in the specified project and region.

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Limit of items on a single page

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
            f"/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters",
            page=AsyncOffsetPage[GPUVirtualCluster],
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
                    gpu_virtual_cluster_list_params.GPUVirtualClusterListParams,
                ),
            ),
            model=GPUVirtualCluster,
        )

    async def delete(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        all_floating_ips: bool | Omit = omit,
        all_reserved_fixed_ips: bool | Omit = omit,
        all_volumes: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        reserved_fixed_ip_ids: SequenceNotStr[str] | Omit = omit,
        volume_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete a virtual GPU cluster and all its associated resources.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          all_floating_ips: Flag indicating whether the floating ips associated with server / cluster are
              deleted

          all_reserved_fixed_ips: Flag indicating whether the reserved fixed ips associated with server / cluster
              are deleted

          all_volumes: Flag indicating whether all attached volumes are deleted

          floating_ip_ids: Optional list of floating ips to be deleted

          reserved_fixed_ip_ids: Optional list of reserved fixed ips to be deleted

          volume_ids: Optional list of volumes to be deleted

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
            f"/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "all_floating_ips": all_floating_ips,
                        "all_reserved_fixed_ips": all_reserved_fixed_ips,
                        "all_volumes": all_volumes,
                        "floating_ip_ids": floating_ip_ids,
                        "reserved_fixed_ip_ids": reserved_fixed_ip_ids,
                        "volume_ids": volume_ids,
                    },
                    gpu_virtual_cluster_delete_params.GPUVirtualClusterDeleteParams,
                ),
            ),
            cast_to=TaskIDList,
        )

    @overload
    async def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Perform a specific action on a virtual GPU cluster.

        Available actions: start,
        stop, soft reboot, hard reboot, resize, update tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          action: Action name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["stop"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Perform a specific action on a virtual GPU cluster.

        Available actions: start,
        stop, soft reboot, hard reboot, resize, update tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          action: Action name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["soft_reboot"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Perform a specific action on a virtual GPU cluster.

        Available actions: start,
        stop, soft reboot, hard reboot, resize, update tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          action: Action name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["hard_reboot"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Perform a specific action on a virtual GPU cluster.

        Available actions: start,
        stop, soft reboot, hard reboot, resize, update tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          action: Action name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
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
        """Perform a specific action on a virtual GPU cluster.

        Available actions: start,
        stop, soft reboot, hard reboot, resize, update tags.

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
        ...

    @overload
    async def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["resize"],
        servers_count: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Perform a specific action on a virtual GPU cluster.

        Available actions: start,
        stop, soft reboot, hard reboot, resize, update tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          action: Action name

          servers_count: Requested servers count

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["action"], ["action", "tags"], ["action", "servers_count"])
    async def action(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"]
        | Literal["stop"]
        | Literal["soft_reboot"]
        | Literal["hard_reboot"]
        | Literal["update_tags"]
        | Literal["resize"],
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        servers_count: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return await self._post(
            f"/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}/action",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "tags": tags,
                    "servers_count": servers_count,
                },
                gpu_virtual_cluster_action_params.GPUVirtualClusterActionParams,
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
    ) -> GPUVirtualCluster:
        """
        Get detailed information about a specific virtual GPU cluster.

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
            f"/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUVirtualCluster,
        )


class GPUVirtualClustersResourceWithRawResponse:
    def __init__(self, gpu_virtual_clusters: GPUVirtualClustersResource) -> None:
        self._gpu_virtual_clusters = gpu_virtual_clusters

        self.create = to_raw_response_wrapper(
            gpu_virtual_clusters.create,
        )
        self.update = to_raw_response_wrapper(
            gpu_virtual_clusters.update,
        )
        self.list = to_raw_response_wrapper(
            gpu_virtual_clusters.list,
        )
        self.delete = to_raw_response_wrapper(
            gpu_virtual_clusters.delete,
        )
        self.action = to_raw_response_wrapper(
            gpu_virtual_clusters.action,
        )
        self.get = to_raw_response_wrapper(
            gpu_virtual_clusters.get,
        )

    @cached_property
    def servers(self) -> ServersResourceWithRawResponse:
        return ServersResourceWithRawResponse(self._gpu_virtual_clusters.servers)

    @cached_property
    def volumes(self) -> VolumesResourceWithRawResponse:
        return VolumesResourceWithRawResponse(self._gpu_virtual_clusters.volumes)

    @cached_property
    def interfaces(self) -> InterfacesResourceWithRawResponse:
        return InterfacesResourceWithRawResponse(self._gpu_virtual_clusters.interfaces)

    @cached_property
    def flavors(self) -> FlavorsResourceWithRawResponse:
        return FlavorsResourceWithRawResponse(self._gpu_virtual_clusters.flavors)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._gpu_virtual_clusters.images)


class AsyncGPUVirtualClustersResourceWithRawResponse:
    def __init__(self, gpu_virtual_clusters: AsyncGPUVirtualClustersResource) -> None:
        self._gpu_virtual_clusters = gpu_virtual_clusters

        self.create = async_to_raw_response_wrapper(
            gpu_virtual_clusters.create,
        )
        self.update = async_to_raw_response_wrapper(
            gpu_virtual_clusters.update,
        )
        self.list = async_to_raw_response_wrapper(
            gpu_virtual_clusters.list,
        )
        self.delete = async_to_raw_response_wrapper(
            gpu_virtual_clusters.delete,
        )
        self.action = async_to_raw_response_wrapper(
            gpu_virtual_clusters.action,
        )
        self.get = async_to_raw_response_wrapper(
            gpu_virtual_clusters.get,
        )

    @cached_property
    def servers(self) -> AsyncServersResourceWithRawResponse:
        return AsyncServersResourceWithRawResponse(self._gpu_virtual_clusters.servers)

    @cached_property
    def volumes(self) -> AsyncVolumesResourceWithRawResponse:
        return AsyncVolumesResourceWithRawResponse(self._gpu_virtual_clusters.volumes)

    @cached_property
    def interfaces(self) -> AsyncInterfacesResourceWithRawResponse:
        return AsyncInterfacesResourceWithRawResponse(self._gpu_virtual_clusters.interfaces)

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithRawResponse:
        return AsyncFlavorsResourceWithRawResponse(self._gpu_virtual_clusters.flavors)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._gpu_virtual_clusters.images)


class GPUVirtualClustersResourceWithStreamingResponse:
    def __init__(self, gpu_virtual_clusters: GPUVirtualClustersResource) -> None:
        self._gpu_virtual_clusters = gpu_virtual_clusters

        self.create = to_streamed_response_wrapper(
            gpu_virtual_clusters.create,
        )
        self.update = to_streamed_response_wrapper(
            gpu_virtual_clusters.update,
        )
        self.list = to_streamed_response_wrapper(
            gpu_virtual_clusters.list,
        )
        self.delete = to_streamed_response_wrapper(
            gpu_virtual_clusters.delete,
        )
        self.action = to_streamed_response_wrapper(
            gpu_virtual_clusters.action,
        )
        self.get = to_streamed_response_wrapper(
            gpu_virtual_clusters.get,
        )

    @cached_property
    def servers(self) -> ServersResourceWithStreamingResponse:
        return ServersResourceWithStreamingResponse(self._gpu_virtual_clusters.servers)

    @cached_property
    def volumes(self) -> VolumesResourceWithStreamingResponse:
        return VolumesResourceWithStreamingResponse(self._gpu_virtual_clusters.volumes)

    @cached_property
    def interfaces(self) -> InterfacesResourceWithStreamingResponse:
        return InterfacesResourceWithStreamingResponse(self._gpu_virtual_clusters.interfaces)

    @cached_property
    def flavors(self) -> FlavorsResourceWithStreamingResponse:
        return FlavorsResourceWithStreamingResponse(self._gpu_virtual_clusters.flavors)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._gpu_virtual_clusters.images)


class AsyncGPUVirtualClustersResourceWithStreamingResponse:
    def __init__(self, gpu_virtual_clusters: AsyncGPUVirtualClustersResource) -> None:
        self._gpu_virtual_clusters = gpu_virtual_clusters

        self.create = async_to_streamed_response_wrapper(
            gpu_virtual_clusters.create,
        )
        self.update = async_to_streamed_response_wrapper(
            gpu_virtual_clusters.update,
        )
        self.list = async_to_streamed_response_wrapper(
            gpu_virtual_clusters.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            gpu_virtual_clusters.delete,
        )
        self.action = async_to_streamed_response_wrapper(
            gpu_virtual_clusters.action,
        )
        self.get = async_to_streamed_response_wrapper(
            gpu_virtual_clusters.get,
        )

    @cached_property
    def servers(self) -> AsyncServersResourceWithStreamingResponse:
        return AsyncServersResourceWithStreamingResponse(self._gpu_virtual_clusters.servers)

    @cached_property
    def volumes(self) -> AsyncVolumesResourceWithStreamingResponse:
        return AsyncVolumesResourceWithStreamingResponse(self._gpu_virtual_clusters.volumes)

    @cached_property
    def interfaces(self) -> AsyncInterfacesResourceWithStreamingResponse:
        return AsyncInterfacesResourceWithStreamingResponse(self._gpu_virtual_clusters.interfaces)

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithStreamingResponse:
        return AsyncFlavorsResourceWithStreamingResponse(self._gpu_virtual_clusters.flavors)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._gpu_virtual_clusters.images)

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from .routers import (
    RoutersResource,
    AsyncRoutersResource,
    RoutersResourceWithRawResponse,
    AsyncRoutersResourceWithRawResponse,
    RoutersResourceWithStreamingResponse,
    AsyncRoutersResourceWithStreamingResponse,
)
from .subnets import (
    SubnetsResource,
    AsyncSubnetsResource,
    SubnetsResourceWithRawResponse,
    AsyncSubnetsResourceWithRawResponse,
    SubnetsResourceWithStreamingResponse,
    AsyncSubnetsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ....types.cloud import network_list_params, network_create_params, network_update_params
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.network import Network
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.tag_update_map_param import TagUpdateMapParam

__all__ = ["NetworksResource", "AsyncNetworksResource"]


class NetworksResource(SyncAPIResource):
    @cached_property
    def subnets(self) -> SubnetsResource:
        return SubnetsResource(self._client)

    @cached_property
    def routers(self) -> RoutersResource:
        return RoutersResource(self._client)

    @cached_property
    def with_raw_response(self) -> NetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return NetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return NetworksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        create_router: bool | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type: Literal["vlan", "vxlan"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create network

        Args:
          project_id: Project ID

          region_id: Region ID

          name: Network name

          create_router: Defaults to True

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

          type: vlan or vxlan network type is allowed. Default value is vxlan

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
            f"/cloud/v1/networks/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "create_router": create_router,
                    "tags": tags,
                    "type": type,
                },
                network_create_params.NetworkCreateParams,
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
        name: str,
        create_router: bool | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type: Literal["vlan", "vxlan"] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Network:
        """Create network and poll for the result."""
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            name=name,
            create_router=create_router,
            tags=tags,
            type=type,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            not task.created_resources
            or not task.created_resources.networks
            or len(task.created_resources.networks) != 1
        ):
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return self.get(
            network_id=task.created_resources.networks[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
        )

    def update(
        self,
        network_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Network:
        """Rename network and/or update network tags.

        The request will only process the
        fields that are provided in the request body. Any fields that are not included
        will remain unchanged.

        Args:
          project_id: Project ID

          region_id: Region ID

          network_id: Network ID

          name: Name.

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
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return self._patch(
            f"/cloud/v1/networks/{project_id}/{region_id}/{network_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "tags": tags,
                },
                network_update_params.NetworkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Network,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["created_at.asc", "created_at.desc", "name.asc", "name.desc"] | Omit = omit,
        tag_key: SequenceNotStr[str] | Omit = omit,
        tag_key_value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[Network]:
        """
        List networks

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Optional. Limit the number of returned items

          name: Filter networks by name

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          order_by: Ordering networks list result by `name`, `created_at` fields of the network and
              directions (`created_at.desc`).

          tag_key: Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2

          tag_key_value: Optional. Filter by tag key-value pairs.

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
            f"/cloud/v1/networks/{project_id}/{region_id}",
            page=SyncOffsetPage[Network],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                    },
                    network_list_params.NetworkListParams,
                ),
            ),
            model=Network,
        )

    def delete(
        self,
        network_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete network

        Args:
          project_id: Project ID

          region_id: Region ID

          network_id: Network ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return self._delete(
            f"/cloud/v1/networks/{project_id}/{region_id}/{network_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def delete_and_poll(
        self,
        network_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete network and poll for the result."""
        response = self.delete(
            network_id=network_id,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )

    def get(
        self,
        network_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Network:
        """
        Get network

        Args:
          project_id: Project ID

          region_id: Region ID

          network_id: Network ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return self._get(
            f"/cloud/v1/networks/{project_id}/{region_id}/{network_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Network,
        )


class AsyncNetworksResource(AsyncAPIResource):
    @cached_property
    def subnets(self) -> AsyncSubnetsResource:
        return AsyncSubnetsResource(self._client)

    @cached_property
    def routers(self) -> AsyncRoutersResource:
        return AsyncRoutersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncNetworksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        create_router: bool | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type: Literal["vlan", "vxlan"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create network

        Args:
          project_id: Project ID

          region_id: Region ID

          name: Network name

          create_router: Defaults to True

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

          type: vlan or vxlan network type is allowed. Default value is vxlan

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
            f"/cloud/v1/networks/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "create_router": create_router,
                    "tags": tags,
                    "type": type,
                },
                network_create_params.NetworkCreateParams,
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
        name: str,
        create_router: bool | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type: Literal["vlan", "vxlan"] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Network:
        """Create network and poll for the result."""
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            name=name,
            create_router=create_router,
            tags=tags,
            type=type,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            not task.created_resources
            or not task.created_resources.networks
            or len(task.created_resources.networks) != 1
        ):
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return await self.get(
            network_id=task.created_resources.networks[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
        )

    async def update(
        self,
        network_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Network:
        """Rename network and/or update network tags.

        The request will only process the
        fields that are provided in the request body. Any fields that are not included
        will remain unchanged.

        Args:
          project_id: Project ID

          region_id: Region ID

          network_id: Network ID

          name: Name.

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
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return await self._patch(
            f"/cloud/v1/networks/{project_id}/{region_id}/{network_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "tags": tags,
                },
                network_update_params.NetworkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Network,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["created_at.asc", "created_at.desc", "name.asc", "name.desc"] | Omit = omit,
        tag_key: SequenceNotStr[str] | Omit = omit,
        tag_key_value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Network, AsyncOffsetPage[Network]]:
        """
        List networks

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Optional. Limit the number of returned items

          name: Filter networks by name

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          order_by: Ordering networks list result by `name`, `created_at` fields of the network and
              directions (`created_at.desc`).

          tag_key: Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2

          tag_key_value: Optional. Filter by tag key-value pairs.

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
            f"/cloud/v1/networks/{project_id}/{region_id}",
            page=AsyncOffsetPage[Network],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                    },
                    network_list_params.NetworkListParams,
                ),
            ),
            model=Network,
        )

    async def delete(
        self,
        network_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete network

        Args:
          project_id: Project ID

          region_id: Region ID

          network_id: Network ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return await self._delete(
            f"/cloud/v1/networks/{project_id}/{region_id}/{network_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def delete_and_poll(
        self,
        network_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete network and poll for the result."""
        response = await self.delete(
            network_id=network_id,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )

    async def get(
        self,
        network_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Network:
        """
        Get network

        Args:
          project_id: Project ID

          region_id: Region ID

          network_id: Network ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return await self._get(
            f"/cloud/v1/networks/{project_id}/{region_id}/{network_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Network,
        )


class NetworksResourceWithRawResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

        self.create = to_raw_response_wrapper(
            networks.create,
        )
        self.create_and_poll = to_raw_response_wrapper(
            networks.create_and_poll,
        )
        self.update = to_raw_response_wrapper(
            networks.update,
        )
        self.list = to_raw_response_wrapper(
            networks.list,
        )
        self.delete = to_raw_response_wrapper(
            networks.delete,
        )
        self.delete_and_poll = to_raw_response_wrapper(
            networks.delete_and_poll,
        )
        self.get = to_raw_response_wrapper(
            networks.get,
        )

    @cached_property
    def subnets(self) -> SubnetsResourceWithRawResponse:
        return SubnetsResourceWithRawResponse(self._networks.subnets)

    @cached_property
    def routers(self) -> RoutersResourceWithRawResponse:
        return RoutersResourceWithRawResponse(self._networks.routers)


class AsyncNetworksResourceWithRawResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

        self.create = async_to_raw_response_wrapper(
            networks.create,
        )
        self.create_and_poll = async_to_raw_response_wrapper(
            networks.create_and_poll,
        )
        self.update = async_to_raw_response_wrapper(
            networks.update,
        )
        self.list = async_to_raw_response_wrapper(
            networks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            networks.delete,
        )
        self.delete_and_poll = async_to_raw_response_wrapper(
            networks.delete_and_poll,
        )
        self.get = async_to_raw_response_wrapper(
            networks.get,
        )

    @cached_property
    def subnets(self) -> AsyncSubnetsResourceWithRawResponse:
        return AsyncSubnetsResourceWithRawResponse(self._networks.subnets)

    @cached_property
    def routers(self) -> AsyncRoutersResourceWithRawResponse:
        return AsyncRoutersResourceWithRawResponse(self._networks.routers)


class NetworksResourceWithStreamingResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

        self.create = to_streamed_response_wrapper(
            networks.create,
        )
        self.create_and_poll = to_streamed_response_wrapper(
            networks.create_and_poll,
        )
        self.update = to_streamed_response_wrapper(
            networks.update,
        )
        self.list = to_streamed_response_wrapper(
            networks.list,
        )
        self.delete = to_streamed_response_wrapper(
            networks.delete,
        )
        self.delete_and_poll = to_streamed_response_wrapper(
            networks.delete_and_poll,
        )
        self.get = to_streamed_response_wrapper(
            networks.get,
        )

    @cached_property
    def subnets(self) -> SubnetsResourceWithStreamingResponse:
        return SubnetsResourceWithStreamingResponse(self._networks.subnets)

    @cached_property
    def routers(self) -> RoutersResourceWithStreamingResponse:
        return RoutersResourceWithStreamingResponse(self._networks.routers)


class AsyncNetworksResourceWithStreamingResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

        self.create = async_to_streamed_response_wrapper(
            networks.create,
        )
        self.create_and_poll = async_to_streamed_response_wrapper(
            networks.create_and_poll,
        )
        self.update = async_to_streamed_response_wrapper(
            networks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            networks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            networks.delete,
        )
        self.delete_and_poll = async_to_streamed_response_wrapper(
            networks.delete_and_poll,
        )
        self.get = async_to_streamed_response_wrapper(
            networks.get,
        )

    @cached_property
    def subnets(self) -> AsyncSubnetsResourceWithStreamingResponse:
        return AsyncSubnetsResourceWithStreamingResponse(self._networks.subnets)

    @cached_property
    def routers(self) -> AsyncRoutersResourceWithStreamingResponse:
        return AsyncRoutersResourceWithStreamingResponse(self._networks.routers)

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .access_rules import (
    AccessRulesResource,
    AsyncAccessRulesResource,
    AccessRulesResourceWithRawResponse,
    AsyncAccessRulesResourceWithRawResponse,
    AccessRulesResourceWithStreamingResponse,
    AsyncAccessRulesResourceWithStreamingResponse,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ....types.cloud import (
    file_share_list_params,
    file_share_create_params,
    file_share_resize_params,
    file_share_update_params,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.file_share import FileShare
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.tag_update_map_param import TagUpdateMapParam

__all__ = ["FileSharesResource", "AsyncFileSharesResource"]


class FileSharesResource(SyncAPIResource):
    @cached_property
    def access_rules(self) -> AccessRulesResource:
        return AccessRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> FileSharesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return FileSharesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileSharesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return FileSharesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        network: file_share_create_params.CreateStandardFileShareSerializerNetwork,
        protocol: Literal["NFS"],
        size: int,
        access: Iterable[file_share_create_params.CreateStandardFileShareSerializerAccess] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type_name: Literal["standard"] | Omit = omit,
        volume_type: Literal["default_share_type"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create file share

        Args:
          project_id: Project ID

          region_id: Region ID

          name: File share name

          network: File share network configuration

          protocol: File share protocol

          size: File share size in GiB

          access: Access Rules

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

          type_name: Standard file share type

          volume_type: Deprecated. Use `type_name` instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        protocol: Literal["NFS"],
        size: int,
        share_settings: file_share_create_params.CreateVastFileShareSerializerShareSettings | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type_name: Literal["vast"] | Omit = omit,
        volume_type: Literal["vast_share_type"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create file share

        Args:
          project_id: Project ID

          region_id: Region ID

          name: File share name

          protocol: File share protocol

          size: File share size in GiB

          share_settings: Configuration settings for the share

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

          type_name: Vast file share type

          volume_type: Deprecated. Use `type_name` instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name", "network", "protocol", "size"], ["name", "protocol", "size"])
    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        network: file_share_create_params.CreateStandardFileShareSerializerNetwork | Omit = omit,
        protocol: Literal["NFS"],
        size: int,
        access: Iterable[file_share_create_params.CreateStandardFileShareSerializerAccess] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type_name: Literal["standard"] | Literal["vast"] | Omit = omit,
        volume_type: Literal["default_share_type"] | Literal["vast_share_type"] | Omit = omit,
        share_settings: file_share_create_params.CreateVastFileShareSerializerShareSettings | Omit = omit,
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
        return self._post(
            f"/cloud/v1/file_shares/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "network": network,
                    "protocol": protocol,
                    "size": size,
                    "access": access,
                    "tags": tags,
                    "type_name": type_name,
                    "volume_type": volume_type,
                    "share_settings": share_settings,
                },
                file_share_create_params.FileShareCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | Omit = omit,
        share_settings: file_share_update_params.ShareSettings | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Rename file share, update tags or set share specific properties

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          name: Name

          share_settings: Configuration settings for the share

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
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        return self._patch(
            f"/cloud/v3/file_shares/{project_id}/{region_id}/{file_share_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "share_settings": share_settings,
                    "tags": tags,
                },
                file_share_update_params.FileShareUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update_and_poll(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | Omit = omit,
        share_settings: file_share_update_params.ShareSettings | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        response = self.update(
            file_share_id,
            project_id=project_id,
            region_id=region_id,
            name=name,
            share_settings=share_settings,
            tags=tags,
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
        return self.get(
            file_share_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        type_name: Literal["standard", "vast"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[FileShare]:
        """
        List file shares

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Optional. Limit the number of returned items

          name: File share name. Uses partial match.

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          type_name: File share type name

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
            f"/cloud/v1/file_shares/{project_id}/{region_id}",
            page=SyncOffsetPage[FileShare],
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
                        "type_name": type_name,
                    },
                    file_share_list_params.FileShareListParams,
                ),
            ),
            model=FileShare,
        )

    def delete(
        self,
        file_share_id: str,
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
        Delete file share

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        return self._delete(
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        """
        Get file share

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        return self._get(
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileShare,
        )

    def resize(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Resize file share

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          size: File Share new size in GiB.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        return self._post(
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/extend",
            body=maybe_transform({"size": size}, file_share_resize_params.FileShareResizeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class AsyncFileSharesResource(AsyncAPIResource):
    @cached_property
    def access_rules(self) -> AsyncAccessRulesResource:
        return AsyncAccessRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFileSharesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFileSharesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileSharesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncFileSharesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        network: file_share_create_params.CreateStandardFileShareSerializerNetwork,
        protocol: Literal["NFS"],
        size: int,
        access: Iterable[file_share_create_params.CreateStandardFileShareSerializerAccess] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type_name: Literal["standard"] | Omit = omit,
        volume_type: Literal["default_share_type"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create file share

        Args:
          project_id: Project ID

          region_id: Region ID

          name: File share name

          network: File share network configuration

          protocol: File share protocol

          size: File share size in GiB

          access: Access Rules

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

          type_name: Standard file share type

          volume_type: Deprecated. Use `type_name` instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        protocol: Literal["NFS"],
        size: int,
        share_settings: file_share_create_params.CreateVastFileShareSerializerShareSettings | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type_name: Literal["vast"] | Omit = omit,
        volume_type: Literal["vast_share_type"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create file share

        Args:
          project_id: Project ID

          region_id: Region ID

          name: File share name

          protocol: File share protocol

          size: File share size in GiB

          share_settings: Configuration settings for the share

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

          type_name: Vast file share type

          volume_type: Deprecated. Use `type_name` instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name", "network", "protocol", "size"], ["name", "protocol", "size"])
    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        network: file_share_create_params.CreateStandardFileShareSerializerNetwork | Omit = omit,
        protocol: Literal["NFS"],
        size: int,
        access: Iterable[file_share_create_params.CreateStandardFileShareSerializerAccess] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type_name: Literal["standard"] | Literal["vast"] | Omit = omit,
        volume_type: Literal["default_share_type"] | Literal["vast_share_type"] | Omit = omit,
        share_settings: file_share_create_params.CreateVastFileShareSerializerShareSettings | Omit = omit,
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
        return await self._post(
            f"/cloud/v1/file_shares/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "network": network,
                    "protocol": protocol,
                    "size": size,
                    "access": access,
                    "tags": tags,
                    "type_name": type_name,
                    "volume_type": volume_type,
                    "share_settings": share_settings,
                },
                file_share_create_params.FileShareCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | Omit = omit,
        share_settings: file_share_update_params.ShareSettings | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Rename file share, update tags or set share specific properties

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          name: Name

          share_settings: Configuration settings for the share

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
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        return await self._patch(
            f"/cloud/v3/file_shares/{project_id}/{region_id}/{file_share_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "share_settings": share_settings,
                    "tags": tags,
                },
                file_share_update_params.FileShareUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update_and_poll(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | Omit = omit,
        share_settings: file_share_update_params.ShareSettings | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        response = await self.update(
            file_share_id,
            project_id=project_id,
            region_id=region_id,
            name=name,
            share_settings=share_settings,
            tags=tags,
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
        return await self.get(
            file_share_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        type_name: Literal["standard", "vast"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FileShare, AsyncOffsetPage[FileShare]]:
        """
        List file shares

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Optional. Limit the number of returned items

          name: File share name. Uses partial match.

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          type_name: File share type name

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
            f"/cloud/v1/file_shares/{project_id}/{region_id}",
            page=AsyncOffsetPage[FileShare],
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
                        "type_name": type_name,
                    },
                    file_share_list_params.FileShareListParams,
                ),
            ),
            model=FileShare,
        )

    async def delete(
        self,
        file_share_id: str,
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
        Delete file share

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        return await self._delete(
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        """
        Get file share

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        return await self._get(
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileShare,
        )

    async def resize(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Resize file share

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          size: File Share new size in GiB.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        return await self._post(
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/extend",
            body=await async_maybe_transform({"size": size}, file_share_resize_params.FileShareResizeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class FileSharesResourceWithRawResponse:
    def __init__(self, file_shares: FileSharesResource) -> None:
        self._file_shares = file_shares

        self.create = to_raw_response_wrapper(
            file_shares.create,
        )
        self.update = to_raw_response_wrapper(
            file_shares.update,
        )
        self.update_and_poll = to_raw_response_wrapper(
            file_shares.update_and_poll,
        )
        self.list = to_raw_response_wrapper(
            file_shares.list,
        )
        self.delete = to_raw_response_wrapper(
            file_shares.delete,
        )
        self.get = to_raw_response_wrapper(
            file_shares.get,
        )
        self.resize = to_raw_response_wrapper(
            file_shares.resize,
        )

    @cached_property
    def access_rules(self) -> AccessRulesResourceWithRawResponse:
        return AccessRulesResourceWithRawResponse(self._file_shares.access_rules)


class AsyncFileSharesResourceWithRawResponse:
    def __init__(self, file_shares: AsyncFileSharesResource) -> None:
        self._file_shares = file_shares

        self.create = async_to_raw_response_wrapper(
            file_shares.create,
        )
        self.update = async_to_raw_response_wrapper(
            file_shares.update,
        )
        self.update_and_poll = async_to_raw_response_wrapper(
            file_shares.update_and_poll,
        )
        self.list = async_to_raw_response_wrapper(
            file_shares.list,
        )
        self.delete = async_to_raw_response_wrapper(
            file_shares.delete,
        )
        self.get = async_to_raw_response_wrapper(
            file_shares.get,
        )
        self.resize = async_to_raw_response_wrapper(
            file_shares.resize,
        )

    @cached_property
    def access_rules(self) -> AsyncAccessRulesResourceWithRawResponse:
        return AsyncAccessRulesResourceWithRawResponse(self._file_shares.access_rules)


class FileSharesResourceWithStreamingResponse:
    def __init__(self, file_shares: FileSharesResource) -> None:
        self._file_shares = file_shares

        self.create = to_streamed_response_wrapper(
            file_shares.create,
        )
        self.update = to_streamed_response_wrapper(
            file_shares.update,
        )
        self.update_and_poll = to_streamed_response_wrapper(
            file_shares.update_and_poll,
        )
        self.list = to_streamed_response_wrapper(
            file_shares.list,
        )
        self.delete = to_streamed_response_wrapper(
            file_shares.delete,
        )
        self.get = to_streamed_response_wrapper(
            file_shares.get,
        )
        self.resize = to_streamed_response_wrapper(
            file_shares.resize,
        )

    @cached_property
    def access_rules(self) -> AccessRulesResourceWithStreamingResponse:
        return AccessRulesResourceWithStreamingResponse(self._file_shares.access_rules)


class AsyncFileSharesResourceWithStreamingResponse:
    def __init__(self, file_shares: AsyncFileSharesResource) -> None:
        self._file_shares = file_shares

        self.create = async_to_streamed_response_wrapper(
            file_shares.create,
        )
        self.update = async_to_streamed_response_wrapper(
            file_shares.update,
        )
        self.update_and_pol = async_to_streamed_response_wrapper(
            file_shares.update_and_poll,
        )
        self.list = async_to_streamed_response_wrapper(
            file_shares.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            file_shares.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            file_shares.get,
        )
        self.resize = async_to_streamed_response_wrapper(
            file_shares.resize,
        )

    @cached_property
    def access_rules(self) -> AsyncAccessRulesResourceWithStreamingResponse:
        return AsyncAccessRulesResourceWithStreamingResponse(self._file_shares.access_rules)

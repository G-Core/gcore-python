# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, overload

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
        access: Iterable[file_share_create_params.CreateStandardFileShareSerializerAccess] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        volume_type: Literal["default_share_type"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create file share

        Args:
          project_id: Project ID

          region_id: Region ID

          name: File share name

          network: File share network configuration

          protocol: File share protocol

          size: File share size

          access: Access Rules

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          volume_type: File share volume type

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
        volume_type: Literal["vast_share_type"],
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create file share

        Args:
          project_id: Project ID

          region_id: Region ID

          name: File share name

          protocol: File share protocol

          size: File share size

          volume_type: File share volume type

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
        ...

    @required_args(["name", "network", "protocol", "size"], ["name", "protocol", "size", "volume_type"])
    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        network: file_share_create_params.CreateStandardFileShareSerializerNetwork | NotGiven = NOT_GIVEN,
        protocol: Literal["NFS"],
        size: int,
        access: Iterable[file_share_create_params.CreateStandardFileShareSerializerAccess] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        volume_type: Literal["default_share_type"] | Literal["vast_share_type"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                    "volume_type": volume_type,
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
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileShare:
        """
        Rename file share

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          name: Name.

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
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}",
            body=maybe_transform({"name": name}, file_share_update_params.FileShareUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileShare,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        type_name: Literal["standard", "vast"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        access: Iterable[file_share_create_params.CreateStandardFileShareSerializerAccess] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        volume_type: Literal["default_share_type"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create file share

        Args:
          project_id: Project ID

          region_id: Region ID

          name: File share name

          network: File share network configuration

          protocol: File share protocol

          size: File share size

          access: Access Rules

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          volume_type: File share volume type

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
        volume_type: Literal["vast_share_type"],
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create file share

        Args:
          project_id: Project ID

          region_id: Region ID

          name: File share name

          protocol: File share protocol

          size: File share size

          volume_type: File share volume type

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
        ...

    @required_args(["name", "network", "protocol", "size"], ["name", "protocol", "size", "volume_type"])
    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        network: file_share_create_params.CreateStandardFileShareSerializerNetwork | NotGiven = NOT_GIVEN,
        protocol: Literal["NFS"],
        size: int,
        access: Iterable[file_share_create_params.CreateStandardFileShareSerializerAccess] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        volume_type: Literal["default_share_type"] | Literal["vast_share_type"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                    "volume_type": volume_type,
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
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileShare:
        """
        Rename file share

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          name: Name.

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
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}",
            body=await async_maybe_transform({"name": name}, file_share_update_params.FileShareUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileShare,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        type_name: Literal["standard", "vast"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

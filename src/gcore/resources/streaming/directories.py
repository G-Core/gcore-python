# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.streaming import directory_create_params, directory_update_params
from ...types.streaming.directory_base import DirectoryBase
from ...types.streaming.directories_tree import DirectoriesTree
from ...types.streaming.directory_get_response import DirectoryGetResponse

__all__ = ["DirectoriesResource", "AsyncDirectoriesResource"]


class DirectoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DirectoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return DirectoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirectoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return DirectoriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        parent_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryBase:
        """
        Use this method to create a new directory entity.

        Args:
          name: Title of the directory.

          parent_id: ID of a parent directory. "null" if it's in the root.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/streaming/directories",
            body=maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                },
                directory_create_params.DirectoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectoryBase,
        )

    def update(
        self,
        directory_id: int,
        *,
        name: str | Omit = omit,
        parent_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryBase:
        """
        Change a directory name or move to another "`parent_id`".

        Args:
          name: Title of the directory. Omit this if you don't want to change.

          parent_id: ID of a parent directory. "null" if it's in the root. Omit this if you don't
              want to change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/streaming/directories/{directory_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                },
                directory_update_params.DirectoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectoryBase,
        )

    def delete(
        self,
        directory_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a directory **and all entities inside**.

        After its execution, all contents of the directory will be deleted recursively:

        - Subdirectories
        - Videos

        The directory and contents are deleted permanently and irreversibly. Therefore,
        it is impossible to restore files after this.

        For details, see the Product Documentation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/streaming/directories/{directory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        directory_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryGetResponse:
        """Complete directory structure with contents.

        The structure contains both
        subfolders and videos in a continuous list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/directories/{directory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectoryGetResponse,
        )

    def get_tree(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoriesTree:
        """
        Tree structure of directories.

        This endpoint returns hierarchical data about directories in video hosting.
        """
        return self._get(
            "/streaming/directories/tree",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectoriesTree,
        )


class AsyncDirectoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDirectoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDirectoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirectoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncDirectoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        parent_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryBase:
        """
        Use this method to create a new directory entity.

        Args:
          name: Title of the directory.

          parent_id: ID of a parent directory. "null" if it's in the root.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/streaming/directories",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                },
                directory_create_params.DirectoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectoryBase,
        )

    async def update(
        self,
        directory_id: int,
        *,
        name: str | Omit = omit,
        parent_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryBase:
        """
        Change a directory name or move to another "`parent_id`".

        Args:
          name: Title of the directory. Omit this if you don't want to change.

          parent_id: ID of a parent directory. "null" if it's in the root. Omit this if you don't
              want to change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/streaming/directories/{directory_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                },
                directory_update_params.DirectoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectoryBase,
        )

    async def delete(
        self,
        directory_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a directory **and all entities inside**.

        After its execution, all contents of the directory will be deleted recursively:

        - Subdirectories
        - Videos

        The directory and contents are deleted permanently and irreversibly. Therefore,
        it is impossible to restore files after this.

        For details, see the Product Documentation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/streaming/directories/{directory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        directory_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryGetResponse:
        """Complete directory structure with contents.

        The structure contains both
        subfolders and videos in a continuous list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/directories/{directory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectoryGetResponse,
        )

    async def get_tree(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoriesTree:
        """
        Tree structure of directories.

        This endpoint returns hierarchical data about directories in video hosting.
        """
        return await self._get(
            "/streaming/directories/tree",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectoriesTree,
        )


class DirectoriesResourceWithRawResponse:
    def __init__(self, directories: DirectoriesResource) -> None:
        self._directories = directories

        self.create = to_raw_response_wrapper(
            directories.create,
        )
        self.update = to_raw_response_wrapper(
            directories.update,
        )
        self.delete = to_raw_response_wrapper(
            directories.delete,
        )
        self.get = to_raw_response_wrapper(
            directories.get,
        )
        self.get_tree = to_raw_response_wrapper(
            directories.get_tree,
        )


class AsyncDirectoriesResourceWithRawResponse:
    def __init__(self, directories: AsyncDirectoriesResource) -> None:
        self._directories = directories

        self.create = async_to_raw_response_wrapper(
            directories.create,
        )
        self.update = async_to_raw_response_wrapper(
            directories.update,
        )
        self.delete = async_to_raw_response_wrapper(
            directories.delete,
        )
        self.get = async_to_raw_response_wrapper(
            directories.get,
        )
        self.get_tree = async_to_raw_response_wrapper(
            directories.get_tree,
        )


class DirectoriesResourceWithStreamingResponse:
    def __init__(self, directories: DirectoriesResource) -> None:
        self._directories = directories

        self.create = to_streamed_response_wrapper(
            directories.create,
        )
        self.update = to_streamed_response_wrapper(
            directories.update,
        )
        self.delete = to_streamed_response_wrapper(
            directories.delete,
        )
        self.get = to_streamed_response_wrapper(
            directories.get,
        )
        self.get_tree = to_streamed_response_wrapper(
            directories.get_tree,
        )


class AsyncDirectoriesResourceWithStreamingResponse:
    def __init__(self, directories: AsyncDirectoriesResource) -> None:
        self._directories = directories

        self.create = async_to_streamed_response_wrapper(
            directories.create,
        )
        self.update = async_to_streamed_response_wrapper(
            directories.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            directories.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            directories.get,
        )
        self.get_tree = async_to_streamed_response_wrapper(
            directories.get_tree,
        )

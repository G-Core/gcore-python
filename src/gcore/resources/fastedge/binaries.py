# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import httpx

from ..._files import read_file_content, async_read_file_content
from ..._types import (
    Body,
    Query,
    Headers,
    NoneType,
    NotGiven,
    BinaryTypes,
    FileContent,
    AsyncBinaryTypes,
    not_given,
)
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.fastedge.binary import Binary
from ...types.fastedge.binary_short import BinaryShort
from ...types.fastedge.binary_list_response import BinaryListResponse

__all__ = ["BinariesResource", "AsyncBinariesResource"]


class BinariesResource(SyncAPIResource):
    """
    FastEdge binaries are immutable WebAssembly modules that implement edge application logic.
    """

    @cached_property
    def with_raw_response(self) -> BinariesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return BinariesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BinariesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return BinariesResourceWithStreamingResponse(self)

    def create(
        self,
        body: FileContent | BinaryTypes,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryShort:
        """Upload a compiled WebAssembly binary to the edge platform.

        The binary is
        automatically analyzed to detect its API type (WASI or Proxy-WASM) and stored
        for use in applications. Maximum binary size is 100MB.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            "/fastedge/v1/binaries/raw",
            content=read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryShort,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryListResponse:
        """Retrieve all WebAssembly binaries owned by the authenticated client.

        Binaries
        can be shared across multiple applications and include both WASI and Proxy-WASM
        formats.
        """
        return self._get(
            "/fastedge/v1/binaries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryListResponse,
        )

    def delete(
        self,
        binary_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a WebAssembly binary from the platform.

        Note: Binaries currently in use
        by applications cannot be deleted. Remove all application associations first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/fastedge/v1/binaries/{binary_id}", binary_id=binary_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        binary_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Binary:
        """
        Retrieve complete information about a specific WebAssembly binary including
        metadata and compiled content. Use this to download or inspect binaries before
        using them in applications.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/fastedge/v1/binaries/{binary_id}", binary_id=binary_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Binary,
        )


class AsyncBinariesResource(AsyncAPIResource):
    """
    FastEdge binaries are immutable WebAssembly modules that implement edge application logic.
    """

    @cached_property
    def with_raw_response(self) -> AsyncBinariesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBinariesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBinariesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncBinariesResourceWithStreamingResponse(self)

    async def create(
        self,
        body: FileContent | AsyncBinaryTypes,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryShort:
        """Upload a compiled WebAssembly binary to the edge platform.

        The binary is
        automatically analyzed to detect its API type (WASI or Proxy-WASM) and stored
        for use in applications. Maximum binary size is 100MB.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            "/fastedge/v1/binaries/raw",
            content=await async_read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryShort,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryListResponse:
        """Retrieve all WebAssembly binaries owned by the authenticated client.

        Binaries
        can be shared across multiple applications and include both WASI and Proxy-WASM
        formats.
        """
        return await self._get(
            "/fastedge/v1/binaries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryListResponse,
        )

    async def delete(
        self,
        binary_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a WebAssembly binary from the platform.

        Note: Binaries currently in use
        by applications cannot be deleted. Remove all application associations first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/fastedge/v1/binaries/{binary_id}", binary_id=binary_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        binary_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Binary:
        """
        Retrieve complete information about a specific WebAssembly binary including
        metadata and compiled content. Use this to download or inspect binaries before
        using them in applications.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/fastedge/v1/binaries/{binary_id}", binary_id=binary_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Binary,
        )


class BinariesResourceWithRawResponse:
    def __init__(self, binaries: BinariesResource) -> None:
        self._binaries = binaries

        self.create = to_raw_response_wrapper(
            binaries.create,
        )
        self.list = to_raw_response_wrapper(
            binaries.list,
        )
        self.delete = to_raw_response_wrapper(
            binaries.delete,
        )
        self.get = to_raw_response_wrapper(
            binaries.get,
        )


class AsyncBinariesResourceWithRawResponse:
    def __init__(self, binaries: AsyncBinariesResource) -> None:
        self._binaries = binaries

        self.create = async_to_raw_response_wrapper(
            binaries.create,
        )
        self.list = async_to_raw_response_wrapper(
            binaries.list,
        )
        self.delete = async_to_raw_response_wrapper(
            binaries.delete,
        )
        self.get = async_to_raw_response_wrapper(
            binaries.get,
        )


class BinariesResourceWithStreamingResponse:
    def __init__(self, binaries: BinariesResource) -> None:
        self._binaries = binaries

        self.create = to_streamed_response_wrapper(
            binaries.create,
        )
        self.list = to_streamed_response_wrapper(
            binaries.list,
        )
        self.delete = to_streamed_response_wrapper(
            binaries.delete,
        )
        self.get = to_streamed_response_wrapper(
            binaries.get,
        )


class AsyncBinariesResourceWithStreamingResponse:
    def __init__(self, binaries: AsyncBinariesResource) -> None:
        self._binaries = binaries

        self.create = async_to_streamed_response_wrapper(
            binaries.create,
        )
        self.list = async_to_streamed_response_wrapper(
            binaries.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            binaries.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            binaries.get,
        )

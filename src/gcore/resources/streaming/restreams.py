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
from ...pagination import SyncPageStreaming, AsyncPageStreaming
from ..._base_client import AsyncPaginator, make_request_options
from ...types.streaming import restream_list_params, restream_create_params, restream_update_params
from ...types.streaming.restream import Restream

__all__ = ["RestreamsResource", "AsyncRestreamsResource"]


class RestreamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RestreamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return RestreamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RestreamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return RestreamsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        restream: restream_create_params.Restream | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create restream

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/streaming/restreams",
            body=maybe_transform({"restream": restream}, restream_create_params.RestreamCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        restream_id: int,
        *,
        restream: restream_update_params.Restream | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Restream:
        """
        Updates restream settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/streaming/restreams/{restream_id}",
            body=maybe_transform({"restream": restream}, restream_update_params.RestreamUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Restream,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageStreaming[Restream]:
        """Returns a list of created restreams

        Args:
          page: Query parameter.

        Use it to list the paginated content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/restreams",
            page=SyncPageStreaming[Restream],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, restream_list_params.RestreamListParams),
            ),
            model=Restream,
        )

    def delete(
        self,
        restream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete restream

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/streaming/restreams/{restream_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        restream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Restream:
        """
        Returns restream details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/restreams/{restream_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Restream,
        )


class AsyncRestreamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRestreamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRestreamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRestreamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncRestreamsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        restream: restream_create_params.Restream | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create restream

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/streaming/restreams",
            body=await async_maybe_transform({"restream": restream}, restream_create_params.RestreamCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        restream_id: int,
        *,
        restream: restream_update_params.Restream | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Restream:
        """
        Updates restream settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/streaming/restreams/{restream_id}",
            body=await async_maybe_transform({"restream": restream}, restream_update_params.RestreamUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Restream,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Restream, AsyncPageStreaming[Restream]]:
        """Returns a list of created restreams

        Args:
          page: Query parameter.

        Use it to list the paginated content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/restreams",
            page=AsyncPageStreaming[Restream],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, restream_list_params.RestreamListParams),
            ),
            model=Restream,
        )

    async def delete(
        self,
        restream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete restream

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/streaming/restreams/{restream_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        restream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Restream:
        """
        Returns restream details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/restreams/{restream_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Restream,
        )


class RestreamsResourceWithRawResponse:
    def __init__(self, restreams: RestreamsResource) -> None:
        self._restreams = restreams

        self.create = to_raw_response_wrapper(
            restreams.create,
        )
        self.update = to_raw_response_wrapper(
            restreams.update,
        )
        self.list = to_raw_response_wrapper(
            restreams.list,
        )
        self.delete = to_raw_response_wrapper(
            restreams.delete,
        )
        self.get = to_raw_response_wrapper(
            restreams.get,
        )


class AsyncRestreamsResourceWithRawResponse:
    def __init__(self, restreams: AsyncRestreamsResource) -> None:
        self._restreams = restreams

        self.create = async_to_raw_response_wrapper(
            restreams.create,
        )
        self.update = async_to_raw_response_wrapper(
            restreams.update,
        )
        self.list = async_to_raw_response_wrapper(
            restreams.list,
        )
        self.delete = async_to_raw_response_wrapper(
            restreams.delete,
        )
        self.get = async_to_raw_response_wrapper(
            restreams.get,
        )


class RestreamsResourceWithStreamingResponse:
    def __init__(self, restreams: RestreamsResource) -> None:
        self._restreams = restreams

        self.create = to_streamed_response_wrapper(
            restreams.create,
        )
        self.update = to_streamed_response_wrapper(
            restreams.update,
        )
        self.list = to_streamed_response_wrapper(
            restreams.list,
        )
        self.delete = to_streamed_response_wrapper(
            restreams.delete,
        )
        self.get = to_streamed_response_wrapper(
            restreams.get,
        )


class AsyncRestreamsResourceWithStreamingResponse:
    def __init__(self, restreams: AsyncRestreamsResource) -> None:
        self._restreams = restreams

        self.create = async_to_streamed_response_wrapper(
            restreams.create,
        )
        self.update = async_to_streamed_response_wrapper(
            restreams.update,
        )
        self.list = async_to_streamed_response_wrapper(
            restreams.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            restreams.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            restreams.get,
        )

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
from ...types.streaming import broadcast_list_params, broadcast_create_params, broadcast_update_params
from ...types.streaming.broadcast import Broadcast
from ...types.streaming.broadcast_spectators_count import BroadcastSpectatorsCount

__all__ = ["BroadcastsResource", "AsyncBroadcastsResource"]


class BroadcastsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BroadcastsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return BroadcastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BroadcastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return BroadcastsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        broadcast: broadcast_create_params.Broadcast | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Broadcast entity is for setting up HTML video player, which serves to combine:

        - many live streams,
        - advertising,
        - and design in one config.

        If you use other players or you get streams by direct .m3u8/.mpd links, then you
        will not need this entity.

        Scheme of "broadcast" entity using:
        ![Scheme of "broadcast" using](https://demo-files.gvideo.io/apidocs/broadcasts.png)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/streaming/broadcasts",
            body=maybe_transform({"broadcast": broadcast}, broadcast_create_params.BroadcastCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        broadcast_id: int,
        *,
        broadcast: broadcast_update_params.Broadcast | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """
        Updates broadcast settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/streaming/broadcasts/{broadcast_id}",
            body=maybe_transform({"broadcast": broadcast}, broadcast_update_params.BroadcastUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
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
    ) -> SyncPageStreaming[Broadcast]:
        """
        Note: Feature "Broadcast" is outdated, soon it will be replaced by
        "Multicamera".

        Returns a list of broadcasts. Please see description in POST method.

        Args:
          page: Query parameter. Use it to list the paginated content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/broadcasts",
            page=SyncPageStreaming[Broadcast],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, broadcast_list_params.BroadcastListParams),
            ),
            model=Broadcast,
        )

    def delete(
        self,
        broadcast_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete broadcast

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/streaming/broadcasts/{broadcast_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        broadcast_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """
        Returns broadcast details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/broadcasts/{broadcast_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    def get_spectators_count(
        self,
        broadcast_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastSpectatorsCount:
        """
        Returns number of simultaneous broadcast viewers at the current moment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/broadcasts/{broadcast_id}/spectators",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastSpectatorsCount,
        )


class AsyncBroadcastsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBroadcastsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBroadcastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBroadcastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncBroadcastsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        broadcast: broadcast_create_params.Broadcast | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Broadcast entity is for setting up HTML video player, which serves to combine:

        - many live streams,
        - advertising,
        - and design in one config.

        If you use other players or you get streams by direct .m3u8/.mpd links, then you
        will not need this entity.

        Scheme of "broadcast" entity using:
        ![Scheme of "broadcast" using](https://demo-files.gvideo.io/apidocs/broadcasts.png)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/streaming/broadcasts",
            body=await async_maybe_transform({"broadcast": broadcast}, broadcast_create_params.BroadcastCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        broadcast_id: int,
        *,
        broadcast: broadcast_update_params.Broadcast | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """
        Updates broadcast settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/streaming/broadcasts/{broadcast_id}",
            body=await async_maybe_transform({"broadcast": broadcast}, broadcast_update_params.BroadcastUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
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
    ) -> AsyncPaginator[Broadcast, AsyncPageStreaming[Broadcast]]:
        """
        Note: Feature "Broadcast" is outdated, soon it will be replaced by
        "Multicamera".

        Returns a list of broadcasts. Please see description in POST method.

        Args:
          page: Query parameter. Use it to list the paginated content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/broadcasts",
            page=AsyncPageStreaming[Broadcast],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, broadcast_list_params.BroadcastListParams),
            ),
            model=Broadcast,
        )

    async def delete(
        self,
        broadcast_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete broadcast

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/streaming/broadcasts/{broadcast_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        broadcast_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """
        Returns broadcast details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/broadcasts/{broadcast_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    async def get_spectators_count(
        self,
        broadcast_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastSpectatorsCount:
        """
        Returns number of simultaneous broadcast viewers at the current moment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/broadcasts/{broadcast_id}/spectators",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastSpectatorsCount,
        )


class BroadcastsResourceWithRawResponse:
    def __init__(self, broadcasts: BroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = to_raw_response_wrapper(
            broadcasts.create,
        )
        self.update = to_raw_response_wrapper(
            broadcasts.update,
        )
        self.list = to_raw_response_wrapper(
            broadcasts.list,
        )
        self.delete = to_raw_response_wrapper(
            broadcasts.delete,
        )
        self.get = to_raw_response_wrapper(
            broadcasts.get,
        )
        self.get_spectators_count = to_raw_response_wrapper(
            broadcasts.get_spectators_count,
        )


class AsyncBroadcastsResourceWithRawResponse:
    def __init__(self, broadcasts: AsyncBroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = async_to_raw_response_wrapper(
            broadcasts.create,
        )
        self.update = async_to_raw_response_wrapper(
            broadcasts.update,
        )
        self.list = async_to_raw_response_wrapper(
            broadcasts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            broadcasts.delete,
        )
        self.get = async_to_raw_response_wrapper(
            broadcasts.get,
        )
        self.get_spectators_count = async_to_raw_response_wrapper(
            broadcasts.get_spectators_count,
        )


class BroadcastsResourceWithStreamingResponse:
    def __init__(self, broadcasts: BroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = to_streamed_response_wrapper(
            broadcasts.create,
        )
        self.update = to_streamed_response_wrapper(
            broadcasts.update,
        )
        self.list = to_streamed_response_wrapper(
            broadcasts.list,
        )
        self.delete = to_streamed_response_wrapper(
            broadcasts.delete,
        )
        self.get = to_streamed_response_wrapper(
            broadcasts.get,
        )
        self.get_spectators_count = to_streamed_response_wrapper(
            broadcasts.get_spectators_count,
        )


class AsyncBroadcastsResourceWithStreamingResponse:
    def __init__(self, broadcasts: AsyncBroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = async_to_streamed_response_wrapper(
            broadcasts.create,
        )
        self.update = async_to_streamed_response_wrapper(
            broadcasts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            broadcasts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            broadcasts.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            broadcasts.get,
        )
        self.get_spectators_count = async_to_streamed_response_wrapper(
            broadcasts.get_spectators_count,
        )

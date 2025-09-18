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
from ...types.streaming import Player, player_list_params, player_create_params, player_update_params
from ...types.streaming.player import Player
from ...types.streaming.player_param import PlayerParam

__all__ = ["PlayersResource", "AsyncPlayersResource"]


class PlayersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlayersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PlayersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlayersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PlayersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        player: PlayerParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Create player

        Args:
          player: Set of properties for displaying videos.

        All parameters may be blank to inherit
              their values from default Streaming player.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/streaming/players",
            body=maybe_transform({"player": player}, player_create_params.PlayerCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        player_id: int,
        *,
        player: PlayerParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Player:
        """Updates player settings

        Args:
          player: Set of properties for displaying videos.

        All parameters may be blank to inherit
              their values from default Streaming player.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/streaming/players/{player_id}",
            body=maybe_transform({"player": player}, player_update_params.PlayerUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Player,
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
    ) -> SyncPageStreaming[Player]:
        """Returns a list of created players

        Args:
          page: Query parameter.

        Use it to list the paginated content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/players",
            page=SyncPageStreaming[Player],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, player_list_params.PlayerListParams),
            ),
            model=Player,
        )

    def delete(
        self,
        player_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete player

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/streaming/players/{player_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        player_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Player:
        """
        Returns player settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/players/{player_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Player,
        )

    def preview(
        self,
        player_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns player configuration in HTML

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/streaming/players/{player_id}/preview",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPlayersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlayersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlayersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlayersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPlayersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        player: PlayerParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Create player

        Args:
          player: Set of properties for displaying videos.

        All parameters may be blank to inherit
              their values from default Streaming player.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/streaming/players",
            body=await async_maybe_transform({"player": player}, player_create_params.PlayerCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        player_id: int,
        *,
        player: PlayerParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Player:
        """Updates player settings

        Args:
          player: Set of properties for displaying videos.

        All parameters may be blank to inherit
              their values from default Streaming player.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/streaming/players/{player_id}",
            body=await async_maybe_transform({"player": player}, player_update_params.PlayerUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Player,
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
    ) -> AsyncPaginator[Player, AsyncPageStreaming[Player]]:
        """Returns a list of created players

        Args:
          page: Query parameter.

        Use it to list the paginated content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/players",
            page=AsyncPageStreaming[Player],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, player_list_params.PlayerListParams),
            ),
            model=Player,
        )

    async def delete(
        self,
        player_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete player

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/streaming/players/{player_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        player_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Player:
        """
        Returns player settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/players/{player_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Player,
        )

    async def preview(
        self,
        player_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns player configuration in HTML

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/streaming/players/{player_id}/preview",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PlayersResourceWithRawResponse:
    def __init__(self, players: PlayersResource) -> None:
        self._players = players

        self.create = to_raw_response_wrapper(
            players.create,
        )
        self.update = to_raw_response_wrapper(
            players.update,
        )
        self.list = to_raw_response_wrapper(
            players.list,
        )
        self.delete = to_raw_response_wrapper(
            players.delete,
        )
        self.get = to_raw_response_wrapper(
            players.get,
        )
        self.preview = to_raw_response_wrapper(
            players.preview,
        )


class AsyncPlayersResourceWithRawResponse:
    def __init__(self, players: AsyncPlayersResource) -> None:
        self._players = players

        self.create = async_to_raw_response_wrapper(
            players.create,
        )
        self.update = async_to_raw_response_wrapper(
            players.update,
        )
        self.list = async_to_raw_response_wrapper(
            players.list,
        )
        self.delete = async_to_raw_response_wrapper(
            players.delete,
        )
        self.get = async_to_raw_response_wrapper(
            players.get,
        )
        self.preview = async_to_raw_response_wrapper(
            players.preview,
        )


class PlayersResourceWithStreamingResponse:
    def __init__(self, players: PlayersResource) -> None:
        self._players = players

        self.create = to_streamed_response_wrapper(
            players.create,
        )
        self.update = to_streamed_response_wrapper(
            players.update,
        )
        self.list = to_streamed_response_wrapper(
            players.list,
        )
        self.delete = to_streamed_response_wrapper(
            players.delete,
        )
        self.get = to_streamed_response_wrapper(
            players.get,
        )
        self.preview = to_streamed_response_wrapper(
            players.preview,
        )


class AsyncPlayersResourceWithStreamingResponse:
    def __init__(self, players: AsyncPlayersResource) -> None:
        self._players = players

        self.create = async_to_streamed_response_wrapper(
            players.create,
        )
        self.update = async_to_streamed_response_wrapper(
            players.update,
        )
        self.list = async_to_streamed_response_wrapper(
            players.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            players.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            players.get,
        )
        self.preview = async_to_streamed_response_wrapper(
            players.preview,
        )

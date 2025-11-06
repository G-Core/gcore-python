# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.security import bgp_announce_list_params, bgp_announce_toggle_params
from ...types.security.bgp_announce_list_response import BgpAnnounceListResponse

__all__ = ["BgpAnnouncesResource", "AsyncBgpAnnouncesResource"]


class BgpAnnouncesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BgpAnnouncesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return BgpAnnouncesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BgpAnnouncesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return BgpAnnouncesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        announced: Optional[bool] | Omit = omit,
        origin: Optional[Literal["STATIC", "DYNAMIC"]] | Omit = omit,
        site: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BgpAnnounceListResponse:
        """Get BGP announces filtered by parameters.

        Shows announces in active profiles,
        meaning that to get a non-empty response, the client must have at least one
        active profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/security/sifter/v2/protected_addresses/announces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "announced": announced,
                        "origin": origin,
                        "site": site,
                    },
                    bgp_announce_list_params.BgpAnnounceListParams,
                ),
            ),
            cast_to=BgpAnnounceListResponse,
        )

    def toggle(
        self,
        *,
        announce: str,
        enabled: bool,
        client_id: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Change BGP announces (it can be enabled or disabled, but not created or
        updated).

        Can be applied to already existing announces in active profiles,
        meaning that the client must have at least one active profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/security/sifter/v2/protected_addresses/announces",
            body=maybe_transform(
                {
                    "announce": announce,
                    "enabled": enabled,
                },
                bgp_announce_toggle_params.BgpAnnounceToggleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"client_id": client_id}, bgp_announce_toggle_params.BgpAnnounceToggleParams),
            ),
            cast_to=object,
        )


class AsyncBgpAnnouncesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBgpAnnouncesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBgpAnnouncesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBgpAnnouncesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncBgpAnnouncesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        announced: Optional[bool] | Omit = omit,
        origin: Optional[Literal["STATIC", "DYNAMIC"]] | Omit = omit,
        site: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BgpAnnounceListResponse:
        """Get BGP announces filtered by parameters.

        Shows announces in active profiles,
        meaning that to get a non-empty response, the client must have at least one
        active profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/security/sifter/v2/protected_addresses/announces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "announced": announced,
                        "origin": origin,
                        "site": site,
                    },
                    bgp_announce_list_params.BgpAnnounceListParams,
                ),
            ),
            cast_to=BgpAnnounceListResponse,
        )

    async def toggle(
        self,
        *,
        announce: str,
        enabled: bool,
        client_id: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Change BGP announces (it can be enabled or disabled, but not created or
        updated).

        Can be applied to already existing announces in active profiles,
        meaning that the client must have at least one active profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/security/sifter/v2/protected_addresses/announces",
            body=await async_maybe_transform(
                {
                    "announce": announce,
                    "enabled": enabled,
                },
                bgp_announce_toggle_params.BgpAnnounceToggleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"client_id": client_id}, bgp_announce_toggle_params.BgpAnnounceToggleParams
                ),
            ),
            cast_to=object,
        )


class BgpAnnouncesResourceWithRawResponse:
    def __init__(self, bgp_announces: BgpAnnouncesResource) -> None:
        self._bgp_announces = bgp_announces

        self.list = to_raw_response_wrapper(
            bgp_announces.list,
        )
        self.toggle = to_raw_response_wrapper(
            bgp_announces.toggle,
        )


class AsyncBgpAnnouncesResourceWithRawResponse:
    def __init__(self, bgp_announces: AsyncBgpAnnouncesResource) -> None:
        self._bgp_announces = bgp_announces

        self.list = async_to_raw_response_wrapper(
            bgp_announces.list,
        )
        self.toggle = async_to_raw_response_wrapper(
            bgp_announces.toggle,
        )


class BgpAnnouncesResourceWithStreamingResponse:
    def __init__(self, bgp_announces: BgpAnnouncesResource) -> None:
        self._bgp_announces = bgp_announces

        self.list = to_streamed_response_wrapper(
            bgp_announces.list,
        )
        self.toggle = to_streamed_response_wrapper(
            bgp_announces.toggle,
        )


class AsyncBgpAnnouncesResourceWithStreamingResponse:
    def __init__(self, bgp_announces: AsyncBgpAnnouncesResource) -> None:
        self._bgp_announces = bgp_announces

        self.list = async_to_streamed_response_wrapper(
            bgp_announces.list,
        )
        self.toggle = async_to_streamed_response_wrapper(
            bgp_announces.toggle,
        )

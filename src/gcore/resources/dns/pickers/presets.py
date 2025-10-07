# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.dns.pickers.preset_list_response import PresetListResponse

__all__ = ["PresetsResource", "AsyncPresetsResource"]


class PresetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PresetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PresetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PresetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PresetsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetListResponse:
        """Returns list of picker preset"""
        return self._get(
            "/dns/v2/pickers/presets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresetListResponse,
        )


class AsyncPresetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPresetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPresetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPresetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPresetsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetListResponse:
        """Returns list of picker preset"""
        return await self._get(
            "/dns/v2/pickers/presets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresetListResponse,
        )


class PresetsResourceWithRawResponse:
    def __init__(self, presets: PresetsResource) -> None:
        self._presets = presets

        self.list = to_raw_response_wrapper(
            presets.list,
        )


class AsyncPresetsResourceWithRawResponse:
    def __init__(self, presets: AsyncPresetsResource) -> None:
        self._presets = presets

        self.list = async_to_raw_response_wrapper(
            presets.list,
        )


class PresetsResourceWithStreamingResponse:
    def __init__(self, presets: PresetsResource) -> None:
        self._presets = presets

        self.list = to_streamed_response_wrapper(
            presets.list,
        )


class AsyncPresetsResourceWithStreamingResponse:
    def __init__(self, presets: AsyncPresetsResource) -> None:
        self._presets = presets

        self.list = async_to_streamed_response_wrapper(
            presets.list,
        )

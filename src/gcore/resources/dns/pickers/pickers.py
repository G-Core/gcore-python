# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .presets import (
    PresetsResource,
    AsyncPresetsResource,
    PresetsResourceWithRawResponse,
    AsyncPresetsResourceWithRawResponse,
    PresetsResourceWithStreamingResponse,
    AsyncPresetsResourceWithStreamingResponse,
)
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
from ....types.dns.picker_list_response import PickerListResponse

__all__ = ["PickersResource", "AsyncPickersResource"]


class PickersResource(SyncAPIResource):
    @cached_property
    def presets(self) -> PresetsResource:
        return PresetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PickersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PickersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PickersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PickersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PickerListResponse:
        """Returns list of picker"""
        return self._get(
            "/dns/v2/pickers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PickerListResponse,
        )


class AsyncPickersResource(AsyncAPIResource):
    @cached_property
    def presets(self) -> AsyncPresetsResource:
        return AsyncPresetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPickersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPickersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPickersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPickersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PickerListResponse:
        """Returns list of picker"""
        return await self._get(
            "/dns/v2/pickers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PickerListResponse,
        )


class PickersResourceWithRawResponse:
    def __init__(self, pickers: PickersResource) -> None:
        self._pickers = pickers

        self.list = to_raw_response_wrapper(
            pickers.list,
        )

    @cached_property
    def presets(self) -> PresetsResourceWithRawResponse:
        return PresetsResourceWithRawResponse(self._pickers.presets)


class AsyncPickersResourceWithRawResponse:
    def __init__(self, pickers: AsyncPickersResource) -> None:
        self._pickers = pickers

        self.list = async_to_raw_response_wrapper(
            pickers.list,
        )

    @cached_property
    def presets(self) -> AsyncPresetsResourceWithRawResponse:
        return AsyncPresetsResourceWithRawResponse(self._pickers.presets)


class PickersResourceWithStreamingResponse:
    def __init__(self, pickers: PickersResource) -> None:
        self._pickers = pickers

        self.list = to_streamed_response_wrapper(
            pickers.list,
        )

    @cached_property
    def presets(self) -> PresetsResourceWithStreamingResponse:
        return PresetsResourceWithStreamingResponse(self._pickers.presets)


class AsyncPickersResourceWithStreamingResponse:
    def __init__(self, pickers: AsyncPickersResource) -> None:
        self._pickers = pickers

        self.list = async_to_streamed_response_wrapper(
            pickers.list,
        )

    @cached_property
    def presets(self) -> AsyncPresetsResourceWithStreamingResponse:
        return AsyncPresetsResourceWithStreamingResponse(self._pickers.presets)

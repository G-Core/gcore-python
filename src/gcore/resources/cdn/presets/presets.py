# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .applied import (
    AppliedResource,
    AsyncAppliedResource,
    AppliedResourceWithRawResponse,
    AsyncAppliedResourceWithRawResponse,
    AppliedResourceWithStreamingResponse,
    AsyncAppliedResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.cdn import preset_list_params
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cdn.preset_detail import PresetDetail

__all__ = ["PresetsResource", "AsyncPresetsResource"]


class PresetsResource(SyncAPIResource):
    """
    CDN presets are predefined sets of CDN resource or rule settings that can be applied to an object in a single request, letting you configure caching, delivery, and security options consistently.
    """

    @cached_property
    def applied(self) -> AppliedResource:
        """
        Applied presets represent the association between a preset and a CDN resource or rule. Use them to apply a preset to an object, list the objects a preset is applied to, unapply it, and inspect which object fields a preset manages.
        """
        return AppliedResource(self._client)

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
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[PresetDetail]:
        """
        Get the list of presets available to your account.

        A preset is a predefined set of CDN resource or rule settings that can be
        applied to an object in one request.

        Args:
          limit: Maximum number of items to return in the response. Cannot exceed 1000.

          offset: Number of items to skip from the beginning of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cdn/presets",
            page=SyncOffsetPage[PresetDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    preset_list_params.PresetListParams,
                ),
            ),
            model=PresetDetail,
        )

    def get(
        self,
        preset_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetDetail:
        """
        Get information about a preset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/cdn/presets/{preset_id}", preset_id=preset_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresetDetail,
        )


class AsyncPresetsResource(AsyncAPIResource):
    """
    CDN presets are predefined sets of CDN resource or rule settings that can be applied to an object in a single request, letting you configure caching, delivery, and security options consistently.
    """

    @cached_property
    def applied(self) -> AsyncAppliedResource:
        """
        Applied presets represent the association between a preset and a CDN resource or rule. Use them to apply a preset to an object, list the objects a preset is applied to, unapply it, and inspect which object fields a preset manages.
        """
        return AsyncAppliedResource(self._client)

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

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PresetDetail, AsyncOffsetPage[PresetDetail]]:
        """
        Get the list of presets available to your account.

        A preset is a predefined set of CDN resource or rule settings that can be
        applied to an object in one request.

        Args:
          limit: Maximum number of items to return in the response. Cannot exceed 1000.

          offset: Number of items to skip from the beginning of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cdn/presets",
            page=AsyncOffsetPage[PresetDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    preset_list_params.PresetListParams,
                ),
            ),
            model=PresetDetail,
        )

    async def get(
        self,
        preset_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetDetail:
        """
        Get information about a preset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/cdn/presets/{preset_id}", preset_id=preset_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresetDetail,
        )


class PresetsResourceWithRawResponse:
    def __init__(self, presets: PresetsResource) -> None:
        self._presets = presets

        self.list = to_raw_response_wrapper(
            presets.list,
        )
        self.get = to_raw_response_wrapper(
            presets.get,
        )

    @cached_property
    def applied(self) -> AppliedResourceWithRawResponse:
        """
        Applied presets represent the association between a preset and a CDN resource or rule. Use them to apply a preset to an object, list the objects a preset is applied to, unapply it, and inspect which object fields a preset manages.
        """
        return AppliedResourceWithRawResponse(self._presets.applied)


class AsyncPresetsResourceWithRawResponse:
    def __init__(self, presets: AsyncPresetsResource) -> None:
        self._presets = presets

        self.list = async_to_raw_response_wrapper(
            presets.list,
        )
        self.get = async_to_raw_response_wrapper(
            presets.get,
        )

    @cached_property
    def applied(self) -> AsyncAppliedResourceWithRawResponse:
        """
        Applied presets represent the association between a preset and a CDN resource or rule. Use them to apply a preset to an object, list the objects a preset is applied to, unapply it, and inspect which object fields a preset manages.
        """
        return AsyncAppliedResourceWithRawResponse(self._presets.applied)


class PresetsResourceWithStreamingResponse:
    def __init__(self, presets: PresetsResource) -> None:
        self._presets = presets

        self.list = to_streamed_response_wrapper(
            presets.list,
        )
        self.get = to_streamed_response_wrapper(
            presets.get,
        )

    @cached_property
    def applied(self) -> AppliedResourceWithStreamingResponse:
        """
        Applied presets represent the association between a preset and a CDN resource or rule. Use them to apply a preset to an object, list the objects a preset is applied to, unapply it, and inspect which object fields a preset manages.
        """
        return AppliedResourceWithStreamingResponse(self._presets.applied)


class AsyncPresetsResourceWithStreamingResponse:
    def __init__(self, presets: AsyncPresetsResource) -> None:
        self._presets = presets

        self.list = async_to_streamed_response_wrapper(
            presets.list,
        )
        self.get = async_to_streamed_response_wrapper(
            presets.get,
        )

    @cached_property
    def applied(self) -> AsyncAppliedResourceWithStreamingResponse:
        """
        Applied presets represent the association between a preset and a CDN resource or rule. Use them to apply a preset to an object, list the objects a preset is applied to, unapply it, and inspect which object fields a preset manages.
        """
        return AsyncAppliedResourceWithStreamingResponse(self._presets.applied)

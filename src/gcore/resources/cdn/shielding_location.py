# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cdn import shielding_location_list_params
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cdn.shielding_location import ShieldingLocation

__all__ = ["ShieldingLocationResource", "AsyncShieldingLocationResource"]


class ShieldingLocationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShieldingLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ShieldingLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShieldingLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ShieldingLocationResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = 1000,  # CDN API only envelopes when limit>=1; default so list() always paginates
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[ShieldingLocation]:
        """
        Get information about all origin shielding locations available in the account.

        Args:
          limit: Maximum number of items to return in the response. Cannot exceed 1000.

          offset: Number of items to skip from the beginning of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cdn/shieldingpop_v2",
            page=SyncOffsetPage[ShieldingLocation],
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
                    shielding_location_list_params.ShieldingLocationListParams,
                ),
            ),
            model=ShieldingLocation,
        )


class AsyncShieldingLocationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShieldingLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncShieldingLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShieldingLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncShieldingLocationResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = 1000,  # CDN API only envelopes when limit>=1; default so list() always paginates
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ShieldingLocation, AsyncOffsetPage[ShieldingLocation]]:
        """
        Get information about all origin shielding locations available in the account.

        Args:
          limit: Maximum number of items to return in the response. Cannot exceed 1000.

          offset: Number of items to skip from the beginning of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cdn/shieldingpop_v2",
            page=AsyncOffsetPage[ShieldingLocation],
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
                    shielding_location_list_params.ShieldingLocationListParams,
                ),
            ),
            model=ShieldingLocation,
        )


class ShieldingLocationResourceWithRawResponse:
    def __init__(self, shielding_location: ShieldingLocationResource) -> None:
        self._shielding_location = shielding_location

        self.list = to_raw_response_wrapper(
            shielding_location.list,
        )


class AsyncShieldingLocationResourceWithRawResponse:
    def __init__(self, shielding_location: AsyncShieldingLocationResource) -> None:
        self._shielding_location = shielding_location

        self.list = async_to_raw_response_wrapper(
            shielding_location.list,
        )


class ShieldingLocationResourceWithStreamingResponse:
    def __init__(self, shielding_location: ShieldingLocationResource) -> None:
        self._shielding_location = shielding_location

        self.list = to_streamed_response_wrapper(
            shielding_location.list,
        )


class AsyncShieldingLocationResourceWithStreamingResponse:
    def __init__(self, shielding_location: AsyncShieldingLocationResource) -> None:
        self._shielding_location = shielding_location

        self.list = async_to_streamed_response_wrapper(
            shielding_location.list,
        )

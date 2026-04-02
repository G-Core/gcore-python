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
from ...types.cdn import shield_list_params
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cdn.shield_list_response import ShieldListResponse

__all__ = ["ShieldsResource", "AsyncShieldsResource"]


class ShieldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ShieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ShieldsResourceWithStreamingResponse(self)

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
    ) -> SyncOffsetPage[ShieldListResponse]:
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
            page=SyncOffsetPage[ShieldListResponse],
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
                    shield_list_params.ShieldListParams,
                ),
            ),
            model=ShieldListResponse,
        )


class AsyncShieldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncShieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncShieldsResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[ShieldListResponse, AsyncOffsetPage[ShieldListResponse]]:
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
            page=AsyncOffsetPage[ShieldListResponse],
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
                    shield_list_params.ShieldListParams,
                ),
            ),
            model=ShieldListResponse,
        )


class ShieldsResourceWithRawResponse:
    def __init__(self, shields: ShieldsResource) -> None:
        self._shields = shields

        self.list = to_raw_response_wrapper(
            shields.list,
        )


class AsyncShieldsResourceWithRawResponse:
    def __init__(self, shields: AsyncShieldsResource) -> None:
        self._shields = shields

        self.list = async_to_raw_response_wrapper(
            shields.list,
        )


class ShieldsResourceWithStreamingResponse:
    def __init__(self, shields: ShieldsResource) -> None:
        self._shields = shields

        self.list = to_streamed_response_wrapper(
            shields.list,
        )


class AsyncShieldsResourceWithStreamingResponse:
    def __init__(self, shields: AsyncShieldsResource) -> None:
        self._shields = shields

        self.list = async_to_streamed_response_wrapper(
            shields.list,
        )

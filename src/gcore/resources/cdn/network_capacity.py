# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.cdn.network_capacity import NetworkCapacity

__all__ = ["NetworkCapacityResource", "AsyncNetworkCapacityResource"]


class NetworkCapacityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NetworkCapacityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return NetworkCapacityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworkCapacityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return NetworkCapacityResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkCapacity:
        """Get network capacity per country."""
        return self._get(
            "/cdn/advanced/v1/capacity",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkCapacity,
        )


class AsyncNetworkCapacityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNetworkCapacityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworkCapacityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworkCapacityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncNetworkCapacityResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkCapacity:
        """Get network capacity per country."""
        return await self._get(
            "/cdn/advanced/v1/capacity",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkCapacity,
        )


class NetworkCapacityResourceWithRawResponse:
    def __init__(self, network_capacity: NetworkCapacityResource) -> None:
        self._network_capacity = network_capacity

        self.list = to_raw_response_wrapper(
            network_capacity.list,
        )


class AsyncNetworkCapacityResourceWithRawResponse:
    def __init__(self, network_capacity: AsyncNetworkCapacityResource) -> None:
        self._network_capacity = network_capacity

        self.list = async_to_raw_response_wrapper(
            network_capacity.list,
        )


class NetworkCapacityResourceWithStreamingResponse:
    def __init__(self, network_capacity: NetworkCapacityResource) -> None:
        self._network_capacity = network_capacity

        self.list = to_streamed_response_wrapper(
            network_capacity.list,
        )


class AsyncNetworkCapacityResourceWithStreamingResponse:
    def __init__(self, network_capacity: AsyncNetworkCapacityResource) -> None:
        self._network_capacity = network_capacity

        self.list = async_to_streamed_response_wrapper(
            network_capacity.list,
        )

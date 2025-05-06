# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.cloud.ip_ranges import IPRanges

__all__ = ["IPRangesResource", "AsyncIPRangesResource"]


class IPRangesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPRangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return IPRangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPRangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return IPRangesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPRanges:
        """List of all Edge Cloud Egress Public IPs."""
        return self._get(
            "/cloud/public/v1/ipranges/egress",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRanges,
        )


class AsyncIPRangesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPRangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPRangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPRangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncIPRangesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPRanges:
        """List of all Edge Cloud Egress Public IPs."""
        return await self._get(
            "/cloud/public/v1/ipranges/egress",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRanges,
        )


class IPRangesResourceWithRawResponse:
    def __init__(self, ip_ranges: IPRangesResource) -> None:
        self._ip_ranges = ip_ranges

        self.list = to_raw_response_wrapper(
            ip_ranges.list,
        )


class AsyncIPRangesResourceWithRawResponse:
    def __init__(self, ip_ranges: AsyncIPRangesResource) -> None:
        self._ip_ranges = ip_ranges

        self.list = async_to_raw_response_wrapper(
            ip_ranges.list,
        )


class IPRangesResourceWithStreamingResponse:
    def __init__(self, ip_ranges: IPRangesResource) -> None:
        self._ip_ranges = ip_ranges

        self.list = to_streamed_response_wrapper(
            ip_ranges.list,
        )


class AsyncIPRangesResourceWithStreamingResponse:
    def __init__(self, ip_ranges: AsyncIPRangesResource) -> None:
        self._ip_ranges = ip_ranges

        self.list = async_to_streamed_response_wrapper(
            ip_ranges.list,
        )

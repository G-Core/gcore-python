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
from ...types.cdn.public_ip_list import PublicIPList
from ...types.cdn.public_network_list import PublicNetworkList

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicNetworkList:
        """
        Get all CDN networks that can be used to pull content from your origin.

        This list is updated periodically. If you want to use network from this list to
        configure IP ACL on your origin, you need to independently monitor its
        relevance. We recommend using a script for automatically update IP ACL.

        This request does not require authorization.
        """
        return self._get(
            "/cdn/public-net-list"
            if self._client._base_url_overridden
            else "https://api.gcore.com//cdn/public-net-list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicNetworkList,
        )

    def list_ips(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicIPList:
        """
        Get all IP addresses of CDN servers that can be used to pull content from your
        origin.

        This list is updated periodically. If you want to use IP from this list to
        configure IP ACL in your origin, you need to independently monitor its
        relevance. We recommend using a script to automatically update IP ACL.

        This request does not require authorization.
        """
        return self._get(
            "/cdn/public-ip-list" if self._client._base_url_overridden else "https://api.gcore.com//cdn/public-ip-list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicIPList,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicNetworkList:
        """
        Get all CDN networks that can be used to pull content from your origin.

        This list is updated periodically. If you want to use network from this list to
        configure IP ACL on your origin, you need to independently monitor its
        relevance. We recommend using a script for automatically update IP ACL.

        This request does not require authorization.
        """
        return await self._get(
            "/cdn/public-net-list"
            if self._client._base_url_overridden
            else "https://api.gcore.com//cdn/public-net-list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicNetworkList,
        )

    async def list_ips(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicIPList:
        """
        Get all IP addresses of CDN servers that can be used to pull content from your
        origin.

        This list is updated periodically. If you want to use IP from this list to
        configure IP ACL in your origin, you need to independently monitor its
        relevance. We recommend using a script to automatically update IP ACL.

        This request does not require authorization.
        """
        return await self._get(
            "/cdn/public-ip-list" if self._client._base_url_overridden else "https://api.gcore.com//cdn/public-ip-list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicIPList,
        )


class IPRangesResourceWithRawResponse:
    def __init__(self, ip_ranges: IPRangesResource) -> None:
        self._ip_ranges = ip_ranges

        self.list = to_raw_response_wrapper(
            ip_ranges.list,
        )
        self.list_ips = to_raw_response_wrapper(
            ip_ranges.list_ips,
        )


class AsyncIPRangesResourceWithRawResponse:
    def __init__(self, ip_ranges: AsyncIPRangesResource) -> None:
        self._ip_ranges = ip_ranges

        self.list = async_to_raw_response_wrapper(
            ip_ranges.list,
        )
        self.list_ips = async_to_raw_response_wrapper(
            ip_ranges.list_ips,
        )


class IPRangesResourceWithStreamingResponse:
    def __init__(self, ip_ranges: IPRangesResource) -> None:
        self._ip_ranges = ip_ranges

        self.list = to_streamed_response_wrapper(
            ip_ranges.list,
        )
        self.list_ips = to_streamed_response_wrapper(
            ip_ranges.list_ips,
        )


class AsyncIPRangesResourceWithStreamingResponse:
    def __init__(self, ip_ranges: AsyncIPRangesResource) -> None:
        self._ip_ranges = ip_ranges

        self.list = async_to_streamed_response_wrapper(
            ip_ranges.list,
        )
        self.list_ips = async_to_streamed_response_wrapper(
            ip_ranges.list_ips,
        )

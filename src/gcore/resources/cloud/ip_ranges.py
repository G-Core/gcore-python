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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPRanges:
        """
        Returns the complete list of IPv4 and IPv6 address ranges that Cloud uses for
        outbound (egress) traffic.

        Typical reasons to call this endpoint:

        - Host-file delivery workflows – You upload images or other assets to the Cloud
          and share a download link that points to your own infrastructure. Add these
          egress prefixes to your firewall or object-storage allow-list so our clients
          can fetch the files without being blocked.
        - Push integrations / webhooks – You subscribe to the user-actions event log and
          Cloud pushes events to your listener endpoint. Whitelisting the egress IP
          ranges lets you accept only traffic that originates from us.
        - General security controls, audit tooling, or SIEM rules that need to verify
          that traffic truly comes from the Cloud.

        The list is global (covers all regions) and refreshed automatically whenever
        Gcore allocates new egress IP space. The response is an array of CIDR blocks;
        duplicate prefixes are not returned.
        """
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPRanges:
        """
        Returns the complete list of IPv4 and IPv6 address ranges that Cloud uses for
        outbound (egress) traffic.

        Typical reasons to call this endpoint:

        - Host-file delivery workflows – You upload images or other assets to the Cloud
          and share a download link that points to your own infrastructure. Add these
          egress prefixes to your firewall or object-storage allow-list so our clients
          can fetch the files without being blocked.
        - Push integrations / webhooks – You subscribe to the user-actions event log and
          Cloud pushes events to your listener endpoint. Whitelisting the egress IP
          ranges lets you accept only traffic that originates from us.
        - General security controls, audit tooling, or SIEM rules that need to verify
          that traffic truly comes from the Cloud.

        The list is global (covers all regions) and refreshed automatically whenever
        Gcore allocates new egress IP space. The response is an array of CIDR blocks;
        duplicate prefixes are not returned.
        """
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

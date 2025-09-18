# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.dns.zones import dnssec_update_params
from ....types.dns.zones.dnssec_get_response import DnssecGetResponse
from ....types.dns.zones.dnssec_update_response import DnssecUpdateResponse

__all__ = ["DnssecResource", "AsyncDnssecResource"]


class DnssecResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DnssecResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return DnssecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DnssecResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return DnssecResourceWithStreamingResponse(self)

    def update(
        self,
        name: str,
        *,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DnssecUpdateResponse:
        """
        Enable or disable DNSSEC for a DNS zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._patch(
            f"/dns/v2/zones/{name}/dnssec",
            body=maybe_transform({"enabled": enabled}, dnssec_update_params.DnssecUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DnssecUpdateResponse,
        )

    def get(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DnssecGetResponse:
        """
        Get DNSSEC DS for a DNS zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/dns/v2/zones/{name}/dnssec",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DnssecGetResponse,
        )


class AsyncDnssecResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDnssecResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDnssecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDnssecResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncDnssecResourceWithStreamingResponse(self)

    async def update(
        self,
        name: str,
        *,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DnssecUpdateResponse:
        """
        Enable or disable DNSSEC for a DNS zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._patch(
            f"/dns/v2/zones/{name}/dnssec",
            body=await async_maybe_transform({"enabled": enabled}, dnssec_update_params.DnssecUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DnssecUpdateResponse,
        )

    async def get(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DnssecGetResponse:
        """
        Get DNSSEC DS for a DNS zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/dns/v2/zones/{name}/dnssec",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DnssecGetResponse,
        )


class DnssecResourceWithRawResponse:
    def __init__(self, dnssec: DnssecResource) -> None:
        self._dnssec = dnssec

        self.update = to_raw_response_wrapper(
            dnssec.update,
        )
        self.get = to_raw_response_wrapper(
            dnssec.get,
        )


class AsyncDnssecResourceWithRawResponse:
    def __init__(self, dnssec: AsyncDnssecResource) -> None:
        self._dnssec = dnssec

        self.update = async_to_raw_response_wrapper(
            dnssec.update,
        )
        self.get = async_to_raw_response_wrapper(
            dnssec.get,
        )


class DnssecResourceWithStreamingResponse:
    def __init__(self, dnssec: DnssecResource) -> None:
        self._dnssec = dnssec

        self.update = to_streamed_response_wrapper(
            dnssec.update,
        )
        self.get = to_streamed_response_wrapper(
            dnssec.get,
        )


class AsyncDnssecResourceWithStreamingResponse:
    def __init__(self, dnssec: AsyncDnssecResource) -> None:
        self._dnssec = dnssec

        self.update = async_to_streamed_response_wrapper(
            dnssec.update,
        )
        self.get = async_to_streamed_response_wrapper(
            dnssec.get,
        )

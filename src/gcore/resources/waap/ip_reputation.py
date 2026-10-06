# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.waap import ip_reputation_list_params, ip_reputation_clear_local_tags_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.waap.waap_local_ip_tags_record import WaapLocalIPTagsRecord
from ...types.waap.waap_clear_local_tags_response import WaapClearLocalTagsResponse

__all__ = ["IPReputationResource", "AsyncIPReputationResource"]


class IPReputationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPReputationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return IPReputationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPReputationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return IPReputationResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        ip: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal["date", "-date", "domain_name", "-domain_name"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapLocalIPTagsRecord]:
        """Retrieve a list of tags associated with the IP address grouped by domains.

        This
        will return records for all domains which were accessed by the IP and received
        tags.

        Args:
          ip: The IP address to check

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Sort the response by given field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v1/ip-reputation",
            page=SyncOffsetPage[WaapLocalIPTagsRecord],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ip": ip,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                    },
                    ip_reputation_list_params.IPReputationListParams,
                ),
            ),
            model=WaapLocalIPTagsRecord,
        )

    def clear_local_tags(
        self,
        *,
        items: Iterable[ip_reputation_clear_local_tags_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapClearLocalTagsResponse:
        """
        Clear all tags associated between the provided IP addresses and domains.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/waap/v2/ip-reputation/clear-local-tags",
            body=maybe_transform(items, Iterable[ip_reputation_clear_local_tags_params.Item]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapClearLocalTagsResponse,
        )


class AsyncIPReputationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPReputationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPReputationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPReputationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncIPReputationResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        ip: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal["date", "-date", "domain_name", "-domain_name"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapLocalIPTagsRecord, AsyncOffsetPage[WaapLocalIPTagsRecord]]:
        """Retrieve a list of tags associated with the IP address grouped by domains.

        This
        will return records for all domains which were accessed by the IP and received
        tags.

        Args:
          ip: The IP address to check

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Sort the response by given field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v1/ip-reputation",
            page=AsyncOffsetPage[WaapLocalIPTagsRecord],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ip": ip,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                    },
                    ip_reputation_list_params.IPReputationListParams,
                ),
            ),
            model=WaapLocalIPTagsRecord,
        )

    async def clear_local_tags(
        self,
        *,
        items: Iterable[ip_reputation_clear_local_tags_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapClearLocalTagsResponse:
        """
        Clear all tags associated between the provided IP addresses and domains.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/waap/v2/ip-reputation/clear-local-tags",
            body=await async_maybe_transform(items, Iterable[ip_reputation_clear_local_tags_params.Item]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapClearLocalTagsResponse,
        )


class IPReputationResourceWithRawResponse:
    def __init__(self, ip_reputation: IPReputationResource) -> None:
        self._ip_reputation = ip_reputation

        self.list = to_raw_response_wrapper(
            ip_reputation.list,
        )
        self.clear_local_tags = to_raw_response_wrapper(
            ip_reputation.clear_local_tags,
        )


class AsyncIPReputationResourceWithRawResponse:
    def __init__(self, ip_reputation: AsyncIPReputationResource) -> None:
        self._ip_reputation = ip_reputation

        self.list = async_to_raw_response_wrapper(
            ip_reputation.list,
        )
        self.clear_local_tags = async_to_raw_response_wrapper(
            ip_reputation.clear_local_tags,
        )


class IPReputationResourceWithStreamingResponse:
    def __init__(self, ip_reputation: IPReputationResource) -> None:
        self._ip_reputation = ip_reputation

        self.list = to_streamed_response_wrapper(
            ip_reputation.list,
        )
        self.clear_local_tags = to_streamed_response_wrapper(
            ip_reputation.clear_local_tags,
        )


class AsyncIPReputationResourceWithStreamingResponse:
    def __init__(self, ip_reputation: AsyncIPReputationResource) -> None:
        self._ip_reputation = ip_reputation

        self.list = async_to_streamed_response_wrapper(
            ip_reputation.list,
        )
        self.clear_local_tags = async_to_streamed_response_wrapper(
            ip_reputation.clear_local_tags,
        )

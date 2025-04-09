# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloud.quotas.regional_quotas import RegionalQuotas

__all__ = ["RegionalResource", "AsyncRegionalResource"]


class RegionalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegionalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return RegionalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegionalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return RegionalResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        client_id: int,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionalQuotas:
        """
        Get a quota by region

        Args:
          client_id: Client ID

          region_id: Region ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
        return self._get(
            f"/cloud/v2/regional_quotas/{client_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegionalQuotas,
        )


class AsyncRegionalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegionalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegionalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegionalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncRegionalResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        client_id: int,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionalQuotas:
        """
        Get a quota by region

        Args:
          client_id: Client ID

          region_id: Region ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
        return await self._get(
            f"/cloud/v2/regional_quotas/{client_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegionalQuotas,
        )


class RegionalResourceWithRawResponse:
    def __init__(self, regional: RegionalResource) -> None:
        self._regional = regional

        self.retrieve = to_raw_response_wrapper(
            regional.retrieve,
        )


class AsyncRegionalResourceWithRawResponse:
    def __init__(self, regional: AsyncRegionalResource) -> None:
        self._regional = regional

        self.retrieve = async_to_raw_response_wrapper(
            regional.retrieve,
        )


class RegionalResourceWithStreamingResponse:
    def __init__(self, regional: RegionalResource) -> None:
        self._regional = regional

        self.retrieve = to_streamed_response_wrapper(
            regional.retrieve,
        )


class AsyncRegionalResourceWithStreamingResponse:
    def __init__(self, regional: AsyncRegionalResource) -> None:
        self._regional = regional

        self.retrieve = async_to_streamed_response_wrapper(
            regional.retrieve,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .requests import (
    RequestsResource,
    AsyncRequestsResource,
    RequestsResourceWithRawResponse,
    AsyncRequestsResourceWithRawResponse,
    RequestsResourceWithStreamingResponse,
    AsyncRequestsResourceWithStreamingResponse,
)
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
from ....types.cloud.quota_get_all_response import QuotaGetAllResponse
from ....types.cloud.quota_get_global_response import QuotaGetGlobalResponse
from ....types.cloud.quota_get_by_region_response import QuotaGetByRegionResponse

__all__ = ["QuotasResource", "AsyncQuotasResource"]


class QuotasResource(SyncAPIResource):
    @cached_property
    def requests(self) -> RequestsResource:
        return RequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> QuotasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return QuotasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuotasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return QuotasResourceWithStreamingResponse(self)

    def get_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuotaGetAllResponse:
        """Get combined client quotas, including both regional and global quotas."""
        return self._get(
            "/cloud/v2/client_quotas",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuotaGetAllResponse,
        )

    def get_by_region(
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
    ) -> QuotaGetByRegionResponse:
        """
        Get quotas for a specific region and client.

        Args:
          client_id: Client ID

          region_id: Region ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get(
            f"/cloud/v2/regional_quotas/{client_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuotaGetByRegionResponse,
        )

    def get_global(
        self,
        client_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuotaGetGlobalResponse:
        """
        Get global quotas for a specific client.

        Args:
          client_id: Client ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cloud/v2/global_quotas/{client_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuotaGetGlobalResponse,
        )


class AsyncQuotasResource(AsyncAPIResource):
    @cached_property
    def requests(self) -> AsyncRequestsResource:
        return AsyncRequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQuotasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQuotasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuotasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncQuotasResourceWithStreamingResponse(self)

    async def get_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuotaGetAllResponse:
        """Get combined client quotas, including both regional and global quotas."""
        return await self._get(
            "/cloud/v2/client_quotas",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuotaGetAllResponse,
        )

    async def get_by_region(
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
    ) -> QuotaGetByRegionResponse:
        """
        Get quotas for a specific region and client.

        Args:
          client_id: Client ID

          region_id: Region ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._get(
            f"/cloud/v2/regional_quotas/{client_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuotaGetByRegionResponse,
        )

    async def get_global(
        self,
        client_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuotaGetGlobalResponse:
        """
        Get global quotas for a specific client.

        Args:
          client_id: Client ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cloud/v2/global_quotas/{client_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuotaGetGlobalResponse,
        )


class QuotasResourceWithRawResponse:
    def __init__(self, quotas: QuotasResource) -> None:
        self._quotas = quotas

        self.get_all = to_raw_response_wrapper(
            quotas.get_all,
        )
        self.get_by_region = to_raw_response_wrapper(
            quotas.get_by_region,
        )
        self.get_global = to_raw_response_wrapper(
            quotas.get_global,
        )

    @cached_property
    def requests(self) -> RequestsResourceWithRawResponse:
        return RequestsResourceWithRawResponse(self._quotas.requests)


class AsyncQuotasResourceWithRawResponse:
    def __init__(self, quotas: AsyncQuotasResource) -> None:
        self._quotas = quotas

        self.get_all = async_to_raw_response_wrapper(
            quotas.get_all,
        )
        self.get_by_region = async_to_raw_response_wrapper(
            quotas.get_by_region,
        )
        self.get_global = async_to_raw_response_wrapper(
            quotas.get_global,
        )

    @cached_property
    def requests(self) -> AsyncRequestsResourceWithRawResponse:
        return AsyncRequestsResourceWithRawResponse(self._quotas.requests)


class QuotasResourceWithStreamingResponse:
    def __init__(self, quotas: QuotasResource) -> None:
        self._quotas = quotas

        self.get_all = to_streamed_response_wrapper(
            quotas.get_all,
        )
        self.get_by_region = to_streamed_response_wrapper(
            quotas.get_by_region,
        )
        self.get_global = to_streamed_response_wrapper(
            quotas.get_global,
        )

    @cached_property
    def requests(self) -> RequestsResourceWithStreamingResponse:
        return RequestsResourceWithStreamingResponse(self._quotas.requests)


class AsyncQuotasResourceWithStreamingResponse:
    def __init__(self, quotas: AsyncQuotasResource) -> None:
        self._quotas = quotas

        self.get_all = async_to_streamed_response_wrapper(
            quotas.get_all,
        )
        self.get_by_region = async_to_streamed_response_wrapper(
            quotas.get_by_region,
        )
        self.get_global = async_to_streamed_response_wrapper(
            quotas.get_global,
        )

    @cached_property
    def requests(self) -> AsyncRequestsResourceWithStreamingResponse:
        return AsyncRequestsResourceWithStreamingResponse(self._quotas.requests)

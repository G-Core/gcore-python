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
from ....types.cloud.quotas.all_client_quotas import AllClientQuotas

__all__ = ["ClientQuotasResource", "AsyncClientQuotasResource"]


class ClientQuotasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientQuotasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ClientQuotasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientQuotasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return ClientQuotasResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllClientQuotas:
        """Get combined client quotas, regional and global."""
        return self._get(
            "/cloud/v2/client_quotas",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllClientQuotas,
        )


class AsyncClientQuotasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientQuotasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClientQuotasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientQuotasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncClientQuotasResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllClientQuotas:
        """Get combined client quotas, regional and global."""
        return await self._get(
            "/cloud/v2/client_quotas",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllClientQuotas,
        )


class ClientQuotasResourceWithRawResponse:
    def __init__(self, client_quotas: ClientQuotasResource) -> None:
        self._client_quotas = client_quotas

        self.retrieve = to_raw_response_wrapper(
            client_quotas.retrieve,
        )


class AsyncClientQuotasResourceWithRawResponse:
    def __init__(self, client_quotas: AsyncClientQuotasResource) -> None:
        self._client_quotas = client_quotas

        self.retrieve = async_to_raw_response_wrapper(
            client_quotas.retrieve,
        )


class ClientQuotasResourceWithStreamingResponse:
    def __init__(self, client_quotas: ClientQuotasResource) -> None:
        self._client_quotas = client_quotas

        self.retrieve = to_streamed_response_wrapper(
            client_quotas.retrieve,
        )


class AsyncClientQuotasResourceWithStreamingResponse:
    def __init__(self, client_quotas: AsyncClientQuotasResource) -> None:
        self._client_quotas = client_quotas

        self.retrieve = async_to_streamed_response_wrapper(
            client_quotas.retrieve,
        )

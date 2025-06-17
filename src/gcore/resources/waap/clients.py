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
from ...types.waap.client_me_response import ClientMeResponse

__all__ = ["ClientsResource", "AsyncClientsResource"]


class ClientsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ClientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ClientsResourceWithStreamingResponse(self)

    def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientMeResponse:
        """Get information about WAAP service for the client"""
        return self._get(
            "/waap/v1/clients/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientMeResponse,
        )


class AsyncClientsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncClientsResourceWithStreamingResponse(self)

    async def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientMeResponse:
        """Get information about WAAP service for the client"""
        return await self._get(
            "/waap/v1/clients/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientMeResponse,
        )


class ClientsResourceWithRawResponse:
    def __init__(self, clients: ClientsResource) -> None:
        self._clients = clients

        self.me = to_raw_response_wrapper(
            clients.me,
        )


class AsyncClientsResourceWithRawResponse:
    def __init__(self, clients: AsyncClientsResource) -> None:
        self._clients = clients

        self.me = async_to_raw_response_wrapper(
            clients.me,
        )


class ClientsResourceWithStreamingResponse:
    def __init__(self, clients: ClientsResource) -> None:
        self._clients = clients

        self.me = to_streamed_response_wrapper(
            clients.me,
        )


class AsyncClientsResourceWithStreamingResponse:
    def __init__(self, clients: AsyncClientsResource) -> None:
        self._clients = clients

        self.me = async_to_streamed_response_wrapper(
            clients.me,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.cdn import client_config_update_params, client_config_replace_params
from ..._base_client import make_request_options
from ...types.cdn.cdn_account import CDNAccount

__all__ = ["ClientConfigResource", "AsyncClientConfigResource"]


class ClientConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ClientConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ClientConfigResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        utilization_level: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CDNAccount:
        """
        Change information about CDN service.

        Args:
          utilization_level: CDN traffic usage limit in gigabytes.

              When the limit is reached, we will send an email notification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/cdn/clients/me",
            body=maybe_transform(
                {"utilization_level": utilization_level}, client_config_update_params.ClientConfigUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CDNAccount,
        )

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CDNAccount:
        """Get information about CDN service."""
        return self._get(
            "/cdn/clients/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CDNAccount,
        )

    def replace(
        self,
        *,
        utilization_level: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CDNAccount:
        """
        Change information about CDN service.

        Args:
          utilization_level: CDN traffic usage limit in gigabytes.

              When the limit is reached, we will send an email notification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/cdn/clients/me",
            body=maybe_transform(
                {"utilization_level": utilization_level}, client_config_replace_params.ClientConfigReplaceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CDNAccount,
        )


class AsyncClientConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClientConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncClientConfigResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        utilization_level: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CDNAccount:
        """
        Change information about CDN service.

        Args:
          utilization_level: CDN traffic usage limit in gigabytes.

              When the limit is reached, we will send an email notification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/cdn/clients/me",
            body=await async_maybe_transform(
                {"utilization_level": utilization_level}, client_config_update_params.ClientConfigUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CDNAccount,
        )

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CDNAccount:
        """Get information about CDN service."""
        return await self._get(
            "/cdn/clients/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CDNAccount,
        )

    async def replace(
        self,
        *,
        utilization_level: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CDNAccount:
        """
        Change information about CDN service.

        Args:
          utilization_level: CDN traffic usage limit in gigabytes.

              When the limit is reached, we will send an email notification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/cdn/clients/me",
            body=await async_maybe_transform(
                {"utilization_level": utilization_level}, client_config_replace_params.ClientConfigReplaceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CDNAccount,
        )


class ClientConfigResourceWithRawResponse:
    def __init__(self, client_config: ClientConfigResource) -> None:
        self._client_config = client_config

        self.update = to_raw_response_wrapper(
            client_config.update,
        )
        self.get = to_raw_response_wrapper(
            client_config.get,
        )
        self.replace = to_raw_response_wrapper(
            client_config.replace,
        )


class AsyncClientConfigResourceWithRawResponse:
    def __init__(self, client_config: AsyncClientConfigResource) -> None:
        self._client_config = client_config

        self.update = async_to_raw_response_wrapper(
            client_config.update,
        )
        self.get = async_to_raw_response_wrapper(
            client_config.get,
        )
        self.replace = async_to_raw_response_wrapper(
            client_config.replace,
        )


class ClientConfigResourceWithStreamingResponse:
    def __init__(self, client_config: ClientConfigResource) -> None:
        self._client_config = client_config

        self.update = to_streamed_response_wrapper(
            client_config.update,
        )
        self.get = to_streamed_response_wrapper(
            client_config.get,
        )
        self.replace = to_streamed_response_wrapper(
            client_config.replace,
        )


class AsyncClientConfigResourceWithStreamingResponse:
    def __init__(self, client_config: AsyncClientConfigResource) -> None:
        self._client_config = client_config

        self.update = async_to_streamed_response_wrapper(
            client_config.update,
        )
        self.get = async_to_streamed_response_wrapper(
            client_config.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            client_config.replace,
        )

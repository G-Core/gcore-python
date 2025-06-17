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
from ....types.waap.domains.api_path_group_list_response import APIPathGroupListResponse

__all__ = ["APIPathGroupsResource", "AsyncAPIPathGroupsResource"]


class APIPathGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIPathGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return APIPathGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIPathGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return APIPathGroupsResourceWithStreamingResponse(self)

    def list(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIPathGroupListResponse:
        """
        Retrieve a list of API path groups for a specific domain

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/waap/v1/domains/{domain_id}/api-path-groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIPathGroupListResponse,
        )


class AsyncAPIPathGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIPathGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIPathGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIPathGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAPIPathGroupsResourceWithStreamingResponse(self)

    async def list(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIPathGroupListResponse:
        """
        Retrieve a list of API path groups for a specific domain

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/waap/v1/domains/{domain_id}/api-path-groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIPathGroupListResponse,
        )


class APIPathGroupsResourceWithRawResponse:
    def __init__(self, api_path_groups: APIPathGroupsResource) -> None:
        self._api_path_groups = api_path_groups

        self.list = to_raw_response_wrapper(
            api_path_groups.list,
        )


class AsyncAPIPathGroupsResourceWithRawResponse:
    def __init__(self, api_path_groups: AsyncAPIPathGroupsResource) -> None:
        self._api_path_groups = api_path_groups

        self.list = async_to_raw_response_wrapper(
            api_path_groups.list,
        )


class APIPathGroupsResourceWithStreamingResponse:
    def __init__(self, api_path_groups: APIPathGroupsResource) -> None:
        self._api_path_groups = api_path_groups

        self.list = to_streamed_response_wrapper(
            api_path_groups.list,
        )


class AsyncAPIPathGroupsResourceWithStreamingResponse:
    def __init__(self, api_path_groups: AsyncAPIPathGroupsResource) -> None:
        self._api_path_groups = api_path_groups

        self.list = async_to_streamed_response_wrapper(
            api_path_groups.list,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ....types.cloud.quotas import request_list_params, request_create_params
from ....types.cloud.quotas.request_get_response import RequestGetResponse

__all__ = ["RequestsResource", "AsyncRequestsResource"]


class RequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return RequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return RequestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        requested_limits: request_create_params.RequestedLimits,
        client_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create request to change quotas

        Args:
          description: '#/components/schemas/LimitsRequestCreateSerializer/properties/description'
              "$.components.schemas.LimitsRequestCreateSerializer.properties.description"

          requested_limits: '#/components/schemas/LimitsRequestCreateSerializer/properties/requested_limits'
              "$.components.schemas.LimitsRequestCreateSerializer.properties.requested_limits"

          client_id: '#/components/schemas/LimitsRequestCreateSerializer/properties/client_id'
              "$.components.schemas.LimitsRequestCreateSerializer.properties.client_id"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cloud/v2/limits_request",
            body=maybe_transform(
                {
                    "description": description,
                    "requested_limits": requested_limits,
                    "client_id": client_id,
                },
                request_create_params.RequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        status: Optional[List[Literal["done", "in progress", "rejected"]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Returns a list of sent requests to change current quotas and their statuses

        Args:
          limit: '#/paths/%2Fcloud%2Fv2%2Flimits_request/get/parameters/0'
              "$.paths['/cloud/v2/limits_request'].get.parameters[0]"

          offset: '#/paths/%2Fcloud%2Fv2%2Flimits_request/get/parameters/1'
              "$.paths['/cloud/v2/limits_request'].get.parameters[1]"

          status: '#/paths/%2Fcloud%2Fv2%2Flimits_request/get/parameters/2/schema/anyOf/0'
              "$.paths['/cloud/v2/limits_request'].get.parameters[2].schema.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/cloud/v2/limits_request",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    request_list_params.RequestListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete request to change quotas

        Args:
          request_id: '#/paths/%2Fcloud%2Fv2%2Flimits_request%2F%7Brequest_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v2/limits_request/{request_id}']['delete'].parameters[0].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cloud/v2/limits_request/{request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequestGetResponse:
        """
        Get request to change quota limits.

        Args:
          request_id: '#/paths/%2Fcloud%2Fv2%2Flimits_request%2F%7Brequest_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v2/limits_request/{request_id}'].get.parameters[0].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            f"/cloud/v2/limits_request/{request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestGetResponse,
        )


class AsyncRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        requested_limits: request_create_params.RequestedLimits,
        client_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create request to change quotas

        Args:
          description: '#/components/schemas/LimitsRequestCreateSerializer/properties/description'
              "$.components.schemas.LimitsRequestCreateSerializer.properties.description"

          requested_limits: '#/components/schemas/LimitsRequestCreateSerializer/properties/requested_limits'
              "$.components.schemas.LimitsRequestCreateSerializer.properties.requested_limits"

          client_id: '#/components/schemas/LimitsRequestCreateSerializer/properties/client_id'
              "$.components.schemas.LimitsRequestCreateSerializer.properties.client_id"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cloud/v2/limits_request",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "requested_limits": requested_limits,
                    "client_id": client_id,
                },
                request_create_params.RequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        status: Optional[List[Literal["done", "in progress", "rejected"]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Returns a list of sent requests to change current quotas and their statuses

        Args:
          limit: '#/paths/%2Fcloud%2Fv2%2Flimits_request/get/parameters/0'
              "$.paths['/cloud/v2/limits_request'].get.parameters[0]"

          offset: '#/paths/%2Fcloud%2Fv2%2Flimits_request/get/parameters/1'
              "$.paths['/cloud/v2/limits_request'].get.parameters[1]"

          status: '#/paths/%2Fcloud%2Fv2%2Flimits_request/get/parameters/2/schema/anyOf/0'
              "$.paths['/cloud/v2/limits_request'].get.parameters[2].schema.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/cloud/v2/limits_request",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    request_list_params.RequestListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete request to change quotas

        Args:
          request_id: '#/paths/%2Fcloud%2Fv2%2Flimits_request%2F%7Brequest_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v2/limits_request/{request_id}']['delete'].parameters[0].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cloud/v2/limits_request/{request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequestGetResponse:
        """
        Get request to change quota limits.

        Args:
          request_id: '#/paths/%2Fcloud%2Fv2%2Flimits_request%2F%7Brequest_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v2/limits_request/{request_id}'].get.parameters[0].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            f"/cloud/v2/limits_request/{request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestGetResponse,
        )


class RequestsResourceWithRawResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.create = to_raw_response_wrapper(
            requests.create,
        )
        self.list = to_raw_response_wrapper(
            requests.list,
        )
        self.delete = to_raw_response_wrapper(
            requests.delete,
        )
        self.get = to_raw_response_wrapper(
            requests.get,
        )


class AsyncRequestsResourceWithRawResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.create = async_to_raw_response_wrapper(
            requests.create,
        )
        self.list = async_to_raw_response_wrapper(
            requests.list,
        )
        self.delete = async_to_raw_response_wrapper(
            requests.delete,
        )
        self.get = async_to_raw_response_wrapper(
            requests.get,
        )


class RequestsResourceWithStreamingResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.create = to_streamed_response_wrapper(
            requests.create,
        )
        self.list = to_streamed_response_wrapper(
            requests.list,
        )
        self.delete = to_streamed_response_wrapper(
            requests.delete,
        )
        self.get = to_streamed_response_wrapper(
            requests.get,
        )


class AsyncRequestsResourceWithStreamingResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.create = async_to_streamed_response_wrapper(
            requests.create,
        )
        self.list = async_to_streamed_response_wrapper(
            requests.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            requests.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            requests.get,
        )

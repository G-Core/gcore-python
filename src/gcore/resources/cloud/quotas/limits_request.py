# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloud.quotas import limits_request_list_params, limits_request_create_params
from ....types.cloud.quotas.limits_request import LimitsRequest

__all__ = ["LimitsRequestResource", "AsyncLimitsRequestResource"]


class LimitsRequestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LimitsRequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return LimitsRequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LimitsRequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return LimitsRequestResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        requested_limits: limits_request_create_params.RequestedLimits,
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
          description: Describe the reason, in general terms.

          requested_limits: Limits you want to increase.

          client_id: Client ID that requests the limit increase.

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
                limits_request_create_params.LimitsRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LimitsRequest:
        """
        Get request to change quota limits.

        Args:
          request_id: LimitRequest ID

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
            cast_to=LimitsRequest,
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
          limit: Optional. Limit the number of returned items

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          status: List of limit requests statuses for filtering

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
                    limits_request_list_params.LimitsRequestListParams,
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
          request_id: LimitRequest ID

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


class AsyncLimitsRequestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLimitsRequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLimitsRequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLimitsRequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncLimitsRequestResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        requested_limits: limits_request_create_params.RequestedLimits,
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
          description: Describe the reason, in general terms.

          requested_limits: Limits you want to increase.

          client_id: Client ID that requests the limit increase.

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
                limits_request_create_params.LimitsRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LimitsRequest:
        """
        Get request to change quota limits.

        Args:
          request_id: LimitRequest ID

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
            cast_to=LimitsRequest,
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
          limit: Optional. Limit the number of returned items

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          status: List of limit requests statuses for filtering

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
                    limits_request_list_params.LimitsRequestListParams,
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
          request_id: LimitRequest ID

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


class LimitsRequestResourceWithRawResponse:
    def __init__(self, limits_request: LimitsRequestResource) -> None:
        self._limits_request = limits_request

        self.create = to_raw_response_wrapper(
            limits_request.create,
        )
        self.retrieve = to_raw_response_wrapper(
            limits_request.retrieve,
        )
        self.list = to_raw_response_wrapper(
            limits_request.list,
        )
        self.delete = to_raw_response_wrapper(
            limits_request.delete,
        )


class AsyncLimitsRequestResourceWithRawResponse:
    def __init__(self, limits_request: AsyncLimitsRequestResource) -> None:
        self._limits_request = limits_request

        self.create = async_to_raw_response_wrapper(
            limits_request.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            limits_request.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            limits_request.list,
        )
        self.delete = async_to_raw_response_wrapper(
            limits_request.delete,
        )


class LimitsRequestResourceWithStreamingResponse:
    def __init__(self, limits_request: LimitsRequestResource) -> None:
        self._limits_request = limits_request

        self.create = to_streamed_response_wrapper(
            limits_request.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            limits_request.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            limits_request.list,
        )
        self.delete = to_streamed_response_wrapper(
            limits_request.delete,
        )


class AsyncLimitsRequestResourceWithStreamingResponse:
    def __init__(self, limits_request: AsyncLimitsRequestResource) -> None:
        self._limits_request = limits_request

        self.create = async_to_streamed_response_wrapper(
            limits_request.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            limits_request.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            limits_request.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            limits_request.delete,
        )

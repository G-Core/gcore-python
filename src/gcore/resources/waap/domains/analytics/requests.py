# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncOffsetPage, AsyncOffsetPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.waap.domains.analytics import request_list_params
from .....types.waap.waap_traffic_type import WaapTrafficType
from .....types.waap.waap_request_details import WaapRequestDetails
from .....types.waap.waap_request_summary import WaapRequestSummary

__all__ = ["RequestsResource", "AsyncRequestsResource"]


class RequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return RequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return RequestsResourceWithStreamingResponse(self)

    def list(
        self,
        domain_id: int,
        *,
        start: Union[str, datetime],
        actions: List[Literal["allow", "block", "captcha", "handshake"]] | NotGiven = NOT_GIVEN,
        countries: List[str] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        ordering: str | NotGiven = NOT_GIVEN,
        reference_id: str | NotGiven = NOT_GIVEN,
        security_rule_name: str | NotGiven = NOT_GIVEN,
        status_code: int | NotGiven = NOT_GIVEN,
        traffic_types: List[WaapTrafficType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[WaapRequestSummary]:
        """
        Retrieve a domain's requests data.

        Args:
          domain_id: The domain ID

          start: Filter traffic starting from a specified date in ISO 8601 format

          actions: Filter the response by actions.

          countries: Filter the response by country codes in ISO 3166-1 alpha-2 format.

          end: Filter traffic up to a specified end date in ISO 8601 format. If not provided,
              defaults to the current date and time.

          ip: Filter the response by IP.

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Sort the response by given field.

          reference_id: Filter the response by reference ID.

          security_rule_name: Filter the response by security rule name.

          status_code: Filter the response by response code.

          traffic_types: Filter the response by traffic types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/requests",
            page=SyncOffsetPage[WaapRequestSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start": start,
                        "actions": actions,
                        "countries": countries,
                        "end": end,
                        "ip": ip,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "reference_id": reference_id,
                        "security_rule_name": security_rule_name,
                        "status_code": status_code,
                        "traffic_types": traffic_types,
                    },
                    request_list_params.RequestListParams,
                ),
            ),
            model=WaapRequestSummary,
        )

    def get(
        self,
        request_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapRequestDetails:
        """
        Retrieves all the available information for a request that matches a given
        request id

        Args:
          domain_id: The domain ID

          request_id: The request ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            f"/waap/v1/domains/{domain_id}/requests/{request_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapRequestDetails,
        )


class AsyncRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncRequestsResourceWithStreamingResponse(self)

    def list(
        self,
        domain_id: int,
        *,
        start: Union[str, datetime],
        actions: List[Literal["allow", "block", "captcha", "handshake"]] | NotGiven = NOT_GIVEN,
        countries: List[str] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        ordering: str | NotGiven = NOT_GIVEN,
        reference_id: str | NotGiven = NOT_GIVEN,
        security_rule_name: str | NotGiven = NOT_GIVEN,
        status_code: int | NotGiven = NOT_GIVEN,
        traffic_types: List[WaapTrafficType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WaapRequestSummary, AsyncOffsetPage[WaapRequestSummary]]:
        """
        Retrieve a domain's requests data.

        Args:
          domain_id: The domain ID

          start: Filter traffic starting from a specified date in ISO 8601 format

          actions: Filter the response by actions.

          countries: Filter the response by country codes in ISO 3166-1 alpha-2 format.

          end: Filter traffic up to a specified end date in ISO 8601 format. If not provided,
              defaults to the current date and time.

          ip: Filter the response by IP.

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Sort the response by given field.

          reference_id: Filter the response by reference ID.

          security_rule_name: Filter the response by security rule name.

          status_code: Filter the response by response code.

          traffic_types: Filter the response by traffic types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/requests",
            page=AsyncOffsetPage[WaapRequestSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start": start,
                        "actions": actions,
                        "countries": countries,
                        "end": end,
                        "ip": ip,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "reference_id": reference_id,
                        "security_rule_name": security_rule_name,
                        "status_code": status_code,
                        "traffic_types": traffic_types,
                    },
                    request_list_params.RequestListParams,
                ),
            ),
            model=WaapRequestSummary,
        )

    async def get(
        self,
        request_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapRequestDetails:
        """
        Retrieves all the available information for a request that matches a given
        request id

        Args:
          domain_id: The domain ID

          request_id: The request ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            f"/waap/v1/domains/{domain_id}/requests/{request_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapRequestDetails,
        )


class RequestsResourceWithRawResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.list = to_raw_response_wrapper(
            requests.list,
        )
        self.get = to_raw_response_wrapper(
            requests.get,
        )


class AsyncRequestsResourceWithRawResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.list = async_to_raw_response_wrapper(
            requests.list,
        )
        self.get = async_to_raw_response_wrapper(
            requests.get,
        )


class RequestsResourceWithStreamingResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.list = to_streamed_response_wrapper(
            requests.list,
        )
        self.get = to_streamed_response_wrapper(
            requests.get,
        )


class AsyncRequestsResourceWithStreamingResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.list = async_to_streamed_response_wrapper(
            requests.list,
        )
        self.get = async_to_streamed_response_wrapper(
            requests.get,
        )

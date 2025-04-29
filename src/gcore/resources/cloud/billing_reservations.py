# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.cloud import billing_reservation_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cloud.billing_reservation import BillingReservation

__all__ = ["BillingReservationsResource", "AsyncBillingReservationsResource"]


class BillingReservationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingReservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return BillingReservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingReservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return BillingReservationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        activated_from: Union[str, date] | NotGiven = NOT_GIVEN,
        activated_to: Union[str, date] | NotGiven = NOT_GIVEN,
        created_from: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_to: Union[str, datetime] | NotGiven = NOT_GIVEN,
        deactivated_from: Union[str, date] | NotGiven = NOT_GIVEN,
        deactivated_to: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metric_name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        region_id: int | NotGiven = NOT_GIVEN,
        status: List[
            Literal[
                "ACTIVATED", "APPROVED", "COPIED", "CREATED", "EXPIRED", "REJECTED", "RESERVED", "WAITING_FOR_PAYMENT"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[BillingReservation]:
        """
        List reservations

        Args:
          activated_from: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/0'
              "$.paths['/cloud/v1/reservations'].get.parameters[0]"

          activated_to: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/1'
              "$.paths['/cloud/v1/reservations'].get.parameters[1]"

          created_from: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/2'
              "$.paths['/cloud/v1/reservations'].get.parameters[2]"

          created_to: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/3'
              "$.paths['/cloud/v1/reservations'].get.parameters[3]"

          deactivated_from: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/4'
              "$.paths['/cloud/v1/reservations'].get.parameters[4]"

          deactivated_to: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/5'
              "$.paths['/cloud/v1/reservations'].get.parameters[5]"

          limit: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/6'
              "$.paths['/cloud/v1/reservations'].get.parameters[6]"

          metric_name: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/7'
              "$.paths['/cloud/v1/reservations'].get.parameters[7]"

          offset: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/8'
              "$.paths['/cloud/v1/reservations'].get.parameters[8]"

          region_id: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/9'
              "$.paths['/cloud/v1/reservations'].get.parameters[9]"

          status: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/10'
              "$.paths['/cloud/v1/reservations'].get.parameters[10]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cloud/v1/reservations",
            page=SyncOffsetPage[BillingReservation],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "activated_from": activated_from,
                        "activated_to": activated_to,
                        "created_from": created_from,
                        "created_to": created_to,
                        "deactivated_from": deactivated_from,
                        "deactivated_to": deactivated_to,
                        "limit": limit,
                        "metric_name": metric_name,
                        "offset": offset,
                        "region_id": region_id,
                        "status": status,
                    },
                    billing_reservation_list_params.BillingReservationListParams,
                ),
            ),
            model=BillingReservation,
        )

    def get(
        self,
        reservation_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingReservation:
        """
        Get specific reservation

        Args:
          reservation_id: '#/paths/%2Fcloud%2Fv1%2Freservations%2F%7Breservation_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/reservations/{reservation_id}'].get.parameters[0].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cloud/v1/reservations/{reservation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingReservation,
        )


class AsyncBillingReservationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingReservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingReservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingReservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncBillingReservationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        activated_from: Union[str, date] | NotGiven = NOT_GIVEN,
        activated_to: Union[str, date] | NotGiven = NOT_GIVEN,
        created_from: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_to: Union[str, datetime] | NotGiven = NOT_GIVEN,
        deactivated_from: Union[str, date] | NotGiven = NOT_GIVEN,
        deactivated_to: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metric_name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        region_id: int | NotGiven = NOT_GIVEN,
        status: List[
            Literal[
                "ACTIVATED", "APPROVED", "COPIED", "CREATED", "EXPIRED", "REJECTED", "RESERVED", "WAITING_FOR_PAYMENT"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BillingReservation, AsyncOffsetPage[BillingReservation]]:
        """
        List reservations

        Args:
          activated_from: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/0'
              "$.paths['/cloud/v1/reservations'].get.parameters[0]"

          activated_to: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/1'
              "$.paths['/cloud/v1/reservations'].get.parameters[1]"

          created_from: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/2'
              "$.paths['/cloud/v1/reservations'].get.parameters[2]"

          created_to: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/3'
              "$.paths['/cloud/v1/reservations'].get.parameters[3]"

          deactivated_from: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/4'
              "$.paths['/cloud/v1/reservations'].get.parameters[4]"

          deactivated_to: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/5'
              "$.paths['/cloud/v1/reservations'].get.parameters[5]"

          limit: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/6'
              "$.paths['/cloud/v1/reservations'].get.parameters[6]"

          metric_name: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/7'
              "$.paths['/cloud/v1/reservations'].get.parameters[7]"

          offset: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/8'
              "$.paths['/cloud/v1/reservations'].get.parameters[8]"

          region_id: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/9'
              "$.paths['/cloud/v1/reservations'].get.parameters[9]"

          status: '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/10'
              "$.paths['/cloud/v1/reservations'].get.parameters[10]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cloud/v1/reservations",
            page=AsyncOffsetPage[BillingReservation],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "activated_from": activated_from,
                        "activated_to": activated_to,
                        "created_from": created_from,
                        "created_to": created_to,
                        "deactivated_from": deactivated_from,
                        "deactivated_to": deactivated_to,
                        "limit": limit,
                        "metric_name": metric_name,
                        "offset": offset,
                        "region_id": region_id,
                        "status": status,
                    },
                    billing_reservation_list_params.BillingReservationListParams,
                ),
            ),
            model=BillingReservation,
        )

    async def get(
        self,
        reservation_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingReservation:
        """
        Get specific reservation

        Args:
          reservation_id: '#/paths/%2Fcloud%2Fv1%2Freservations%2F%7Breservation_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/reservations/{reservation_id}'].get.parameters[0].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cloud/v1/reservations/{reservation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingReservation,
        )


class BillingReservationsResourceWithRawResponse:
    def __init__(self, billing_reservations: BillingReservationsResource) -> None:
        self._billing_reservations = billing_reservations

        self.list = to_raw_response_wrapper(
            billing_reservations.list,
        )
        self.get = to_raw_response_wrapper(
            billing_reservations.get,
        )


class AsyncBillingReservationsResourceWithRawResponse:
    def __init__(self, billing_reservations: AsyncBillingReservationsResource) -> None:
        self._billing_reservations = billing_reservations

        self.list = async_to_raw_response_wrapper(
            billing_reservations.list,
        )
        self.get = async_to_raw_response_wrapper(
            billing_reservations.get,
        )


class BillingReservationsResourceWithStreamingResponse:
    def __init__(self, billing_reservations: BillingReservationsResource) -> None:
        self._billing_reservations = billing_reservations

        self.list = to_streamed_response_wrapper(
            billing_reservations.list,
        )
        self.get = to_streamed_response_wrapper(
            billing_reservations.get,
        )


class AsyncBillingReservationsResourceWithStreamingResponse:
    def __init__(self, billing_reservations: AsyncBillingReservationsResource) -> None:
        self._billing_reservations = billing_reservations

        self.list = async_to_streamed_response_wrapper(
            billing_reservations.list,
        )
        self.get = async_to_streamed_response_wrapper(
            billing_reservations.get,
        )

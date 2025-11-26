# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.cloud import billing_reservation_list_params
from ..._base_client import make_request_options
from ...types.cloud.billing_reservations import BillingReservations

__all__ = ["BillingReservationsResource", "AsyncBillingReservationsResource"]


class BillingReservationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingReservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return BillingReservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingReservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return BillingReservationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        metric_name: str | Omit = omit,
        order_by: Literal["active_from.asc", "active_from.desc", "active_to.asc", "active_to.desc"] | Omit = omit,
        region_id: int | Omit = omit,
        show_inactive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingReservations:
        """
        Get a list of billing reservations along with detailed information on resource
        configurations and associated pricing.

        Args:
          metric_name: Metric name for the resource (e.g., 'bm1-hf-`medium_min`')

          order_by: Order by field and direction.

          region_id: Region for reservation

          show_inactive: Include inactive commits in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cloud/v2/reservations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "metric_name": metric_name,
                        "order_by": order_by,
                        "region_id": region_id,
                        "show_inactive": show_inactive,
                    },
                    billing_reservation_list_params.BillingReservationListParams,
                ),
            ),
            cast_to=BillingReservations,
        )


class AsyncBillingReservationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingReservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingReservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingReservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncBillingReservationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        metric_name: str | Omit = omit,
        order_by: Literal["active_from.asc", "active_from.desc", "active_to.asc", "active_to.desc"] | Omit = omit,
        region_id: int | Omit = omit,
        show_inactive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingReservations:
        """
        Get a list of billing reservations along with detailed information on resource
        configurations and associated pricing.

        Args:
          metric_name: Metric name for the resource (e.g., 'bm1-hf-`medium_min`')

          order_by: Order by field and direction.

          region_id: Region for reservation

          show_inactive: Include inactive commits in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cloud/v2/reservations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "metric_name": metric_name,
                        "order_by": order_by,
                        "region_id": region_id,
                        "show_inactive": show_inactive,
                    },
                    billing_reservation_list_params.BillingReservationListParams,
                ),
            ),
            cast_to=BillingReservations,
        )


class BillingReservationsResourceWithRawResponse:
    def __init__(self, billing_reservations: BillingReservationsResource) -> None:
        self._billing_reservations = billing_reservations

        self.list = to_raw_response_wrapper(
            billing_reservations.list,
        )


class AsyncBillingReservationsResourceWithRawResponse:
    def __init__(self, billing_reservations: AsyncBillingReservationsResource) -> None:
        self._billing_reservations = billing_reservations

        self.list = async_to_raw_response_wrapper(
            billing_reservations.list,
        )


class BillingReservationsResourceWithStreamingResponse:
    def __init__(self, billing_reservations: BillingReservationsResource) -> None:
        self._billing_reservations = billing_reservations

        self.list = to_streamed_response_wrapper(
            billing_reservations.list,
        )


class AsyncBillingReservationsResourceWithStreamingResponse:
    def __init__(self, billing_reservations: AsyncBillingReservationsResource) -> None:
        self._billing_reservations = billing_reservations

        self.list = async_to_streamed_response_wrapper(
            billing_reservations.list,
        )

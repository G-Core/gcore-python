# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.waap import prebilling_get_total_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.waap.waap_billing_report_item import WaapBillingReportItem

__all__ = ["PrebillingResource", "AsyncPrebillingResource"]


class PrebillingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrebillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PrebillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrebillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PrebillingResourceWithStreamingResponse(self)

    def get_total(
        self,
        metric: Literal["domains", "volume", "requests", "requests_clean"],
        *,
        from_: Union[str, date],
        to: Union[str, date],
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapBillingReportItem]:
        """
        Retrieve an aggregated report on the calling client's own billable consumption
        by given metric

        Args:
          metric: The metric to get billable consumption for

          from_: The report start date (inclusive) in ISO 8601 format

          to: The report end date (exclusive) in ISO 8601 format

          limit: Number of items to return

          offset: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric:
            raise ValueError(f"Expected a non-empty value for `metric` but received {metric!r}")
        return self._get_api_list(
            path_template("/waap/v1/prebilling/total/{metric}", metric=metric),
            page=SyncOffsetPage[WaapBillingReportItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "limit": limit,
                        "offset": offset,
                    },
                    prebilling_get_total_params.PrebillingGetTotalParams,
                ),
            ),
            model=WaapBillingReportItem,
        )


class AsyncPrebillingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrebillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrebillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrebillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPrebillingResourceWithStreamingResponse(self)

    def get_total(
        self,
        metric: Literal["domains", "volume", "requests", "requests_clean"],
        *,
        from_: Union[str, date],
        to: Union[str, date],
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapBillingReportItem, AsyncOffsetPage[WaapBillingReportItem]]:
        """
        Retrieve an aggregated report on the calling client's own billable consumption
        by given metric

        Args:
          metric: The metric to get billable consumption for

          from_: The report start date (inclusive) in ISO 8601 format

          to: The report end date (exclusive) in ISO 8601 format

          limit: Number of items to return

          offset: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric:
            raise ValueError(f"Expected a non-empty value for `metric` but received {metric!r}")
        return self._get_api_list(
            path_template("/waap/v1/prebilling/total/{metric}", metric=metric),
            page=AsyncOffsetPage[WaapBillingReportItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "limit": limit,
                        "offset": offset,
                    },
                    prebilling_get_total_params.PrebillingGetTotalParams,
                ),
            ),
            model=WaapBillingReportItem,
        )


class PrebillingResourceWithRawResponse:
    def __init__(self, prebilling: PrebillingResource) -> None:
        self._prebilling = prebilling

        self.get_total = to_raw_response_wrapper(
            prebilling.get_total,
        )


class AsyncPrebillingResourceWithRawResponse:
    def __init__(self, prebilling: AsyncPrebillingResource) -> None:
        self._prebilling = prebilling

        self.get_total = async_to_raw_response_wrapper(
            prebilling.get_total,
        )


class PrebillingResourceWithStreamingResponse:
    def __init__(self, prebilling: PrebillingResource) -> None:
        self._prebilling = prebilling

        self.get_total = to_streamed_response_wrapper(
            prebilling.get_total,
        )


class AsyncPrebillingResourceWithStreamingResponse:
    def __init__(self, prebilling: AsyncPrebillingResource) -> None:
        self._prebilling = prebilling

        self.get_total = async_to_streamed_response_wrapper(
            prebilling.get_total,
        )

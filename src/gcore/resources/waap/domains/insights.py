# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.waap.domains import insight_list_params, insight_replace_params
from ....types.waap.domains.waap_insight import WaapInsight

__all__ = ["InsightsResource", "AsyncInsightsResource"]


class InsightsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return InsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return InsightsResourceWithStreamingResponse(self)

    def list(
        self,
        domain_id: int,
        *,
        id: Optional[SequenceNotStr[str]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        insight_type: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal[
            "id",
            "-id",
            "insight_type",
            "-insight_type",
            "first_seen",
            "-first_seen",
            "last_seen",
            "-last_seen",
            "last_status_change",
            "-last_status_change",
            "status",
            "-status",
        ]
        | Omit = omit,
        status: Optional[List[Literal["OPEN", "ACKED", "CLOSED"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapInsight]:
        """
        Retrieve a list of insights for a specific domain.

        Args:
          domain_id: The domain ID

          id: The ID of the insight

          description: The description of the insight. Supports '\\**' as a wildcard.

          insight_type: The type of the insight

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Sort the response by given field.

          status: The status of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/insights",
            page=SyncOffsetPage[WaapInsight],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "description": description,
                        "insight_type": insight_type,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "status": status,
                    },
                    insight_list_params.InsightListParams,
                ),
            ),
            model=WaapInsight,
        )

    def get(
        self,
        insight_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapInsight:
        """
        Retrieve a specific insight for a specific domain.

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return self._get(
            f"/waap/v1/domains/{domain_id}/insights/{insight_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapInsight,
        )

    def replace(
        self,
        insight_id: str,
        *,
        domain_id: int,
        status: Literal["OPEN", "ACKED", "CLOSED"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapInsight:
        """
        Update the status of an insight for a specific domain.

        Args:
          domain_id: The domain ID

          insight_id: The ID of the insight

          status: The status of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return self._put(
            f"/waap/v1/domains/{domain_id}/insights/{insight_id}",
            body=maybe_transform({"status": status}, insight_replace_params.InsightReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapInsight,
        )


class AsyncInsightsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncInsightsResourceWithStreamingResponse(self)

    def list(
        self,
        domain_id: int,
        *,
        id: Optional[SequenceNotStr[str]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        insight_type: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal[
            "id",
            "-id",
            "insight_type",
            "-insight_type",
            "first_seen",
            "-first_seen",
            "last_seen",
            "-last_seen",
            "last_status_change",
            "-last_status_change",
            "status",
            "-status",
        ]
        | Omit = omit,
        status: Optional[List[Literal["OPEN", "ACKED", "CLOSED"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapInsight, AsyncOffsetPage[WaapInsight]]:
        """
        Retrieve a list of insights for a specific domain.

        Args:
          domain_id: The domain ID

          id: The ID of the insight

          description: The description of the insight. Supports '\\**' as a wildcard.

          insight_type: The type of the insight

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Sort the response by given field.

          status: The status of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/insights",
            page=AsyncOffsetPage[WaapInsight],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "description": description,
                        "insight_type": insight_type,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "status": status,
                    },
                    insight_list_params.InsightListParams,
                ),
            ),
            model=WaapInsight,
        )

    async def get(
        self,
        insight_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapInsight:
        """
        Retrieve a specific insight for a specific domain.

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return await self._get(
            f"/waap/v1/domains/{domain_id}/insights/{insight_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapInsight,
        )

    async def replace(
        self,
        insight_id: str,
        *,
        domain_id: int,
        status: Literal["OPEN", "ACKED", "CLOSED"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapInsight:
        """
        Update the status of an insight for a specific domain.

        Args:
          domain_id: The domain ID

          insight_id: The ID of the insight

          status: The status of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return await self._put(
            f"/waap/v1/domains/{domain_id}/insights/{insight_id}",
            body=await async_maybe_transform({"status": status}, insight_replace_params.InsightReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapInsight,
        )


class InsightsResourceWithRawResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.list = to_raw_response_wrapper(
            insights.list,
        )
        self.get = to_raw_response_wrapper(
            insights.get,
        )
        self.replace = to_raw_response_wrapper(
            insights.replace,
        )


class AsyncInsightsResourceWithRawResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.list = async_to_raw_response_wrapper(
            insights.list,
        )
        self.get = async_to_raw_response_wrapper(
            insights.get,
        )
        self.replace = async_to_raw_response_wrapper(
            insights.replace,
        )


class InsightsResourceWithStreamingResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.list = to_streamed_response_wrapper(
            insights.list,
        )
        self.get = to_streamed_response_wrapper(
            insights.get,
        )
        self.replace = to_streamed_response_wrapper(
            insights.replace,
        )


class AsyncInsightsResourceWithStreamingResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.list = async_to_streamed_response_wrapper(
            insights.list,
        )
        self.get = async_to_streamed_response_wrapper(
            insights.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            insights.replace,
        )

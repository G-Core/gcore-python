# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.waap.domains import (
    insight_silence_list_params,
    insight_silence_create_params,
    insight_silence_update_params,
)
from ....types.waap.domains.waap_insight_silence import WaapInsightSilence

__all__ = ["InsightSilencesResource", "AsyncInsightSilencesResource"]


class InsightSilencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InsightSilencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return InsightSilencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightSilencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return InsightSilencesResourceWithStreamingResponse(self)

    def create(
        self,
        domain_id: int,
        *,
        author: str,
        comment: str,
        insight_type: str,
        labels: Dict[str, str],
        expire_at: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapInsightSilence:
        """Create a new insight silence for a specified domain.

        Insight silences help in
        temporarily disabling certain insights based on specific criteria.

        Args:
          domain_id: The domain ID

          author: The author of the silence

          comment: A comment explaining the reason for the silence

          insight_type: The slug of the insight type

          labels: A hash table of label names and values that apply to the insight silence

          expire_at: The date and time the silence expires in ISO 8601 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/waap/v1/domains/{domain_id}/insight-silences",
            body=maybe_transform(
                {
                    "author": author,
                    "comment": comment,
                    "insight_type": insight_type,
                    "labels": labels,
                    "expire_at": expire_at,
                },
                insight_silence_create_params.InsightSilenceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapInsightSilence,
        )

    def update(
        self,
        silence_id: str,
        *,
        domain_id: int,
        author: str,
        comment: str,
        expire_at: Union[str, datetime, None],
        labels: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapInsightSilence:
        """
        Update an insight silence for a specific domain.

        Args:
          domain_id: The domain ID

          silence_id: A generated unique identifier for the silence

          author: The author of the silence

          comment: A comment explaining the reason for the silence

          expire_at: The date and time the silence expires in ISO 8601 format

          labels: A hash table of label names and values that apply to the insight silence

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not silence_id:
            raise ValueError(f"Expected a non-empty value for `silence_id` but received {silence_id!r}")
        return self._patch(
            f"/waap/v1/domains/{domain_id}/insight-silences/{silence_id}",
            body=maybe_transform(
                {
                    "author": author,
                    "comment": comment,
                    "expire_at": expire_at,
                    "labels": labels,
                },
                insight_silence_update_params.InsightSilenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapInsightSilence,
        )

    def list(
        self,
        domain_id: int,
        *,
        id: Optional[SequenceNotStr[str]] | Omit = omit,
        author: Optional[str] | Omit = omit,
        comment: Optional[str] | Omit = omit,
        insight_type: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal[
            "id",
            "-id",
            "insight_type",
            "-insight_type",
            "comment",
            "-comment",
            "author",
            "-author",
            "expire_at",
            "-expire_at",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapInsightSilence]:
        """
        Retrieve a list of insight silences for a specific domain

        Args:
          domain_id: The domain ID

          id: The ID of the insight silence

          author: The author of the insight silence

          comment: The comment of the insight silence

          insight_type: The type of the insight silence

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Sort the response by given field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/insight-silences",
            page=SyncOffsetPage[WaapInsightSilence],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "author": author,
                        "comment": comment,
                        "insight_type": insight_type,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                    },
                    insight_silence_list_params.InsightSilenceListParams,
                ),
            ),
            model=WaapInsightSilence,
        )

    def delete(
        self,
        silence_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an insight silence for a specific domain.

        Args:
          domain_id: The domain ID

          silence_id: A generated unique identifier for the silence

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not silence_id:
            raise ValueError(f"Expected a non-empty value for `silence_id` but received {silence_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/waap/v1/domains/{domain_id}/insight-silences/{silence_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        silence_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapInsightSilence:
        """
        Retrieve a specific insight silence for a specific domain

        Args:
          domain_id: The domain ID

          silence_id: A generated unique identifier for the silence

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not silence_id:
            raise ValueError(f"Expected a non-empty value for `silence_id` but received {silence_id!r}")
        return self._get(
            f"/waap/v1/domains/{domain_id}/insight-silences/{silence_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapInsightSilence,
        )


class AsyncInsightSilencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInsightSilencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsightSilencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightSilencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncInsightSilencesResourceWithStreamingResponse(self)

    async def create(
        self,
        domain_id: int,
        *,
        author: str,
        comment: str,
        insight_type: str,
        labels: Dict[str, str],
        expire_at: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapInsightSilence:
        """Create a new insight silence for a specified domain.

        Insight silences help in
        temporarily disabling certain insights based on specific criteria.

        Args:
          domain_id: The domain ID

          author: The author of the silence

          comment: A comment explaining the reason for the silence

          insight_type: The slug of the insight type

          labels: A hash table of label names and values that apply to the insight silence

          expire_at: The date and time the silence expires in ISO 8601 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/waap/v1/domains/{domain_id}/insight-silences",
            body=await async_maybe_transform(
                {
                    "author": author,
                    "comment": comment,
                    "insight_type": insight_type,
                    "labels": labels,
                    "expire_at": expire_at,
                },
                insight_silence_create_params.InsightSilenceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapInsightSilence,
        )

    async def update(
        self,
        silence_id: str,
        *,
        domain_id: int,
        author: str,
        comment: str,
        expire_at: Union[str, datetime, None],
        labels: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapInsightSilence:
        """
        Update an insight silence for a specific domain.

        Args:
          domain_id: The domain ID

          silence_id: A generated unique identifier for the silence

          author: The author of the silence

          comment: A comment explaining the reason for the silence

          expire_at: The date and time the silence expires in ISO 8601 format

          labels: A hash table of label names and values that apply to the insight silence

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not silence_id:
            raise ValueError(f"Expected a non-empty value for `silence_id` but received {silence_id!r}")
        return await self._patch(
            f"/waap/v1/domains/{domain_id}/insight-silences/{silence_id}",
            body=await async_maybe_transform(
                {
                    "author": author,
                    "comment": comment,
                    "expire_at": expire_at,
                    "labels": labels,
                },
                insight_silence_update_params.InsightSilenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapInsightSilence,
        )

    def list(
        self,
        domain_id: int,
        *,
        id: Optional[SequenceNotStr[str]] | Omit = omit,
        author: Optional[str] | Omit = omit,
        comment: Optional[str] | Omit = omit,
        insight_type: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal[
            "id",
            "-id",
            "insight_type",
            "-insight_type",
            "comment",
            "-comment",
            "author",
            "-author",
            "expire_at",
            "-expire_at",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapInsightSilence, AsyncOffsetPage[WaapInsightSilence]]:
        """
        Retrieve a list of insight silences for a specific domain

        Args:
          domain_id: The domain ID

          id: The ID of the insight silence

          author: The author of the insight silence

          comment: The comment of the insight silence

          insight_type: The type of the insight silence

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Sort the response by given field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/insight-silences",
            page=AsyncOffsetPage[WaapInsightSilence],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "author": author,
                        "comment": comment,
                        "insight_type": insight_type,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                    },
                    insight_silence_list_params.InsightSilenceListParams,
                ),
            ),
            model=WaapInsightSilence,
        )

    async def delete(
        self,
        silence_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an insight silence for a specific domain.

        Args:
          domain_id: The domain ID

          silence_id: A generated unique identifier for the silence

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not silence_id:
            raise ValueError(f"Expected a non-empty value for `silence_id` but received {silence_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/waap/v1/domains/{domain_id}/insight-silences/{silence_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        silence_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapInsightSilence:
        """
        Retrieve a specific insight silence for a specific domain

        Args:
          domain_id: The domain ID

          silence_id: A generated unique identifier for the silence

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not silence_id:
            raise ValueError(f"Expected a non-empty value for `silence_id` but received {silence_id!r}")
        return await self._get(
            f"/waap/v1/domains/{domain_id}/insight-silences/{silence_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapInsightSilence,
        )


class InsightSilencesResourceWithRawResponse:
    def __init__(self, insight_silences: InsightSilencesResource) -> None:
        self._insight_silences = insight_silences

        self.create = to_raw_response_wrapper(
            insight_silences.create,
        )
        self.update = to_raw_response_wrapper(
            insight_silences.update,
        )
        self.list = to_raw_response_wrapper(
            insight_silences.list,
        )
        self.delete = to_raw_response_wrapper(
            insight_silences.delete,
        )
        self.get = to_raw_response_wrapper(
            insight_silences.get,
        )


class AsyncInsightSilencesResourceWithRawResponse:
    def __init__(self, insight_silences: AsyncInsightSilencesResource) -> None:
        self._insight_silences = insight_silences

        self.create = async_to_raw_response_wrapper(
            insight_silences.create,
        )
        self.update = async_to_raw_response_wrapper(
            insight_silences.update,
        )
        self.list = async_to_raw_response_wrapper(
            insight_silences.list,
        )
        self.delete = async_to_raw_response_wrapper(
            insight_silences.delete,
        )
        self.get = async_to_raw_response_wrapper(
            insight_silences.get,
        )


class InsightSilencesResourceWithStreamingResponse:
    def __init__(self, insight_silences: InsightSilencesResource) -> None:
        self._insight_silences = insight_silences

        self.create = to_streamed_response_wrapper(
            insight_silences.create,
        )
        self.update = to_streamed_response_wrapper(
            insight_silences.update,
        )
        self.list = to_streamed_response_wrapper(
            insight_silences.list,
        )
        self.delete = to_streamed_response_wrapper(
            insight_silences.delete,
        )
        self.get = to_streamed_response_wrapper(
            insight_silences.get,
        )


class AsyncInsightSilencesResourceWithStreamingResponse:
    def __init__(self, insight_silences: AsyncInsightSilencesResource) -> None:
        self._insight_silences = insight_silences

        self.create = async_to_streamed_response_wrapper(
            insight_silences.create,
        )
        self.update = async_to_streamed_response_wrapper(
            insight_silences.update,
        )
        self.list = async_to_streamed_response_wrapper(
            insight_silences.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            insight_silences.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            insight_silences.get,
        )

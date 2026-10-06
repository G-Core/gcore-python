# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.waap import filter_template_list_params, filter_template_create_params, filter_template_update_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.waap.waap_filter_template import WaapFilterTemplate

__all__ = ["FilterTemplatesResource", "AsyncFilterTemplatesResource"]


class FilterTemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilterTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return FilterTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilterTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return FilterTemplatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        filter_config: Dict[str, object],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapFilterTemplate:
        """
        Create a filter template for the authenticated user.

        Args:
          filter_config: Arbitrary JSON object storing the frontend filter state

          name: Human-readable template name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/waap/v1/filter-templates",
            body=maybe_transform(
                {
                    "filter_config": filter_config,
                    "name": name,
                },
                filter_template_create_params.FilterTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapFilterTemplate,
        )

    def update(
        self,
        template_id: int,
        *,
        filter_config: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapFilterTemplate:
        """
        Update or rename a filter template owned by the authenticated user.

        Args:
          template_id: The ID of the filter template

          filter_config: Arbitrary JSON object storing the frontend filter state

          name: Human-readable template name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/waap/v1/filter-templates/{template_id}", template_id=template_id),
            body=maybe_transform(
                {
                    "filter_config": filter_config,
                    "name": name,
                },
                filter_template_update_params.FilterTemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapFilterTemplate,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapFilterTemplate]:
        """
        List filter templates owned by the authenticated user.

        Args:
          limit: Number of items to return

          name: Filter template names by case-insensitive substring match

          offset: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v1/filter-templates",
            page=SyncOffsetPage[WaapFilterTemplate],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                    },
                    filter_template_list_params.FilterTemplateListParams,
                ),
            ),
            model=WaapFilterTemplate,
        )

    def delete(
        self,
        template_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a filter template owned by the authenticated user.

        Args:
          template_id: The ID of the filter template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/waap/v1/filter-templates/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        template_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapFilterTemplate:
        """
        Retrieve a single filter template, scoped to the authenticated user.

        Args:
          template_id: The ID of the filter template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/waap/v1/filter-templates/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapFilterTemplate,
        )


class AsyncFilterTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilterTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilterTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilterTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncFilterTemplatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        filter_config: Dict[str, object],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapFilterTemplate:
        """
        Create a filter template for the authenticated user.

        Args:
          filter_config: Arbitrary JSON object storing the frontend filter state

          name: Human-readable template name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/waap/v1/filter-templates",
            body=await async_maybe_transform(
                {
                    "filter_config": filter_config,
                    "name": name,
                },
                filter_template_create_params.FilterTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapFilterTemplate,
        )

    async def update(
        self,
        template_id: int,
        *,
        filter_config: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapFilterTemplate:
        """
        Update or rename a filter template owned by the authenticated user.

        Args:
          template_id: The ID of the filter template

          filter_config: Arbitrary JSON object storing the frontend filter state

          name: Human-readable template name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/waap/v1/filter-templates/{template_id}", template_id=template_id),
            body=await async_maybe_transform(
                {
                    "filter_config": filter_config,
                    "name": name,
                },
                filter_template_update_params.FilterTemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapFilterTemplate,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapFilterTemplate, AsyncOffsetPage[WaapFilterTemplate]]:
        """
        List filter templates owned by the authenticated user.

        Args:
          limit: Number of items to return

          name: Filter template names by case-insensitive substring match

          offset: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v1/filter-templates",
            page=AsyncOffsetPage[WaapFilterTemplate],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                    },
                    filter_template_list_params.FilterTemplateListParams,
                ),
            ),
            model=WaapFilterTemplate,
        )

    async def delete(
        self,
        template_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a filter template owned by the authenticated user.

        Args:
          template_id: The ID of the filter template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/waap/v1/filter-templates/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        template_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapFilterTemplate:
        """
        Retrieve a single filter template, scoped to the authenticated user.

        Args:
          template_id: The ID of the filter template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/waap/v1/filter-templates/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapFilterTemplate,
        )


class FilterTemplatesResourceWithRawResponse:
    def __init__(self, filter_templates: FilterTemplatesResource) -> None:
        self._filter_templates = filter_templates

        self.create = to_raw_response_wrapper(
            filter_templates.create,
        )
        self.update = to_raw_response_wrapper(
            filter_templates.update,
        )
        self.list = to_raw_response_wrapper(
            filter_templates.list,
        )
        self.delete = to_raw_response_wrapper(
            filter_templates.delete,
        )
        self.get = to_raw_response_wrapper(
            filter_templates.get,
        )


class AsyncFilterTemplatesResourceWithRawResponse:
    def __init__(self, filter_templates: AsyncFilterTemplatesResource) -> None:
        self._filter_templates = filter_templates

        self.create = async_to_raw_response_wrapper(
            filter_templates.create,
        )
        self.update = async_to_raw_response_wrapper(
            filter_templates.update,
        )
        self.list = async_to_raw_response_wrapper(
            filter_templates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            filter_templates.delete,
        )
        self.get = async_to_raw_response_wrapper(
            filter_templates.get,
        )


class FilterTemplatesResourceWithStreamingResponse:
    def __init__(self, filter_templates: FilterTemplatesResource) -> None:
        self._filter_templates = filter_templates

        self.create = to_streamed_response_wrapper(
            filter_templates.create,
        )
        self.update = to_streamed_response_wrapper(
            filter_templates.update,
        )
        self.list = to_streamed_response_wrapper(
            filter_templates.list,
        )
        self.delete = to_streamed_response_wrapper(
            filter_templates.delete,
        )
        self.get = to_streamed_response_wrapper(
            filter_templates.get,
        )


class AsyncFilterTemplatesResourceWithStreamingResponse:
    def __init__(self, filter_templates: AsyncFilterTemplatesResource) -> None:
        self._filter_templates = filter_templates

        self.create = async_to_streamed_response_wrapper(
            filter_templates.create,
        )
        self.update = async_to_streamed_response_wrapper(
            filter_templates.update,
        )
        self.list = async_to_streamed_response_wrapper(
            filter_templates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            filter_templates.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            filter_templates.get,
        )

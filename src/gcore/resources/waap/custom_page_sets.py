# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.waap import (
    WaapPageType,
    custom_page_set_list_params,
    custom_page_set_create_params,
    custom_page_set_update_params,
    custom_page_set_preview_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.waap.waap_page_type import WaapPageType
from ...types.waap.waap_custom_page_set import WaapCustomPageSet
from ...types.waap.waap_custom_page_preview import WaapCustomPagePreview
from ...types.waap.waap_block_page_data_param import WaapBlockPageDataParam
from ...types.waap.waap_captcha_page_data_param import WaapCaptchaPageDataParam
from ...types.waap.waap_handshake_page_data_param import WaapHandshakePageDataParam
from ...types.waap.waap_block_csrf_page_data_param import WaapBlockCsrfPageDataParam
from ...types.waap.waap_cookie_disabled_page_data_param import WaapCookieDisabledPageDataParam
from ...types.waap.waap_javascript_disabled_page_data_param import WaapJavascriptDisabledPageDataParam

__all__ = ["CustomPageSetsResource", "AsyncCustomPageSetsResource"]


class CustomPageSetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomPageSetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return CustomPageSetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomPageSetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return CustomPageSetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        block: Optional[WaapBlockPageDataParam] | NotGiven = NOT_GIVEN,
        block_csrf: Optional[WaapBlockCsrfPageDataParam] | NotGiven = NOT_GIVEN,
        captcha: Optional[WaapCaptchaPageDataParam] | NotGiven = NOT_GIVEN,
        cookie_disabled: Optional[WaapCookieDisabledPageDataParam] | NotGiven = NOT_GIVEN,
        domains: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        handshake: Optional[WaapHandshakePageDataParam] | NotGiven = NOT_GIVEN,
        javascript_disabled: Optional[WaapJavascriptDisabledPageDataParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapCustomPageSet:
        """Create a custom page set based on the provided data.

        For any custom page type
        (block, `block_csrf`, etc) that is not provided the default page will be used.

        Args:
          name: Name of the custom page set

          domains: List of domain IDs that are associated with this page set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/waap/v1/custom-page-sets",
            body=maybe_transform(
                {
                    "name": name,
                    "block": block,
                    "block_csrf": block_csrf,
                    "captcha": captcha,
                    "cookie_disabled": cookie_disabled,
                    "domains": domains,
                    "handshake": handshake,
                    "javascript_disabled": javascript_disabled,
                },
                custom_page_set_create_params.CustomPageSetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapCustomPageSet,
        )

    def update(
        self,
        set_id: int,
        *,
        block: Optional[WaapBlockPageDataParam] | NotGiven = NOT_GIVEN,
        block_csrf: Optional[WaapBlockCsrfPageDataParam] | NotGiven = NOT_GIVEN,
        captcha: Optional[WaapCaptchaPageDataParam] | NotGiven = NOT_GIVEN,
        cookie_disabled: Optional[WaapCookieDisabledPageDataParam] | NotGiven = NOT_GIVEN,
        domains: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        handshake: Optional[WaapHandshakePageDataParam] | NotGiven = NOT_GIVEN,
        javascript_disabled: Optional[WaapJavascriptDisabledPageDataParam] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Update a custom page set based on the provided parameters.

        To update a field,
        provide the field with the new value. To remove a field, provide it as null. To
        keep a field unaltered, do not include it in the request. Note: `name` cannot be
        removed. When updating a custom page, include all the fields that you want it to
        have. Any field not included will be removed.

        Args:
          set_id: The ID of the custom page set

          domains: List of domain IDs that are associated with this page set

          name: Name of the custom page set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/waap/v1/custom-page-sets/{set_id}",
            body=maybe_transform(
                {
                    "block": block,
                    "block_csrf": block_csrf,
                    "captcha": captcha,
                    "cookie_disabled": cookie_disabled,
                    "domains": domains,
                    "handshake": handshake,
                    "javascript_disabled": javascript_disabled,
                    "name": name,
                },
                custom_page_set_update_params.CustomPageSetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ids: Iterable[int] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        ordering: Literal["name", "-name", "id", "-id"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[WaapCustomPageSet]:
        """
        Retrieve a list of custom page sets available for use

        Args:
          ids: Filter page sets based on their IDs

          limit: Number of items to return

          name: Filter page sets based on their name. Supports '\\**' as a wildcard character

          offset: Number of items to skip

          ordering: Sort the response by given field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v1/custom-page-sets",
            page=SyncOffsetPage[WaapCustomPageSet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                    },
                    custom_page_set_list_params.CustomPageSetListParams,
                ),
            ),
            model=WaapCustomPageSet,
        )

    def delete(
        self,
        set_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a custom page set

        Args:
          set_id: The ID of the custom page set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/waap/v1/custom-page-sets/{set_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        set_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapCustomPageSet:
        """
        Retrieve a custom page set based on the provided ID

        Args:
          set_id: The ID of the custom page set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/waap/v1/custom-page-sets/{set_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapCustomPageSet,
        )

    def preview(
        self,
        *,
        page_type: WaapPageType,
        error: Optional[str] | NotGiven = NOT_GIVEN,
        header: Optional[str] | NotGiven = NOT_GIVEN,
        logo: Optional[str] | NotGiven = NOT_GIVEN,
        text: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapCustomPagePreview:
        """
        Allows to preview a custom page without creating it based on the provided type
        and data

        Args:
          page_type: The type of the custom page

          error: Error message

          header: The text to display in the header of the custom page

          logo: Supported image types are JPEG, PNG and JPG, size is limited to width 450px,
              height 130px. This should be a base 64 encoding of the full HTML img tag
              compatible image, with the header included.

          text: The text to display in the body of the custom page

          title: The text to display in the title of the custom page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/waap/v1/preview-custom-page",
            body=maybe_transform(
                {
                    "error": error,
                    "header": header,
                    "logo": logo,
                    "text": text,
                    "title": title,
                },
                custom_page_set_preview_params.CustomPageSetPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"page_type": page_type}, custom_page_set_preview_params.CustomPageSetPreviewParams
                ),
            ),
            cast_to=WaapCustomPagePreview,
        )


class AsyncCustomPageSetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomPageSetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomPageSetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomPageSetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncCustomPageSetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        block: Optional[WaapBlockPageDataParam] | NotGiven = NOT_GIVEN,
        block_csrf: Optional[WaapBlockCsrfPageDataParam] | NotGiven = NOT_GIVEN,
        captcha: Optional[WaapCaptchaPageDataParam] | NotGiven = NOT_GIVEN,
        cookie_disabled: Optional[WaapCookieDisabledPageDataParam] | NotGiven = NOT_GIVEN,
        domains: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        handshake: Optional[WaapHandshakePageDataParam] | NotGiven = NOT_GIVEN,
        javascript_disabled: Optional[WaapJavascriptDisabledPageDataParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapCustomPageSet:
        """Create a custom page set based on the provided data.

        For any custom page type
        (block, `block_csrf`, etc) that is not provided the default page will be used.

        Args:
          name: Name of the custom page set

          domains: List of domain IDs that are associated with this page set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/waap/v1/custom-page-sets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "block": block,
                    "block_csrf": block_csrf,
                    "captcha": captcha,
                    "cookie_disabled": cookie_disabled,
                    "domains": domains,
                    "handshake": handshake,
                    "javascript_disabled": javascript_disabled,
                },
                custom_page_set_create_params.CustomPageSetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapCustomPageSet,
        )

    async def update(
        self,
        set_id: int,
        *,
        block: Optional[WaapBlockPageDataParam] | NotGiven = NOT_GIVEN,
        block_csrf: Optional[WaapBlockCsrfPageDataParam] | NotGiven = NOT_GIVEN,
        captcha: Optional[WaapCaptchaPageDataParam] | NotGiven = NOT_GIVEN,
        cookie_disabled: Optional[WaapCookieDisabledPageDataParam] | NotGiven = NOT_GIVEN,
        domains: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        handshake: Optional[WaapHandshakePageDataParam] | NotGiven = NOT_GIVEN,
        javascript_disabled: Optional[WaapJavascriptDisabledPageDataParam] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Update a custom page set based on the provided parameters.

        To update a field,
        provide the field with the new value. To remove a field, provide it as null. To
        keep a field unaltered, do not include it in the request. Note: `name` cannot be
        removed. When updating a custom page, include all the fields that you want it to
        have. Any field not included will be removed.

        Args:
          set_id: The ID of the custom page set

          domains: List of domain IDs that are associated with this page set

          name: Name of the custom page set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/waap/v1/custom-page-sets/{set_id}",
            body=await async_maybe_transform(
                {
                    "block": block,
                    "block_csrf": block_csrf,
                    "captcha": captcha,
                    "cookie_disabled": cookie_disabled,
                    "domains": domains,
                    "handshake": handshake,
                    "javascript_disabled": javascript_disabled,
                    "name": name,
                },
                custom_page_set_update_params.CustomPageSetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ids: Iterable[int] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        ordering: Literal["name", "-name", "id", "-id"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WaapCustomPageSet, AsyncOffsetPage[WaapCustomPageSet]]:
        """
        Retrieve a list of custom page sets available for use

        Args:
          ids: Filter page sets based on their IDs

          limit: Number of items to return

          name: Filter page sets based on their name. Supports '\\**' as a wildcard character

          offset: Number of items to skip

          ordering: Sort the response by given field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v1/custom-page-sets",
            page=AsyncOffsetPage[WaapCustomPageSet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                    },
                    custom_page_set_list_params.CustomPageSetListParams,
                ),
            ),
            model=WaapCustomPageSet,
        )

    async def delete(
        self,
        set_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a custom page set

        Args:
          set_id: The ID of the custom page set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/waap/v1/custom-page-sets/{set_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        set_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapCustomPageSet:
        """
        Retrieve a custom page set based on the provided ID

        Args:
          set_id: The ID of the custom page set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/waap/v1/custom-page-sets/{set_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapCustomPageSet,
        )

    async def preview(
        self,
        *,
        page_type: WaapPageType,
        error: Optional[str] | NotGiven = NOT_GIVEN,
        header: Optional[str] | NotGiven = NOT_GIVEN,
        logo: Optional[str] | NotGiven = NOT_GIVEN,
        text: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapCustomPagePreview:
        """
        Allows to preview a custom page without creating it based on the provided type
        and data

        Args:
          page_type: The type of the custom page

          error: Error message

          header: The text to display in the header of the custom page

          logo: Supported image types are JPEG, PNG and JPG, size is limited to width 450px,
              height 130px. This should be a base 64 encoding of the full HTML img tag
              compatible image, with the header included.

          text: The text to display in the body of the custom page

          title: The text to display in the title of the custom page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/waap/v1/preview-custom-page",
            body=await async_maybe_transform(
                {
                    "error": error,
                    "header": header,
                    "logo": logo,
                    "text": text,
                    "title": title,
                },
                custom_page_set_preview_params.CustomPageSetPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page_type": page_type}, custom_page_set_preview_params.CustomPageSetPreviewParams
                ),
            ),
            cast_to=WaapCustomPagePreview,
        )


class CustomPageSetsResourceWithRawResponse:
    def __init__(self, custom_page_sets: CustomPageSetsResource) -> None:
        self._custom_page_sets = custom_page_sets

        self.create = to_raw_response_wrapper(
            custom_page_sets.create,
        )
        self.update = to_raw_response_wrapper(
            custom_page_sets.update,
        )
        self.list = to_raw_response_wrapper(
            custom_page_sets.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_page_sets.delete,
        )
        self.get = to_raw_response_wrapper(
            custom_page_sets.get,
        )
        self.preview = to_raw_response_wrapper(
            custom_page_sets.preview,
        )


class AsyncCustomPageSetsResourceWithRawResponse:
    def __init__(self, custom_page_sets: AsyncCustomPageSetsResource) -> None:
        self._custom_page_sets = custom_page_sets

        self.create = async_to_raw_response_wrapper(
            custom_page_sets.create,
        )
        self.update = async_to_raw_response_wrapper(
            custom_page_sets.update,
        )
        self.list = async_to_raw_response_wrapper(
            custom_page_sets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_page_sets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            custom_page_sets.get,
        )
        self.preview = async_to_raw_response_wrapper(
            custom_page_sets.preview,
        )


class CustomPageSetsResourceWithStreamingResponse:
    def __init__(self, custom_page_sets: CustomPageSetsResource) -> None:
        self._custom_page_sets = custom_page_sets

        self.create = to_streamed_response_wrapper(
            custom_page_sets.create,
        )
        self.update = to_streamed_response_wrapper(
            custom_page_sets.update,
        )
        self.list = to_streamed_response_wrapper(
            custom_page_sets.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_page_sets.delete,
        )
        self.get = to_streamed_response_wrapper(
            custom_page_sets.get,
        )
        self.preview = to_streamed_response_wrapper(
            custom_page_sets.preview,
        )


class AsyncCustomPageSetsResourceWithStreamingResponse:
    def __init__(self, custom_page_sets: AsyncCustomPageSetsResource) -> None:
        self._custom_page_sets = custom_page_sets

        self.create = async_to_streamed_response_wrapper(
            custom_page_sets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            custom_page_sets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_page_sets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_page_sets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_page_sets.get,
        )
        self.preview = async_to_streamed_response_wrapper(
            custom_page_sets.preview,
        )

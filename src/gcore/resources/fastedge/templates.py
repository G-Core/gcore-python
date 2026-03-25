# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

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
from ...pagination import SyncOffsetPageFastedgeTemplates, AsyncOffsetPageFastedgeTemplates
from ..._base_client import AsyncPaginator, make_request_options
from ...types.fastedge import (
    template_list_params,
    template_create_params,
    template_delete_params,
    template_replace_params,
)
from ...types.fastedge.template import Template
from ...types.fastedge.template_short import TemplateShort
from ...types.fastedge.template_parameter_param import TemplateParameterParam

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
    """
    FastEdge templates encapsulate reusable configurations for FastEdge applications, including a WebAssembly binary reference and configurable parameters.
    """

    @cached_property
    def with_raw_response(self) -> TemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return TemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return TemplatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        binary_id: int,
        name: str,
        owned: bool,
        params: Iterable[TemplateParameterParam],
        long_descr: str | Omit = omit,
        short_descr: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateShort:
        """
        Create a new application template from an existing binary and configuration.
        Templates can be shared with groups to enable collaborative application
        development.

        Args:
          binary_id: ID of the WebAssembly binary to use for this template

          name: Unique name for the template (used for identification and searching)

          owned: Is the template owned by user?

          params: Parameters

          long_descr: Detailed markdown description explaining template features and usage

          short_descr: Brief one-line description displayed in template listings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fastedge/v1/template",
            body=maybe_transform(
                {
                    "binary_id": binary_id,
                    "name": name,
                    "owned": owned,
                    "params": params,
                    "long_descr": long_descr,
                    "short_descr": short_descr,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateShort,
        )

    def list(
        self,
        *,
        api_type: Literal["wasi-http", "proxy-wasm"] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        only_mine: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPageFastedgeTemplates[TemplateShort]:
        """
        Retrieve available application templates including system templates and
        user-created templates. Templates provide pre-configured application settings
        that can be reused for quick deployment.

        Args:
          api_type:
              API type:
              wasi-http - WASI with HTTP entry point
              proxy-wasm - Proxy-Wasm app, callable from CDN

          limit: Maximum number of results to return

          offset: Number of results to skip for pagination

          only_mine: When true, returns only templates created by the client. When false, includes
              shared templates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/fastedge/v1/template",
            page=SyncOffsetPageFastedgeTemplates[TemplateShort],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "api_type": api_type,
                        "limit": limit,
                        "offset": offset,
                        "only_mine": only_mine,
                    },
                    template_list_params.TemplateListParams,
                ),
            ),
            model=TemplateShort,
        )

    def delete(
        self,
        template_id: int,
        *,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Remove a template from the platform.

        Templates shared with groups require
        force=true parameter to delete.

        Args:
          force: When true, deletes template even if shared with groups. Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/fastedge/v1/template/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force": force}, template_delete_params.TemplateDeleteParams),
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
    ) -> Template:
        """Retrieve complete configuration and metadata for a specific template.

        Use this
        to inspect template parameters before creating applications from it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/fastedge/v1/template/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Template,
        )

    def replace(
        self,
        template_id: int,
        *,
        binary_id: int,
        name: str,
        owned: bool,
        params: Iterable[TemplateParameterParam],
        long_descr: str | Omit = omit,
        short_descr: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateShort:
        """Modify an existing template's configuration.

        Updates affect future applications
        created from this template; existing apps are not changed.

        Args:
          binary_id: ID of the WebAssembly binary to use for this template

          name: Unique name for the template (used for identification and searching)

          owned: Is the template owned by user?

          params: Parameters

          long_descr: Detailed markdown description explaining template features and usage

          short_descr: Brief one-line description displayed in template listings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            path_template("/fastedge/v1/template/{template_id}", template_id=template_id),
            body=maybe_transform(
                {
                    "binary_id": binary_id,
                    "name": name,
                    "owned": owned,
                    "params": params,
                    "long_descr": long_descr,
                    "short_descr": short_descr,
                },
                template_replace_params.TemplateReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateShort,
        )


class AsyncTemplatesResource(AsyncAPIResource):
    """
    FastEdge templates encapsulate reusable configurations for FastEdge applications, including a WebAssembly binary reference and configurable parameters.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncTemplatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        binary_id: int,
        name: str,
        owned: bool,
        params: Iterable[TemplateParameterParam],
        long_descr: str | Omit = omit,
        short_descr: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateShort:
        """
        Create a new application template from an existing binary and configuration.
        Templates can be shared with groups to enable collaborative application
        development.

        Args:
          binary_id: ID of the WebAssembly binary to use for this template

          name: Unique name for the template (used for identification and searching)

          owned: Is the template owned by user?

          params: Parameters

          long_descr: Detailed markdown description explaining template features and usage

          short_descr: Brief one-line description displayed in template listings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fastedge/v1/template",
            body=await async_maybe_transform(
                {
                    "binary_id": binary_id,
                    "name": name,
                    "owned": owned,
                    "params": params,
                    "long_descr": long_descr,
                    "short_descr": short_descr,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateShort,
        )

    def list(
        self,
        *,
        api_type: Literal["wasi-http", "proxy-wasm"] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        only_mine: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TemplateShort, AsyncOffsetPageFastedgeTemplates[TemplateShort]]:
        """
        Retrieve available application templates including system templates and
        user-created templates. Templates provide pre-configured application settings
        that can be reused for quick deployment.

        Args:
          api_type:
              API type:
              wasi-http - WASI with HTTP entry point
              proxy-wasm - Proxy-Wasm app, callable from CDN

          limit: Maximum number of results to return

          offset: Number of results to skip for pagination

          only_mine: When true, returns only templates created by the client. When false, includes
              shared templates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/fastedge/v1/template",
            page=AsyncOffsetPageFastedgeTemplates[TemplateShort],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "api_type": api_type,
                        "limit": limit,
                        "offset": offset,
                        "only_mine": only_mine,
                    },
                    template_list_params.TemplateListParams,
                ),
            ),
            model=TemplateShort,
        )

    async def delete(
        self,
        template_id: int,
        *,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Remove a template from the platform.

        Templates shared with groups require
        force=true parameter to delete.

        Args:
          force: When true, deletes template even if shared with groups. Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/fastedge/v1/template/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"force": force}, template_delete_params.TemplateDeleteParams),
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
    ) -> Template:
        """Retrieve complete configuration and metadata for a specific template.

        Use this
        to inspect template parameters before creating applications from it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/fastedge/v1/template/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Template,
        )

    async def replace(
        self,
        template_id: int,
        *,
        binary_id: int,
        name: str,
        owned: bool,
        params: Iterable[TemplateParameterParam],
        long_descr: str | Omit = omit,
        short_descr: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateShort:
        """Modify an existing template's configuration.

        Updates affect future applications
        created from this template; existing apps are not changed.

        Args:
          binary_id: ID of the WebAssembly binary to use for this template

          name: Unique name for the template (used for identification and searching)

          owned: Is the template owned by user?

          params: Parameters

          long_descr: Detailed markdown description explaining template features and usage

          short_descr: Brief one-line description displayed in template listings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            path_template("/fastedge/v1/template/{template_id}", template_id=template_id),
            body=await async_maybe_transform(
                {
                    "binary_id": binary_id,
                    "name": name,
                    "owned": owned,
                    "params": params,
                    "long_descr": long_descr,
                    "short_descr": short_descr,
                },
                template_replace_params.TemplateReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateShort,
        )


class TemplatesResourceWithRawResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_raw_response_wrapper(
            templates.create,
        )
        self.list = to_raw_response_wrapper(
            templates.list,
        )
        self.delete = to_raw_response_wrapper(
            templates.delete,
        )
        self.get = to_raw_response_wrapper(
            templates.get,
        )
        self.replace = to_raw_response_wrapper(
            templates.replace,
        )


class AsyncTemplatesResourceWithRawResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_raw_response_wrapper(
            templates.create,
        )
        self.list = async_to_raw_response_wrapper(
            templates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            templates.delete,
        )
        self.get = async_to_raw_response_wrapper(
            templates.get,
        )
        self.replace = async_to_raw_response_wrapper(
            templates.replace,
        )


class TemplatesResourceWithStreamingResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_streamed_response_wrapper(
            templates.create,
        )
        self.list = to_streamed_response_wrapper(
            templates.list,
        )
        self.delete = to_streamed_response_wrapper(
            templates.delete,
        )
        self.get = to_streamed_response_wrapper(
            templates.get,
        )
        self.replace = to_streamed_response_wrapper(
            templates.replace,
        )


class AsyncTemplatesResourceWithStreamingResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_streamed_response_wrapper(
            templates.create,
        )
        self.list = async_to_streamed_response_wrapper(
            templates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            templates.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            templates.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            templates.replace,
        )

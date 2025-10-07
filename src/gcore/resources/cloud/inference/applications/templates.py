# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloud.inference.applications.inference_application_template import InferenceApplicationTemplate
from .....types.cloud.inference.applications.inference_application_template_list import InferenceApplicationTemplateList

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
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

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceApplicationTemplateList:
        """
        Returns a list of available machine learning application templates from the
        catalog. Each template includes metadata such as name, description, cover image,
        documentation, tags, and a set of configurable components (e.g., `model`, `ui`).
        Components define parameters, supported deployment flavors, and other attributes
        required to create a fully functional application deployment.
        """
        return self._get(
            "/cloud/v3/inference/applications/catalog",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceApplicationTemplateList,
        )

    def get(
        self,
        application_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceApplicationTemplate:
        """
        Retrieves detailed information about a specific machine learning application
        template from the catalog. The response includes the application’s metadata,
        documentation, tags, and a complete set of components with configuration
        options, compatible flavors, and deployment capabilities — all necessary for
        building and customizing an AI application.

        Args:
          application_name: Name of application in catalog

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_name:
            raise ValueError(f"Expected a non-empty value for `application_name` but received {application_name!r}")
        return self._get(
            f"/cloud/v3/inference/applications/catalog/{application_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceApplicationTemplate,
        )


class AsyncTemplatesResource(AsyncAPIResource):
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

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceApplicationTemplateList:
        """
        Returns a list of available machine learning application templates from the
        catalog. Each template includes metadata such as name, description, cover image,
        documentation, tags, and a set of configurable components (e.g., `model`, `ui`).
        Components define parameters, supported deployment flavors, and other attributes
        required to create a fully functional application deployment.
        """
        return await self._get(
            "/cloud/v3/inference/applications/catalog",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceApplicationTemplateList,
        )

    async def get(
        self,
        application_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceApplicationTemplate:
        """
        Retrieves detailed information about a specific machine learning application
        template from the catalog. The response includes the application’s metadata,
        documentation, tags, and a complete set of components with configuration
        options, compatible flavors, and deployment capabilities — all necessary for
        building and customizing an AI application.

        Args:
          application_name: Name of application in catalog

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_name:
            raise ValueError(f"Expected a non-empty value for `application_name` but received {application_name!r}")
        return await self._get(
            f"/cloud/v3/inference/applications/catalog/{application_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceApplicationTemplate,
        )


class TemplatesResourceWithRawResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.list = to_raw_response_wrapper(
            templates.list,
        )
        self.get = to_raw_response_wrapper(
            templates.get,
        )


class AsyncTemplatesResourceWithRawResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.list = async_to_raw_response_wrapper(
            templates.list,
        )
        self.get = async_to_raw_response_wrapper(
            templates.get,
        )


class TemplatesResourceWithStreamingResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.list = to_streamed_response_wrapper(
            templates.list,
        )
        self.get = to_streamed_response_wrapper(
            templates.get,
        )


class AsyncTemplatesResourceWithStreamingResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.list = async_to_streamed_response_wrapper(
            templates.list,
        )
        self.get = async_to_streamed_response_wrapper(
            templates.get,
        )

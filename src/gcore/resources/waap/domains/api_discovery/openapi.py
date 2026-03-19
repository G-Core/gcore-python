# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.waap.domains.api_discovery import openapi_upload_params
from .....types.waap.domains.api_discovery.waap_task_id import WaapTaskID

__all__ = ["OpenAPIResource", "AsyncOpenAPIResource"]


class OpenAPIResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OpenAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return OpenAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpenAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return OpenAPIResourceWithStreamingResponse(self)

    def scan(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapTaskID:
        """Scan an API description file hosted online.

        The file must be in YAML or JSON
        format and adhere to the OpenAPI specification. The location of the API
        description file should be specified in the API discovery settings.

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/waap/v1/domains/{domain_id}/api-discovery/scan", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapTaskID,
        )

    def upload(
        self,
        domain_id: int,
        *,
        file_data: str,
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapTaskID:
        """
        An API description file must adhere to the OpenAPI specification and be written
        in YAML or JSON format. The file name should be provided as the value for the
        `file_name` parameter. The contents of the file must be base64 encoded and
        supplied as the value for the `file_data` parameter.

        Args:
          domain_id: The domain ID

          file_data: Base64 representation of the description file. Supported formats are YAML and
              JSON, and it must adhere to OpenAPI versions 2, 3, or 3.1.

          file_name: The name of the file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/waap/v1/domains/{domain_id}/api-discovery/upload", domain_id=domain_id),
            body=maybe_transform(
                {
                    "file_data": file_data,
                    "file_name": file_name,
                },
                openapi_upload_params.OpenAPIUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapTaskID,
        )


class AsyncOpenAPIResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOpenAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOpenAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpenAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncOpenAPIResourceWithStreamingResponse(self)

    async def scan(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapTaskID:
        """Scan an API description file hosted online.

        The file must be in YAML or JSON
        format and adhere to the OpenAPI specification. The location of the API
        description file should be specified in the API discovery settings.

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/waap/v1/domains/{domain_id}/api-discovery/scan", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapTaskID,
        )

    async def upload(
        self,
        domain_id: int,
        *,
        file_data: str,
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapTaskID:
        """
        An API description file must adhere to the OpenAPI specification and be written
        in YAML or JSON format. The file name should be provided as the value for the
        `file_name` parameter. The contents of the file must be base64 encoded and
        supplied as the value for the `file_data` parameter.

        Args:
          domain_id: The domain ID

          file_data: Base64 representation of the description file. Supported formats are YAML and
              JSON, and it must adhere to OpenAPI versions 2, 3, or 3.1.

          file_name: The name of the file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/waap/v1/domains/{domain_id}/api-discovery/upload", domain_id=domain_id),
            body=await async_maybe_transform(
                {
                    "file_data": file_data,
                    "file_name": file_name,
                },
                openapi_upload_params.OpenAPIUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapTaskID,
        )


class OpenAPIResourceWithRawResponse:
    def __init__(self, openapi: OpenAPIResource) -> None:
        self._openapi = openapi

        self.scan = to_raw_response_wrapper(
            openapi.scan,
        )
        self.upload = to_raw_response_wrapper(
            openapi.upload,
        )


class AsyncOpenAPIResourceWithRawResponse:
    def __init__(self, openapi: AsyncOpenAPIResource) -> None:
        self._openapi = openapi

        self.scan = async_to_raw_response_wrapper(
            openapi.scan,
        )
        self.upload = async_to_raw_response_wrapper(
            openapi.upload,
        )


class OpenAPIResourceWithStreamingResponse:
    def __init__(self, openapi: OpenAPIResource) -> None:
        self._openapi = openapi

        self.scan = to_streamed_response_wrapper(
            openapi.scan,
        )
        self.upload = to_streamed_response_wrapper(
            openapi.upload,
        )


class AsyncOpenAPIResourceWithStreamingResponse:
    def __init__(self, openapi: AsyncOpenAPIResource) -> None:
        self._openapi = openapi

        self.scan = async_to_streamed_response_wrapper(
            openapi.scan,
        )
        self.upload = async_to_streamed_response_wrapper(
            openapi.upload,
        )

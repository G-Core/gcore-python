# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from .scan_results import (
    ScanResultsResource,
    AsyncScanResultsResource,
    ScanResultsResourceWithRawResponse,
    AsyncScanResultsResourceWithRawResponse,
    ScanResultsResourceWithStreamingResponse,
    AsyncScanResultsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.waap.domains import api_discovery_upload_openapi_params, api_discovery_update_settings_params
from .....types.waap.domains.api_discovery_get_settings_response import APIDiscoveryGetSettingsResponse
from .....types.waap.domains.api_discovery_scan_openapi_response import APIDiscoveryScanOpenAPIResponse
from .....types.waap.domains.api_discovery_upload_openapi_response import APIDiscoveryUploadOpenAPIResponse
from .....types.waap.domains.api_discovery_update_settings_response import APIDiscoveryUpdateSettingsResponse

__all__ = ["APIDiscoveryResource", "AsyncAPIDiscoveryResource"]


class APIDiscoveryResource(SyncAPIResource):
    @cached_property
    def scan_results(self) -> ScanResultsResource:
        return ScanResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIDiscoveryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return APIDiscoveryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIDiscoveryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return APIDiscoveryResourceWithStreamingResponse(self)

    def get_settings(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIDiscoveryGetSettingsResponse:
        """
        Retrieve the API discovery settings for a domain

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/waap/v1/domains/{domain_id}/api-discovery/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIDiscoveryGetSettingsResponse,
        )

    def scan_openapi(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIDiscoveryScanOpenAPIResponse:
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
            f"/waap/v1/domains/{domain_id}/api-discovery/scan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIDiscoveryScanOpenAPIResponse,
        )

    def update_settings(
        self,
        domain_id: int,
        *,
        description_file_location: Optional[str] | NotGiven = NOT_GIVEN,
        description_file_scan_enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        description_file_scan_interval_hours: Optional[int] | NotGiven = NOT_GIVEN,
        traffic_scan_enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        traffic_scan_interval_hours: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIDiscoveryUpdateSettingsResponse:
        """
        Update the API discovery settings for a domain

        Args:
          domain_id: The domain ID

          description_file_location: The URL of the API description file. This will be periodically scanned if
              `descriptionFileScanEnabled` is enabled. Supported formats are YAML and JSON,
              and it must adhere to OpenAPI versions 2, 3, or 3.1.

          description_file_scan_enabled: Indicates if periodic scan of the description file is enabled

          description_file_scan_interval_hours: The interval in hours for scanning the description file

          traffic_scan_enabled: Indicates if traffic scan is enabled

          traffic_scan_interval_hours: The interval in hours for scanning the traffic

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/waap/v1/domains/{domain_id}/api-discovery/settings",
            body=maybe_transform(
                {
                    "description_file_location": description_file_location,
                    "description_file_scan_enabled": description_file_scan_enabled,
                    "description_file_scan_interval_hours": description_file_scan_interval_hours,
                    "traffic_scan_enabled": traffic_scan_enabled,
                    "traffic_scan_interval_hours": traffic_scan_interval_hours,
                },
                api_discovery_update_settings_params.APIDiscoveryUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIDiscoveryUpdateSettingsResponse,
        )

    def upload_openapi(
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIDiscoveryUploadOpenAPIResponse:
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
            f"/waap/v1/domains/{domain_id}/api-discovery/upload",
            body=maybe_transform(
                {
                    "file_data": file_data,
                    "file_name": file_name,
                },
                api_discovery_upload_openapi_params.APIDiscoveryUploadOpenAPIParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIDiscoveryUploadOpenAPIResponse,
        )


class AsyncAPIDiscoveryResource(AsyncAPIResource):
    @cached_property
    def scan_results(self) -> AsyncScanResultsResource:
        return AsyncScanResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIDiscoveryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIDiscoveryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIDiscoveryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAPIDiscoveryResourceWithStreamingResponse(self)

    async def get_settings(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIDiscoveryGetSettingsResponse:
        """
        Retrieve the API discovery settings for a domain

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/waap/v1/domains/{domain_id}/api-discovery/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIDiscoveryGetSettingsResponse,
        )

    async def scan_openapi(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIDiscoveryScanOpenAPIResponse:
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
            f"/waap/v1/domains/{domain_id}/api-discovery/scan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIDiscoveryScanOpenAPIResponse,
        )

    async def update_settings(
        self,
        domain_id: int,
        *,
        description_file_location: Optional[str] | NotGiven = NOT_GIVEN,
        description_file_scan_enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        description_file_scan_interval_hours: Optional[int] | NotGiven = NOT_GIVEN,
        traffic_scan_enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        traffic_scan_interval_hours: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIDiscoveryUpdateSettingsResponse:
        """
        Update the API discovery settings for a domain

        Args:
          domain_id: The domain ID

          description_file_location: The URL of the API description file. This will be periodically scanned if
              `descriptionFileScanEnabled` is enabled. Supported formats are YAML and JSON,
              and it must adhere to OpenAPI versions 2, 3, or 3.1.

          description_file_scan_enabled: Indicates if periodic scan of the description file is enabled

          description_file_scan_interval_hours: The interval in hours for scanning the description file

          traffic_scan_enabled: Indicates if traffic scan is enabled

          traffic_scan_interval_hours: The interval in hours for scanning the traffic

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/waap/v1/domains/{domain_id}/api-discovery/settings",
            body=await async_maybe_transform(
                {
                    "description_file_location": description_file_location,
                    "description_file_scan_enabled": description_file_scan_enabled,
                    "description_file_scan_interval_hours": description_file_scan_interval_hours,
                    "traffic_scan_enabled": traffic_scan_enabled,
                    "traffic_scan_interval_hours": traffic_scan_interval_hours,
                },
                api_discovery_update_settings_params.APIDiscoveryUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIDiscoveryUpdateSettingsResponse,
        )

    async def upload_openapi(
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIDiscoveryUploadOpenAPIResponse:
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
            f"/waap/v1/domains/{domain_id}/api-discovery/upload",
            body=await async_maybe_transform(
                {
                    "file_data": file_data,
                    "file_name": file_name,
                },
                api_discovery_upload_openapi_params.APIDiscoveryUploadOpenAPIParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIDiscoveryUploadOpenAPIResponse,
        )


class APIDiscoveryResourceWithRawResponse:
    def __init__(self, api_discovery: APIDiscoveryResource) -> None:
        self._api_discovery = api_discovery

        self.get_settings = to_raw_response_wrapper(
            api_discovery.get_settings,
        )
        self.scan_openapi = to_raw_response_wrapper(
            api_discovery.scan_openapi,
        )
        self.update_settings = to_raw_response_wrapper(
            api_discovery.update_settings,
        )
        self.upload_openapi = to_raw_response_wrapper(
            api_discovery.upload_openapi,
        )

    @cached_property
    def scan_results(self) -> ScanResultsResourceWithRawResponse:
        return ScanResultsResourceWithRawResponse(self._api_discovery.scan_results)


class AsyncAPIDiscoveryResourceWithRawResponse:
    def __init__(self, api_discovery: AsyncAPIDiscoveryResource) -> None:
        self._api_discovery = api_discovery

        self.get_settings = async_to_raw_response_wrapper(
            api_discovery.get_settings,
        )
        self.scan_openapi = async_to_raw_response_wrapper(
            api_discovery.scan_openapi,
        )
        self.update_settings = async_to_raw_response_wrapper(
            api_discovery.update_settings,
        )
        self.upload_openapi = async_to_raw_response_wrapper(
            api_discovery.upload_openapi,
        )

    @cached_property
    def scan_results(self) -> AsyncScanResultsResourceWithRawResponse:
        return AsyncScanResultsResourceWithRawResponse(self._api_discovery.scan_results)


class APIDiscoveryResourceWithStreamingResponse:
    def __init__(self, api_discovery: APIDiscoveryResource) -> None:
        self._api_discovery = api_discovery

        self.get_settings = to_streamed_response_wrapper(
            api_discovery.get_settings,
        )
        self.scan_openapi = to_streamed_response_wrapper(
            api_discovery.scan_openapi,
        )
        self.update_settings = to_streamed_response_wrapper(
            api_discovery.update_settings,
        )
        self.upload_openapi = to_streamed_response_wrapper(
            api_discovery.upload_openapi,
        )

    @cached_property
    def scan_results(self) -> ScanResultsResourceWithStreamingResponse:
        return ScanResultsResourceWithStreamingResponse(self._api_discovery.scan_results)


class AsyncAPIDiscoveryResourceWithStreamingResponse:
    def __init__(self, api_discovery: AsyncAPIDiscoveryResource) -> None:
        self._api_discovery = api_discovery

        self.get_settings = async_to_streamed_response_wrapper(
            api_discovery.get_settings,
        )
        self.scan_openapi = async_to_streamed_response_wrapper(
            api_discovery.scan_openapi,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            api_discovery.update_settings,
        )
        self.upload_openapi = async_to_streamed_response_wrapper(
            api_discovery.upload_openapi,
        )

    @cached_property
    def scan_results(self) -> AsyncScanResultsResourceWithStreamingResponse:
        return AsyncScanResultsResourceWithStreamingResponse(self._api_discovery.scan_results)

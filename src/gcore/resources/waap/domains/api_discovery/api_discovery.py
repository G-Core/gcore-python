# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .openapi import (
    OpenAPIResource,
    AsyncOpenAPIResource,
    OpenAPIResourceWithRawResponse,
    AsyncOpenAPIResourceWithRawResponse,
    OpenAPIResourceWithStreamingResponse,
    AsyncOpenAPIResourceWithStreamingResponse,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
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

__all__ = ["APIDiscoveryResource", "AsyncAPIDiscoveryResource"]


class APIDiscoveryResource(SyncAPIResource):
    @cached_property
    def scan_results(self) -> ScanResultsResource:
        return ScanResultsResource(self._client)

    @cached_property
    def openapi(self) -> OpenAPIResource:
        return OpenAPIResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

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


class AsyncAPIDiscoveryResource(AsyncAPIResource):
    @cached_property
    def scan_results(self) -> AsyncScanResultsResource:
        return AsyncScanResultsResource(self._client)

    @cached_property
    def openapi(self) -> AsyncOpenAPIResource:
        return AsyncOpenAPIResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

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


class APIDiscoveryResourceWithRawResponse:
    def __init__(self, api_discovery: APIDiscoveryResource) -> None:
        self._api_discovery = api_discovery

    @cached_property
    def scan_results(self) -> ScanResultsResourceWithRawResponse:
        return ScanResultsResourceWithRawResponse(self._api_discovery.scan_results)

    @cached_property
    def openapi(self) -> OpenAPIResourceWithRawResponse:
        return OpenAPIResourceWithRawResponse(self._api_discovery.openapi)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._api_discovery.settings)


class AsyncAPIDiscoveryResourceWithRawResponse:
    def __init__(self, api_discovery: AsyncAPIDiscoveryResource) -> None:
        self._api_discovery = api_discovery

    @cached_property
    def scan_results(self) -> AsyncScanResultsResourceWithRawResponse:
        return AsyncScanResultsResourceWithRawResponse(self._api_discovery.scan_results)

    @cached_property
    def openapi(self) -> AsyncOpenAPIResourceWithRawResponse:
        return AsyncOpenAPIResourceWithRawResponse(self._api_discovery.openapi)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._api_discovery.settings)


class APIDiscoveryResourceWithStreamingResponse:
    def __init__(self, api_discovery: APIDiscoveryResource) -> None:
        self._api_discovery = api_discovery

    @cached_property
    def scan_results(self) -> ScanResultsResourceWithStreamingResponse:
        return ScanResultsResourceWithStreamingResponse(self._api_discovery.scan_results)

    @cached_property
    def openapi(self) -> OpenAPIResourceWithStreamingResponse:
        return OpenAPIResourceWithStreamingResponse(self._api_discovery.openapi)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._api_discovery.settings)


class AsyncAPIDiscoveryResourceWithStreamingResponse:
    def __init__(self, api_discovery: AsyncAPIDiscoveryResource) -> None:
        self._api_discovery = api_discovery

    @cached_property
    def scan_results(self) -> AsyncScanResultsResourceWithStreamingResponse:
        return AsyncScanResultsResourceWithStreamingResponse(self._api_discovery.scan_results)

    @cached_property
    def openapi(self) -> AsyncOpenAPIResourceWithStreamingResponse:
        return AsyncOpenAPIResourceWithStreamingResponse(self._api_discovery.openapi)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._api_discovery.settings)

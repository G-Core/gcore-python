# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .routers import (
    RoutersResource,
    AsyncRoutersResource,
    RoutersResourceWithRawResponse,
    AsyncRoutersResourceWithRawResponse,
    RoutersResourceWithStreamingResponse,
    AsyncRoutersResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["NetworksResource", "AsyncNetworksResource"]


class NetworksResource(SyncAPIResource):
    @cached_property
    def routers(self) -> RoutersResource:
        return RoutersResource(self._client)

    @cached_property
    def with_raw_response(self) -> NetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return NetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return NetworksResourceWithStreamingResponse(self)


class AsyncNetworksResource(AsyncAPIResource):
    @cached_property
    def routers(self) -> AsyncRoutersResource:
        return AsyncRoutersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncNetworksResourceWithStreamingResponse(self)


class NetworksResourceWithRawResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

    @cached_property
    def routers(self) -> RoutersResourceWithRawResponse:
        return RoutersResourceWithRawResponse(self._networks.routers)


class AsyncNetworksResourceWithRawResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

    @cached_property
    def routers(self) -> AsyncRoutersResourceWithRawResponse:
        return AsyncRoutersResourceWithRawResponse(self._networks.routers)


class NetworksResourceWithStreamingResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

    @cached_property
    def routers(self) -> RoutersResourceWithStreamingResponse:
        return RoutersResourceWithStreamingResponse(self._networks.routers)


class AsyncNetworksResourceWithStreamingResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

    @cached_property
    def routers(self) -> AsyncRoutersResourceWithStreamingResponse:
        return AsyncRoutersResourceWithStreamingResponse(self._networks.routers)

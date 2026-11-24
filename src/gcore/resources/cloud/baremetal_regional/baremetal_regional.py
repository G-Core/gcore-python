# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .flavors import (
    FlavorsResource,
    AsyncFlavorsResource,
    FlavorsResourceWithRawResponse,
    AsyncFlavorsResourceWithRawResponse,
    FlavorsResourceWithStreamingResponse,
    AsyncFlavorsResourceWithStreamingResponse,
)
from .servers import (
    ServersResource,
    AsyncServersResource,
    ServersResourceWithRawResponse,
    AsyncServersResourceWithRawResponse,
    ServersResourceWithStreamingResponse,
    AsyncServersResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BaremetalRegionalResource", "AsyncBaremetalRegionalResource"]


class BaremetalRegionalResource(SyncAPIResource):
    """Region-pathed bare metal servers and flavors.

    This client is temporary, and a future release will remove it. Use `cloud.baremetal` in new code.
    """

    @cached_property
    def flavors(self) -> FlavorsResource:
        return FlavorsResource(self._client)

    @cached_property
    def servers(self) -> ServersResource:
        """
        Bare metal servers are dedicated physical machines with direct hardware access, supporting provisioning, rebuilding, and network configuration within a cloud region.
        """
        return ServersResource(self._client)

    @cached_property
    def with_raw_response(self) -> BaremetalRegionalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return BaremetalRegionalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BaremetalRegionalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return BaremetalRegionalResourceWithStreamingResponse(self)


class AsyncBaremetalRegionalResource(AsyncAPIResource):
    """Region-pathed bare metal servers and flavors.

    This client is temporary, and a future release will remove it. Use `cloud.baremetal` in new code.
    """

    @cached_property
    def flavors(self) -> AsyncFlavorsResource:
        return AsyncFlavorsResource(self._client)

    @cached_property
    def servers(self) -> AsyncServersResource:
        """
        Bare metal servers are dedicated physical machines with direct hardware access, supporting provisioning, rebuilding, and network configuration within a cloud region.
        """
        return AsyncServersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBaremetalRegionalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBaremetalRegionalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBaremetalRegionalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncBaremetalRegionalResourceWithStreamingResponse(self)


class BaremetalRegionalResourceWithRawResponse:
    def __init__(self, baremetal_regional: BaremetalRegionalResource) -> None:
        self._baremetal_regional = baremetal_regional

    @cached_property
    def flavors(self) -> FlavorsResourceWithRawResponse:
        return FlavorsResourceWithRawResponse(self._baremetal_regional.flavors)

    @cached_property
    def servers(self) -> ServersResourceWithRawResponse:
        """
        Bare metal servers are dedicated physical machines with direct hardware access, supporting provisioning, rebuilding, and network configuration within a cloud region.
        """
        return ServersResourceWithRawResponse(self._baremetal_regional.servers)


class AsyncBaremetalRegionalResourceWithRawResponse:
    def __init__(self, baremetal_regional: AsyncBaremetalRegionalResource) -> None:
        self._baremetal_regional = baremetal_regional

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithRawResponse:
        return AsyncFlavorsResourceWithRawResponse(self._baremetal_regional.flavors)

    @cached_property
    def servers(self) -> AsyncServersResourceWithRawResponse:
        """
        Bare metal servers are dedicated physical machines with direct hardware access, supporting provisioning, rebuilding, and network configuration within a cloud region.
        """
        return AsyncServersResourceWithRawResponse(self._baremetal_regional.servers)


class BaremetalRegionalResourceWithStreamingResponse:
    def __init__(self, baremetal_regional: BaremetalRegionalResource) -> None:
        self._baremetal_regional = baremetal_regional

    @cached_property
    def flavors(self) -> FlavorsResourceWithStreamingResponse:
        return FlavorsResourceWithStreamingResponse(self._baremetal_regional.flavors)

    @cached_property
    def servers(self) -> ServersResourceWithStreamingResponse:
        """
        Bare metal servers are dedicated physical machines with direct hardware access, supporting provisioning, rebuilding, and network configuration within a cloud region.
        """
        return ServersResourceWithStreamingResponse(self._baremetal_regional.servers)


class AsyncBaremetalRegionalResourceWithStreamingResponse:
    def __init__(self, baremetal_regional: AsyncBaremetalRegionalResource) -> None:
        self._baremetal_regional = baremetal_regional

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithStreamingResponse:
        return AsyncFlavorsResourceWithStreamingResponse(self._baremetal_regional.flavors)

    @cached_property
    def servers(self) -> AsyncServersResourceWithStreamingResponse:
        """
        Bare metal servers are dedicated physical machines with direct hardware access, supporting provisioning, rebuilding, and network configuration within a cloud region.
        """
        return AsyncServersResourceWithStreamingResponse(self._baremetal_regional.servers)

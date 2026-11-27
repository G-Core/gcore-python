# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .gpu import (
    GPUResource,
    AsyncGPUResource,
    GPUResourceWithRawResponse,
    AsyncGPUResourceWithRawResponse,
    GPUResourceWithStreamingResponse,
    AsyncGPUResourceWithStreamingResponse,
)
from .ports import (
    PortsResource,
    AsyncPortsResource,
    PortsResourceWithRawResponse,
    AsyncPortsResourceWithRawResponse,
    PortsResourceWithStreamingResponse,
    AsyncPortsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .baremetal.baremetal import (
    BaremetalResource,
    AsyncBaremetalResource,
    BaremetalResourceWithRawResponse,
    AsyncBaremetalResourceWithRawResponse,
    BaremetalResourceWithStreamingResponse,
    AsyncBaremetalResourceWithStreamingResponse,
)
from .instances.instances import (
    InstancesResource,
    AsyncInstancesResource,
    InstancesResourceWithRawResponse,
    AsyncInstancesResourceWithRawResponse,
    InstancesResourceWithStreamingResponse,
    AsyncInstancesResourceWithStreamingResponse,
)

__all__ = ["PricingResource", "AsyncPricingResource"]


class PricingResource(SyncAPIResource):
    """
    Pricing gives the prices of instances, bare metal servers and ports in all regions of the project: flavor prices, the price of a configuration before you create it, and the price of an existing server.
    """

    @cached_property
    def instances(self) -> InstancesResource:
        return InstancesResource(self._client)

    @cached_property
    def baremetal(self) -> BaremetalResource:
        return BaremetalResource(self._client)

    @cached_property
    def ports(self) -> PortsResource:
        return PortsResource(self._client)

    @cached_property
    def gpu(self) -> GPUResource:
        """
        GPU pricing lists the public list prices of bare metal and virtual GPUs in EUR and USD.
        """
        return GPUResource(self._client)

    @cached_property
    def with_raw_response(self) -> PricingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PricingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PricingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PricingResourceWithStreamingResponse(self)


class AsyncPricingResource(AsyncAPIResource):
    """
    Pricing gives the prices of instances, bare metal servers and ports in all regions of the project: flavor prices, the price of a configuration before you create it, and the price of an existing server.
    """

    @cached_property
    def instances(self) -> AsyncInstancesResource:
        return AsyncInstancesResource(self._client)

    @cached_property
    def baremetal(self) -> AsyncBaremetalResource:
        return AsyncBaremetalResource(self._client)

    @cached_property
    def ports(self) -> AsyncPortsResource:
        return AsyncPortsResource(self._client)

    @cached_property
    def gpu(self) -> AsyncGPUResource:
        """
        GPU pricing lists the public list prices of bare metal and virtual GPUs in EUR and USD.
        """
        return AsyncGPUResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPricingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPricingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPricingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPricingResourceWithStreamingResponse(self)


class PricingResourceWithRawResponse:
    def __init__(self, pricing: PricingResource) -> None:
        self._pricing = pricing

    @cached_property
    def instances(self) -> InstancesResourceWithRawResponse:
        return InstancesResourceWithRawResponse(self._pricing.instances)

    @cached_property
    def baremetal(self) -> BaremetalResourceWithRawResponse:
        return BaremetalResourceWithRawResponse(self._pricing.baremetal)

    @cached_property
    def ports(self) -> PortsResourceWithRawResponse:
        return PortsResourceWithRawResponse(self._pricing.ports)

    @cached_property
    def gpu(self) -> GPUResourceWithRawResponse:
        """
        GPU pricing lists the public list prices of bare metal and virtual GPUs in EUR and USD.
        """
        return GPUResourceWithRawResponse(self._pricing.gpu)


class AsyncPricingResourceWithRawResponse:
    def __init__(self, pricing: AsyncPricingResource) -> None:
        self._pricing = pricing

    @cached_property
    def instances(self) -> AsyncInstancesResourceWithRawResponse:
        return AsyncInstancesResourceWithRawResponse(self._pricing.instances)

    @cached_property
    def baremetal(self) -> AsyncBaremetalResourceWithRawResponse:
        return AsyncBaremetalResourceWithRawResponse(self._pricing.baremetal)

    @cached_property
    def ports(self) -> AsyncPortsResourceWithRawResponse:
        return AsyncPortsResourceWithRawResponse(self._pricing.ports)

    @cached_property
    def gpu(self) -> AsyncGPUResourceWithRawResponse:
        """
        GPU pricing lists the public list prices of bare metal and virtual GPUs in EUR and USD.
        """
        return AsyncGPUResourceWithRawResponse(self._pricing.gpu)


class PricingResourceWithStreamingResponse:
    def __init__(self, pricing: PricingResource) -> None:
        self._pricing = pricing

    @cached_property
    def instances(self) -> InstancesResourceWithStreamingResponse:
        return InstancesResourceWithStreamingResponse(self._pricing.instances)

    @cached_property
    def baremetal(self) -> BaremetalResourceWithStreamingResponse:
        return BaremetalResourceWithStreamingResponse(self._pricing.baremetal)

    @cached_property
    def ports(self) -> PortsResourceWithStreamingResponse:
        return PortsResourceWithStreamingResponse(self._pricing.ports)

    @cached_property
    def gpu(self) -> GPUResourceWithStreamingResponse:
        """
        GPU pricing lists the public list prices of bare metal and virtual GPUs in EUR and USD.
        """
        return GPUResourceWithStreamingResponse(self._pricing.gpu)


class AsyncPricingResourceWithStreamingResponse:
    def __init__(self, pricing: AsyncPricingResource) -> None:
        self._pricing = pricing

    @cached_property
    def instances(self) -> AsyncInstancesResourceWithStreamingResponse:
        return AsyncInstancesResourceWithStreamingResponse(self._pricing.instances)

    @cached_property
    def baremetal(self) -> AsyncBaremetalResourceWithStreamingResponse:
        return AsyncBaremetalResourceWithStreamingResponse(self._pricing.baremetal)

    @cached_property
    def ports(self) -> AsyncPortsResourceWithStreamingResponse:
        return AsyncPortsResourceWithStreamingResponse(self._pricing.ports)

    @cached_property
    def gpu(self) -> AsyncGPUResourceWithStreamingResponse:
        """
        GPU pricing lists the public list prices of bare metal and virtual GPUs in EUR and USD.
        """
        return AsyncGPUResourceWithStreamingResponse(self._pricing.gpu)

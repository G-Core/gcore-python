# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .clusters.clusters import (
    ClustersResource,
    AsyncClustersResource,
    ClustersResourceWithRawResponse,
    AsyncClustersResourceWithRawResponse,
    ClustersResourceWithStreamingResponse,
    AsyncClustersResourceWithStreamingResponse,
)

__all__ = ["GPUBaremetalResource", "AsyncGPUBaremetalResource"]


class GPUBaremetalResource(SyncAPIResource):
    @cached_property
    def clusters(self) -> ClustersResource:
        return ClustersResource(self._client)

    @cached_property
    def with_raw_response(self) -> GPUBaremetalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return GPUBaremetalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GPUBaremetalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return GPUBaremetalResourceWithStreamingResponse(self)


class AsyncGPUBaremetalResource(AsyncAPIResource):
    @cached_property
    def clusters(self) -> AsyncClustersResource:
        return AsyncClustersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGPUBaremetalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGPUBaremetalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGPUBaremetalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncGPUBaremetalResourceWithStreamingResponse(self)


class GPUBaremetalResourceWithRawResponse:
    def __init__(self, gpu_baremetal: GPUBaremetalResource) -> None:
        self._gpu_baremetal = gpu_baremetal

    @cached_property
    def clusters(self) -> ClustersResourceWithRawResponse:
        return ClustersResourceWithRawResponse(self._gpu_baremetal.clusters)


class AsyncGPUBaremetalResourceWithRawResponse:
    def __init__(self, gpu_baremetal: AsyncGPUBaremetalResource) -> None:
        self._gpu_baremetal = gpu_baremetal

    @cached_property
    def clusters(self) -> AsyncClustersResourceWithRawResponse:
        return AsyncClustersResourceWithRawResponse(self._gpu_baremetal.clusters)


class GPUBaremetalResourceWithStreamingResponse:
    def __init__(self, gpu_baremetal: GPUBaremetalResource) -> None:
        self._gpu_baremetal = gpu_baremetal

    @cached_property
    def clusters(self) -> ClustersResourceWithStreamingResponse:
        return ClustersResourceWithStreamingResponse(self._gpu_baremetal.clusters)


class AsyncGPUBaremetalResourceWithStreamingResponse:
    def __init__(self, gpu_baremetal: AsyncGPUBaremetalResource) -> None:
        self._gpu_baremetal = gpu_baremetal

    @cached_property
    def clusters(self) -> AsyncClustersResourceWithStreamingResponse:
        return AsyncClustersResourceWithStreamingResponse(self._gpu_baremetal.clusters)

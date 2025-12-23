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

__all__ = ["GPUVirtualResource", "AsyncGPUVirtualResource"]


class GPUVirtualResource(SyncAPIResource):
    @cached_property
    def clusters(self) -> ClustersResource:
        return ClustersResource(self._client)

    @cached_property
    def with_raw_response(self) -> GPUVirtualResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return GPUVirtualResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GPUVirtualResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return GPUVirtualResourceWithStreamingResponse(self)


class AsyncGPUVirtualResource(AsyncAPIResource):
    @cached_property
    def clusters(self) -> AsyncClustersResource:
        return AsyncClustersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGPUVirtualResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGPUVirtualResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGPUVirtualResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncGPUVirtualResourceWithStreamingResponse(self)


class GPUVirtualResourceWithRawResponse:
    def __init__(self, gpu_virtual: GPUVirtualResource) -> None:
        self._gpu_virtual = gpu_virtual

    @cached_property
    def clusters(self) -> ClustersResourceWithRawResponse:
        return ClustersResourceWithRawResponse(self._gpu_virtual.clusters)


class AsyncGPUVirtualResourceWithRawResponse:
    def __init__(self, gpu_virtual: AsyncGPUVirtualResource) -> None:
        self._gpu_virtual = gpu_virtual

    @cached_property
    def clusters(self) -> AsyncClustersResourceWithRawResponse:
        return AsyncClustersResourceWithRawResponse(self._gpu_virtual.clusters)


class GPUVirtualResourceWithStreamingResponse:
    def __init__(self, gpu_virtual: GPUVirtualResource) -> None:
        self._gpu_virtual = gpu_virtual

    @cached_property
    def clusters(self) -> ClustersResourceWithStreamingResponse:
        return ClustersResourceWithStreamingResponse(self._gpu_virtual.clusters)


class AsyncGPUVirtualResourceWithStreamingResponse:
    def __init__(self, gpu_virtual: AsyncGPUVirtualResource) -> None:
        self._gpu_virtual = gpu_virtual

    @cached_property
    def clusters(self) -> AsyncClustersResourceWithStreamingResponse:
        return AsyncClustersResourceWithStreamingResponse(self._gpu_virtual.clusters)

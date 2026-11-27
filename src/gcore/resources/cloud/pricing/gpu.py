# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloud.pricing.gpu_price_catalog import GPUPriceCatalog

__all__ = ["GPUResource", "AsyncGPUResource"]


class GPUResource(SyncAPIResource):
    """
    GPU pricing lists the public list prices of bare metal and virtual GPUs in EUR and USD.
    """

    @cached_property
    def with_raw_response(self) -> GPUResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return GPUResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GPUResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return GPUResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUPriceCatalog:
        """
        Returns list prices for GPUs, bare metal and virtual, in EUR and USD.

        The response has no pagination. The catalog is small. The list sorts by price
        per hour, from low to high.
        """
        return self._get(
            "/cloud/public/v1/pricing/gpu",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUPriceCatalog,
        )


class AsyncGPUResource(AsyncAPIResource):
    """
    GPU pricing lists the public list prices of bare metal and virtual GPUs in EUR and USD.
    """

    @cached_property
    def with_raw_response(self) -> AsyncGPUResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGPUResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGPUResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncGPUResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUPriceCatalog:
        """
        Returns list prices for GPUs, bare metal and virtual, in EUR and USD.

        The response has no pagination. The catalog is small. The list sorts by price
        per hour, from low to high.
        """
        return await self._get(
            "/cloud/public/v1/pricing/gpu",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUPriceCatalog,
        )


class GPUResourceWithRawResponse:
    def __init__(self, gpu: GPUResource) -> None:
        self._gpu = gpu

        self.list = to_raw_response_wrapper(
            gpu.list,
        )


class AsyncGPUResourceWithRawResponse:
    def __init__(self, gpu: AsyncGPUResource) -> None:
        self._gpu = gpu

        self.list = async_to_raw_response_wrapper(
            gpu.list,
        )


class GPUResourceWithStreamingResponse:
    def __init__(self, gpu: GPUResource) -> None:
        self._gpu = gpu

        self.list = to_streamed_response_wrapper(
            gpu.list,
        )


class AsyncGPUResourceWithStreamingResponse:
    def __init__(self, gpu: AsyncGPUResource) -> None:
        self._gpu = gpu

        self.list = async_to_streamed_response_wrapper(
            gpu.list,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BaremetalResource", "AsyncBaremetalResource"]


class BaremetalResource(SyncAPIResource):
    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BaremetalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return BaremetalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BaremetalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return BaremetalResourceWithStreamingResponse(self)


class AsyncBaremetalResource(AsyncAPIResource):
    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBaremetalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBaremetalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBaremetalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncBaremetalResourceWithStreamingResponse(self)


class BaremetalResourceWithRawResponse:
    def __init__(self, baremetal: BaremetalResource) -> None:
        self._baremetal = baremetal

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._baremetal.images)


class AsyncBaremetalResourceWithRawResponse:
    def __init__(self, baremetal: AsyncBaremetalResource) -> None:
        self._baremetal = baremetal

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._baremetal.images)


class BaremetalResourceWithStreamingResponse:
    def __init__(self, baremetal: BaremetalResource) -> None:
        self._baremetal = baremetal

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._baremetal.images)


class AsyncBaremetalResourceWithStreamingResponse:
    def __init__(self, baremetal: AsyncBaremetalResource) -> None:
        self._baremetal = baremetal

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._baremetal.images)

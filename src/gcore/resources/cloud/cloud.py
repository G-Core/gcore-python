# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .projects import (
    ProjectsResource,
    AsyncProjectsResource,
    ProjectsResourceWithRawResponse,
    AsyncProjectsResourceWithRawResponse,
    ProjectsResourceWithStreamingResponse,
    AsyncProjectsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CloudResource", "AsyncCloudResource"]


class CloudResource(SyncAPIResource):
    @cached_property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CloudResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return CloudResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return CloudResourceWithStreamingResponse(self)


class AsyncCloudResource(AsyncAPIResource):
    @cached_property
    def projects(self) -> AsyncProjectsResource:
        return AsyncProjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCloudResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCloudResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncCloudResourceWithStreamingResponse(self)


class CloudResourceWithRawResponse:
    def __init__(self, cloud: CloudResource) -> None:
        self._cloud = cloud

    @cached_property
    def projects(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self._cloud.projects)


class AsyncCloudResourceWithRawResponse:
    def __init__(self, cloud: AsyncCloudResource) -> None:
        self._cloud = cloud

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self._cloud.projects)


class CloudResourceWithStreamingResponse:
    def __init__(self, cloud: CloudResource) -> None:
        self._cloud = cloud

    @cached_property
    def projects(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self._cloud.projects)


class AsyncCloudResourceWithStreamingResponse:
    def __init__(self, cloud: AsyncCloudResource) -> None:
        self._cloud = cloud

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self._cloud.projects)

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from .regions import (
    RegionsResource,
    AsyncRegionsResource,
    RegionsResourceWithRawResponse,
    AsyncRegionsResourceWithRawResponse,
    RegionsResourceWithStreamingResponse,
    AsyncRegionsResourceWithStreamingResponse,
)
from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
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
from .quotas.quotas import (
    QuotasResource,
    AsyncQuotasResource,
    QuotasResourceWithRawResponse,
    AsyncQuotasResourceWithRawResponse,
    QuotasResourceWithStreamingResponse,
    AsyncQuotasResourceWithStreamingResponse,
)

__all__ = ["CloudResource", "AsyncCloudResource"]


class CloudResource(SyncAPIResource):
    @cached_property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def regions(self) -> RegionsResource:
        return RegionsResource(self._client)

    @cached_property
    def quotas(self) -> QuotasResource:
        return QuotasResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

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
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def regions(self) -> AsyncRegionsResource:
        return AsyncRegionsResource(self._client)

    @cached_property
    def quotas(self) -> AsyncQuotasResource:
        return AsyncQuotasResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

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

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._cloud.tasks)

    @cached_property
    def regions(self) -> RegionsResourceWithRawResponse:
        return RegionsResourceWithRawResponse(self._cloud.regions)

    @cached_property
    def quotas(self) -> QuotasResourceWithRawResponse:
        return QuotasResourceWithRawResponse(self._cloud.quotas)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._cloud.secrets)


class AsyncCloudResourceWithRawResponse:
    def __init__(self, cloud: AsyncCloudResource) -> None:
        self._cloud = cloud

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self._cloud.projects)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._cloud.tasks)

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithRawResponse:
        return AsyncRegionsResourceWithRawResponse(self._cloud.regions)

    @cached_property
    def quotas(self) -> AsyncQuotasResourceWithRawResponse:
        return AsyncQuotasResourceWithRawResponse(self._cloud.quotas)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._cloud.secrets)


class CloudResourceWithStreamingResponse:
    def __init__(self, cloud: CloudResource) -> None:
        self._cloud = cloud

    @cached_property
    def projects(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self._cloud.projects)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._cloud.tasks)

    @cached_property
    def regions(self) -> RegionsResourceWithStreamingResponse:
        return RegionsResourceWithStreamingResponse(self._cloud.regions)

    @cached_property
    def quotas(self) -> QuotasResourceWithStreamingResponse:
        return QuotasResourceWithStreamingResponse(self._cloud.quotas)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._cloud.secrets)


class AsyncCloudResourceWithStreamingResponse:
    def __init__(self, cloud: AsyncCloudResource) -> None:
        self._cloud = cloud

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self._cloud.projects)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._cloud.tasks)

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithStreamingResponse:
        return AsyncRegionsResourceWithStreamingResponse(self._cloud.regions)

    @cached_property
    def quotas(self) -> AsyncQuotasResourceWithStreamingResponse:
        return AsyncQuotasResourceWithStreamingResponse(self._cloud.quotas)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._cloud.secrets)

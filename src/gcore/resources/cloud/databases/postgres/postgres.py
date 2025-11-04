# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .configurations import (
    ConfigurationsResource,
    AsyncConfigurationsResource,
    ConfigurationsResourceWithRawResponse,
    AsyncConfigurationsResourceWithRawResponse,
    ConfigurationsResourceWithStreamingResponse,
    AsyncConfigurationsResourceWithStreamingResponse,
)
from .clusters.clusters import (
    ClustersResource,
    AsyncClustersResource,
    ClustersResourceWithRawResponse,
    AsyncClustersResourceWithRawResponse,
    ClustersResourceWithStreamingResponse,
    AsyncClustersResourceWithStreamingResponse,
)
from .custom_configurations import (
    CustomConfigurationsResource,
    AsyncCustomConfigurationsResource,
    CustomConfigurationsResourceWithRawResponse,
    AsyncCustomConfigurationsResourceWithRawResponse,
    CustomConfigurationsResourceWithStreamingResponse,
    AsyncCustomConfigurationsResourceWithStreamingResponse,
)

__all__ = ["PostgresResource", "AsyncPostgresResource"]


class PostgresResource(SyncAPIResource):
    @cached_property
    def clusters(self) -> ClustersResource:
        return ClustersResource(self._client)

    @cached_property
    def configurations(self) -> ConfigurationsResource:
        return ConfigurationsResource(self._client)

    @cached_property
    def custom_configurations(self) -> CustomConfigurationsResource:
        return CustomConfigurationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostgresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PostgresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostgresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PostgresResourceWithStreamingResponse(self)


class AsyncPostgresResource(AsyncAPIResource):
    @cached_property
    def clusters(self) -> AsyncClustersResource:
        return AsyncClustersResource(self._client)

    @cached_property
    def configurations(self) -> AsyncConfigurationsResource:
        return AsyncConfigurationsResource(self._client)

    @cached_property
    def custom_configurations(self) -> AsyncCustomConfigurationsResource:
        return AsyncCustomConfigurationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostgresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostgresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostgresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPostgresResourceWithStreamingResponse(self)


class PostgresResourceWithRawResponse:
    def __init__(self, postgres: PostgresResource) -> None:
        self._postgres = postgres

    @cached_property
    def clusters(self) -> ClustersResourceWithRawResponse:
        return ClustersResourceWithRawResponse(self._postgres.clusters)

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithRawResponse:
        return ConfigurationsResourceWithRawResponse(self._postgres.configurations)

    @cached_property
    def custom_configurations(self) -> CustomConfigurationsResourceWithRawResponse:
        return CustomConfigurationsResourceWithRawResponse(self._postgres.custom_configurations)


class AsyncPostgresResourceWithRawResponse:
    def __init__(self, postgres: AsyncPostgresResource) -> None:
        self._postgres = postgres

    @cached_property
    def clusters(self) -> AsyncClustersResourceWithRawResponse:
        return AsyncClustersResourceWithRawResponse(self._postgres.clusters)

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithRawResponse:
        return AsyncConfigurationsResourceWithRawResponse(self._postgres.configurations)

    @cached_property
    def custom_configurations(self) -> AsyncCustomConfigurationsResourceWithRawResponse:
        return AsyncCustomConfigurationsResourceWithRawResponse(self._postgres.custom_configurations)


class PostgresResourceWithStreamingResponse:
    def __init__(self, postgres: PostgresResource) -> None:
        self._postgres = postgres

    @cached_property
    def clusters(self) -> ClustersResourceWithStreamingResponse:
        return ClustersResourceWithStreamingResponse(self._postgres.clusters)

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithStreamingResponse:
        return ConfigurationsResourceWithStreamingResponse(self._postgres.configurations)

    @cached_property
    def custom_configurations(self) -> CustomConfigurationsResourceWithStreamingResponse:
        return CustomConfigurationsResourceWithStreamingResponse(self._postgres.custom_configurations)


class AsyncPostgresResourceWithStreamingResponse:
    def __init__(self, postgres: AsyncPostgresResource) -> None:
        self._postgres = postgres

    @cached_property
    def clusters(self) -> AsyncClustersResourceWithStreamingResponse:
        return AsyncClustersResourceWithStreamingResponse(self._postgres.clusters)

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        return AsyncConfigurationsResourceWithStreamingResponse(self._postgres.configurations)

    @cached_property
    def custom_configurations(self) -> AsyncCustomConfigurationsResourceWithStreamingResponse:
        return AsyncCustomConfigurationsResourceWithStreamingResponse(self._postgres.custom_configurations)

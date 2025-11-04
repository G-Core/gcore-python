# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .postgres.postgres import (
    PostgresResource,
    AsyncPostgresResource,
    PostgresResourceWithRawResponse,
    AsyncPostgresResourceWithRawResponse,
    PostgresResourceWithStreamingResponse,
    AsyncPostgresResourceWithStreamingResponse,
)

__all__ = ["DatabasesResource", "AsyncDatabasesResource"]


class DatabasesResource(SyncAPIResource):
    @cached_property
    def postgres(self) -> PostgresResource:
        return PostgresResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatabasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return DatabasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatabasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return DatabasesResourceWithStreamingResponse(self)


class AsyncDatabasesResource(AsyncAPIResource):
    @cached_property
    def postgres(self) -> AsyncPostgresResource:
        return AsyncPostgresResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatabasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatabasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatabasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncDatabasesResourceWithStreamingResponse(self)


class DatabasesResourceWithRawResponse:
    def __init__(self, databases: DatabasesResource) -> None:
        self._databases = databases

    @cached_property
    def postgres(self) -> PostgresResourceWithRawResponse:
        return PostgresResourceWithRawResponse(self._databases.postgres)


class AsyncDatabasesResourceWithRawResponse:
    def __init__(self, databases: AsyncDatabasesResource) -> None:
        self._databases = databases

    @cached_property
    def postgres(self) -> AsyncPostgresResourceWithRawResponse:
        return AsyncPostgresResourceWithRawResponse(self._databases.postgres)


class DatabasesResourceWithStreamingResponse:
    def __init__(self, databases: DatabasesResource) -> None:
        self._databases = databases

    @cached_property
    def postgres(self) -> PostgresResourceWithStreamingResponse:
        return PostgresResourceWithStreamingResponse(self._databases.postgres)


class AsyncDatabasesResourceWithStreamingResponse:
    def __init__(self, databases: AsyncDatabasesResource) -> None:
        self._databases = databases

    @cached_property
    def postgres(self) -> AsyncPostgresResourceWithStreamingResponse:
        return AsyncPostgresResourceWithStreamingResponse(self._databases.postgres)

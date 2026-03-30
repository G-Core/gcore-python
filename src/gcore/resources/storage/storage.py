# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ssh_keys import (
    SSHKeysResource,
    AsyncSSHKeysResource,
    SSHKeysResourceWithRawResponse,
    AsyncSSHKeysResourceWithRawResponse,
    SSHKeysResourceWithStreamingResponse,
    AsyncSSHKeysResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .locations import (
    LocationsResource,
    AsyncLocationsResource,
    LocationsResourceWithRawResponse,
    AsyncLocationsResourceWithRawResponse,
    LocationsResourceWithStreamingResponse,
    AsyncLocationsResourceWithStreamingResponse,
)
from .statistics import (
    StatisticsResource,
    AsyncStatisticsResource,
    StatisticsResourceWithRawResponse,
    AsyncStatisticsResourceWithRawResponse,
    StatisticsResourceWithStreamingResponse,
    AsyncStatisticsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .sftp_storages import (
    SftpStoragesResource,
    AsyncSftpStoragesResource,
    SftpStoragesResourceWithRawResponse,
    AsyncSftpStoragesResourceWithRawResponse,
    SftpStoragesResourceWithStreamingResponse,
    AsyncSftpStoragesResourceWithStreamingResponse,
)
from .object_storages.object_storages import (
    ObjectStoragesResource,
    AsyncObjectStoragesResource,
    ObjectStoragesResourceWithRawResponse,
    AsyncObjectStoragesResourceWithRawResponse,
    ObjectStoragesResourceWithStreamingResponse,
    AsyncObjectStoragesResourceWithStreamingResponse,
)

__all__ = ["StorageResource", "AsyncStorageResource"]


class StorageResource(SyncAPIResource):
    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def object_storages(self) -> ObjectStoragesResource:
        return ObjectStoragesResource(self._client)

    @cached_property
    def sftp_storages(self) -> SftpStoragesResource:
        return SftpStoragesResource(self._client)

    @cached_property
    def ssh_keys(self) -> SSHKeysResource:
        return SSHKeysResource(self._client)

    @cached_property
    def statistics(self) -> StatisticsResource:
        return StatisticsResource(self._client)

    @cached_property
    def with_raw_response(self) -> StorageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return StorageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StorageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return StorageResourceWithStreamingResponse(self)


class AsyncStorageResource(AsyncAPIResource):
    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def object_storages(self) -> AsyncObjectStoragesResource:
        return AsyncObjectStoragesResource(self._client)

    @cached_property
    def sftp_storages(self) -> AsyncSftpStoragesResource:
        return AsyncSftpStoragesResource(self._client)

    @cached_property
    def ssh_keys(self) -> AsyncSSHKeysResource:
        return AsyncSSHKeysResource(self._client)

    @cached_property
    def statistics(self) -> AsyncStatisticsResource:
        return AsyncStatisticsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStorageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStorageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStorageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncStorageResourceWithStreamingResponse(self)


class StorageResourceWithRawResponse:
    def __init__(self, storage: StorageResource) -> None:
        self._storage = storage

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._storage.locations)

    @cached_property
    def object_storages(self) -> ObjectStoragesResourceWithRawResponse:
        return ObjectStoragesResourceWithRawResponse(self._storage.object_storages)

    @cached_property
    def sftp_storages(self) -> SftpStoragesResourceWithRawResponse:
        return SftpStoragesResourceWithRawResponse(self._storage.sftp_storages)

    @cached_property
    def ssh_keys(self) -> SSHKeysResourceWithRawResponse:
        return SSHKeysResourceWithRawResponse(self._storage.ssh_keys)

    @cached_property
    def statistics(self) -> StatisticsResourceWithRawResponse:
        return StatisticsResourceWithRawResponse(self._storage.statistics)


class AsyncStorageResourceWithRawResponse:
    def __init__(self, storage: AsyncStorageResource) -> None:
        self._storage = storage

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._storage.locations)

    @cached_property
    def object_storages(self) -> AsyncObjectStoragesResourceWithRawResponse:
        return AsyncObjectStoragesResourceWithRawResponse(self._storage.object_storages)

    @cached_property
    def sftp_storages(self) -> AsyncSftpStoragesResourceWithRawResponse:
        return AsyncSftpStoragesResourceWithRawResponse(self._storage.sftp_storages)

    @cached_property
    def ssh_keys(self) -> AsyncSSHKeysResourceWithRawResponse:
        return AsyncSSHKeysResourceWithRawResponse(self._storage.ssh_keys)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithRawResponse:
        return AsyncStatisticsResourceWithRawResponse(self._storage.statistics)


class StorageResourceWithStreamingResponse:
    def __init__(self, storage: StorageResource) -> None:
        self._storage = storage

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._storage.locations)

    @cached_property
    def object_storages(self) -> ObjectStoragesResourceWithStreamingResponse:
        return ObjectStoragesResourceWithStreamingResponse(self._storage.object_storages)

    @cached_property
    def sftp_storages(self) -> SftpStoragesResourceWithStreamingResponse:
        return SftpStoragesResourceWithStreamingResponse(self._storage.sftp_storages)

    @cached_property
    def ssh_keys(self) -> SSHKeysResourceWithStreamingResponse:
        return SSHKeysResourceWithStreamingResponse(self._storage.ssh_keys)

    @cached_property
    def statistics(self) -> StatisticsResourceWithStreamingResponse:
        return StatisticsResourceWithStreamingResponse(self._storage.statistics)


class AsyncStorageResourceWithStreamingResponse:
    def __init__(self, storage: AsyncStorageResource) -> None:
        self._storage = storage

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._storage.locations)

    @cached_property
    def object_storages(self) -> AsyncObjectStoragesResourceWithStreamingResponse:
        return AsyncObjectStoragesResourceWithStreamingResponse(self._storage.object_storages)

    @cached_property
    def sftp_storages(self) -> AsyncSftpStoragesResourceWithStreamingResponse:
        return AsyncSftpStoragesResourceWithStreamingResponse(self._storage.sftp_storages)

    @cached_property
    def ssh_keys(self) -> AsyncSSHKeysResourceWithStreamingResponse:
        return AsyncSSHKeysResourceWithStreamingResponse(self._storage.ssh_keys)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithStreamingResponse:
        return AsyncStatisticsResourceWithStreamingResponse(self._storage.statistics)

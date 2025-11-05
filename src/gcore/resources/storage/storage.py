# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .credentials import (
    CredentialsResource,
    AsyncCredentialsResource,
    CredentialsResourceWithRawResponse,
    AsyncCredentialsResourceWithRawResponse,
    CredentialsResourceWithStreamingResponse,
    AsyncCredentialsResourceWithStreamingResponse,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.storage import storage_list_params, storage_create_params, storage_update_params, storage_restore_params
from .buckets.buckets import (
    BucketsResource,
    AsyncBucketsResource,
    BucketsResourceWithRawResponse,
    AsyncBucketsResourceWithRawResponse,
    BucketsResourceWithStreamingResponse,
    AsyncBucketsResourceWithStreamingResponse,
)
from ...types.storage.storage import Storage

__all__ = ["StorageResource", "AsyncStorageResource"]


class StorageResource(SyncAPIResource):
    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def statistics(self) -> StatisticsResource:
        return StatisticsResource(self._client)

    @cached_property
    def credentials(self) -> CredentialsResource:
        return CredentialsResource(self._client)

    @cached_property
    def buckets(self) -> BucketsResource:
        return BucketsResource(self._client)

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

    def create(
        self,
        *,
        location: str,
        name: str,
        type: Literal["sftp", "s3"],
        generate_sftp_password: bool | Omit = omit,
        sftp_password: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        """
        Creates a new storage instance (S3 or SFTP) in the specified location and
        returns the storage details including credentials.

        Args:
          location: Geographic location where the storage will be provisioned. Each location
              represents a specific data center region.

          name: Unique storage name identifier. Must contain only letters, numbers, dashes, and
              underscores. Cannot be empty and must be less than 256 characters.

          type: Storage protocol type. Choose 's3' for S3-compatible object storage with API
              access, or `sftp` for SFTP file transfer protocol.

          generate_sftp_password: Automatically generate a secure password for SFTP storage access. Only
              applicable when type is `sftp`. When `true`, a random password will be generated
              and returned in the response.

          sftp_password: Custom password for SFTP storage access. Only applicable when type is `sftp`. If
              not provided and `generate_sftp_password` is `false`, no password authentication
              will be available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/storage/provisioning/v2/storage",
            body=maybe_transform(
                {
                    "location": location,
                    "name": name,
                    "type": type,
                    "generate_sftp_password": generate_sftp_password,
                    "sftp_password": sftp_password,
                },
                storage_create_params.StorageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Storage,
        )

    def update(
        self,
        storage_id: int,
        *,
        expires: str | Omit = omit,
        server_alias: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        """Updates storage configuration such as expiration date and server alias.

        Used for
        SFTP storages.

        Args:
          expires: Duration when the storage should expire in format like "1 years 6 months 2 weeks
              3 days 5 hours 10 minutes 15 seconds". Set empty to remove expiration.

          server_alias: Custom domain alias for accessing the storage. Set empty to remove alias.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/storage/provisioning/v2/storage/{storage_id}",
            body=maybe_transform(
                {
                    "expires": expires,
                    "server_alias": server_alias,
                },
                storage_update_params.StorageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Storage,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        limit: int | Omit = omit,
        location: str | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        order_direction: Literal["asc", "desc"] | Omit = omit,
        show_deleted: bool | Omit = omit,
        status: Literal["active", "suspended", "deleted", "pending"] | Omit = omit,
        type: Literal["s3", "sftp"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[Storage]:
        """
        Returns storages with the same filtering and pagination as v2, but in a
        simplified response shape for easier client consumption.

        Response format: count: total number of storages matching the filter
        (independent of pagination) results: the current page of storages according to
        limit/offset

        Args:
          id: Filter by storage ID

          limit: Max number of records in response

          location: Filter by storage location/region

          name: Filter by storage name (exact match)

          offset: Number of records to skip before beginning to write in response.

          order_by: Field name to sort by

          order_direction: Ascending or descending order

          show_deleted: Include deleted storages in the response

          status: Filter by storage status

          type: Filter by storage type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/provisioning/v3/storage",
            page=SyncOffsetPage[Storage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "show_deleted": show_deleted,
                        "status": status,
                        "type": type,
                    },
                    storage_list_params.StorageListParams,
                ),
            ),
            model=Storage,
        )

    def delete(
        self,
        storage_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Permanently deletes a storage and all its data.

        This action cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/storage/provisioning/v1/storage/{storage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        storage_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        """
        Retrieves detailed information about a specific storage including its
        configuration, credentials, and current status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/storage/provisioning/v1/storage/{storage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Storage,
        )

    def link_ssh_key(
        self,
        key_id: int,
        *,
        storage_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Associates an SSH public key with an SFTP storage, enabling passwordless
        authentication. Only works with SFTP storage types - not applicable to
        S3-compatible storage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/key/{key_id}/link",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def restore(
        self,
        storage_id: int,
        *,
        client_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Restores a previously deleted S3 storage if it was deleted within the last 2
        weeks. SFTP storages cannot be restored.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/restore",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"client_id": client_id}, storage_restore_params.StorageRestoreParams),
            ),
            cast_to=NoneType,
        )

    def unlink_ssh_key(
        self,
        key_id: int,
        *,
        storage_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes SSH key association from an SFTP storage, disabling passwordless
        authentication for that key. The key itself remains available for other
        storages.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/key/{key_id}/unlink",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncStorageResource(AsyncAPIResource):
    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def statistics(self) -> AsyncStatisticsResource:
        return AsyncStatisticsResource(self._client)

    @cached_property
    def credentials(self) -> AsyncCredentialsResource:
        return AsyncCredentialsResource(self._client)

    @cached_property
    def buckets(self) -> AsyncBucketsResource:
        return AsyncBucketsResource(self._client)

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

    async def create(
        self,
        *,
        location: str,
        name: str,
        type: Literal["sftp", "s3"],
        generate_sftp_password: bool | Omit = omit,
        sftp_password: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        """
        Creates a new storage instance (S3 or SFTP) in the specified location and
        returns the storage details including credentials.

        Args:
          location: Geographic location where the storage will be provisioned. Each location
              represents a specific data center region.

          name: Unique storage name identifier. Must contain only letters, numbers, dashes, and
              underscores. Cannot be empty and must be less than 256 characters.

          type: Storage protocol type. Choose 's3' for S3-compatible object storage with API
              access, or `sftp` for SFTP file transfer protocol.

          generate_sftp_password: Automatically generate a secure password for SFTP storage access. Only
              applicable when type is `sftp`. When `true`, a random password will be generated
              and returned in the response.

          sftp_password: Custom password for SFTP storage access. Only applicable when type is `sftp`. If
              not provided and `generate_sftp_password` is `false`, no password authentication
              will be available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/storage/provisioning/v2/storage",
            body=await async_maybe_transform(
                {
                    "location": location,
                    "name": name,
                    "type": type,
                    "generate_sftp_password": generate_sftp_password,
                    "sftp_password": sftp_password,
                },
                storage_create_params.StorageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Storage,
        )

    async def update(
        self,
        storage_id: int,
        *,
        expires: str | Omit = omit,
        server_alias: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        """Updates storage configuration such as expiration date and server alias.

        Used for
        SFTP storages.

        Args:
          expires: Duration when the storage should expire in format like "1 years 6 months 2 weeks
              3 days 5 hours 10 minutes 15 seconds". Set empty to remove expiration.

          server_alias: Custom domain alias for accessing the storage. Set empty to remove alias.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/storage/provisioning/v2/storage/{storage_id}",
            body=await async_maybe_transform(
                {
                    "expires": expires,
                    "server_alias": server_alias,
                },
                storage_update_params.StorageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Storage,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        limit: int | Omit = omit,
        location: str | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        order_direction: Literal["asc", "desc"] | Omit = omit,
        show_deleted: bool | Omit = omit,
        status: Literal["active", "suspended", "deleted", "pending"] | Omit = omit,
        type: Literal["s3", "sftp"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Storage, AsyncOffsetPage[Storage]]:
        """
        Returns storages with the same filtering and pagination as v2, but in a
        simplified response shape for easier client consumption.

        Response format: count: total number of storages matching the filter
        (independent of pagination) results: the current page of storages according to
        limit/offset

        Args:
          id: Filter by storage ID

          limit: Max number of records in response

          location: Filter by storage location/region

          name: Filter by storage name (exact match)

          offset: Number of records to skip before beginning to write in response.

          order_by: Field name to sort by

          order_direction: Ascending or descending order

          show_deleted: Include deleted storages in the response

          status: Filter by storage status

          type: Filter by storage type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/provisioning/v3/storage",
            page=AsyncOffsetPage[Storage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "show_deleted": show_deleted,
                        "status": status,
                        "type": type,
                    },
                    storage_list_params.StorageListParams,
                ),
            ),
            model=Storage,
        )

    async def delete(
        self,
        storage_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Permanently deletes a storage and all its data.

        This action cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/storage/provisioning/v1/storage/{storage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        storage_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        """
        Retrieves detailed information about a specific storage including its
        configuration, credentials, and current status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/storage/provisioning/v1/storage/{storage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Storage,
        )

    async def link_ssh_key(
        self,
        key_id: int,
        *,
        storage_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Associates an SSH public key with an SFTP storage, enabling passwordless
        authentication. Only works with SFTP storage types - not applicable to
        S3-compatible storage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/key/{key_id}/link",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def restore(
        self,
        storage_id: int,
        *,
        client_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Restores a previously deleted S3 storage if it was deleted within the last 2
        weeks. SFTP storages cannot be restored.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/restore",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"client_id": client_id}, storage_restore_params.StorageRestoreParams
                ),
            ),
            cast_to=NoneType,
        )

    async def unlink_ssh_key(
        self,
        key_id: int,
        *,
        storage_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes SSH key association from an SFTP storage, disabling passwordless
        authentication for that key. The key itself remains available for other
        storages.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/key/{key_id}/unlink",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class StorageResourceWithRawResponse:
    def __init__(self, storage: StorageResource) -> None:
        self._storage = storage

        self.create = to_raw_response_wrapper(
            storage.create,
        )
        self.update = to_raw_response_wrapper(
            storage.update,
        )
        self.list = to_raw_response_wrapper(
            storage.list,
        )
        self.delete = to_raw_response_wrapper(
            storage.delete,
        )
        self.get = to_raw_response_wrapper(
            storage.get,
        )
        self.link_ssh_key = to_raw_response_wrapper(
            storage.link_ssh_key,
        )
        self.restore = to_raw_response_wrapper(
            storage.restore,
        )
        self.unlink_ssh_key = to_raw_response_wrapper(
            storage.unlink_ssh_key,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._storage.locations)

    @cached_property
    def statistics(self) -> StatisticsResourceWithRawResponse:
        return StatisticsResourceWithRawResponse(self._storage.statistics)

    @cached_property
    def credentials(self) -> CredentialsResourceWithRawResponse:
        return CredentialsResourceWithRawResponse(self._storage.credentials)

    @cached_property
    def buckets(self) -> BucketsResourceWithRawResponse:
        return BucketsResourceWithRawResponse(self._storage.buckets)


class AsyncStorageResourceWithRawResponse:
    def __init__(self, storage: AsyncStorageResource) -> None:
        self._storage = storage

        self.create = async_to_raw_response_wrapper(
            storage.create,
        )
        self.update = async_to_raw_response_wrapper(
            storage.update,
        )
        self.list = async_to_raw_response_wrapper(
            storage.list,
        )
        self.delete = async_to_raw_response_wrapper(
            storage.delete,
        )
        self.get = async_to_raw_response_wrapper(
            storage.get,
        )
        self.link_ssh_key = async_to_raw_response_wrapper(
            storage.link_ssh_key,
        )
        self.restore = async_to_raw_response_wrapper(
            storage.restore,
        )
        self.unlink_ssh_key = async_to_raw_response_wrapper(
            storage.unlink_ssh_key,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._storage.locations)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithRawResponse:
        return AsyncStatisticsResourceWithRawResponse(self._storage.statistics)

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithRawResponse:
        return AsyncCredentialsResourceWithRawResponse(self._storage.credentials)

    @cached_property
    def buckets(self) -> AsyncBucketsResourceWithRawResponse:
        return AsyncBucketsResourceWithRawResponse(self._storage.buckets)


class StorageResourceWithStreamingResponse:
    def __init__(self, storage: StorageResource) -> None:
        self._storage = storage

        self.create = to_streamed_response_wrapper(
            storage.create,
        )
        self.update = to_streamed_response_wrapper(
            storage.update,
        )
        self.list = to_streamed_response_wrapper(
            storage.list,
        )
        self.delete = to_streamed_response_wrapper(
            storage.delete,
        )
        self.get = to_streamed_response_wrapper(
            storage.get,
        )
        self.link_ssh_key = to_streamed_response_wrapper(
            storage.link_ssh_key,
        )
        self.restore = to_streamed_response_wrapper(
            storage.restore,
        )
        self.unlink_ssh_key = to_streamed_response_wrapper(
            storage.unlink_ssh_key,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._storage.locations)

    @cached_property
    def statistics(self) -> StatisticsResourceWithStreamingResponse:
        return StatisticsResourceWithStreamingResponse(self._storage.statistics)

    @cached_property
    def credentials(self) -> CredentialsResourceWithStreamingResponse:
        return CredentialsResourceWithStreamingResponse(self._storage.credentials)

    @cached_property
    def buckets(self) -> BucketsResourceWithStreamingResponse:
        return BucketsResourceWithStreamingResponse(self._storage.buckets)


class AsyncStorageResourceWithStreamingResponse:
    def __init__(self, storage: AsyncStorageResource) -> None:
        self._storage = storage

        self.create = async_to_streamed_response_wrapper(
            storage.create,
        )
        self.update = async_to_streamed_response_wrapper(
            storage.update,
        )
        self.list = async_to_streamed_response_wrapper(
            storage.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            storage.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            storage.get,
        )
        self.link_ssh_key = async_to_streamed_response_wrapper(
            storage.link_ssh_key,
        )
        self.restore = async_to_streamed_response_wrapper(
            storage.restore,
        )
        self.unlink_ssh_key = async_to_streamed_response_wrapper(
            storage.unlink_ssh_key,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._storage.locations)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithStreamingResponse:
        return AsyncStatisticsResourceWithStreamingResponse(self._storage.statistics)

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithStreamingResponse:
        return AsyncCredentialsResourceWithStreamingResponse(self._storage.credentials)

    @cached_property
    def buckets(self) -> AsyncBucketsResourceWithStreamingResponse:
        return AsyncBucketsResourceWithStreamingResponse(self._storage.buckets)

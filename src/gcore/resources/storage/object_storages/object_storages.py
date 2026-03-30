# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .buckets import (
    BucketsResource,
    AsyncBucketsResource,
    BucketsResourceWithRawResponse,
    AsyncBucketsResourceWithRawResponse,
    BucketsResourceWithStreamingResponse,
    AsyncBucketsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .access_keys import (
    AccessKeysResource,
    AsyncAccessKeysResource,
    AccessKeysResourceWithRawResponse,
    AsyncAccessKeysResourceWithRawResponse,
    AccessKeysResourceWithStreamingResponse,
    AsyncAccessKeysResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.storage import object_storage_list_params, object_storage_create_params
from ....types.storage.s3_storage import S3Storage
from ....types.storage.s3_storage_created import S3StorageCreated

__all__ = ["ObjectStoragesResource", "AsyncObjectStoragesResource"]


class ObjectStoragesResource(SyncAPIResource):
    @cached_property
    def access_keys(self) -> AccessKeysResource:
        return AccessKeysResource(self._client)

    @cached_property
    def buckets(self) -> BucketsResource:
        return BucketsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ObjectStoragesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ObjectStoragesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectStoragesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ObjectStoragesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        location_name: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> S3StorageCreated:
        """
        Creates a new S3-compatible storage instance in the specified location and
        returns the storage details including credentials.

        Args:
          location_name: Location code where the storage should be created

          name: User-defined name for the storage instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/storage/v4/object_storages",
            body=maybe_transform(
                {
                    "location_name": location_name,
                    "name": name,
                },
                object_storage_create_params.ObjectStorageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3StorageCreated,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        limit: int | Omit = omit,
        location_name: str | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        provisioning_status: Literal["active", "creating", "updating", "deleting", "deleted"] | Omit = omit,
        show_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[S3Storage]:
        """
        Returns a paginated list of S3-compatible storage instances for the
        authenticated client.

        Args:
          id: Filter by storage ID

          limit: Max number of records in response

          location_name: Filter by storage location/region

          name: Filter by storage name

          offset: Number of records to skip

          provisioning_status: Filter by provisioning status

          show_deleted: Include deleted storages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/v4/object_storages",
            page=SyncOffsetPage[S3Storage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "limit": limit,
                        "location_name": location_name,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "provisioning_status": provisioning_status,
                        "show_deleted": show_deleted,
                    },
                    object_storage_list_params.ObjectStorageListParams,
                ),
            ),
            model=S3Storage,
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
        """Deletes an S3-compatible storage instance.

        This operation cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/storage/v4/object_storages/{storage_id}", storage_id=storage_id),
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
    ) -> S3Storage:
        """
        Returns details of a specific S3-compatible storage instance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/storage/v4/object_storages/{storage_id}", storage_id=storage_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3Storage,
        )

    def restore(
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
        """
        Restores a previously deleted S3-compatible storage instance if it was deleted
        within the last 2 weeks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/storage/v4/object_storages/{storage_id}/restore", storage_id=storage_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncObjectStoragesResource(AsyncAPIResource):
    @cached_property
    def access_keys(self) -> AsyncAccessKeysResource:
        return AsyncAccessKeysResource(self._client)

    @cached_property
    def buckets(self) -> AsyncBucketsResource:
        return AsyncBucketsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncObjectStoragesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectStoragesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectStoragesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncObjectStoragesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        location_name: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> S3StorageCreated:
        """
        Creates a new S3-compatible storage instance in the specified location and
        returns the storage details including credentials.

        Args:
          location_name: Location code where the storage should be created

          name: User-defined name for the storage instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/storage/v4/object_storages",
            body=await async_maybe_transform(
                {
                    "location_name": location_name,
                    "name": name,
                },
                object_storage_create_params.ObjectStorageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3StorageCreated,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        limit: int | Omit = omit,
        location_name: str | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        provisioning_status: Literal["active", "creating", "updating", "deleting", "deleted"] | Omit = omit,
        show_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[S3Storage, AsyncOffsetPage[S3Storage]]:
        """
        Returns a paginated list of S3-compatible storage instances for the
        authenticated client.

        Args:
          id: Filter by storage ID

          limit: Max number of records in response

          location_name: Filter by storage location/region

          name: Filter by storage name

          offset: Number of records to skip

          provisioning_status: Filter by provisioning status

          show_deleted: Include deleted storages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/v4/object_storages",
            page=AsyncOffsetPage[S3Storage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "limit": limit,
                        "location_name": location_name,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "provisioning_status": provisioning_status,
                        "show_deleted": show_deleted,
                    },
                    object_storage_list_params.ObjectStorageListParams,
                ),
            ),
            model=S3Storage,
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
        """Deletes an S3-compatible storage instance.

        This operation cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/storage/v4/object_storages/{storage_id}", storage_id=storage_id),
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
    ) -> S3Storage:
        """
        Returns details of a specific S3-compatible storage instance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/storage/v4/object_storages/{storage_id}", storage_id=storage_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3Storage,
        )

    async def restore(
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
        """
        Restores a previously deleted S3-compatible storage instance if it was deleted
        within the last 2 weeks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/storage/v4/object_storages/{storage_id}/restore", storage_id=storage_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ObjectStoragesResourceWithRawResponse:
    def __init__(self, object_storages: ObjectStoragesResource) -> None:
        self._object_storages = object_storages

        self.create = to_raw_response_wrapper(
            object_storages.create,
        )
        self.list = to_raw_response_wrapper(
            object_storages.list,
        )
        self.delete = to_raw_response_wrapper(
            object_storages.delete,
        )
        self.get = to_raw_response_wrapper(
            object_storages.get,
        )
        self.restore = to_raw_response_wrapper(
            object_storages.restore,
        )

    @cached_property
    def access_keys(self) -> AccessKeysResourceWithRawResponse:
        return AccessKeysResourceWithRawResponse(self._object_storages.access_keys)

    @cached_property
    def buckets(self) -> BucketsResourceWithRawResponse:
        return BucketsResourceWithRawResponse(self._object_storages.buckets)


class AsyncObjectStoragesResourceWithRawResponse:
    def __init__(self, object_storages: AsyncObjectStoragesResource) -> None:
        self._object_storages = object_storages

        self.create = async_to_raw_response_wrapper(
            object_storages.create,
        )
        self.list = async_to_raw_response_wrapper(
            object_storages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            object_storages.delete,
        )
        self.get = async_to_raw_response_wrapper(
            object_storages.get,
        )
        self.restore = async_to_raw_response_wrapper(
            object_storages.restore,
        )

    @cached_property
    def access_keys(self) -> AsyncAccessKeysResourceWithRawResponse:
        return AsyncAccessKeysResourceWithRawResponse(self._object_storages.access_keys)

    @cached_property
    def buckets(self) -> AsyncBucketsResourceWithRawResponse:
        return AsyncBucketsResourceWithRawResponse(self._object_storages.buckets)


class ObjectStoragesResourceWithStreamingResponse:
    def __init__(self, object_storages: ObjectStoragesResource) -> None:
        self._object_storages = object_storages

        self.create = to_streamed_response_wrapper(
            object_storages.create,
        )
        self.list = to_streamed_response_wrapper(
            object_storages.list,
        )
        self.delete = to_streamed_response_wrapper(
            object_storages.delete,
        )
        self.get = to_streamed_response_wrapper(
            object_storages.get,
        )
        self.restore = to_streamed_response_wrapper(
            object_storages.restore,
        )

    @cached_property
    def access_keys(self) -> AccessKeysResourceWithStreamingResponse:
        return AccessKeysResourceWithStreamingResponse(self._object_storages.access_keys)

    @cached_property
    def buckets(self) -> BucketsResourceWithStreamingResponse:
        return BucketsResourceWithStreamingResponse(self._object_storages.buckets)


class AsyncObjectStoragesResourceWithStreamingResponse:
    def __init__(self, object_storages: AsyncObjectStoragesResource) -> None:
        self._object_storages = object_storages

        self.create = async_to_streamed_response_wrapper(
            object_storages.create,
        )
        self.list = async_to_streamed_response_wrapper(
            object_storages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            object_storages.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            object_storages.get,
        )
        self.restore = async_to_streamed_response_wrapper(
            object_storages.restore,
        )

    @cached_property
    def access_keys(self) -> AsyncAccessKeysResourceWithStreamingResponse:
        return AsyncAccessKeysResourceWithStreamingResponse(self._object_storages.access_keys)

    @cached_property
    def buckets(self) -> AsyncBucketsResourceWithStreamingResponse:
        return AsyncBucketsResourceWithStreamingResponse(self._object_storages.buckets)

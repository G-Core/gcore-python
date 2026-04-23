# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.storage.object_storages import bucket_list_params, bucket_create_params, bucket_update_params
from ....types.storage.object_storages.bucket import Bucket

__all__ = ["BucketsResource", "AsyncBucketsResource"]


class BucketsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BucketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return BucketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BucketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return BucketsResourceWithStreamingResponse(self)

    def create(
        self,
        storage_id: int,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Bucket:
        """
        Creates a new bucket within an S3-compatible storage.

        Args:
          name: Name of the bucket to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/storage/v4/object_storages/{storage_id}/buckets", storage_id=storage_id),
            body=maybe_transform({"name": name}, bucket_create_params.BucketCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bucket,
        )

    def update(
        self,
        bucket_name: str,
        *,
        storage_id: int,
        cors: bucket_update_params.Cors | Omit = omit,
        lifecycle: bucket_update_params.Lifecycle | Omit = omit,
        policy: bucket_update_params.Policy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Bucket:
        """Updates bucket CORS, Lifecycle, and/or Policy settings.

        Supports partial
        updates - only specified fields will be modified.

        Lifecycle: set `expiration_days` to a positive integer to enable, null or 0 to
        remove. Negative values return 400. CORS: set `allowed_origins` to a non-empty
        array to configure, empty array to remove. Policy: set `is_public` to true/false
        to update.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return self._patch(
            path_template(
                "/storage/v4/object_storages/{storage_id}/buckets/{bucket_name}",
                storage_id=storage_id,
                bucket_name=bucket_name,
            ),
            body=maybe_transform(
                {
                    "cors": cors,
                    "lifecycle": lifecycle,
                    "policy": policy,
                },
                bucket_update_params.BucketUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bucket,
        )

    def list(
        self,
        storage_id: int,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[Bucket]:
        """
        Returns a paginated list of buckets for an S3-compatible storage, including each
        bucket's CORS, Lifecycle, and Policy configuration. Results are sorted
        alphabetically by bucket name (ascending).

        Args:
          limit: Max number of records in response

          offset: Number of records to skip before beginning to return results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            path_template("/storage/v4/object_storages/{storage_id}/buckets", storage_id=storage_id),
            page=SyncOffsetPage[Bucket],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    bucket_list_params.BucketListParams,
                ),
            ),
            model=Bucket,
        )

    def delete(
        self,
        bucket_name: str,
        *,
        storage_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes a bucket from an S3-compatible storage.

        All objects in the bucket will
        be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/storage/v4/object_storages/{storage_id}/buckets/{bucket_name}",
                storage_id=storage_id,
                bucket_name=bucket_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        bucket_name: str,
        *,
        storage_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Bucket:
        """
        Returns bucket configuration including CORS, Lifecycle, and Policy settings in a
        consolidated response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return self._get(
            path_template(
                "/storage/v4/object_storages/{storage_id}/buckets/{bucket_name}",
                storage_id=storage_id,
                bucket_name=bucket_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bucket,
        )


class AsyncBucketsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBucketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBucketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBucketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncBucketsResourceWithStreamingResponse(self)

    async def create(
        self,
        storage_id: int,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Bucket:
        """
        Creates a new bucket within an S3-compatible storage.

        Args:
          name: Name of the bucket to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/storage/v4/object_storages/{storage_id}/buckets", storage_id=storage_id),
            body=await async_maybe_transform({"name": name}, bucket_create_params.BucketCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bucket,
        )

    async def update(
        self,
        bucket_name: str,
        *,
        storage_id: int,
        cors: bucket_update_params.Cors | Omit = omit,
        lifecycle: bucket_update_params.Lifecycle | Omit = omit,
        policy: bucket_update_params.Policy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Bucket:
        """Updates bucket CORS, Lifecycle, and/or Policy settings.

        Supports partial
        updates - only specified fields will be modified.

        Lifecycle: set `expiration_days` to a positive integer to enable, null or 0 to
        remove. Negative values return 400. CORS: set `allowed_origins` to a non-empty
        array to configure, empty array to remove. Policy: set `is_public` to true/false
        to update.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return await self._patch(
            path_template(
                "/storage/v4/object_storages/{storage_id}/buckets/{bucket_name}",
                storage_id=storage_id,
                bucket_name=bucket_name,
            ),
            body=await async_maybe_transform(
                {
                    "cors": cors,
                    "lifecycle": lifecycle,
                    "policy": policy,
                },
                bucket_update_params.BucketUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bucket,
        )

    def list(
        self,
        storage_id: int,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Bucket, AsyncOffsetPage[Bucket]]:
        """
        Returns a paginated list of buckets for an S3-compatible storage, including each
        bucket's CORS, Lifecycle, and Policy configuration. Results are sorted
        alphabetically by bucket name (ascending).

        Args:
          limit: Max number of records in response

          offset: Number of records to skip before beginning to return results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            path_template("/storage/v4/object_storages/{storage_id}/buckets", storage_id=storage_id),
            page=AsyncOffsetPage[Bucket],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    bucket_list_params.BucketListParams,
                ),
            ),
            model=Bucket,
        )

    async def delete(
        self,
        bucket_name: str,
        *,
        storage_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes a bucket from an S3-compatible storage.

        All objects in the bucket will
        be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/storage/v4/object_storages/{storage_id}/buckets/{bucket_name}",
                storage_id=storage_id,
                bucket_name=bucket_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        bucket_name: str,
        *,
        storage_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Bucket:
        """
        Returns bucket configuration including CORS, Lifecycle, and Policy settings in a
        consolidated response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return await self._get(
            path_template(
                "/storage/v4/object_storages/{storage_id}/buckets/{bucket_name}",
                storage_id=storage_id,
                bucket_name=bucket_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bucket,
        )


class BucketsResourceWithRawResponse:
    def __init__(self, buckets: BucketsResource) -> None:
        self._buckets = buckets

        self.create = to_raw_response_wrapper(
            buckets.create,
        )
        self.update = to_raw_response_wrapper(
            buckets.update,
        )
        self.list = to_raw_response_wrapper(
            buckets.list,
        )
        self.delete = to_raw_response_wrapper(
            buckets.delete,
        )
        self.get = to_raw_response_wrapper(
            buckets.get,
        )


class AsyncBucketsResourceWithRawResponse:
    def __init__(self, buckets: AsyncBucketsResource) -> None:
        self._buckets = buckets

        self.create = async_to_raw_response_wrapper(
            buckets.create,
        )
        self.update = async_to_raw_response_wrapper(
            buckets.update,
        )
        self.list = async_to_raw_response_wrapper(
            buckets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            buckets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            buckets.get,
        )


class BucketsResourceWithStreamingResponse:
    def __init__(self, buckets: BucketsResource) -> None:
        self._buckets = buckets

        self.create = to_streamed_response_wrapper(
            buckets.create,
        )
        self.update = to_streamed_response_wrapper(
            buckets.update,
        )
        self.list = to_streamed_response_wrapper(
            buckets.list,
        )
        self.delete = to_streamed_response_wrapper(
            buckets.delete,
        )
        self.get = to_streamed_response_wrapper(
            buckets.get,
        )


class AsyncBucketsResourceWithStreamingResponse:
    def __init__(self, buckets: AsyncBucketsResource) -> None:
        self._buckets = buckets

        self.create = async_to_streamed_response_wrapper(
            buckets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            buckets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            buckets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            buckets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            buckets.get,
        )

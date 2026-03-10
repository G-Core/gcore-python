# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions

import httpx

from .cors import (
    CorsResource,
    AsyncCorsResource,
    CorsResourceWithRawResponse,
    AsyncCorsResourceWithRawResponse,
    CorsResourceWithStreamingResponse,
    AsyncCorsResourceWithStreamingResponse,
)
from .policy import (
    PolicyResource,
    AsyncPolicyResource,
    PolicyResourceWithRawResponse,
    AsyncPolicyResourceWithRawResponse,
    PolicyResourceWithStreamingResponse,
    AsyncPolicyResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform
from .lifecycle import (
    LifecycleResource,
    AsyncLifecycleResource,
    LifecycleResourceWithRawResponse,
    AsyncLifecycleResourceWithRawResponse,
    LifecycleResourceWithStreamingResponse,
    AsyncLifecycleResourceWithStreamingResponse,
)
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
from ....types.storage import bucket_list_params
from ....types.storage.bucket import Bucket

__all__ = ["BucketsResource", "AsyncBucketsResource"]


class BucketsResource(SyncAPIResource):
    @cached_property
    def cors(self) -> CorsResource:
        return CorsResource(self._client)

    @cached_property
    def lifecycle(self) -> LifecycleResource:
        return LifecycleResource(self._client)

    @cached_property
    def policy(self) -> PolicyResource:
        return PolicyResource(self._client)

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

    @typing_extensions.deprecated("deprecated")
    def create(
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
        """Creates a new bucket within an S3 storage.

        Only applicable to S3-compatible
        storages.

        Deprecated: Use POST /v4/`object_storages`/{`storage_id`}/buckets with {"name":
        "bucket-name"} instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
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
        Returns the list of buckets for the storage in a wrapped response.

        Response format: count: total number of buckets (independent of pagination)
        results: current page of buckets according to limit/offset

        Deprecated: Use GET /v4/`object_storages`/{`storage_id`}/buckets/{`bucket_name`}
        for individual bucket details instead.

        Args:
          limit: Max number of records in response

          offset: Number of records to skip before beginning to write in response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/storage/provisioning/v2/storage/{storage_id}/s3/buckets",
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

    @typing_extensions.deprecated("deprecated")
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
        """Removes a bucket from an S3 storage.

        All objects in the bucket will be
        automatically deleted before the bucket is removed.

        Deprecated: Use DELETE
        /v4/`object_storages`/{`storage_id`}/buckets/{`bucket_name`} instead.

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
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBucketsResource(AsyncAPIResource):
    @cached_property
    def cors(self) -> AsyncCorsResource:
        return AsyncCorsResource(self._client)

    @cached_property
    def lifecycle(self) -> AsyncLifecycleResource:
        return AsyncLifecycleResource(self._client)

    @cached_property
    def policy(self) -> AsyncPolicyResource:
        return AsyncPolicyResource(self._client)

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

    @typing_extensions.deprecated("deprecated")
    async def create(
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
        """Creates a new bucket within an S3 storage.

        Only applicable to S3-compatible
        storages.

        Deprecated: Use POST /v4/`object_storages`/{`storage_id`}/buckets with {"name":
        "bucket-name"} instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
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
        Returns the list of buckets for the storage in a wrapped response.

        Response format: count: total number of buckets (independent of pagination)
        results: current page of buckets according to limit/offset

        Deprecated: Use GET /v4/`object_storages`/{`storage_id`}/buckets/{`bucket_name`}
        for individual bucket details instead.

        Args:
          limit: Max number of records in response

          offset: Number of records to skip before beginning to write in response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/storage/provisioning/v2/storage/{storage_id}/s3/buckets",
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

    @typing_extensions.deprecated("deprecated")
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
        """Removes a bucket from an S3 storage.

        All objects in the bucket will be
        automatically deleted before the bucket is removed.

        Deprecated: Use DELETE
        /v4/`object_storages`/{`storage_id`}/buckets/{`bucket_name`} instead.

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
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BucketsResourceWithRawResponse:
    def __init__(self, buckets: BucketsResource) -> None:
        self._buckets = buckets

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                buckets.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                buckets.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                buckets.delete,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def cors(self) -> CorsResourceWithRawResponse:
        return CorsResourceWithRawResponse(self._buckets.cors)

    @cached_property
    def lifecycle(self) -> LifecycleResourceWithRawResponse:
        return LifecycleResourceWithRawResponse(self._buckets.lifecycle)

    @cached_property
    def policy(self) -> PolicyResourceWithRawResponse:
        return PolicyResourceWithRawResponse(self._buckets.policy)


class AsyncBucketsResourceWithRawResponse:
    def __init__(self, buckets: AsyncBucketsResource) -> None:
        self._buckets = buckets

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                buckets.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                buckets.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                buckets.delete,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def cors(self) -> AsyncCorsResourceWithRawResponse:
        return AsyncCorsResourceWithRawResponse(self._buckets.cors)

    @cached_property
    def lifecycle(self) -> AsyncLifecycleResourceWithRawResponse:
        return AsyncLifecycleResourceWithRawResponse(self._buckets.lifecycle)

    @cached_property
    def policy(self) -> AsyncPolicyResourceWithRawResponse:
        return AsyncPolicyResourceWithRawResponse(self._buckets.policy)


class BucketsResourceWithStreamingResponse:
    def __init__(self, buckets: BucketsResource) -> None:
        self._buckets = buckets

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                buckets.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                buckets.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                buckets.delete,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def cors(self) -> CorsResourceWithStreamingResponse:
        return CorsResourceWithStreamingResponse(self._buckets.cors)

    @cached_property
    def lifecycle(self) -> LifecycleResourceWithStreamingResponse:
        return LifecycleResourceWithStreamingResponse(self._buckets.lifecycle)

    @cached_property
    def policy(self) -> PolicyResourceWithStreamingResponse:
        return PolicyResourceWithStreamingResponse(self._buckets.policy)


class AsyncBucketsResourceWithStreamingResponse:
    def __init__(self, buckets: AsyncBucketsResource) -> None:
        self._buckets = buckets

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                buckets.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                buckets.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                buckets.delete,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def cors(self) -> AsyncCorsResourceWithStreamingResponse:
        return AsyncCorsResourceWithStreamingResponse(self._buckets.cors)

    @cached_property
    def lifecycle(self) -> AsyncLifecycleResourceWithStreamingResponse:
        return AsyncLifecycleResourceWithStreamingResponse(self._buckets.lifecycle)

    @cached_property
    def policy(self) -> AsyncPolicyResourceWithStreamingResponse:
        return AsyncPolicyResourceWithStreamingResponse(self._buckets.policy)

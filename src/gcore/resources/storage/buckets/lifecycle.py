# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.storage.buckets import lifecycle_create_params

__all__ = ["LifecycleResource", "AsyncLifecycleResource"]


class LifecycleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LifecycleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return LifecycleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LifecycleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return LifecycleResourceWithStreamingResponse(self)

    def create(
        self,
        bucket_name: str,
        *,
        storage_id: int,
        expiration_days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sets up automatic object expiration for an S3 bucket.

        All objects in the bucket
        will be automatically deleted after the specified number of days to help manage
        storage costs and meet compliance requirements. This applies a global lifecycle
        rule to the entire bucket - all existing and future objects will be subject to
        the expiration policy.

        Args:
          expiration_days: Number of days after which objects will be automatically deleted from the
              bucket. Must be a positive integer. Common values: 30 for monthly cleanup, 365
              for yearly retention.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/lifecycle",
            body=maybe_transform({"expiration_days": expiration_days}, lifecycle_create_params.LifecycleCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        """
        Removes all lifecycle rules from an S3 bucket, disabling automatic object
        expiration. Objects will no longer be automatically deleted based on age.

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
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/lifecycle",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLifecycleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLifecycleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLifecycleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLifecycleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncLifecycleResourceWithStreamingResponse(self)

    async def create(
        self,
        bucket_name: str,
        *,
        storage_id: int,
        expiration_days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sets up automatic object expiration for an S3 bucket.

        All objects in the bucket
        will be automatically deleted after the specified number of days to help manage
        storage costs and meet compliance requirements. This applies a global lifecycle
        rule to the entire bucket - all existing and future objects will be subject to
        the expiration policy.

        Args:
          expiration_days: Number of days after which objects will be automatically deleted from the
              bucket. Must be a positive integer. Common values: 30 for monthly cleanup, 365
              for yearly retention.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/lifecycle",
            body=await async_maybe_transform(
                {"expiration_days": expiration_days}, lifecycle_create_params.LifecycleCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        """
        Removes all lifecycle rules from an S3 bucket, disabling automatic object
        expiration. Objects will no longer be automatically deleted based on age.

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
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/lifecycle",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LifecycleResourceWithRawResponse:
    def __init__(self, lifecycle: LifecycleResource) -> None:
        self._lifecycle = lifecycle

        self.create = to_raw_response_wrapper(
            lifecycle.create,
        )
        self.delete = to_raw_response_wrapper(
            lifecycle.delete,
        )


class AsyncLifecycleResourceWithRawResponse:
    def __init__(self, lifecycle: AsyncLifecycleResource) -> None:
        self._lifecycle = lifecycle

        self.create = async_to_raw_response_wrapper(
            lifecycle.create,
        )
        self.delete = async_to_raw_response_wrapper(
            lifecycle.delete,
        )


class LifecycleResourceWithStreamingResponse:
    def __init__(self, lifecycle: LifecycleResource) -> None:
        self._lifecycle = lifecycle

        self.create = to_streamed_response_wrapper(
            lifecycle.create,
        )
        self.delete = to_streamed_response_wrapper(
            lifecycle.delete,
        )


class AsyncLifecycleResourceWithStreamingResponse:
    def __init__(self, lifecycle: AsyncLifecycleResource) -> None:
        self._lifecycle = lifecycle

        self.create = async_to_streamed_response_wrapper(
            lifecycle.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            lifecycle.delete,
        )

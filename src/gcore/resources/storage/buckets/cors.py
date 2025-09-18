# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.storage.buckets import cor_create_params
from ....types.storage.buckets.bucket_cors import BucketCors

__all__ = ["CorsResource", "AsyncCorsResource"]


class CorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return CorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return CorsResourceWithStreamingResponse(self)

    def create(
        self,
        bucket_name: str,
        *,
        storage_id: int,
        allowed_origins: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Configures Cross-Origin Resource Sharing (CORS) rules for an S3 bucket, allowing
        web applications from specified domains to access bucket resources directly from
        browsers.

        Args:
          allowed_origins: List of allowed origins for CORS requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/cors",
            body=maybe_transform({"allowed_origins": allowed_origins}, cor_create_params.CorCreateParams),
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
    ) -> BucketCors:
        """
        Retrieves the current Cross-Origin Resource Sharing (CORS) configuration for an
        S3 bucket, showing which domains are allowed to access the bucket from web
        browsers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return self._get(
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/cors",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BucketCors,
        )


class AsyncCorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncCorsResourceWithStreamingResponse(self)

    async def create(
        self,
        bucket_name: str,
        *,
        storage_id: int,
        allowed_origins: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Configures Cross-Origin Resource Sharing (CORS) rules for an S3 bucket, allowing
        web applications from specified domains to access bucket resources directly from
        browsers.

        Args:
          allowed_origins: List of allowed origins for CORS requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/cors",
            body=await async_maybe_transform({"allowed_origins": allowed_origins}, cor_create_params.CorCreateParams),
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
    ) -> BucketCors:
        """
        Retrieves the current Cross-Origin Resource Sharing (CORS) configuration for an
        S3 bucket, showing which domains are allowed to access the bucket from web
        browsers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return await self._get(
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/cors",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BucketCors,
        )


class CorsResourceWithRawResponse:
    def __init__(self, cors: CorsResource) -> None:
        self._cors = cors

        self.create = to_raw_response_wrapper(
            cors.create,
        )
        self.get = to_raw_response_wrapper(
            cors.get,
        )


class AsyncCorsResourceWithRawResponse:
    def __init__(self, cors: AsyncCorsResource) -> None:
        self._cors = cors

        self.create = async_to_raw_response_wrapper(
            cors.create,
        )
        self.get = async_to_raw_response_wrapper(
            cors.get,
        )


class CorsResourceWithStreamingResponse:
    def __init__(self, cors: CorsResource) -> None:
        self._cors = cors

        self.create = to_streamed_response_wrapper(
            cors.create,
        )
        self.get = to_streamed_response_wrapper(
            cors.get,
        )


class AsyncCorsResourceWithStreamingResponse:
    def __init__(self, cors: AsyncCorsResource) -> None:
        self._cors = cors

        self.create = async_to_streamed_response_wrapper(
            cors.create,
        )
        self.get = async_to_streamed_response_wrapper(
            cors.get,
        )

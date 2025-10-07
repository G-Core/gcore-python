# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.storage.buckets.policy_get_response import PolicyGetResponse

__all__ = ["PolicyResource", "AsyncPolicyResource"]


class PolicyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PolicyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PolicyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolicyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PolicyResourceWithStreamingResponse(self)

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
        """
        Applies a public read policy to the S3 bucket, allowing anonymous users to
        download/access all objects in the bucket via HTTP GET requests. This makes the
        bucket suitable for static website hosting, public file sharing, or CDN
        integration. Only grants read access - users cannot upload, modify, or delete
        objects without proper authentication.

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
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/policy",
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
        Removes the public read policy from an S3 bucket, making all objects private and
        accessible only with proper authentication credentials. After this operation,
        anonymous users will no longer be able to access bucket contents via HTTP
        requests.

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
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/policy",
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
    ) -> PolicyGetResponse:
        """
        Returns whether the S3 bucket is currently configured for public read access.
        Shows if anonymous users can download objects from the bucket via HTTP requests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return self._get(
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/policy",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyGetResponse,
        )


class AsyncPolicyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPolicyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolicyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolicyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPolicyResourceWithStreamingResponse(self)

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
        """
        Applies a public read policy to the S3 bucket, allowing anonymous users to
        download/access all objects in the bucket via HTTP GET requests. This makes the
        bucket suitable for static website hosting, public file sharing, or CDN
        integration. Only grants read access - users cannot upload, modify, or delete
        objects without proper authentication.

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
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/policy",
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
        Removes the public read policy from an S3 bucket, making all objects private and
        accessible only with proper authentication credentials. After this operation,
        anonymous users will no longer be able to access bucket contents via HTTP
        requests.

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
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/policy",
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
    ) -> PolicyGetResponse:
        """
        Returns whether the S3 bucket is currently configured for public read access.
        Shows if anonymous users can download objects from the bucket via HTTP requests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return await self._get(
            f"/storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/policy",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyGetResponse,
        )


class PolicyResourceWithRawResponse:
    def __init__(self, policy: PolicyResource) -> None:
        self._policy = policy

        self.create = to_raw_response_wrapper(
            policy.create,
        )
        self.delete = to_raw_response_wrapper(
            policy.delete,
        )
        self.get = to_raw_response_wrapper(
            policy.get,
        )


class AsyncPolicyResourceWithRawResponse:
    def __init__(self, policy: AsyncPolicyResource) -> None:
        self._policy = policy

        self.create = async_to_raw_response_wrapper(
            policy.create,
        )
        self.delete = async_to_raw_response_wrapper(
            policy.delete,
        )
        self.get = async_to_raw_response_wrapper(
            policy.get,
        )


class PolicyResourceWithStreamingResponse:
    def __init__(self, policy: PolicyResource) -> None:
        self._policy = policy

        self.create = to_streamed_response_wrapper(
            policy.create,
        )
        self.delete = to_streamed_response_wrapper(
            policy.delete,
        )
        self.get = to_streamed_response_wrapper(
            policy.get,
        )


class AsyncPolicyResourceWithStreamingResponse:
    def __init__(self, policy: AsyncPolicyResource) -> None:
        self._policy = policy

        self.create = async_to_streamed_response_wrapper(
            policy.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            policy.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            policy.get,
        )

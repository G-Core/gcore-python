# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.storage import credential_recreate_params
from ...types.storage.storage import Storage

__all__ = ["CredentialsResource", "AsyncCredentialsResource"]


class CredentialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return CredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return CredentialsResourceWithStreamingResponse(self)

    def recreate(
        self,
        storage_id: int,
        *,
        delete_sftp_password: bool | Omit = omit,
        generate_s3_keys: bool | Omit = omit,
        generate_sftp_password: bool | Omit = omit,
        reset_sftp_keys: bool | Omit = omit,
        sftp_password: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        """
        Generates new access credentials for the storage (S3 keys for S3 storage, SFTP
        password for SFTP storage).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/credentials",
            body=maybe_transform(
                {
                    "delete_sftp_password": delete_sftp_password,
                    "generate_s3_keys": generate_s3_keys,
                    "generate_sftp_password": generate_sftp_password,
                    "reset_sftp_keys": reset_sftp_keys,
                    "sftp_password": sftp_password,
                },
                credential_recreate_params.CredentialRecreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Storage,
        )


class AsyncCredentialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncCredentialsResourceWithStreamingResponse(self)

    async def recreate(
        self,
        storage_id: int,
        *,
        delete_sftp_password: bool | Omit = omit,
        generate_s3_keys: bool | Omit = omit,
        generate_sftp_password: bool | Omit = omit,
        reset_sftp_keys: bool | Omit = omit,
        sftp_password: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        """
        Generates new access credentials for the storage (S3 keys for S3 storage, SFTP
        password for SFTP storage).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/storage/provisioning/v1/storage/{storage_id}/credentials",
            body=await async_maybe_transform(
                {
                    "delete_sftp_password": delete_sftp_password,
                    "generate_s3_keys": generate_s3_keys,
                    "generate_sftp_password": generate_sftp_password,
                    "reset_sftp_keys": reset_sftp_keys,
                    "sftp_password": sftp_password,
                },
                credential_recreate_params.CredentialRecreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Storage,
        )


class CredentialsResourceWithRawResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.recreate = to_raw_response_wrapper(
            credentials.recreate,
        )


class AsyncCredentialsResourceWithRawResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.recreate = async_to_raw_response_wrapper(
            credentials.recreate,
        )


class CredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.recreate = to_streamed_response_wrapper(
            credentials.recreate,
        )


class AsyncCredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.recreate = async_to_streamed_response_wrapper(
            credentials.recreate,
        )

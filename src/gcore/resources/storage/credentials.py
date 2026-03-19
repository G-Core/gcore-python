# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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

    @typing_extensions.deprecated("deprecated")
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
        WARNING: This is a destructive operation — it removes ALL existing access keys
        and generates a single new key pair. Any applications using the old keys will
        lose access immediately.

        For S3 storage this replaces all existing access keys with a single new key
        pair. For SFTP storage this resets the password.

        Deprecated: Use POST /v4/`object_storages`/{`storage_id`}/`access_keys` to
        create individual access keys, DELETE
        /v4/`object_storages`/{`storage_id`}/`access_keys`/{`access_key`} to remove
        specific keys, or PATCH /v4/`sftp_storages`/{`storage_id`}/credentials for SFTP
        storage instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/storage/provisioning/v1/storage/{storage_id}/credentials", storage_id=storage_id),
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

    @typing_extensions.deprecated("deprecated")
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
        WARNING: This is a destructive operation — it removes ALL existing access keys
        and generates a single new key pair. Any applications using the old keys will
        lose access immediately.

        For S3 storage this replaces all existing access keys with a single new key
        pair. For SFTP storage this resets the password.

        Deprecated: Use POST /v4/`object_storages`/{`storage_id`}/`access_keys` to
        create individual access keys, DELETE
        /v4/`object_storages`/{`storage_id`}/`access_keys`/{`access_key`} to remove
        specific keys, or PATCH /v4/`sftp_storages`/{`storage_id`}/credentials for SFTP
        storage instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/storage/provisioning/v1/storage/{storage_id}/credentials", storage_id=storage_id),
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

        self.recreate = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                credentials.recreate,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncCredentialsResourceWithRawResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.recreate = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                credentials.recreate,  # pyright: ignore[reportDeprecated],
            )
        )


class CredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.recreate = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                credentials.recreate,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncCredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.recreate = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                credentials.recreate,  # pyright: ignore[reportDeprecated],
            )
        )

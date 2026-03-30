# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.storage import ssh_key_list_params, ssh_key_create_params
from ...types.storage.ssh_key import SSHKey

__all__ = ["SSHKeysResource", "AsyncSSHKeysResource"]


class SSHKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SSHKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return SSHKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSHKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return SSHKeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        public_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSHKey:
        """Creates an SSH public key for SFTP storage access.

        These keys are used for
        passwordless authentication to SFTP storages.

        Args:
          name: User-defined name for the SSH key

          public_key: The SSH public key content (ssh-rsa or ssh-ed25519 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/storage/v4/ssh_keys",
            body=maybe_transform(
                {
                    "name": name,
                    "public_key": public_key,
                },
                ssh_key_create_params.SSHKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSHKey,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[SSHKey]:
        """
        Returns a paginated list of all SSH public keys for SFTP storage access.

        Args:
          limit: Maximum number of items to return

          name: Filter by name (partial match)

          offset: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/v4/ssh_keys",
            page=SyncOffsetPage[SSHKey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    ssh_key_list_params.SSHKeyListParams,
                ),
            ),
            model=SSHKey,
        )

    def delete(
        self,
        ssh_key_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes an SSH public key.

        This will revoke SFTP access for any storages using
        this key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/storage/v4/ssh_keys/{ssh_key_id}", ssh_key_id=ssh_key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        ssh_key_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSHKey:
        """
        Retrieves a single SSH key by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/storage/v4/ssh_keys/{ssh_key_id}", ssh_key_id=ssh_key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSHKey,
        )


class AsyncSSHKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSSHKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSSHKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSHKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncSSHKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        public_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSHKey:
        """Creates an SSH public key for SFTP storage access.

        These keys are used for
        passwordless authentication to SFTP storages.

        Args:
          name: User-defined name for the SSH key

          public_key: The SSH public key content (ssh-rsa or ssh-ed25519 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/storage/v4/ssh_keys",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "public_key": public_key,
                },
                ssh_key_create_params.SSHKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSHKey,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SSHKey, AsyncOffsetPage[SSHKey]]:
        """
        Returns a paginated list of all SSH public keys for SFTP storage access.

        Args:
          limit: Maximum number of items to return

          name: Filter by name (partial match)

          offset: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/v4/ssh_keys",
            page=AsyncOffsetPage[SSHKey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    ssh_key_list_params.SSHKeyListParams,
                ),
            ),
            model=SSHKey,
        )

    async def delete(
        self,
        ssh_key_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes an SSH public key.

        This will revoke SFTP access for any storages using
        this key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/storage/v4/ssh_keys/{ssh_key_id}", ssh_key_id=ssh_key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        ssh_key_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSHKey:
        """
        Retrieves a single SSH key by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/storage/v4/ssh_keys/{ssh_key_id}", ssh_key_id=ssh_key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSHKey,
        )


class SSHKeysResourceWithRawResponse:
    def __init__(self, ssh_keys: SSHKeysResource) -> None:
        self._ssh_keys = ssh_keys

        self.create = to_raw_response_wrapper(
            ssh_keys.create,
        )
        self.list = to_raw_response_wrapper(
            ssh_keys.list,
        )
        self.delete = to_raw_response_wrapper(
            ssh_keys.delete,
        )
        self.get = to_raw_response_wrapper(
            ssh_keys.get,
        )


class AsyncSSHKeysResourceWithRawResponse:
    def __init__(self, ssh_keys: AsyncSSHKeysResource) -> None:
        self._ssh_keys = ssh_keys

        self.create = async_to_raw_response_wrapper(
            ssh_keys.create,
        )
        self.list = async_to_raw_response_wrapper(
            ssh_keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ssh_keys.delete,
        )
        self.get = async_to_raw_response_wrapper(
            ssh_keys.get,
        )


class SSHKeysResourceWithStreamingResponse:
    def __init__(self, ssh_keys: SSHKeysResource) -> None:
        self._ssh_keys = ssh_keys

        self.create = to_streamed_response_wrapper(
            ssh_keys.create,
        )
        self.list = to_streamed_response_wrapper(
            ssh_keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            ssh_keys.delete,
        )
        self.get = to_streamed_response_wrapper(
            ssh_keys.get,
        )


class AsyncSSHKeysResourceWithStreamingResponse:
    def __init__(self, ssh_keys: AsyncSSHKeysResource) -> None:
        self._ssh_keys = ssh_keys

        self.create = async_to_streamed_response_wrapper(
            ssh_keys.create,
        )
        self.list = async_to_streamed_response_wrapper(
            ssh_keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ssh_keys.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            ssh_keys.get,
        )

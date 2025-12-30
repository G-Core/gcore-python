# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.cloud import ssh_key_list_params, ssh_key_create_params, ssh_key_update_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cloud.ssh_key import SSHKey
from ...types.cloud.ssh_key_created import SSHKeyCreated

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
        project_id: int | None = None,
        name: str,
        public_key: str | Omit = omit,
        shared_in_project: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSHKeyCreated:
        """
        To generate a key, omit the `public_key` parameter from the request body

        Args:
          project_id: Project ID

          name: SSH key name

          public_key: The public part of an SSH key is the shareable portion of an SSH key pair. It
              can be safely sent to servers or services to grant access. It does not contain
              sensitive information.

              - If you’re uploading your own key, provide the public part here (usually found
                in a file like `id_ed25519.pub`).
              - If you want the platform to generate an Ed25519 key pair for you, leave this
                field empty — the system will return the private key in the response **once
                only**.

          shared_in_project: SSH key is shared with all users in the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._post(
            f"/cloud/v1/ssh_keys/{project_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "public_key": public_key,
                    "shared_in_project": shared_in_project,
                },
                ssh_key_create_params.SSHKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSHKeyCreated,
        )

    def update(
        self,
        ssh_key_id: str,
        *,
        project_id: int | None = None,
        shared_in_project: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSHKey:
        """
        Share or unshare SSH key with users

        Args:
          project_id: Project ID

          ssh_key_id: SSH key ID

          shared_in_project: Share your ssh key with all users in the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not ssh_key_id:
            raise ValueError(f"Expected a non-empty value for `ssh_key_id` but received {ssh_key_id!r}")
        return self._patch(
            f"/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}",
            body=maybe_transform({"shared_in_project": shared_in_project}, ssh_key_update_params.SSHKeyUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSHKey,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["created_at.asc", "created_at.desc", "name.asc", "name.desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[SSHKey]:
        """
        List SSH keys

        Args:
          project_id: Project ID

          limit: Maximum number of SSH keys to return

          name: SSH key name. Partial substring match. Example: `name=abc` matches any key
              containing `abc` in name.

          offset: Offset for pagination

          order_by: Sort order for the SSH keys

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/ssh_keys/{project_id}",
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
        ssh_key_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete SSH key

        Args:
          project_id: Project ID

          ssh_key_id: SSH key ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not ssh_key_id:
            raise ValueError(f"Expected a non-empty value for `ssh_key_id` but received {ssh_key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        ssh_key_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSHKey:
        """
        Get SSH key

        Args:
          project_id: Project ID

          ssh_key_id: SSH key ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not ssh_key_id:
            raise ValueError(f"Expected a non-empty value for `ssh_key_id` but received {ssh_key_id!r}")
        return self._get(
            f"/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}",
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
        project_id: int | None = None,
        name: str,
        public_key: str | Omit = omit,
        shared_in_project: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSHKeyCreated:
        """
        To generate a key, omit the `public_key` parameter from the request body

        Args:
          project_id: Project ID

          name: SSH key name

          public_key: The public part of an SSH key is the shareable portion of an SSH key pair. It
              can be safely sent to servers or services to grant access. It does not contain
              sensitive information.

              - If you’re uploading your own key, provide the public part here (usually found
                in a file like `id_ed25519.pub`).
              - If you want the platform to generate an Ed25519 key pair for you, leave this
                field empty — the system will return the private key in the response **once
                only**.

          shared_in_project: SSH key is shared with all users in the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return await self._post(
            f"/cloud/v1/ssh_keys/{project_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "public_key": public_key,
                    "shared_in_project": shared_in_project,
                },
                ssh_key_create_params.SSHKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSHKeyCreated,
        )

    async def update(
        self,
        ssh_key_id: str,
        *,
        project_id: int | None = None,
        shared_in_project: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSHKey:
        """
        Share or unshare SSH key with users

        Args:
          project_id: Project ID

          ssh_key_id: SSH key ID

          shared_in_project: Share your ssh key with all users in the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not ssh_key_id:
            raise ValueError(f"Expected a non-empty value for `ssh_key_id` but received {ssh_key_id!r}")
        return await self._patch(
            f"/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}",
            body=await async_maybe_transform(
                {"shared_in_project": shared_in_project}, ssh_key_update_params.SSHKeyUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSHKey,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["created_at.asc", "created_at.desc", "name.asc", "name.desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SSHKey, AsyncOffsetPage[SSHKey]]:
        """
        List SSH keys

        Args:
          project_id: Project ID

          limit: Maximum number of SSH keys to return

          name: SSH key name. Partial substring match. Example: `name=abc` matches any key
              containing `abc` in name.

          offset: Offset for pagination

          order_by: Sort order for the SSH keys

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/ssh_keys/{project_id}",
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
        ssh_key_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete SSH key

        Args:
          project_id: Project ID

          ssh_key_id: SSH key ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not ssh_key_id:
            raise ValueError(f"Expected a non-empty value for `ssh_key_id` but received {ssh_key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        ssh_key_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSHKey:
        """
        Get SSH key

        Args:
          project_id: Project ID

          ssh_key_id: SSH key ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not ssh_key_id:
            raise ValueError(f"Expected a non-empty value for `ssh_key_id` but received {ssh_key_id!r}")
        return await self._get(
            f"/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}",
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
        self.update = to_raw_response_wrapper(
            ssh_keys.update,
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
        self.update = async_to_raw_response_wrapper(
            ssh_keys.update,
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
        self.update = to_streamed_response_wrapper(
            ssh_keys.update,
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
        self.update = async_to_streamed_response_wrapper(
            ssh_keys.update,
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

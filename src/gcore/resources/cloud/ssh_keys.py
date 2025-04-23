# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return SSHKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSHKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return SSHKeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        name: str,
        public_key: str | NotGiven = NOT_GIVEN,
        shared_in_project: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSHKeyCreated:
        """
        To generate a key, omit the public_key parameter from the request body

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}'].post.parameters[0].schema"

          name: '#/components/schemas/CreateSSHKeySerializer/properties/name'
              "$.components.schemas.CreateSSHKeySerializer.properties.name"

          public_key: '#/components/schemas/CreateSSHKeySerializer/properties/public_key'
              "$.components.schemas.CreateSSHKeySerializer.properties.public_key"

          shared_in_project: '#/components/schemas/CreateSSHKeySerializer/properties/shared_in_project'
              "$.components.schemas.CreateSSHKeySerializer.properties.shared_in_project"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSHKey:
        """
        Share or unshare SSH key with users

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D%2F%7Bssh_key_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}'].patch.parameters[0].schema"

          ssh_key_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D%2F%7Bssh_key_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}'].patch.parameters[1].schema"

          shared_in_project: '#/components/schemas/ShareSSHKeySerializer/properties/shared_in_project'
              "$.components.schemas.ShareSSHKeySerializer.properties.shared_in_project"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
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
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: Literal["created_at.asc", "created_at.desc", "name.asc", "name.desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[SSHKey]:
        """
        List SSH keys

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}'].get.parameters[0].schema"

          limit: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/get/parameters/1'
              "$.paths['/cloud/v1/ssh_keys/{project_id}'].get.parameters[1]"

          offset: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/ssh_keys/{project_id}'].get.parameters[2]"

          order_by: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/ssh_keys/{project_id}'].get.parameters[3]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete SSH key

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D%2F%7Bssh_key_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}']['delete'].parameters[0].schema"

          ssh_key_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D%2F%7Bssh_key_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}']['delete'].parameters[1].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSHKey:
        """
        Get SSH key

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D%2F%7Bssh_key_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}'].get.parameters[0].schema"

          ssh_key_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D%2F%7Bssh_key_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}'].get.parameters[1].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
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

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSSHKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSHKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncSSHKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        name: str,
        public_key: str | NotGiven = NOT_GIVEN,
        shared_in_project: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSHKeyCreated:
        """
        To generate a key, omit the public_key parameter from the request body

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}'].post.parameters[0].schema"

          name: '#/components/schemas/CreateSSHKeySerializer/properties/name'
              "$.components.schemas.CreateSSHKeySerializer.properties.name"

          public_key: '#/components/schemas/CreateSSHKeySerializer/properties/public_key'
              "$.components.schemas.CreateSSHKeySerializer.properties.public_key"

          shared_in_project: '#/components/schemas/CreateSSHKeySerializer/properties/shared_in_project'
              "$.components.schemas.CreateSSHKeySerializer.properties.shared_in_project"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSHKey:
        """
        Share or unshare SSH key with users

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D%2F%7Bssh_key_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}'].patch.parameters[0].schema"

          ssh_key_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D%2F%7Bssh_key_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}'].patch.parameters[1].schema"

          shared_in_project: '#/components/schemas/ShareSSHKeySerializer/properties/shared_in_project'
              "$.components.schemas.ShareSSHKeySerializer.properties.shared_in_project"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
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
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: Literal["created_at.asc", "created_at.desc", "name.asc", "name.desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SSHKey, AsyncOffsetPage[SSHKey]]:
        """
        List SSH keys

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}'].get.parameters[0].schema"

          limit: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/get/parameters/1'
              "$.paths['/cloud/v1/ssh_keys/{project_id}'].get.parameters[1]"

          offset: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/ssh_keys/{project_id}'].get.parameters[2]"

          order_by: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/ssh_keys/{project_id}'].get.parameters[3]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete SSH key

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D%2F%7Bssh_key_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}']['delete'].parameters[0].schema"

          ssh_key_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D%2F%7Bssh_key_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}']['delete'].parameters[1].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSHKey:
        """
        Get SSH key

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D%2F%7Bssh_key_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}'].get.parameters[0].schema"

          ssh_key_id: '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D%2F%7Bssh_key_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}'].get.parameters[1].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
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

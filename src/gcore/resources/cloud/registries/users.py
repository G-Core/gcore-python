# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ....types.cloud.registries import user_create_params, user_update_params, user_create_multiple_params
from ....types.cloud.registries.registry_user import RegistryUser
from ....types.cloud.registries.registry_user_list import RegistryUserList
from ....types.cloud.registries.registry_user_create import RegistryUserCreate
from ....types.cloud.registries.user_refresh_secret_response import UserRefreshSecretResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def create(
        self,
        registry_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        duration: int,
        name: str,
        read_only: bool | Omit = omit,
        secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryUserCreate:
        """
        Create a new user for accessing the container registry.

        Args:
          duration: User account operating time, days

          name: A name for the registry user.

              Should be in lowercase, consisting only of numbers and letters,

              with maximum length of 16 characters

          read_only: Read-only user

          secret: User secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._post(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users",
            body=maybe_transform(
                {
                    "duration": duration,
                    "name": name,
                    "read_only": read_only,
                    "secret": secret,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegistryUserCreate,
        )

    def update(
        self,
        user_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        registry_id: int,
        duration: int,
        read_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryUser:
        """
        Update the configuration of a specific registry user.

        Args:
          duration: User account operating time, days

          read_only: Read-only user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._patch(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}",
            body=maybe_transform(
                {
                    "duration": duration,
                    "read_only": read_only,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegistryUser,
        )

    def list(
        self,
        registry_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryUserList:
        """
        List all users with access to the container registry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegistryUserList,
        )

    def delete(
        self,
        user_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        registry_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific user from the container registry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_multiple(
        self,
        registry_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        users: Iterable[user_create_multiple_params.User],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryUserCreate:
        """
        Create multiple users for accessing the container registry in a single request.

        Args:
          users: Set of users

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._post(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/batch",
            body=maybe_transform({"users": users}, user_create_multiple_params.UserCreateMultipleParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegistryUserCreate,
        )

    def refresh_secret(
        self,
        user_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        registry_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRefreshSecretResponse:
        """
        Generate a new secret for a specific registry user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._post(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}/refresh_secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRefreshSecretResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        registry_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        duration: int,
        name: str,
        read_only: bool | Omit = omit,
        secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryUserCreate:
        """
        Create a new user for accessing the container registry.

        Args:
          duration: User account operating time, days

          name: A name for the registry user.

              Should be in lowercase, consisting only of numbers and letters,

              with maximum length of 16 characters

          read_only: Read-only user

          secret: User secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._post(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users",
            body=await async_maybe_transform(
                {
                    "duration": duration,
                    "name": name,
                    "read_only": read_only,
                    "secret": secret,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegistryUserCreate,
        )

    async def update(
        self,
        user_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        registry_id: int,
        duration: int,
        read_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryUser:
        """
        Update the configuration of a specific registry user.

        Args:
          duration: User account operating time, days

          read_only: Read-only user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._patch(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}",
            body=await async_maybe_transform(
                {
                    "duration": duration,
                    "read_only": read_only,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegistryUser,
        )

    async def list(
        self,
        registry_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryUserList:
        """
        List all users with access to the container registry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._get(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegistryUserList,
        )

    async def delete(
        self,
        user_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        registry_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific user from the container registry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_multiple(
        self,
        registry_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        users: Iterable[user_create_multiple_params.User],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryUserCreate:
        """
        Create multiple users for accessing the container registry in a single request.

        Args:
          users: Set of users

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._post(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/batch",
            body=await async_maybe_transform({"users": users}, user_create_multiple_params.UserCreateMultipleParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegistryUserCreate,
        )

    async def refresh_secret(
        self,
        user_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        registry_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRefreshSecretResponse:
        """
        Generate a new secret for a specific registry user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._post(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}/refresh_secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRefreshSecretResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.create_multiple = to_raw_response_wrapper(
            users.create_multiple,
        )
        self.refresh_secret = to_raw_response_wrapper(
            users.refresh_secret,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.create_multiple = async_to_raw_response_wrapper(
            users.create_multiple,
        )
        self.refresh_secret = async_to_raw_response_wrapper(
            users.refresh_secret,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.create_multiple = to_streamed_response_wrapper(
            users.create_multiple,
        )
        self.refresh_secret = to_streamed_response_wrapper(
            users.refresh_secret,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.create_multiple = async_to_streamed_response_wrapper(
            users.create_multiple,
        )
        self.refresh_secret = async_to_streamed_response_wrapper(
            users.refresh_secret,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ....types.cloud.registries.registry_user_created import RegistryUserCreated

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
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
        read_only: bool | NotGiven = NOT_GIVEN,
        secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegistryUser:
        """
        Create a user

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/post/parameters/0/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/post/parameters/1/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].post.parameters[1].schema"

          registry_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/post/parameters/2/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].post.parameters[2].schema"

          duration: '#/components/schemas/RegistryUserCreateSerializer/properties/duration'
              "$.components.schemas.RegistryUserCreateSerializer.properties.duration"

          name: '#/components/schemas/RegistryUserCreateSerializer/properties/name'
              "$.components.schemas.RegistryUserCreateSerializer.properties.name"

          read_only: '#/components/schemas/RegistryUserCreateSerializer/properties/read_only'
              "$.components.schemas.RegistryUserCreateSerializer.properties.read_only"

          secret: '#/components/schemas/RegistryUserCreateSerializer/properties/secret'
              "$.components.schemas.RegistryUserCreateSerializer.properties.secret"

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
            cast_to=RegistryUser,
        )

    def update(
        self,
        user_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        registry_id: int,
        duration: int,
        read_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegistryUser:
        """
        Update a user

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}'].patch.parameters[1].schema"

          registry_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}'].patch.parameters[2].schema"

          user_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/patch/parameters/3/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}'].patch.parameters[3].schema"

          duration: '#/components/schemas/RegistryUserUpdateSerializer/properties/duration'
              "$.components.schemas.RegistryUserUpdateSerializer.properties.duration"

          read_only: '#/components/schemas/RegistryUserUpdateSerializer/properties/read_only'
              "$.components.schemas.RegistryUserUpdateSerializer.properties.read_only"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegistryUserList:
        """
        Get user list

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/get/parameters/0/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/get/parameters/1/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].get.parameters[1].schema"

          registry_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/get/parameters/2/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].get.parameters[2].schema"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a user

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}']['delete'].parameters[1].schema"

          registry_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}']['delete'].parameters[2].schema"

          user_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/delete/parameters/3/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}']['delete'].parameters[3].schema"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegistryUserCreated:
        """
        Batch create users

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2Fbatch/post/parameters/0/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/batch'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2Fbatch/post/parameters/1/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/batch'].post.parameters[1].schema"

          registry_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2Fbatch/post/parameters/2/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/batch'].post.parameters[2].schema"

          users: '#/components/schemas/RegistryBatchUsersCreateSerializer/properties/users'
              "$.components.schemas.RegistryBatchUsersCreateSerializer.properties.users"

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
            cast_to=RegistryUserCreated,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Refresh a secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D%2Frefresh_secret/post/parameters/0/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}/refresh_secret'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D%2Frefresh_secret/post/parameters/1/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}/refresh_secret'].post.parameters[1].schema"

          registry_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D%2Frefresh_secret/post/parameters/2/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}/refresh_secret'].post.parameters[2].schema"

          user_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D%2Frefresh_secret/post/parameters/3/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}/refresh_secret'].post.parameters[3].schema"

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
        return self._post(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}/refresh_secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
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
        read_only: bool | NotGiven = NOT_GIVEN,
        secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegistryUser:
        """
        Create a user

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/post/parameters/0/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/post/parameters/1/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].post.parameters[1].schema"

          registry_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/post/parameters/2/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].post.parameters[2].schema"

          duration: '#/components/schemas/RegistryUserCreateSerializer/properties/duration'
              "$.components.schemas.RegistryUserCreateSerializer.properties.duration"

          name: '#/components/schemas/RegistryUserCreateSerializer/properties/name'
              "$.components.schemas.RegistryUserCreateSerializer.properties.name"

          read_only: '#/components/schemas/RegistryUserCreateSerializer/properties/read_only'
              "$.components.schemas.RegistryUserCreateSerializer.properties.read_only"

          secret: '#/components/schemas/RegistryUserCreateSerializer/properties/secret'
              "$.components.schemas.RegistryUserCreateSerializer.properties.secret"

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
            cast_to=RegistryUser,
        )

    async def update(
        self,
        user_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        registry_id: int,
        duration: int,
        read_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegistryUser:
        """
        Update a user

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}'].patch.parameters[1].schema"

          registry_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}'].patch.parameters[2].schema"

          user_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/patch/parameters/3/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}'].patch.parameters[3].schema"

          duration: '#/components/schemas/RegistryUserUpdateSerializer/properties/duration'
              "$.components.schemas.RegistryUserUpdateSerializer.properties.duration"

          read_only: '#/components/schemas/RegistryUserUpdateSerializer/properties/read_only'
              "$.components.schemas.RegistryUserUpdateSerializer.properties.read_only"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegistryUserList:
        """
        Get user list

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/get/parameters/0/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/get/parameters/1/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].get.parameters[1].schema"

          registry_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/get/parameters/2/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].get.parameters[2].schema"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a user

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}']['delete'].parameters[1].schema"

          registry_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}']['delete'].parameters[2].schema"

          user_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D/delete/parameters/3/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}']['delete'].parameters[3].schema"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegistryUserCreated:
        """
        Batch create users

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2Fbatch/post/parameters/0/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/batch'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2Fbatch/post/parameters/1/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/batch'].post.parameters[1].schema"

          registry_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2Fbatch/post/parameters/2/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/batch'].post.parameters[2].schema"

          users: '#/components/schemas/RegistryBatchUsersCreateSerializer/properties/users'
              "$.components.schemas.RegistryBatchUsersCreateSerializer.properties.users"

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
            cast_to=RegistryUserCreated,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Refresh a secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D%2Frefresh_secret/post/parameters/0/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}/refresh_secret'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D%2Frefresh_secret/post/parameters/1/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}/refresh_secret'].post.parameters[1].schema"

          registry_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D%2Frefresh_secret/post/parameters/2/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}/refresh_secret'].post.parameters[2].schema"

          user_id: '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers%2F%7Buser_id%7D%2Frefresh_secret/post/parameters/3/schema'
              "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}/refresh_secret'].post.parameters[3].schema"

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
        return await self._post(
            f"/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}/refresh_secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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

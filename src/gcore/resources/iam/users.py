# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
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
from ...types.iam import user_list_params, user_invite_params, user_update_params
from ...pagination import SyncOffsetPageIam, AsyncOffsetPageIam
from ..._base_client import AsyncPaginator, make_request_options
from ...types.iam.user import User
from ...types.iam.user_invite import UserInvite
from ...types.iam.user_update import UserUpdate
from ...types.iam.user_detailed import UserDetailed

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

    def update(
        self,
        user_id: int,
        *,
        auth_types: List[Literal["password", "sso", "github", "google-oauth2"]] | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        groups: Iterable[user_update_params.Group] | NotGiven = NOT_GIVEN,
        lang: Literal["de", "en", "ru", "zh", "az"] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        phone: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserUpdate:
        """This method updates user's details.

        Args:
          auth_types: System field.

        List of auth types available for the account.

          company: User's company.

          email: User's email address.

          groups:
              User's group in the current account. IAM supports 5 groups:

              - Users
              - Administrators
              - Engineers
              - Purge and Prefetch only (API)
              - Purge and Prefetch only (API+Web)

          lang: User's language. Defines language of the control panel and email messages.

          name: User's name.

          phone: User's phone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/iam/users/{user_id}",
            body=maybe_transform(
                {
                    "auth_types": auth_types,
                    "company": company,
                    "email": email,
                    "groups": groups,
                    "lang": lang,
                    "name": name,
                    "phone": phone,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUpdate,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPageIam[User]:
        """Get a list of users.

        Pass a value for the `limit` parameter in your request if
        you want retrieve a paginated result. Otherwise API returns a list with all
        users without pagination.

        Args:
          limit: The maximum number of items.

          offset: Offset relative to the beginning of list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/iam/users",
            page=SyncOffsetPageIam[User],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=User,
        )

    def delete(
        self,
        user_id: int,
        *,
        client_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Revokes user's access to the specified account.

        If the specified user doesn't
        have access to multiple accounts, the user is deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/iam/clients/{client_id}/client-users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        user_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserDetailed:
        """
        Get user's details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/iam/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDetailed,
        )

    def invite(
        self,
        *,
        client_id: int,
        email: str,
        user_role: user_invite_params.UserRole,
        lang: Literal["de", "en", "ru", "zh", "az"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserInvite:
        """Invite a user to the account.

        User will receive an email. The new user will
        receive an invitation email with a link to create an account password, the
        existing user will be notified about the invitation to the account.

        Args:
          client_id: ID of account.

          email: User email.

          lang: User's language. Defines language of the control panel and email messages.

          name: User name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/iam/clients/invite_user",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "email": email,
                    "user_role": user_role,
                    "lang": lang,
                    "name": name,
                },
                user_invite_params.UserInviteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserInvite,
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

    async def update(
        self,
        user_id: int,
        *,
        auth_types: List[Literal["password", "sso", "github", "google-oauth2"]] | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        groups: Iterable[user_update_params.Group] | NotGiven = NOT_GIVEN,
        lang: Literal["de", "en", "ru", "zh", "az"] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        phone: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserUpdate:
        """This method updates user's details.

        Args:
          auth_types: System field.

        List of auth types available for the account.

          company: User's company.

          email: User's email address.

          groups:
              User's group in the current account. IAM supports 5 groups:

              - Users
              - Administrators
              - Engineers
              - Purge and Prefetch only (API)
              - Purge and Prefetch only (API+Web)

          lang: User's language. Defines language of the control panel and email messages.

          name: User's name.

          phone: User's phone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/iam/users/{user_id}",
            body=await async_maybe_transform(
                {
                    "auth_types": auth_types,
                    "company": company,
                    "email": email,
                    "groups": groups,
                    "lang": lang,
                    "name": name,
                    "phone": phone,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUpdate,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[User, AsyncOffsetPageIam[User]]:
        """Get a list of users.

        Pass a value for the `limit` parameter in your request if
        you want retrieve a paginated result. Otherwise API returns a list with all
        users without pagination.

        Args:
          limit: The maximum number of items.

          offset: Offset relative to the beginning of list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/iam/users",
            page=AsyncOffsetPageIam[User],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=User,
        )

    async def delete(
        self,
        user_id: int,
        *,
        client_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Revokes user's access to the specified account.

        If the specified user doesn't
        have access to multiple accounts, the user is deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/iam/clients/{client_id}/client-users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        user_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserDetailed:
        """
        Get user's details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/iam/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDetailed,
        )

    async def invite(
        self,
        *,
        client_id: int,
        email: str,
        user_role: user_invite_params.UserRole,
        lang: Literal["de", "en", "ru", "zh", "az"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserInvite:
        """Invite a user to the account.

        User will receive an email. The new user will
        receive an invitation email with a link to create an account password, the
        existing user will be notified about the invitation to the account.

        Args:
          client_id: ID of account.

          email: User email.

          lang: User's language. Defines language of the control panel and email messages.

          name: User name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/iam/clients/invite_user",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "email": email,
                    "user_role": user_role,
                    "lang": lang,
                    "name": name,
                },
                user_invite_params.UserInviteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserInvite,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.get = to_raw_response_wrapper(
            users.get,
        )
        self.invite = to_raw_response_wrapper(
            users.invite,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.get = async_to_raw_response_wrapper(
            users.get,
        )
        self.invite = async_to_raw_response_wrapper(
            users.invite,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.get = to_streamed_response_wrapper(
            users.get,
        )
        self.invite = to_streamed_response_wrapper(
            users.invite,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            users.get,
        )
        self.invite = async_to_streamed_response_wrapper(
            users.invite,
        )

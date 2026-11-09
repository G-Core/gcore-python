# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal

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
from ...types.iam import UserLanguage, user_list_params, user_invite_params, user_update_params
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.iam.user import User
from ...types.iam.user_me import UserMe
from ...types.iam.auth_type import AuthType
from ...types.iam.user_invited import UserInvited
from ...types.iam.user_updated import UserUpdated
from ...types.iam.user_language import UserLanguage
from ...types.iam.user_group_param import UserGroupParam

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
        auth_types: List[AuthType] | Omit = omit,
        email: str | Omit = omit,
        lang: UserLanguage | Omit = omit,
        name: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserUpdated:
        """This method updates user's details.

        Args:
          auth_types: System field.

        List of auth types available for the account.

          email: User's email address.

          lang: User's language.

              Defines language of the control panel and email messages.

          name: User's name.

          phone: User's phone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/iam/users/{user_id}", user_id=user_id),
            body=maybe_transform(
                {
                    "auth_types": auth_types,
                    "email": email,
                    "lang": lang,
                    "name": name,
                    "phone": phone,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUpdated,
        )

    def list(
        self,
        *,
        auth_type: Literal["password", "sso", "google-oauth2", "github"] | Omit = omit,
        created_at: Dict[str, object] | Omit = omit,
        email: Dict[str, object] | Omit = omit,
        ids: Iterable[int] | Omit = omit,
        langs: List[Literal["az", "de", "en", "ru", "zh"]] | Omit = omit,
        limit: int | Omit = omit,
        name: Dict[str, object] | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[User]:
        """List the users of the caller's own client.

        Replaces the deprecated `GET /users`.

        Filtering follows the standard query filtering rules: `ids` and `langs` are
        repeated flat parameters (OR), e.g. `ids=1&ids=2`; `email`, `name` and
        `created_at` require a bracket operator, e.g. `email[contains]=example.com`.
        Sorting is `order_by=field.direction` (e.g. `order_by=created_at.desc`, the
        default); results are paginated with `limit`/`offset`.

        Args:
          auth_type: Filter by login method - a specific social provider, 'sso', or 'password'.

          created_at: Filter by creation time. Bracket operator required: `created_at[gte]`,
              `created_at[gt]`, `created_at[lt]` or `created_at[lte]` (ISO 8601), e.g.
              `created_at[gte]=2026-01-01T00:00:00Z&created_at[lt]=2026-02-01T00:00:00Z`.

          email: Filter by email, case-insensitive. Bracket operator required: `email[exact]`,
              `email[prefix]`, `email[contains]` or `email[suffix]`, e.g.
              `email[contains]=example.com`.

          ids: Filter by user id. Repeat the parameter for several values (OR), e.g.
              `ids=1&ids=2`.

          langs: Filter by interface language. Repeat the parameter for several values (OR), e.g.
              `langs=en&langs=ru`.

          limit: The maximum number of items.

          name: Filter by name, case-insensitive. Bracket operator required: `name[exact]`,
              `name[prefix]`, `name[contains]` or `name[suffix]`, e.g. `name[prefix]=Jo`.

          offset: Offset relative to the beginning of list.

          order_by: Sort order as `field.direction`, e.g. `order_by=created_at.desc`. Allowed
              fields: `created_at`, `email`, `name`. Defaults to `created_at.desc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/iam/v2/users",
            page=SyncOffsetPage[User],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "auth_type": auth_type,
                        "created_at": created_at,
                        "email": email,
                        "ids": ids,
                        "langs": langs,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/iam/clients/{client_id}/client-users/{user_id}", client_id=client_id, user_id=user_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """Get a single user of the caller's own client.

        Replaces the deprecated
        `GET /users/{userId}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/iam/v2/users/{user_id}", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserMe:
        """The authenticated user's own profile, including the clients they belong to."""
        return self._get(
            "/iam/v2/users/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserMe,
        )

    def invite(
        self,
        *,
        client_id: int,
        email: str,
        user_role: UserGroupParam,
        lang: UserLanguage | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserInvited:
        """Invite a user to the account.

        User will receive an email.

        The new user will receive an invitation email with a
        link to create an account password, the existing user will be notified about the
        invitation to the account.

        Args:
          client_id: ID of account.

          email: User email.

          lang: User's language.

              Defines language of the control panel and email messages.

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
            cast_to=UserInvited,
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
        auth_types: List[AuthType] | Omit = omit,
        email: str | Omit = omit,
        lang: UserLanguage | Omit = omit,
        name: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserUpdated:
        """This method updates user's details.

        Args:
          auth_types: System field.

        List of auth types available for the account.

          email: User's email address.

          lang: User's language.

              Defines language of the control panel and email messages.

          name: User's name.

          phone: User's phone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/iam/users/{user_id}", user_id=user_id),
            body=await async_maybe_transform(
                {
                    "auth_types": auth_types,
                    "email": email,
                    "lang": lang,
                    "name": name,
                    "phone": phone,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUpdated,
        )

    def list(
        self,
        *,
        auth_type: Literal["password", "sso", "google-oauth2", "github"] | Omit = omit,
        created_at: Dict[str, object] | Omit = omit,
        email: Dict[str, object] | Omit = omit,
        ids: Iterable[int] | Omit = omit,
        langs: List[Literal["az", "de", "en", "ru", "zh"]] | Omit = omit,
        limit: int | Omit = omit,
        name: Dict[str, object] | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[User, AsyncOffsetPage[User]]:
        """List the users of the caller's own client.

        Replaces the deprecated `GET /users`.

        Filtering follows the standard query filtering rules: `ids` and `langs` are
        repeated flat parameters (OR), e.g. `ids=1&ids=2`; `email`, `name` and
        `created_at` require a bracket operator, e.g. `email[contains]=example.com`.
        Sorting is `order_by=field.direction` (e.g. `order_by=created_at.desc`, the
        default); results are paginated with `limit`/`offset`.

        Args:
          auth_type: Filter by login method - a specific social provider, 'sso', or 'password'.

          created_at: Filter by creation time. Bracket operator required: `created_at[gte]`,
              `created_at[gt]`, `created_at[lt]` or `created_at[lte]` (ISO 8601), e.g.
              `created_at[gte]=2026-01-01T00:00:00Z&created_at[lt]=2026-02-01T00:00:00Z`.

          email: Filter by email, case-insensitive. Bracket operator required: `email[exact]`,
              `email[prefix]`, `email[contains]` or `email[suffix]`, e.g.
              `email[contains]=example.com`.

          ids: Filter by user id. Repeat the parameter for several values (OR), e.g.
              `ids=1&ids=2`.

          langs: Filter by interface language. Repeat the parameter for several values (OR), e.g.
              `langs=en&langs=ru`.

          limit: The maximum number of items.

          name: Filter by name, case-insensitive. Bracket operator required: `name[exact]`,
              `name[prefix]`, `name[contains]` or `name[suffix]`, e.g. `name[prefix]=Jo`.

          offset: Offset relative to the beginning of list.

          order_by: Sort order as `field.direction`, e.g. `order_by=created_at.desc`. Allowed
              fields: `created_at`, `email`, `name`. Defaults to `created_at.desc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/iam/v2/users",
            page=AsyncOffsetPage[User],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "auth_type": auth_type,
                        "created_at": created_at,
                        "email": email,
                        "ids": ids,
                        "langs": langs,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/iam/clients/{client_id}/client-users/{user_id}", client_id=client_id, user_id=user_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """Get a single user of the caller's own client.

        Replaces the deprecated
        `GET /users/{userId}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/iam/v2/users/{user_id}", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserMe:
        """The authenticated user's own profile, including the clients they belong to."""
        return await self._get(
            "/iam/v2/users/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserMe,
        )

    async def invite(
        self,
        *,
        client_id: int,
        email: str,
        user_role: UserGroupParam,
        lang: UserLanguage | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserInvited:
        """Invite a user to the account.

        User will receive an email.

        The new user will receive an invitation email with a
        link to create an account password, the existing user will be notified about the
        invitation to the account.

        Args:
          client_id: ID of account.

          email: User email.

          lang: User's language.

              Defines language of the control panel and email messages.

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
            cast_to=UserInvited,
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
        self.get_me = to_raw_response_wrapper(
            users.get_me,
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
        self.get_me = async_to_raw_response_wrapper(
            users.get_me,
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
        self.get_me = to_streamed_response_wrapper(
            users.get_me,
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
        self.get_me = async_to_streamed_response_wrapper(
            users.get_me,
        )
        self.invite = async_to_streamed_response_wrapper(
            users.invite,
        )

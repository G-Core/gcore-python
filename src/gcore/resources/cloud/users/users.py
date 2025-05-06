# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .role_assignments import (
    RoleAssignmentsResource,
    AsyncRoleAssignmentsResource,
    RoleAssignmentsResourceWithRawResponse,
    AsyncRoleAssignmentsResourceWithRawResponse,
    RoleAssignmentsResourceWithStreamingResponse,
    AsyncRoleAssignmentsResourceWithStreamingResponse,
)

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def role_assignments(self) -> RoleAssignmentsResource:
        return RoleAssignmentsResource(self._client)

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


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def role_assignments(self) -> AsyncRoleAssignmentsResource:
        return AsyncRoleAssignmentsResource(self._client)

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


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

    @cached_property
    def role_assignments(self) -> RoleAssignmentsResourceWithRawResponse:
        return RoleAssignmentsResourceWithRawResponse(self._users.role_assignments)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

    @cached_property
    def role_assignments(self) -> AsyncRoleAssignmentsResourceWithRawResponse:
        return AsyncRoleAssignmentsResourceWithRawResponse(self._users.role_assignments)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

    @cached_property
    def role_assignments(self) -> RoleAssignmentsResourceWithStreamingResponse:
        return RoleAssignmentsResourceWithStreamingResponse(self._users.role_assignments)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

    @cached_property
    def role_assignments(self) -> AsyncRoleAssignmentsResourceWithStreamingResponse:
        return AsyncRoleAssignmentsResourceWithStreamingResponse(self._users.role_assignments)

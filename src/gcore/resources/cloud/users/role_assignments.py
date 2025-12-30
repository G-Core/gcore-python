# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.users import (
    role_assignment_list_params,
    role_assignment_create_params,
    role_assignment_update_params,
)
from ....types.cloud.users.role_assignment import RoleAssignment
from ....types.cloud.users.role_assignment_updated_deleted import RoleAssignmentUpdatedDeleted

__all__ = ["RoleAssignmentsResource", "AsyncRoleAssignmentsResource"]


class RoleAssignmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoleAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return RoleAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoleAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return RoleAssignmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        role: Literal["ClientAdministrator", "InternalNetworkOnlyUser", "Observer", "ProjectAdministrator", "User"],
        user_id: int,
        client_id: Optional[int] | Omit = omit,
        project_id: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleAssignment:
        """
        Assign a role to an existing user in the specified scope.

        Args:
          role: User role

          user_id: User ID

          client_id: Client ID. Required if `project_id` is specified

          project_id: Project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cloud/v1/users/assignments",
            body=maybe_transform(
                {
                    "role": role,
                    "user_id": user_id,
                    "client_id": client_id,
                    "project_id": project_id,
                },
                role_assignment_create_params.RoleAssignmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleAssignment,
        )

    def update(
        self,
        assignment_id: int,
        *,
        role: Literal["ClientAdministrator", "InternalNetworkOnlyUser", "Observer", "ProjectAdministrator", "User"],
        user_id: int,
        client_id: Optional[int] | Omit = omit,
        project_id: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleAssignmentUpdatedDeleted:
        """
        Modify an existing role assignment for a user.

        Args:
          assignment_id: Assignment ID

          role: User role

          user_id: User ID

          client_id: Client ID. Required if `project_id` is specified

          project_id: Project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/cloud/v1/users/assignments/{assignment_id}",
            body=maybe_transform(
                {
                    "role": role,
                    "user_id": user_id,
                    "client_id": client_id,
                    "project_id": project_id,
                },
                role_assignment_update_params.RoleAssignmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleAssignmentUpdatedDeleted,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        project_id: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[RoleAssignment]:
        """
        List all role assignments in the specified scope.

        Args:
          limit: Limit the number of returned items. Falls back to default of 1000 if not
              specified. Limited by max limit value of 1000

          offset: Offset value is used to exclude the first set of records from the result

          project_id: Project ID

          user_id: User ID for filtering

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cloud/v1/users/assignments",
            page=SyncOffsetPage[RoleAssignment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "project_id": project_id,
                        "user_id": user_id,
                    },
                    role_assignment_list_params.RoleAssignmentListParams,
                ),
            ),
            model=RoleAssignment,
        )

    def delete(
        self,
        assignment_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleAssignmentUpdatedDeleted:
        """
        Delete an existing role assignment.

        Args:
          assignment_id: Assignment ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/cloud/v1/users/assignments/{assignment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleAssignmentUpdatedDeleted,
        )


class AsyncRoleAssignmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoleAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoleAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoleAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncRoleAssignmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        role: Literal["ClientAdministrator", "InternalNetworkOnlyUser", "Observer", "ProjectAdministrator", "User"],
        user_id: int,
        client_id: Optional[int] | Omit = omit,
        project_id: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleAssignment:
        """
        Assign a role to an existing user in the specified scope.

        Args:
          role: User role

          user_id: User ID

          client_id: Client ID. Required if `project_id` is specified

          project_id: Project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cloud/v1/users/assignments",
            body=await async_maybe_transform(
                {
                    "role": role,
                    "user_id": user_id,
                    "client_id": client_id,
                    "project_id": project_id,
                },
                role_assignment_create_params.RoleAssignmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleAssignment,
        )

    async def update(
        self,
        assignment_id: int,
        *,
        role: Literal["ClientAdministrator", "InternalNetworkOnlyUser", "Observer", "ProjectAdministrator", "User"],
        user_id: int,
        client_id: Optional[int] | Omit = omit,
        project_id: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleAssignmentUpdatedDeleted:
        """
        Modify an existing role assignment for a user.

        Args:
          assignment_id: Assignment ID

          role: User role

          user_id: User ID

          client_id: Client ID. Required if `project_id` is specified

          project_id: Project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/cloud/v1/users/assignments/{assignment_id}",
            body=await async_maybe_transform(
                {
                    "role": role,
                    "user_id": user_id,
                    "client_id": client_id,
                    "project_id": project_id,
                },
                role_assignment_update_params.RoleAssignmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleAssignmentUpdatedDeleted,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        project_id: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RoleAssignment, AsyncOffsetPage[RoleAssignment]]:
        """
        List all role assignments in the specified scope.

        Args:
          limit: Limit the number of returned items. Falls back to default of 1000 if not
              specified. Limited by max limit value of 1000

          offset: Offset value is used to exclude the first set of records from the result

          project_id: Project ID

          user_id: User ID for filtering

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cloud/v1/users/assignments",
            page=AsyncOffsetPage[RoleAssignment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "project_id": project_id,
                        "user_id": user_id,
                    },
                    role_assignment_list_params.RoleAssignmentListParams,
                ),
            ),
            model=RoleAssignment,
        )

    async def delete(
        self,
        assignment_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleAssignmentUpdatedDeleted:
        """
        Delete an existing role assignment.

        Args:
          assignment_id: Assignment ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/cloud/v1/users/assignments/{assignment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleAssignmentUpdatedDeleted,
        )


class RoleAssignmentsResourceWithRawResponse:
    def __init__(self, role_assignments: RoleAssignmentsResource) -> None:
        self._role_assignments = role_assignments

        self.create = to_raw_response_wrapper(
            role_assignments.create,
        )
        self.update = to_raw_response_wrapper(
            role_assignments.update,
        )
        self.list = to_raw_response_wrapper(
            role_assignments.list,
        )
        self.delete = to_raw_response_wrapper(
            role_assignments.delete,
        )


class AsyncRoleAssignmentsResourceWithRawResponse:
    def __init__(self, role_assignments: AsyncRoleAssignmentsResource) -> None:
        self._role_assignments = role_assignments

        self.create = async_to_raw_response_wrapper(
            role_assignments.create,
        )
        self.update = async_to_raw_response_wrapper(
            role_assignments.update,
        )
        self.list = async_to_raw_response_wrapper(
            role_assignments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            role_assignments.delete,
        )


class RoleAssignmentsResourceWithStreamingResponse:
    def __init__(self, role_assignments: RoleAssignmentsResource) -> None:
        self._role_assignments = role_assignments

        self.create = to_streamed_response_wrapper(
            role_assignments.create,
        )
        self.update = to_streamed_response_wrapper(
            role_assignments.update,
        )
        self.list = to_streamed_response_wrapper(
            role_assignments.list,
        )
        self.delete = to_streamed_response_wrapper(
            role_assignments.delete,
        )


class AsyncRoleAssignmentsResourceWithStreamingResponse:
    def __init__(self, role_assignments: AsyncRoleAssignmentsResource) -> None:
        self._role_assignments = role_assignments

        self.create = async_to_streamed_response_wrapper(
            role_assignments.create,
        )
        self.update = async_to_streamed_response_wrapper(
            role_assignments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            role_assignments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            role_assignments.delete,
        )

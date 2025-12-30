# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud.users import (
    RoleAssignment,
    RoleAssignmentUpdatedDeleted,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoleAssignments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        role_assignment = client.cloud.users.role_assignments.create(
            role="ClientAdministrator",
            user_id=777,
        )
        assert_matches_type(RoleAssignment, role_assignment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        role_assignment = client.cloud.users.role_assignments.create(
            role="ClientAdministrator",
            user_id=777,
            client_id=8,
            project_id=None,
        )
        assert_matches_type(RoleAssignment, role_assignment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.users.role_assignments.with_raw_response.create(
            role="ClientAdministrator",
            user_id=777,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role_assignment = response.parse()
        assert_matches_type(RoleAssignment, role_assignment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.users.role_assignments.with_streaming_response.create(
            role="ClientAdministrator",
            user_id=777,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role_assignment = response.parse()
            assert_matches_type(RoleAssignment, role_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        role_assignment = client.cloud.users.role_assignments.update(
            assignment_id=123,
            role="ClientAdministrator",
            user_id=777,
        )
        assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        role_assignment = client.cloud.users.role_assignments.update(
            assignment_id=123,
            role="ClientAdministrator",
            user_id=777,
            client_id=8,
            project_id=None,
        )
        assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.users.role_assignments.with_raw_response.update(
            assignment_id=123,
            role="ClientAdministrator",
            user_id=777,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role_assignment = response.parse()
        assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.users.role_assignments.with_streaming_response.update(
            assignment_id=123,
            role="ClientAdministrator",
            user_id=777,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role_assignment = response.parse()
            assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        role_assignment = client.cloud.users.role_assignments.list()
        assert_matches_type(SyncOffsetPage[RoleAssignment], role_assignment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        role_assignment = client.cloud.users.role_assignments.list(
            limit=100,
            offset=0,
            project_id=123,
            user_id=123,
        )
        assert_matches_type(SyncOffsetPage[RoleAssignment], role_assignment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.users.role_assignments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role_assignment = response.parse()
        assert_matches_type(SyncOffsetPage[RoleAssignment], role_assignment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.users.role_assignments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role_assignment = response.parse()
            assert_matches_type(SyncOffsetPage[RoleAssignment], role_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        role_assignment = client.cloud.users.role_assignments.delete(
            123,
        )
        assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.users.role_assignments.with_raw_response.delete(
            123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role_assignment = response.parse()
        assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.users.role_assignments.with_streaming_response.delete(
            123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role_assignment = response.parse()
            assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoleAssignments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        role_assignment = await async_client.cloud.users.role_assignments.create(
            role="ClientAdministrator",
            user_id=777,
        )
        assert_matches_type(RoleAssignment, role_assignment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        role_assignment = await async_client.cloud.users.role_assignments.create(
            role="ClientAdministrator",
            user_id=777,
            client_id=8,
            project_id=None,
        )
        assert_matches_type(RoleAssignment, role_assignment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.users.role_assignments.with_raw_response.create(
            role="ClientAdministrator",
            user_id=777,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role_assignment = await response.parse()
        assert_matches_type(RoleAssignment, role_assignment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.users.role_assignments.with_streaming_response.create(
            role="ClientAdministrator",
            user_id=777,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role_assignment = await response.parse()
            assert_matches_type(RoleAssignment, role_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        role_assignment = await async_client.cloud.users.role_assignments.update(
            assignment_id=123,
            role="ClientAdministrator",
            user_id=777,
        )
        assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        role_assignment = await async_client.cloud.users.role_assignments.update(
            assignment_id=123,
            role="ClientAdministrator",
            user_id=777,
            client_id=8,
            project_id=None,
        )
        assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.users.role_assignments.with_raw_response.update(
            assignment_id=123,
            role="ClientAdministrator",
            user_id=777,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role_assignment = await response.parse()
        assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.users.role_assignments.with_streaming_response.update(
            assignment_id=123,
            role="ClientAdministrator",
            user_id=777,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role_assignment = await response.parse()
            assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        role_assignment = await async_client.cloud.users.role_assignments.list()
        assert_matches_type(AsyncOffsetPage[RoleAssignment], role_assignment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        role_assignment = await async_client.cloud.users.role_assignments.list(
            limit=100,
            offset=0,
            project_id=123,
            user_id=123,
        )
        assert_matches_type(AsyncOffsetPage[RoleAssignment], role_assignment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.users.role_assignments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role_assignment = await response.parse()
        assert_matches_type(AsyncOffsetPage[RoleAssignment], role_assignment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.users.role_assignments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role_assignment = await response.parse()
            assert_matches_type(AsyncOffsetPage[RoleAssignment], role_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        role_assignment = await async_client.cloud.users.role_assignments.delete(
            123,
        )
        assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.users.role_assignments.with_raw_response.delete(
            123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role_assignment = await response.parse()
        assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.users.role_assignments.with_streaming_response.delete(
            123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role_assignment = await response.parse()
            assert_matches_type(RoleAssignmentUpdatedDeleted, role_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

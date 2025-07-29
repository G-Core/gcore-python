# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.iam import (
    User,
    UserInvite,
    UserUpdate,
    UserDetailed,
)
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        user = client.iam.users.update(
            user_id=0,
        )
        assert_matches_type(UserUpdate, user, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        user = client.iam.users.update(
            user_id=0,
            auth_types=["password"],
            company="company",
            email="dev@stainless.com",
            groups=[
                {
                    "id": 1,
                    "name": "Administrators",
                }
            ],
            lang="de",
            name="name",
            phone="phone",
        )
        assert_matches_type(UserUpdate, user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.iam.users.with_raw_response.update(
            user_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUpdate, user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.iam.users.with_streaming_response.update(
            user_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUpdate, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        user = client.iam.users.list()
        assert_matches_type(SyncOffsetPage[User], user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        user = client.iam.users.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[User], user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.iam.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncOffsetPage[User], user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.iam.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncOffsetPage[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        user = client.iam.users.delete(
            user_id=0,
            client_id=0,
        )
        assert user is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.iam.users.with_raw_response.delete(
            user_id=0,
            client_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.iam.users.with_streaming_response.delete(
            user_id=0,
            client_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        user = client.iam.users.get(
            0,
        )
        assert_matches_type(UserDetailed, user, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.iam.users.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserDetailed, user, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.iam.users.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserDetailed, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_invite(self, client: Gcore) -> None:
        user = client.iam.users.invite(
            client_id=0,
            email="dev@stainless.com",
            user_role={},
        )
        assert_matches_type(UserInvite, user, path=["response"])

    @parametrize
    def test_method_invite_with_all_params(self, client: Gcore) -> None:
        user = client.iam.users.invite(
            client_id=0,
            email="dev@stainless.com",
            user_role={
                "id": 1,
                "name": "Administrators",
            },
            lang="de",
            name="name",
        )
        assert_matches_type(UserInvite, user, path=["response"])

    @parametrize
    def test_raw_response_invite(self, client: Gcore) -> None:
        response = client.iam.users.with_raw_response.invite(
            client_id=0,
            email="dev@stainless.com",
            user_role={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserInvite, user, path=["response"])

    @parametrize
    def test_streaming_response_invite(self, client: Gcore) -> None:
        with client.iam.users.with_streaming_response.invite(
            client_id=0,
            email="dev@stainless.com",
            user_role={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserInvite, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        user = await async_client.iam.users.update(
            user_id=0,
        )
        assert_matches_type(UserUpdate, user, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        user = await async_client.iam.users.update(
            user_id=0,
            auth_types=["password"],
            company="company",
            email="dev@stainless.com",
            groups=[
                {
                    "id": 1,
                    "name": "Administrators",
                }
            ],
            lang="de",
            name="name",
            phone="phone",
        )
        assert_matches_type(UserUpdate, user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.iam.users.with_raw_response.update(
            user_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUpdate, user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.iam.users.with_streaming_response.update(
            user_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUpdate, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        user = await async_client.iam.users.list()
        assert_matches_type(AsyncOffsetPage[User], user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        user = await async_client.iam.users.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[User], user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.iam.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncOffsetPage[User], user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.iam.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncOffsetPage[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        user = await async_client.iam.users.delete(
            user_id=0,
            client_id=0,
        )
        assert user is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.iam.users.with_raw_response.delete(
            user_id=0,
            client_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.iam.users.with_streaming_response.delete(
            user_id=0,
            client_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        user = await async_client.iam.users.get(
            0,
        )
        assert_matches_type(UserDetailed, user, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.iam.users.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserDetailed, user, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.iam.users.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserDetailed, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_invite(self, async_client: AsyncGcore) -> None:
        user = await async_client.iam.users.invite(
            client_id=0,
            email="dev@stainless.com",
            user_role={},
        )
        assert_matches_type(UserInvite, user, path=["response"])

    @parametrize
    async def test_method_invite_with_all_params(self, async_client: AsyncGcore) -> None:
        user = await async_client.iam.users.invite(
            client_id=0,
            email="dev@stainless.com",
            user_role={
                "id": 1,
                "name": "Administrators",
            },
            lang="de",
            name="name",
        )
        assert_matches_type(UserInvite, user, path=["response"])

    @parametrize
    async def test_raw_response_invite(self, async_client: AsyncGcore) -> None:
        response = await async_client.iam.users.with_raw_response.invite(
            client_id=0,
            email="dev@stainless.com",
            user_role={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserInvite, user, path=["response"])

    @parametrize
    async def test_streaming_response_invite(self, async_client: AsyncGcore) -> None:
        async with async_client.iam.users.with_streaming_response.invite(
            client_id=0,
            email="dev@stainless.com",
            user_role={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserInvite, user, path=["response"])

        assert cast(Any, response.is_closed) is True

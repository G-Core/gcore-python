# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.registries import (
    RegistryUser,
    RegistryUserList,
    RegistryUserCreated,
    UserRefreshSecretResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        user = client.cloud.registries.users.create(
            registry_id=0,
            project_id=0,
            region_id=0,
            duration=14,
            name="user1",
        )
        assert_matches_type(RegistryUserCreated, user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        user = client.cloud.registries.users.create(
            registry_id=0,
            project_id=0,
            region_id=0,
            duration=14,
            name="user1",
            read_only=False,
            secret="secret",
        )
        assert_matches_type(RegistryUserCreated, user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.registries.users.with_raw_response.create(
            registry_id=0,
            project_id=0,
            region_id=0,
            duration=14,
            name="user1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(RegistryUserCreated, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.registries.users.with_streaming_response.create(
            registry_id=0,
            project_id=0,
            region_id=0,
            duration=14,
            name="user1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(RegistryUserCreated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        user = client.cloud.registries.users.update(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
            duration=14,
        )
        assert_matches_type(RegistryUser, user, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        user = client.cloud.registries.users.update(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
            duration=14,
            read_only=False,
        )
        assert_matches_type(RegistryUser, user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.registries.users.with_raw_response.update(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
            duration=14,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(RegistryUser, user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.registries.users.with_streaming_response.update(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
            duration=14,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(RegistryUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        user = client.cloud.registries.users.list(
            registry_id=0,
            project_id=0,
            region_id=0,
        )
        assert_matches_type(RegistryUserList, user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.registries.users.with_raw_response.list(
            registry_id=0,
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(RegistryUserList, user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.registries.users.with_streaming_response.list(
            registry_id=0,
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(RegistryUserList, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        user = client.cloud.registries.users.delete(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
        )
        assert user is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.registries.users.with_raw_response.delete(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.registries.users.with_streaming_response.delete(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_multiple(self, client: Gcore) -> None:
        user = client.cloud.registries.users.create_multiple(
            registry_id=0,
            project_id=0,
            region_id=0,
            users=[
                {
                    "duration": -1,
                    "name": "user1",
                }
            ],
        )
        assert_matches_type(RegistryUserCreated, user, path=["response"])

    @parametrize
    def test_raw_response_create_multiple(self, client: Gcore) -> None:
        response = client.cloud.registries.users.with_raw_response.create_multiple(
            registry_id=0,
            project_id=0,
            region_id=0,
            users=[
                {
                    "duration": -1,
                    "name": "user1",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(RegistryUserCreated, user, path=["response"])

    @parametrize
    def test_streaming_response_create_multiple(self, client: Gcore) -> None:
        with client.cloud.registries.users.with_streaming_response.create_multiple(
            registry_id=0,
            project_id=0,
            region_id=0,
            users=[
                {
                    "duration": -1,
                    "name": "user1",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(RegistryUserCreated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_refresh_secret(self, client: Gcore) -> None:
        user = client.cloud.registries.users.refresh_secret(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
        )
        assert_matches_type(UserRefreshSecretResponse, user, path=["response"])

    @parametrize
    def test_raw_response_refresh_secret(self, client: Gcore) -> None:
        response = client.cloud.registries.users.with_raw_response.refresh_secret(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRefreshSecretResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_refresh_secret(self, client: Gcore) -> None:
        with client.cloud.registries.users.with_streaming_response.refresh_secret(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRefreshSecretResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        user = await async_client.cloud.registries.users.create(
            registry_id=0,
            project_id=0,
            region_id=0,
            duration=14,
            name="user1",
        )
        assert_matches_type(RegistryUserCreated, user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        user = await async_client.cloud.registries.users.create(
            registry_id=0,
            project_id=0,
            region_id=0,
            duration=14,
            name="user1",
            read_only=False,
            secret="secret",
        )
        assert_matches_type(RegistryUserCreated, user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.users.with_raw_response.create(
            registry_id=0,
            project_id=0,
            region_id=0,
            duration=14,
            name="user1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(RegistryUserCreated, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.users.with_streaming_response.create(
            registry_id=0,
            project_id=0,
            region_id=0,
            duration=14,
            name="user1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(RegistryUserCreated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        user = await async_client.cloud.registries.users.update(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
            duration=14,
        )
        assert_matches_type(RegistryUser, user, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        user = await async_client.cloud.registries.users.update(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
            duration=14,
            read_only=False,
        )
        assert_matches_type(RegistryUser, user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.users.with_raw_response.update(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
            duration=14,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(RegistryUser, user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.users.with_streaming_response.update(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
            duration=14,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(RegistryUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        user = await async_client.cloud.registries.users.list(
            registry_id=0,
            project_id=0,
            region_id=0,
        )
        assert_matches_type(RegistryUserList, user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.users.with_raw_response.list(
            registry_id=0,
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(RegistryUserList, user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.users.with_streaming_response.list(
            registry_id=0,
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(RegistryUserList, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        user = await async_client.cloud.registries.users.delete(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
        )
        assert user is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.users.with_raw_response.delete(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.users.with_streaming_response.delete(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_multiple(self, async_client: AsyncGcore) -> None:
        user = await async_client.cloud.registries.users.create_multiple(
            registry_id=0,
            project_id=0,
            region_id=0,
            users=[
                {
                    "duration": -1,
                    "name": "user1",
                }
            ],
        )
        assert_matches_type(RegistryUserCreated, user, path=["response"])

    @parametrize
    async def test_raw_response_create_multiple(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.users.with_raw_response.create_multiple(
            registry_id=0,
            project_id=0,
            region_id=0,
            users=[
                {
                    "duration": -1,
                    "name": "user1",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(RegistryUserCreated, user, path=["response"])

    @parametrize
    async def test_streaming_response_create_multiple(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.users.with_streaming_response.create_multiple(
            registry_id=0,
            project_id=0,
            region_id=0,
            users=[
                {
                    "duration": -1,
                    "name": "user1",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(RegistryUserCreated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_refresh_secret(self, async_client: AsyncGcore) -> None:
        user = await async_client.cloud.registries.users.refresh_secret(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
        )
        assert_matches_type(UserRefreshSecretResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_refresh_secret(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.users.with_raw_response.refresh_secret(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRefreshSecretResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_refresh_secret(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.users.with_streaming_response.refresh_secret(
            user_id=0,
            project_id=0,
            region_id=0,
            registry_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRefreshSecretResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

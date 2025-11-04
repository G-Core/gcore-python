# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.databases.postgres.clusters import PostgresUserCredentials

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        user_credential = client.cloud.databases.postgres.clusters.user_credentials.get(
            username="username",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )
        assert_matches_type(PostgresUserCredentials, user_credential, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.databases.postgres.clusters.user_credentials.with_raw_response.get(
            username="username",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_credential = response.parse()
        assert_matches_type(PostgresUserCredentials, user_credential, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.databases.postgres.clusters.user_credentials.with_streaming_response.get(
            username="username",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_credential = response.parse()
            assert_matches_type(PostgresUserCredentials, user_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.databases.postgres.clusters.user_credentials.with_raw_response.get(
                username="username",
                project_id=0,
                region_id=0,
                cluster_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.cloud.databases.postgres.clusters.user_credentials.with_raw_response.get(
                username="",
                project_id=0,
                region_id=0,
                cluster_name="cluster_name",
            )

    @parametrize
    def test_method_regenerate(self, client: Gcore) -> None:
        user_credential = client.cloud.databases.postgres.clusters.user_credentials.regenerate(
            username="username",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )
        assert_matches_type(PostgresUserCredentials, user_credential, path=["response"])

    @parametrize
    def test_raw_response_regenerate(self, client: Gcore) -> None:
        response = client.cloud.databases.postgres.clusters.user_credentials.with_raw_response.regenerate(
            username="username",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_credential = response.parse()
        assert_matches_type(PostgresUserCredentials, user_credential, path=["response"])

    @parametrize
    def test_streaming_response_regenerate(self, client: Gcore) -> None:
        with client.cloud.databases.postgres.clusters.user_credentials.with_streaming_response.regenerate(
            username="username",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_credential = response.parse()
            assert_matches_type(PostgresUserCredentials, user_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_regenerate(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.databases.postgres.clusters.user_credentials.with_raw_response.regenerate(
                username="username",
                project_id=0,
                region_id=0,
                cluster_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.cloud.databases.postgres.clusters.user_credentials.with_raw_response.regenerate(
                username="",
                project_id=0,
                region_id=0,
                cluster_name="cluster_name",
            )


class TestAsyncUserCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        user_credential = await async_client.cloud.databases.postgres.clusters.user_credentials.get(
            username="username",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )
        assert_matches_type(PostgresUserCredentials, user_credential, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.databases.postgres.clusters.user_credentials.with_raw_response.get(
            username="username",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_credential = await response.parse()
        assert_matches_type(PostgresUserCredentials, user_credential, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.databases.postgres.clusters.user_credentials.with_streaming_response.get(
            username="username",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_credential = await response.parse()
            assert_matches_type(PostgresUserCredentials, user_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.databases.postgres.clusters.user_credentials.with_raw_response.get(
                username="username",
                project_id=0,
                region_id=0,
                cluster_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.cloud.databases.postgres.clusters.user_credentials.with_raw_response.get(
                username="",
                project_id=0,
                region_id=0,
                cluster_name="cluster_name",
            )

    @parametrize
    async def test_method_regenerate(self, async_client: AsyncGcore) -> None:
        user_credential = await async_client.cloud.databases.postgres.clusters.user_credentials.regenerate(
            username="username",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )
        assert_matches_type(PostgresUserCredentials, user_credential, path=["response"])

    @parametrize
    async def test_raw_response_regenerate(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.databases.postgres.clusters.user_credentials.with_raw_response.regenerate(
            username="username",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_credential = await response.parse()
        assert_matches_type(PostgresUserCredentials, user_credential, path=["response"])

    @parametrize
    async def test_streaming_response_regenerate(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.databases.postgres.clusters.user_credentials.with_streaming_response.regenerate(
            username="username",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_credential = await response.parse()
            assert_matches_type(PostgresUserCredentials, user_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_regenerate(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.databases.postgres.clusters.user_credentials.with_raw_response.regenerate(
                username="username",
                project_id=0,
                region_id=0,
                cluster_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.cloud.databases.postgres.clusters.user_credentials.with_raw_response.regenerate(
                username="",
                project_id=0,
                region_id=0,
                cluster_name="cluster_name",
            )

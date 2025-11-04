# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.databases.postgres import PostgresConfiguration

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        configuration = client.cloud.databases.postgres.configurations.get(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(PostgresConfiguration, configuration, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.databases.postgres.configurations.with_raw_response.get(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(PostgresConfiguration, configuration, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.databases.postgres.configurations.with_streaming_response.get(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(PostgresConfiguration, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigurations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        configuration = await async_client.cloud.databases.postgres.configurations.get(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(PostgresConfiguration, configuration, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.databases.postgres.configurations.with_raw_response.get(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(PostgresConfiguration, configuration, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.databases.postgres.configurations.with_streaming_response.get(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(PostgresConfiguration, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

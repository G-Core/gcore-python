# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.databases.postgres import PgConfValidation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_validate(self, client: Gcore) -> None:
        custom_configuration = client.cloud.databases.postgres.custom_configurations.validate(
            project_id=0,
            region_id=0,
            pg_conf="\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
            version="15",
        )
        assert_matches_type(PgConfValidation, custom_configuration, path=["response"])

    @parametrize
    def test_raw_response_validate(self, client: Gcore) -> None:
        response = client.cloud.databases.postgres.custom_configurations.with_raw_response.validate(
            project_id=0,
            region_id=0,
            pg_conf="\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
            version="15",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_configuration = response.parse()
        assert_matches_type(PgConfValidation, custom_configuration, path=["response"])

    @parametrize
    def test_streaming_response_validate(self, client: Gcore) -> None:
        with client.cloud.databases.postgres.custom_configurations.with_streaming_response.validate(
            project_id=0,
            region_id=0,
            pg_conf="\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
            version="15",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_configuration = response.parse()
            assert_matches_type(PgConfValidation, custom_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomConfigurations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_validate(self, async_client: AsyncGcore) -> None:
        custom_configuration = await async_client.cloud.databases.postgres.custom_configurations.validate(
            project_id=0,
            region_id=0,
            pg_conf="\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
            version="15",
        )
        assert_matches_type(PgConfValidation, custom_configuration, path=["response"])

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.databases.postgres.custom_configurations.with_raw_response.validate(
            project_id=0,
            region_id=0,
            pg_conf="\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
            version="15",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_configuration = await response.parse()
        assert_matches_type(PgConfValidation, custom_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.databases.postgres.custom_configurations.with_streaming_response.validate(
            project_id=0,
            region_id=0,
            pg_conf="\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
            version="15",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_configuration = await response.parse()
            assert_matches_type(PgConfValidation, custom_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

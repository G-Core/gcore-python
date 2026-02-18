# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.waap.domains.api_discovery import WaapTaskID

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOpenAPI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_scan(self, client: Gcore) -> None:
        openapi = client.waap.domains.api_discovery.openapi.scan(
            1,
        )
        assert_matches_type(WaapTaskID, openapi, path=["response"])

    @parametrize
    def test_raw_response_scan(self, client: Gcore) -> None:
        response = client.waap.domains.api_discovery.openapi.with_raw_response.scan(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openapi = response.parse()
        assert_matches_type(WaapTaskID, openapi, path=["response"])

    @parametrize
    def test_streaming_response_scan(self, client: Gcore) -> None:
        with client.waap.domains.api_discovery.openapi.with_streaming_response.scan(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openapi = response.parse()
            assert_matches_type(WaapTaskID, openapi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload(self, client: Gcore) -> None:
        openapi = client.waap.domains.api_discovery.openapi.upload(
            domain_id=1,
            file_data="file_data",
            file_name="file_name",
        )
        assert_matches_type(WaapTaskID, openapi, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Gcore) -> None:
        response = client.waap.domains.api_discovery.openapi.with_raw_response.upload(
            domain_id=1,
            file_data="file_data",
            file_name="file_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openapi = response.parse()
        assert_matches_type(WaapTaskID, openapi, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Gcore) -> None:
        with client.waap.domains.api_discovery.openapi.with_streaming_response.upload(
            domain_id=1,
            file_data="file_data",
            file_name="file_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openapi = response.parse()
            assert_matches_type(WaapTaskID, openapi, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOpenAPI:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_scan(self, async_client: AsyncGcore) -> None:
        openapi = await async_client.waap.domains.api_discovery.openapi.scan(
            1,
        )
        assert_matches_type(WaapTaskID, openapi, path=["response"])

    @parametrize
    async def test_raw_response_scan(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_discovery.openapi.with_raw_response.scan(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openapi = await response.parse()
        assert_matches_type(WaapTaskID, openapi, path=["response"])

    @parametrize
    async def test_streaming_response_scan(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_discovery.openapi.with_streaming_response.scan(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openapi = await response.parse()
            assert_matches_type(WaapTaskID, openapi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload(self, async_client: AsyncGcore) -> None:
        openapi = await async_client.waap.domains.api_discovery.openapi.upload(
            domain_id=1,
            file_data="file_data",
            file_name="file_name",
        )
        assert_matches_type(WaapTaskID, openapi, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_discovery.openapi.with_raw_response.upload(
            domain_id=1,
            file_data="file_data",
            file_name="file_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openapi = await response.parse()
        assert_matches_type(WaapTaskID, openapi, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_discovery.openapi.with_streaming_response.upload(
            domain_id=1,
            file_data="file_data",
            file_name="file_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openapi = await response.parse()
            assert_matches_type(WaapTaskID, openapi, path=["response"])

        assert cast(Any, response.is_closed) is True

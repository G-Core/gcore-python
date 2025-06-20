# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.waap import WaapGetAccountOverviewResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWaap:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_account_overview(self, client: Gcore) -> None:
        waap = client.waap.get_account_overview()
        assert_matches_type(WaapGetAccountOverviewResponse, waap, path=["response"])

    @parametrize
    def test_raw_response_get_account_overview(self, client: Gcore) -> None:
        response = client.waap.with_raw_response.get_account_overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waap = response.parse()
        assert_matches_type(WaapGetAccountOverviewResponse, waap, path=["response"])

    @parametrize
    def test_streaming_response_get_account_overview(self, client: Gcore) -> None:
        with client.waap.with_streaming_response.get_account_overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waap = response.parse()
            assert_matches_type(WaapGetAccountOverviewResponse, waap, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWaap:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_account_overview(self, async_client: AsyncGcore) -> None:
        waap = await async_client.waap.get_account_overview()
        assert_matches_type(WaapGetAccountOverviewResponse, waap, path=["response"])

    @parametrize
    async def test_raw_response_get_account_overview(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.with_raw_response.get_account_overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waap = await response.parse()
        assert_matches_type(WaapGetAccountOverviewResponse, waap, path=["response"])

    @parametrize
    async def test_streaming_response_get_account_overview(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.with_streaming_response.get_account_overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waap = await response.parse()
            assert_matches_type(WaapGetAccountOverviewResponse, waap, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.waap import WaapTag

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        tag = client.waap.tags.list()
        assert_matches_type(SyncOffsetPage[WaapTag], tag, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        tag = client.waap.tags.list(
            limit=0,
            name="xss",
            offset=0,
            ordering="name",
            readable_name="Cross-Site Scripting",
            reserved=True,
        )
        assert_matches_type(SyncOffsetPage[WaapTag], tag, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.waap.tags.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(SyncOffsetPage[WaapTag], tag, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.waap.tags.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(SyncOffsetPage[WaapTag], tag, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        tag = await async_client.waap.tags.list()
        assert_matches_type(AsyncOffsetPage[WaapTag], tag, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        tag = await async_client.waap.tags.list(
            limit=0,
            name="xss",
            offset=0,
            ordering="name",
            readable_name="Cross-Site Scripting",
            reserved=True,
        )
        assert_matches_type(AsyncOffsetPage[WaapTag], tag, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.tags.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapTag], tag, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.tags.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapTag], tag, path=["response"])

        assert cast(Any, response.is_closed) is True

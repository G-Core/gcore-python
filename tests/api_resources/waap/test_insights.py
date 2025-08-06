# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.waap import WaapInsightType

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInsights:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_types(self, client: Gcore) -> None:
        insight = client.waap.insights.list_types()
        assert_matches_type(SyncOffsetPage[WaapInsightType], insight, path=["response"])

    @parametrize
    def test_method_list_types_with_all_params(self, client: Gcore) -> None:
        insight = client.waap.insights.list_types(
            insight_frequency=1,
            limit=0,
            name="name",
            offset=0,
            ordering="name",
            slug="slug",
        )
        assert_matches_type(SyncOffsetPage[WaapInsightType], insight, path=["response"])

    @parametrize
    def test_raw_response_list_types(self, client: Gcore) -> None:
        response = client.waap.insights.with_raw_response.list_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(SyncOffsetPage[WaapInsightType], insight, path=["response"])

    @parametrize
    def test_streaming_response_list_types(self, client: Gcore) -> None:
        with client.waap.insights.with_streaming_response.list_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(SyncOffsetPage[WaapInsightType], insight, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInsights:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list_types(self, async_client: AsyncGcore) -> None:
        insight = await async_client.waap.insights.list_types()
        assert_matches_type(AsyncOffsetPage[WaapInsightType], insight, path=["response"])

    @parametrize
    async def test_method_list_types_with_all_params(self, async_client: AsyncGcore) -> None:
        insight = await async_client.waap.insights.list_types(
            insight_frequency=1,
            limit=0,
            name="name",
            offset=0,
            ordering="name",
            slug="slug",
        )
        assert_matches_type(AsyncOffsetPage[WaapInsightType], insight, path=["response"])

    @parametrize
    async def test_raw_response_list_types(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.insights.with_raw_response.list_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapInsightType], insight, path=["response"])

    @parametrize
    async def test_streaming_response_list_types(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.insights.with_streaming_response.list_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapInsightType], insight, path=["response"])

        assert cast(Any, response.is_closed) is True

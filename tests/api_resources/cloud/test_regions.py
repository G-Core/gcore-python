# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import Region

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        region = client.cloud.regions.list()
        assert_matches_type(SyncOffsetPage[Region], region, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        region = client.cloud.regions.list(
            limit=100,
            offset=0,
            order_by="created_at.desc",
            product="inference",
            show_volume_types=False,
        )
        assert_matches_type(SyncOffsetPage[Region], region, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.regions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = response.parse()
        assert_matches_type(SyncOffsetPage[Region], region, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.regions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = response.parse()
            assert_matches_type(SyncOffsetPage[Region], region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        region = client.cloud.regions.get(
            region_id=11,
        )
        assert_matches_type(Region, region, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Gcore) -> None:
        region = client.cloud.regions.get(
            region_id=11,
            show_volume_types=False,
        )
        assert_matches_type(Region, region, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.regions.with_raw_response.get(
            region_id=11,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = response.parse()
        assert_matches_type(Region, region, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.regions.with_streaming_response.get(
            region_id=11,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = response.parse()
            assert_matches_type(Region, region, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRegions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        region = await async_client.cloud.regions.list()
        assert_matches_type(AsyncOffsetPage[Region], region, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        region = await async_client.cloud.regions.list(
            limit=100,
            offset=0,
            order_by="created_at.desc",
            product="inference",
            show_volume_types=False,
        )
        assert_matches_type(AsyncOffsetPage[Region], region, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.regions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = await response.parse()
        assert_matches_type(AsyncOffsetPage[Region], region, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.regions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = await response.parse()
            assert_matches_type(AsyncOffsetPage[Region], region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        region = await async_client.cloud.regions.get(
            region_id=11,
        )
        assert_matches_type(Region, region, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncGcore) -> None:
        region = await async_client.cloud.regions.get(
            region_id=11,
            show_volume_types=False,
        )
        assert_matches_type(Region, region, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.regions.with_raw_response.get(
            region_id=11,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = await response.parse()
        assert_matches_type(Region, region, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.regions.with_streaming_response.get(
            region_id=11,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = await response.parse()
            assert_matches_type(Region, region, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.streaming import QualitySets

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQualitySets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        quality_set = client.streaming.quality_sets.list()
        assert_matches_type(QualitySets, quality_set, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.streaming.quality_sets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_set = response.parse()
        assert_matches_type(QualitySets, quality_set, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.streaming.quality_sets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_set = response.parse()
            assert_matches_type(QualitySets, quality_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_default(self, client: Gcore) -> None:
        quality_set = client.streaming.quality_sets.set_default()
        assert_matches_type(QualitySets, quality_set, path=["response"])

    @parametrize
    def test_method_set_default_with_all_params(self, client: Gcore) -> None:
        quality_set = client.streaming.quality_sets.set_default(
            live={"id": 0},
            vod={"id": 0},
        )
        assert_matches_type(QualitySets, quality_set, path=["response"])

    @parametrize
    def test_raw_response_set_default(self, client: Gcore) -> None:
        response = client.streaming.quality_sets.with_raw_response.set_default()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_set = response.parse()
        assert_matches_type(QualitySets, quality_set, path=["response"])

    @parametrize
    def test_streaming_response_set_default(self, client: Gcore) -> None:
        with client.streaming.quality_sets.with_streaming_response.set_default() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_set = response.parse()
            assert_matches_type(QualitySets, quality_set, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQualitySets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        quality_set = await async_client.streaming.quality_sets.list()
        assert_matches_type(QualitySets, quality_set, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.quality_sets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_set = await response.parse()
        assert_matches_type(QualitySets, quality_set, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.quality_sets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_set = await response.parse()
            assert_matches_type(QualitySets, quality_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_default(self, async_client: AsyncGcore) -> None:
        quality_set = await async_client.streaming.quality_sets.set_default()
        assert_matches_type(QualitySets, quality_set, path=["response"])

    @parametrize
    async def test_method_set_default_with_all_params(self, async_client: AsyncGcore) -> None:
        quality_set = await async_client.streaming.quality_sets.set_default(
            live={"id": 0},
            vod={"id": 0},
        )
        assert_matches_type(QualitySets, quality_set, path=["response"])

    @parametrize
    async def test_raw_response_set_default(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.quality_sets.with_raw_response.set_default()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_set = await response.parse()
        assert_matches_type(QualitySets, quality_set, path=["response"])

    @parametrize
    async def test_streaming_response_set_default(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.quality_sets.with_streaming_response.set_default() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_set = await response.parse()
            assert_matches_type(QualitySets, quality_set, path=["response"])

        assert cast(Any, response.is_closed) is True

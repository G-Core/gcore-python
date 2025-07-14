# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import InferenceRegionCapacityList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInference:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_capacity_by_region(self, client: Gcore) -> None:
        inference = client.cloud.inference.get_capacity_by_region()
        assert_matches_type(InferenceRegionCapacityList, inference, path=["response"])

    @parametrize
    def test_raw_response_get_capacity_by_region(self, client: Gcore) -> None:
        response = client.cloud.inference.with_raw_response.get_capacity_by_region()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = response.parse()
        assert_matches_type(InferenceRegionCapacityList, inference, path=["response"])

    @parametrize
    def test_streaming_response_get_capacity_by_region(self, client: Gcore) -> None:
        with client.cloud.inference.with_streaming_response.get_capacity_by_region() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = response.parse()
            assert_matches_type(InferenceRegionCapacityList, inference, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInference:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_capacity_by_region(self, async_client: AsyncGcore) -> None:
        inference = await async_client.cloud.inference.get_capacity_by_region()
        assert_matches_type(InferenceRegionCapacityList, inference, path=["response"])

    @parametrize
    async def test_raw_response_get_capacity_by_region(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.with_raw_response.get_capacity_by_region()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = await response.parse()
        assert_matches_type(InferenceRegionCapacityList, inference, path=["response"])

    @parametrize
    async def test_streaming_response_get_capacity_by_region(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.with_streaming_response.get_capacity_by_region() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = await response.parse()
            assert_matches_type(InferenceRegionCapacityList, inference, path=["response"])

        assert cast(Any, response.is_closed) is True

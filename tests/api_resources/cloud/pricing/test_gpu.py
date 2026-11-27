# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.pricing import GPUPriceCatalog

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGPU:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        gpu = client.cloud.pricing.gpu.list()
        assert_matches_type(GPUPriceCatalog, gpu, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.pricing.gpu.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu = response.parse()
        assert_matches_type(GPUPriceCatalog, gpu, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.pricing.gpu.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu = response.parse()
            assert_matches_type(GPUPriceCatalog, gpu, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGPU:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        gpu = await async_client.cloud.pricing.gpu.list()
        assert_matches_type(GPUPriceCatalog, gpu, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.pricing.gpu.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu = await response.parse()
        assert_matches_type(GPUPriceCatalog, gpu, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.pricing.gpu.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu = await response.parse()
            assert_matches_type(GPUPriceCatalog, gpu, path=["response"])

        assert cast(Any, response.is_closed) is True

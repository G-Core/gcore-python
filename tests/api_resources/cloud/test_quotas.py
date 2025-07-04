# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import QuotaGetAllResponse, QuotaGetGlobalResponse, QuotaGetByRegionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuotas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_all(self, client: Gcore) -> None:
        quota = client.cloud.quotas.get_all()
        assert_matches_type(QuotaGetAllResponse, quota, path=["response"])

    @parametrize
    def test_raw_response_get_all(self, client: Gcore) -> None:
        response = client.cloud.quotas.with_raw_response.get_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quota = response.parse()
        assert_matches_type(QuotaGetAllResponse, quota, path=["response"])

    @parametrize
    def test_streaming_response_get_all(self, client: Gcore) -> None:
        with client.cloud.quotas.with_streaming_response.get_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quota = response.parse()
            assert_matches_type(QuotaGetAllResponse, quota, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_region(self, client: Gcore) -> None:
        quota = client.cloud.quotas.get_by_region(
            client_id=3,
            region_id=1,
        )
        assert_matches_type(QuotaGetByRegionResponse, quota, path=["response"])

    @parametrize
    def test_raw_response_get_by_region(self, client: Gcore) -> None:
        response = client.cloud.quotas.with_raw_response.get_by_region(
            client_id=3,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quota = response.parse()
        assert_matches_type(QuotaGetByRegionResponse, quota, path=["response"])

    @parametrize
    def test_streaming_response_get_by_region(self, client: Gcore) -> None:
        with client.cloud.quotas.with_streaming_response.get_by_region(
            client_id=3,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quota = response.parse()
            assert_matches_type(QuotaGetByRegionResponse, quota, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_global(self, client: Gcore) -> None:
        quota = client.cloud.quotas.get_global(
            3,
        )
        assert_matches_type(QuotaGetGlobalResponse, quota, path=["response"])

    @parametrize
    def test_raw_response_get_global(self, client: Gcore) -> None:
        response = client.cloud.quotas.with_raw_response.get_global(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quota = response.parse()
        assert_matches_type(QuotaGetGlobalResponse, quota, path=["response"])

    @parametrize
    def test_streaming_response_get_global(self, client: Gcore) -> None:
        with client.cloud.quotas.with_streaming_response.get_global(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quota = response.parse()
            assert_matches_type(QuotaGetGlobalResponse, quota, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQuotas:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_all(self, async_client: AsyncGcore) -> None:
        quota = await async_client.cloud.quotas.get_all()
        assert_matches_type(QuotaGetAllResponse, quota, path=["response"])

    @parametrize
    async def test_raw_response_get_all(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.quotas.with_raw_response.get_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quota = await response.parse()
        assert_matches_type(QuotaGetAllResponse, quota, path=["response"])

    @parametrize
    async def test_streaming_response_get_all(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.quotas.with_streaming_response.get_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quota = await response.parse()
            assert_matches_type(QuotaGetAllResponse, quota, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_region(self, async_client: AsyncGcore) -> None:
        quota = await async_client.cloud.quotas.get_by_region(
            client_id=3,
            region_id=1,
        )
        assert_matches_type(QuotaGetByRegionResponse, quota, path=["response"])

    @parametrize
    async def test_raw_response_get_by_region(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.quotas.with_raw_response.get_by_region(
            client_id=3,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quota = await response.parse()
        assert_matches_type(QuotaGetByRegionResponse, quota, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_region(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.quotas.with_streaming_response.get_by_region(
            client_id=3,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quota = await response.parse()
            assert_matches_type(QuotaGetByRegionResponse, quota, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_global(self, async_client: AsyncGcore) -> None:
        quota = await async_client.cloud.quotas.get_global(
            3,
        )
        assert_matches_type(QuotaGetGlobalResponse, quota, path=["response"])

    @parametrize
    async def test_raw_response_get_global(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.quotas.with_raw_response.get_global(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quota = await response.parse()
        assert_matches_type(QuotaGetGlobalResponse, quota, path=["response"])

    @parametrize
    async def test_streaming_response_get_global(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.quotas.with_streaming_response.get_global(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quota = await response.parse()
            assert_matches_type(QuotaGetGlobalResponse, quota, path=["response"])

        assert cast(Any, response.is_closed) is True

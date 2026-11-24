# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud.baremetal import BaremetalFlavor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFlavors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        flavor = client.cloud.baremetal.flavors.list(
            project_id=1,
        )
        assert_matches_type(SyncOffsetPage[BaremetalFlavor], flavor, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        flavor = client.cloud.baremetal.flavors.list(
            project_id=1,
            architectures=["aarch64"],
            compatible_with_image_id="compatible_with_image_id",
            cpu_threads={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            limit=1,
            name={
                "contains": ["string"],
                "exact": ["string"],
                "prefix": ["string"],
                "suffix": ["string"],
            },
            offset=0,
            order_by="cpu_threads.asc",
            os_types=["linux"],
            ram_mib={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            region_ids=[0],
        )
        assert_matches_type(SyncOffsetPage[BaremetalFlavor], flavor, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.baremetal.flavors.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flavor = response.parse()
        assert_matches_type(SyncOffsetPage[BaremetalFlavor], flavor, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.baremetal.flavors.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flavor = response.parse()
            assert_matches_type(SyncOffsetPage[BaremetalFlavor], flavor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFlavors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        flavor = await async_client.cloud.baremetal.flavors.list(
            project_id=1,
        )
        assert_matches_type(AsyncOffsetPage[BaremetalFlavor], flavor, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        flavor = await async_client.cloud.baremetal.flavors.list(
            project_id=1,
            architectures=["aarch64"],
            compatible_with_image_id="compatible_with_image_id",
            cpu_threads={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            limit=1,
            name={
                "contains": ["string"],
                "exact": ["string"],
                "prefix": ["string"],
                "suffix": ["string"],
            },
            offset=0,
            order_by="cpu_threads.asc",
            os_types=["linux"],
            ram_mib={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            region_ids=[0],
        )
        assert_matches_type(AsyncOffsetPage[BaremetalFlavor], flavor, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.baremetal.flavors.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flavor = await response.parse()
        assert_matches_type(AsyncOffsetPage[BaremetalFlavor], flavor, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.baremetal.flavors.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flavor = await response.parse()
            assert_matches_type(AsyncOffsetPage[BaremetalFlavor], flavor, path=["response"])

        assert cast(Any, response.is_closed) is True

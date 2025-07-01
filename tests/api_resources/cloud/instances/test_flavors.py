# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.instances import InstanceFlavorList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFlavors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        flavor = client.cloud.instances.flavors.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(InstanceFlavorList, flavor, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        flavor = client.cloud.instances.flavors.list(
            project_id=0,
            region_id=0,
            disabled=True,
            exclude_linux=True,
            exclude_windows=True,
            include_prices=True,
        )
        assert_matches_type(InstanceFlavorList, flavor, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.instances.flavors.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flavor = response.parse()
        assert_matches_type(InstanceFlavorList, flavor, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.instances.flavors.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flavor = response.parse()
            assert_matches_type(InstanceFlavorList, flavor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFlavors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        flavor = await async_client.cloud.instances.flavors.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(InstanceFlavorList, flavor, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        flavor = await async_client.cloud.instances.flavors.list(
            project_id=0,
            region_id=0,
            disabled=True,
            exclude_linux=True,
            exclude_windows=True,
            include_prices=True,
        )
        assert_matches_type(InstanceFlavorList, flavor, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.flavors.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flavor = await response.parse()
        assert_matches_type(InstanceFlavorList, flavor, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.flavors.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flavor = await response.parse()
            assert_matches_type(InstanceFlavorList, flavor, path=["response"])

        assert cast(Any, response.is_closed) is True

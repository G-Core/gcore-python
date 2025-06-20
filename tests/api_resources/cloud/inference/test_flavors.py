# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud.inference import InferenceFlavor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFlavors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        flavor = client.cloud.inference.flavors.list()
        assert_matches_type(SyncOffsetPage[InferenceFlavor], flavor, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        flavor = client.cloud.inference.flavors.list(
            limit=1000,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[InferenceFlavor], flavor, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.inference.flavors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flavor = response.parse()
        assert_matches_type(SyncOffsetPage[InferenceFlavor], flavor, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.inference.flavors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flavor = response.parse()
            assert_matches_type(SyncOffsetPage[InferenceFlavor], flavor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        flavor = client.cloud.inference.flavors.get(
            "inference-16vcpu-232gib-1xh100-80gb",
        )
        assert_matches_type(InferenceFlavor, flavor, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.inference.flavors.with_raw_response.get(
            "inference-16vcpu-232gib-1xh100-80gb",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flavor = response.parse()
        assert_matches_type(InferenceFlavor, flavor, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.inference.flavors.with_streaming_response.get(
            "inference-16vcpu-232gib-1xh100-80gb",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flavor = response.parse()
            assert_matches_type(InferenceFlavor, flavor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flavor_name` but received ''"):
            client.cloud.inference.flavors.with_raw_response.get(
                "",
            )


class TestAsyncFlavors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        flavor = await async_client.cloud.inference.flavors.list()
        assert_matches_type(AsyncOffsetPage[InferenceFlavor], flavor, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        flavor = await async_client.cloud.inference.flavors.list(
            limit=1000,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[InferenceFlavor], flavor, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.flavors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flavor = await response.parse()
        assert_matches_type(AsyncOffsetPage[InferenceFlavor], flavor, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.flavors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flavor = await response.parse()
            assert_matches_type(AsyncOffsetPage[InferenceFlavor], flavor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        flavor = await async_client.cloud.inference.flavors.get(
            "inference-16vcpu-232gib-1xh100-80gb",
        )
        assert_matches_type(InferenceFlavor, flavor, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.flavors.with_raw_response.get(
            "inference-16vcpu-232gib-1xh100-80gb",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flavor = await response.parse()
        assert_matches_type(InferenceFlavor, flavor, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.flavors.with_streaming_response.get(
            "inference-16vcpu-232gib-1xh100-80gb",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flavor = await response.parse()
            assert_matches_type(InferenceFlavor, flavor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flavor_name` but received ''"):
            await async_client.cloud.inference.flavors.with_raw_response.get(
                "",
            )

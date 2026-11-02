# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.volumes import VolumeTypeList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        type = client.cloud.volumes.types.list()
        assert_matches_type(VolumeTypeList, type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        type = client.cloud.volumes.types.list(
            region_id=1,
        )
        assert_matches_type(VolumeTypeList, type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.volumes.types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = response.parse()
        assert_matches_type(VolumeTypeList, type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.volumes.types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = response.parse()
            assert_matches_type(VolumeTypeList, type, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTypes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        type = await async_client.cloud.volumes.types.list()
        assert_matches_type(VolumeTypeList, type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        type = await async_client.cloud.volumes.types.list(
            region_id=1,
        )
        assert_matches_type(VolumeTypeList, type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volumes.types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = await response.parse()
        assert_matches_type(VolumeTypeList, type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volumes.types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = await response.parse()
            assert_matches_type(VolumeTypeList, type, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.dns.pickers import PresetListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPresets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        preset = client.dns.pickers.presets.list()
        assert_matches_type(PresetListResponse, preset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.dns.pickers.presets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preset = response.parse()
        assert_matches_type(PresetListResponse, preset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.dns.pickers.presets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preset = response.parse()
            assert_matches_type(PresetListResponse, preset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPresets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        preset = await async_client.dns.pickers.presets.list()
        assert_matches_type(PresetListResponse, preset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.pickers.presets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preset = await response.parse()
        assert_matches_type(PresetListResponse, preset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.pickers.presets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preset = await response.parse()
            assert_matches_type(PresetListResponse, preset, path=["response"])

        assert cast(Any, response.is_closed) is True

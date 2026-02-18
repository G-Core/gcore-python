# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.waap.domains.api_discovery import WaapAPIDiscoverySettings

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        setting = client.waap.domains.api_discovery.settings.update(
            domain_id=1,
        )
        assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        setting = client.waap.domains.api_discovery.settings.update(
            domain_id=1,
            description_file_location="descriptionFileLocation",
            description_file_scan_enabled=True,
            description_file_scan_interval_hours=1,
            traffic_scan_enabled=True,
            traffic_scan_interval_hours=1,
        )
        assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.waap.domains.api_discovery.settings.with_raw_response.update(
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.waap.domains.api_discovery.settings.with_streaming_response.update(
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        setting = client.waap.domains.api_discovery.settings.get(
            1,
        )
        assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.waap.domains.api_discovery.settings.with_raw_response.get(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.waap.domains.api_discovery.settings.with_streaming_response.get(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        setting = await async_client.waap.domains.api_discovery.settings.update(
            domain_id=1,
        )
        assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        setting = await async_client.waap.domains.api_discovery.settings.update(
            domain_id=1,
            description_file_location="descriptionFileLocation",
            description_file_scan_enabled=True,
            description_file_scan_interval_hours=1,
            traffic_scan_enabled=True,
            traffic_scan_interval_hours=1,
        )
        assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_discovery.settings.with_raw_response.update(
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_discovery.settings.with_streaming_response.update(
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        setting = await async_client.waap.domains.api_discovery.settings.get(
            1,
        )
        assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_discovery.settings.with_raw_response.get(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_discovery.settings.with_streaming_response.get(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(WaapAPIDiscoverySettings, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

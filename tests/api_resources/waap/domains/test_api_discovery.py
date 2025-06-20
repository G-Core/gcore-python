# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.waap.domains import (
    APIDiscoveryGetSettingsResponse,
    APIDiscoveryScanOpenAPIResponse,
    APIDiscoveryUploadOpenAPIResponse,
    APIDiscoveryUpdateSettingsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIDiscovery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_settings(self, client: Gcore) -> None:
        api_discovery = client.waap.domains.api_discovery.get_settings(
            0,
        )
        assert_matches_type(APIDiscoveryGetSettingsResponse, api_discovery, path=["response"])

    @parametrize
    def test_raw_response_get_settings(self, client: Gcore) -> None:
        response = client.waap.domains.api_discovery.with_raw_response.get_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_discovery = response.parse()
        assert_matches_type(APIDiscoveryGetSettingsResponse, api_discovery, path=["response"])

    @parametrize
    def test_streaming_response_get_settings(self, client: Gcore) -> None:
        with client.waap.domains.api_discovery.with_streaming_response.get_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_discovery = response.parse()
            assert_matches_type(APIDiscoveryGetSettingsResponse, api_discovery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_scan_openapi(self, client: Gcore) -> None:
        api_discovery = client.waap.domains.api_discovery.scan_openapi(
            0,
        )
        assert_matches_type(APIDiscoveryScanOpenAPIResponse, api_discovery, path=["response"])

    @parametrize
    def test_raw_response_scan_openapi(self, client: Gcore) -> None:
        response = client.waap.domains.api_discovery.with_raw_response.scan_openapi(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_discovery = response.parse()
        assert_matches_type(APIDiscoveryScanOpenAPIResponse, api_discovery, path=["response"])

    @parametrize
    def test_streaming_response_scan_openapi(self, client: Gcore) -> None:
        with client.waap.domains.api_discovery.with_streaming_response.scan_openapi(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_discovery = response.parse()
            assert_matches_type(APIDiscoveryScanOpenAPIResponse, api_discovery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_settings(self, client: Gcore) -> None:
        api_discovery = client.waap.domains.api_discovery.update_settings(
            domain_id=0,
        )
        assert_matches_type(APIDiscoveryUpdateSettingsResponse, api_discovery, path=["response"])

    @parametrize
    def test_method_update_settings_with_all_params(self, client: Gcore) -> None:
        api_discovery = client.waap.domains.api_discovery.update_settings(
            domain_id=0,
            description_file_location="descriptionFileLocation",
            description_file_scan_enabled=True,
            description_file_scan_interval_hours=1,
            traffic_scan_enabled=True,
            traffic_scan_interval_hours=1,
        )
        assert_matches_type(APIDiscoveryUpdateSettingsResponse, api_discovery, path=["response"])

    @parametrize
    def test_raw_response_update_settings(self, client: Gcore) -> None:
        response = client.waap.domains.api_discovery.with_raw_response.update_settings(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_discovery = response.parse()
        assert_matches_type(APIDiscoveryUpdateSettingsResponse, api_discovery, path=["response"])

    @parametrize
    def test_streaming_response_update_settings(self, client: Gcore) -> None:
        with client.waap.domains.api_discovery.with_streaming_response.update_settings(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_discovery = response.parse()
            assert_matches_type(APIDiscoveryUpdateSettingsResponse, api_discovery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_openapi(self, client: Gcore) -> None:
        api_discovery = client.waap.domains.api_discovery.upload_openapi(
            domain_id=0,
            file_data="file_data",
            file_name="file_name",
        )
        assert_matches_type(APIDiscoveryUploadOpenAPIResponse, api_discovery, path=["response"])

    @parametrize
    def test_raw_response_upload_openapi(self, client: Gcore) -> None:
        response = client.waap.domains.api_discovery.with_raw_response.upload_openapi(
            domain_id=0,
            file_data="file_data",
            file_name="file_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_discovery = response.parse()
        assert_matches_type(APIDiscoveryUploadOpenAPIResponse, api_discovery, path=["response"])

    @parametrize
    def test_streaming_response_upload_openapi(self, client: Gcore) -> None:
        with client.waap.domains.api_discovery.with_streaming_response.upload_openapi(
            domain_id=0,
            file_data="file_data",
            file_name="file_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_discovery = response.parse()
            assert_matches_type(APIDiscoveryUploadOpenAPIResponse, api_discovery, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIDiscovery:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_settings(self, async_client: AsyncGcore) -> None:
        api_discovery = await async_client.waap.domains.api_discovery.get_settings(
            0,
        )
        assert_matches_type(APIDiscoveryGetSettingsResponse, api_discovery, path=["response"])

    @parametrize
    async def test_raw_response_get_settings(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_discovery.with_raw_response.get_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_discovery = await response.parse()
        assert_matches_type(APIDiscoveryGetSettingsResponse, api_discovery, path=["response"])

    @parametrize
    async def test_streaming_response_get_settings(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_discovery.with_streaming_response.get_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_discovery = await response.parse()
            assert_matches_type(APIDiscoveryGetSettingsResponse, api_discovery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_scan_openapi(self, async_client: AsyncGcore) -> None:
        api_discovery = await async_client.waap.domains.api_discovery.scan_openapi(
            0,
        )
        assert_matches_type(APIDiscoveryScanOpenAPIResponse, api_discovery, path=["response"])

    @parametrize
    async def test_raw_response_scan_openapi(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_discovery.with_raw_response.scan_openapi(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_discovery = await response.parse()
        assert_matches_type(APIDiscoveryScanOpenAPIResponse, api_discovery, path=["response"])

    @parametrize
    async def test_streaming_response_scan_openapi(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_discovery.with_streaming_response.scan_openapi(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_discovery = await response.parse()
            assert_matches_type(APIDiscoveryScanOpenAPIResponse, api_discovery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_settings(self, async_client: AsyncGcore) -> None:
        api_discovery = await async_client.waap.domains.api_discovery.update_settings(
            domain_id=0,
        )
        assert_matches_type(APIDiscoveryUpdateSettingsResponse, api_discovery, path=["response"])

    @parametrize
    async def test_method_update_settings_with_all_params(self, async_client: AsyncGcore) -> None:
        api_discovery = await async_client.waap.domains.api_discovery.update_settings(
            domain_id=0,
            description_file_location="descriptionFileLocation",
            description_file_scan_enabled=True,
            description_file_scan_interval_hours=1,
            traffic_scan_enabled=True,
            traffic_scan_interval_hours=1,
        )
        assert_matches_type(APIDiscoveryUpdateSettingsResponse, api_discovery, path=["response"])

    @parametrize
    async def test_raw_response_update_settings(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_discovery.with_raw_response.update_settings(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_discovery = await response.parse()
        assert_matches_type(APIDiscoveryUpdateSettingsResponse, api_discovery, path=["response"])

    @parametrize
    async def test_streaming_response_update_settings(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_discovery.with_streaming_response.update_settings(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_discovery = await response.parse()
            assert_matches_type(APIDiscoveryUpdateSettingsResponse, api_discovery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_openapi(self, async_client: AsyncGcore) -> None:
        api_discovery = await async_client.waap.domains.api_discovery.upload_openapi(
            domain_id=0,
            file_data="file_data",
            file_name="file_name",
        )
        assert_matches_type(APIDiscoveryUploadOpenAPIResponse, api_discovery, path=["response"])

    @parametrize
    async def test_raw_response_upload_openapi(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_discovery.with_raw_response.upload_openapi(
            domain_id=0,
            file_data="file_data",
            file_name="file_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_discovery = await response.parse()
        assert_matches_type(APIDiscoveryUploadOpenAPIResponse, api_discovery, path=["response"])

    @parametrize
    async def test_streaming_response_upload_openapi(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_discovery.with_streaming_response.upload_openapi(
            domain_id=0,
            file_data="file_data",
            file_name="file_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_discovery = await response.parse()
            assert_matches_type(APIDiscoveryUploadOpenAPIResponse, api_discovery, path=["response"])

        assert cast(Any, response.is_closed) is True

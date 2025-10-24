# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn import PublicIPList, PublicNetworkList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPRanges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        ip_range = client.cdn.ip_ranges.list()
        assert_matches_type(PublicNetworkList, ip_range, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        ip_range = client.cdn.ip_ranges.list(
            format="json",
            accept="application/json",
        )
        assert_matches_type(PublicNetworkList, ip_range, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.ip_ranges.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_range = response.parse()
        assert_matches_type(PublicNetworkList, ip_range, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.ip_ranges.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_range = response.parse()
            assert_matches_type(PublicNetworkList, ip_range, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_ips(self, client: Gcore) -> None:
        ip_range = client.cdn.ip_ranges.list_ips()
        assert_matches_type(PublicIPList, ip_range, path=["response"])

    @parametrize
    def test_method_list_ips_with_all_params(self, client: Gcore) -> None:
        ip_range = client.cdn.ip_ranges.list_ips(
            format="json",
            accept="application/json",
        )
        assert_matches_type(PublicIPList, ip_range, path=["response"])

    @parametrize
    def test_raw_response_list_ips(self, client: Gcore) -> None:
        response = client.cdn.ip_ranges.with_raw_response.list_ips()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_range = response.parse()
        assert_matches_type(PublicIPList, ip_range, path=["response"])

    @parametrize
    def test_streaming_response_list_ips(self, client: Gcore) -> None:
        with client.cdn.ip_ranges.with_streaming_response.list_ips() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_range = response.parse()
            assert_matches_type(PublicIPList, ip_range, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIPRanges:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        ip_range = await async_client.cdn.ip_ranges.list()
        assert_matches_type(PublicNetworkList, ip_range, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        ip_range = await async_client.cdn.ip_ranges.list(
            format="json",
            accept="application/json",
        )
        assert_matches_type(PublicNetworkList, ip_range, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.ip_ranges.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_range = await response.parse()
        assert_matches_type(PublicNetworkList, ip_range, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.ip_ranges.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_range = await response.parse()
            assert_matches_type(PublicNetworkList, ip_range, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_ips(self, async_client: AsyncGcore) -> None:
        ip_range = await async_client.cdn.ip_ranges.list_ips()
        assert_matches_type(PublicIPList, ip_range, path=["response"])

    @parametrize
    async def test_method_list_ips_with_all_params(self, async_client: AsyncGcore) -> None:
        ip_range = await async_client.cdn.ip_ranges.list_ips(
            format="json",
            accept="application/json",
        )
        assert_matches_type(PublicIPList, ip_range, path=["response"])

    @parametrize
    async def test_raw_response_list_ips(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.ip_ranges.with_raw_response.list_ips()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_range = await response.parse()
        assert_matches_type(PublicIPList, ip_range, path=["response"])

    @parametrize
    async def test_streaming_response_list_ips(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.ip_ranges.with_streaming_response.list_ips() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_range = await response.parse()
            assert_matches_type(PublicIPList, ip_range, path=["response"])

        assert cast(Any, response.is_closed) is True

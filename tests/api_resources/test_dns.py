# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.dns import DNSLookupResponse, DNSGetAccountOverviewResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDNS:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_account_overview(self, client: Gcore) -> None:
        dns = client.dns.get_account_overview()
        assert_matches_type(DNSGetAccountOverviewResponse, dns, path=["response"])

    @parametrize
    def test_raw_response_get_account_overview(self, client: Gcore) -> None:
        response = client.dns.with_raw_response.get_account_overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = response.parse()
        assert_matches_type(DNSGetAccountOverviewResponse, dns, path=["response"])

    @parametrize
    def test_streaming_response_get_account_overview(self, client: Gcore) -> None:
        with client.dns.with_streaming_response.get_account_overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = response.parse()
            assert_matches_type(DNSGetAccountOverviewResponse, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_lookup(self, client: Gcore) -> None:
        dns = client.dns.lookup()
        assert_matches_type(DNSLookupResponse, dns, path=["response"])

    @parametrize
    def test_method_lookup_with_all_params(self, client: Gcore) -> None:
        dns = client.dns.lookup(
            name="name",
            request_server="authoritative_dns",
        )
        assert_matches_type(DNSLookupResponse, dns, path=["response"])

    @parametrize
    def test_raw_response_lookup(self, client: Gcore) -> None:
        response = client.dns.with_raw_response.lookup()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = response.parse()
        assert_matches_type(DNSLookupResponse, dns, path=["response"])

    @parametrize
    def test_streaming_response_lookup(self, client: Gcore) -> None:
        with client.dns.with_streaming_response.lookup() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = response.parse()
            assert_matches_type(DNSLookupResponse, dns, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDNS:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_account_overview(self, async_client: AsyncGcore) -> None:
        dns = await async_client.dns.get_account_overview()
        assert_matches_type(DNSGetAccountOverviewResponse, dns, path=["response"])

    @parametrize
    async def test_raw_response_get_account_overview(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.with_raw_response.get_account_overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = await response.parse()
        assert_matches_type(DNSGetAccountOverviewResponse, dns, path=["response"])

    @parametrize
    async def test_streaming_response_get_account_overview(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.with_streaming_response.get_account_overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = await response.parse()
            assert_matches_type(DNSGetAccountOverviewResponse, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_lookup(self, async_client: AsyncGcore) -> None:
        dns = await async_client.dns.lookup()
        assert_matches_type(DNSLookupResponse, dns, path=["response"])

    @parametrize
    async def test_method_lookup_with_all_params(self, async_client: AsyncGcore) -> None:
        dns = await async_client.dns.lookup(
            name="name",
            request_server="authoritative_dns",
        )
        assert_matches_type(DNSLookupResponse, dns, path=["response"])

    @parametrize
    async def test_raw_response_lookup(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.with_raw_response.lookup()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = await response.parse()
        assert_matches_type(DNSLookupResponse, dns, path=["response"])

    @parametrize
    async def test_streaming_response_lookup(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.with_streaming_response.lookup() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = await response.parse()
            assert_matches_type(DNSLookupResponse, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

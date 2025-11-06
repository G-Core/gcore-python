# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.security import BgpAnnounceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBgpAnnounces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        bgp_announce = client.security.bgp_announces.list()
        assert_matches_type(BgpAnnounceListResponse, bgp_announce, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        bgp_announce = client.security.bgp_announces.list(
            announced=True,
            origin="STATIC",
            site="x",
        )
        assert_matches_type(BgpAnnounceListResponse, bgp_announce, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.security.bgp_announces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_announce = response.parse()
        assert_matches_type(BgpAnnounceListResponse, bgp_announce, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.security.bgp_announces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_announce = response.parse()
            assert_matches_type(BgpAnnounceListResponse, bgp_announce, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_toggle(self, client: Gcore) -> None:
        bgp_announce = client.security.bgp_announces.toggle(
            announce="192.9.9.1/32",
            enabled=True,
        )
        assert_matches_type(object, bgp_announce, path=["response"])

    @parametrize
    def test_method_toggle_with_all_params(self, client: Gcore) -> None:
        bgp_announce = client.security.bgp_announces.toggle(
            announce="192.9.9.1/32",
            enabled=True,
            client_id=0,
        )
        assert_matches_type(object, bgp_announce, path=["response"])

    @parametrize
    def test_raw_response_toggle(self, client: Gcore) -> None:
        response = client.security.bgp_announces.with_raw_response.toggle(
            announce="192.9.9.1/32",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_announce = response.parse()
        assert_matches_type(object, bgp_announce, path=["response"])

    @parametrize
    def test_streaming_response_toggle(self, client: Gcore) -> None:
        with client.security.bgp_announces.with_streaming_response.toggle(
            announce="192.9.9.1/32",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_announce = response.parse()
            assert_matches_type(object, bgp_announce, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBgpAnnounces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        bgp_announce = await async_client.security.bgp_announces.list()
        assert_matches_type(BgpAnnounceListResponse, bgp_announce, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        bgp_announce = await async_client.security.bgp_announces.list(
            announced=True,
            origin="STATIC",
            site="x",
        )
        assert_matches_type(BgpAnnounceListResponse, bgp_announce, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.security.bgp_announces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_announce = await response.parse()
        assert_matches_type(BgpAnnounceListResponse, bgp_announce, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.security.bgp_announces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_announce = await response.parse()
            assert_matches_type(BgpAnnounceListResponse, bgp_announce, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_toggle(self, async_client: AsyncGcore) -> None:
        bgp_announce = await async_client.security.bgp_announces.toggle(
            announce="192.9.9.1/32",
            enabled=True,
        )
        assert_matches_type(object, bgp_announce, path=["response"])

    @parametrize
    async def test_method_toggle_with_all_params(self, async_client: AsyncGcore) -> None:
        bgp_announce = await async_client.security.bgp_announces.toggle(
            announce="192.9.9.1/32",
            enabled=True,
            client_id=0,
        )
        assert_matches_type(object, bgp_announce, path=["response"])

    @parametrize
    async def test_raw_response_toggle(self, async_client: AsyncGcore) -> None:
        response = await async_client.security.bgp_announces.with_raw_response.toggle(
            announce="192.9.9.1/32",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_announce = await response.parse()
        assert_matches_type(object, bgp_announce, path=["response"])

    @parametrize
    async def test_streaming_response_toggle(self, async_client: AsyncGcore) -> None:
        async with async_client.security.bgp_announces.with_streaming_response.toggle(
            announce="192.9.9.1/32",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_announce = await response.parse()
            assert_matches_type(object, bgp_announce, path=["response"])

        assert cast(Any, response.is_closed) is True

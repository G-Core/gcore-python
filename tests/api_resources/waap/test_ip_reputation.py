# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.waap import (
    WaapLocalIPTagsRecord,
    WaapClearLocalTagsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPReputation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        ip_reputation = client.waap.ip_reputation.list(
            ip="ip",
        )
        assert_matches_type(SyncOffsetPage[WaapLocalIPTagsRecord], ip_reputation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        ip_reputation = client.waap.ip_reputation.list(
            ip="ip",
            limit=0,
            offset=0,
            ordering="date",
        )
        assert_matches_type(SyncOffsetPage[WaapLocalIPTagsRecord], ip_reputation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.waap.ip_reputation.with_raw_response.list(
            ip="ip",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_reputation = response.parse()
        assert_matches_type(SyncOffsetPage[WaapLocalIPTagsRecord], ip_reputation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.waap.ip_reputation.with_streaming_response.list(
            ip="ip",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_reputation = response.parse()
            assert_matches_type(SyncOffsetPage[WaapLocalIPTagsRecord], ip_reputation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_clear_local_tags(self, client: Gcore) -> None:
        ip_reputation = client.waap.ip_reputation.clear_local_tags(
            items=[
                {
                    "domain_id": 1,
                    "ip": "ip",
                }
            ],
        )
        assert_matches_type(WaapClearLocalTagsResponse, ip_reputation, path=["response"])

    @parametrize
    def test_raw_response_clear_local_tags(self, client: Gcore) -> None:
        response = client.waap.ip_reputation.with_raw_response.clear_local_tags(
            items=[
                {
                    "domain_id": 1,
                    "ip": "ip",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_reputation = response.parse()
        assert_matches_type(WaapClearLocalTagsResponse, ip_reputation, path=["response"])

    @parametrize
    def test_streaming_response_clear_local_tags(self, client: Gcore) -> None:
        with client.waap.ip_reputation.with_streaming_response.clear_local_tags(
            items=[
                {
                    "domain_id": 1,
                    "ip": "ip",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_reputation = response.parse()
            assert_matches_type(WaapClearLocalTagsResponse, ip_reputation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIPReputation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        ip_reputation = await async_client.waap.ip_reputation.list(
            ip="ip",
        )
        assert_matches_type(AsyncOffsetPage[WaapLocalIPTagsRecord], ip_reputation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        ip_reputation = await async_client.waap.ip_reputation.list(
            ip="ip",
            limit=0,
            offset=0,
            ordering="date",
        )
        assert_matches_type(AsyncOffsetPage[WaapLocalIPTagsRecord], ip_reputation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.ip_reputation.with_raw_response.list(
            ip="ip",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_reputation = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapLocalIPTagsRecord], ip_reputation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.ip_reputation.with_streaming_response.list(
            ip="ip",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_reputation = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapLocalIPTagsRecord], ip_reputation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_clear_local_tags(self, async_client: AsyncGcore) -> None:
        ip_reputation = await async_client.waap.ip_reputation.clear_local_tags(
            items=[
                {
                    "domain_id": 1,
                    "ip": "ip",
                }
            ],
        )
        assert_matches_type(WaapClearLocalTagsResponse, ip_reputation, path=["response"])

    @parametrize
    async def test_raw_response_clear_local_tags(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.ip_reputation.with_raw_response.clear_local_tags(
            items=[
                {
                    "domain_id": 1,
                    "ip": "ip",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_reputation = await response.parse()
        assert_matches_type(WaapClearLocalTagsResponse, ip_reputation, path=["response"])

    @parametrize
    async def test_streaming_response_clear_local_tags(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.ip_reputation.with_streaming_response.clear_local_tags(
            items=[
                {
                    "domain_id": 1,
                    "ip": "ip",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_reputation = await response.parse()
            assert_matches_type(WaapClearLocalTagsResponse, ip_reputation, path=["response"])

        assert cast(Any, response.is_closed) is True

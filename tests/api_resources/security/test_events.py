# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.security import ClientView

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        event = client.security.events.list()
        assert_matches_type(SyncOffsetPage[ClientView], event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        event = client.security.events.list(
            alert_type="ddos_alert",
            date_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_to=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            offset=0,
            ordering="attack_start_time",
            targeted_ip_addresses="targeted_ip_addresses",
        )
        assert_matches_type(SyncOffsetPage[ClientView], event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.security.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncOffsetPage[ClientView], event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.security.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncOffsetPage[ClientView], event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        event = await async_client.security.events.list()
        assert_matches_type(AsyncOffsetPage[ClientView], event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        event = await async_client.security.events.list(
            alert_type="ddos_alert",
            date_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_to=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            offset=0,
            ordering="attack_start_time",
            targeted_ip_addresses="targeted_ip_addresses",
        )
        assert_matches_type(AsyncOffsetPage[ClientView], event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.security.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(AsyncOffsetPage[ClientView], event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.security.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncOffsetPage[ClientView], event, path=["response"])

        assert cast(Any, response.is_closed) is True

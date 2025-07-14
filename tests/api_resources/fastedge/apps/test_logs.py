# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.pagination import SyncOffsetPageFastedgeAppLogs, AsyncOffsetPageFastedgeAppLogs
from gcore.types.fastedge.apps import Log

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        log = client.fastedge.apps.logs.list(
            id=0,
        )
        assert_matches_type(SyncOffsetPageFastedgeAppLogs[Log], log, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        log = client.fastedge.apps.logs.list(
            id=0,
            client_ip="192.168.1.1",
            edge="edge",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
            search="search",
            sort="desc",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPageFastedgeAppLogs[Log], log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.fastedge.apps.logs.with_raw_response.list(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(SyncOffsetPageFastedgeAppLogs[Log], log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.fastedge.apps.logs.with_streaming_response.list(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(SyncOffsetPageFastedgeAppLogs[Log], log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        log = await async_client.fastedge.apps.logs.list(
            id=0,
        )
        assert_matches_type(AsyncOffsetPageFastedgeAppLogs[Log], log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        log = await async_client.fastedge.apps.logs.list(
            id=0,
            client_ip="192.168.1.1",
            edge="edge",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
            search="search",
            sort="desc",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPageFastedgeAppLogs[Log], log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.apps.logs.with_raw_response.list(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(AsyncOffsetPageFastedgeAppLogs[Log], log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.apps.logs.with_streaming_response.list(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(AsyncOffsetPageFastedgeAppLogs[Log], log, path=["response"])

        assert cast(Any, response.is_closed) is True

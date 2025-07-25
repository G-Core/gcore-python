# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncPageStreaming, AsyncPageStreaming
from gcore.types.streaming import (
    Broadcast,
    BroadcastSpectatorsCount,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBroadcasts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        broadcast = client.streaming.broadcasts.create()
        assert broadcast is None

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        broadcast = client.streaming.broadcasts.create(
            broadcast={
                "name": "Broadcast",
                "ad_id": 1,
                "custom_iframe_url": "",
                "pending_message": "pending_message",
                "player_id": 14,
                "poster": "poster",
                "share_url": "",
                "show_dvr_after_finish": True,
                "status": "live",
                "stream_ids": [10],
            },
        )
        assert broadcast is None

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.streaming.broadcasts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert broadcast is None

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.streaming.broadcasts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert broadcast is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        broadcast = client.streaming.broadcasts.update(
            broadcast_id=0,
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        broadcast = client.streaming.broadcasts.update(
            broadcast_id=0,
            broadcast={
                "name": "Broadcast",
                "ad_id": 1,
                "custom_iframe_url": "",
                "pending_message": "pending_message",
                "player_id": 14,
                "poster": "poster",
                "share_url": "",
                "show_dvr_after_finish": True,
                "status": "live",
                "stream_ids": [10],
            },
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.streaming.broadcasts.with_raw_response.update(
            broadcast_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.streaming.broadcasts.with_streaming_response.update(
            broadcast_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        broadcast = client.streaming.broadcasts.list()
        assert_matches_type(SyncPageStreaming[Broadcast], broadcast, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        broadcast = client.streaming.broadcasts.list(
            page=0,
        )
        assert_matches_type(SyncPageStreaming[Broadcast], broadcast, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.streaming.broadcasts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(SyncPageStreaming[Broadcast], broadcast, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.streaming.broadcasts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(SyncPageStreaming[Broadcast], broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        broadcast = client.streaming.broadcasts.delete(
            0,
        )
        assert broadcast is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.streaming.broadcasts.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert broadcast is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.streaming.broadcasts.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert broadcast is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        broadcast = client.streaming.broadcasts.get(
            0,
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.streaming.broadcasts.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.streaming.broadcasts.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_spectators_count(self, client: Gcore) -> None:
        broadcast = client.streaming.broadcasts.get_spectators_count(
            0,
        )
        assert_matches_type(BroadcastSpectatorsCount, broadcast, path=["response"])

    @parametrize
    def test_raw_response_get_spectators_count(self, client: Gcore) -> None:
        response = client.streaming.broadcasts.with_raw_response.get_spectators_count(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastSpectatorsCount, broadcast, path=["response"])

    @parametrize
    def test_streaming_response_get_spectators_count(self, client: Gcore) -> None:
        with client.streaming.broadcasts.with_streaming_response.get_spectators_count(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastSpectatorsCount, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBroadcasts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        broadcast = await async_client.streaming.broadcasts.create()
        assert broadcast is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        broadcast = await async_client.streaming.broadcasts.create(
            broadcast={
                "name": "Broadcast",
                "ad_id": 1,
                "custom_iframe_url": "",
                "pending_message": "pending_message",
                "player_id": 14,
                "poster": "poster",
                "share_url": "",
                "show_dvr_after_finish": True,
                "status": "live",
                "stream_ids": [10],
            },
        )
        assert broadcast is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.broadcasts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert broadcast is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.broadcasts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert broadcast is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        broadcast = await async_client.streaming.broadcasts.update(
            broadcast_id=0,
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        broadcast = await async_client.streaming.broadcasts.update(
            broadcast_id=0,
            broadcast={
                "name": "Broadcast",
                "ad_id": 1,
                "custom_iframe_url": "",
                "pending_message": "pending_message",
                "player_id": 14,
                "poster": "poster",
                "share_url": "",
                "show_dvr_after_finish": True,
                "status": "live",
                "stream_ids": [10],
            },
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.broadcasts.with_raw_response.update(
            broadcast_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.broadcasts.with_streaming_response.update(
            broadcast_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        broadcast = await async_client.streaming.broadcasts.list()
        assert_matches_type(AsyncPageStreaming[Broadcast], broadcast, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        broadcast = await async_client.streaming.broadcasts.list(
            page=0,
        )
        assert_matches_type(AsyncPageStreaming[Broadcast], broadcast, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.broadcasts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(AsyncPageStreaming[Broadcast], broadcast, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.broadcasts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(AsyncPageStreaming[Broadcast], broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        broadcast = await async_client.streaming.broadcasts.delete(
            0,
        )
        assert broadcast is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.broadcasts.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert broadcast is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.broadcasts.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert broadcast is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        broadcast = await async_client.streaming.broadcasts.get(
            0,
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.broadcasts.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.broadcasts.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_spectators_count(self, async_client: AsyncGcore) -> None:
        broadcast = await async_client.streaming.broadcasts.get_spectators_count(
            0,
        )
        assert_matches_type(BroadcastSpectatorsCount, broadcast, path=["response"])

    @parametrize
    async def test_raw_response_get_spectators_count(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.broadcasts.with_raw_response.get_spectators_count(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastSpectatorsCount, broadcast, path=["response"])

    @parametrize
    async def test_streaming_response_get_spectators_count(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.broadcasts.with_streaming_response.get_spectators_count(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastSpectatorsCount, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncPageStreaming, AsyncPageStreaming
from gcore.types.streaming import Player

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlayers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        player = client.streaming.players.create()
        assert player is None

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        player = client.streaming.players.create(
            player={
                "name": "name",
                "id": 0,
                "autoplay": True,
                "bg_color": "bg_color",
                "client_id": 0,
                "custom_css": "custom_css",
                "design": "design",
                "disable_skin": True,
                "fg_color": "fg_color",
                "framework": "framework",
                "hover_color": "hover_color",
                "js_url": "js_url",
                "logo": "logo",
                "logo_position": "logo_position",
                "mute": True,
                "save_options_to_cookies": True,
                "show_sharing": True,
                "skin_is_url": "skin_is_url",
                "speed_control": True,
                "text_color": "text_color",
            },
        )
        assert player is None

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.streaming.players.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = response.parse()
        assert player is None

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.streaming.players.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = response.parse()
            assert player is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        player = client.streaming.players.update(
            player_id=0,
        )
        assert_matches_type(Player, player, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        player = client.streaming.players.update(
            player_id=0,
            player={
                "name": "name",
                "id": 0,
                "autoplay": True,
                "bg_color": "bg_color",
                "client_id": 0,
                "custom_css": "custom_css",
                "design": "design",
                "disable_skin": True,
                "fg_color": "fg_color",
                "framework": "framework",
                "hover_color": "hover_color",
                "js_url": "js_url",
                "logo": "logo",
                "logo_position": "logo_position",
                "mute": True,
                "save_options_to_cookies": True,
                "show_sharing": True,
                "skin_is_url": "skin_is_url",
                "speed_control": True,
                "text_color": "text_color",
            },
        )
        assert_matches_type(Player, player, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.streaming.players.with_raw_response.update(
            player_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = response.parse()
        assert_matches_type(Player, player, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.streaming.players.with_streaming_response.update(
            player_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = response.parse()
            assert_matches_type(Player, player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        player = client.streaming.players.list()
        assert_matches_type(SyncPageStreaming[Player], player, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        player = client.streaming.players.list(
            page=0,
        )
        assert_matches_type(SyncPageStreaming[Player], player, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.streaming.players.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = response.parse()
        assert_matches_type(SyncPageStreaming[Player], player, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.streaming.players.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = response.parse()
            assert_matches_type(SyncPageStreaming[Player], player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        player = client.streaming.players.delete(
            0,
        )
        assert player is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.streaming.players.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = response.parse()
        assert player is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.streaming.players.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = response.parse()
            assert player is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        player = client.streaming.players.get(
            0,
        )
        assert_matches_type(Player, player, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.streaming.players.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = response.parse()
        assert_matches_type(Player, player, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.streaming.players.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = response.parse()
            assert_matches_type(Player, player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_preview(self, client: Gcore) -> None:
        player = client.streaming.players.preview(
            0,
        )
        assert player is None

    @parametrize
    def test_raw_response_preview(self, client: Gcore) -> None:
        response = client.streaming.players.with_raw_response.preview(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = response.parse()
        assert player is None

    @parametrize
    def test_streaming_response_preview(self, client: Gcore) -> None:
        with client.streaming.players.with_streaming_response.preview(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = response.parse()
            assert player is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPlayers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        player = await async_client.streaming.players.create()
        assert player is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        player = await async_client.streaming.players.create(
            player={
                "name": "name",
                "id": 0,
                "autoplay": True,
                "bg_color": "bg_color",
                "client_id": 0,
                "custom_css": "custom_css",
                "design": "design",
                "disable_skin": True,
                "fg_color": "fg_color",
                "framework": "framework",
                "hover_color": "hover_color",
                "js_url": "js_url",
                "logo": "logo",
                "logo_position": "logo_position",
                "mute": True,
                "save_options_to_cookies": True,
                "show_sharing": True,
                "skin_is_url": "skin_is_url",
                "speed_control": True,
                "text_color": "text_color",
            },
        )
        assert player is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.players.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = await response.parse()
        assert player is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.players.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = await response.parse()
            assert player is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        player = await async_client.streaming.players.update(
            player_id=0,
        )
        assert_matches_type(Player, player, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        player = await async_client.streaming.players.update(
            player_id=0,
            player={
                "name": "name",
                "id": 0,
                "autoplay": True,
                "bg_color": "bg_color",
                "client_id": 0,
                "custom_css": "custom_css",
                "design": "design",
                "disable_skin": True,
                "fg_color": "fg_color",
                "framework": "framework",
                "hover_color": "hover_color",
                "js_url": "js_url",
                "logo": "logo",
                "logo_position": "logo_position",
                "mute": True,
                "save_options_to_cookies": True,
                "show_sharing": True,
                "skin_is_url": "skin_is_url",
                "speed_control": True,
                "text_color": "text_color",
            },
        )
        assert_matches_type(Player, player, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.players.with_raw_response.update(
            player_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = await response.parse()
        assert_matches_type(Player, player, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.players.with_streaming_response.update(
            player_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = await response.parse()
            assert_matches_type(Player, player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        player = await async_client.streaming.players.list()
        assert_matches_type(AsyncPageStreaming[Player], player, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        player = await async_client.streaming.players.list(
            page=0,
        )
        assert_matches_type(AsyncPageStreaming[Player], player, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.players.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = await response.parse()
        assert_matches_type(AsyncPageStreaming[Player], player, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.players.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = await response.parse()
            assert_matches_type(AsyncPageStreaming[Player], player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        player = await async_client.streaming.players.delete(
            0,
        )
        assert player is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.players.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = await response.parse()
        assert player is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.players.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = await response.parse()
            assert player is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        player = await async_client.streaming.players.get(
            0,
        )
        assert_matches_type(Player, player, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.players.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = await response.parse()
        assert_matches_type(Player, player, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.players.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = await response.parse()
            assert_matches_type(Player, player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_preview(self, async_client: AsyncGcore) -> None:
        player = await async_client.streaming.players.preview(
            0,
        )
        assert player is None

    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.players.with_raw_response.preview(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = await response.parse()
        assert player is None

    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.players.with_streaming_response.preview(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = await response.parse()
            assert player is None

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncPageStreaming, AsyncPageStreaming
from gcore.types.streaming import (
    Playlist,
    PlaylistCreate,
    PlaylistListVideosResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlaylists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        playlist = client.streaming.playlists.create()
        assert_matches_type(PlaylistCreate, playlist, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        playlist = client.streaming.playlists.create(
            active=True,
            ad_id=0,
            client_id=0,
            client_user_id=2876,
            countdown=True,
            hls_cmaf_url="hls_cmaf_url",
            hls_url="hls_url",
            iframe_url="iframe_url",
            loop=False,
            name="Playlist: Webinar 'Onboarding for new employees on working with the corporate portal'",
            player_id=0,
            playlist_type="live",
            start_time="2024-07-01T11:00:00Z",
            video_ids=[17800, 17801],
        )
        assert_matches_type(PlaylistCreate, playlist, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.streaming.playlists.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = response.parse()
        assert_matches_type(PlaylistCreate, playlist, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.streaming.playlists.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = response.parse()
            assert_matches_type(PlaylistCreate, playlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        playlist = client.streaming.playlists.update(
            playlist_id=0,
        )
        assert_matches_type(Playlist, playlist, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        playlist = client.streaming.playlists.update(
            playlist_id=0,
            active=True,
            ad_id=0,
            client_id=0,
            client_user_id=2876,
            countdown=True,
            hls_cmaf_url="hls_cmaf_url",
            hls_url="hls_url",
            iframe_url="iframe_url",
            loop=False,
            name="Playlist: Webinar 'Onboarding for new employees on working with the corporate portal'",
            player_id=0,
            playlist_type="live",
            start_time="2024-07-01T11:00:00Z",
            video_ids=[17800, 17801],
        )
        assert_matches_type(Playlist, playlist, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.streaming.playlists.with_raw_response.update(
            playlist_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = response.parse()
        assert_matches_type(Playlist, playlist, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.streaming.playlists.with_streaming_response.update(
            playlist_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = response.parse()
            assert_matches_type(Playlist, playlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        playlist = client.streaming.playlists.list()
        assert_matches_type(SyncPageStreaming[Playlist], playlist, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        playlist = client.streaming.playlists.list(
            page=0,
        )
        assert_matches_type(SyncPageStreaming[Playlist], playlist, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.streaming.playlists.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = response.parse()
        assert_matches_type(SyncPageStreaming[Playlist], playlist, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.streaming.playlists.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = response.parse()
            assert_matches_type(SyncPageStreaming[Playlist], playlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        playlist = client.streaming.playlists.delete(
            0,
        )
        assert playlist is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.streaming.playlists.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = response.parse()
        assert playlist is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.streaming.playlists.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = response.parse()
            assert playlist is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        playlist = client.streaming.playlists.get(
            0,
        )
        assert_matches_type(Playlist, playlist, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.streaming.playlists.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = response.parse()
        assert_matches_type(Playlist, playlist, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.streaming.playlists.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = response.parse()
            assert_matches_type(Playlist, playlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_videos(self, client: Gcore) -> None:
        playlist = client.streaming.playlists.list_videos(
            0,
        )
        assert_matches_type(PlaylistListVideosResponse, playlist, path=["response"])

    @parametrize
    def test_raw_response_list_videos(self, client: Gcore) -> None:
        response = client.streaming.playlists.with_raw_response.list_videos(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = response.parse()
        assert_matches_type(PlaylistListVideosResponse, playlist, path=["response"])

    @parametrize
    def test_streaming_response_list_videos(self, client: Gcore) -> None:
        with client.streaming.playlists.with_streaming_response.list_videos(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = response.parse()
            assert_matches_type(PlaylistListVideosResponse, playlist, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPlaylists:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        playlist = await async_client.streaming.playlists.create()
        assert_matches_type(PlaylistCreate, playlist, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        playlist = await async_client.streaming.playlists.create(
            active=True,
            ad_id=0,
            client_id=0,
            client_user_id=2876,
            countdown=True,
            hls_cmaf_url="hls_cmaf_url",
            hls_url="hls_url",
            iframe_url="iframe_url",
            loop=False,
            name="Playlist: Webinar 'Onboarding for new employees on working with the corporate portal'",
            player_id=0,
            playlist_type="live",
            start_time="2024-07-01T11:00:00Z",
            video_ids=[17800, 17801],
        )
        assert_matches_type(PlaylistCreate, playlist, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.playlists.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = await response.parse()
        assert_matches_type(PlaylistCreate, playlist, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.playlists.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = await response.parse()
            assert_matches_type(PlaylistCreate, playlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        playlist = await async_client.streaming.playlists.update(
            playlist_id=0,
        )
        assert_matches_type(Playlist, playlist, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        playlist = await async_client.streaming.playlists.update(
            playlist_id=0,
            active=True,
            ad_id=0,
            client_id=0,
            client_user_id=2876,
            countdown=True,
            hls_cmaf_url="hls_cmaf_url",
            hls_url="hls_url",
            iframe_url="iframe_url",
            loop=False,
            name="Playlist: Webinar 'Onboarding for new employees on working with the corporate portal'",
            player_id=0,
            playlist_type="live",
            start_time="2024-07-01T11:00:00Z",
            video_ids=[17800, 17801],
        )
        assert_matches_type(Playlist, playlist, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.playlists.with_raw_response.update(
            playlist_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = await response.parse()
        assert_matches_type(Playlist, playlist, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.playlists.with_streaming_response.update(
            playlist_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = await response.parse()
            assert_matches_type(Playlist, playlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        playlist = await async_client.streaming.playlists.list()
        assert_matches_type(AsyncPageStreaming[Playlist], playlist, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        playlist = await async_client.streaming.playlists.list(
            page=0,
        )
        assert_matches_type(AsyncPageStreaming[Playlist], playlist, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.playlists.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = await response.parse()
        assert_matches_type(AsyncPageStreaming[Playlist], playlist, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.playlists.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = await response.parse()
            assert_matches_type(AsyncPageStreaming[Playlist], playlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        playlist = await async_client.streaming.playlists.delete(
            0,
        )
        assert playlist is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.playlists.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = await response.parse()
        assert playlist is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.playlists.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = await response.parse()
            assert playlist is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        playlist = await async_client.streaming.playlists.get(
            0,
        )
        assert_matches_type(Playlist, playlist, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.playlists.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = await response.parse()
        assert_matches_type(Playlist, playlist, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.playlists.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = await response.parse()
            assert_matches_type(Playlist, playlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_videos(self, async_client: AsyncGcore) -> None:
        playlist = await async_client.streaming.playlists.list_videos(
            0,
        )
        assert_matches_type(PlaylistListVideosResponse, playlist, path=["response"])

    @parametrize
    async def test_raw_response_list_videos(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.playlists.with_raw_response.list_videos(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = await response.parse()
        assert_matches_type(PlaylistListVideosResponse, playlist, path=["response"])

    @parametrize
    async def test_streaming_response_list_videos(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.playlists.with_streaming_response.list_videos(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = await response.parse()
            assert_matches_type(PlaylistListVideosResponse, playlist, path=["response"])

        assert cast(Any, response.is_closed) is True

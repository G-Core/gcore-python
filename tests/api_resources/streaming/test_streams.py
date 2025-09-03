# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncPageStreaming, AsyncPageStreaming
from gcore.types.streaming import (
    Clip,
    Video,
    Stream,
    StreamListClipsResponse,
    StreamStartRecordingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStreams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        stream = client.streaming.streams.create(
            name="Live stream by user e4d0f942-f35d",
        )
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        stream = client.streaming.streams.create(
            name="Live stream by user e4d0f942-f35d",
            active=True,
            auto_record=False,
            broadcast_ids=[0],
            cdn_id=0,
            client_entity_data="client_entity_data",
            client_user_id=1001,
            dvr_duration=0,
            dvr_enabled=True,
            hls_mpegts_endlist_tag=True,
            html_overlay=False,
            projection="regular",
            pull=True,
            quality_set_id=0,
            record_type="origin",
            uri="srt://domain.com:5000/?streamid=12345",
        )
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.streaming.streams.with_raw_response.create(
            name="Live stream by user e4d0f942-f35d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.streaming.streams.with_streaming_response.create(
            name="Live stream by user e4d0f942-f35d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(Stream, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        stream = client.streaming.streams.update(
            stream_id=0,
        )
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        stream = client.streaming.streams.update(
            stream_id=0,
            stream={
                "name": "Live stream by user e4d0f942-f35d",
                "active": True,
                "auto_record": False,
                "broadcast_ids": [0],
                "cdn_id": 0,
                "client_entity_data": "client_entity_data",
                "client_user_id": 1001,
                "dvr_duration": 0,
                "dvr_enabled": True,
                "hls_mpegts_endlist_tag": True,
                "html_overlay": False,
                "projection": "regular",
                "pull": True,
                "quality_set_id": 0,
                "record_type": "origin",
                "uri": "srt://domain.com:5000/?streamid=12345",
            },
        )
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.streaming.streams.with_raw_response.update(
            stream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.streaming.streams.with_streaming_response.update(
            stream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(Stream, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        stream = client.streaming.streams.list()
        assert_matches_type(SyncPageStreaming[Stream], stream, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        stream = client.streaming.streams.list(
            page=0,
            with_broadcasts=0,
        )
        assert_matches_type(SyncPageStreaming[Stream], stream, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.streaming.streams.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(SyncPageStreaming[Stream], stream, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.streaming.streams.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(SyncPageStreaming[Stream], stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        stream = client.streaming.streams.delete(
            0,
        )
        assert stream is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.streaming.streams.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert stream is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.streaming.streams.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert stream is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_clear_dvr(self, client: Gcore) -> None:
        stream = client.streaming.streams.clear_dvr(
            0,
        )
        assert stream is None

    @parametrize
    def test_raw_response_clear_dvr(self, client: Gcore) -> None:
        response = client.streaming.streams.with_raw_response.clear_dvr(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert stream is None

    @parametrize
    def test_streaming_response_clear_dvr(self, client: Gcore) -> None:
        with client.streaming.streams.with_streaming_response.clear_dvr(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert stream is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    def test_method_create_clip(self, client: Gcore) -> None:
        stream = client.streaming.streams.create_clip(
            stream_id=0,
            duration=0,
        )
        assert_matches_type(Clip, stream, path=["response"])

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    def test_method_create_clip_with_all_params(self, client: Gcore) -> None:
        stream = client.streaming.streams.create_clip(
            stream_id=0,
            duration=0,
            expiration=0,
            start=0,
            vod_required=True,
        )
        assert_matches_type(Clip, stream, path=["response"])

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    def test_raw_response_create_clip(self, client: Gcore) -> None:
        response = client.streaming.streams.with_raw_response.create_clip(
            stream_id=0,
            duration=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(Clip, stream, path=["response"])

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    def test_streaming_response_create_clip(self, client: Gcore) -> None:
        with client.streaming.streams.with_streaming_response.create_clip(
            stream_id=0,
            duration=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(Clip, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        stream = client.streaming.streams.get(
            0,
        )
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.streaming.streams.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.streaming.streams.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(Stream, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    def test_method_list_clips(self, client: Gcore) -> None:
        stream = client.streaming.streams.list_clips(
            0,
        )
        assert_matches_type(StreamListClipsResponse, stream, path=["response"])

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    def test_raw_response_list_clips(self, client: Gcore) -> None:
        response = client.streaming.streams.with_raw_response.list_clips(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(StreamListClipsResponse, stream, path=["response"])

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    def test_streaming_response_list_clips(self, client: Gcore) -> None:
        with client.streaming.streams.with_streaming_response.list_clips(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(StreamListClipsResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_start_recording(self, client: Gcore) -> None:
        stream = client.streaming.streams.start_recording(
            0,
        )
        assert_matches_type(StreamStartRecordingResponse, stream, path=["response"])

    @parametrize
    def test_raw_response_start_recording(self, client: Gcore) -> None:
        response = client.streaming.streams.with_raw_response.start_recording(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(StreamStartRecordingResponse, stream, path=["response"])

    @parametrize
    def test_streaming_response_start_recording(self, client: Gcore) -> None:
        with client.streaming.streams.with_streaming_response.start_recording(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(StreamStartRecordingResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stop_recording(self, client: Gcore) -> None:
        stream = client.streaming.streams.stop_recording(
            0,
        )
        assert_matches_type(Video, stream, path=["response"])

    @parametrize
    def test_raw_response_stop_recording(self, client: Gcore) -> None:
        response = client.streaming.streams.with_raw_response.stop_recording(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(Video, stream, path=["response"])

    @parametrize
    def test_streaming_response_stop_recording(self, client: Gcore) -> None:
        with client.streaming.streams.with_streaming_response.stop_recording(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(Video, stream, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStreams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.create(
            name="Live stream by user e4d0f942-f35d",
        )
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.create(
            name="Live stream by user e4d0f942-f35d",
            active=True,
            auto_record=False,
            broadcast_ids=[0],
            cdn_id=0,
            client_entity_data="client_entity_data",
            client_user_id=1001,
            dvr_duration=0,
            dvr_enabled=True,
            hls_mpegts_endlist_tag=True,
            html_overlay=False,
            projection="regular",
            pull=True,
            quality_set_id=0,
            record_type="origin",
            uri="srt://domain.com:5000/?streamid=12345",
        )
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.with_raw_response.create(
            name="Live stream by user e4d0f942-f35d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.with_streaming_response.create(
            name="Live stream by user e4d0f942-f35d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(Stream, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.update(
            stream_id=0,
        )
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.update(
            stream_id=0,
            stream={
                "name": "Live stream by user e4d0f942-f35d",
                "active": True,
                "auto_record": False,
                "broadcast_ids": [0],
                "cdn_id": 0,
                "client_entity_data": "client_entity_data",
                "client_user_id": 1001,
                "dvr_duration": 0,
                "dvr_enabled": True,
                "hls_mpegts_endlist_tag": True,
                "html_overlay": False,
                "projection": "regular",
                "pull": True,
                "quality_set_id": 0,
                "record_type": "origin",
                "uri": "srt://domain.com:5000/?streamid=12345",
            },
        )
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.with_raw_response.update(
            stream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.with_streaming_response.update(
            stream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(Stream, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.list()
        assert_matches_type(AsyncPageStreaming[Stream], stream, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.list(
            page=0,
            with_broadcasts=0,
        )
        assert_matches_type(AsyncPageStreaming[Stream], stream, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(AsyncPageStreaming[Stream], stream, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(AsyncPageStreaming[Stream], stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.delete(
            0,
        )
        assert stream is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert stream is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert stream is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_clear_dvr(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.clear_dvr(
            0,
        )
        assert stream is None

    @parametrize
    async def test_raw_response_clear_dvr(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.with_raw_response.clear_dvr(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert stream is None

    @parametrize
    async def test_streaming_response_clear_dvr(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.with_streaming_response.clear_dvr(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert stream is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    async def test_method_create_clip(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.create_clip(
            stream_id=0,
            duration=0,
        )
        assert_matches_type(Clip, stream, path=["response"])

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    async def test_method_create_clip_with_all_params(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.create_clip(
            stream_id=0,
            duration=0,
            expiration=0,
            start=0,
            vod_required=True,
        )
        assert_matches_type(Clip, stream, path=["response"])

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    async def test_raw_response_create_clip(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.with_raw_response.create_clip(
            stream_id=0,
            duration=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(Clip, stream, path=["response"])

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    async def test_streaming_response_create_clip(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.with_streaming_response.create_clip(
            stream_id=0,
            duration=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(Clip, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.get(
            0,
        )
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(Stream, stream, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(Stream, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    async def test_method_list_clips(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.list_clips(
            0,
        )
        assert_matches_type(StreamListClipsResponse, stream, path=["response"])

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    async def test_raw_response_list_clips(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.with_raw_response.list_clips(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(StreamListClipsResponse, stream, path=["response"])

    @pytest.mark.skip(reason="OAS example mismatch with schema")
    @parametrize
    async def test_streaming_response_list_clips(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.with_streaming_response.list_clips(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(StreamListClipsResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_start_recording(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.start_recording(
            0,
        )
        assert_matches_type(StreamStartRecordingResponse, stream, path=["response"])

    @parametrize
    async def test_raw_response_start_recording(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.with_raw_response.start_recording(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(StreamStartRecordingResponse, stream, path=["response"])

    @parametrize
    async def test_streaming_response_start_recording(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.with_streaming_response.start_recording(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(StreamStartRecordingResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stop_recording(self, async_client: AsyncGcore) -> None:
        stream = await async_client.streaming.streams.stop_recording(
            0,
        )
        assert_matches_type(Video, stream, path=["response"])

    @parametrize
    async def test_raw_response_stop_recording(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.with_raw_response.stop_recording(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(Video, stream, path=["response"])

    @parametrize
    async def test_streaming_response_stop_recording(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.with_streaming_response.stop_recording(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(Video, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

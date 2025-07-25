# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncPageStreaming, AsyncPageStreaming
from gcore.types.streaming import (
    Video,
    VideoCreateResponse,
    DirectUploadParameters,
    VideoCreateMultipleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVideos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        video = client.streaming.videos.create()
        assert_matches_type(VideoCreateResponse, video, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        video = client.streaming.videos.create(
            video={
                "name": "IBC 2025 - International Broadcasting Convention",
                "auto_transcribe_audio_language": "auto",
                "auto_translate_subtitles_language": "disable",
                "client_user_id": 10,
                "clip_duration_seconds": 60,
                "clip_start_seconds": 137,
                "custom_iframe_url": "custom_iframe_url",
                "description": "We look forward to welcoming you at IBC2025, which will take place 12-15 September 2025.",
                "directory_id": 800,
                "origin_http_headers": "Authorization: Bearer ...",
                "origin_url": "https://www.googleapis.com/drive/v3/files/...?alt=media",
                "poster": "data:image/jpeg;base64,/9j/4AA...qf/2Q==",
                "priority": 0,
                "projection": "regular",
                "quality_set_id": 0,
                "remote_poster_url": "remote_poster_url",
                "remove_poster": True,
                "screenshot_id": -1,
                "share_url": "share_url",
                "source_bitrate_limit": True,
            },
        )
        assert_matches_type(VideoCreateResponse, video, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.streaming.videos.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(VideoCreateResponse, video, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.streaming.videos.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(VideoCreateResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        video = client.streaming.videos.update(
            video_id=0,
            name="IBC 2025 - International Broadcasting Convention",
        )
        assert_matches_type(Video, video, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        video = client.streaming.videos.update(
            video_id=0,
            name="IBC 2025 - International Broadcasting Convention",
            auto_transcribe_audio_language="auto",
            auto_translate_subtitles_language="disable",
            client_user_id=10,
            clip_duration_seconds=60,
            clip_start_seconds=137,
            custom_iframe_url="custom_iframe_url",
            description="We look forward to welcoming you at IBC2025, which will take place 12-15 September 2025.",
            directory_id=800,
            origin_http_headers="Authorization: Bearer ...",
            origin_url="https://www.googleapis.com/drive/v3/files/...?alt=media",
            poster="data:image/jpeg;base64,/9j/4AA...qf/2Q==",
            priority=0,
            projection="regular",
            quality_set_id=0,
            remote_poster_url="remote_poster_url",
            remove_poster=True,
            screenshot_id=-1,
            share_url="share_url",
            source_bitrate_limit=True,
        )
        assert_matches_type(Video, video, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.streaming.videos.with_raw_response.update(
            video_id=0,
            name="IBC 2025 - International Broadcasting Convention",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(Video, video, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.streaming.videos.with_streaming_response.update(
            video_id=0,
            name="IBC 2025 - International Broadcasting Convention",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(Video, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        video = client.streaming.videos.list()
        assert_matches_type(SyncPageStreaming[Video], video, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        video = client.streaming.videos.list(
            id="id",
            client_user_id=0,
            fields="fields",
            page=0,
            per_page=0,
            search="search",
            status="status",
            stream_id=0,
        )
        assert_matches_type(SyncPageStreaming[Video], video, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.streaming.videos.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(SyncPageStreaming[Video], video, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.streaming.videos.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(SyncPageStreaming[Video], video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        video = client.streaming.videos.delete(
            0,
        )
        assert video is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.streaming.videos.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert video is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.streaming.videos.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert video is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_multiple(self, client: Gcore) -> None:
        video = client.streaming.videos.create_multiple()
        assert_matches_type(VideoCreateMultipleResponse, video, path=["response"])

    @parametrize
    def test_method_create_multiple_with_all_params(self, client: Gcore) -> None:
        video = client.streaming.videos.create_multiple(
            fields="fields",
            videos=[
                {
                    "name": "IBC 2025 - International Broadcasting Convention",
                    "auto_transcribe_audio_language": "auto",
                    "auto_translate_subtitles_language": "disable",
                    "client_user_id": 10,
                    "clip_duration_seconds": 60,
                    "clip_start_seconds": 137,
                    "custom_iframe_url": "custom_iframe_url",
                    "description": "We look forward to welcoming you at IBC2025, which will take place 12-15 September 2025.",
                    "directory_id": 800,
                    "origin_http_headers": "Authorization: Bearer ...",
                    "origin_url": "https://www.googleapis.com/drive/v3/files/...?alt=media",
                    "poster": "data:image/jpeg;base64,/9j/4AA...qf/2Q==",
                    "priority": 0,
                    "projection": "regular",
                    "quality_set_id": 0,
                    "remote_poster_url": "remote_poster_url",
                    "remove_poster": True,
                    "screenshot_id": -1,
                    "share_url": "share_url",
                    "source_bitrate_limit": True,
                    "subtitles": [
                        {
                            "language": "eng",
                            "vtt": "WEBVTT\n\n1\n00:00:07.154 --> 00:00:12.736\nWe have 100 million registered users or active users who play at least once a week.\n\n2\n00:00:13.236 --> 00:00:20.198\nWe might have 80 or 100,000 playing on a given cluster.",
                            "name": "English (AI-generated)",
                        },
                        {
                            "language": "ger",
                            "vtt": "WEBVTT\n\n1\n00:00:07.154 --> 00:00:12.736\nWir haben 100 Millionen registrierte Benutzer oder aktive Benutzer, die mindestens einmal pro Woche spielen.\n\n2\n00:00:13.236 --> 00:00:20.198\nWir haben vielleicht 80 oder 100.000, die auf einem bestimmten Cluster spielen.",
                            "name": "German (AI-translated)",
                        },
                    ],
                }
            ],
        )
        assert_matches_type(VideoCreateMultipleResponse, video, path=["response"])

    @parametrize
    def test_raw_response_create_multiple(self, client: Gcore) -> None:
        response = client.streaming.videos.with_raw_response.create_multiple()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(VideoCreateMultipleResponse, video, path=["response"])

    @parametrize
    def test_streaming_response_create_multiple(self, client: Gcore) -> None:
        with client.streaming.videos.with_streaming_response.create_multiple() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(VideoCreateMultipleResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        video = client.streaming.videos.get(
            0,
        )
        assert_matches_type(Video, video, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.streaming.videos.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(Video, video, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.streaming.videos.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(Video, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_parameters_for_direct_upload(self, client: Gcore) -> None:
        video = client.streaming.videos.get_parameters_for_direct_upload(
            0,
        )
        assert_matches_type(DirectUploadParameters, video, path=["response"])

    @parametrize
    def test_raw_response_get_parameters_for_direct_upload(self, client: Gcore) -> None:
        response = client.streaming.videos.with_raw_response.get_parameters_for_direct_upload(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(DirectUploadParameters, video, path=["response"])

    @parametrize
    def test_streaming_response_get_parameters_for_direct_upload(self, client: Gcore) -> None:
        with client.streaming.videos.with_streaming_response.get_parameters_for_direct_upload(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(DirectUploadParameters, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_names(self, client: Gcore) -> None:
        video = client.streaming.videos.list_names()
        assert video is None

    @parametrize
    def test_method_list_names_with_all_params(self, client: Gcore) -> None:
        video = client.streaming.videos.list_names(
            ids=[0],
        )
        assert video is None

    @parametrize
    def test_raw_response_list_names(self, client: Gcore) -> None:
        response = client.streaming.videos.with_raw_response.list_names()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert video is None

    @parametrize
    def test_streaming_response_list_names(self, client: Gcore) -> None:
        with client.streaming.videos.with_streaming_response.list_names() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert video is None

        assert cast(Any, response.is_closed) is True


class TestAsyncVideos:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        video = await async_client.streaming.videos.create()
        assert_matches_type(VideoCreateResponse, video, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        video = await async_client.streaming.videos.create(
            video={
                "name": "IBC 2025 - International Broadcasting Convention",
                "auto_transcribe_audio_language": "auto",
                "auto_translate_subtitles_language": "disable",
                "client_user_id": 10,
                "clip_duration_seconds": 60,
                "clip_start_seconds": 137,
                "custom_iframe_url": "custom_iframe_url",
                "description": "We look forward to welcoming you at IBC2025, which will take place 12-15 September 2025.",
                "directory_id": 800,
                "origin_http_headers": "Authorization: Bearer ...",
                "origin_url": "https://www.googleapis.com/drive/v3/files/...?alt=media",
                "poster": "data:image/jpeg;base64,/9j/4AA...qf/2Q==",
                "priority": 0,
                "projection": "regular",
                "quality_set_id": 0,
                "remote_poster_url": "remote_poster_url",
                "remove_poster": True,
                "screenshot_id": -1,
                "share_url": "share_url",
                "source_bitrate_limit": True,
            },
        )
        assert_matches_type(VideoCreateResponse, video, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.videos.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(VideoCreateResponse, video, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.videos.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(VideoCreateResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        video = await async_client.streaming.videos.update(
            video_id=0,
            name="IBC 2025 - International Broadcasting Convention",
        )
        assert_matches_type(Video, video, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        video = await async_client.streaming.videos.update(
            video_id=0,
            name="IBC 2025 - International Broadcasting Convention",
            auto_transcribe_audio_language="auto",
            auto_translate_subtitles_language="disable",
            client_user_id=10,
            clip_duration_seconds=60,
            clip_start_seconds=137,
            custom_iframe_url="custom_iframe_url",
            description="We look forward to welcoming you at IBC2025, which will take place 12-15 September 2025.",
            directory_id=800,
            origin_http_headers="Authorization: Bearer ...",
            origin_url="https://www.googleapis.com/drive/v3/files/...?alt=media",
            poster="data:image/jpeg;base64,/9j/4AA...qf/2Q==",
            priority=0,
            projection="regular",
            quality_set_id=0,
            remote_poster_url="remote_poster_url",
            remove_poster=True,
            screenshot_id=-1,
            share_url="share_url",
            source_bitrate_limit=True,
        )
        assert_matches_type(Video, video, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.videos.with_raw_response.update(
            video_id=0,
            name="IBC 2025 - International Broadcasting Convention",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(Video, video, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.videos.with_streaming_response.update(
            video_id=0,
            name="IBC 2025 - International Broadcasting Convention",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(Video, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        video = await async_client.streaming.videos.list()
        assert_matches_type(AsyncPageStreaming[Video], video, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        video = await async_client.streaming.videos.list(
            id="id",
            client_user_id=0,
            fields="fields",
            page=0,
            per_page=0,
            search="search",
            status="status",
            stream_id=0,
        )
        assert_matches_type(AsyncPageStreaming[Video], video, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.videos.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(AsyncPageStreaming[Video], video, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.videos.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(AsyncPageStreaming[Video], video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        video = await async_client.streaming.videos.delete(
            0,
        )
        assert video is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.videos.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert video is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.videos.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert video is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_multiple(self, async_client: AsyncGcore) -> None:
        video = await async_client.streaming.videos.create_multiple()
        assert_matches_type(VideoCreateMultipleResponse, video, path=["response"])

    @parametrize
    async def test_method_create_multiple_with_all_params(self, async_client: AsyncGcore) -> None:
        video = await async_client.streaming.videos.create_multiple(
            fields="fields",
            videos=[
                {
                    "name": "IBC 2025 - International Broadcasting Convention",
                    "auto_transcribe_audio_language": "auto",
                    "auto_translate_subtitles_language": "disable",
                    "client_user_id": 10,
                    "clip_duration_seconds": 60,
                    "clip_start_seconds": 137,
                    "custom_iframe_url": "custom_iframe_url",
                    "description": "We look forward to welcoming you at IBC2025, which will take place 12-15 September 2025.",
                    "directory_id": 800,
                    "origin_http_headers": "Authorization: Bearer ...",
                    "origin_url": "https://www.googleapis.com/drive/v3/files/...?alt=media",
                    "poster": "data:image/jpeg;base64,/9j/4AA...qf/2Q==",
                    "priority": 0,
                    "projection": "regular",
                    "quality_set_id": 0,
                    "remote_poster_url": "remote_poster_url",
                    "remove_poster": True,
                    "screenshot_id": -1,
                    "share_url": "share_url",
                    "source_bitrate_limit": True,
                    "subtitles": [
                        {
                            "language": "eng",
                            "vtt": "WEBVTT\n\n1\n00:00:07.154 --> 00:00:12.736\nWe have 100 million registered users or active users who play at least once a week.\n\n2\n00:00:13.236 --> 00:00:20.198\nWe might have 80 or 100,000 playing on a given cluster.",
                            "name": "English (AI-generated)",
                        },
                        {
                            "language": "ger",
                            "vtt": "WEBVTT\n\n1\n00:00:07.154 --> 00:00:12.736\nWir haben 100 Millionen registrierte Benutzer oder aktive Benutzer, die mindestens einmal pro Woche spielen.\n\n2\n00:00:13.236 --> 00:00:20.198\nWir haben vielleicht 80 oder 100.000, die auf einem bestimmten Cluster spielen.",
                            "name": "German (AI-translated)",
                        },
                    ],
                }
            ],
        )
        assert_matches_type(VideoCreateMultipleResponse, video, path=["response"])

    @parametrize
    async def test_raw_response_create_multiple(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.videos.with_raw_response.create_multiple()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(VideoCreateMultipleResponse, video, path=["response"])

    @parametrize
    async def test_streaming_response_create_multiple(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.videos.with_streaming_response.create_multiple() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(VideoCreateMultipleResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        video = await async_client.streaming.videos.get(
            0,
        )
        assert_matches_type(Video, video, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.videos.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(Video, video, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.videos.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(Video, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_parameters_for_direct_upload(self, async_client: AsyncGcore) -> None:
        video = await async_client.streaming.videos.get_parameters_for_direct_upload(
            0,
        )
        assert_matches_type(DirectUploadParameters, video, path=["response"])

    @parametrize
    async def test_raw_response_get_parameters_for_direct_upload(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.videos.with_raw_response.get_parameters_for_direct_upload(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(DirectUploadParameters, video, path=["response"])

    @parametrize
    async def test_streaming_response_get_parameters_for_direct_upload(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.videos.with_streaming_response.get_parameters_for_direct_upload(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(DirectUploadParameters, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_names(self, async_client: AsyncGcore) -> None:
        video = await async_client.streaming.videos.list_names()
        assert video is None

    @parametrize
    async def test_method_list_names_with_all_params(self, async_client: AsyncGcore) -> None:
        video = await async_client.streaming.videos.list_names(
            ids=[0],
        )
        assert video is None

    @parametrize
    async def test_raw_response_list_names(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.videos.with_raw_response.list_names()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert video is None

    @parametrize
    async def test_streaming_response_list_names(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.videos.with_streaming_response.list_names() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert video is None

        assert cast(Any, response.is_closed) is True

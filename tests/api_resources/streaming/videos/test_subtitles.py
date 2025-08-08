# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.streaming import Subtitle, SubtitleBase
from gcore.types.streaming.videos import SubtitleListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubtitles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Language code is not recognized."}'
    )
    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        subtitle = client.streaming.videos.subtitles.create(
            video_id=0,
            body={},
        )
        assert_matches_type(Subtitle, subtitle, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        subtitle = client.streaming.videos.subtitles.create(
            video_id=0,
            body={
                "language": "language",
                "name": "German (AI-generated)",
                "vtt": "WEBVTT\n\n1\n00:00:07.154 --> 00:00:12.736\nWir haben 100 Millionen registrierte Benutzer oder aktive Benutzer, die mindestens einmal pro Woche spielen.\n\n2\n00:00:13.236 --> 00:00:20.198\nWir haben vielleicht 80 oder 100.000, die auf einem bestimmten Cluster spielen.",
            },
        )
        assert_matches_type(Subtitle, subtitle, path=["response"])

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Language code is not recognized."}'
    )
    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.streaming.videos.subtitles.with_raw_response.create(
            video_id=0,
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subtitle = response.parse()
        assert_matches_type(Subtitle, subtitle, path=["response"])

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Language code is not recognized."}'
    )
    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.streaming.videos.subtitles.with_streaming_response.create(
            video_id=0,
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subtitle = response.parse()
            assert_matches_type(Subtitle, subtitle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        subtitle = client.streaming.videos.subtitles.update(
            id=0,
            video_id=0,
        )
        assert_matches_type(SubtitleBase, subtitle, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        subtitle = client.streaming.videos.subtitles.update(
            id=0,
            video_id=0,
            language="ltz",
            name="name",
            vtt="vtt",
        )
        assert_matches_type(SubtitleBase, subtitle, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.streaming.videos.subtitles.with_raw_response.update(
            id=0,
            video_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subtitle = response.parse()
        assert_matches_type(SubtitleBase, subtitle, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.streaming.videos.subtitles.with_streaming_response.update(
            id=0,
            video_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subtitle = response.parse()
            assert_matches_type(SubtitleBase, subtitle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        subtitle = client.streaming.videos.subtitles.list(
            0,
        )
        assert_matches_type(SubtitleListResponse, subtitle, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.streaming.videos.subtitles.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subtitle = response.parse()
        assert_matches_type(SubtitleListResponse, subtitle, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.streaming.videos.subtitles.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subtitle = response.parse()
            assert_matches_type(SubtitleListResponse, subtitle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        subtitle = client.streaming.videos.subtitles.delete(
            id=0,
            video_id=0,
        )
        assert subtitle is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.streaming.videos.subtitles.with_raw_response.delete(
            id=0,
            video_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subtitle = response.parse()
        assert subtitle is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.streaming.videos.subtitles.with_streaming_response.delete(
            id=0,
            video_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subtitle = response.parse()
            assert subtitle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        subtitle = client.streaming.videos.subtitles.get(
            id=0,
            video_id=0,
        )
        assert_matches_type(Subtitle, subtitle, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.streaming.videos.subtitles.with_raw_response.get(
            id=0,
            video_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subtitle = response.parse()
        assert_matches_type(Subtitle, subtitle, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.streaming.videos.subtitles.with_streaming_response.get(
            id=0,
            video_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subtitle = response.parse()
            assert_matches_type(Subtitle, subtitle, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSubtitles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Language code is not recognized."}'
    )
    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        subtitle = await async_client.streaming.videos.subtitles.create(
            video_id=0,
            body={},
        )
        assert_matches_type(Subtitle, subtitle, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        subtitle = await async_client.streaming.videos.subtitles.create(
            video_id=0,
            body={
                "language": "language",
                "name": "German (AI-generated)",
                "vtt": "WEBVTT\n\n1\n00:00:07.154 --> 00:00:12.736\nWir haben 100 Millionen registrierte Benutzer oder aktive Benutzer, die mindestens einmal pro Woche spielen.\n\n2\n00:00:13.236 --> 00:00:20.198\nWir haben vielleicht 80 oder 100.000, die auf einem bestimmten Cluster spielen.",
            },
        )
        assert_matches_type(Subtitle, subtitle, path=["response"])

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Language code is not recognized."}'
    )
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.videos.subtitles.with_raw_response.create(
            video_id=0,
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subtitle = await response.parse()
        assert_matches_type(Subtitle, subtitle, path=["response"])

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Language code is not recognized."}'
    )
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.videos.subtitles.with_streaming_response.create(
            video_id=0,
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subtitle = await response.parse()
            assert_matches_type(Subtitle, subtitle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        subtitle = await async_client.streaming.videos.subtitles.update(
            id=0,
            video_id=0,
        )
        assert_matches_type(SubtitleBase, subtitle, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        subtitle = await async_client.streaming.videos.subtitles.update(
            id=0,
            video_id=0,
            language="ltz",
            name="name",
            vtt="vtt",
        )
        assert_matches_type(SubtitleBase, subtitle, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.videos.subtitles.with_raw_response.update(
            id=0,
            video_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subtitle = await response.parse()
        assert_matches_type(SubtitleBase, subtitle, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.videos.subtitles.with_streaming_response.update(
            id=0,
            video_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subtitle = await response.parse()
            assert_matches_type(SubtitleBase, subtitle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        subtitle = await async_client.streaming.videos.subtitles.list(
            0,
        )
        assert_matches_type(SubtitleListResponse, subtitle, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.videos.subtitles.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subtitle = await response.parse()
        assert_matches_type(SubtitleListResponse, subtitle, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.videos.subtitles.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subtitle = await response.parse()
            assert_matches_type(SubtitleListResponse, subtitle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        subtitle = await async_client.streaming.videos.subtitles.delete(
            id=0,
            video_id=0,
        )
        assert subtitle is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.videos.subtitles.with_raw_response.delete(
            id=0,
            video_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subtitle = await response.parse()
        assert subtitle is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.videos.subtitles.with_streaming_response.delete(
            id=0,
            video_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subtitle = await response.parse()
            assert subtitle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        subtitle = await async_client.streaming.videos.subtitles.get(
            id=0,
            video_id=0,
        )
        assert_matches_type(Subtitle, subtitle, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.videos.subtitles.with_raw_response.get(
            id=0,
            video_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subtitle = await response.parse()
        assert_matches_type(Subtitle, subtitle, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.videos.subtitles.with_streaming_response.get(
            id=0,
            video_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subtitle = await response.parse()
            assert_matches_type(Subtitle, subtitle, path=["response"])

        assert cast(Any, response.is_closed) is True

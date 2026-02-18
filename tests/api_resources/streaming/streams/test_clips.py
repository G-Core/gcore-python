# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.streaming.streams import Clip, ClipListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClips:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        clip = client.streaming.streams.clips.create(
            stream_id=0,
            duration=0,
        )
        assert_matches_type(Clip, clip, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        clip = client.streaming.streams.clips.create(
            stream_id=0,
            duration=0,
            expiration=0,
            start=0,
            vod_required=True,
        )
        assert_matches_type(Clip, clip, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.streaming.streams.clips.with_raw_response.create(
            stream_id=0,
            duration=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clip = response.parse()
        assert_matches_type(Clip, clip, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.streaming.streams.clips.with_streaming_response.create(
            stream_id=0,
            duration=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clip = response.parse()
            assert_matches_type(Clip, clip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        clip = client.streaming.streams.clips.list(
            0,
        )
        assert_matches_type(ClipListResponse, clip, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.streaming.streams.clips.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clip = response.parse()
        assert_matches_type(ClipListResponse, clip, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.streaming.streams.clips.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clip = response.parse()
            assert_matches_type(ClipListResponse, clip, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClips:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        clip = await async_client.streaming.streams.clips.create(
            stream_id=0,
            duration=0,
        )
        assert_matches_type(Clip, clip, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        clip = await async_client.streaming.streams.clips.create(
            stream_id=0,
            duration=0,
            expiration=0,
            start=0,
            vod_required=True,
        )
        assert_matches_type(Clip, clip, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.clips.with_raw_response.create(
            stream_id=0,
            duration=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clip = await response.parse()
        assert_matches_type(Clip, clip, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.clips.with_streaming_response.create(
            stream_id=0,
            duration=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clip = await response.parse()
            assert_matches_type(Clip, clip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        clip = await async_client.streaming.streams.clips.list(
            0,
        )
        assert_matches_type(ClipListResponse, clip, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.clips.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clip = await response.parse()
        assert_matches_type(ClipListResponse, clip, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.clips.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clip = await response.parse()
            assert_matches_type(ClipListResponse, clip, path=["response"])

        assert cast(Any, response.is_closed) is True

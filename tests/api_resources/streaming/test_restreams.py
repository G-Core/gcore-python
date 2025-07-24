# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncPageStreaming, AsyncPageStreaming
from gcore.types.streaming import Restream

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRestreams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        restream = client.streaming.restreams.create()
        assert restream is None

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        restream = client.streaming.restreams.create(
            restream={
                "active": True,
                "client_user_id": 10,
                "live": True,
                "name": "first restream",
                "stream_id": 20,
                "uri": "rtmp://a.rtmp.youtube.com/live/k17a-13s8",
            },
        )
        assert restream is None

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.streaming.restreams.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restream = response.parse()
        assert restream is None

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.streaming.restreams.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restream = response.parse()
            assert restream is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        restream = client.streaming.restreams.update(
            restream_id=0,
        )
        assert_matches_type(Restream, restream, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        restream = client.streaming.restreams.update(
            restream_id=0,
            restream={
                "active": True,
                "client_user_id": 10,
                "live": True,
                "name": "first restream",
                "stream_id": 20,
                "uri": "rtmp://a.rtmp.youtube.com/live/k17a-13s8",
            },
        )
        assert_matches_type(Restream, restream, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.streaming.restreams.with_raw_response.update(
            restream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restream = response.parse()
        assert_matches_type(Restream, restream, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.streaming.restreams.with_streaming_response.update(
            restream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restream = response.parse()
            assert_matches_type(Restream, restream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        restream = client.streaming.restreams.list()
        assert_matches_type(SyncPageStreaming[Restream], restream, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        restream = client.streaming.restreams.list(
            page=0,
        )
        assert_matches_type(SyncPageStreaming[Restream], restream, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.streaming.restreams.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restream = response.parse()
        assert_matches_type(SyncPageStreaming[Restream], restream, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.streaming.restreams.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restream = response.parse()
            assert_matches_type(SyncPageStreaming[Restream], restream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        restream = client.streaming.restreams.delete(
            0,
        )
        assert restream is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.streaming.restreams.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restream = response.parse()
        assert restream is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.streaming.restreams.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restream = response.parse()
            assert restream is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        restream = client.streaming.restreams.get(
            0,
        )
        assert_matches_type(Restream, restream, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.streaming.restreams.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restream = response.parse()
        assert_matches_type(Restream, restream, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.streaming.restreams.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restream = response.parse()
            assert_matches_type(Restream, restream, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRestreams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        restream = await async_client.streaming.restreams.create()
        assert restream is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        restream = await async_client.streaming.restreams.create(
            restream={
                "active": True,
                "client_user_id": 10,
                "live": True,
                "name": "first restream",
                "stream_id": 20,
                "uri": "rtmp://a.rtmp.youtube.com/live/k17a-13s8",
            },
        )
        assert restream is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.restreams.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restream = await response.parse()
        assert restream is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.restreams.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restream = await response.parse()
            assert restream is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        restream = await async_client.streaming.restreams.update(
            restream_id=0,
        )
        assert_matches_type(Restream, restream, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        restream = await async_client.streaming.restreams.update(
            restream_id=0,
            restream={
                "active": True,
                "client_user_id": 10,
                "live": True,
                "name": "first restream",
                "stream_id": 20,
                "uri": "rtmp://a.rtmp.youtube.com/live/k17a-13s8",
            },
        )
        assert_matches_type(Restream, restream, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.restreams.with_raw_response.update(
            restream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restream = await response.parse()
        assert_matches_type(Restream, restream, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.restreams.with_streaming_response.update(
            restream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restream = await response.parse()
            assert_matches_type(Restream, restream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        restream = await async_client.streaming.restreams.list()
        assert_matches_type(AsyncPageStreaming[Restream], restream, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        restream = await async_client.streaming.restreams.list(
            page=0,
        )
        assert_matches_type(AsyncPageStreaming[Restream], restream, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.restreams.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restream = await response.parse()
        assert_matches_type(AsyncPageStreaming[Restream], restream, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.restreams.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restream = await response.parse()
            assert_matches_type(AsyncPageStreaming[Restream], restream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        restream = await async_client.streaming.restreams.delete(
            0,
        )
        assert restream is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.restreams.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restream = await response.parse()
        assert restream is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.restreams.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restream = await response.parse()
            assert restream is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        restream = await async_client.streaming.restreams.get(
            0,
        )
        assert_matches_type(Restream, restream, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.restreams.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restream = await response.parse()
        assert_matches_type(Restream, restream, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.restreams.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restream = await response.parse()
            assert_matches_type(Restream, restream, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.streaming.streams import (
    Overlay,
    OverlayListResponse,
    OverlayCreateResponse,
    OverlayUpdateMultipleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOverlays:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        overlay = client.streaming.streams.overlays.create(
            stream_id=0,
        )
        assert_matches_type(OverlayCreateResponse, overlay, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        overlay = client.streaming.streams.overlays.create(
            stream_id=0,
            body=[
                {
                    "url": "http://domain.com/myoverlay1.html",
                    "height": 40,
                    "stretch": False,
                    "width": 120,
                    "x": 30,
                    "y": 30,
                }
            ],
        )
        assert_matches_type(OverlayCreateResponse, overlay, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.streaming.streams.overlays.with_raw_response.create(
            stream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overlay = response.parse()
        assert_matches_type(OverlayCreateResponse, overlay, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.streaming.streams.overlays.with_streaming_response.create(
            stream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overlay = response.parse()
            assert_matches_type(OverlayCreateResponse, overlay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        overlay = client.streaming.streams.overlays.update(
            overlay_id=0,
            stream_id=0,
        )
        assert_matches_type(Overlay, overlay, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        overlay = client.streaming.streams.overlays.update(
            overlay_id=0,
            stream_id=0,
            height=0,
            stretch=True,
            url="http://domain.com/myoverlay_new_3.html",
            width=0,
            x=0,
            y=0,
        )
        assert_matches_type(Overlay, overlay, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.streaming.streams.overlays.with_raw_response.update(
            overlay_id=0,
            stream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overlay = response.parse()
        assert_matches_type(Overlay, overlay, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.streaming.streams.overlays.with_streaming_response.update(
            overlay_id=0,
            stream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overlay = response.parse()
            assert_matches_type(Overlay, overlay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        overlay = client.streaming.streams.overlays.list(
            0,
        )
        assert_matches_type(OverlayListResponse, overlay, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.streaming.streams.overlays.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overlay = response.parse()
        assert_matches_type(OverlayListResponse, overlay, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.streaming.streams.overlays.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overlay = response.parse()
            assert_matches_type(OverlayListResponse, overlay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        overlay = client.streaming.streams.overlays.delete(
            overlay_id=0,
            stream_id=0,
        )
        assert overlay is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.streaming.streams.overlays.with_raw_response.delete(
            overlay_id=0,
            stream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overlay = response.parse()
        assert overlay is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.streaming.streams.overlays.with_streaming_response.delete(
            overlay_id=0,
            stream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overlay = response.parse()
            assert overlay is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        overlay = client.streaming.streams.overlays.get(
            overlay_id=0,
            stream_id=0,
        )
        assert_matches_type(Overlay, overlay, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.streaming.streams.overlays.with_raw_response.get(
            overlay_id=0,
            stream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overlay = response.parse()
        assert_matches_type(Overlay, overlay, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.streaming.streams.overlays.with_streaming_response.get(
            overlay_id=0,
            stream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overlay = response.parse()
            assert_matches_type(Overlay, overlay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_multiple(self, client: Gcore) -> None:
        overlay = client.streaming.streams.overlays.update_multiple(
            stream_id=0,
        )
        assert_matches_type(OverlayUpdateMultipleResponse, overlay, path=["response"])

    @parametrize
    def test_method_update_multiple_with_all_params(self, client: Gcore) -> None:
        overlay = client.streaming.streams.overlays.update_multiple(
            stream_id=0,
            body=[
                {
                    "id": 0,
                    "height": 0,
                    "stretch": True,
                    "url": "url",
                    "width": 0,
                    "x": 0,
                    "y": 0,
                }
            ],
        )
        assert_matches_type(OverlayUpdateMultipleResponse, overlay, path=["response"])

    @parametrize
    def test_raw_response_update_multiple(self, client: Gcore) -> None:
        response = client.streaming.streams.overlays.with_raw_response.update_multiple(
            stream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overlay = response.parse()
        assert_matches_type(OverlayUpdateMultipleResponse, overlay, path=["response"])

    @parametrize
    def test_streaming_response_update_multiple(self, client: Gcore) -> None:
        with client.streaming.streams.overlays.with_streaming_response.update_multiple(
            stream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overlay = response.parse()
            assert_matches_type(OverlayUpdateMultipleResponse, overlay, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOverlays:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        overlay = await async_client.streaming.streams.overlays.create(
            stream_id=0,
        )
        assert_matches_type(OverlayCreateResponse, overlay, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        overlay = await async_client.streaming.streams.overlays.create(
            stream_id=0,
            body=[
                {
                    "url": "http://domain.com/myoverlay1.html",
                    "height": 40,
                    "stretch": False,
                    "width": 120,
                    "x": 30,
                    "y": 30,
                }
            ],
        )
        assert_matches_type(OverlayCreateResponse, overlay, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.overlays.with_raw_response.create(
            stream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overlay = await response.parse()
        assert_matches_type(OverlayCreateResponse, overlay, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.overlays.with_streaming_response.create(
            stream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overlay = await response.parse()
            assert_matches_type(OverlayCreateResponse, overlay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        overlay = await async_client.streaming.streams.overlays.update(
            overlay_id=0,
            stream_id=0,
        )
        assert_matches_type(Overlay, overlay, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        overlay = await async_client.streaming.streams.overlays.update(
            overlay_id=0,
            stream_id=0,
            height=0,
            stretch=True,
            url="http://domain.com/myoverlay_new_3.html",
            width=0,
            x=0,
            y=0,
        )
        assert_matches_type(Overlay, overlay, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.overlays.with_raw_response.update(
            overlay_id=0,
            stream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overlay = await response.parse()
        assert_matches_type(Overlay, overlay, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.overlays.with_streaming_response.update(
            overlay_id=0,
            stream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overlay = await response.parse()
            assert_matches_type(Overlay, overlay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        overlay = await async_client.streaming.streams.overlays.list(
            0,
        )
        assert_matches_type(OverlayListResponse, overlay, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.overlays.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overlay = await response.parse()
        assert_matches_type(OverlayListResponse, overlay, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.overlays.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overlay = await response.parse()
            assert_matches_type(OverlayListResponse, overlay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        overlay = await async_client.streaming.streams.overlays.delete(
            overlay_id=0,
            stream_id=0,
        )
        assert overlay is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.overlays.with_raw_response.delete(
            overlay_id=0,
            stream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overlay = await response.parse()
        assert overlay is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.overlays.with_streaming_response.delete(
            overlay_id=0,
            stream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overlay = await response.parse()
            assert overlay is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        overlay = await async_client.streaming.streams.overlays.get(
            overlay_id=0,
            stream_id=0,
        )
        assert_matches_type(Overlay, overlay, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.overlays.with_raw_response.get(
            overlay_id=0,
            stream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overlay = await response.parse()
        assert_matches_type(Overlay, overlay, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.overlays.with_streaming_response.get(
            overlay_id=0,
            stream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overlay = await response.parse()
            assert_matches_type(Overlay, overlay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_multiple(self, async_client: AsyncGcore) -> None:
        overlay = await async_client.streaming.streams.overlays.update_multiple(
            stream_id=0,
        )
        assert_matches_type(OverlayUpdateMultipleResponse, overlay, path=["response"])

    @parametrize
    async def test_method_update_multiple_with_all_params(self, async_client: AsyncGcore) -> None:
        overlay = await async_client.streaming.streams.overlays.update_multiple(
            stream_id=0,
            body=[
                {
                    "id": 0,
                    "height": 0,
                    "stretch": True,
                    "url": "url",
                    "width": 0,
                    "x": 0,
                    "y": 0,
                }
            ],
        )
        assert_matches_type(OverlayUpdateMultipleResponse, overlay, path=["response"])

    @parametrize
    async def test_raw_response_update_multiple(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.streams.overlays.with_raw_response.update_multiple(
            stream_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overlay = await response.parse()
        assert_matches_type(OverlayUpdateMultipleResponse, overlay, path=["response"])

    @parametrize
    async def test_streaming_response_update_multiple(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.streams.overlays.with_streaming_response.update_multiple(
            stream_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overlay = await response.parse()
            assert_matches_type(OverlayUpdateMultipleResponse, overlay, path=["response"])

        assert cast(Any, response.is_closed) is True

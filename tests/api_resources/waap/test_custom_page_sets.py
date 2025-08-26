# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.waap import (
    WaapCustomPageSet,
    WaapCustomPagePreview,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomPageSets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        custom_page_set = client.waap.custom_page_sets.create(
            name="x",
        )
        assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        custom_page_set = client.waap.custom_page_sets.create(
            name="x",
            block={
                "enabled": True,
                "header": "xxx",
                "logo": "logo",
                "text": "xxxxxxxxxxxxxxxxxxxx",
                "title": "xxx",
            },
            block_csrf={
                "enabled": True,
                "header": "xxx",
                "logo": "logo",
                "text": "xxxxxxxxxxxxxxxxxxxx",
                "title": "xxx",
            },
            captcha={
                "enabled": True,
                "error": "xxxxxxxxxx",
                "header": "xxx",
                "logo": "logo",
                "text": "xxxxxxxxxxxxxxxxxxxx",
                "title": "xxx",
            },
            cookie_disabled={
                "enabled": True,
                "header": "xxx",
                "text": "xxxxxxxxxxxxxxxxxxxx",
            },
            domains=[1],
            handshake={
                "enabled": True,
                "header": "xxx",
                "logo": "logo",
                "title": "xxx",
            },
            javascript_disabled={
                "enabled": True,
                "header": "xxx",
                "text": "xxxxxxxxxxxxxxxxxxxx",
            },
        )
        assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.waap.custom_page_sets.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page_set = response.parse()
        assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.waap.custom_page_sets.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page_set = response.parse()
            assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        custom_page_set = client.waap.custom_page_sets.update(
            set_id=0,
        )
        assert custom_page_set is None

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        custom_page_set = client.waap.custom_page_sets.update(
            set_id=0,
            block={
                "enabled": True,
                "header": "xxx",
                "logo": "logo",
                "text": "xxxxxxxxxxxxxxxxxxxx",
                "title": "xxx",
            },
            block_csrf={
                "enabled": True,
                "header": "xxx",
                "logo": "logo",
                "text": "xxxxxxxxxxxxxxxxxxxx",
                "title": "xxx",
            },
            captcha={
                "enabled": True,
                "error": "xxxxxxxxxx",
                "header": "xxx",
                "logo": "logo",
                "text": "xxxxxxxxxxxxxxxxxxxx",
                "title": "xxx",
            },
            cookie_disabled={
                "enabled": True,
                "header": "xxx",
                "text": "xxxxxxxxxxxxxxxxxxxx",
            },
            domains=[1],
            handshake={
                "enabled": True,
                "header": "xxx",
                "logo": "logo",
                "title": "xxx",
            },
            javascript_disabled={
                "enabled": True,
                "header": "xxx",
                "text": "xxxxxxxxxxxxxxxxxxxx",
            },
            name="x",
        )
        assert custom_page_set is None

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.waap.custom_page_sets.with_raw_response.update(
            set_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page_set = response.parse()
        assert custom_page_set is None

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.waap.custom_page_sets.with_streaming_response.update(
            set_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page_set = response.parse()
            assert custom_page_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        custom_page_set = client.waap.custom_page_sets.list()
        assert_matches_type(SyncOffsetPage[WaapCustomPageSet], custom_page_set, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        custom_page_set = client.waap.custom_page_sets.list(
            ids=[0],
            limit=0,
            name="*example",
            offset=0,
            ordering="name",
        )
        assert_matches_type(SyncOffsetPage[WaapCustomPageSet], custom_page_set, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.waap.custom_page_sets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page_set = response.parse()
        assert_matches_type(SyncOffsetPage[WaapCustomPageSet], custom_page_set, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.waap.custom_page_sets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page_set = response.parse()
            assert_matches_type(SyncOffsetPage[WaapCustomPageSet], custom_page_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        custom_page_set = client.waap.custom_page_sets.delete(
            0,
        )
        assert custom_page_set is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.waap.custom_page_sets.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page_set = response.parse()
        assert custom_page_set is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.waap.custom_page_sets.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page_set = response.parse()
            assert custom_page_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        custom_page_set = client.waap.custom_page_sets.get(
            0,
        )
        assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.waap.custom_page_sets.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page_set = response.parse()
        assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.waap.custom_page_sets.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page_set = response.parse()
            assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_preview(self, client: Gcore) -> None:
        custom_page_set = client.waap.custom_page_sets.preview(
            page_type="block.html",
        )
        assert_matches_type(WaapCustomPagePreview, custom_page_set, path=["response"])

    @parametrize
    def test_method_preview_with_all_params(self, client: Gcore) -> None:
        custom_page_set = client.waap.custom_page_sets.preview(
            page_type="block.html",
            error="xxxxxxxxxx",
            header="xxx",
            logo="logo",
            text="xxxxxxxxxxxxxxxxxxxx",
            title="xxx",
        )
        assert_matches_type(WaapCustomPagePreview, custom_page_set, path=["response"])

    @parametrize
    def test_raw_response_preview(self, client: Gcore) -> None:
        response = client.waap.custom_page_sets.with_raw_response.preview(
            page_type="block.html",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page_set = response.parse()
        assert_matches_type(WaapCustomPagePreview, custom_page_set, path=["response"])

    @parametrize
    def test_streaming_response_preview(self, client: Gcore) -> None:
        with client.waap.custom_page_sets.with_streaming_response.preview(
            page_type="block.html",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page_set = response.parse()
            assert_matches_type(WaapCustomPagePreview, custom_page_set, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomPageSets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        custom_page_set = await async_client.waap.custom_page_sets.create(
            name="x",
        )
        assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        custom_page_set = await async_client.waap.custom_page_sets.create(
            name="x",
            block={
                "enabled": True,
                "header": "xxx",
                "logo": "logo",
                "text": "xxxxxxxxxxxxxxxxxxxx",
                "title": "xxx",
            },
            block_csrf={
                "enabled": True,
                "header": "xxx",
                "logo": "logo",
                "text": "xxxxxxxxxxxxxxxxxxxx",
                "title": "xxx",
            },
            captcha={
                "enabled": True,
                "error": "xxxxxxxxxx",
                "header": "xxx",
                "logo": "logo",
                "text": "xxxxxxxxxxxxxxxxxxxx",
                "title": "xxx",
            },
            cookie_disabled={
                "enabled": True,
                "header": "xxx",
                "text": "xxxxxxxxxxxxxxxxxxxx",
            },
            domains=[1],
            handshake={
                "enabled": True,
                "header": "xxx",
                "logo": "logo",
                "title": "xxx",
            },
            javascript_disabled={
                "enabled": True,
                "header": "xxx",
                "text": "xxxxxxxxxxxxxxxxxxxx",
            },
        )
        assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.custom_page_sets.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page_set = await response.parse()
        assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.custom_page_sets.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page_set = await response.parse()
            assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        custom_page_set = await async_client.waap.custom_page_sets.update(
            set_id=0,
        )
        assert custom_page_set is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        custom_page_set = await async_client.waap.custom_page_sets.update(
            set_id=0,
            block={
                "enabled": True,
                "header": "xxx",
                "logo": "logo",
                "text": "xxxxxxxxxxxxxxxxxxxx",
                "title": "xxx",
            },
            block_csrf={
                "enabled": True,
                "header": "xxx",
                "logo": "logo",
                "text": "xxxxxxxxxxxxxxxxxxxx",
                "title": "xxx",
            },
            captcha={
                "enabled": True,
                "error": "xxxxxxxxxx",
                "header": "xxx",
                "logo": "logo",
                "text": "xxxxxxxxxxxxxxxxxxxx",
                "title": "xxx",
            },
            cookie_disabled={
                "enabled": True,
                "header": "xxx",
                "text": "xxxxxxxxxxxxxxxxxxxx",
            },
            domains=[1],
            handshake={
                "enabled": True,
                "header": "xxx",
                "logo": "logo",
                "title": "xxx",
            },
            javascript_disabled={
                "enabled": True,
                "header": "xxx",
                "text": "xxxxxxxxxxxxxxxxxxxx",
            },
            name="x",
        )
        assert custom_page_set is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.custom_page_sets.with_raw_response.update(
            set_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page_set = await response.parse()
        assert custom_page_set is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.custom_page_sets.with_streaming_response.update(
            set_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page_set = await response.parse()
            assert custom_page_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        custom_page_set = await async_client.waap.custom_page_sets.list()
        assert_matches_type(AsyncOffsetPage[WaapCustomPageSet], custom_page_set, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        custom_page_set = await async_client.waap.custom_page_sets.list(
            ids=[0],
            limit=0,
            name="*example",
            offset=0,
            ordering="name",
        )
        assert_matches_type(AsyncOffsetPage[WaapCustomPageSet], custom_page_set, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.custom_page_sets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page_set = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapCustomPageSet], custom_page_set, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.custom_page_sets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page_set = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapCustomPageSet], custom_page_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        custom_page_set = await async_client.waap.custom_page_sets.delete(
            0,
        )
        assert custom_page_set is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.custom_page_sets.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page_set = await response.parse()
        assert custom_page_set is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.custom_page_sets.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page_set = await response.parse()
            assert custom_page_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        custom_page_set = await async_client.waap.custom_page_sets.get(
            0,
        )
        assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.custom_page_sets.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page_set = await response.parse()
        assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.custom_page_sets.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page_set = await response.parse()
            assert_matches_type(WaapCustomPageSet, custom_page_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_preview(self, async_client: AsyncGcore) -> None:
        custom_page_set = await async_client.waap.custom_page_sets.preview(
            page_type="block.html",
        )
        assert_matches_type(WaapCustomPagePreview, custom_page_set, path=["response"])

    @parametrize
    async def test_method_preview_with_all_params(self, async_client: AsyncGcore) -> None:
        custom_page_set = await async_client.waap.custom_page_sets.preview(
            page_type="block.html",
            error="xxxxxxxxxx",
            header="xxx",
            logo="logo",
            text="xxxxxxxxxxxxxxxxxxxx",
            title="xxx",
        )
        assert_matches_type(WaapCustomPagePreview, custom_page_set, path=["response"])

    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.custom_page_sets.with_raw_response.preview(
            page_type="block.html",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page_set = await response.parse()
        assert_matches_type(WaapCustomPagePreview, custom_page_set, path=["response"])

    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.custom_page_sets.with_streaming_response.preview(
            page_type="block.html",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page_set = await response.parse()
            assert_matches_type(WaapCustomPagePreview, custom_page_set, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.waap import (
    WaapFilterTemplate,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFilterTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        filter_template = client.waap.filter_templates.create(
            filter_config={
                "domains": "bar",
                "event": "bar",
            },
            name="name",
        )
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.waap.filter_templates.with_raw_response.create(
            filter_config={
                "domains": "bar",
                "event": "bar",
            },
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter_template = response.parse()
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.waap.filter_templates.with_streaming_response.create(
            filter_config={
                "domains": "bar",
                "event": "bar",
            },
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter_template = response.parse()
            assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        filter_template = client.waap.filter_templates.update(
            template_id=0,
        )
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        filter_template = client.waap.filter_templates.update(
            template_id=0,
            filter_config={"foo": "bar"},
            name="name",
        )
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.waap.filter_templates.with_raw_response.update(
            template_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter_template = response.parse()
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.waap.filter_templates.with_streaming_response.update(
            template_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter_template = response.parse()
            assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        filter_template = client.waap.filter_templates.list()
        assert_matches_type(SyncOffsetPage[WaapFilterTemplate], filter_template, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        filter_template = client.waap.filter_templates.list(
            limit=0,
            name="name",
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[WaapFilterTemplate], filter_template, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.waap.filter_templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter_template = response.parse()
        assert_matches_type(SyncOffsetPage[WaapFilterTemplate], filter_template, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.waap.filter_templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter_template = response.parse()
            assert_matches_type(SyncOffsetPage[WaapFilterTemplate], filter_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        filter_template = client.waap.filter_templates.delete(
            0,
        )
        assert filter_template is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.waap.filter_templates.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter_template = response.parse()
        assert filter_template is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.waap.filter_templates.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter_template = response.parse()
            assert filter_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        filter_template = client.waap.filter_templates.get(
            0,
        )
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.waap.filter_templates.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter_template = response.parse()
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.waap.filter_templates.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter_template = response.parse()
            assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFilterTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        filter_template = await async_client.waap.filter_templates.create(
            filter_config={
                "domains": "bar",
                "event": "bar",
            },
            name="name",
        )
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.filter_templates.with_raw_response.create(
            filter_config={
                "domains": "bar",
                "event": "bar",
            },
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter_template = await response.parse()
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.filter_templates.with_streaming_response.create(
            filter_config={
                "domains": "bar",
                "event": "bar",
            },
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter_template = await response.parse()
            assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        filter_template = await async_client.waap.filter_templates.update(
            template_id=0,
        )
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        filter_template = await async_client.waap.filter_templates.update(
            template_id=0,
            filter_config={"foo": "bar"},
            name="name",
        )
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.filter_templates.with_raw_response.update(
            template_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter_template = await response.parse()
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.filter_templates.with_streaming_response.update(
            template_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter_template = await response.parse()
            assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        filter_template = await async_client.waap.filter_templates.list()
        assert_matches_type(AsyncOffsetPage[WaapFilterTemplate], filter_template, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        filter_template = await async_client.waap.filter_templates.list(
            limit=0,
            name="name",
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[WaapFilterTemplate], filter_template, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.filter_templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter_template = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapFilterTemplate], filter_template, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.filter_templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter_template = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapFilterTemplate], filter_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        filter_template = await async_client.waap.filter_templates.delete(
            0,
        )
        assert filter_template is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.filter_templates.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter_template = await response.parse()
        assert filter_template is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.filter_templates.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter_template = await response.parse()
            assert filter_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        filter_template = await async_client.waap.filter_templates.get(
            0,
        )
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.filter_templates.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter_template = await response.parse()
        assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.filter_templates.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter_template = await response.parse()
            assert_matches_type(WaapFilterTemplate, filter_template, path=["response"])

        assert cast(Any, response.is_closed) is True

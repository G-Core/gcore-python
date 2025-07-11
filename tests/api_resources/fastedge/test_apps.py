# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPageFastedgeApps, AsyncOffsetPageFastedgeApps
from gcore.types.fastedge import (
    App,
    AppShort,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        app = client.fastedge.apps.create()
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        app = client.fastedge.apps.create(
            binary=0,
            comment="comment",
            debug=True,
            env={
                "var1": "value1",
                "var2": "value2",
            },
            log="kafka",
            name="name",
            rsp_headers={
                "header1": "value1",
                "header2": "value2",
            },
            secrets={"foo": {"id": 0}},
            status=0,
            stores={
                "country_allow": 1,
                "ip_block": 2,
            },
            template=0,
        )
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.fastedge.apps.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.fastedge.apps.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppShort, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        app = client.fastedge.apps.update(
            id=0,
        )
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        app = client.fastedge.apps.update(
            id=0,
            binary=0,
            comment="comment",
            debug=True,
            env={
                "var1": "value1",
                "var2": "value2",
            },
            log="kafka",
            name="name",
            rsp_headers={
                "header1": "value1",
                "header2": "value2",
            },
            secrets={"foo": {"id": 0}},
            status=0,
            stores={
                "country_allow": 1,
                "ip_block": 2,
            },
            template=0,
        )
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.fastedge.apps.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.fastedge.apps.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppShort, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        app = client.fastedge.apps.list()
        assert_matches_type(SyncOffsetPageFastedgeApps[AppShort], app, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        app = client.fastedge.apps.list(
            api_type="wasi-http",
            binary=0,
            limit=0,
            name="name",
            offset=0,
            ordering="name",
            plan=0,
            status=0,
            template=0,
        )
        assert_matches_type(SyncOffsetPageFastedgeApps[AppShort], app, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.fastedge.apps.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(SyncOffsetPageFastedgeApps[AppShort], app, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.fastedge.apps.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(SyncOffsetPageFastedgeApps[AppShort], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        app = client.fastedge.apps.delete(
            0,
        )
        assert app is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.fastedge.apps.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert app is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.fastedge.apps.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert app is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        app = client.fastedge.apps.get(
            0,
        )
        assert_matches_type(App, app, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.fastedge.apps.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(App, app, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.fastedge.apps.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(App, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        app = client.fastedge.apps.replace(
            id=0,
        )
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        app = client.fastedge.apps.replace(
            id=0,
            body={
                "binary": 0,
                "comment": "comment",
                "debug": True,
                "env": {
                    "var1": "value1",
                    "var2": "value2",
                },
                "log": "kafka",
                "name": "name",
                "rsp_headers": {
                    "header1": "value1",
                    "header2": "value2",
                },
                "secrets": {"foo": {"id": 0}},
                "status": 0,
                "stores": {
                    "country_allow": 1,
                    "ip_block": 2,
                },
                "template": 0,
            },
        )
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.fastedge.apps.with_raw_response.replace(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.fastedge.apps.with_streaming_response.replace(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppShort, app, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncApps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        app = await async_client.fastedge.apps.create()
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        app = await async_client.fastedge.apps.create(
            binary=0,
            comment="comment",
            debug=True,
            env={
                "var1": "value1",
                "var2": "value2",
            },
            log="kafka",
            name="name",
            rsp_headers={
                "header1": "value1",
                "header2": "value2",
            },
            secrets={"foo": {"id": 0}},
            status=0,
            stores={
                "country_allow": 1,
                "ip_block": 2,
            },
            template=0,
        )
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.apps.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.apps.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppShort, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        app = await async_client.fastedge.apps.update(
            id=0,
        )
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        app = await async_client.fastedge.apps.update(
            id=0,
            binary=0,
            comment="comment",
            debug=True,
            env={
                "var1": "value1",
                "var2": "value2",
            },
            log="kafka",
            name="name",
            rsp_headers={
                "header1": "value1",
                "header2": "value2",
            },
            secrets={"foo": {"id": 0}},
            status=0,
            stores={
                "country_allow": 1,
                "ip_block": 2,
            },
            template=0,
        )
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.apps.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.apps.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppShort, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        app = await async_client.fastedge.apps.list()
        assert_matches_type(AsyncOffsetPageFastedgeApps[AppShort], app, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        app = await async_client.fastedge.apps.list(
            api_type="wasi-http",
            binary=0,
            limit=0,
            name="name",
            offset=0,
            ordering="name",
            plan=0,
            status=0,
            template=0,
        )
        assert_matches_type(AsyncOffsetPageFastedgeApps[AppShort], app, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.apps.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AsyncOffsetPageFastedgeApps[AppShort], app, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.apps.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AsyncOffsetPageFastedgeApps[AppShort], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        app = await async_client.fastedge.apps.delete(
            0,
        )
        assert app is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.apps.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert app is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.apps.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert app is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        app = await async_client.fastedge.apps.get(
            0,
        )
        assert_matches_type(App, app, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.apps.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(App, app, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.apps.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(App, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        app = await async_client.fastedge.apps.replace(
            id=0,
        )
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        app = await async_client.fastedge.apps.replace(
            id=0,
            body={
                "binary": 0,
                "comment": "comment",
                "debug": True,
                "env": {
                    "var1": "value1",
                    "var2": "value2",
                },
                "log": "kafka",
                "name": "name",
                "rsp_headers": {
                    "header1": "value1",
                    "header2": "value2",
                },
                "secrets": {"foo": {"id": 0}},
                "status": 0,
                "stores": {
                    "country_allow": 1,
                    "ip_block": 2,
                },
                "template": 0,
            },
        )
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.apps.with_raw_response.replace(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppShort, app, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.apps.with_streaming_response.replace(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppShort, app, path=["response"])

        assert cast(Any, response.is_closed) is True

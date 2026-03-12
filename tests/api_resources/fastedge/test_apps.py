# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPageFastedgeApps, AsyncOffsetPageFastedgeApps
from gcore.types.fastedge import AppShort

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
            binary=12345,
            comment="Production API gateway for customer portal",
            debug=False,
            env={
                "var1": "value1",
                "var2": "value2",
            },
            log="kafka",
            name="my-edge-app",
            rsp_headers={
                "header1": "value1",
                "header2": "value2",
            },
            secrets={"foo": {"id": 0}},
            status=1,
            stores={"foo": {"id": 0}},
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
    def test_method_list(self, client: Gcore) -> None:
        app = client.fastedge.apps.list()
        assert_matches_type(SyncOffsetPageFastedgeApps[AppShort], app, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        app = client.fastedge.apps.list(
            api_type="wasi-http",
            binary=1,
            limit=1,
            name="x",
            offset=0,
            ordering="name",
            plan=1,
            status=0,
            template=1,
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
            binary=12345,
            comment="Production API gateway for customer portal",
            debug=False,
            env={
                "var1": "value1",
                "var2": "value2",
            },
            log="kafka",
            name="my-edge-app",
            rsp_headers={
                "header1": "value1",
                "header2": "value2",
            },
            secrets={"foo": {"id": 0}},
            status=1,
            stores={"foo": {"id": 0}},
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
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        app = await async_client.fastedge.apps.list()
        assert_matches_type(AsyncOffsetPageFastedgeApps[AppShort], app, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        app = await async_client.fastedge.apps.list(
            api_type="wasi-http",
            binary=1,
            limit=1,
            name="x",
            offset=0,
            ordering="name",
            plan=1,
            status=0,
            template=1,
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

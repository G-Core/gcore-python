# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPageFastedgeTemplates, AsyncOffsetPageFastedgeTemplates
from gcore.types.fastedge import TemplateShort

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        template = client.fastedge.templates.create(
            binary_id=12345,
            name="api-gateway-template",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "api_key",
                }
            ],
        )
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        template = client.fastedge.templates.create(
            binary_id=12345,
            name="api-gateway-template",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "api_key",
                    "descr": "API key for external service authentication",
                    "metadata": "metadata",
                }
            ],
            long_descr="Complete API gateway solution with JWT authentication, rate limiting, and request transformation capabilities.",
            short_descr="HTTP API gateway with authentication",
        )
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.fastedge.templates.with_raw_response.create(
            binary_id=12345,
            name="api-gateway-template",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "api_key",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.fastedge.templates.with_streaming_response.create(
            binary_id=12345,
            name="api-gateway-template",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "api_key",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateShort, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        template = client.fastedge.templates.list()
        assert_matches_type(SyncOffsetPageFastedgeTemplates[TemplateShort], template, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        template = client.fastedge.templates.list(
            api_type="wasi-http",
            limit=1,
            offset=0,
            only_mine=True,
        )
        assert_matches_type(SyncOffsetPageFastedgeTemplates[TemplateShort], template, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.fastedge.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(SyncOffsetPageFastedgeTemplates[TemplateShort], template, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.fastedge.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(SyncOffsetPageFastedgeTemplates[TemplateShort], template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        template = await async_client.fastedge.templates.create(
            binary_id=12345,
            name="api-gateway-template",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "api_key",
                }
            ],
        )
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        template = await async_client.fastedge.templates.create(
            binary_id=12345,
            name="api-gateway-template",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "api_key",
                    "descr": "API key for external service authentication",
                    "metadata": "metadata",
                }
            ],
            long_descr="Complete API gateway solution with JWT authentication, rate limiting, and request transformation capabilities.",
            short_descr="HTTP API gateway with authentication",
        )
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.templates.with_raw_response.create(
            binary_id=12345,
            name="api-gateway-template",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "api_key",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.templates.with_streaming_response.create(
            binary_id=12345,
            name="api-gateway-template",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "api_key",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateShort, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        template = await async_client.fastedge.templates.list()
        assert_matches_type(AsyncOffsetPageFastedgeTemplates[TemplateShort], template, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        template = await async_client.fastedge.templates.list(
            api_type="wasi-http",
            limit=1,
            offset=0,
            only_mine=True,
        )
        assert_matches_type(AsyncOffsetPageFastedgeTemplates[TemplateShort], template, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(AsyncOffsetPageFastedgeTemplates[TemplateShort], template, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(AsyncOffsetPageFastedgeTemplates[TemplateShort], template, path=["response"])

        assert cast(Any, response.is_closed) is True

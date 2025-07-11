# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPageFastedgeTemplates, AsyncOffsetPageFastedgeTemplates
from gcore.types.fastedge import (
    Template,
    TemplateShort,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        template = client.fastedge.templates.create(
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
                }
            ],
        )
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        template = client.fastedge.templates.create(
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
                    "descr": "descr",
                }
            ],
            long_descr="long_descr",
            short_descr="short_descr",
        )
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.fastedge.templates.with_raw_response.create(
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
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
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
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
            limit=0,
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

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        template = client.fastedge.templates.delete(
            id=0,
        )
        assert template is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        template = client.fastedge.templates.delete(
            id=0,
            force=True,
        )
        assert template is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.fastedge.templates.with_raw_response.delete(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert template is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.fastedge.templates.with_streaming_response.delete(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        template = client.fastedge.templates.get(
            0,
        )
        assert_matches_type(Template, template, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.fastedge.templates.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(Template, template, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.fastedge.templates.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(Template, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        template = client.fastedge.templates.replace(
            id=0,
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
                }
            ],
        )
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        template = client.fastedge.templates.replace(
            id=0,
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
                    "descr": "descr",
                }
            ],
            long_descr="long_descr",
            short_descr="short_descr",
        )
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.fastedge.templates.with_raw_response.replace(
            id=0,
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.fastedge.templates.with_streaming_response.replace(
            id=0,
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateShort, template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        template = await async_client.fastedge.templates.create(
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
                }
            ],
        )
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        template = await async_client.fastedge.templates.create(
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
                    "descr": "descr",
                }
            ],
            long_descr="long_descr",
            short_descr="short_descr",
        )
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.templates.with_raw_response.create(
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
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
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
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
            limit=0,
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

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        template = await async_client.fastedge.templates.delete(
            id=0,
        )
        assert template is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        template = await async_client.fastedge.templates.delete(
            id=0,
            force=True,
        )
        assert template is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.templates.with_raw_response.delete(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert template is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.templates.with_streaming_response.delete(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        template = await async_client.fastedge.templates.get(
            0,
        )
        assert_matches_type(Template, template, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.templates.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(Template, template, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.templates.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(Template, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        template = await async_client.fastedge.templates.replace(
            id=0,
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
                }
            ],
        )
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        template = await async_client.fastedge.templates.replace(
            id=0,
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
                    "descr": "descr",
                }
            ],
            long_descr="long_descr",
            short_descr="short_descr",
        )
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.templates.with_raw_response.replace(
            id=0,
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateShort, template, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.templates.with_streaming_response.replace(
            id=0,
            binary_id=0,
            name="name",
            owned=True,
            params=[
                {
                    "data_type": "string",
                    "mandatory": True,
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateShort, template, path=["response"])

        assert cast(Any, response.is_closed) is True

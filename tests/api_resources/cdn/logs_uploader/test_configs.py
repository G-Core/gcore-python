# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn import LogsUploaderValidation
from gcore.types.cdn.logs_uploader import (
    LogsUploaderConfig,
    LogsUploaderConfigList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        config = client.cdn.logs_uploader.configs.create(
            name="name",
            policy=0,
            target=0,
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        config = client.cdn.logs_uploader.configs.create(
            name="name",
            policy=0,
            target=0,
            enabled=True,
            for_all_resources=True,
            resources=[0],
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.configs.with_raw_response.create(
            name="name",
            policy=0,
            target=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.configs.with_streaming_response.create(
            name="name",
            policy=0,
            target=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(LogsUploaderConfig, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        config = client.cdn.logs_uploader.configs.update(
            id=0,
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        config = client.cdn.logs_uploader.configs.update(
            id=0,
            enabled=True,
            for_all_resources=True,
            name="name",
            policy=0,
            resources=[0],
            target=0,
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.configs.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.configs.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(LogsUploaderConfig, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        config = client.cdn.logs_uploader.configs.list()
        assert_matches_type(LogsUploaderConfigList, config, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        config = client.cdn.logs_uploader.configs.list(
            resource_ids=[0],
            search="search",
        )
        assert_matches_type(LogsUploaderConfigList, config, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.configs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(LogsUploaderConfigList, config, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.configs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(LogsUploaderConfigList, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        config = client.cdn.logs_uploader.configs.delete(
            0,
        )
        assert config is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.configs.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert config is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.configs.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert config is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        config = client.cdn.logs_uploader.configs.get(
            0,
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.configs.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.configs.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(LogsUploaderConfig, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        config = client.cdn.logs_uploader.configs.replace(
            id=0,
            name="name",
            policy=0,
            target=0,
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        config = client.cdn.logs_uploader.configs.replace(
            id=0,
            name="name",
            policy=0,
            target=0,
            enabled=True,
            for_all_resources=True,
            resources=[0],
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.configs.with_raw_response.replace(
            id=0,
            name="name",
            policy=0,
            target=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.configs.with_streaming_response.replace(
            id=0,
            name="name",
            policy=0,
            target=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(LogsUploaderConfig, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_validate(self, client: Gcore) -> None:
        config = client.cdn.logs_uploader.configs.validate(
            0,
        )
        assert_matches_type(LogsUploaderValidation, config, path=["response"])

    @parametrize
    def test_raw_response_validate(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.configs.with_raw_response.validate(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(LogsUploaderValidation, config, path=["response"])

    @parametrize
    def test_streaming_response_validate(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.configs.with_streaming_response.validate(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(LogsUploaderValidation, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        config = await async_client.cdn.logs_uploader.configs.create(
            name="name",
            policy=0,
            target=0,
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        config = await async_client.cdn.logs_uploader.configs.create(
            name="name",
            policy=0,
            target=0,
            enabled=True,
            for_all_resources=True,
            resources=[0],
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.configs.with_raw_response.create(
            name="name",
            policy=0,
            target=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.configs.with_streaming_response.create(
            name="name",
            policy=0,
            target=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(LogsUploaderConfig, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        config = await async_client.cdn.logs_uploader.configs.update(
            id=0,
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        config = await async_client.cdn.logs_uploader.configs.update(
            id=0,
            enabled=True,
            for_all_resources=True,
            name="name",
            policy=0,
            resources=[0],
            target=0,
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.configs.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.configs.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(LogsUploaderConfig, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        config = await async_client.cdn.logs_uploader.configs.list()
        assert_matches_type(LogsUploaderConfigList, config, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        config = await async_client.cdn.logs_uploader.configs.list(
            resource_ids=[0],
            search="search",
        )
        assert_matches_type(LogsUploaderConfigList, config, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.configs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(LogsUploaderConfigList, config, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.configs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(LogsUploaderConfigList, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        config = await async_client.cdn.logs_uploader.configs.delete(
            0,
        )
        assert config is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.configs.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert config is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.configs.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert config is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        config = await async_client.cdn.logs_uploader.configs.get(
            0,
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.configs.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.configs.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(LogsUploaderConfig, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        config = await async_client.cdn.logs_uploader.configs.replace(
            id=0,
            name="name",
            policy=0,
            target=0,
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        config = await async_client.cdn.logs_uploader.configs.replace(
            id=0,
            name="name",
            policy=0,
            target=0,
            enabled=True,
            for_all_resources=True,
            resources=[0],
        )
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.configs.with_raw_response.replace(
            id=0,
            name="name",
            policy=0,
            target=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(LogsUploaderConfig, config, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.configs.with_streaming_response.replace(
            id=0,
            name="name",
            policy=0,
            target=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(LogsUploaderConfig, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_validate(self, async_client: AsyncGcore) -> None:
        config = await async_client.cdn.logs_uploader.configs.validate(
            0,
        )
        assert_matches_type(LogsUploaderValidation, config, path=["response"])

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.configs.with_raw_response.validate(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(LogsUploaderValidation, config, path=["response"])

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.configs.with_streaming_response.validate(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(LogsUploaderValidation, config, path=["response"])

        assert cast(Any, response.is_closed) is True

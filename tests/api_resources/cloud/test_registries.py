# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import Registry, RegistryList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegistries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        registry = client.cloud.registries.create(
            project_id=0,
            region_id=0,
            name="reg-home1",
        )
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        registry = client.cloud.registries.create(
            project_id=0,
            region_id=0,
            name="reg-home1",
            storage_limit=5,
        )
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.registries.with_raw_response.create(
            project_id=0,
            region_id=0,
            name="reg-home1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = response.parse()
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.registries.with_streaming_response.create(
            project_id=0,
            region_id=0,
            name="reg-home1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = response.parse()
            assert_matches_type(Registry, registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        registry = client.cloud.registries.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(RegistryList, registry, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.registries.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = response.parse()
        assert_matches_type(RegistryList, registry, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.registries.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = response.parse()
            assert_matches_type(RegistryList, registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        registry = client.cloud.registries.delete(
            registry_id=0,
            project_id=0,
            region_id=0,
        )
        assert registry is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.registries.with_raw_response.delete(
            registry_id=0,
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = response.parse()
        assert registry is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.registries.with_streaming_response.delete(
            registry_id=0,
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = response.parse()
            assert registry is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        registry = client.cloud.registries.get(
            registry_id=0,
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.registries.with_raw_response.get(
            registry_id=0,
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = response.parse()
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.registries.with_streaming_response.get(
            registry_id=0,
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = response.parse()
            assert_matches_type(Registry, registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_resize(self, client: Gcore) -> None:
        registry = client.cloud.registries.resize(
            registry_id=0,
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    def test_method_resize_with_all_params(self, client: Gcore) -> None:
        registry = client.cloud.registries.resize(
            registry_id=0,
            project_id=0,
            region_id=0,
            storage_limit=5,
        )
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    def test_raw_response_resize(self, client: Gcore) -> None:
        response = client.cloud.registries.with_raw_response.resize(
            registry_id=0,
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = response.parse()
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    def test_streaming_response_resize(self, client: Gcore) -> None:
        with client.cloud.registries.with_streaming_response.resize(
            registry_id=0,
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = response.parse()
            assert_matches_type(Registry, registry, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRegistries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        registry = await async_client.cloud.registries.create(
            project_id=0,
            region_id=0,
            name="reg-home1",
        )
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        registry = await async_client.cloud.registries.create(
            project_id=0,
            region_id=0,
            name="reg-home1",
            storage_limit=5,
        )
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.with_raw_response.create(
            project_id=0,
            region_id=0,
            name="reg-home1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = await response.parse()
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.with_streaming_response.create(
            project_id=0,
            region_id=0,
            name="reg-home1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = await response.parse()
            assert_matches_type(Registry, registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        registry = await async_client.cloud.registries.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(RegistryList, registry, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = await response.parse()
        assert_matches_type(RegistryList, registry, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = await response.parse()
            assert_matches_type(RegistryList, registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        registry = await async_client.cloud.registries.delete(
            registry_id=0,
            project_id=0,
            region_id=0,
        )
        assert registry is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.with_raw_response.delete(
            registry_id=0,
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = await response.parse()
        assert registry is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.with_streaming_response.delete(
            registry_id=0,
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = await response.parse()
            assert registry is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        registry = await async_client.cloud.registries.get(
            registry_id=0,
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.with_raw_response.get(
            registry_id=0,
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = await response.parse()
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.with_streaming_response.get(
            registry_id=0,
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = await response.parse()
            assert_matches_type(Registry, registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_resize(self, async_client: AsyncGcore) -> None:
        registry = await async_client.cloud.registries.resize(
            registry_id=0,
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    async def test_method_resize_with_all_params(self, async_client: AsyncGcore) -> None:
        registry = await async_client.cloud.registries.resize(
            registry_id=0,
            project_id=0,
            region_id=0,
            storage_limit=5,
        )
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    async def test_raw_response_resize(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.with_raw_response.resize(
            registry_id=0,
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = await response.parse()
        assert_matches_type(Registry, registry, path=["response"])

    @parametrize
    async def test_streaming_response_resize(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.with_streaming_response.resize(
            registry_id=0,
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = await response.parse()
            assert_matches_type(Registry, registry, path=["response"])

        assert cast(Any, response.is_closed) is True

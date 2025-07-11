# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.fastedge import (
    KvStore,
    KvStoreGetResponse,
    KvStoreListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKvStores:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        kv_store = client.fastedge.kv_stores.create()
        assert_matches_type(KvStore, kv_store, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        kv_store = client.fastedge.kv_stores.create(
            byod={
                "prefix": "prefix",
                "url": "url",
            },
            comment="comment",
        )
        assert_matches_type(KvStore, kv_store, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.fastedge.kv_stores.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kv_store = response.parse()
        assert_matches_type(KvStore, kv_store, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.fastedge.kv_stores.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kv_store = response.parse()
            assert_matches_type(KvStore, kv_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        kv_store = client.fastedge.kv_stores.list()
        assert_matches_type(KvStoreListResponse, kv_store, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        kv_store = client.fastedge.kv_stores.list(
            app_id=0,
        )
        assert_matches_type(KvStoreListResponse, kv_store, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.fastedge.kv_stores.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kv_store = response.parse()
        assert_matches_type(KvStoreListResponse, kv_store, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.fastedge.kv_stores.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kv_store = response.parse()
            assert_matches_type(KvStoreListResponse, kv_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        kv_store = client.fastedge.kv_stores.delete(
            0,
        )
        assert kv_store is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.fastedge.kv_stores.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kv_store = response.parse()
        assert kv_store is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.fastedge.kv_stores.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kv_store = response.parse()
            assert kv_store is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        kv_store = client.fastedge.kv_stores.get(
            0,
        )
        assert_matches_type(KvStoreGetResponse, kv_store, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.fastedge.kv_stores.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kv_store = response.parse()
        assert_matches_type(KvStoreGetResponse, kv_store, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.fastedge.kv_stores.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kv_store = response.parse()
            assert_matches_type(KvStoreGetResponse, kv_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        kv_store = client.fastedge.kv_stores.replace(
            id=0,
        )
        assert_matches_type(KvStore, kv_store, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        kv_store = client.fastedge.kv_stores.replace(
            id=0,
            byod={
                "prefix": "prefix",
                "url": "url",
            },
            comment="comment",
        )
        assert_matches_type(KvStore, kv_store, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.fastedge.kv_stores.with_raw_response.replace(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kv_store = response.parse()
        assert_matches_type(KvStore, kv_store, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.fastedge.kv_stores.with_streaming_response.replace(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kv_store = response.parse()
            assert_matches_type(KvStore, kv_store, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKvStores:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        kv_store = await async_client.fastedge.kv_stores.create()
        assert_matches_type(KvStore, kv_store, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        kv_store = await async_client.fastedge.kv_stores.create(
            byod={
                "prefix": "prefix",
                "url": "url",
            },
            comment="comment",
        )
        assert_matches_type(KvStore, kv_store, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.kv_stores.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kv_store = await response.parse()
        assert_matches_type(KvStore, kv_store, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.kv_stores.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kv_store = await response.parse()
            assert_matches_type(KvStore, kv_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        kv_store = await async_client.fastedge.kv_stores.list()
        assert_matches_type(KvStoreListResponse, kv_store, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        kv_store = await async_client.fastedge.kv_stores.list(
            app_id=0,
        )
        assert_matches_type(KvStoreListResponse, kv_store, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.kv_stores.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kv_store = await response.parse()
        assert_matches_type(KvStoreListResponse, kv_store, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.kv_stores.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kv_store = await response.parse()
            assert_matches_type(KvStoreListResponse, kv_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        kv_store = await async_client.fastedge.kv_stores.delete(
            0,
        )
        assert kv_store is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.kv_stores.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kv_store = await response.parse()
        assert kv_store is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.kv_stores.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kv_store = await response.parse()
            assert kv_store is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        kv_store = await async_client.fastedge.kv_stores.get(
            0,
        )
        assert_matches_type(KvStoreGetResponse, kv_store, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.kv_stores.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kv_store = await response.parse()
        assert_matches_type(KvStoreGetResponse, kv_store, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.kv_stores.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kv_store = await response.parse()
            assert_matches_type(KvStoreGetResponse, kv_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        kv_store = await async_client.fastedge.kv_stores.replace(
            id=0,
        )
        assert_matches_type(KvStore, kv_store, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        kv_store = await async_client.fastedge.kv_stores.replace(
            id=0,
            byod={
                "prefix": "prefix",
                "url": "url",
            },
            comment="comment",
        )
        assert_matches_type(KvStore, kv_store, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.kv_stores.with_raw_response.replace(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kv_store = await response.parse()
        assert_matches_type(KvStore, kv_store, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.kv_stores.with_streaming_response.replace(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kv_store = await response.parse()
            assert_matches_type(KvStore, kv_store, path=["response"])

        assert cast(Any, response.is_closed) is True

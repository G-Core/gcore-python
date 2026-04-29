# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.storage.object_storages import AccessKey, AccessKeyCreated

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        access_key = client.storage.object_storages.access_keys.create(
            0,
        )
        assert_matches_type(AccessKeyCreated, access_key, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.storage.object_storages.access_keys.with_raw_response.create(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = response.parse()
        assert_matches_type(AccessKeyCreated, access_key, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.storage.object_storages.access_keys.with_streaming_response.create(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = response.parse()
            assert_matches_type(AccessKeyCreated, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        access_key = client.storage.object_storages.access_keys.list(
            storage_id=0,
        )
        assert_matches_type(SyncOffsetPage[AccessKey], access_key, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        access_key = client.storage.object_storages.access_keys.list(
            storage_id=0,
            limit=1,
            offset=0,
            order_by="order_by",
        )
        assert_matches_type(SyncOffsetPage[AccessKey], access_key, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.storage.object_storages.access_keys.with_raw_response.list(
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = response.parse()
        assert_matches_type(SyncOffsetPage[AccessKey], access_key, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.storage.object_storages.access_keys.with_streaming_response.list(
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = response.parse()
            assert_matches_type(SyncOffsetPage[AccessKey], access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        access_key = client.storage.object_storages.access_keys.delete(
            access_key="access_key",
            storage_id=0,
        )
        assert access_key is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.storage.object_storages.access_keys.with_raw_response.delete(
            access_key="access_key",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = response.parse()
        assert access_key is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.storage.object_storages.access_keys.with_streaming_response.delete(
            access_key="access_key",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = response.parse()
            assert access_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_key` but received ''"):
            client.storage.object_storages.access_keys.with_raw_response.delete(
                access_key="",
                storage_id=0,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        access_key = client.storage.object_storages.access_keys.get(
            access_key="access_key",
            storage_id=0,
        )
        assert_matches_type(AccessKey, access_key, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.storage.object_storages.access_keys.with_raw_response.get(
            access_key="access_key",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = response.parse()
        assert_matches_type(AccessKey, access_key, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.storage.object_storages.access_keys.with_streaming_response.get(
            access_key="access_key",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = response.parse()
            assert_matches_type(AccessKey, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_key` but received ''"):
            client.storage.object_storages.access_keys.with_raw_response.get(
                access_key="",
                storage_id=0,
            )


class TestAsyncAccessKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        access_key = await async_client.storage.object_storages.access_keys.create(
            0,
        )
        assert_matches_type(AccessKeyCreated, access_key, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.object_storages.access_keys.with_raw_response.create(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = await response.parse()
        assert_matches_type(AccessKeyCreated, access_key, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.object_storages.access_keys.with_streaming_response.create(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = await response.parse()
            assert_matches_type(AccessKeyCreated, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        access_key = await async_client.storage.object_storages.access_keys.list(
            storage_id=0,
        )
        assert_matches_type(AsyncOffsetPage[AccessKey], access_key, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        access_key = await async_client.storage.object_storages.access_keys.list(
            storage_id=0,
            limit=1,
            offset=0,
            order_by="order_by",
        )
        assert_matches_type(AsyncOffsetPage[AccessKey], access_key, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.object_storages.access_keys.with_raw_response.list(
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = await response.parse()
        assert_matches_type(AsyncOffsetPage[AccessKey], access_key, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.object_storages.access_keys.with_streaming_response.list(
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = await response.parse()
            assert_matches_type(AsyncOffsetPage[AccessKey], access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        access_key = await async_client.storage.object_storages.access_keys.delete(
            access_key="access_key",
            storage_id=0,
        )
        assert access_key is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.object_storages.access_keys.with_raw_response.delete(
            access_key="access_key",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = await response.parse()
        assert access_key is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.object_storages.access_keys.with_streaming_response.delete(
            access_key="access_key",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = await response.parse()
            assert access_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_key` but received ''"):
            await async_client.storage.object_storages.access_keys.with_raw_response.delete(
                access_key="",
                storage_id=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        access_key = await async_client.storage.object_storages.access_keys.get(
            access_key="access_key",
            storage_id=0,
        )
        assert_matches_type(AccessKey, access_key, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.object_storages.access_keys.with_raw_response.get(
            access_key="access_key",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = await response.parse()
        assert_matches_type(AccessKey, access_key, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.object_storages.access_keys.with_streaming_response.get(
            access_key="access_key",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = await response.parse()
            assert_matches_type(AccessKey, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_key` but received ''"):
            await async_client.storage.object_storages.access_keys.with_raw_response.get(
                access_key="",
                storage_id=0,
            )

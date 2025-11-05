# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.storage import (
    Storage,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStorage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        storage = client.storage.create(
            location="s-region-1",
            name="my-storage-prod",
            type="s3",
        )
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        storage = client.storage.create(
            location="s-region-1",
            name="my-storage-prod",
            type="s3",
            generate_sftp_password=True,
            sftp_password="sftp_password",
        )
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.storage.with_raw_response.create(
            location="s-region-1",
            name="my-storage-prod",
            type="s3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = response.parse()
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.storage.with_streaming_response.create(
            location="s-region-1",
            name="my-storage-prod",
            type="s3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = response.parse()
            assert_matches_type(Storage, storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        storage = client.storage.update(
            storage_id=0,
        )
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        storage = client.storage.update(
            storage_id=0,
            expires="1 years 6 months",
            server_alias="my-storage.company.com",
        )
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.storage.with_raw_response.update(
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = response.parse()
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.storage.with_streaming_response.update(
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = response.parse()
            assert_matches_type(Storage, storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        storage = client.storage.list()
        assert_matches_type(SyncOffsetPage[Storage], storage, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        storage = client.storage.list(
            id="id",
            limit=1,
            location="location",
            name="name",
            offset=0,
            order_by="order_by",
            order_direction="asc",
            show_deleted=True,
            status="active",
            type="s3",
        )
        assert_matches_type(SyncOffsetPage[Storage], storage, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.storage.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = response.parse()
        assert_matches_type(SyncOffsetPage[Storage], storage, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.storage.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = response.parse()
            assert_matches_type(SyncOffsetPage[Storage], storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        storage = client.storage.delete(
            0,
        )
        assert storage is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.storage.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = response.parse()
        assert storage is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.storage.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = response.parse()
            assert storage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        storage = client.storage.get(
            0,
        )
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.storage.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = response.parse()
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.storage.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = response.parse()
            assert_matches_type(Storage, storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_link_ssh_key(self, client: Gcore) -> None:
        storage = client.storage.link_ssh_key(
            key_id=0,
            storage_id=0,
        )
        assert storage is None

    @parametrize
    def test_raw_response_link_ssh_key(self, client: Gcore) -> None:
        response = client.storage.with_raw_response.link_ssh_key(
            key_id=0,
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = response.parse()
        assert storage is None

    @parametrize
    def test_streaming_response_link_ssh_key(self, client: Gcore) -> None:
        with client.storage.with_streaming_response.link_ssh_key(
            key_id=0,
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = response.parse()
            assert storage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_restore(self, client: Gcore) -> None:
        storage = client.storage.restore(
            storage_id=0,
        )
        assert storage is None

    @parametrize
    def test_method_restore_with_all_params(self, client: Gcore) -> None:
        storage = client.storage.restore(
            storage_id=0,
            client_id=0,
        )
        assert storage is None

    @parametrize
    def test_raw_response_restore(self, client: Gcore) -> None:
        response = client.storage.with_raw_response.restore(
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = response.parse()
        assert storage is None

    @parametrize
    def test_streaming_response_restore(self, client: Gcore) -> None:
        with client.storage.with_streaming_response.restore(
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = response.parse()
            assert storage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unlink_ssh_key(self, client: Gcore) -> None:
        storage = client.storage.unlink_ssh_key(
            key_id=0,
            storage_id=0,
        )
        assert storage is None

    @parametrize
    def test_raw_response_unlink_ssh_key(self, client: Gcore) -> None:
        response = client.storage.with_raw_response.unlink_ssh_key(
            key_id=0,
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = response.parse()
        assert storage is None

    @parametrize
    def test_streaming_response_unlink_ssh_key(self, client: Gcore) -> None:
        with client.storage.with_streaming_response.unlink_ssh_key(
            key_id=0,
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = response.parse()
            assert storage is None

        assert cast(Any, response.is_closed) is True


class TestAsyncStorage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        storage = await async_client.storage.create(
            location="s-region-1",
            name="my-storage-prod",
            type="s3",
        )
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        storage = await async_client.storage.create(
            location="s-region-1",
            name="my-storage-prod",
            type="s3",
            generate_sftp_password=True,
            sftp_password="sftp_password",
        )
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.with_raw_response.create(
            location="s-region-1",
            name="my-storage-prod",
            type="s3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = await response.parse()
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.with_streaming_response.create(
            location="s-region-1",
            name="my-storage-prod",
            type="s3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = await response.parse()
            assert_matches_type(Storage, storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        storage = await async_client.storage.update(
            storage_id=0,
        )
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        storage = await async_client.storage.update(
            storage_id=0,
            expires="1 years 6 months",
            server_alias="my-storage.company.com",
        )
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.with_raw_response.update(
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = await response.parse()
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.with_streaming_response.update(
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = await response.parse()
            assert_matches_type(Storage, storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        storage = await async_client.storage.list()
        assert_matches_type(AsyncOffsetPage[Storage], storage, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        storage = await async_client.storage.list(
            id="id",
            limit=1,
            location="location",
            name="name",
            offset=0,
            order_by="order_by",
            order_direction="asc",
            show_deleted=True,
            status="active",
            type="s3",
        )
        assert_matches_type(AsyncOffsetPage[Storage], storage, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = await response.parse()
        assert_matches_type(AsyncOffsetPage[Storage], storage, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = await response.parse()
            assert_matches_type(AsyncOffsetPage[Storage], storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        storage = await async_client.storage.delete(
            0,
        )
        assert storage is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = await response.parse()
        assert storage is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = await response.parse()
            assert storage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        storage = await async_client.storage.get(
            0,
        )
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = await response.parse()
        assert_matches_type(Storage, storage, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = await response.parse()
            assert_matches_type(Storage, storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_link_ssh_key(self, async_client: AsyncGcore) -> None:
        storage = await async_client.storage.link_ssh_key(
            key_id=0,
            storage_id=0,
        )
        assert storage is None

    @parametrize
    async def test_raw_response_link_ssh_key(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.with_raw_response.link_ssh_key(
            key_id=0,
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = await response.parse()
        assert storage is None

    @parametrize
    async def test_streaming_response_link_ssh_key(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.with_streaming_response.link_ssh_key(
            key_id=0,
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = await response.parse()
            assert storage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_restore(self, async_client: AsyncGcore) -> None:
        storage = await async_client.storage.restore(
            storage_id=0,
        )
        assert storage is None

    @parametrize
    async def test_method_restore_with_all_params(self, async_client: AsyncGcore) -> None:
        storage = await async_client.storage.restore(
            storage_id=0,
            client_id=0,
        )
        assert storage is None

    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.with_raw_response.restore(
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = await response.parse()
        assert storage is None

    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.with_streaming_response.restore(
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = await response.parse()
            assert storage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unlink_ssh_key(self, async_client: AsyncGcore) -> None:
        storage = await async_client.storage.unlink_ssh_key(
            key_id=0,
            storage_id=0,
        )
        assert storage is None

    @parametrize
    async def test_raw_response_unlink_ssh_key(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.with_raw_response.unlink_ssh_key(
            key_id=0,
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = await response.parse()
        assert storage is None

    @parametrize
    async def test_streaming_response_unlink_ssh_key(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.with_streaming_response.unlink_ssh_key(
            key_id=0,
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = await response.parse()
            assert storage is None

        assert cast(Any, response.is_closed) is True

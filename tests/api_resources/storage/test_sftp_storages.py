# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.storage import (
    SftpStorage,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSftpStorages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        sftp_storage = client.storage.sftp_storages.create(
            location_name="mia",
            name="my-sftp-storage",
            password_mode="auto",
        )
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        sftp_storage = client.storage.sftp_storages.create(
            location_name="mia",
            name="my-sftp-storage",
            password_mode="auto",
            expires="2 years 6 months",
            has_custom_config_file=False,
            is_http_disabled=False,
            server_alias="my-storage.example.com",
            sftp_password="sftp_password",
            ssh_key_ids=[1, 2, 3],
        )
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.storage.sftp_storages.with_raw_response.create(
            location_name="mia",
            name="my-sftp-storage",
            password_mode="auto",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sftp_storage = response.parse()
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.storage.sftp_storages.with_streaming_response.create(
            location_name="mia",
            name="my-sftp-storage",
            password_mode="auto",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sftp_storage = response.parse()
            assert_matches_type(SftpStorage, sftp_storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        sftp_storage = client.storage.sftp_storages.update(
            storage_id=0,
        )
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        sftp_storage = client.storage.sftp_storages.update(
            storage_id=0,
            expires="2 years 6 months",
            has_custom_config_file=False,
            is_http_disabled=False,
            password_mode="auto",
            server_alias="my-storage.example.com",
            ssh_key_ids=[1, 2, 3],
        )
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.storage.sftp_storages.with_raw_response.update(
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sftp_storage = response.parse()
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.storage.sftp_storages.with_streaming_response.update(
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sftp_storage = response.parse()
            assert_matches_type(SftpStorage, sftp_storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        sftp_storage = client.storage.sftp_storages.list()
        assert_matches_type(SyncOffsetPage[SftpStorage], sftp_storage, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        sftp_storage = client.storage.sftp_storages.list(
            id="id",
            limit=1,
            location_name="location_name",
            name="name",
            offset=0,
            order_by="order_by",
            provisioning_status="active",
            show_deleted=True,
        )
        assert_matches_type(SyncOffsetPage[SftpStorage], sftp_storage, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.storage.sftp_storages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sftp_storage = response.parse()
        assert_matches_type(SyncOffsetPage[SftpStorage], sftp_storage, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.storage.sftp_storages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sftp_storage = response.parse()
            assert_matches_type(SyncOffsetPage[SftpStorage], sftp_storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        sftp_storage = client.storage.sftp_storages.delete(
            0,
        )
        assert sftp_storage is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.storage.sftp_storages.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sftp_storage = response.parse()
        assert sftp_storage is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.storage.sftp_storages.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sftp_storage = response.parse()
            assert sftp_storage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        sftp_storage = client.storage.sftp_storages.get(
            0,
        )
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.storage.sftp_storages.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sftp_storage = response.parse()
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.storage.sftp_storages.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sftp_storage = response.parse()
            assert_matches_type(SftpStorage, sftp_storage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSftpStorages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        sftp_storage = await async_client.storage.sftp_storages.create(
            location_name="mia",
            name="my-sftp-storage",
            password_mode="auto",
        )
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        sftp_storage = await async_client.storage.sftp_storages.create(
            location_name="mia",
            name="my-sftp-storage",
            password_mode="auto",
            expires="2 years 6 months",
            has_custom_config_file=False,
            is_http_disabled=False,
            server_alias="my-storage.example.com",
            sftp_password="sftp_password",
            ssh_key_ids=[1, 2, 3],
        )
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.sftp_storages.with_raw_response.create(
            location_name="mia",
            name="my-sftp-storage",
            password_mode="auto",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sftp_storage = await response.parse()
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.sftp_storages.with_streaming_response.create(
            location_name="mia",
            name="my-sftp-storage",
            password_mode="auto",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sftp_storage = await response.parse()
            assert_matches_type(SftpStorage, sftp_storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        sftp_storage = await async_client.storage.sftp_storages.update(
            storage_id=0,
        )
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        sftp_storage = await async_client.storage.sftp_storages.update(
            storage_id=0,
            expires="2 years 6 months",
            has_custom_config_file=False,
            is_http_disabled=False,
            password_mode="auto",
            server_alias="my-storage.example.com",
            ssh_key_ids=[1, 2, 3],
        )
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.sftp_storages.with_raw_response.update(
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sftp_storage = await response.parse()
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.sftp_storages.with_streaming_response.update(
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sftp_storage = await response.parse()
            assert_matches_type(SftpStorage, sftp_storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        sftp_storage = await async_client.storage.sftp_storages.list()
        assert_matches_type(AsyncOffsetPage[SftpStorage], sftp_storage, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        sftp_storage = await async_client.storage.sftp_storages.list(
            id="id",
            limit=1,
            location_name="location_name",
            name="name",
            offset=0,
            order_by="order_by",
            provisioning_status="active",
            show_deleted=True,
        )
        assert_matches_type(AsyncOffsetPage[SftpStorage], sftp_storage, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.sftp_storages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sftp_storage = await response.parse()
        assert_matches_type(AsyncOffsetPage[SftpStorage], sftp_storage, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.sftp_storages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sftp_storage = await response.parse()
            assert_matches_type(AsyncOffsetPage[SftpStorage], sftp_storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        sftp_storage = await async_client.storage.sftp_storages.delete(
            0,
        )
        assert sftp_storage is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.sftp_storages.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sftp_storage = await response.parse()
        assert sftp_storage is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.sftp_storages.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sftp_storage = await response.parse()
            assert sftp_storage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        sftp_storage = await async_client.storage.sftp_storages.get(
            0,
        )
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.sftp_storages.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sftp_storage = await response.parse()
        assert_matches_type(SftpStorage, sftp_storage, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.sftp_storages.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sftp_storage = await response.parse()
            assert_matches_type(SftpStorage, sftp_storage, path=["response"])

        assert cast(Any, response.is_closed) is True

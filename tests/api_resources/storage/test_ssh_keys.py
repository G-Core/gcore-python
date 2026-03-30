# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.storage import SSHKey

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSSHKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        ssh_key = client.storage.ssh_keys.create(
            name="my-production-key",
            public_key="ssh-rsa AAAAB3NzaC1yc2EAAA... user@example.com",
        )
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.storage.ssh_keys.with_raw_response.create(
            name="my-production-key",
            public_key="ssh-rsa AAAAB3NzaC1yc2EAAA... user@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = response.parse()
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.storage.ssh_keys.with_streaming_response.create(
            name="my-production-key",
            public_key="ssh-rsa AAAAB3NzaC1yc2EAAA... user@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = response.parse()
            assert_matches_type(SSHKey, ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        ssh_key = client.storage.ssh_keys.list()
        assert_matches_type(SyncOffsetPage[SSHKey], ssh_key, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        ssh_key = client.storage.ssh_keys.list(
            limit=1,
            name="name",
            offset=0,
            order_by="order_by",
        )
        assert_matches_type(SyncOffsetPage[SSHKey], ssh_key, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.storage.ssh_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = response.parse()
        assert_matches_type(SyncOffsetPage[SSHKey], ssh_key, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.storage.ssh_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = response.parse()
            assert_matches_type(SyncOffsetPage[SSHKey], ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        ssh_key = client.storage.ssh_keys.delete(
            0,
        )
        assert ssh_key is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.storage.ssh_keys.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = response.parse()
        assert ssh_key is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.storage.ssh_keys.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = response.parse()
            assert ssh_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        ssh_key = client.storage.ssh_keys.get(
            0,
        )
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.storage.ssh_keys.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = response.parse()
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.storage.ssh_keys.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = response.parse()
            assert_matches_type(SSHKey, ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSSHKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        ssh_key = await async_client.storage.ssh_keys.create(
            name="my-production-key",
            public_key="ssh-rsa AAAAB3NzaC1yc2EAAA... user@example.com",
        )
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.ssh_keys.with_raw_response.create(
            name="my-production-key",
            public_key="ssh-rsa AAAAB3NzaC1yc2EAAA... user@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = await response.parse()
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.ssh_keys.with_streaming_response.create(
            name="my-production-key",
            public_key="ssh-rsa AAAAB3NzaC1yc2EAAA... user@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = await response.parse()
            assert_matches_type(SSHKey, ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        ssh_key = await async_client.storage.ssh_keys.list()
        assert_matches_type(AsyncOffsetPage[SSHKey], ssh_key, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        ssh_key = await async_client.storage.ssh_keys.list(
            limit=1,
            name="name",
            offset=0,
            order_by="order_by",
        )
        assert_matches_type(AsyncOffsetPage[SSHKey], ssh_key, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.ssh_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = await response.parse()
        assert_matches_type(AsyncOffsetPage[SSHKey], ssh_key, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.ssh_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = await response.parse()
            assert_matches_type(AsyncOffsetPage[SSHKey], ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        ssh_key = await async_client.storage.ssh_keys.delete(
            0,
        )
        assert ssh_key is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.ssh_keys.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = await response.parse()
        assert ssh_key is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.ssh_keys.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = await response.parse()
            assert ssh_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        ssh_key = await async_client.storage.ssh_keys.get(
            0,
        )
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.ssh_keys.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = await response.parse()
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.ssh_keys.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = await response.parse()
            assert_matches_type(SSHKey, ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True

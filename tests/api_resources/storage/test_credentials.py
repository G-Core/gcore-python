# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.storage import Storage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_recreate(self, client: Gcore) -> None:
        credential = client.storage.credentials.recreate(
            storage_id=0,
        )
        assert_matches_type(Storage, credential, path=["response"])

    @parametrize
    def test_method_recreate_with_all_params(self, client: Gcore) -> None:
        credential = client.storage.credentials.recreate(
            storage_id=0,
            delete_sftp_password=True,
            generate_s3_keys=True,
            generate_sftp_password=True,
            reset_sftp_keys=True,
            sftp_password="sftp_password",
        )
        assert_matches_type(Storage, credential, path=["response"])

    @parametrize
    def test_raw_response_recreate(self, client: Gcore) -> None:
        response = client.storage.credentials.with_raw_response.recreate(
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(Storage, credential, path=["response"])

    @parametrize
    def test_streaming_response_recreate(self, client: Gcore) -> None:
        with client.storage.credentials.with_streaming_response.recreate(
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(Storage, credential, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_recreate(self, async_client: AsyncGcore) -> None:
        credential = await async_client.storage.credentials.recreate(
            storage_id=0,
        )
        assert_matches_type(Storage, credential, path=["response"])

    @parametrize
    async def test_method_recreate_with_all_params(self, async_client: AsyncGcore) -> None:
        credential = await async_client.storage.credentials.recreate(
            storage_id=0,
            delete_sftp_password=True,
            generate_s3_keys=True,
            generate_sftp_password=True,
            reset_sftp_keys=True,
            sftp_password="sftp_password",
        )
        assert_matches_type(Storage, credential, path=["response"])

    @parametrize
    async def test_raw_response_recreate(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.credentials.with_raw_response.recreate(
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(Storage, credential, path=["response"])

    @parametrize
    async def test_streaming_response_recreate(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.credentials.with_streaming_response.recreate(
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(Storage, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

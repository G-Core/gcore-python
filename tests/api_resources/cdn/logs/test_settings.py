# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn.logs import LogSettings

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        setting = client.cdn.logs.settings.create(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[{}],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
        )
        assert setting is None

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        setting = client.cdn.logs.settings.create(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[
                {
                    "id": 0,
                    "bucket": "bucket",
                    "cdn_resource": 0,
                    "folder": "folder",
                }
            ],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
            archive_size_mb=500,
            enabled=True,
            ftp_prepend_folder="ftp_prepend_folder",
            ignore_empty_logs=True,
            s3_aws_region=0,
            s3_bucket_location="s3_bucket_location",
            s3_host_bucket="s3_host_bucket",
            sftp_key_passphrase="sftp_key_passphrase",
            sftp_prepend_folder="sftp_prepend_folder",
            sftp_private_key="sftp_private_key",
        )
        assert setting is None

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cdn.logs.settings.with_raw_response.create(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[{}],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cdn.logs.settings.with_streaming_response.create(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[{}],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        setting = client.cdn.logs.settings.update(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[{}],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
        )
        assert setting is None

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        setting = client.cdn.logs.settings.update(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[
                {
                    "id": 0,
                    "bucket": "bucket",
                    "cdn_resource": 0,
                    "folder": "folder",
                }
            ],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
            archive_size_mb=500,
            enabled=True,
            ftp_prepend_folder="ftp_prepend_folder",
            ignore_empty_logs=True,
            s3_aws_region=0,
            s3_bucket_location="s3_bucket_location",
            s3_host_bucket="s3_host_bucket",
            sftp_key_passphrase="sftp_key_passphrase",
            sftp_prepend_folder="sftp_prepend_folder",
            sftp_private_key="sftp_private_key",
        )
        assert setting is None

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cdn.logs.settings.with_raw_response.update(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[{}],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cdn.logs.settings.with_streaming_response.update(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[{}],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        setting = client.cdn.logs.settings.delete()
        assert setting is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cdn.logs.settings.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cdn.logs.settings.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        setting = client.cdn.logs.settings.get()
        assert_matches_type(LogSettings, setting, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cdn.logs.settings.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(LogSettings, setting, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cdn.logs.settings.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(LogSettings, setting, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        setting = await async_client.cdn.logs.settings.create(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[{}],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
        )
        assert setting is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        setting = await async_client.cdn.logs.settings.create(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[
                {
                    "id": 0,
                    "bucket": "bucket",
                    "cdn_resource": 0,
                    "folder": "folder",
                }
            ],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
            archive_size_mb=500,
            enabled=True,
            ftp_prepend_folder="ftp_prepend_folder",
            ignore_empty_logs=True,
            s3_aws_region=0,
            s3_bucket_location="s3_bucket_location",
            s3_host_bucket="s3_host_bucket",
            sftp_key_passphrase="sftp_key_passphrase",
            sftp_prepend_folder="sftp_prepend_folder",
            sftp_private_key="sftp_private_key",
        )
        assert setting is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs.settings.with_raw_response.create(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[{}],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs.settings.with_streaming_response.create(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[{}],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        setting = await async_client.cdn.logs.settings.update(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[{}],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
        )
        assert setting is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        setting = await async_client.cdn.logs.settings.update(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[
                {
                    "id": 0,
                    "bucket": "bucket",
                    "cdn_resource": 0,
                    "folder": "folder",
                }
            ],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
            archive_size_mb=500,
            enabled=True,
            ftp_prepend_folder="ftp_prepend_folder",
            ignore_empty_logs=True,
            s3_aws_region=0,
            s3_bucket_location="s3_bucket_location",
            s3_host_bucket="s3_host_bucket",
            sftp_key_passphrase="sftp_key_passphrase",
            sftp_prepend_folder="sftp_prepend_folder",
            sftp_private_key="sftp_private_key",
        )
        assert setting is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs.settings.with_raw_response.update(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[{}],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs.settings.with_streaming_response.update(
            all_resources_bucket="all_resources_bucket",
            all_resources_folder="all_resources_folder",
            folders=[{}],
            for_all_resources=True,
            ftp_hostname="ftp_hostname",
            ftp_login="ftp_login",
            ftp_password="ftp_password",
            s3_access_key_id="s3_access_key_id",
            s3_hostname="s3_hostname",
            s3_secret_key="s3_secret_key",
            s3_type="s3_type",
            sftp_hostname="sftp_hostname",
            sftp_login="sftp_login",
            sftp_password="sftp_password",
            storage_type="storage_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        setting = await async_client.cdn.logs.settings.delete()
        assert setting is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs.settings.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs.settings.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        setting = await async_client.cdn.logs.settings.get()
        assert_matches_type(LogSettings, setting, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs.settings.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(LogSettings, setting, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs.settings.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(LogSettings, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

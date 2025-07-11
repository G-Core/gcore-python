# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import Secret, TaskIDList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        secret = client.cloud.secrets.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(SyncOffsetPage[Secret], secret, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        secret = client.cloud.secrets.list(
            project_id=1,
            region_id=1,
            limit=1000,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[Secret], secret, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.secrets.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SyncOffsetPage[Secret], secret, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.secrets.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SyncOffsetPage[Secret], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        secret = client.cloud.secrets.delete(
            secret_id="bfc7824b-31b6-4a28-a0c4-7df137139215",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.secrets.with_raw_response.delete(
            secret_id="bfc7824b-31b6-4a28-a0c4-7df137139215",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.secrets.with_streaming_response.delete(
            secret_id="bfc7824b-31b6-4a28-a0c4-7df137139215",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(TaskIDList, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.cloud.secrets.with_raw_response.delete(
                secret_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        secret = client.cloud.secrets.get(
            secret_id="bfc7824b-31b6-4a28-a0c4-7df137139215",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.secrets.with_raw_response.get(
            secret_id="bfc7824b-31b6-4a28-a0c4-7df137139215",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.secrets.with_streaming_response.get(
            secret_id="bfc7824b-31b6-4a28-a0c4-7df137139215",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.cloud.secrets.with_raw_response.get(
                secret_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_upload_tls_certificate(self, client: Gcore) -> None:
        secret = client.cloud.secrets.upload_tls_certificate(
            project_id=1,
            region_id=1,
            name="Load balancer certificate #1",
            payload={
                "certificate": "<certificate>",
                "certificate_chain": "<certificate_chain>",
                "private_key": "<private_key>",
            },
        )
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    def test_method_upload_tls_certificate_with_all_params(self, client: Gcore) -> None:
        secret = client.cloud.secrets.upload_tls_certificate(
            project_id=1,
            region_id=1,
            name="Load balancer certificate #1",
            payload={
                "certificate": "<certificate>",
                "certificate_chain": "<certificate_chain>",
                "private_key": "<private_key>",
            },
            expiration=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    def test_raw_response_upload_tls_certificate(self, client: Gcore) -> None:
        response = client.cloud.secrets.with_raw_response.upload_tls_certificate(
            project_id=1,
            region_id=1,
            name="Load balancer certificate #1",
            payload={
                "certificate": "<certificate>",
                "certificate_chain": "<certificate_chain>",
                "private_key": "<private_key>",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    def test_streaming_response_upload_tls_certificate(self, client: Gcore) -> None:
        with client.cloud.secrets.with_streaming_response.upload_tls_certificate(
            project_id=1,
            region_id=1,
            name="Load balancer certificate #1",
            payload={
                "certificate": "<certificate>",
                "certificate_chain": "<certificate_chain>",
                "private_key": "<private_key>",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(TaskIDList, secret, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.secrets.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(AsyncOffsetPage[Secret], secret, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.secrets.list(
            project_id=1,
            region_id=1,
            limit=1000,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[Secret], secret, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.secrets.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(AsyncOffsetPage[Secret], secret, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.secrets.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(AsyncOffsetPage[Secret], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.secrets.delete(
            secret_id="bfc7824b-31b6-4a28-a0c4-7df137139215",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.secrets.with_raw_response.delete(
            secret_id="bfc7824b-31b6-4a28-a0c4-7df137139215",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.secrets.with_streaming_response.delete(
            secret_id="bfc7824b-31b6-4a28-a0c4-7df137139215",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(TaskIDList, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.cloud.secrets.with_raw_response.delete(
                secret_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.secrets.get(
            secret_id="bfc7824b-31b6-4a28-a0c4-7df137139215",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.secrets.with_raw_response.get(
            secret_id="bfc7824b-31b6-4a28-a0c4-7df137139215",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.secrets.with_streaming_response.get(
            secret_id="bfc7824b-31b6-4a28-a0c4-7df137139215",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.cloud.secrets.with_raw_response.get(
                secret_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_upload_tls_certificate(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.secrets.upload_tls_certificate(
            project_id=1,
            region_id=1,
            name="Load balancer certificate #1",
            payload={
                "certificate": "<certificate>",
                "certificate_chain": "<certificate_chain>",
                "private_key": "<private_key>",
            },
        )
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    async def test_method_upload_tls_certificate_with_all_params(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.secrets.upload_tls_certificate(
            project_id=1,
            region_id=1,
            name="Load balancer certificate #1",
            payload={
                "certificate": "<certificate>",
                "certificate_chain": "<certificate_chain>",
                "private_key": "<private_key>",
            },
            expiration=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    async def test_raw_response_upload_tls_certificate(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.secrets.with_raw_response.upload_tls_certificate(
            project_id=1,
            region_id=1,
            name="Load balancer certificate #1",
            payload={
                "certificate": "<certificate>",
                "certificate_chain": "<certificate_chain>",
                "private_key": "<private_key>",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    async def test_streaming_response_upload_tls_certificate(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.secrets.with_streaming_response.upload_tls_certificate(
            project_id=1,
            region_id=1,
            name="Load balancer certificate #1",
            payload={
                "certificate": "<certificate>",
                "certificate_chain": "<certificate_chain>",
                "private_key": "<private_key>",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(TaskIDList, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

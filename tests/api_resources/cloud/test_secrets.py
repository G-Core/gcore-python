# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.types.cloud import (
    Secret,
    TaskIDList,
    SecretListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        secret = client.cloud.secrets.create(
            project_id=1,
            region_id=1,
            name="AES key",
            payload="aGVsbG8sIHRlc3Qgc3RyaW5nCg==",
            payload_content_encoding="base64",
            payload_content_type="application/octet-stream",
            secret_type="certificate",
        )
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        secret = client.cloud.secrets.create(
            project_id=1,
            region_id=1,
            name="AES key",
            payload="aGVsbG8sIHRlc3Qgc3RyaW5nCg==",
            payload_content_encoding="base64",
            payload_content_type="application/octet-stream",
            secret_type="certificate",
            algorithm="aes",
            bit_length=256,
            expiration="2025-12-28T19:14:44.180394",
            mode="cbc",
        )
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.secrets.with_raw_response.create(
            project_id=1,
            region_id=1,
            name="AES key",
            payload="aGVsbG8sIHRlc3Qgc3RyaW5nCg==",
            payload_content_encoding="base64",
            payload_content_type="application/octet-stream",
            secret_type="certificate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.secrets.with_streaming_response.create(
            project_id=1,
            region_id=1,
            name="AES key",
            payload="aGVsbG8sIHRlc3Qgc3RyaW5nCg==",
            payload_content_encoding="base64",
            payload_content_type="application/octet-stream",
            secret_type="certificate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(TaskIDList, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        secret = client.cloud.secrets.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.secrets.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.secrets.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.secrets.create(
            project_id=1,
            region_id=1,
            name="AES key",
            payload="aGVsbG8sIHRlc3Qgc3RyaW5nCg==",
            payload_content_encoding="base64",
            payload_content_type="application/octet-stream",
            secret_type="certificate",
        )
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.secrets.create(
            project_id=1,
            region_id=1,
            name="AES key",
            payload="aGVsbG8sIHRlc3Qgc3RyaW5nCg==",
            payload_content_encoding="base64",
            payload_content_type="application/octet-stream",
            secret_type="certificate",
            algorithm="aes",
            bit_length=256,
            expiration="2025-12-28T19:14:44.180394",
            mode="cbc",
        )
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.secrets.with_raw_response.create(
            project_id=1,
            region_id=1,
            name="AES key",
            payload="aGVsbG8sIHRlc3Qgc3RyaW5nCg==",
            payload_content_encoding="base64",
            payload_content_type="application/octet-stream",
            secret_type="certificate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(TaskIDList, secret, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.secrets.with_streaming_response.create(
            project_id=1,
            region_id=1,
            name="AES key",
            payload="aGVsbG8sIHRlc3Qgc3RyaW5nCg==",
            payload_content_encoding="base64",
            payload_content_type="application/octet-stream",
            secret_type="certificate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(TaskIDList, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.secrets.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.secrets.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.secrets.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

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

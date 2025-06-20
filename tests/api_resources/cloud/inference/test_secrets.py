# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud.inference import InferenceSecret

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        secret = client.cloud.inference.secrets.create(
            project_id=1,
            data={
                "aws_access_key_id": "fake-key-id",
                "aws_secret_access_key": "fake-secret",
            },
            name="aws-dev",
            type="aws-iam",
        )
        assert_matches_type(InferenceSecret, secret, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.inference.secrets.with_raw_response.create(
            project_id=1,
            data={
                "aws_access_key_id": "fake-key-id",
                "aws_secret_access_key": "fake-secret",
            },
            name="aws-dev",
            type="aws-iam",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(InferenceSecret, secret, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.inference.secrets.with_streaming_response.create(
            project_id=1,
            data={
                "aws_access_key_id": "fake-key-id",
                "aws_secret_access_key": "fake-secret",
            },
            name="aws-dev",
            type="aws-iam",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(InferenceSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        secret = client.cloud.inference.secrets.list(
            project_id=1,
        )
        assert_matches_type(SyncOffsetPage[InferenceSecret], secret, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        secret = client.cloud.inference.secrets.list(
            project_id=1,
            limit=1000,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[InferenceSecret], secret, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.inference.secrets.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SyncOffsetPage[InferenceSecret], secret, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.inference.secrets.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SyncOffsetPage[InferenceSecret], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        secret = client.cloud.inference.secrets.delete(
            secret_name="aws-dev",
            project_id=1,
        )
        assert secret is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.inference.secrets.with_raw_response.delete(
            secret_name="aws-dev",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert secret is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.inference.secrets.with_streaming_response.delete(
            secret_name="aws-dev",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            client.cloud.inference.secrets.with_raw_response.delete(
                secret_name="",
                project_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        secret = client.cloud.inference.secrets.get(
            secret_name="aws-dev",
            project_id=1,
        )
        assert_matches_type(InferenceSecret, secret, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.inference.secrets.with_raw_response.get(
            secret_name="aws-dev",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(InferenceSecret, secret, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.inference.secrets.with_streaming_response.get(
            secret_name="aws-dev",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(InferenceSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            client.cloud.inference.secrets.with_raw_response.get(
                secret_name="",
                project_id=1,
            )

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        secret = client.cloud.inference.secrets.replace(
            secret_name="aws-dev",
            project_id=1,
            data={
                "aws_access_key_id": "fake-key-id",
                "aws_secret_access_key": "fake-secret",
            },
            type="aws-iam",
        )
        assert_matches_type(InferenceSecret, secret, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.cloud.inference.secrets.with_raw_response.replace(
            secret_name="aws-dev",
            project_id=1,
            data={
                "aws_access_key_id": "fake-key-id",
                "aws_secret_access_key": "fake-secret",
            },
            type="aws-iam",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(InferenceSecret, secret, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.cloud.inference.secrets.with_streaming_response.replace(
            secret_name="aws-dev",
            project_id=1,
            data={
                "aws_access_key_id": "fake-key-id",
                "aws_secret_access_key": "fake-secret",
            },
            type="aws-iam",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(InferenceSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            client.cloud.inference.secrets.with_raw_response.replace(
                secret_name="",
                project_id=1,
                data={
                    "aws_access_key_id": "fake-key-id",
                    "aws_secret_access_key": "fake-secret",
                },
                type="aws-iam",
            )


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.inference.secrets.create(
            project_id=1,
            data={
                "aws_access_key_id": "fake-key-id",
                "aws_secret_access_key": "fake-secret",
            },
            name="aws-dev",
            type="aws-iam",
        )
        assert_matches_type(InferenceSecret, secret, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.secrets.with_raw_response.create(
            project_id=1,
            data={
                "aws_access_key_id": "fake-key-id",
                "aws_secret_access_key": "fake-secret",
            },
            name="aws-dev",
            type="aws-iam",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(InferenceSecret, secret, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.secrets.with_streaming_response.create(
            project_id=1,
            data={
                "aws_access_key_id": "fake-key-id",
                "aws_secret_access_key": "fake-secret",
            },
            name="aws-dev",
            type="aws-iam",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(InferenceSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.inference.secrets.list(
            project_id=1,
        )
        assert_matches_type(AsyncOffsetPage[InferenceSecret], secret, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.inference.secrets.list(
            project_id=1,
            limit=1000,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[InferenceSecret], secret, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.secrets.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(AsyncOffsetPage[InferenceSecret], secret, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.secrets.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(AsyncOffsetPage[InferenceSecret], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.inference.secrets.delete(
            secret_name="aws-dev",
            project_id=1,
        )
        assert secret is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.secrets.with_raw_response.delete(
            secret_name="aws-dev",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert secret is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.secrets.with_streaming_response.delete(
            secret_name="aws-dev",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            await async_client.cloud.inference.secrets.with_raw_response.delete(
                secret_name="",
                project_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.inference.secrets.get(
            secret_name="aws-dev",
            project_id=1,
        )
        assert_matches_type(InferenceSecret, secret, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.secrets.with_raw_response.get(
            secret_name="aws-dev",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(InferenceSecret, secret, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.secrets.with_streaming_response.get(
            secret_name="aws-dev",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(InferenceSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            await async_client.cloud.inference.secrets.with_raw_response.get(
                secret_name="",
                project_id=1,
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        secret = await async_client.cloud.inference.secrets.replace(
            secret_name="aws-dev",
            project_id=1,
            data={
                "aws_access_key_id": "fake-key-id",
                "aws_secret_access_key": "fake-secret",
            },
            type="aws-iam",
        )
        assert_matches_type(InferenceSecret, secret, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.secrets.with_raw_response.replace(
            secret_name="aws-dev",
            project_id=1,
            data={
                "aws_access_key_id": "fake-key-id",
                "aws_secret_access_key": "fake-secret",
            },
            type="aws-iam",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(InferenceSecret, secret, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.secrets.with_streaming_response.replace(
            secret_name="aws-dev",
            project_id=1,
            data={
                "aws_access_key_id": "fake-key-id",
                "aws_secret_access_key": "fake-secret",
            },
            type="aws-iam",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(InferenceSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            await async_client.cloud.inference.secrets.with_raw_response.replace(
                secret_name="",
                project_id=1,
                data={
                    "aws_access_key_id": "fake-key-id",
                    "aws_secret_access_key": "fake-secret",
                },
                type="aws-iam",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.storage.buckets import PolicyGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        policy = client.storage.buckets.policy.create(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert policy is None

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.storage.buckets.policy.with_raw_response.create(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert policy is None

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.storage.buckets.policy.with_streaming_response.create(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.buckets.policy.with_raw_response.create(
                bucket_name="",
                storage_id=0,
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        policy = client.storage.buckets.policy.delete(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert policy is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.storage.buckets.policy.with_raw_response.delete(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert policy is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.storage.buckets.policy.with_streaming_response.delete(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.buckets.policy.with_raw_response.delete(
                bucket_name="",
                storage_id=0,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        policy = client.storage.buckets.policy.get(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert_matches_type(PolicyGetResponse, policy, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.storage.buckets.policy.with_raw_response.get(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(PolicyGetResponse, policy, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.storage.buckets.policy.with_streaming_response.get(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(PolicyGetResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.buckets.policy.with_raw_response.get(
                bucket_name="",
                storage_id=0,
            )


class TestAsyncPolicy:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        policy = await async_client.storage.buckets.policy.create(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert policy is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.buckets.policy.with_raw_response.create(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert policy is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.buckets.policy.with_streaming_response.create(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.buckets.policy.with_raw_response.create(
                bucket_name="",
                storage_id=0,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        policy = await async_client.storage.buckets.policy.delete(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert policy is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.buckets.policy.with_raw_response.delete(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert policy is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.buckets.policy.with_streaming_response.delete(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.buckets.policy.with_raw_response.delete(
                bucket_name="",
                storage_id=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        policy = await async_client.storage.buckets.policy.get(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert_matches_type(PolicyGetResponse, policy, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.buckets.policy.with_raw_response.get(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(PolicyGetResponse, policy, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.buckets.policy.with_streaming_response.get(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(PolicyGetResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.buckets.policy.with_raw_response.get(
                bucket_name="",
                storage_id=0,
            )

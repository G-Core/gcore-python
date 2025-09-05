# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLifecycle:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        lifecycle = client.storage.buckets.lifecycle.create(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert lifecycle is None

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        lifecycle = client.storage.buckets.lifecycle.create(
            bucket_name="bucket_name",
            storage_id=0,
            expiration_days=30,
        )
        assert lifecycle is None

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.storage.buckets.lifecycle.with_raw_response.create(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle = response.parse()
        assert lifecycle is None

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.storage.buckets.lifecycle.with_streaming_response.create(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle = response.parse()
            assert lifecycle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.buckets.lifecycle.with_raw_response.create(
                bucket_name="",
                storage_id=0,
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        lifecycle = client.storage.buckets.lifecycle.delete(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert lifecycle is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.storage.buckets.lifecycle.with_raw_response.delete(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle = response.parse()
        assert lifecycle is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.storage.buckets.lifecycle.with_streaming_response.delete(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle = response.parse()
            assert lifecycle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.buckets.lifecycle.with_raw_response.delete(
                bucket_name="",
                storage_id=0,
            )


class TestAsyncLifecycle:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        lifecycle = await async_client.storage.buckets.lifecycle.create(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert lifecycle is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        lifecycle = await async_client.storage.buckets.lifecycle.create(
            bucket_name="bucket_name",
            storage_id=0,
            expiration_days=30,
        )
        assert lifecycle is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.buckets.lifecycle.with_raw_response.create(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle = await response.parse()
        assert lifecycle is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.buckets.lifecycle.with_streaming_response.create(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle = await response.parse()
            assert lifecycle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.buckets.lifecycle.with_raw_response.create(
                bucket_name="",
                storage_id=0,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        lifecycle = await async_client.storage.buckets.lifecycle.delete(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert lifecycle is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.buckets.lifecycle.with_raw_response.delete(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle = await response.parse()
        assert lifecycle is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.buckets.lifecycle.with_streaming_response.delete(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle = await response.parse()
            assert lifecycle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.buckets.lifecycle.with_raw_response.delete(
                bucket_name="",
                storage_id=0,
            )

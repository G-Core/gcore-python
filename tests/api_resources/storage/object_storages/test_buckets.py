# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.storage.object_storages import Bucket

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBuckets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        bucket = client.storage.object_storages.buckets.create(
            storage_id=0,
            name="my-new-bucket",
        )
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.storage.object_storages.buckets.with_raw_response.create(
            storage_id=0,
            name="my-new-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.storage.object_storages.buckets.with_streaming_response.create(
            storage_id=0,
            name="my-new-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert_matches_type(Bucket, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        bucket = client.storage.object_storages.buckets.update(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        bucket = client.storage.object_storages.buckets.update(
            bucket_name="bucket_name",
            storage_id=0,
            cors={"allowed_origins": ["https://example.com"]},
            lifecycle={"expiration_days": 30},
            policy={"is_public": True},
        )
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.storage.object_storages.buckets.with_raw_response.update(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.storage.object_storages.buckets.with_streaming_response.update(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert_matches_type(Bucket, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.object_storages.buckets.with_raw_response.update(
                bucket_name="",
                storage_id=0,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        bucket = client.storage.object_storages.buckets.list(
            storage_id=0,
        )
        assert_matches_type(SyncOffsetPage[Bucket], bucket, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        bucket = client.storage.object_storages.buckets.list(
            storage_id=0,
            limit=1,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[Bucket], bucket, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.storage.object_storages.buckets.with_raw_response.list(
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert_matches_type(SyncOffsetPage[Bucket], bucket, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.storage.object_storages.buckets.with_streaming_response.list(
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert_matches_type(SyncOffsetPage[Bucket], bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        bucket = client.storage.object_storages.buckets.delete(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert bucket is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.storage.object_storages.buckets.with_raw_response.delete(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert bucket is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.storage.object_storages.buckets.with_streaming_response.delete(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert bucket is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.object_storages.buckets.with_raw_response.delete(
                bucket_name="",
                storage_id=0,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        bucket = client.storage.object_storages.buckets.get(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.storage.object_storages.buckets.with_raw_response.get(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.storage.object_storages.buckets.with_streaming_response.get(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert_matches_type(Bucket, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.object_storages.buckets.with_raw_response.get(
                bucket_name="",
                storage_id=0,
            )


class TestAsyncBuckets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        bucket = await async_client.storage.object_storages.buckets.create(
            storage_id=0,
            name="my-new-bucket",
        )
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.object_storages.buckets.with_raw_response.create(
            storage_id=0,
            name="my-new-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.object_storages.buckets.with_streaming_response.create(
            storage_id=0,
            name="my-new-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert_matches_type(Bucket, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        bucket = await async_client.storage.object_storages.buckets.update(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        bucket = await async_client.storage.object_storages.buckets.update(
            bucket_name="bucket_name",
            storage_id=0,
            cors={"allowed_origins": ["https://example.com"]},
            lifecycle={"expiration_days": 30},
            policy={"is_public": True},
        )
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.object_storages.buckets.with_raw_response.update(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.object_storages.buckets.with_streaming_response.update(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert_matches_type(Bucket, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.object_storages.buckets.with_raw_response.update(
                bucket_name="",
                storage_id=0,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        bucket = await async_client.storage.object_storages.buckets.list(
            storage_id=0,
        )
        assert_matches_type(AsyncOffsetPage[Bucket], bucket, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        bucket = await async_client.storage.object_storages.buckets.list(
            storage_id=0,
            limit=1,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[Bucket], bucket, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.object_storages.buckets.with_raw_response.list(
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert_matches_type(AsyncOffsetPage[Bucket], bucket, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.object_storages.buckets.with_streaming_response.list(
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert_matches_type(AsyncOffsetPage[Bucket], bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        bucket = await async_client.storage.object_storages.buckets.delete(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert bucket is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.object_storages.buckets.with_raw_response.delete(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert bucket is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.object_storages.buckets.with_streaming_response.delete(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert bucket is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.object_storages.buckets.with_raw_response.delete(
                bucket_name="",
                storage_id=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        bucket = await async_client.storage.object_storages.buckets.get(
            bucket_name="bucket_name",
            storage_id=0,
        )
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.object_storages.buckets.with_raw_response.get(
            bucket_name="bucket_name",
            storage_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert_matches_type(Bucket, bucket, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.object_storages.buckets.with_streaming_response.get(
            bucket_name="bucket_name",
            storage_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert_matches_type(Bucket, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.object_storages.buckets.with_raw_response.get(
                bucket_name="",
                storage_id=0,
            )

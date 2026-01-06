# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import (
    Snapshot,
    TaskIDList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVolumeSnapshots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        volume_snapshot = client.cloud.volume_snapshots.create(
            project_id=0,
            region_id=0,
            name="my-snapshot",
            volume_id="67baa7d1-08ea-4fc5-bef2-6b2465b7d227",
        )
        assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        volume_snapshot = client.cloud.volume_snapshots.create(
            project_id=0,
            region_id=0,
            name="my-snapshot",
            volume_id="67baa7d1-08ea-4fc5-bef2-6b2465b7d227",
            description="Snapshot description",
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.volume_snapshots.with_raw_response.create(
            project_id=0,
            region_id=0,
            name="my-snapshot",
            volume_id="67baa7d1-08ea-4fc5-bef2-6b2465b7d227",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume_snapshot = response.parse()
        assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.volume_snapshots.with_streaming_response.create(
            project_id=0,
            region_id=0,
            name="my-snapshot",
            volume_id="67baa7d1-08ea-4fc5-bef2-6b2465b7d227",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume_snapshot = response.parse()
            assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        volume_snapshot = client.cloud.volume_snapshots.update(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Snapshot, volume_snapshot, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        volume_snapshot = client.cloud.volume_snapshots.update(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            name="my-backup-snapshot",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(Snapshot, volume_snapshot, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.volume_snapshots.with_raw_response.update(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume_snapshot = response.parse()
        assert_matches_type(Snapshot, volume_snapshot, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.volume_snapshots.with_streaming_response.update(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume_snapshot = response.parse()
            assert_matches_type(Snapshot, volume_snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            client.cloud.volume_snapshots.with_raw_response.update(
                snapshot_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        volume_snapshot = client.cloud.volume_snapshots.delete(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.volume_snapshots.with_raw_response.delete(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume_snapshot = response.parse()
        assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.volume_snapshots.with_streaming_response.delete(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume_snapshot = response.parse()
            assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            client.cloud.volume_snapshots.with_raw_response.delete(
                snapshot_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        volume_snapshot = client.cloud.volume_snapshots.get(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Snapshot, volume_snapshot, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.volume_snapshots.with_raw_response.get(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume_snapshot = response.parse()
        assert_matches_type(Snapshot, volume_snapshot, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.volume_snapshots.with_streaming_response.get(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume_snapshot = response.parse()
            assert_matches_type(Snapshot, volume_snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            client.cloud.volume_snapshots.with_raw_response.get(
                snapshot_id="",
                project_id=1,
                region_id=1,
            )


class TestAsyncVolumeSnapshots:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        volume_snapshot = await async_client.cloud.volume_snapshots.create(
            project_id=0,
            region_id=0,
            name="my-snapshot",
            volume_id="67baa7d1-08ea-4fc5-bef2-6b2465b7d227",
        )
        assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        volume_snapshot = await async_client.cloud.volume_snapshots.create(
            project_id=0,
            region_id=0,
            name="my-snapshot",
            volume_id="67baa7d1-08ea-4fc5-bef2-6b2465b7d227",
            description="Snapshot description",
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volume_snapshots.with_raw_response.create(
            project_id=0,
            region_id=0,
            name="my-snapshot",
            volume_id="67baa7d1-08ea-4fc5-bef2-6b2465b7d227",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume_snapshot = await response.parse()
        assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volume_snapshots.with_streaming_response.create(
            project_id=0,
            region_id=0,
            name="my-snapshot",
            volume_id="67baa7d1-08ea-4fc5-bef2-6b2465b7d227",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume_snapshot = await response.parse()
            assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        volume_snapshot = await async_client.cloud.volume_snapshots.update(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Snapshot, volume_snapshot, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        volume_snapshot = await async_client.cloud.volume_snapshots.update(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            name="my-backup-snapshot",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(Snapshot, volume_snapshot, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volume_snapshots.with_raw_response.update(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume_snapshot = await response.parse()
        assert_matches_type(Snapshot, volume_snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volume_snapshots.with_streaming_response.update(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume_snapshot = await response.parse()
            assert_matches_type(Snapshot, volume_snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            await async_client.cloud.volume_snapshots.with_raw_response.update(
                snapshot_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        volume_snapshot = await async_client.cloud.volume_snapshots.delete(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volume_snapshots.with_raw_response.delete(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume_snapshot = await response.parse()
        assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volume_snapshots.with_streaming_response.delete(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume_snapshot = await response.parse()
            assert_matches_type(TaskIDList, volume_snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            await async_client.cloud.volume_snapshots.with_raw_response.delete(
                snapshot_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        volume_snapshot = await async_client.cloud.volume_snapshots.get(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Snapshot, volume_snapshot, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volume_snapshots.with_raw_response.get(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume_snapshot = await response.parse()
        assert_matches_type(Snapshot, volume_snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volume_snapshots.with_streaming_response.get(
            snapshot_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume_snapshot = await response.parse()
            assert_matches_type(Snapshot, volume_snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            await async_client.cloud.volume_snapshots.with_raw_response.get(
                snapshot_id="",
                project_id=1,
                region_id=1,
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import (
    FileShare,
    TaskIDList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFileShares:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Gcore) -> None:
        file_share = client.cloud.file_shares.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            network={"network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8"},
            protocol="NFS",
            size=5,
        )
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Gcore) -> None:
        file_share = client.cloud.file_shares.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            network={
                "network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8",
                "subnet_id": "91200a6c-07e0-42aa-98da-32d1f6545ae7",
            },
            protocol="NFS",
            size=5,
            access=[
                {
                    "access_mode": "ro",
                    "ip_address": "10.0.0.1",
                }
            ],
            tags={"my-tag": "my-tag-value"},
            volume_type="default_share_type",
        )
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Gcore) -> None:
        response = client.cloud.file_shares.with_raw_response.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            network={"network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8"},
            protocol="NFS",
            size=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = response.parse()
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gcore) -> None:
        with client.cloud.file_shares.with_streaming_response.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            network={"network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8"},
            protocol="NFS",
            size=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = response.parse()
            assert_matches_type(TaskIDList, file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Gcore) -> None:
        file_share = client.cloud.file_shares.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            protocol="NFS",
            size=5,
            volume_type="vast_share_type",
        )
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Gcore) -> None:
        file_share = client.cloud.file_shares.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            protocol="NFS",
            size=5,
            volume_type="vast_share_type",
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Gcore) -> None:
        response = client.cloud.file_shares.with_raw_response.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            protocol="NFS",
            size=5,
            volume_type="vast_share_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = response.parse()
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gcore) -> None:
        with client.cloud.file_shares.with_streaming_response.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            protocol="NFS",
            size=5,
            volume_type="vast_share_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = response.parse()
            assert_matches_type(TaskIDList, file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        file_share = client.cloud.file_shares.update(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            name="my-resource",
        )
        assert_matches_type(FileShare, file_share, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.file_shares.with_raw_response.update(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            name="my-resource",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = response.parse()
        assert_matches_type(FileShare, file_share, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.file_shares.with_streaming_response.update(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            name="my-resource",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = response.parse()
            assert_matches_type(FileShare, file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            client.cloud.file_shares.with_raw_response.update(
                file_share_id="",
                project_id=1,
                region_id=1,
                name="my-resource",
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        file_share = client.cloud.file_shares.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(SyncOffsetPage[FileShare], file_share, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        file_share = client.cloud.file_shares.list(
            project_id=1,
            region_id=1,
            limit=1000,
            name="test-sfs",
            offset=0,
            type_name="standard",
        )
        assert_matches_type(SyncOffsetPage[FileShare], file_share, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.file_shares.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = response.parse()
        assert_matches_type(SyncOffsetPage[FileShare], file_share, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.file_shares.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = response.parse()
            assert_matches_type(SyncOffsetPage[FileShare], file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        file_share = client.cloud.file_shares.delete(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.file_shares.with_raw_response.delete(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = response.parse()
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.file_shares.with_streaming_response.delete(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = response.parse()
            assert_matches_type(TaskIDList, file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            client.cloud.file_shares.with_raw_response.delete(
                file_share_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        file_share = client.cloud.file_shares.get(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(FileShare, file_share, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.file_shares.with_raw_response.get(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = response.parse()
        assert_matches_type(FileShare, file_share, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.file_shares.with_streaming_response.get(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = response.parse()
            assert_matches_type(FileShare, file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            client.cloud.file_shares.with_raw_response.get(
                file_share_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_resize(self, client: Gcore) -> None:
        file_share = client.cloud.file_shares.resize(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            size=5,
        )
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    def test_raw_response_resize(self, client: Gcore) -> None:
        response = client.cloud.file_shares.with_raw_response.resize(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            size=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = response.parse()
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    def test_streaming_response_resize(self, client: Gcore) -> None:
        with client.cloud.file_shares.with_streaming_response.resize(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            size=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = response.parse()
            assert_matches_type(TaskIDList, file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resize(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            client.cloud.file_shares.with_raw_response.resize(
                file_share_id="",
                project_id=1,
                region_id=1,
                size=5,
            )


class TestAsyncFileShares:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGcore) -> None:
        file_share = await async_client.cloud.file_shares.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            network={"network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8"},
            protocol="NFS",
            size=5,
        )
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncGcore) -> None:
        file_share = await async_client.cloud.file_shares.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            network={
                "network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8",
                "subnet_id": "91200a6c-07e0-42aa-98da-32d1f6545ae7",
            },
            protocol="NFS",
            size=5,
            access=[
                {
                    "access_mode": "ro",
                    "ip_address": "10.0.0.1",
                }
            ],
            tags={"my-tag": "my-tag-value"},
            volume_type="default_share_type",
        )
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.file_shares.with_raw_response.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            network={"network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8"},
            protocol="NFS",
            size=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = await response.parse()
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.file_shares.with_streaming_response.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            network={"network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8"},
            protocol="NFS",
            size=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = await response.parse()
            assert_matches_type(TaskIDList, file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGcore) -> None:
        file_share = await async_client.cloud.file_shares.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            protocol="NFS",
            size=5,
            volume_type="vast_share_type",
        )
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncGcore) -> None:
        file_share = await async_client.cloud.file_shares.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            protocol="NFS",
            size=5,
            volume_type="vast_share_type",
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.file_shares.with_raw_response.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            protocol="NFS",
            size=5,
            volume_type="vast_share_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = await response.parse()
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.file_shares.with_streaming_response.create(
            project_id=1,
            region_id=1,
            name="test-share-file-system",
            protocol="NFS",
            size=5,
            volume_type="vast_share_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = await response.parse()
            assert_matches_type(TaskIDList, file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        file_share = await async_client.cloud.file_shares.update(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            name="my-resource",
        )
        assert_matches_type(FileShare, file_share, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.file_shares.with_raw_response.update(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            name="my-resource",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = await response.parse()
        assert_matches_type(FileShare, file_share, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.file_shares.with_streaming_response.update(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            name="my-resource",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = await response.parse()
            assert_matches_type(FileShare, file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            await async_client.cloud.file_shares.with_raw_response.update(
                file_share_id="",
                project_id=1,
                region_id=1,
                name="my-resource",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        file_share = await async_client.cloud.file_shares.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(AsyncOffsetPage[FileShare], file_share, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        file_share = await async_client.cloud.file_shares.list(
            project_id=1,
            region_id=1,
            limit=1000,
            name="test-sfs",
            offset=0,
            type_name="standard",
        )
        assert_matches_type(AsyncOffsetPage[FileShare], file_share, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.file_shares.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = await response.parse()
        assert_matches_type(AsyncOffsetPage[FileShare], file_share, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.file_shares.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = await response.parse()
            assert_matches_type(AsyncOffsetPage[FileShare], file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        file_share = await async_client.cloud.file_shares.delete(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.file_shares.with_raw_response.delete(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = await response.parse()
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.file_shares.with_streaming_response.delete(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = await response.parse()
            assert_matches_type(TaskIDList, file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            await async_client.cloud.file_shares.with_raw_response.delete(
                file_share_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        file_share = await async_client.cloud.file_shares.get(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(FileShare, file_share, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.file_shares.with_raw_response.get(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = await response.parse()
        assert_matches_type(FileShare, file_share, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.file_shares.with_streaming_response.get(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = await response.parse()
            assert_matches_type(FileShare, file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            await async_client.cloud.file_shares.with_raw_response.get(
                file_share_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_resize(self, async_client: AsyncGcore) -> None:
        file_share = await async_client.cloud.file_shares.resize(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            size=5,
        )
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    async def test_raw_response_resize(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.file_shares.with_raw_response.resize(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            size=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_share = await response.parse()
        assert_matches_type(TaskIDList, file_share, path=["response"])

    @parametrize
    async def test_streaming_response_resize(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.file_shares.with_streaming_response.resize(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            size=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_share = await response.parse()
            assert_matches_type(TaskIDList, file_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resize(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            await async_client.cloud.file_shares.with_raw_response.resize(
                file_share_id="",
                project_id=1,
                region_id=1,
                size=5,
            )

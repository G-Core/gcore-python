# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.types.cloud import TaskIDList
from gcore.types.cloud.gpu_virtual.clusters import GPUVirtualClusterServerList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        server = client.cloud.gpu_virtual.clusters.servers.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(GPUVirtualClusterServerList, server, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.gpu_virtual.clusters.servers.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            changed_before=parse_datetime("2025-10-01T12:00:00Z"),
            changed_since=parse_datetime("2025-10-01T12:00:00Z"),
            ip_address="237.84.2.178",
            limit=10,
            name="name",
            offset=0,
            order_by="created_at.asc",
            status="ACTIVE",
            uuids=["string"],
        )
        assert_matches_type(GPUVirtualClusterServerList, server, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.servers.with_raw_response.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(GPUVirtualClusterServerList, server, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.servers.with_streaming_response.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(GPUVirtualClusterServerList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_virtual.clusters.servers.with_raw_response.list(
                cluster_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        server = client.cloud.gpu_virtual.clusters.servers.delete(
            server_id="f1c1eeb6-1834-48c9-a7b0-daafce64872b",
            project_id=1,
            region_id=7,
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.gpu_virtual.clusters.servers.delete(
            server_id="f1c1eeb6-1834-48c9-a7b0-daafce64872b",
            project_id=1,
            region_id=7,
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            all_floating_ips=True,
            all_reserved_fixed_ips=True,
            all_volumes=True,
            floating_ip_ids=["e4a01208-d6ac-4304-bf86-3028154b070a"],
            reserved_fixed_ip_ids=["a29b8e1e-08d3-4cec-91fb-06e81e5f46d5"],
            volume_ids=["1333c684-c3da-4b91-ac9e-a92706aa2824"],
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.servers.with_raw_response.delete(
            server_id="f1c1eeb6-1834-48c9-a7b0-daafce64872b",
            project_id=1,
            region_id=7,
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.servers.with_streaming_response.delete(
            server_id="f1c1eeb6-1834-48c9-a7b0-daafce64872b",
            project_id=1,
            region_id=7,
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_virtual.clusters.servers.with_raw_response.delete(
                server_id="f1c1eeb6-1834-48c9-a7b0-daafce64872b",
                project_id=1,
                region_id=7,
                cluster_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.cloud.gpu_virtual.clusters.servers.with_raw_response.delete(
                server_id="",
                project_id=1,
                region_id=7,
                cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            )


class TestAsyncServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_virtual.clusters.servers.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(GPUVirtualClusterServerList, server, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_virtual.clusters.servers.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            changed_before=parse_datetime("2025-10-01T12:00:00Z"),
            changed_since=parse_datetime("2025-10-01T12:00:00Z"),
            ip_address="237.84.2.178",
            limit=10,
            name="name",
            offset=0,
            order_by="created_at.asc",
            status="ACTIVE",
            uuids=["string"],
        )
        assert_matches_type(GPUVirtualClusterServerList, server, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.servers.with_raw_response.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(GPUVirtualClusterServerList, server, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.servers.with_streaming_response.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(GPUVirtualClusterServerList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.servers.with_raw_response.list(
                cluster_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_virtual.clusters.servers.delete(
            server_id="f1c1eeb6-1834-48c9-a7b0-daafce64872b",
            project_id=1,
            region_id=7,
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_virtual.clusters.servers.delete(
            server_id="f1c1eeb6-1834-48c9-a7b0-daafce64872b",
            project_id=1,
            region_id=7,
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            all_floating_ips=True,
            all_reserved_fixed_ips=True,
            all_volumes=True,
            floating_ip_ids=["e4a01208-d6ac-4304-bf86-3028154b070a"],
            reserved_fixed_ip_ids=["a29b8e1e-08d3-4cec-91fb-06e81e5f46d5"],
            volume_ids=["1333c684-c3da-4b91-ac9e-a92706aa2824"],
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.servers.with_raw_response.delete(
            server_id="f1c1eeb6-1834-48c9-a7b0-daafce64872b",
            project_id=1,
            region_id=7,
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.servers.with_streaming_response.delete(
            server_id="f1c1eeb6-1834-48c9-a7b0-daafce64872b",
            project_id=1,
            region_id=7,
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.servers.with_raw_response.delete(
                server_id="f1c1eeb6-1834-48c9-a7b0-daafce64872b",
                project_id=1,
                region_id=7,
                cluster_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.servers.with_raw_response.delete(
                server_id="",
                project_id=1,
                region_id=7,
                cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            )

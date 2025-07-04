# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import (
    TaskIDList,
    GPUBaremetalCluster,
    GPUBaremetalClusterServerList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGPUBaremetalClusters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        gpu_baremetal_cluster = client.cloud.gpu_baremetal_clusters.create(
            project_id=0,
            region_id=0,
            flavor="bm3-ai-1xlarge-h100-80-8",
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            interfaces=[
                {
                    "network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8",
                    "subnet_id": "91200a6c-07e0-42aa-98da-32d1f6545ae7",
                    "type": "subnet",
                }
            ],
            name="my-gpu-cluster",
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        gpu_baremetal_cluster = client.cloud.gpu_baremetal_clusters.create(
            project_id=0,
            region_id=0,
            flavor="bm3-ai-1xlarge-h100-80-8",
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            interfaces=[
                {
                    "network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8",
                    "subnet_id": "91200a6c-07e0-42aa-98da-32d1f6545ae7",
                    "type": "subnet",
                    "floating_ip": {"source": "new"},
                    "interface_name": "interface_name",
                }
            ],
            name="my-gpu-cluster",
            instances_count=1,
            password="password",
            ssh_key_name="my-ssh-key",
            tags={"my-tag": "my-tag-value"},
            user_data="user_data",
            username="username",
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.with_raw_response.create(
            project_id=0,
            region_id=0,
            flavor="bm3-ai-1xlarge-h100-80-8",
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            interfaces=[
                {
                    "network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8",
                    "subnet_id": "91200a6c-07e0-42aa-98da-32d1f6545ae7",
                    "type": "subnet",
                }
            ],
            name="my-gpu-cluster",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = response.parse()
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.with_streaming_response.create(
            project_id=0,
            region_id=0,
            flavor="bm3-ai-1xlarge-h100-80-8",
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            interfaces=[
                {
                    "network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8",
                    "subnet_id": "91200a6c-07e0-42aa-98da-32d1f6545ae7",
                    "type": "subnet",
                }
            ],
            name="my-gpu-cluster",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = response.parse()
            assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        gpu_baremetal_cluster = client.cloud.gpu_baremetal_clusters.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SyncOffsetPage[GPUBaremetalCluster], gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        gpu_baremetal_cluster = client.cloud.gpu_baremetal_clusters.list(
            project_id=0,
            region_id=0,
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[GPUBaremetalCluster], gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = response.parse()
        assert_matches_type(SyncOffsetPage[GPUBaremetalCluster], gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = response.parse()
            assert_matches_type(SyncOffsetPage[GPUBaremetalCluster], gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        gpu_baremetal_cluster = client.cloud.gpu_baremetal_clusters.delete(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        gpu_baremetal_cluster = client.cloud.gpu_baremetal_clusters.delete(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            delete_floatings=True,
            floatings="floatings",
            reserved_fixed_ips="reserved_fixed_ips",
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.with_raw_response.delete(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = response.parse()
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.with_streaming_response.delete(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = response.parse()
            assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.with_raw_response.delete(
                cluster_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        gpu_baremetal_cluster = client.cloud.gpu_baremetal_clusters.get(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalCluster, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.with_raw_response.get(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = response.parse()
        assert_matches_type(GPUBaremetalCluster, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.with_streaming_response.get(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = response.parse()
            assert_matches_type(GPUBaremetalCluster, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.with_raw_response.get(
                cluster_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_powercycle_all_servers(self, client: Gcore) -> None:
        gpu_baremetal_cluster = client.cloud.gpu_baremetal_clusters.powercycle_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServerList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_raw_response_powercycle_all_servers(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.with_raw_response.powercycle_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = response.parse()
        assert_matches_type(GPUBaremetalClusterServerList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_streaming_response_powercycle_all_servers(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.with_streaming_response.powercycle_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = response.parse()
            assert_matches_type(GPUBaremetalClusterServerList, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_powercycle_all_servers(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.with_raw_response.powercycle_all_servers(
                cluster_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_reboot_all_servers(self, client: Gcore) -> None:
        gpu_baremetal_cluster = client.cloud.gpu_baremetal_clusters.reboot_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServerList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_raw_response_reboot_all_servers(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.with_raw_response.reboot_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = response.parse()
        assert_matches_type(GPUBaremetalClusterServerList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_streaming_response_reboot_all_servers(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.with_streaming_response.reboot_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = response.parse()
            assert_matches_type(GPUBaremetalClusterServerList, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reboot_all_servers(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.with_raw_response.reboot_all_servers(
                cluster_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_rebuild(self, client: Gcore) -> None:
        gpu_baremetal_cluster = client.cloud.gpu_baremetal_clusters.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_method_rebuild_with_all_params(self, client: Gcore) -> None:
        gpu_baremetal_cluster = client.cloud.gpu_baremetal_clusters.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            user_data="user_data",
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_raw_response_rebuild(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.with_raw_response.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = response.parse()
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_streaming_response_rebuild(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.with_streaming_response.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = response.parse()
            assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rebuild(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.with_raw_response.rebuild(
                cluster_id="",
                project_id=0,
                region_id=0,
                nodes=["string"],
            )

    @parametrize
    def test_method_resize(self, client: Gcore) -> None:
        gpu_baremetal_cluster = client.cloud.gpu_baremetal_clusters.resize(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            instances_count=1,
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_raw_response_resize(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.with_raw_response.resize(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            instances_count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = response.parse()
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    def test_streaming_response_resize(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.with_streaming_response.resize(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            instances_count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = response.parse()
            assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resize(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.with_raw_response.resize(
                cluster_id="",
                project_id=0,
                region_id=0,
                instances_count=1,
            )


class TestAsyncGPUBaremetalClusters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        gpu_baremetal_cluster = await async_client.cloud.gpu_baremetal_clusters.create(
            project_id=0,
            region_id=0,
            flavor="bm3-ai-1xlarge-h100-80-8",
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            interfaces=[
                {
                    "network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8",
                    "subnet_id": "91200a6c-07e0-42aa-98da-32d1f6545ae7",
                    "type": "subnet",
                }
            ],
            name="my-gpu-cluster",
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        gpu_baremetal_cluster = await async_client.cloud.gpu_baremetal_clusters.create(
            project_id=0,
            region_id=0,
            flavor="bm3-ai-1xlarge-h100-80-8",
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            interfaces=[
                {
                    "network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8",
                    "subnet_id": "91200a6c-07e0-42aa-98da-32d1f6545ae7",
                    "type": "subnet",
                    "floating_ip": {"source": "new"},
                    "interface_name": "interface_name",
                }
            ],
            name="my-gpu-cluster",
            instances_count=1,
            password="password",
            ssh_key_name="my-ssh-key",
            tags={"my-tag": "my-tag-value"},
            user_data="user_data",
            username="username",
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.with_raw_response.create(
            project_id=0,
            region_id=0,
            flavor="bm3-ai-1xlarge-h100-80-8",
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            interfaces=[
                {
                    "network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8",
                    "subnet_id": "91200a6c-07e0-42aa-98da-32d1f6545ae7",
                    "type": "subnet",
                }
            ],
            name="my-gpu-cluster",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = await response.parse()
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.with_streaming_response.create(
            project_id=0,
            region_id=0,
            flavor="bm3-ai-1xlarge-h100-80-8",
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            interfaces=[
                {
                    "network_id": "024a29e9-b4b7-4c91-9a46-505be123d9f8",
                    "subnet_id": "91200a6c-07e0-42aa-98da-32d1f6545ae7",
                    "type": "subnet",
                }
            ],
            name="my-gpu-cluster",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = await response.parse()
            assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        gpu_baremetal_cluster = await async_client.cloud.gpu_baremetal_clusters.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(AsyncOffsetPage[GPUBaremetalCluster], gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        gpu_baremetal_cluster = await async_client.cloud.gpu_baremetal_clusters.list(
            project_id=0,
            region_id=0,
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[GPUBaremetalCluster], gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = await response.parse()
        assert_matches_type(AsyncOffsetPage[GPUBaremetalCluster], gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = await response.parse()
            assert_matches_type(AsyncOffsetPage[GPUBaremetalCluster], gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        gpu_baremetal_cluster = await async_client.cloud.gpu_baremetal_clusters.delete(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        gpu_baremetal_cluster = await async_client.cloud.gpu_baremetal_clusters.delete(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            delete_floatings=True,
            floatings="floatings",
            reserved_fixed_ips="reserved_fixed_ips",
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.with_raw_response.delete(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = await response.parse()
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.with_streaming_response.delete(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = await response.parse()
            assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.with_raw_response.delete(
                cluster_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        gpu_baremetal_cluster = await async_client.cloud.gpu_baremetal_clusters.get(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalCluster, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.with_raw_response.get(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = await response.parse()
        assert_matches_type(GPUBaremetalCluster, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.with_streaming_response.get(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = await response.parse()
            assert_matches_type(GPUBaremetalCluster, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.with_raw_response.get(
                cluster_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_powercycle_all_servers(self, async_client: AsyncGcore) -> None:
        gpu_baremetal_cluster = await async_client.cloud.gpu_baremetal_clusters.powercycle_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServerList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_raw_response_powercycle_all_servers(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.with_raw_response.powercycle_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = await response.parse()
        assert_matches_type(GPUBaremetalClusterServerList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_streaming_response_powercycle_all_servers(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.with_streaming_response.powercycle_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = await response.parse()
            assert_matches_type(GPUBaremetalClusterServerList, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_powercycle_all_servers(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.with_raw_response.powercycle_all_servers(
                cluster_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_reboot_all_servers(self, async_client: AsyncGcore) -> None:
        gpu_baremetal_cluster = await async_client.cloud.gpu_baremetal_clusters.reboot_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServerList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_raw_response_reboot_all_servers(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.with_raw_response.reboot_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = await response.parse()
        assert_matches_type(GPUBaremetalClusterServerList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_streaming_response_reboot_all_servers(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.with_streaming_response.reboot_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = await response.parse()
            assert_matches_type(GPUBaremetalClusterServerList, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reboot_all_servers(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.with_raw_response.reboot_all_servers(
                cluster_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_rebuild(self, async_client: AsyncGcore) -> None:
        gpu_baremetal_cluster = await async_client.cloud.gpu_baremetal_clusters.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_method_rebuild_with_all_params(self, async_client: AsyncGcore) -> None:
        gpu_baremetal_cluster = await async_client.cloud.gpu_baremetal_clusters.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            user_data="user_data",
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_raw_response_rebuild(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.with_raw_response.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = await response.parse()
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_streaming_response_rebuild(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.with_streaming_response.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = await response.parse()
            assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rebuild(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.with_raw_response.rebuild(
                cluster_id="",
                project_id=0,
                region_id=0,
                nodes=["string"],
            )

    @parametrize
    async def test_method_resize(self, async_client: AsyncGcore) -> None:
        gpu_baremetal_cluster = await async_client.cloud.gpu_baremetal_clusters.resize(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            instances_count=1,
        )
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_raw_response_resize(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.with_raw_response.resize(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            instances_count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_baremetal_cluster = await response.parse()
        assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

    @parametrize
    async def test_streaming_response_resize(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.with_streaming_response.resize(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            instances_count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_baremetal_cluster = await response.parse()
            assert_matches_type(TaskIDList, gpu_baremetal_cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resize(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.with_raw_response.resize(
                cluster_id="",
                project_id=0,
                region_id=0,
                instances_count=1,
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import TaskIDList
from gcore.types.cloud.gpu_baremetal import (
    GPUBaremetalCluster,
)
from gcore.types.cloud.gpu_baremetal.clusters import GPUBaremetalClusterServerV1List

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClusters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_baremetal.clusters.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            image_id="3793c250-0b3b-4678-bab3-e11afbc29657",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={"interfaces": [{"type": "external"}]},
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_baremetal.clusters.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            image_id="3793c250-0b3b-4678-bab3-e11afbc29657",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={
                "interfaces": [
                    {
                        "type": "external",
                        "ip_family": "ipv4",
                        "name": "eth0",
                    }
                ],
                "credentials": {
                    "password": "securepassword",
                    "ssh_key_name": "my-ssh-key",
                    "username": "admin",
                },
                "file_shares": [
                    {
                        "id": "a3f2d1b8-45e6-4f8a-bb5d-19dbf2cd7e9a",
                        "mount_path": "/mnt/vast",
                    }
                ],
                "security_groups": [{"id": "b4849ffa-89f2-45a1-951f-0ae5b7809d98"}],
                "user_data": "eyJ0ZXN0IjogImRhdGEifQ==",
            },
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.with_raw_response.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            image_id="3793c250-0b3b-4678-bab3-e11afbc29657",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={"interfaces": [{"type": "external"}]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.with_streaming_response.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            image_id="3793c250-0b3b-4678-bab3-e11afbc29657",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={"interfaces": [{"type": "external"}]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_baremetal.clusters.list(
            project_id=1,
            region_id=7,
        )
        assert_matches_type(SyncOffsetPage[GPUBaremetalCluster], cluster, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_baremetal.clusters.list(
            project_id=1,
            region_id=7,
            limit=10,
            managed_by=["k8s"],
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[GPUBaremetalCluster], cluster, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.with_raw_response.list(
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(SyncOffsetPage[GPUBaremetalCluster], cluster, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.with_streaming_response.list(
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(SyncOffsetPage[GPUBaremetalCluster], cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_baremetal.clusters.delete(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_baremetal.clusters.delete(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            all_floating_ips=True,
            all_reserved_fixed_ips=True,
            floating_ip_ids=["e4a01208-d6ac-4304-bf86-3028154b070a"],
            reserved_fixed_ip_ids=["a29b8e1e-08d3-4cec-91fb-06e81e5f46d5"],
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.with_raw_response.delete(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.with_streaming_response.delete(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal.clusters.with_raw_response.delete(
                cluster_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    def test_method_action(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_baremetal.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="update_tags",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_action(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.with_raw_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="update_tags",
            tags={"foo": "my-tag-value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_action(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.with_streaming_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="update_tags",
            tags={"foo": "my-tag-value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_action(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="update_tags",
                tags={"foo": "my-tag-value"},
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_baremetal.clusters.get(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(GPUBaremetalCluster, cluster, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.with_raw_response.get(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(GPUBaremetalCluster, cluster, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.with_streaming_response.get(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(GPUBaremetalCluster, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal.clusters.with_raw_response.get(
                cluster_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    def test_method_powercycle_all_servers(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_baremetal.clusters.powercycle_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServerV1List, cluster, path=["response"])

    @parametrize
    def test_raw_response_powercycle_all_servers(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.with_raw_response.powercycle_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(GPUBaremetalClusterServerV1List, cluster, path=["response"])

    @parametrize
    def test_streaming_response_powercycle_all_servers(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.with_streaming_response.powercycle_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(GPUBaremetalClusterServerV1List, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_powercycle_all_servers(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal.clusters.with_raw_response.powercycle_all_servers(
                cluster_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_reboot_all_servers(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_baremetal.clusters.reboot_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServerV1List, cluster, path=["response"])

    @parametrize
    def test_raw_response_reboot_all_servers(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.with_raw_response.reboot_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(GPUBaremetalClusterServerV1List, cluster, path=["response"])

    @parametrize
    def test_streaming_response_reboot_all_servers(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.with_streaming_response.reboot_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(GPUBaremetalClusterServerV1List, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reboot_all_servers(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal.clusters.with_raw_response.reboot_all_servers(
                cluster_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_rebuild(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_baremetal.clusters.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_method_rebuild_with_all_params(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_baremetal.clusters.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            user_data="user_data",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_rebuild(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.with_raw_response.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_rebuild(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.with_streaming_response.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rebuild(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal.clusters.with_raw_response.rebuild(
                cluster_id="",
                project_id=0,
                region_id=0,
                nodes=["string"],
            )

    @parametrize
    def test_method_resize(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_baremetal.clusters.resize(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            instances_count=1,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_resize(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.with_raw_response.resize(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            instances_count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_resize(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.with_streaming_response.resize(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            instances_count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resize(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal.clusters.with_raw_response.resize(
                cluster_id="",
                project_id=0,
                region_id=0,
                instances_count=1,
            )


class TestAsyncClusters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_baremetal.clusters.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            image_id="3793c250-0b3b-4678-bab3-e11afbc29657",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={"interfaces": [{"type": "external"}]},
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_baremetal.clusters.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            image_id="3793c250-0b3b-4678-bab3-e11afbc29657",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={
                "interfaces": [
                    {
                        "type": "external",
                        "ip_family": "ipv4",
                        "name": "eth0",
                    }
                ],
                "credentials": {
                    "password": "securepassword",
                    "ssh_key_name": "my-ssh-key",
                    "username": "admin",
                },
                "file_shares": [
                    {
                        "id": "a3f2d1b8-45e6-4f8a-bb5d-19dbf2cd7e9a",
                        "mount_path": "/mnt/vast",
                    }
                ],
                "security_groups": [{"id": "b4849ffa-89f2-45a1-951f-0ae5b7809d98"}],
                "user_data": "eyJ0ZXN0IjogImRhdGEifQ==",
            },
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.with_raw_response.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            image_id="3793c250-0b3b-4678-bab3-e11afbc29657",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={"interfaces": [{"type": "external"}]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.with_streaming_response.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            image_id="3793c250-0b3b-4678-bab3-e11afbc29657",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={"interfaces": [{"type": "external"}]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_baremetal.clusters.list(
            project_id=1,
            region_id=7,
        )
        assert_matches_type(AsyncOffsetPage[GPUBaremetalCluster], cluster, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_baremetal.clusters.list(
            project_id=1,
            region_id=7,
            limit=10,
            managed_by=["k8s"],
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[GPUBaremetalCluster], cluster, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.with_raw_response.list(
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(AsyncOffsetPage[GPUBaremetalCluster], cluster, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.with_streaming_response.list(
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(AsyncOffsetPage[GPUBaremetalCluster], cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_baremetal.clusters.delete(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_baremetal.clusters.delete(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            all_floating_ips=True,
            all_reserved_fixed_ips=True,
            floating_ip_ids=["e4a01208-d6ac-4304-bf86-3028154b070a"],
            reserved_fixed_ip_ids=["a29b8e1e-08d3-4cec-91fb-06e81e5f46d5"],
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.with_raw_response.delete(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.with_streaming_response.delete(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal.clusters.with_raw_response.delete(
                cluster_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    async def test_method_action(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_baremetal.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="update_tags",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_action(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.with_raw_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="update_tags",
            tags={"foo": "my-tag-value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_action(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.with_streaming_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="update_tags",
            tags={"foo": "my-tag-value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_action(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="update_tags",
                tags={"foo": "my-tag-value"},
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_baremetal.clusters.get(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(GPUBaremetalCluster, cluster, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.with_raw_response.get(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(GPUBaremetalCluster, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.with_streaming_response.get(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(GPUBaremetalCluster, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal.clusters.with_raw_response.get(
                cluster_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    async def test_method_powercycle_all_servers(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_baremetal.clusters.powercycle_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServerV1List, cluster, path=["response"])

    @parametrize
    async def test_raw_response_powercycle_all_servers(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.with_raw_response.powercycle_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(GPUBaremetalClusterServerV1List, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_powercycle_all_servers(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.with_streaming_response.powercycle_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(GPUBaremetalClusterServerV1List, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_powercycle_all_servers(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal.clusters.with_raw_response.powercycle_all_servers(
                cluster_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_reboot_all_servers(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_baremetal.clusters.reboot_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServerV1List, cluster, path=["response"])

    @parametrize
    async def test_raw_response_reboot_all_servers(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.with_raw_response.reboot_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(GPUBaremetalClusterServerV1List, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_reboot_all_servers(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.with_streaming_response.reboot_all_servers(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(GPUBaremetalClusterServerV1List, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reboot_all_servers(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal.clusters.with_raw_response.reboot_all_servers(
                cluster_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_rebuild(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_baremetal.clusters.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_method_rebuild_with_all_params(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_baremetal.clusters.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            user_data="user_data",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_rebuild(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.with_raw_response.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_rebuild(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.with_streaming_response.rebuild(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            nodes=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rebuild(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal.clusters.with_raw_response.rebuild(
                cluster_id="",
                project_id=0,
                region_id=0,
                nodes=["string"],
            )

    @parametrize
    async def test_method_resize(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_baremetal.clusters.resize(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            instances_count=1,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_resize(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.with_raw_response.resize(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            instances_count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_resize(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.with_streaming_response.resize(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
            instances_count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resize(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal.clusters.with_raw_response.resize(
                cluster_id="",
                project_id=0,
                region_id=0,
                instances_count=1,
            )

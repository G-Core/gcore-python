# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import TaskIDList
from gcore.types.cloud.gpu_virtual import (
    GPUVirtualCluster,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClusters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={
                "interfaces": [{"type": "external"}],
                "volumes": [
                    {
                        "boot_index": 1,
                        "name": "my-data-disk",
                        "size": 100,
                        "source": "new",
                        "type": "cold",
                    }
                ],
            },
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
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
                "volumes": [
                    {
                        "boot_index": 1,
                        "name": "my-data-disk",
                        "size": 100,
                        "source": "new",
                        "type": "cold",
                        "delete_on_termination": True,
                        "tags": {"key1": "value1"},
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
        response = client.cloud.gpu_virtual.clusters.with_raw_response.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={
                "interfaces": [{"type": "external"}],
                "volumes": [
                    {
                        "boot_index": 1,
                        "name": "my-data-disk",
                        "size": 100,
                        "source": "new",
                        "type": "cold",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.with_streaming_response.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={
                "interfaces": [{"type": "external"}],
                "volumes": [
                    {
                        "boot_index": 1,
                        "name": "my-data-disk",
                        "size": 100,
                        "source": "new",
                        "type": "cold",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.update(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            name="gpu-cluster-1",
        )
        assert_matches_type(GPUVirtualCluster, cluster, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.with_raw_response.update(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            name="gpu-cluster-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(GPUVirtualCluster, cluster, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.with_streaming_response.update(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            name="gpu-cluster-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(GPUVirtualCluster, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_virtual.clusters.with_raw_response.update(
                cluster_id="",
                project_id=1,
                region_id=7,
                name="gpu-cluster-1",
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.list(
            project_id=1,
            region_id=7,
        )
        assert_matches_type(SyncOffsetPage[GPUVirtualCluster], cluster, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.list(
            project_id=1,
            region_id=7,
            limit=10,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[GPUVirtualCluster], cluster, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.with_raw_response.list(
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(SyncOffsetPage[GPUVirtualCluster], cluster, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.with_streaming_response.list(
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(SyncOffsetPage[GPUVirtualCluster], cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.delete(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.delete(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            all_floating_ips=True,
            all_reserved_fixed_ips=True,
            all_volumes=True,
            floating_ip_ids=["e4a01208-d6ac-4304-bf86-3028154b070a"],
            reserved_fixed_ip_ids=["a29b8e1e-08d3-4cec-91fb-06e81e5f46d5"],
            volume_ids=["1333c684-c3da-4b91-ac9e-a92706aa2824"],
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.with_raw_response.delete(
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
        with client.cloud.gpu_virtual.clusters.with_streaming_response.delete(
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
            client.cloud.gpu_virtual.clusters.with_raw_response.delete(
                cluster_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    def test_method_action_overload_1(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="start",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_action_overload_1(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.with_raw_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_action_overload_1(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.with_streaming_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_action_overload_1(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_virtual.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="start",
            )

    @parametrize
    def test_method_action_overload_2(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="stop",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_action_overload_2(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.with_raw_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="stop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_action_overload_2(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.with_streaming_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="stop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_action_overload_2(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_virtual.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="stop",
            )

    @parametrize
    def test_method_action_overload_3(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="soft_reboot",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_action_overload_3(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.with_raw_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="soft_reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_action_overload_3(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.with_streaming_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="soft_reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_action_overload_3(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_virtual.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="soft_reboot",
            )

    @parametrize
    def test_method_action_overload_4(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="hard_reboot",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_action_overload_4(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.with_raw_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="hard_reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_action_overload_4(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.with_streaming_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="hard_reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_action_overload_4(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_virtual.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="hard_reboot",
            )

    @parametrize
    def test_method_action_overload_5(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="update_tags",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_action_overload_5(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.with_raw_response.action(
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
    def test_streaming_response_action_overload_5(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.with_streaming_response.action(
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
    def test_path_params_action_overload_5(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_virtual.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="update_tags",
                tags={"foo": "my-tag-value"},
            )

    @parametrize
    def test_method_action_overload_6(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="resize",
            servers_count=5,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_action_overload_6(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.with_raw_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="resize",
            servers_count=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_action_overload_6(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.with_streaming_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="resize",
            servers_count=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_action_overload_6(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_virtual.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="resize",
                servers_count=5,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        cluster = client.cloud.gpu_virtual.clusters.get(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(GPUVirtualCluster, cluster, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.with_raw_response.get(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(GPUVirtualCluster, cluster, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.with_streaming_response.get(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(GPUVirtualCluster, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_virtual.clusters.with_raw_response.get(
                cluster_id="",
                project_id=1,
                region_id=7,
            )


class TestAsyncClusters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={
                "interfaces": [{"type": "external"}],
                "volumes": [
                    {
                        "boot_index": 1,
                        "name": "my-data-disk",
                        "size": 100,
                        "source": "new",
                        "type": "cold",
                    }
                ],
            },
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
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
                "volumes": [
                    {
                        "boot_index": 1,
                        "name": "my-data-disk",
                        "size": 100,
                        "source": "new",
                        "type": "cold",
                        "delete_on_termination": True,
                        "tags": {"key1": "value1"},
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
        response = await async_client.cloud.gpu_virtual.clusters.with_raw_response.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={
                "interfaces": [{"type": "external"}],
                "volumes": [
                    {
                        "boot_index": 1,
                        "name": "my-data-disk",
                        "size": 100,
                        "source": "new",
                        "type": "cold",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.with_streaming_response.create(
            project_id=1,
            region_id=7,
            flavor="g3-ai-32-192-1500-l40s-48-1",
            name="gpu-cluster-1",
            servers_count=3,
            servers_settings={
                "interfaces": [{"type": "external"}],
                "volumes": [
                    {
                        "boot_index": 1,
                        "name": "my-data-disk",
                        "size": 100,
                        "source": "new",
                        "type": "cold",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.update(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            name="gpu-cluster-1",
        )
        assert_matches_type(GPUVirtualCluster, cluster, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.with_raw_response.update(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            name="gpu-cluster-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(GPUVirtualCluster, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.with_streaming_response.update(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            name="gpu-cluster-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(GPUVirtualCluster, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.with_raw_response.update(
                cluster_id="",
                project_id=1,
                region_id=7,
                name="gpu-cluster-1",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.list(
            project_id=1,
            region_id=7,
        )
        assert_matches_type(AsyncOffsetPage[GPUVirtualCluster], cluster, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.list(
            project_id=1,
            region_id=7,
            limit=10,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[GPUVirtualCluster], cluster, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.with_raw_response.list(
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(AsyncOffsetPage[GPUVirtualCluster], cluster, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.with_streaming_response.list(
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(AsyncOffsetPage[GPUVirtualCluster], cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.delete(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.delete(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            all_floating_ips=True,
            all_reserved_fixed_ips=True,
            all_volumes=True,
            floating_ip_ids=["e4a01208-d6ac-4304-bf86-3028154b070a"],
            reserved_fixed_ip_ids=["a29b8e1e-08d3-4cec-91fb-06e81e5f46d5"],
            volume_ids=["1333c684-c3da-4b91-ac9e-a92706aa2824"],
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.with_raw_response.delete(
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
        async with async_client.cloud.gpu_virtual.clusters.with_streaming_response.delete(
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
            await async_client.cloud.gpu_virtual.clusters.with_raw_response.delete(
                cluster_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    async def test_method_action_overload_1(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="start",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_action_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.with_raw_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_action_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.with_streaming_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_action_overload_1(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="start",
            )

    @parametrize
    async def test_method_action_overload_2(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="stop",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_action_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.with_raw_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="stop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_action_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.with_streaming_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="stop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_action_overload_2(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="stop",
            )

    @parametrize
    async def test_method_action_overload_3(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="soft_reboot",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_action_overload_3(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.with_raw_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="soft_reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_action_overload_3(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.with_streaming_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="soft_reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_action_overload_3(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="soft_reboot",
            )

    @parametrize
    async def test_method_action_overload_4(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="hard_reboot",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_action_overload_4(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.with_raw_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="hard_reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_action_overload_4(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.with_streaming_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="hard_reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_action_overload_4(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="hard_reboot",
            )

    @parametrize
    async def test_method_action_overload_5(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="update_tags",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_action_overload_5(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.with_raw_response.action(
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
    async def test_streaming_response_action_overload_5(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.with_streaming_response.action(
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
    async def test_path_params_action_overload_5(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="update_tags",
                tags={"foo": "my-tag-value"},
            )

    @parametrize
    async def test_method_action_overload_6(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="resize",
            servers_count=5,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_action_overload_6(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.with_raw_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="resize",
            servers_count=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_action_overload_6(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.with_streaming_response.action(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            action="resize",
            servers_count=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_action_overload_6(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.with_raw_response.action(
                cluster_id="",
                project_id=1,
                region_id=7,
                action="resize",
                servers_count=5,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.gpu_virtual.clusters.get(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(GPUVirtualCluster, cluster, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.with_raw_response.get(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(GPUVirtualCluster, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.with_streaming_response.get(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(GPUVirtualCluster, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.with_raw_response.get(
                cluster_id="",
                project_id=1,
                region_id=7,
            )

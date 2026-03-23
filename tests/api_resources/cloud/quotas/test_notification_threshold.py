# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.quotas import NotificationThreshold

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotificationThreshold:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        notification_threshold = client.cloud.quotas.notification_threshold.update(
            client_id=3,
            threshold=95,
        )
        assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        notification_threshold = client.cloud.quotas.notification_threshold.update(
            client_id=3,
            threshold=95,
            last_message={
                "global_quotas": {
                    "inference_cpu_millicore_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_cpu_millicore_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_gpu_a100_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_gpu_a100_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_gpu_h100_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_gpu_h100_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_gpu_l40s_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_gpu_l40s_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_instance_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_instance_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "keypair_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "keypair_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "project_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "project_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                },
                "regional_quotas": [
                    {
                        "region_id": 2,
                        "region_name": "Luxembourg",
                        "baremetal_basic_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_basic_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_a100_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_a100_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_h100_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_h100_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_h200_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_h200_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_l40s_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_l40s_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_hf_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_hf_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_infrastructure_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_infrastructure_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_network_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_network_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_storage_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_storage_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_container_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_container_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_cpu_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_cpu_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_gpu_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_gpu_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_ram_size_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_ram_size_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "cluster_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "cluster_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "cpu_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "cpu_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "dbaas_postgres_cluster_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "dbaas_postgres_cluster_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "external_ip_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "external_ip_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_cpu_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_cpu_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_function_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_function_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_namespace_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_namespace_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_ram_size_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_ram_size_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "firewall_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "firewall_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "floating_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "floating_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_a100_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_a100_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_h100_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_h100_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_h200_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_h200_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_l40s_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_l40s_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "image_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "image_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "image_size_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "image_size_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "ipu_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "ipu_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "laas_topic_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "laas_topic_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "loadbalancer_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "loadbalancer_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "network_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "network_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "ram_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "ram_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "registry_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "registry_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "registry_storage_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "registry_storage_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "router_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "router_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "secret_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "secret_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "servergroup_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "servergroup_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "sfs_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "sfs_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "sfs_size_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "sfs_size_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "shared_vm_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "shared_vm_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "snapshot_schedule_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "snapshot_schedule_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "subnet_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "subnet_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "vm_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "vm_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_size_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_size_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_snapshots_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_snapshots_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_snapshots_size_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_snapshots_size_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                    }
                ],
            },
            last_sending=None,
        )
        assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.quotas.notification_threshold.with_raw_response.update(
            client_id=3,
            threshold=95,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_threshold = response.parse()
        assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.quotas.notification_threshold.with_streaming_response.update(
            client_id=3,
            threshold=95,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_threshold = response.parse()
            assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        notification_threshold = client.cloud.quotas.notification_threshold.delete(
            3,
        )
        assert notification_threshold is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.quotas.notification_threshold.with_raw_response.delete(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_threshold = response.parse()
        assert notification_threshold is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.quotas.notification_threshold.with_streaming_response.delete(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_threshold = response.parse()
            assert notification_threshold is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        notification_threshold = client.cloud.quotas.notification_threshold.get(
            3,
        )
        assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.quotas.notification_threshold.with_raw_response.get(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_threshold = response.parse()
        assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.quotas.notification_threshold.with_streaming_response.get(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_threshold = response.parse()
            assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNotificationThreshold:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        notification_threshold = await async_client.cloud.quotas.notification_threshold.update(
            client_id=3,
            threshold=95,
        )
        assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        notification_threshold = await async_client.cloud.quotas.notification_threshold.update(
            client_id=3,
            threshold=95,
            last_message={
                "global_quotas": {
                    "inference_cpu_millicore_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_cpu_millicore_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_gpu_a100_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_gpu_a100_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_gpu_h100_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_gpu_h100_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_gpu_l40s_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_gpu_l40s_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_instance_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "inference_instance_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "keypair_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "keypair_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "project_count_limit": {
                        "limit": 10,
                        "usage": 8,
                    },
                    "project_count_usage": {
                        "limit": 10,
                        "usage": 8,
                    },
                },
                "regional_quotas": [
                    {
                        "region_id": 2,
                        "region_name": "Luxembourg",
                        "baremetal_basic_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_basic_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_a100_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_a100_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_h100_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_h100_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_h200_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_h200_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_l40s_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_gpu_l40s_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_hf_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_hf_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_infrastructure_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_infrastructure_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_network_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_network_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_storage_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "baremetal_storage_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_container_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_container_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_cpu_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_cpu_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_gpu_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_gpu_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_ram_size_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "caas_ram_size_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "cluster_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "cluster_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "cpu_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "cpu_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "dbaas_postgres_cluster_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "dbaas_postgres_cluster_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "external_ip_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "external_ip_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_cpu_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_cpu_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_function_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_function_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_namespace_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_namespace_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_ram_size_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "faas_ram_size_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "firewall_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "firewall_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "floating_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "floating_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_a100_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_a100_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_h100_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_h100_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_h200_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_h200_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_l40s_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "gpu_virtual_l40s_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "image_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "image_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "image_size_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "image_size_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "ipu_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "ipu_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "laas_topic_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "laas_topic_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "loadbalancer_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "loadbalancer_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "network_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "network_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "ram_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "ram_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "registry_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "registry_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "registry_storage_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "registry_storage_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "router_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "router_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "secret_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "secret_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "servergroup_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "servergroup_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "sfs_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "sfs_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "sfs_size_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "sfs_size_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "shared_vm_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "shared_vm_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "snapshot_schedule_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "snapshot_schedule_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "subnet_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "subnet_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "vm_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "vm_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_size_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_size_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_snapshots_count_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_snapshots_count_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_snapshots_size_limit": {
                            "limit": 10,
                            "usage": 8,
                        },
                        "volume_snapshots_size_usage": {
                            "limit": 10,
                            "usage": 8,
                        },
                    }
                ],
            },
            last_sending=None,
        )
        assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.quotas.notification_threshold.with_raw_response.update(
            client_id=3,
            threshold=95,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_threshold = await response.parse()
        assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.quotas.notification_threshold.with_streaming_response.update(
            client_id=3,
            threshold=95,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_threshold = await response.parse()
            assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        notification_threshold = await async_client.cloud.quotas.notification_threshold.delete(
            3,
        )
        assert notification_threshold is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.quotas.notification_threshold.with_raw_response.delete(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_threshold = await response.parse()
        assert notification_threshold is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.quotas.notification_threshold.with_streaming_response.delete(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_threshold = await response.parse()
            assert notification_threshold is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        notification_threshold = await async_client.cloud.quotas.notification_threshold.get(
            3,
        )
        assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.quotas.notification_threshold.with_raw_response.get(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_threshold = await response.parse()
        assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.quotas.notification_threshold.with_streaming_response.get(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_threshold = await response.parse()
            assert_matches_type(NotificationThreshold, notification_threshold, path=["response"])

        assert cast(Any, response.is_closed) is True

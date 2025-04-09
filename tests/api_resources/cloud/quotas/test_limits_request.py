# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.quotas import LimitsRequest

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLimitsRequest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        limits_request = client.cloud.quotas.limits_request.create(
            description="Scale up mysql cluster",
            requested_limits={},
        )
        assert limits_request is None

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        limits_request = client.cloud.quotas.limits_request.create(
            description="Scale up mysql cluster",
            requested_limits={
                "global_limits": {
                    "inference_cpu_millicore_count_limit": 0,
                    "inference_gpu_a100_count_limit": 0,
                    "inference_gpu_h100_count_limit": 0,
                    "inference_gpu_l40s_count_limit": 0,
                    "inference_instance_count_limit": 0,
                    "keypair_count_limit": 100,
                    "project_count_limit": 2,
                },
                "regional_limits": [
                    {
                        "baremetal_basic_count_limit": 0,
                        "baremetal_gpu_count_limit": 0,
                        "baremetal_hf_count_limit": 0,
                        "baremetal_infrastructure_count_limit": 0,
                        "baremetal_network_count_limit": 0,
                        "baremetal_storage_count_limit": 0,
                        "caas_container_count_limit": 0,
                        "caas_cpu_count_limit": 0,
                        "caas_gpu_count_limit": 0,
                        "caas_ram_size_limit": 0,
                        "cluster_count_limit": 0,
                        "cpu_count_limit": 0,
                        "dbaas_postgres_cluster_count_limit": 0,
                        "external_ip_count_limit": 0,
                        "faas_cpu_count_limit": 0,
                        "faas_function_count_limit": 0,
                        "faas_namespace_count_limit": 0,
                        "faas_ram_size_limit": 0,
                        "firewall_count_limit": 0,
                        "floating_count_limit": 0,
                        "gpu_count_limit": 0,
                        "gpu_virtual_a100_count_limit": 0,
                        "gpu_virtual_h100_count_limit": 0,
                        "gpu_virtual_l40s_count_limit": 0,
                        "image_count_limit": 0,
                        "image_size_limit": 0,
                        "ipu_count_limit": 0,
                        "laas_topic_count_limit": 0,
                        "loadbalancer_count_limit": 0,
                        "network_count_limit": 0,
                        "ram_limit": 0,
                        "region_id": 1,
                        "registry_count_limit": 0,
                        "registry_storage_limit": 0,
                        "router_count_limit": 0,
                        "secret_count_limit": 0,
                        "servergroup_count_limit": 0,
                        "sfs_count_limit": 0,
                        "sfs_size_limit": 0,
                        "shared_vm_count_limit": 0,
                        "snapshot_schedule_count_limit": 0,
                        "subnet_count_limit": 0,
                        "vm_count_limit": 0,
                        "volume_count_limit": 0,
                        "volume_size_limit": 0,
                        "volume_snapshots_count_limit": 0,
                        "volume_snapshots_size_limit": 0,
                    }
                ],
            },
            client_id=1,
        )
        assert limits_request is None

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.quotas.limits_request.with_raw_response.create(
            description="Scale up mysql cluster",
            requested_limits={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limits_request = response.parse()
        assert limits_request is None

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.quotas.limits_request.with_streaming_response.create(
            description="Scale up mysql cluster",
            requested_limits={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limits_request = response.parse()
            assert limits_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gcore) -> None:
        limits_request = client.cloud.quotas.limits_request.retrieve(
            "request_id",
        )
        assert_matches_type(LimitsRequest, limits_request, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gcore) -> None:
        response = client.cloud.quotas.limits_request.with_raw_response.retrieve(
            "request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limits_request = response.parse()
        assert_matches_type(LimitsRequest, limits_request, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gcore) -> None:
        with client.cloud.quotas.limits_request.with_streaming_response.retrieve(
            "request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limits_request = response.parse()
            assert_matches_type(LimitsRequest, limits_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.cloud.quotas.limits_request.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        limits_request = client.cloud.quotas.limits_request.list()
        assert limits_request is None

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        limits_request = client.cloud.quotas.limits_request.list(
            limit=1000,
            offset=0,
            status=["done", "in progress"],
        )
        assert limits_request is None

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.quotas.limits_request.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limits_request = response.parse()
        assert limits_request is None

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.quotas.limits_request.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limits_request = response.parse()
            assert limits_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        limits_request = client.cloud.quotas.limits_request.delete(
            "request_id",
        )
        assert limits_request is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.quotas.limits_request.with_raw_response.delete(
            "request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limits_request = response.parse()
        assert limits_request is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.quotas.limits_request.with_streaming_response.delete(
            "request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limits_request = response.parse()
            assert limits_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.cloud.quotas.limits_request.with_raw_response.delete(
                "",
            )


class TestAsyncLimitsRequest:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        limits_request = await async_client.cloud.quotas.limits_request.create(
            description="Scale up mysql cluster",
            requested_limits={},
        )
        assert limits_request is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        limits_request = await async_client.cloud.quotas.limits_request.create(
            description="Scale up mysql cluster",
            requested_limits={
                "global_limits": {
                    "inference_cpu_millicore_count_limit": 0,
                    "inference_gpu_a100_count_limit": 0,
                    "inference_gpu_h100_count_limit": 0,
                    "inference_gpu_l40s_count_limit": 0,
                    "inference_instance_count_limit": 0,
                    "keypair_count_limit": 100,
                    "project_count_limit": 2,
                },
                "regional_limits": [
                    {
                        "baremetal_basic_count_limit": 0,
                        "baremetal_gpu_count_limit": 0,
                        "baremetal_hf_count_limit": 0,
                        "baremetal_infrastructure_count_limit": 0,
                        "baremetal_network_count_limit": 0,
                        "baremetal_storage_count_limit": 0,
                        "caas_container_count_limit": 0,
                        "caas_cpu_count_limit": 0,
                        "caas_gpu_count_limit": 0,
                        "caas_ram_size_limit": 0,
                        "cluster_count_limit": 0,
                        "cpu_count_limit": 0,
                        "dbaas_postgres_cluster_count_limit": 0,
                        "external_ip_count_limit": 0,
                        "faas_cpu_count_limit": 0,
                        "faas_function_count_limit": 0,
                        "faas_namespace_count_limit": 0,
                        "faas_ram_size_limit": 0,
                        "firewall_count_limit": 0,
                        "floating_count_limit": 0,
                        "gpu_count_limit": 0,
                        "gpu_virtual_a100_count_limit": 0,
                        "gpu_virtual_h100_count_limit": 0,
                        "gpu_virtual_l40s_count_limit": 0,
                        "image_count_limit": 0,
                        "image_size_limit": 0,
                        "ipu_count_limit": 0,
                        "laas_topic_count_limit": 0,
                        "loadbalancer_count_limit": 0,
                        "network_count_limit": 0,
                        "ram_limit": 0,
                        "region_id": 1,
                        "registry_count_limit": 0,
                        "registry_storage_limit": 0,
                        "router_count_limit": 0,
                        "secret_count_limit": 0,
                        "servergroup_count_limit": 0,
                        "sfs_count_limit": 0,
                        "sfs_size_limit": 0,
                        "shared_vm_count_limit": 0,
                        "snapshot_schedule_count_limit": 0,
                        "subnet_count_limit": 0,
                        "vm_count_limit": 0,
                        "volume_count_limit": 0,
                        "volume_size_limit": 0,
                        "volume_snapshots_count_limit": 0,
                        "volume_snapshots_size_limit": 0,
                    }
                ],
            },
            client_id=1,
        )
        assert limits_request is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.quotas.limits_request.with_raw_response.create(
            description="Scale up mysql cluster",
            requested_limits={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limits_request = await response.parse()
        assert limits_request is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.quotas.limits_request.with_streaming_response.create(
            description="Scale up mysql cluster",
            requested_limits={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limits_request = await response.parse()
            assert limits_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGcore) -> None:
        limits_request = await async_client.cloud.quotas.limits_request.retrieve(
            "request_id",
        )
        assert_matches_type(LimitsRequest, limits_request, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.quotas.limits_request.with_raw_response.retrieve(
            "request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limits_request = await response.parse()
        assert_matches_type(LimitsRequest, limits_request, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.quotas.limits_request.with_streaming_response.retrieve(
            "request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limits_request = await response.parse()
            assert_matches_type(LimitsRequest, limits_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.cloud.quotas.limits_request.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        limits_request = await async_client.cloud.quotas.limits_request.list()
        assert limits_request is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        limits_request = await async_client.cloud.quotas.limits_request.list(
            limit=1000,
            offset=0,
            status=["done", "in progress"],
        )
        assert limits_request is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.quotas.limits_request.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limits_request = await response.parse()
        assert limits_request is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.quotas.limits_request.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limits_request = await response.parse()
            assert limits_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        limits_request = await async_client.cloud.quotas.limits_request.delete(
            "request_id",
        )
        assert limits_request is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.quotas.limits_request.with_raw_response.delete(
            "request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limits_request = await response.parse()
        assert limits_request is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.quotas.limits_request.with_streaming_response.delete(
            "request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limits_request = await response.parse()
            assert limits_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.cloud.quotas.limits_request.with_raw_response.delete(
                "",
            )

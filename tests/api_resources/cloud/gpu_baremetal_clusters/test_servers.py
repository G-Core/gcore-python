# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import Console, TaskIDList, GPUBaremetalClusterServer

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
            delete_floatings=True,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.servers.with_raw_response.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.servers.with_raw_response.delete(
                instance_id="instance_id",
                project_id=0,
                region_id=0,
                cluster_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.servers.with_raw_response.delete(
                instance_id="",
                project_id=0,
                region_id=0,
                cluster_id="cluster_id",
            )

    @parametrize
    def test_method_attach_interface_overload_1(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_method_attach_interface_with_all_params_overload_1(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            ddos_profile={
                "profile_template": 29,
                "fields": [
                    {
                        "base_field": 10,
                        "field_name": "field_name",
                        "field_value": [45046, 45047],
                        "value": None,
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="interface_name",
            ip_family="dual",
            port_group=0,
            security_groups=[
                {"id": "4536dba1-93b1-492e-b3df-270b6b9f3650"},
                {"id": "cee2ca1f-507a-4a31-b714-f6c1ffb4bdfa"},
            ],
            type="external",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_attach_interface_overload_1(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_attach_interface_overload_1(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_attach_interface_overload_1(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_attach_interface_overload_2(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_method_attach_interface_with_all_params_overload_2(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            ddos_profile={
                "profile_template": 29,
                "fields": [
                    {
                        "base_field": 10,
                        "field_name": "field_name",
                        "field_value": [45046, 45047],
                        "value": None,
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="my-subnet-interface",
            port_group=0,
            security_groups=[
                {"id": "4536dba1-93b1-492e-b3df-270b6b9f3650"},
                {"id": "cee2ca1f-507a-4a31-b714-f6c1ffb4bdfa"},
            ],
            type="subnet",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_attach_interface_overload_2(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_attach_interface_overload_2(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_attach_interface_overload_2(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
                instance_id="",
                project_id=0,
                region_id=0,
                subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            )

    @parametrize
    def test_method_attach_interface_overload_3(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_method_attach_interface_with_all_params_overload_3(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            ddos_profile={
                "profile_template": 29,
                "fields": [
                    {
                        "base_field": 10,
                        "field_name": "field_name",
                        "field_value": [45046, 45047],
                        "value": None,
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="my-any-subnet-interface",
            ip_family="dual",
            port_group=0,
            security_groups=[
                {"id": "4536dba1-93b1-492e-b3df-270b6b9f3650"},
                {"id": "cee2ca1f-507a-4a31-b714-f6c1ffb4bdfa"},
            ],
            type="any_subnet",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_attach_interface_overload_3(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_attach_interface_overload_3(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_attach_interface_overload_3(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
                instance_id="",
                project_id=0,
                region_id=0,
                network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            )

    @parametrize
    def test_method_attach_interface_overload_4(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            port_id="59905c8e-2619-420a-b046-536096473370",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_method_attach_interface_with_all_params_overload_4(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            port_id="59905c8e-2619-420a-b046-536096473370",
            ddos_profile={
                "profile_template": 29,
                "fields": [
                    {
                        "base_field": 10,
                        "field_name": "field_name",
                        "field_value": [45046, 45047],
                        "value": None,
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="my-rfip-interface",
            port_group=0,
            security_groups=[
                {"id": "4536dba1-93b1-492e-b3df-270b6b9f3650"},
                {"id": "cee2ca1f-507a-4a31-b714-f6c1ffb4bdfa"},
            ],
            type="reserved_fixed_ip",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_attach_interface_overload_4(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            port_id="59905c8e-2619-420a-b046-536096473370",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_attach_interface_overload_4(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            port_id="59905c8e-2619-420a-b046-536096473370",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_attach_interface_overload_4(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
                instance_id="",
                project_id=0,
                region_id=0,
                port_id="59905c8e-2619-420a-b046-536096473370",
            )

    @parametrize
    def test_method_detach_interface(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.detach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            port_id="351b0dd7-ca09-431c-be53-935db3785067",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_detach_interface(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.servers.with_raw_response.detach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            port_id="351b0dd7-ca09-431c-be53-935db3785067",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_detach_interface(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.detach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            port_id="351b0dd7-ca09-431c-be53-935db3785067",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_detach_interface(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.servers.with_raw_response.detach_interface(
                instance_id="",
                project_id=0,
                region_id=0,
                ip_address="192.168.123.20",
                port_id="351b0dd7-ca09-431c-be53-935db3785067",
            )

    @parametrize
    def test_method_get_console(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Console, server, path=["response"])

    @parametrize
    def test_raw_response_get_console(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.servers.with_raw_response.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(Console, server, path=["response"])

    @parametrize
    def test_streaming_response_get_console(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(Console, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_console(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.servers.with_raw_response.get_console(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_powercycle(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.powercycle(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServer, server, path=["response"])

    @parametrize
    def test_raw_response_powercycle(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.servers.with_raw_response.powercycle(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(GPUBaremetalClusterServer, server, path=["response"])

    @parametrize
    def test_streaming_response_powercycle(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.powercycle(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(GPUBaremetalClusterServer, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_powercycle(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.servers.with_raw_response.powercycle(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_reboot(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal_clusters.servers.reboot(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServer, server, path=["response"])

    @parametrize
    def test_raw_response_reboot(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.servers.with_raw_response.reboot(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(GPUBaremetalClusterServer, server, path=["response"])

    @parametrize
    def test_streaming_response_reboot(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.reboot(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(GPUBaremetalClusterServer, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reboot(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.servers.with_raw_response.reboot(
                instance_id="",
                project_id=0,
                region_id=0,
            )


class TestAsyncServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
            delete_floatings=True,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.delete(
                instance_id="instance_id",
                project_id=0,
                region_id=0,
                cluster_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.delete(
                instance_id="",
                project_id=0,
                region_id=0,
                cluster_id="cluster_id",
            )

    @parametrize
    async def test_method_attach_interface_overload_1(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_method_attach_interface_with_all_params_overload_1(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            ddos_profile={
                "profile_template": 29,
                "fields": [
                    {
                        "base_field": 10,
                        "field_name": "field_name",
                        "field_value": [45046, 45047],
                        "value": None,
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="interface_name",
            ip_family="dual",
            port_group=0,
            security_groups=[
                {"id": "4536dba1-93b1-492e-b3df-270b6b9f3650"},
                {"id": "cee2ca1f-507a-4a31-b714-f6c1ffb4bdfa"},
            ],
            type="external",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_attach_interface_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_attach_interface_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_attach_interface_overload_1(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_attach_interface_overload_2(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_method_attach_interface_with_all_params_overload_2(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            ddos_profile={
                "profile_template": 29,
                "fields": [
                    {
                        "base_field": 10,
                        "field_name": "field_name",
                        "field_value": [45046, 45047],
                        "value": None,
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="my-subnet-interface",
            port_group=0,
            security_groups=[
                {"id": "4536dba1-93b1-492e-b3df-270b6b9f3650"},
                {"id": "cee2ca1f-507a-4a31-b714-f6c1ffb4bdfa"},
            ],
            type="subnet",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_attach_interface_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_attach_interface_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_attach_interface_overload_2(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
                instance_id="",
                project_id=0,
                region_id=0,
                subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            )

    @parametrize
    async def test_method_attach_interface_overload_3(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_method_attach_interface_with_all_params_overload_3(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            ddos_profile={
                "profile_template": 29,
                "fields": [
                    {
                        "base_field": 10,
                        "field_name": "field_name",
                        "field_value": [45046, 45047],
                        "value": None,
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="my-any-subnet-interface",
            ip_family="dual",
            port_group=0,
            security_groups=[
                {"id": "4536dba1-93b1-492e-b3df-270b6b9f3650"},
                {"id": "cee2ca1f-507a-4a31-b714-f6c1ffb4bdfa"},
            ],
            type="any_subnet",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_attach_interface_overload_3(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_attach_interface_overload_3(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_attach_interface_overload_3(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
                instance_id="",
                project_id=0,
                region_id=0,
                network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            )

    @parametrize
    async def test_method_attach_interface_overload_4(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            port_id="59905c8e-2619-420a-b046-536096473370",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_method_attach_interface_with_all_params_overload_4(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            port_id="59905c8e-2619-420a-b046-536096473370",
            ddos_profile={
                "profile_template": 29,
                "fields": [
                    {
                        "base_field": 10,
                        "field_name": "field_name",
                        "field_value": [45046, 45047],
                        "value": None,
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="my-rfip-interface",
            port_group=0,
            security_groups=[
                {"id": "4536dba1-93b1-492e-b3df-270b6b9f3650"},
                {"id": "cee2ca1f-507a-4a31-b714-f6c1ffb4bdfa"},
            ],
            type="reserved_fixed_ip",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_attach_interface_overload_4(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            port_id="59905c8e-2619-420a-b046-536096473370",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_attach_interface_overload_4(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.attach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            port_id="59905c8e-2619-420a-b046-536096473370",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_attach_interface_overload_4(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.attach_interface(
                instance_id="",
                project_id=0,
                region_id=0,
                port_id="59905c8e-2619-420a-b046-536096473370",
            )

    @parametrize
    async def test_method_detach_interface(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.detach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            port_id="351b0dd7-ca09-431c-be53-935db3785067",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_detach_interface(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.detach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            port_id="351b0dd7-ca09-431c-be53-935db3785067",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_detach_interface(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.detach_interface(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            port_id="351b0dd7-ca09-431c-be53-935db3785067",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_detach_interface(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.detach_interface(
                instance_id="",
                project_id=0,
                region_id=0,
                ip_address="192.168.123.20",
                port_id="351b0dd7-ca09-431c-be53-935db3785067",
            )

    @parametrize
    async def test_method_get_console(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Console, server, path=["response"])

    @parametrize
    async def test_raw_response_get_console(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(Console, server, path=["response"])

    @parametrize
    async def test_streaming_response_get_console(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(Console, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_console(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.get_console(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_powercycle(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.powercycle(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServer, server, path=["response"])

    @parametrize
    async def test_raw_response_powercycle(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.powercycle(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(GPUBaremetalClusterServer, server, path=["response"])

    @parametrize
    async def test_streaming_response_powercycle(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.powercycle(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(GPUBaremetalClusterServer, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_powercycle(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.powercycle(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_reboot(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal_clusters.servers.reboot(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServer, server, path=["response"])

    @parametrize
    async def test_raw_response_reboot(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.reboot(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(GPUBaremetalClusterServer, server, path=["response"])

    @parametrize
    async def test_streaming_response_reboot(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.servers.with_streaming_response.reboot(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(GPUBaremetalClusterServer, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reboot(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.servers.with_raw_response.reboot(
                instance_id="",
                project_id=0,
                region_id=0,
            )

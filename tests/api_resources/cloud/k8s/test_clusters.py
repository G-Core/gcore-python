# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import TaskIDList, K8SClusterVersionList
from gcore.types.cloud.k8s import (
    K8SCluster,
    K8SClusterList,
    K8SClusterKubeconfig,
    K8SClusterCertificate,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClusters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        cluster = client.cloud.k8s.clusters.create(
            project_id=0,
            region_id=0,
            keypair="some_keypair",
            name="string",
            pools=[
                {
                    "flavor_id": "g1-standard-1-2",
                    "min_node_count": 3,
                    "name": "my-pool",
                }
            ],
            version="1.28.1",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        cluster = client.cloud.k8s.clusters.create(
            project_id=0,
            region_id=0,
            keypair="some_keypair",
            name="string",
            pools=[
                {
                    "flavor_id": "g1-standard-1-2",
                    "min_node_count": 3,
                    "name": "my-pool",
                    "auto_healing_enabled": True,
                    "boot_volume_size": 50,
                    "boot_volume_type": "ssd_hiiops",
                    "crio_config": {"default-ulimits": "nofile=1024:2048"},
                    "is_public_ipv4": True,
                    "kubelet_config": {"podMaxPids": "4096"},
                    "labels": {"my-label": "foo"},
                    "max_node_count": 5,
                    "servergroup_policy": "affinity",
                    "taints": {"my-taint": "bar:NoSchedule"},
                }
            ],
            version="1.28.1",
            add_ons={
                "slurm": {
                    "enabled": True,
                    "file_share_id": "cbc94d0e-06c6-4d12-9e86-9782ba14fc8c",
                    "ssh_key_ids": ["25735292-bd97-44b0-a1af-d7eab876261d", "efc01f3a-35b9-4385-89f9-e38439093ee7"],
                    "worker_count": 2,
                }
            },
            authentication={
                "oidc": {
                    "client_id": "kubernetes",
                    "groups_claim": "groups",
                    "groups_prefix": "oidc:",
                    "issuer_url": "https://accounts.provider.example",
                    "required_claims": {"claim": "value"},
                    "signing_algs": ["RS256", "RS512"],
                    "username_claim": "sub",
                    "username_prefix": "oidc:",
                }
            },
            autoscaler_config={"scale-down-unneeded-time": "5m"},
            cni={
                "cilium": {
                    "encryption": True,
                    "hubble_relay": True,
                    "hubble_ui": True,
                    "lb_acceleration": True,
                    "lb_mode": "snat",
                    "mask_size": 24,
                    "mask_size_v6": 120,
                    "routing_mode": "tunnel",
                    "tunnel": "geneve",
                },
                "provider": "cilium",
            },
            csi={"nfs": {"vast_enabled": True}},
            ddos_profile={
                "enabled": True,
                "fields": [
                    {
                        "base_field": 10,
                        "field_value": [45046, 45047],
                        "value": None,
                    }
                ],
                "profile_template": 29,
                "profile_template_name": "profile_template_name",
            },
            fixed_network="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            fixed_subnet="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            is_ipv6=True,
            logging={
                "destination_region_id": 1,
                "enabled": True,
                "retention_policy": {"period": 45},
                "topic_name": "my-log-name",
            },
            pods_ip_pool="172.16.0.0/18",
            pods_ipv6_pool="2a03:90c0:88:393::/64",
            services_ip_pool="172.24.0.0/18",
            services_ipv6_pool="2a03:90c0:88:381::/108",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.with_raw_response.create(
            project_id=0,
            region_id=0,
            keypair="some_keypair",
            name="string",
            pools=[
                {
                    "flavor_id": "g1-standard-1-2",
                    "min_node_count": 3,
                    "name": "my-pool",
                }
            ],
            version="1.28.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.with_streaming_response.create(
            project_id=0,
            region_id=0,
            keypair="some_keypair",
            name="string",
            pools=[
                {
                    "flavor_id": "g1-standard-1-2",
                    "min_node_count": 3,
                    "name": "my-pool",
                }
            ],
            version="1.28.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        cluster = client.cloud.k8s.clusters.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        cluster = client.cloud.k8s.clusters.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            add_ons={
                "slurm": {
                    "enabled": True,
                    "file_share_id": "cbc94d0e-06c6-4d12-9e86-9782ba14fc8c",
                    "ssh_key_ids": ["25735292-bd97-44b0-a1af-d7eab876261d", "efc01f3a-35b9-4385-89f9-e38439093ee7"],
                    "worker_count": 2,
                }
            },
            authentication={
                "oidc": {
                    "client_id": "kubernetes",
                    "groups_claim": "groups",
                    "groups_prefix": "oidc:",
                    "issuer_url": "https://accounts.provider.example",
                    "required_claims": {"claim": "value"},
                    "signing_algs": ["RS256", "RS512"],
                    "username_claim": "sub",
                    "username_prefix": "oidc:",
                }
            },
            autoscaler_config={"scale-down-unneeded-time": "5m"},
            cni={
                "cilium": {
                    "encryption": True,
                    "hubble_relay": True,
                    "hubble_ui": True,
                    "lb_acceleration": True,
                    "lb_mode": "snat",
                    "mask_size": 24,
                    "mask_size_v6": 120,
                    "routing_mode": "tunnel",
                    "tunnel": "geneve",
                },
                "provider": "cilium",
            },
            ddos_profile={
                "enabled": True,
                "fields": [
                    {
                        "base_field": 10,
                        "field_value": [45046, 45047],
                        "value": None,
                    }
                ],
                "profile_template": 29,
                "profile_template_name": "profile_template_name",
            },
            logging={
                "destination_region_id": 1,
                "enabled": True,
                "retention_policy": {"period": 45},
                "topic_name": "my-log-name",
            },
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.with_raw_response.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.with_streaming_response.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.with_raw_response.update(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        cluster = client.cloud.k8s.clusters.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SClusterList, cluster, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(K8SClusterList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(K8SClusterList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        cluster = client.cloud.k8s.clusters.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        cluster = client.cloud.k8s.clusters.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            volumes="volumes",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.with_raw_response.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.with_streaming_response.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.with_raw_response.delete(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        cluster = client.cloud.k8s.clusters.get(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SCluster, cluster, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.with_raw_response.get(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(K8SCluster, cluster, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.with_streaming_response.get(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(K8SCluster, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.with_raw_response.get(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_get_certificate(self, client: Gcore) -> None:
        cluster = client.cloud.k8s.clusters.get_certificate(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SClusterCertificate, cluster, path=["response"])

    @parametrize
    def test_raw_response_get_certificate(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.with_raw_response.get_certificate(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(K8SClusterCertificate, cluster, path=["response"])

    @parametrize
    def test_streaming_response_get_certificate(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.with_streaming_response.get_certificate(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(K8SClusterCertificate, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_certificate(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.with_raw_response.get_certificate(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_get_kubeconfig(self, client: Gcore) -> None:
        cluster = client.cloud.k8s.clusters.get_kubeconfig(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SClusterKubeconfig, cluster, path=["response"])

    @parametrize
    def test_raw_response_get_kubeconfig(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.with_raw_response.get_kubeconfig(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(K8SClusterKubeconfig, cluster, path=["response"])

    @parametrize
    def test_streaming_response_get_kubeconfig(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.with_streaming_response.get_kubeconfig(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(K8SClusterKubeconfig, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_kubeconfig(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.with_raw_response.get_kubeconfig(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_list_versions_for_upgrade(self, client: Gcore) -> None:
        cluster = client.cloud.k8s.clusters.list_versions_for_upgrade(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SClusterVersionList, cluster, path=["response"])

    @parametrize
    def test_raw_response_list_versions_for_upgrade(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.with_raw_response.list_versions_for_upgrade(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(K8SClusterVersionList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_list_versions_for_upgrade(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.with_streaming_response.list_versions_for_upgrade(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(K8SClusterVersionList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_versions_for_upgrade(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.with_raw_response.list_versions_for_upgrade(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_upgrade(self, client: Gcore) -> None:
        cluster = client.cloud.k8s.clusters.upgrade(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            version="v1.28.1",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_upgrade(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.with_raw_response.upgrade(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            version="v1.28.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_upgrade(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.with_streaming_response.upgrade(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            version="v1.28.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upgrade(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.with_raw_response.upgrade(
                cluster_name="",
                project_id=0,
                region_id=0,
                version="v1.28.1",
            )


class TestAsyncClusters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.k8s.clusters.create(
            project_id=0,
            region_id=0,
            keypair="some_keypair",
            name="string",
            pools=[
                {
                    "flavor_id": "g1-standard-1-2",
                    "min_node_count": 3,
                    "name": "my-pool",
                }
            ],
            version="1.28.1",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.k8s.clusters.create(
            project_id=0,
            region_id=0,
            keypair="some_keypair",
            name="string",
            pools=[
                {
                    "flavor_id": "g1-standard-1-2",
                    "min_node_count": 3,
                    "name": "my-pool",
                    "auto_healing_enabled": True,
                    "boot_volume_size": 50,
                    "boot_volume_type": "ssd_hiiops",
                    "crio_config": {"default-ulimits": "nofile=1024:2048"},
                    "is_public_ipv4": True,
                    "kubelet_config": {"podMaxPids": "4096"},
                    "labels": {"my-label": "foo"},
                    "max_node_count": 5,
                    "servergroup_policy": "affinity",
                    "taints": {"my-taint": "bar:NoSchedule"},
                }
            ],
            version="1.28.1",
            add_ons={
                "slurm": {
                    "enabled": True,
                    "file_share_id": "cbc94d0e-06c6-4d12-9e86-9782ba14fc8c",
                    "ssh_key_ids": ["25735292-bd97-44b0-a1af-d7eab876261d", "efc01f3a-35b9-4385-89f9-e38439093ee7"],
                    "worker_count": 2,
                }
            },
            authentication={
                "oidc": {
                    "client_id": "kubernetes",
                    "groups_claim": "groups",
                    "groups_prefix": "oidc:",
                    "issuer_url": "https://accounts.provider.example",
                    "required_claims": {"claim": "value"},
                    "signing_algs": ["RS256", "RS512"],
                    "username_claim": "sub",
                    "username_prefix": "oidc:",
                }
            },
            autoscaler_config={"scale-down-unneeded-time": "5m"},
            cni={
                "cilium": {
                    "encryption": True,
                    "hubble_relay": True,
                    "hubble_ui": True,
                    "lb_acceleration": True,
                    "lb_mode": "snat",
                    "mask_size": 24,
                    "mask_size_v6": 120,
                    "routing_mode": "tunnel",
                    "tunnel": "geneve",
                },
                "provider": "cilium",
            },
            csi={"nfs": {"vast_enabled": True}},
            ddos_profile={
                "enabled": True,
                "fields": [
                    {
                        "base_field": 10,
                        "field_value": [45046, 45047],
                        "value": None,
                    }
                ],
                "profile_template": 29,
                "profile_template_name": "profile_template_name",
            },
            fixed_network="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            fixed_subnet="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            is_ipv6=True,
            logging={
                "destination_region_id": 1,
                "enabled": True,
                "retention_policy": {"period": 45},
                "topic_name": "my-log-name",
            },
            pods_ip_pool="172.16.0.0/18",
            pods_ipv6_pool="2a03:90c0:88:393::/64",
            services_ip_pool="172.24.0.0/18",
            services_ipv6_pool="2a03:90c0:88:381::/108",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.with_raw_response.create(
            project_id=0,
            region_id=0,
            keypair="some_keypair",
            name="string",
            pools=[
                {
                    "flavor_id": "g1-standard-1-2",
                    "min_node_count": 3,
                    "name": "my-pool",
                }
            ],
            version="1.28.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.with_streaming_response.create(
            project_id=0,
            region_id=0,
            keypair="some_keypair",
            name="string",
            pools=[
                {
                    "flavor_id": "g1-standard-1-2",
                    "min_node_count": 3,
                    "name": "my-pool",
                }
            ],
            version="1.28.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.k8s.clusters.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.k8s.clusters.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            add_ons={
                "slurm": {
                    "enabled": True,
                    "file_share_id": "cbc94d0e-06c6-4d12-9e86-9782ba14fc8c",
                    "ssh_key_ids": ["25735292-bd97-44b0-a1af-d7eab876261d", "efc01f3a-35b9-4385-89f9-e38439093ee7"],
                    "worker_count": 2,
                }
            },
            authentication={
                "oidc": {
                    "client_id": "kubernetes",
                    "groups_claim": "groups",
                    "groups_prefix": "oidc:",
                    "issuer_url": "https://accounts.provider.example",
                    "required_claims": {"claim": "value"},
                    "signing_algs": ["RS256", "RS512"],
                    "username_claim": "sub",
                    "username_prefix": "oidc:",
                }
            },
            autoscaler_config={"scale-down-unneeded-time": "5m"},
            cni={
                "cilium": {
                    "encryption": True,
                    "hubble_relay": True,
                    "hubble_ui": True,
                    "lb_acceleration": True,
                    "lb_mode": "snat",
                    "mask_size": 24,
                    "mask_size_v6": 120,
                    "routing_mode": "tunnel",
                    "tunnel": "geneve",
                },
                "provider": "cilium",
            },
            ddos_profile={
                "enabled": True,
                "fields": [
                    {
                        "base_field": 10,
                        "field_value": [45046, 45047],
                        "value": None,
                    }
                ],
                "profile_template": 29,
                "profile_template_name": "profile_template_name",
            },
            logging={
                "destination_region_id": 1,
                "enabled": True,
                "retention_policy": {"period": 45},
                "topic_name": "my-log-name",
            },
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.with_raw_response.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.with_streaming_response.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.with_raw_response.update(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.k8s.clusters.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SClusterList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(K8SClusterList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(K8SClusterList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.k8s.clusters.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.k8s.clusters.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            volumes="volumes",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.with_raw_response.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.with_streaming_response.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.with_raw_response.delete(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.k8s.clusters.get(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SCluster, cluster, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.with_raw_response.get(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(K8SCluster, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.with_streaming_response.get(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(K8SCluster, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.with_raw_response.get(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_get_certificate(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.k8s.clusters.get_certificate(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SClusterCertificate, cluster, path=["response"])

    @parametrize
    async def test_raw_response_get_certificate(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.with_raw_response.get_certificate(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(K8SClusterCertificate, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_get_certificate(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.with_streaming_response.get_certificate(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(K8SClusterCertificate, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_certificate(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.with_raw_response.get_certificate(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_get_kubeconfig(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.k8s.clusters.get_kubeconfig(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SClusterKubeconfig, cluster, path=["response"])

    @parametrize
    async def test_raw_response_get_kubeconfig(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.with_raw_response.get_kubeconfig(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(K8SClusterKubeconfig, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_get_kubeconfig(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.with_streaming_response.get_kubeconfig(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(K8SClusterKubeconfig, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_kubeconfig(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.with_raw_response.get_kubeconfig(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_list_versions_for_upgrade(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.k8s.clusters.list_versions_for_upgrade(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SClusterVersionList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_list_versions_for_upgrade(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.with_raw_response.list_versions_for_upgrade(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(K8SClusterVersionList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_list_versions_for_upgrade(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.with_streaming_response.list_versions_for_upgrade(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(K8SClusterVersionList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_versions_for_upgrade(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.with_raw_response.list_versions_for_upgrade(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_upgrade(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.k8s.clusters.upgrade(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            version="v1.28.1",
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_upgrade(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.with_raw_response.upgrade(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            version="v1.28.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_upgrade(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.with_streaming_response.upgrade(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            version="v1.28.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upgrade(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.with_raw_response.upgrade(
                cluster_name="",
                project_id=0,
                region_id=0,
                version="v1.28.1",
            )

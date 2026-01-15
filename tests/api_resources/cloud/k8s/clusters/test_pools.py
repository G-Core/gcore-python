# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import TaskIDList
from gcore.types.cloud.k8s.clusters import (
    K8SClusterPool,
    K8SClusterPoolList,
    K8SClusterPoolQuota,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        pool = client.cloud.k8s.clusters.pools.create(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            flavor_id="g1-standard-1-2",
            min_node_count=3,
            name="my-pool",
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        pool = client.cloud.k8s.clusters.pools.create(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            flavor_id="g1-standard-1-2",
            min_node_count=3,
            name="my-pool",
            auto_healing_enabled=True,
            boot_volume_size=50,
            boot_volume_type="ssd_hiiops",
            crio_config={"default-ulimits": "nofile=1024:2048"},
            is_public_ipv4=True,
            kubelet_config={"podMaxPids": "4096"},
            labels={"my-label": "foo"},
            max_node_count=5,
            servergroup_policy="affinity",
            taints={"my-taint": "bar:NoSchedule"},
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.pools.with_raw_response.create(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            flavor_id="g1-standard-1-2",
            min_node_count=3,
            name="my-pool",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.pools.with_streaming_response.create(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            flavor_id="g1-standard-1-2",
            min_node_count=3,
            name="my-pool",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(TaskIDList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.pools.with_raw_response.create(
                cluster_name="",
                project_id=0,
                region_id=0,
                flavor_id="g1-standard-1-2",
                min_node_count=3,
                name="my-pool",
            )

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        pool = client.cloud.k8s.clusters.pools.update(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )
        assert_matches_type(K8SClusterPool, pool, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        pool = client.cloud.k8s.clusters.pools.update(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
            auto_healing_enabled=True,
            labels={"my-label": "foo"},
            max_node_count=3,
            min_node_count=1,
            node_count=2,
            taints={"my-taint": "bar:NoSchedule"},
        )
        assert_matches_type(K8SClusterPool, pool, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.pools.with_raw_response.update(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(K8SClusterPool, pool, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.pools.with_streaming_response.update(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(K8SClusterPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.pools.with_raw_response.update(
                pool_name="pool_name",
                project_id=0,
                region_id=0,
                cluster_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_name` but received ''"):
            client.cloud.k8s.clusters.pools.with_raw_response.update(
                pool_name="",
                project_id=0,
                region_id=0,
                cluster_name="cluster_name",
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        pool = client.cloud.k8s.clusters.pools.list(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SClusterPoolList, pool, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.pools.with_raw_response.list(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(K8SClusterPoolList, pool, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.pools.with_streaming_response.list(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(K8SClusterPoolList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.pools.with_raw_response.list(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        pool = client.cloud.k8s.clusters.pools.delete(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.pools.with_raw_response.delete(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.pools.with_streaming_response.delete(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(TaskIDList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.pools.with_raw_response.delete(
                pool_name="pool_name",
                project_id=0,
                region_id=0,
                cluster_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_name` but received ''"):
            client.cloud.k8s.clusters.pools.with_raw_response.delete(
                pool_name="",
                project_id=0,
                region_id=0,
                cluster_name="cluster_name",
            )

    @parametrize
    def test_method_check_quota(self, client: Gcore) -> None:
        pool = client.cloud.k8s.clusters.pools.check_quota(
            project_id=1,
            region_id=7,
            flavor_id="g1-standard-1-2",
        )
        assert_matches_type(K8SClusterPoolQuota, pool, path=["response"])

    @parametrize
    def test_method_check_quota_with_all_params(self, client: Gcore) -> None:
        pool = client.cloud.k8s.clusters.pools.check_quota(
            project_id=1,
            region_id=7,
            flavor_id="g1-standard-1-2",
            boot_volume_size=50,
            max_node_count=5,
            min_node_count=3,
            name="test",
            node_count=5,
            servergroup_policy="anti-affinity",
        )
        assert_matches_type(K8SClusterPoolQuota, pool, path=["response"])

    @parametrize
    def test_raw_response_check_quota(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.pools.with_raw_response.check_quota(
            project_id=1,
            region_id=7,
            flavor_id="g1-standard-1-2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(K8SClusterPoolQuota, pool, path=["response"])

    @parametrize
    def test_streaming_response_check_quota(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.pools.with_streaming_response.check_quota(
            project_id=1,
            region_id=7,
            flavor_id="g1-standard-1-2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(K8SClusterPoolQuota, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        pool = client.cloud.k8s.clusters.pools.get(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )
        assert_matches_type(K8SClusterPool, pool, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.pools.with_raw_response.get(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(K8SClusterPool, pool, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.pools.with_streaming_response.get(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(K8SClusterPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.pools.with_raw_response.get(
                pool_name="pool_name",
                project_id=0,
                region_id=0,
                cluster_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_name` but received ''"):
            client.cloud.k8s.clusters.pools.with_raw_response.get(
                pool_name="",
                project_id=0,
                region_id=0,
                cluster_name="cluster_name",
            )

    @parametrize
    def test_method_resize(self, client: Gcore) -> None:
        pool = client.cloud.k8s.clusters.pools.resize(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
            node_count=2,
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_raw_response_resize(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.pools.with_raw_response.resize(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
            node_count=2,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_streaming_response_resize(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.pools.with_streaming_response.resize(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
            node_count=2,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(TaskIDList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resize(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.pools.with_raw_response.resize(
                pool_name="pool_name",
                project_id=0,
                region_id=0,
                cluster_name="",
                node_count=2,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_name` but received ''"):
            client.cloud.k8s.clusters.pools.with_raw_response.resize(
                pool_name="",
                project_id=0,
                region_id=0,
                cluster_name="cluster_name",
                node_count=2,
            )


class TestAsyncPools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.k8s.clusters.pools.create(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            flavor_id="g1-standard-1-2",
            min_node_count=3,
            name="my-pool",
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.k8s.clusters.pools.create(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            flavor_id="g1-standard-1-2",
            min_node_count=3,
            name="my-pool",
            auto_healing_enabled=True,
            boot_volume_size=50,
            boot_volume_type="ssd_hiiops",
            crio_config={"default-ulimits": "nofile=1024:2048"},
            is_public_ipv4=True,
            kubelet_config={"podMaxPids": "4096"},
            labels={"my-label": "foo"},
            max_node_count=5,
            servergroup_policy="affinity",
            taints={"my-taint": "bar:NoSchedule"},
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.pools.with_raw_response.create(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            flavor_id="g1-standard-1-2",
            min_node_count=3,
            name="my-pool",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.pools.with_streaming_response.create(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            flavor_id="g1-standard-1-2",
            min_node_count=3,
            name="my-pool",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(TaskIDList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.pools.with_raw_response.create(
                cluster_name="",
                project_id=0,
                region_id=0,
                flavor_id="g1-standard-1-2",
                min_node_count=3,
                name="my-pool",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.k8s.clusters.pools.update(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )
        assert_matches_type(K8SClusterPool, pool, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.k8s.clusters.pools.update(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
            auto_healing_enabled=True,
            labels={"my-label": "foo"},
            max_node_count=3,
            min_node_count=1,
            node_count=2,
            taints={"my-taint": "bar:NoSchedule"},
        )
        assert_matches_type(K8SClusterPool, pool, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.pools.with_raw_response.update(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(K8SClusterPool, pool, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.pools.with_streaming_response.update(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(K8SClusterPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.pools.with_raw_response.update(
                pool_name="pool_name",
                project_id=0,
                region_id=0,
                cluster_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_name` but received ''"):
            await async_client.cloud.k8s.clusters.pools.with_raw_response.update(
                pool_name="",
                project_id=0,
                region_id=0,
                cluster_name="cluster_name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.k8s.clusters.pools.list(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SClusterPoolList, pool, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.pools.with_raw_response.list(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(K8SClusterPoolList, pool, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.pools.with_streaming_response.list(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(K8SClusterPoolList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.pools.with_raw_response.list(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.k8s.clusters.pools.delete(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.pools.with_raw_response.delete(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.pools.with_streaming_response.delete(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(TaskIDList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.pools.with_raw_response.delete(
                pool_name="pool_name",
                project_id=0,
                region_id=0,
                cluster_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_name` but received ''"):
            await async_client.cloud.k8s.clusters.pools.with_raw_response.delete(
                pool_name="",
                project_id=0,
                region_id=0,
                cluster_name="cluster_name",
            )

    @parametrize
    async def test_method_check_quota(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.k8s.clusters.pools.check_quota(
            project_id=1,
            region_id=7,
            flavor_id="g1-standard-1-2",
        )
        assert_matches_type(K8SClusterPoolQuota, pool, path=["response"])

    @parametrize
    async def test_method_check_quota_with_all_params(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.k8s.clusters.pools.check_quota(
            project_id=1,
            region_id=7,
            flavor_id="g1-standard-1-2",
            boot_volume_size=50,
            max_node_count=5,
            min_node_count=3,
            name="test",
            node_count=5,
            servergroup_policy="anti-affinity",
        )
        assert_matches_type(K8SClusterPoolQuota, pool, path=["response"])

    @parametrize
    async def test_raw_response_check_quota(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.pools.with_raw_response.check_quota(
            project_id=1,
            region_id=7,
            flavor_id="g1-standard-1-2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(K8SClusterPoolQuota, pool, path=["response"])

    @parametrize
    async def test_streaming_response_check_quota(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.pools.with_streaming_response.check_quota(
            project_id=1,
            region_id=7,
            flavor_id="g1-standard-1-2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(K8SClusterPoolQuota, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.k8s.clusters.pools.get(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )
        assert_matches_type(K8SClusterPool, pool, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.pools.with_raw_response.get(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(K8SClusterPool, pool, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.pools.with_streaming_response.get(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(K8SClusterPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.pools.with_raw_response.get(
                pool_name="pool_name",
                project_id=0,
                region_id=0,
                cluster_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_name` but received ''"):
            await async_client.cloud.k8s.clusters.pools.with_raw_response.get(
                pool_name="",
                project_id=0,
                region_id=0,
                cluster_name="cluster_name",
            )

    @parametrize
    async def test_method_resize(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.k8s.clusters.pools.resize(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
            node_count=2,
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_raw_response_resize(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.pools.with_raw_response.resize(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
            node_count=2,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_streaming_response_resize(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.pools.with_streaming_response.resize(
            pool_name="pool_name",
            project_id=0,
            region_id=0,
            cluster_name="cluster_name",
            node_count=2,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(TaskIDList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resize(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.pools.with_raw_response.resize(
                pool_name="pool_name",
                project_id=0,
                region_id=0,
                cluster_name="",
                node_count=2,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_name` but received ''"):
            await async_client.cloud.k8s.clusters.pools.with_raw_response.resize(
                pool_name="",
                project_id=0,
                region_id=0,
                cluster_name="cluster_name",
                node_count=2,
            )

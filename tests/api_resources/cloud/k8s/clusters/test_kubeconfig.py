# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.k8s import K8SClusterKubeconfig

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKubeconfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        kubeconfig = client.cloud.k8s.clusters.kubeconfig.get(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(K8SClusterKubeconfig, kubeconfig, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.kubeconfig.with_raw_response.get(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kubeconfig = response.parse()
        assert_matches_type(K8SClusterKubeconfig, kubeconfig, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.kubeconfig.with_streaming_response.get(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kubeconfig = response.parse()
            assert_matches_type(K8SClusterKubeconfig, kubeconfig, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.kubeconfig.with_raw_response.get(
                cluster_name="",
                project_id=1,
                region_id=7,
            )


class TestAsyncKubeconfig:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        kubeconfig = await async_client.cloud.k8s.clusters.kubeconfig.get(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(K8SClusterKubeconfig, kubeconfig, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.kubeconfig.with_raw_response.get(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kubeconfig = await response.parse()
        assert_matches_type(K8SClusterKubeconfig, kubeconfig, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.kubeconfig.with_streaming_response.get(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kubeconfig = await response.parse()
            assert_matches_type(K8SClusterKubeconfig, kubeconfig, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.kubeconfig.with_raw_response.get(
                cluster_name="",
                project_id=1,
                region_id=7,
            )

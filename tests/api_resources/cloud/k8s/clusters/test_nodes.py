# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import InstanceList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        node = client.cloud.k8s.clusters.nodes.list(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(InstanceList, node, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        node = client.cloud.k8s.clusters.nodes.list(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
            with_ddos=False,
        )
        assert_matches_type(InstanceList, node, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.nodes.with_raw_response.list(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(InstanceList, node, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.nodes.with_streaming_response.list(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(InstanceList, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.nodes.with_raw_response.list(
                cluster_name="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        node = client.cloud.k8s.clusters.nodes.delete(
            instance_id="550e8400-e29b-41d4-a716-446655440000",
            project_id=1,
            region_id=7,
            cluster_name="my-cluster",
        )
        assert node is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.k8s.clusters.nodes.with_raw_response.delete(
            instance_id="550e8400-e29b-41d4-a716-446655440000",
            project_id=1,
            region_id=7,
            cluster_name="my-cluster",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert node is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.k8s.clusters.nodes.with_streaming_response.delete(
            instance_id="550e8400-e29b-41d4-a716-446655440000",
            project_id=1,
            region_id=7,
            cluster_name="my-cluster",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert node is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.k8s.clusters.nodes.with_raw_response.delete(
                instance_id="550e8400-e29b-41d4-a716-446655440000",
                project_id=1,
                region_id=7,
                cluster_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.k8s.clusters.nodes.with_raw_response.delete(
                instance_id="",
                project_id=1,
                region_id=7,
                cluster_name="my-cluster",
            )


class TestAsyncNodes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        node = await async_client.cloud.k8s.clusters.nodes.list(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(InstanceList, node, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        node = await async_client.cloud.k8s.clusters.nodes.list(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
            with_ddos=False,
        )
        assert_matches_type(InstanceList, node, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.nodes.with_raw_response.list(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(InstanceList, node, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.nodes.with_streaming_response.list(
            cluster_name="my-cluster",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(InstanceList, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.nodes.with_raw_response.list(
                cluster_name="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        node = await async_client.cloud.k8s.clusters.nodes.delete(
            instance_id="550e8400-e29b-41d4-a716-446655440000",
            project_id=1,
            region_id=7,
            cluster_name="my-cluster",
        )
        assert node is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.clusters.nodes.with_raw_response.delete(
            instance_id="550e8400-e29b-41d4-a716-446655440000",
            project_id=1,
            region_id=7,
            cluster_name="my-cluster",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert node is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.clusters.nodes.with_streaming_response.delete(
            instance_id="550e8400-e29b-41d4-a716-446655440000",
            project_id=1,
            region_id=7,
            cluster_name="my-cluster",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert node is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.k8s.clusters.nodes.with_raw_response.delete(
                instance_id="550e8400-e29b-41d4-a716-446655440000",
                project_id=1,
                region_id=7,
                cluster_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.k8s.clusters.nodes.with_raw_response.delete(
                instance_id="",
                project_id=1,
                region_id=7,
                cluster_name="my-cluster",
            )

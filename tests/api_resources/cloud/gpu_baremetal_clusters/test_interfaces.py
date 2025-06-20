# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import NetworkInterfaceList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInterfaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        interface = client.cloud.gpu_baremetal_clusters.interfaces.list(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(NetworkInterfaceList, interface, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal_clusters.interfaces.with_raw_response.list(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = response.parse()
        assert_matches_type(NetworkInterfaceList, interface, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal_clusters.interfaces.with_streaming_response.list(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = response.parse()
            assert_matches_type(NetworkInterfaceList, interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal_clusters.interfaces.with_raw_response.list(
                cluster_id="",
                project_id=0,
                region_id=0,
            )


class TestAsyncInterfaces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        interface = await async_client.cloud.gpu_baremetal_clusters.interfaces.list(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(NetworkInterfaceList, interface, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal_clusters.interfaces.with_raw_response.list(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = await response.parse()
        assert_matches_type(NetworkInterfaceList, interface, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal_clusters.interfaces.with_streaming_response.list(
            cluster_id="cluster_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = await response.parse()
            assert_matches_type(NetworkInterfaceList, interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal_clusters.interfaces.with_raw_response.list(
                cluster_id="",
                project_id=0,
                region_id=0,
            )

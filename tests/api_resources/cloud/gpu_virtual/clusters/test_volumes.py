# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.gpu_virtual.clusters import GPUVirtualClusterVolumeList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVolumes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        volume = client.cloud.gpu_virtual.clusters.volumes.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(GPUVirtualClusterVolumeList, volume, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.volumes.with_raw_response.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(GPUVirtualClusterVolumeList, volume, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.volumes.with_streaming_response.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(GPUVirtualClusterVolumeList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_virtual.clusters.volumes.with_raw_response.list(
                cluster_id="",
                project_id=1,
                region_id=7,
            )


class TestAsyncVolumes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.gpu_virtual.clusters.volumes.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(GPUVirtualClusterVolumeList, volume, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.volumes.with_raw_response.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(GPUVirtualClusterVolumeList, volume, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.volumes.with_streaming_response.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(GPUVirtualClusterVolumeList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.volumes.with_raw_response.list(
                cluster_id="",
                project_id=1,
                region_id=7,
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import K8SClusterVersionList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestK8S:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_versions(self, client: Gcore) -> None:
        k8s = client.cloud.k8s.list_versions(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SClusterVersionList, k8s, path=["response"])

    @parametrize
    def test_raw_response_list_versions(self, client: Gcore) -> None:
        response = client.cloud.k8s.with_raw_response.list_versions(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        k8s = response.parse()
        assert_matches_type(K8SClusterVersionList, k8s, path=["response"])

    @parametrize
    def test_streaming_response_list_versions(self, client: Gcore) -> None:
        with client.cloud.k8s.with_streaming_response.list_versions(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            k8s = response.parse()
            assert_matches_type(K8SClusterVersionList, k8s, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncK8S:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list_versions(self, async_client: AsyncGcore) -> None:
        k8s = await async_client.cloud.k8s.list_versions(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(K8SClusterVersionList, k8s, path=["response"])

    @parametrize
    async def test_raw_response_list_versions(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.k8s.with_raw_response.list_versions(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        k8s = await response.parse()
        assert_matches_type(K8SClusterVersionList, k8s, path=["response"])

    @parametrize
    async def test_streaming_response_list_versions(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.k8s.with_streaming_response.list_versions(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            k8s = await response.parse()
            assert_matches_type(K8SClusterVersionList, k8s, path=["response"])

        assert cast(Any, response.is_closed) is True

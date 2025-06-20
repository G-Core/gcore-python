# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import LoadBalancerMetricsList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        metric = client.cloud.load_balancers.metrics.list(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            time_interval=6,
            time_unit="day",
        )
        assert_matches_type(LoadBalancerMetricsList, metric, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.metrics.with_raw_response.list(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            time_interval=6,
            time_unit="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(LoadBalancerMetricsList, metric, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.load_balancers.metrics.with_streaming_response.list(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            time_interval=6,
            time_unit="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(LoadBalancerMetricsList, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loadbalancer_id` but received ''"):
            client.cloud.load_balancers.metrics.with_raw_response.list(
                loadbalancer_id="",
                project_id=0,
                region_id=0,
                time_interval=6,
                time_unit="day",
            )


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        metric = await async_client.cloud.load_balancers.metrics.list(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            time_interval=6,
            time_unit="day",
        )
        assert_matches_type(LoadBalancerMetricsList, metric, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.metrics.with_raw_response.list(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            time_interval=6,
            time_unit="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(LoadBalancerMetricsList, metric, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.metrics.with_streaming_response.list(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            time_interval=6,
            time_unit="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(LoadBalancerMetricsList, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loadbalancer_id` but received ''"):
            await async_client.cloud.load_balancers.metrics.with_raw_response.list(
                loadbalancer_id="",
                project_id=0,
                region_id=0,
                time_interval=6,
                time_unit="day",
            )

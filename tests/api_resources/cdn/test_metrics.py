# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn import CdnMetrics

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        metric = client.cdn.metrics.list(
            from_="2021-06-14T00:00:00Z",
            metrics=["edge_status_2xx", "edge_status_3xx", "edge_status_4xx", "edge_status_5xx"],
            to="2021-06-15T00:00:00Z",
        )
        assert_matches_type(CdnMetrics, metric, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        metric = client.cdn.metrics.list(
            from_="2021-06-14T00:00:00Z",
            metrics=["edge_status_2xx", "edge_status_3xx", "edge_status_4xx", "edge_status_5xx"],
            to="2021-06-15T00:00:00Z",
            filter_by=[
                {
                    "field": "resource",
                    "op": "eq",
                    "values": [1234],
                }
            ],
            granularity="P1D",
            group_by=["cname"],
        )
        assert_matches_type(CdnMetrics, metric, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.metrics.with_raw_response.list(
            from_="2021-06-14T00:00:00Z",
            metrics=["edge_status_2xx", "edge_status_3xx", "edge_status_4xx", "edge_status_5xx"],
            to="2021-06-15T00:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(CdnMetrics, metric, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.metrics.with_streaming_response.list(
            from_="2021-06-14T00:00:00Z",
            metrics=["edge_status_2xx", "edge_status_3xx", "edge_status_4xx", "edge_status_5xx"],
            to="2021-06-15T00:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(CdnMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        metric = await async_client.cdn.metrics.list(
            from_="2021-06-14T00:00:00Z",
            metrics=["edge_status_2xx", "edge_status_3xx", "edge_status_4xx", "edge_status_5xx"],
            to="2021-06-15T00:00:00Z",
        )
        assert_matches_type(CdnMetrics, metric, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        metric = await async_client.cdn.metrics.list(
            from_="2021-06-14T00:00:00Z",
            metrics=["edge_status_2xx", "edge_status_3xx", "edge_status_4xx", "edge_status_5xx"],
            to="2021-06-15T00:00:00Z",
            filter_by=[
                {
                    "field": "resource",
                    "op": "eq",
                    "values": [1234],
                }
            ],
            granularity="P1D",
            group_by=["cname"],
        )
        assert_matches_type(CdnMetrics, metric, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.metrics.with_raw_response.list(
            from_="2021-06-14T00:00:00Z",
            metrics=["edge_status_2xx", "edge_status_3xx", "edge_status_4xx", "edge_status_5xx"],
            to="2021-06-15T00:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(CdnMetrics, metric, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.metrics.with_streaming_response.list(
            from_="2021-06-14T00:00:00Z",
            metrics=["edge_status_2xx", "edge_status_3xx", "edge_status_4xx", "edge_status_5xx"],
            to="2021-06-15T00:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(CdnMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

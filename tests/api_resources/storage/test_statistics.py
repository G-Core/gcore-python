# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.storage import (
    UsageTotal,
    StatisticGetUsageSeriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatistics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_usage_aggregated(self, client: Gcore) -> None:
        statistic = client.storage.statistics.get_usage_aggregated()
        assert_matches_type(UsageTotal, statistic, path=["response"])

    @parametrize
    def test_method_get_usage_aggregated_with_all_params(self, client: Gcore) -> None:
        statistic = client.storage.statistics.get_usage_aggregated(
            from_="2006-01-02",
            locations=["s-region-1", "s-region-2"],
            storages=["123-myStorage"],
            to="2006-01-02",
        )
        assert_matches_type(UsageTotal, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_usage_aggregated(self, client: Gcore) -> None:
        response = client.storage.statistics.with_raw_response.get_usage_aggregated()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(UsageTotal, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_usage_aggregated(self, client: Gcore) -> None:
        with client.storage.statistics.with_streaming_response.get_usage_aggregated() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(UsageTotal, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_usage_series(self, client: Gcore) -> None:
        statistic = client.storage.statistics.get_usage_series()
        assert_matches_type(StatisticGetUsageSeriesResponse, statistic, path=["response"])

    @parametrize
    def test_method_get_usage_series_with_all_params(self, client: Gcore) -> None:
        statistic = client.storage.statistics.get_usage_series(
            from_="2006-01-02",
            granularity="12h",
            locations=["s-region-1", "s-region-2"],
            source=0,
            storages=["123-myStorage"],
            to="2006-01-02",
            ts_string=True,
        )
        assert_matches_type(StatisticGetUsageSeriesResponse, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_usage_series(self, client: Gcore) -> None:
        response = client.storage.statistics.with_raw_response.get_usage_series()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(StatisticGetUsageSeriesResponse, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_usage_series(self, client: Gcore) -> None:
        with client.storage.statistics.with_streaming_response.get_usage_series() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(StatisticGetUsageSeriesResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatistics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_usage_aggregated(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.storage.statistics.get_usage_aggregated()
        assert_matches_type(UsageTotal, statistic, path=["response"])

    @parametrize
    async def test_method_get_usage_aggregated_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.storage.statistics.get_usage_aggregated(
            from_="2006-01-02",
            locations=["s-region-1", "s-region-2"],
            storages=["123-myStorage"],
            to="2006-01-02",
        )
        assert_matches_type(UsageTotal, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_usage_aggregated(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.statistics.with_raw_response.get_usage_aggregated()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(UsageTotal, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_usage_aggregated(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.statistics.with_streaming_response.get_usage_aggregated() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(UsageTotal, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_usage_series(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.storage.statistics.get_usage_series()
        assert_matches_type(StatisticGetUsageSeriesResponse, statistic, path=["response"])

    @parametrize
    async def test_method_get_usage_series_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.storage.statistics.get_usage_series(
            from_="2006-01-02",
            granularity="12h",
            locations=["s-region-1", "s-region-2"],
            source=0,
            storages=["123-myStorage"],
            to="2006-01-02",
            ts_string=True,
        )
        assert_matches_type(StatisticGetUsageSeriesResponse, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_usage_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.storage.statistics.with_raw_response.get_usage_series()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(StatisticGetUsageSeriesResponse, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_usage_series(self, async_client: AsyncGcore) -> None:
        async with async_client.storage.statistics.with_streaming_response.get_usage_series() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(StatisticGetUsageSeriesResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

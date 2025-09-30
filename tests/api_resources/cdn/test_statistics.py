# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn import (
    UsageSeriesStats,
    ResourceUsageStats,
    LogsAggregatedStats,
    ShieldAggregatedStats,
    ResourceAggregatedStats,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatistics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_logs_usage_aggregated(self, client: Gcore) -> None:
        statistic = client.cdn.statistics.get_logs_usage_aggregated(
            from_="from",
            to="to",
        )
        assert_matches_type(LogsAggregatedStats, statistic, path=["response"])

    @parametrize
    def test_method_get_logs_usage_aggregated_with_all_params(self, client: Gcore) -> None:
        statistic = client.cdn.statistics.get_logs_usage_aggregated(
            from_="from",
            to="to",
            flat=True,
            group_by="group_by",
            resource=0,
        )
        assert_matches_type(LogsAggregatedStats, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_logs_usage_aggregated(self, client: Gcore) -> None:
        response = client.cdn.statistics.with_raw_response.get_logs_usage_aggregated(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(LogsAggregatedStats, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_logs_usage_aggregated(self, client: Gcore) -> None:
        with client.cdn.statistics.with_streaming_response.get_logs_usage_aggregated(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(LogsAggregatedStats, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_logs_usage_series(self, client: Gcore) -> None:
        statistic = client.cdn.statistics.get_logs_usage_series(
            from_="from",
            to="to",
        )
        assert_matches_type(UsageSeriesStats, statistic, path=["response"])

    @parametrize
    def test_method_get_logs_usage_series_with_all_params(self, client: Gcore) -> None:
        statistic = client.cdn.statistics.get_logs_usage_series(
            from_="from",
            to="to",
            resource=0,
        )
        assert_matches_type(UsageSeriesStats, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_logs_usage_series(self, client: Gcore) -> None:
        response = client.cdn.statistics.with_raw_response.get_logs_usage_series(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(UsageSeriesStats, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_logs_usage_series(self, client: Gcore) -> None:
        with client.cdn.statistics.with_streaming_response.get_logs_usage_series(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(UsageSeriesStats, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_resource_usage_aggregated(self, client: Gcore) -> None:
        statistic = client.cdn.statistics.get_resource_usage_aggregated(
            from_="from",
            metrics="metrics",
            service="service",
            to="to",
        )
        assert_matches_type(ResourceAggregatedStats, statistic, path=["response"])

    @parametrize
    def test_method_get_resource_usage_aggregated_with_all_params(self, client: Gcore) -> None:
        statistic = client.cdn.statistics.get_resource_usage_aggregated(
            from_="from",
            metrics="metrics",
            service="service",
            to="to",
            countries="countries",
            flat=True,
            group_by="group_by",
            regions="regions",
            resource=0,
        )
        assert_matches_type(ResourceAggregatedStats, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_resource_usage_aggregated(self, client: Gcore) -> None:
        response = client.cdn.statistics.with_raw_response.get_resource_usage_aggregated(
            from_="from",
            metrics="metrics",
            service="service",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(ResourceAggregatedStats, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_resource_usage_aggregated(self, client: Gcore) -> None:
        with client.cdn.statistics.with_streaming_response.get_resource_usage_aggregated(
            from_="from",
            metrics="metrics",
            service="service",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(ResourceAggregatedStats, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_resource_usage_series(self, client: Gcore) -> None:
        statistic = client.cdn.statistics.get_resource_usage_series(
            from_="from",
            granularity="granularity",
            metrics="metrics",
            service="service",
            to="to",
        )
        assert_matches_type(ResourceUsageStats, statistic, path=["response"])

    @parametrize
    def test_method_get_resource_usage_series_with_all_params(self, client: Gcore) -> None:
        statistic = client.cdn.statistics.get_resource_usage_series(
            from_="from",
            granularity="granularity",
            metrics="metrics",
            service="service",
            to="to",
            countries="countries",
            group_by="group_by",
            regions="regions",
            resource=0,
        )
        assert_matches_type(ResourceUsageStats, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_resource_usage_series(self, client: Gcore) -> None:
        response = client.cdn.statistics.with_raw_response.get_resource_usage_series(
            from_="from",
            granularity="granularity",
            metrics="metrics",
            service="service",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(ResourceUsageStats, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_resource_usage_series(self, client: Gcore) -> None:
        with client.cdn.statistics.with_streaming_response.get_resource_usage_series(
            from_="from",
            granularity="granularity",
            metrics="metrics",
            service="service",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(ResourceUsageStats, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_shield_usage_aggregated(self, client: Gcore) -> None:
        statistic = client.cdn.statistics.get_shield_usage_aggregated(
            from_="from",
            to="to",
        )
        assert_matches_type(ShieldAggregatedStats, statistic, path=["response"])

    @parametrize
    def test_method_get_shield_usage_aggregated_with_all_params(self, client: Gcore) -> None:
        statistic = client.cdn.statistics.get_shield_usage_aggregated(
            from_="from",
            to="to",
            flat=True,
            group_by="group_by",
            resource=0,
        )
        assert_matches_type(ShieldAggregatedStats, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_shield_usage_aggregated(self, client: Gcore) -> None:
        response = client.cdn.statistics.with_raw_response.get_shield_usage_aggregated(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(ShieldAggregatedStats, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_shield_usage_aggregated(self, client: Gcore) -> None:
        with client.cdn.statistics.with_streaming_response.get_shield_usage_aggregated(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(ShieldAggregatedStats, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_shield_usage_series(self, client: Gcore) -> None:
        statistic = client.cdn.statistics.get_shield_usage_series(
            from_="from",
            to="to",
        )
        assert_matches_type(UsageSeriesStats, statistic, path=["response"])

    @parametrize
    def test_method_get_shield_usage_series_with_all_params(self, client: Gcore) -> None:
        statistic = client.cdn.statistics.get_shield_usage_series(
            from_="from",
            to="to",
            resource=0,
        )
        assert_matches_type(UsageSeriesStats, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_shield_usage_series(self, client: Gcore) -> None:
        response = client.cdn.statistics.with_raw_response.get_shield_usage_series(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(UsageSeriesStats, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_shield_usage_series(self, client: Gcore) -> None:
        with client.cdn.statistics.with_streaming_response.get_shield_usage_series(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(UsageSeriesStats, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatistics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_logs_usage_aggregated(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.cdn.statistics.get_logs_usage_aggregated(
            from_="from",
            to="to",
        )
        assert_matches_type(LogsAggregatedStats, statistic, path=["response"])

    @parametrize
    async def test_method_get_logs_usage_aggregated_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.cdn.statistics.get_logs_usage_aggregated(
            from_="from",
            to="to",
            flat=True,
            group_by="group_by",
            resource=0,
        )
        assert_matches_type(LogsAggregatedStats, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_logs_usage_aggregated(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.statistics.with_raw_response.get_logs_usage_aggregated(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(LogsAggregatedStats, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_logs_usage_aggregated(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.statistics.with_streaming_response.get_logs_usage_aggregated(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(LogsAggregatedStats, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_logs_usage_series(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.cdn.statistics.get_logs_usage_series(
            from_="from",
            to="to",
        )
        assert_matches_type(UsageSeriesStats, statistic, path=["response"])

    @parametrize
    async def test_method_get_logs_usage_series_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.cdn.statistics.get_logs_usage_series(
            from_="from",
            to="to",
            resource=0,
        )
        assert_matches_type(UsageSeriesStats, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_logs_usage_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.statistics.with_raw_response.get_logs_usage_series(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(UsageSeriesStats, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_logs_usage_series(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.statistics.with_streaming_response.get_logs_usage_series(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(UsageSeriesStats, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_resource_usage_aggregated(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.cdn.statistics.get_resource_usage_aggregated(
            from_="from",
            metrics="metrics",
            service="service",
            to="to",
        )
        assert_matches_type(ResourceAggregatedStats, statistic, path=["response"])

    @parametrize
    async def test_method_get_resource_usage_aggregated_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.cdn.statistics.get_resource_usage_aggregated(
            from_="from",
            metrics="metrics",
            service="service",
            to="to",
            countries="countries",
            flat=True,
            group_by="group_by",
            regions="regions",
            resource=0,
        )
        assert_matches_type(ResourceAggregatedStats, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_resource_usage_aggregated(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.statistics.with_raw_response.get_resource_usage_aggregated(
            from_="from",
            metrics="metrics",
            service="service",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(ResourceAggregatedStats, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_resource_usage_aggregated(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.statistics.with_streaming_response.get_resource_usage_aggregated(
            from_="from",
            metrics="metrics",
            service="service",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(ResourceAggregatedStats, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_resource_usage_series(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.cdn.statistics.get_resource_usage_series(
            from_="from",
            granularity="granularity",
            metrics="metrics",
            service="service",
            to="to",
        )
        assert_matches_type(ResourceUsageStats, statistic, path=["response"])

    @parametrize
    async def test_method_get_resource_usage_series_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.cdn.statistics.get_resource_usage_series(
            from_="from",
            granularity="granularity",
            metrics="metrics",
            service="service",
            to="to",
            countries="countries",
            group_by="group_by",
            regions="regions",
            resource=0,
        )
        assert_matches_type(ResourceUsageStats, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_resource_usage_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.statistics.with_raw_response.get_resource_usage_series(
            from_="from",
            granularity="granularity",
            metrics="metrics",
            service="service",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(ResourceUsageStats, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_resource_usage_series(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.statistics.with_streaming_response.get_resource_usage_series(
            from_="from",
            granularity="granularity",
            metrics="metrics",
            service="service",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(ResourceUsageStats, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_shield_usage_aggregated(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.cdn.statistics.get_shield_usage_aggregated(
            from_="from",
            to="to",
        )
        assert_matches_type(ShieldAggregatedStats, statistic, path=["response"])

    @parametrize
    async def test_method_get_shield_usage_aggregated_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.cdn.statistics.get_shield_usage_aggregated(
            from_="from",
            to="to",
            flat=True,
            group_by="group_by",
            resource=0,
        )
        assert_matches_type(ShieldAggregatedStats, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_shield_usage_aggregated(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.statistics.with_raw_response.get_shield_usage_aggregated(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(ShieldAggregatedStats, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_shield_usage_aggregated(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.statistics.with_streaming_response.get_shield_usage_aggregated(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(ShieldAggregatedStats, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_shield_usage_series(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.cdn.statistics.get_shield_usage_series(
            from_="from",
            to="to",
        )
        assert_matches_type(UsageSeriesStats, statistic, path=["response"])

    @parametrize
    async def test_method_get_shield_usage_series_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.cdn.statistics.get_shield_usage_series(
            from_="from",
            to="to",
            resource=0,
        )
        assert_matches_type(UsageSeriesStats, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_shield_usage_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.statistics.with_raw_response.get_shield_usage_series(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(UsageSeriesStats, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_shield_usage_series(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.statistics.with_streaming_response.get_shield_usage_series(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(UsageSeriesStats, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

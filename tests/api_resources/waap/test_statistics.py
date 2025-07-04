# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.types.waap import WaapStatisticsSeries

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatistics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_usage_series(self, client: Gcore) -> None:
        statistic = client.waap.statistics.get_usage_series(
            from_=parse_datetime("2024-12-14T12:00:00Z"),
            granularity="1h",
            metrics=["total_bytes"],
            to=parse_datetime("2024-12-14T12:00:00Z"),
        )
        assert_matches_type(WaapStatisticsSeries, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_usage_series(self, client: Gcore) -> None:
        response = client.waap.statistics.with_raw_response.get_usage_series(
            from_=parse_datetime("2024-12-14T12:00:00Z"),
            granularity="1h",
            metrics=["total_bytes"],
            to=parse_datetime("2024-12-14T12:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(WaapStatisticsSeries, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_usage_series(self, client: Gcore) -> None:
        with client.waap.statistics.with_streaming_response.get_usage_series(
            from_=parse_datetime("2024-12-14T12:00:00Z"),
            granularity="1h",
            metrics=["total_bytes"],
            to=parse_datetime("2024-12-14T12:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(WaapStatisticsSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatistics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_usage_series(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.waap.statistics.get_usage_series(
            from_=parse_datetime("2024-12-14T12:00:00Z"),
            granularity="1h",
            metrics=["total_bytes"],
            to=parse_datetime("2024-12-14T12:00:00Z"),
        )
        assert_matches_type(WaapStatisticsSeries, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_usage_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.statistics.with_raw_response.get_usage_series(
            from_=parse_datetime("2024-12-14T12:00:00Z"),
            granularity="1h",
            metrics=["total_bytes"],
            to=parse_datetime("2024-12-14T12:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(WaapStatisticsSeries, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_usage_series(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.statistics.with_streaming_response.get_usage_series(
            from_=parse_datetime("2024-12-14T12:00:00Z"),
            granularity="1h",
            metrics=["total_bytes"],
            to=parse_datetime("2024-12-14T12:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(WaapStatisticsSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

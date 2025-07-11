# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.types.fastedge import (
    StatisticGetCallSeriesResponse,
    StatisticGetDurationSeriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatistics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_call_series(self, client: Gcore) -> None:
        statistic = client.fastedge.statistics.get_call_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(StatisticGetCallSeriesResponse, statistic, path=["response"])

    @parametrize
    def test_method_get_call_series_with_all_params(self, client: Gcore) -> None:
        statistic = client.fastedge.statistics.get_call_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            id=0,
            network="network",
        )
        assert_matches_type(StatisticGetCallSeriesResponse, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_call_series(self, client: Gcore) -> None:
        response = client.fastedge.statistics.with_raw_response.get_call_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(StatisticGetCallSeriesResponse, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_call_series(self, client: Gcore) -> None:
        with client.fastedge.statistics.with_streaming_response.get_call_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(StatisticGetCallSeriesResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_duration_series(self, client: Gcore) -> None:
        statistic = client.fastedge.statistics.get_duration_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(StatisticGetDurationSeriesResponse, statistic, path=["response"])

    @parametrize
    def test_method_get_duration_series_with_all_params(self, client: Gcore) -> None:
        statistic = client.fastedge.statistics.get_duration_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            id=0,
            network="network",
        )
        assert_matches_type(StatisticGetDurationSeriesResponse, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_duration_series(self, client: Gcore) -> None:
        response = client.fastedge.statistics.with_raw_response.get_duration_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(StatisticGetDurationSeriesResponse, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_duration_series(self, client: Gcore) -> None:
        with client.fastedge.statistics.with_streaming_response.get_duration_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(StatisticGetDurationSeriesResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatistics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_call_series(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.fastedge.statistics.get_call_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(StatisticGetCallSeriesResponse, statistic, path=["response"])

    @parametrize
    async def test_method_get_call_series_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.fastedge.statistics.get_call_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            id=0,
            network="network",
        )
        assert_matches_type(StatisticGetCallSeriesResponse, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_call_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.statistics.with_raw_response.get_call_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(StatisticGetCallSeriesResponse, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_call_series(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.statistics.with_streaming_response.get_call_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(StatisticGetCallSeriesResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_duration_series(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.fastedge.statistics.get_duration_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(StatisticGetDurationSeriesResponse, statistic, path=["response"])

    @parametrize
    async def test_method_get_duration_series_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.fastedge.statistics.get_duration_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            id=0,
            network="network",
        )
        assert_matches_type(StatisticGetDurationSeriesResponse, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_duration_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.statistics.with_raw_response.get_duration_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(StatisticGetDurationSeriesResponse, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_duration_series(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.statistics.with_streaming_response.get_duration_series(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            step=0,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(StatisticGetDurationSeriesResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

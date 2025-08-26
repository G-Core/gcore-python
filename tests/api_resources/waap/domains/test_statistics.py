# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.waap.domains import (
    WaapDDOSInfo,
    WaapDDOSAttack,
    WaapRequestDetails,
    WaapRequestSummary,
    WaapEventStatistics,
    StatisticGetTrafficSeriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatistics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_ddos_attacks(self, client: Gcore) -> None:
        statistic = client.waap.domains.statistics.get_ddos_attacks(
            domain_id=1,
        )
        assert_matches_type(SyncOffsetPage[WaapDDOSAttack], statistic, path=["response"])

    @parametrize
    def test_method_get_ddos_attacks_with_all_params(self, client: Gcore) -> None:
        statistic = client.waap.domains.statistics.get_ddos_attacks(
            domain_id=1,
            end_time=parse_datetime("2024-04-27T13:00:00Z"),
            limit=0,
            offset=0,
            ordering="start_time",
            start_time=parse_datetime("2024-04-26T13:32:49Z"),
        )
        assert_matches_type(SyncOffsetPage[WaapDDOSAttack], statistic, path=["response"])

    @parametrize
    def test_raw_response_get_ddos_attacks(self, client: Gcore) -> None:
        response = client.waap.domains.statistics.with_raw_response.get_ddos_attacks(
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(SyncOffsetPage[WaapDDOSAttack], statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_ddos_attacks(self, client: Gcore) -> None:
        with client.waap.domains.statistics.with_streaming_response.get_ddos_attacks(
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(SyncOffsetPage[WaapDDOSAttack], statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_ddos_info(self, client: Gcore) -> None:
        statistic = client.waap.domains.statistics.get_ddos_info(
            domain_id=1,
            group_by="URL",
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(SyncOffsetPage[WaapDDOSInfo], statistic, path=["response"])

    @parametrize
    def test_method_get_ddos_info_with_all_params(self, client: Gcore) -> None:
        statistic = client.waap.domains.statistics.get_ddos_info(
            domain_id=1,
            group_by="URL",
            start="2024-04-13T00:00:00+01:00",
            end="2024-04-14T12:00:00Z",
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[WaapDDOSInfo], statistic, path=["response"])

    @parametrize
    def test_raw_response_get_ddos_info(self, client: Gcore) -> None:
        response = client.waap.domains.statistics.with_raw_response.get_ddos_info(
            domain_id=1,
            group_by="URL",
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(SyncOffsetPage[WaapDDOSInfo], statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_ddos_info(self, client: Gcore) -> None:
        with client.waap.domains.statistics.with_streaming_response.get_ddos_info(
            domain_id=1,
            group_by="URL",
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(SyncOffsetPage[WaapDDOSInfo], statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_events_aggregated(self, client: Gcore) -> None:
        statistic = client.waap.domains.statistics.get_events_aggregated(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(WaapEventStatistics, statistic, path=["response"])

    @parametrize
    def test_method_get_events_aggregated_with_all_params(self, client: Gcore) -> None:
        statistic = client.waap.domains.statistics.get_events_aggregated(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
            action=["block", "captcha"],
            end="2024-04-14T12:00:00Z",
            ip=["string", "string"],
            reference_id=["string", "string"],
            result=["passed", "blocked"],
        )
        assert_matches_type(WaapEventStatistics, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_events_aggregated(self, client: Gcore) -> None:
        response = client.waap.domains.statistics.with_raw_response.get_events_aggregated(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(WaapEventStatistics, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_events_aggregated(self, client: Gcore) -> None:
        with client.waap.domains.statistics.with_streaming_response.get_events_aggregated(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(WaapEventStatistics, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_request_details(self, client: Gcore) -> None:
        statistic = client.waap.domains.statistics.get_request_details(
            request_id="request_id",
            domain_id=1,
        )
        assert_matches_type(WaapRequestDetails, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_request_details(self, client: Gcore) -> None:
        response = client.waap.domains.statistics.with_raw_response.get_request_details(
            request_id="request_id",
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(WaapRequestDetails, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_request_details(self, client: Gcore) -> None:
        with client.waap.domains.statistics.with_streaming_response.get_request_details(
            request_id="request_id",
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(WaapRequestDetails, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_request_details(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.waap.domains.statistics.with_raw_response.get_request_details(
                request_id="",
                domain_id=1,
            )

    @parametrize
    def test_method_get_requests_series(self, client: Gcore) -> None:
        statistic = client.waap.domains.statistics.get_requests_series(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(SyncOffsetPage[WaapRequestSummary], statistic, path=["response"])

    @parametrize
    def test_method_get_requests_series_with_all_params(self, client: Gcore) -> None:
        statistic = client.waap.domains.statistics.get_requests_series(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
            actions=["allow"],
            countries=["Mv"],
            end="2024-04-14T12:00:00Z",
            ip=".:",
            limit=0,
            offset=0,
            ordering="ordering",
            reference_id="ad07c06f19054e484974fa22e9fb6bb1",
            security_rule_name="security_rule_name",
            status_code=100,
            traffic_types=["policy_allowed"],
        )
        assert_matches_type(SyncOffsetPage[WaapRequestSummary], statistic, path=["response"])

    @parametrize
    def test_raw_response_get_requests_series(self, client: Gcore) -> None:
        response = client.waap.domains.statistics.with_raw_response.get_requests_series(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(SyncOffsetPage[WaapRequestSummary], statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_requests_series(self, client: Gcore) -> None:
        with client.waap.domains.statistics.with_streaming_response.get_requests_series(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(SyncOffsetPage[WaapRequestSummary], statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_traffic_series(self, client: Gcore) -> None:
        statistic = client.waap.domains.statistics.get_traffic_series(
            domain_id=1,
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(StatisticGetTrafficSeriesResponse, statistic, path=["response"])

    @parametrize
    def test_method_get_traffic_series_with_all_params(self, client: Gcore) -> None:
        statistic = client.waap.domains.statistics.get_traffic_series(
            domain_id=1,
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
            end="2024-04-14T12:00:00Z",
        )
        assert_matches_type(StatisticGetTrafficSeriesResponse, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_traffic_series(self, client: Gcore) -> None:
        response = client.waap.domains.statistics.with_raw_response.get_traffic_series(
            domain_id=1,
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(StatisticGetTrafficSeriesResponse, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_traffic_series(self, client: Gcore) -> None:
        with client.waap.domains.statistics.with_streaming_response.get_traffic_series(
            domain_id=1,
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(StatisticGetTrafficSeriesResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatistics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_ddos_attacks(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.waap.domains.statistics.get_ddos_attacks(
            domain_id=1,
        )
        assert_matches_type(AsyncOffsetPage[WaapDDOSAttack], statistic, path=["response"])

    @parametrize
    async def test_method_get_ddos_attacks_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.waap.domains.statistics.get_ddos_attacks(
            domain_id=1,
            end_time=parse_datetime("2024-04-27T13:00:00Z"),
            limit=0,
            offset=0,
            ordering="start_time",
            start_time=parse_datetime("2024-04-26T13:32:49Z"),
        )
        assert_matches_type(AsyncOffsetPage[WaapDDOSAttack], statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_ddos_attacks(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.statistics.with_raw_response.get_ddos_attacks(
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapDDOSAttack], statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_ddos_attacks(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.statistics.with_streaming_response.get_ddos_attacks(
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapDDOSAttack], statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_ddos_info(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.waap.domains.statistics.get_ddos_info(
            domain_id=1,
            group_by="URL",
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(AsyncOffsetPage[WaapDDOSInfo], statistic, path=["response"])

    @parametrize
    async def test_method_get_ddos_info_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.waap.domains.statistics.get_ddos_info(
            domain_id=1,
            group_by="URL",
            start="2024-04-13T00:00:00+01:00",
            end="2024-04-14T12:00:00Z",
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[WaapDDOSInfo], statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_ddos_info(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.statistics.with_raw_response.get_ddos_info(
            domain_id=1,
            group_by="URL",
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapDDOSInfo], statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_ddos_info(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.statistics.with_streaming_response.get_ddos_info(
            domain_id=1,
            group_by="URL",
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapDDOSInfo], statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_events_aggregated(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.waap.domains.statistics.get_events_aggregated(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(WaapEventStatistics, statistic, path=["response"])

    @parametrize
    async def test_method_get_events_aggregated_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.waap.domains.statistics.get_events_aggregated(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
            action=["block", "captcha"],
            end="2024-04-14T12:00:00Z",
            ip=["string", "string"],
            reference_id=["string", "string"],
            result=["passed", "blocked"],
        )
        assert_matches_type(WaapEventStatistics, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_events_aggregated(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.statistics.with_raw_response.get_events_aggregated(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(WaapEventStatistics, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_events_aggregated(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.statistics.with_streaming_response.get_events_aggregated(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(WaapEventStatistics, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_request_details(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.waap.domains.statistics.get_request_details(
            request_id="request_id",
            domain_id=1,
        )
        assert_matches_type(WaapRequestDetails, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_request_details(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.statistics.with_raw_response.get_request_details(
            request_id="request_id",
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(WaapRequestDetails, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_request_details(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.statistics.with_streaming_response.get_request_details(
            request_id="request_id",
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(WaapRequestDetails, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_request_details(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.waap.domains.statistics.with_raw_response.get_request_details(
                request_id="",
                domain_id=1,
            )

    @parametrize
    async def test_method_get_requests_series(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.waap.domains.statistics.get_requests_series(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(AsyncOffsetPage[WaapRequestSummary], statistic, path=["response"])

    @parametrize
    async def test_method_get_requests_series_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.waap.domains.statistics.get_requests_series(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
            actions=["allow"],
            countries=["Mv"],
            end="2024-04-14T12:00:00Z",
            ip=".:",
            limit=0,
            offset=0,
            ordering="ordering",
            reference_id="ad07c06f19054e484974fa22e9fb6bb1",
            security_rule_name="security_rule_name",
            status_code=100,
            traffic_types=["policy_allowed"],
        )
        assert_matches_type(AsyncOffsetPage[WaapRequestSummary], statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_requests_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.statistics.with_raw_response.get_requests_series(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapRequestSummary], statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_requests_series(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.statistics.with_streaming_response.get_requests_series(
            domain_id=1,
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapRequestSummary], statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_traffic_series(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.waap.domains.statistics.get_traffic_series(
            domain_id=1,
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(StatisticGetTrafficSeriesResponse, statistic, path=["response"])

    @parametrize
    async def test_method_get_traffic_series_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.waap.domains.statistics.get_traffic_series(
            domain_id=1,
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
            end="2024-04-14T12:00:00Z",
        )
        assert_matches_type(StatisticGetTrafficSeriesResponse, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_traffic_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.statistics.with_raw_response.get_traffic_series(
            domain_id=1,
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(StatisticGetTrafficSeriesResponse, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_traffic_series(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.statistics.with_streaming_response.get_traffic_series(
            domain_id=1,
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(StatisticGetTrafficSeriesResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

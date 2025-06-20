# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.waap import WaapDDOSInfo, WaapDDOSAttack, WaapEventStatistics
from gcore.types.waap.domains import (
    AnalyticsListEventTrafficResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalytics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_event_statistics(self, client: Gcore) -> None:
        analytics = client.waap.domains.analytics.get_event_statistics(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WaapEventStatistics, analytics, path=["response"])

    @parametrize
    def test_method_get_event_statistics_with_all_params(self, client: Gcore) -> None:
        analytics = client.waap.domains.analytics.get_event_statistics(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            action=["block", "captcha"],
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ip=["string", "string"],
            reference_id=["string", "string"],
            result=["passed", "blocked"],
        )
        assert_matches_type(WaapEventStatistics, analytics, path=["response"])

    @parametrize
    def test_raw_response_get_event_statistics(self, client: Gcore) -> None:
        response = client.waap.domains.analytics.with_raw_response.get_event_statistics(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(WaapEventStatistics, analytics, path=["response"])

    @parametrize
    def test_streaming_response_get_event_statistics(self, client: Gcore) -> None:
        with client.waap.domains.analytics.with_streaming_response.get_event_statistics(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(WaapEventStatistics, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_ddos_attacks(self, client: Gcore) -> None:
        analytics = client.waap.domains.analytics.list_ddos_attacks(
            domain_id=0,
        )
        assert_matches_type(SyncOffsetPage[WaapDDOSAttack], analytics, path=["response"])

    @parametrize
    def test_method_list_ddos_attacks_with_all_params(self, client: Gcore) -> None:
        analytics = client.waap.domains.analytics.list_ddos_attacks(
            domain_id=0,
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
            ordering="start_time",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[WaapDDOSAttack], analytics, path=["response"])

    @parametrize
    def test_raw_response_list_ddos_attacks(self, client: Gcore) -> None:
        response = client.waap.domains.analytics.with_raw_response.list_ddos_attacks(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(SyncOffsetPage[WaapDDOSAttack], analytics, path=["response"])

    @parametrize
    def test_streaming_response_list_ddos_attacks(self, client: Gcore) -> None:
        with client.waap.domains.analytics.with_streaming_response.list_ddos_attacks(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(SyncOffsetPage[WaapDDOSAttack], analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_ddos_info(self, client: Gcore) -> None:
        analytics = client.waap.domains.analytics.list_ddos_info(
            domain_id=0,
            group_by="URL",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[WaapDDOSInfo], analytics, path=["response"])

    @parametrize
    def test_method_list_ddos_info_with_all_params(self, client: Gcore) -> None:
        analytics = client.waap.domains.analytics.list_ddos_info(
            domain_id=0,
            group_by="URL",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[WaapDDOSInfo], analytics, path=["response"])

    @parametrize
    def test_raw_response_list_ddos_info(self, client: Gcore) -> None:
        response = client.waap.domains.analytics.with_raw_response.list_ddos_info(
            domain_id=0,
            group_by="URL",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(SyncOffsetPage[WaapDDOSInfo], analytics, path=["response"])

    @parametrize
    def test_streaming_response_list_ddos_info(self, client: Gcore) -> None:
        with client.waap.domains.analytics.with_streaming_response.list_ddos_info(
            domain_id=0,
            group_by="URL",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(SyncOffsetPage[WaapDDOSInfo], analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_event_traffic(self, client: Gcore) -> None:
        analytics = client.waap.domains.analytics.list_event_traffic(
            domain_id=0,
            resolution="daily",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticsListEventTrafficResponse, analytics, path=["response"])

    @parametrize
    def test_method_list_event_traffic_with_all_params(self, client: Gcore) -> None:
        analytics = client.waap.domains.analytics.list_event_traffic(
            domain_id=0,
            resolution="daily",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticsListEventTrafficResponse, analytics, path=["response"])

    @parametrize
    def test_raw_response_list_event_traffic(self, client: Gcore) -> None:
        response = client.waap.domains.analytics.with_raw_response.list_event_traffic(
            domain_id=0,
            resolution="daily",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsListEventTrafficResponse, analytics, path=["response"])

    @parametrize
    def test_streaming_response_list_event_traffic(self, client: Gcore) -> None:
        with client.waap.domains.analytics.with_streaming_response.list_event_traffic(
            domain_id=0,
            resolution="daily",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsListEventTrafficResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnalytics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_event_statistics(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.domains.analytics.get_event_statistics(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WaapEventStatistics, analytics, path=["response"])

    @parametrize
    async def test_method_get_event_statistics_with_all_params(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.domains.analytics.get_event_statistics(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            action=["block", "captcha"],
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ip=["string", "string"],
            reference_id=["string", "string"],
            result=["passed", "blocked"],
        )
        assert_matches_type(WaapEventStatistics, analytics, path=["response"])

    @parametrize
    async def test_raw_response_get_event_statistics(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.analytics.with_raw_response.get_event_statistics(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(WaapEventStatistics, analytics, path=["response"])

    @parametrize
    async def test_streaming_response_get_event_statistics(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.analytics.with_streaming_response.get_event_statistics(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(WaapEventStatistics, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_ddos_attacks(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.domains.analytics.list_ddos_attacks(
            domain_id=0,
        )
        assert_matches_type(AsyncOffsetPage[WaapDDOSAttack], analytics, path=["response"])

    @parametrize
    async def test_method_list_ddos_attacks_with_all_params(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.domains.analytics.list_ddos_attacks(
            domain_id=0,
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
            ordering="start_time",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[WaapDDOSAttack], analytics, path=["response"])

    @parametrize
    async def test_raw_response_list_ddos_attacks(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.analytics.with_raw_response.list_ddos_attacks(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapDDOSAttack], analytics, path=["response"])

    @parametrize
    async def test_streaming_response_list_ddos_attacks(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.analytics.with_streaming_response.list_ddos_attacks(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapDDOSAttack], analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_ddos_info(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.domains.analytics.list_ddos_info(
            domain_id=0,
            group_by="URL",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[WaapDDOSInfo], analytics, path=["response"])

    @parametrize
    async def test_method_list_ddos_info_with_all_params(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.domains.analytics.list_ddos_info(
            domain_id=0,
            group_by="URL",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[WaapDDOSInfo], analytics, path=["response"])

    @parametrize
    async def test_raw_response_list_ddos_info(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.analytics.with_raw_response.list_ddos_info(
            domain_id=0,
            group_by="URL",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapDDOSInfo], analytics, path=["response"])

    @parametrize
    async def test_streaming_response_list_ddos_info(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.analytics.with_streaming_response.list_ddos_info(
            domain_id=0,
            group_by="URL",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapDDOSInfo], analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_event_traffic(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.domains.analytics.list_event_traffic(
            domain_id=0,
            resolution="daily",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticsListEventTrafficResponse, analytics, path=["response"])

    @parametrize
    async def test_method_list_event_traffic_with_all_params(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.domains.analytics.list_event_traffic(
            domain_id=0,
            resolution="daily",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticsListEventTrafficResponse, analytics, path=["response"])

    @parametrize
    async def test_raw_response_list_event_traffic(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.analytics.with_raw_response.list_event_traffic(
            domain_id=0,
            resolution="daily",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsListEventTrafficResponse, analytics, path=["response"])

    @parametrize
    async def test_streaming_response_list_event_traffic(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.analytics.with_streaming_response.list_event_traffic(
            domain_id=0,
            resolution="daily",
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsListEventTrafficResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

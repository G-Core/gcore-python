# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.waap import (
    WaapRequestSummary,
    WaapSimpleEventStatistics,
    AnalyticsGetFiltersResponse,
    AnalyticsGetTrafficResponse,
    AnalyticsGetTrafficFilteredResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalytics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_event_statistics(self, client: Gcore) -> None:
        analytics = client.waap.analytics.get_event_statistics(
            dimension="country",
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(WaapSimpleEventStatistics, analytics, path=["response"])

    @parametrize
    def test_method_get_event_statistics_with_all_params(self, client: Gcore) -> None:
        analytics = client.waap.analytics.get_event_statistics(
            dimension="country",
            start="2024-04-13T00:00:00+01:00",
            domains=[1, 2, 3],
            end="2024-04-14T12:00:00Z",
            ips=["1.2.3.4", "2001:678:194::3c25:ddad"],
            order_by="total.desc",
            security_rule_names=["SQL injection"],
        )
        assert_matches_type(WaapSimpleEventStatistics, analytics, path=["response"])

    @parametrize
    def test_raw_response_get_event_statistics(self, client: Gcore) -> None:
        response = client.waap.analytics.with_raw_response.get_event_statistics(
            dimension="country",
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(WaapSimpleEventStatistics, analytics, path=["response"])

    @parametrize
    def test_streaming_response_get_event_statistics(self, client: Gcore) -> None:
        with client.waap.analytics.with_streaming_response.get_event_statistics(
            dimension="country",
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(WaapSimpleEventStatistics, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_filters(self, client: Gcore) -> None:
        analytics = client.waap.analytics.get_filters(
            type="user-agent-clients",
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(SyncOffsetPage[AnalyticsGetFiltersResponse], analytics, path=["response"])

    @parametrize
    def test_method_get_filters_with_all_params(self, client: Gcore) -> None:
        analytics = client.waap.analytics.get_filters(
            type="user-agent-clients",
            start="2024-04-13T00:00:00+01:00",
            domains=[1, 2, 3],
            end="2024-04-14T12:00:00Z",
            limit=50,
            name="xx",
            offset=0,
            ordering="count",
        )
        assert_matches_type(SyncOffsetPage[AnalyticsGetFiltersResponse], analytics, path=["response"])

    @parametrize
    def test_raw_response_get_filters(self, client: Gcore) -> None:
        response = client.waap.analytics.with_raw_response.get_filters(
            type="user-agent-clients",
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(SyncOffsetPage[AnalyticsGetFiltersResponse], analytics, path=["response"])

    @parametrize
    def test_streaming_response_get_filters(self, client: Gcore) -> None:
        with client.waap.analytics.with_streaming_response.get_filters(
            type="user-agent-clients",
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(SyncOffsetPage[AnalyticsGetFiltersResponse], analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_requests(self, client: Gcore) -> None:
        analytics = client.waap.analytics.get_requests(
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(SyncOffsetPage[WaapRequestSummary], analytics, path=["response"])

    @parametrize
    def test_method_get_requests_with_all_params(self, client: Gcore) -> None:
        analytics = client.waap.analytics.get_requests(
            start="2024-04-13T00:00:00+01:00",
            countries=["DE", "MY"],
            decision=["allowed", "blocked"],
            domains=[1, 2, 3],
            end="2024-04-14T12:00:00Z",
            exclude_countries=["DE", "MY"],
            exclude_decision=["allowed", "blocked"],
            exclude_domains=[0],
            exclude_http_methods=["POST", "PUT"],
            exclude_ips=["1.2.3.4", "2001:678:194::3c25:ddad"],
            exclude_ja3=["e7d705a3286e19ea42f587b344ee6865"],
            exclude_ja4=["t13d3113h2_e8f1e7e78f70_ce5650b735ce"],
            exclude_optional_action=["captcha", "challenge"],
            exclude_organizations=["Acme corp"],
            exclude_path=["/home", "/users/*/profile"],
            exclude_reference_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            exclude_request_ids=["96763b8fb655e9f18a2e04097b704e39-458959"],
            exclude_security_rule_names=["SQL injection"],
            exclude_session_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            exclude_status_codes=[100],
            exclude_tags=["mousedevice"],
            exclude_user_agent=["python-requests", "bot"],
            exclude_user_agent_clients=["OpenAI GPTBot", "Uptimerobot"],
            exclude_user_agent_devices=["SMART TV"],
            http_methods=["GET", "HEAD"],
            ips=["1.2.3.4", " 2001:678:194::3c25:ddad"],
            ja3=["e7d705a3286e19ea42f587b344ee6865"],
            ja4=["t13d3113h2_e8f1e7e78f70_ce5650b735ce"],
            limit=0,
            offset=0,
            optional_action=["captcha", "challenge"],
            ordering="userAgent",
            organizations=["Example Org", "Acme Corp"],
            path=["/home", "/users/*/profile"],
            reference_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            request_ids=["96763b8fb655e9f18a2e04097b704e39-458959"],
            security_rule_names=["SQL injection"],
            session_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            status_codes=[100],
            tags=["evasiveclient", "injectionattack"],
            user_agent=["Mozilla/5.0", "python-requests"],
            user_agent_clients=["Chrome", "Firefox"],
            user_agent_devices=["mac", "Nokia", "PlayStation"],
        )
        assert_matches_type(SyncOffsetPage[WaapRequestSummary], analytics, path=["response"])

    @parametrize
    def test_raw_response_get_requests(self, client: Gcore) -> None:
        response = client.waap.analytics.with_raw_response.get_requests(
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(SyncOffsetPage[WaapRequestSummary], analytics, path=["response"])

    @parametrize
    def test_streaming_response_get_requests(self, client: Gcore) -> None:
        with client.waap.analytics.with_streaming_response.get_requests(
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(SyncOffsetPage[WaapRequestSummary], analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_traffic(self, client: Gcore) -> None:
        analytics = client.waap.analytics.get_traffic(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(AnalyticsGetTrafficResponse, analytics, path=["response"])

    @parametrize
    def test_method_get_traffic_with_all_params(self, client: Gcore) -> None:
        analytics = client.waap.analytics.get_traffic(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
            bucket_size=60,
            domains=[1, 2, 3],
            end="2024-04-14T12:00:00Z",
        )
        assert_matches_type(AnalyticsGetTrafficResponse, analytics, path=["response"])

    @parametrize
    def test_raw_response_get_traffic(self, client: Gcore) -> None:
        response = client.waap.analytics.with_raw_response.get_traffic(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsGetTrafficResponse, analytics, path=["response"])

    @parametrize
    def test_streaming_response_get_traffic(self, client: Gcore) -> None:
        with client.waap.analytics.with_streaming_response.get_traffic(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsGetTrafficResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_traffic_filtered(self, client: Gcore) -> None:
        analytics = client.waap.analytics.get_traffic_filtered(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(AnalyticsGetTrafficFilteredResponse, analytics, path=["response"])

    @parametrize
    def test_method_get_traffic_filtered_with_all_params(self, client: Gcore) -> None:
        analytics = client.waap.analytics.get_traffic_filtered(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
            bucket_size=60,
            countries=["DE", "MY"],
            decision=["allowed", "blocked"],
            domains=[1, 2, 3],
            end="2024-04-14T12:00:00Z",
            exclude_countries=["DE", "MY"],
            exclude_decision=["allowed", "blocked"],
            exclude_domains=[0],
            exclude_http_methods=["POST", "PUT"],
            exclude_ips=["1.2.3.4", "2001:678:194::3c25:ddad"],
            exclude_ja3=["e7d705a3286e19ea42f587b344ee6865"],
            exclude_ja4=["t13d3113h2_e8f1e7e78f70_ce5650b735ce"],
            exclude_optional_action=["captcha", "challenge"],
            exclude_organizations=["Acme corp"],
            exclude_path=["/home", "/users/*/profile"],
            exclude_reference_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            exclude_request_ids=["96763b8fb655e9f18a2e04097b704e39-458959"],
            exclude_security_rule_names=["SQL injection"],
            exclude_session_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            exclude_status_codes=[100],
            exclude_tags=["mousedevice"],
            exclude_user_agent=["python-requests", "bot"],
            exclude_user_agent_clients=["OpenAI GPTBot", "Uptimerobot"],
            exclude_user_agent_devices=["SMART TV"],
            http_methods=["GET", "HEAD"],
            ips=["1.2.3.4", " 2001:678:194::3c25:ddad"],
            ja3=["e7d705a3286e19ea42f587b344ee6865"],
            ja4=["t13d3113h2_e8f1e7e78f70_ce5650b735ce"],
            optional_action=["captcha", "challenge"],
            organizations=["Example Org", "Acme Corp"],
            path=["/home", "/users/*/profile"],
            reference_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            request_ids=["96763b8fb655e9f18a2e04097b704e39-458959"],
            security_rule_names=["SQL injection"],
            session_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            status_codes=[100],
            tags=["evasiveclient", "injectionattack"],
            user_agent=["Mozilla/5.0", "python-requests"],
            user_agent_clients=["Chrome", "Firefox"],
            user_agent_devices=["mac", "Nokia", "PlayStation"],
        )
        assert_matches_type(AnalyticsGetTrafficFilteredResponse, analytics, path=["response"])

    @parametrize
    def test_raw_response_get_traffic_filtered(self, client: Gcore) -> None:
        response = client.waap.analytics.with_raw_response.get_traffic_filtered(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsGetTrafficFilteredResponse, analytics, path=["response"])

    @parametrize
    def test_streaming_response_get_traffic_filtered(self, client: Gcore) -> None:
        with client.waap.analytics.with_streaming_response.get_traffic_filtered(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsGetTrafficFilteredResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnalytics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_event_statistics(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.analytics.get_event_statistics(
            dimension="country",
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(WaapSimpleEventStatistics, analytics, path=["response"])

    @parametrize
    async def test_method_get_event_statistics_with_all_params(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.analytics.get_event_statistics(
            dimension="country",
            start="2024-04-13T00:00:00+01:00",
            domains=[1, 2, 3],
            end="2024-04-14T12:00:00Z",
            ips=["1.2.3.4", "2001:678:194::3c25:ddad"],
            order_by="total.desc",
            security_rule_names=["SQL injection"],
        )
        assert_matches_type(WaapSimpleEventStatistics, analytics, path=["response"])

    @parametrize
    async def test_raw_response_get_event_statistics(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.analytics.with_raw_response.get_event_statistics(
            dimension="country",
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(WaapSimpleEventStatistics, analytics, path=["response"])

    @parametrize
    async def test_streaming_response_get_event_statistics(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.analytics.with_streaming_response.get_event_statistics(
            dimension="country",
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(WaapSimpleEventStatistics, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_filters(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.analytics.get_filters(
            type="user-agent-clients",
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(AsyncOffsetPage[AnalyticsGetFiltersResponse], analytics, path=["response"])

    @parametrize
    async def test_method_get_filters_with_all_params(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.analytics.get_filters(
            type="user-agent-clients",
            start="2024-04-13T00:00:00+01:00",
            domains=[1, 2, 3],
            end="2024-04-14T12:00:00Z",
            limit=50,
            name="xx",
            offset=0,
            ordering="count",
        )
        assert_matches_type(AsyncOffsetPage[AnalyticsGetFiltersResponse], analytics, path=["response"])

    @parametrize
    async def test_raw_response_get_filters(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.analytics.with_raw_response.get_filters(
            type="user-agent-clients",
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AsyncOffsetPage[AnalyticsGetFiltersResponse], analytics, path=["response"])

    @parametrize
    async def test_streaming_response_get_filters(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.analytics.with_streaming_response.get_filters(
            type="user-agent-clients",
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AsyncOffsetPage[AnalyticsGetFiltersResponse], analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_requests(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.analytics.get_requests(
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(AsyncOffsetPage[WaapRequestSummary], analytics, path=["response"])

    @parametrize
    async def test_method_get_requests_with_all_params(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.analytics.get_requests(
            start="2024-04-13T00:00:00+01:00",
            countries=["DE", "MY"],
            decision=["allowed", "blocked"],
            domains=[1, 2, 3],
            end="2024-04-14T12:00:00Z",
            exclude_countries=["DE", "MY"],
            exclude_decision=["allowed", "blocked"],
            exclude_domains=[0],
            exclude_http_methods=["POST", "PUT"],
            exclude_ips=["1.2.3.4", "2001:678:194::3c25:ddad"],
            exclude_ja3=["e7d705a3286e19ea42f587b344ee6865"],
            exclude_ja4=["t13d3113h2_e8f1e7e78f70_ce5650b735ce"],
            exclude_optional_action=["captcha", "challenge"],
            exclude_organizations=["Acme corp"],
            exclude_path=["/home", "/users/*/profile"],
            exclude_reference_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            exclude_request_ids=["96763b8fb655e9f18a2e04097b704e39-458959"],
            exclude_security_rule_names=["SQL injection"],
            exclude_session_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            exclude_status_codes=[100],
            exclude_tags=["mousedevice"],
            exclude_user_agent=["python-requests", "bot"],
            exclude_user_agent_clients=["OpenAI GPTBot", "Uptimerobot"],
            exclude_user_agent_devices=["SMART TV"],
            http_methods=["GET", "HEAD"],
            ips=["1.2.3.4", " 2001:678:194::3c25:ddad"],
            ja3=["e7d705a3286e19ea42f587b344ee6865"],
            ja4=["t13d3113h2_e8f1e7e78f70_ce5650b735ce"],
            limit=0,
            offset=0,
            optional_action=["captcha", "challenge"],
            ordering="userAgent",
            organizations=["Example Org", "Acme Corp"],
            path=["/home", "/users/*/profile"],
            reference_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            request_ids=["96763b8fb655e9f18a2e04097b704e39-458959"],
            security_rule_names=["SQL injection"],
            session_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            status_codes=[100],
            tags=["evasiveclient", "injectionattack"],
            user_agent=["Mozilla/5.0", "python-requests"],
            user_agent_clients=["Chrome", "Firefox"],
            user_agent_devices=["mac", "Nokia", "PlayStation"],
        )
        assert_matches_type(AsyncOffsetPage[WaapRequestSummary], analytics, path=["response"])

    @parametrize
    async def test_raw_response_get_requests(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.analytics.with_raw_response.get_requests(
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapRequestSummary], analytics, path=["response"])

    @parametrize
    async def test_streaming_response_get_requests(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.analytics.with_streaming_response.get_requests(
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapRequestSummary], analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_traffic(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.analytics.get_traffic(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(AnalyticsGetTrafficResponse, analytics, path=["response"])

    @parametrize
    async def test_method_get_traffic_with_all_params(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.analytics.get_traffic(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
            bucket_size=60,
            domains=[1, 2, 3],
            end="2024-04-14T12:00:00Z",
        )
        assert_matches_type(AnalyticsGetTrafficResponse, analytics, path=["response"])

    @parametrize
    async def test_raw_response_get_traffic(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.analytics.with_raw_response.get_traffic(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsGetTrafficResponse, analytics, path=["response"])

    @parametrize
    async def test_streaming_response_get_traffic(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.analytics.with_streaming_response.get_traffic(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsGetTrafficResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_traffic_filtered(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.analytics.get_traffic_filtered(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        )
        assert_matches_type(AnalyticsGetTrafficFilteredResponse, analytics, path=["response"])

    @parametrize
    async def test_method_get_traffic_filtered_with_all_params(self, async_client: AsyncGcore) -> None:
        analytics = await async_client.waap.analytics.get_traffic_filtered(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
            bucket_size=60,
            countries=["DE", "MY"],
            decision=["allowed", "blocked"],
            domains=[1, 2, 3],
            end="2024-04-14T12:00:00Z",
            exclude_countries=["DE", "MY"],
            exclude_decision=["allowed", "blocked"],
            exclude_domains=[0],
            exclude_http_methods=["POST", "PUT"],
            exclude_ips=["1.2.3.4", "2001:678:194::3c25:ddad"],
            exclude_ja3=["e7d705a3286e19ea42f587b344ee6865"],
            exclude_ja4=["t13d3113h2_e8f1e7e78f70_ce5650b735ce"],
            exclude_optional_action=["captcha", "challenge"],
            exclude_organizations=["Acme corp"],
            exclude_path=["/home", "/users/*/profile"],
            exclude_reference_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            exclude_request_ids=["96763b8fb655e9f18a2e04097b704e39-458959"],
            exclude_security_rule_names=["SQL injection"],
            exclude_session_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            exclude_status_codes=[100],
            exclude_tags=["mousedevice"],
            exclude_user_agent=["python-requests", "bot"],
            exclude_user_agent_clients=["OpenAI GPTBot", "Uptimerobot"],
            exclude_user_agent_devices=["SMART TV"],
            http_methods=["GET", "HEAD"],
            ips=["1.2.3.4", " 2001:678:194::3c25:ddad"],
            ja3=["e7d705a3286e19ea42f587b344ee6865"],
            ja4=["t13d3113h2_e8f1e7e78f70_ce5650b735ce"],
            optional_action=["captcha", "challenge"],
            organizations=["Example Org", "Acme Corp"],
            path=["/home", "/users/*/profile"],
            reference_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            request_ids=["96763b8fb655e9f18a2e04097b704e39-458959"],
            security_rule_names=["SQL injection"],
            session_ids=["210b9798eb53baa4e69d31c1071cf03d"],
            status_codes=[100],
            tags=["evasiveclient", "injectionattack"],
            user_agent=["Mozilla/5.0", "python-requests"],
            user_agent_clients=["Chrome", "Firefox"],
            user_agent_devices=["mac", "Nokia", "PlayStation"],
        )
        assert_matches_type(AnalyticsGetTrafficFilteredResponse, analytics, path=["response"])

    @parametrize
    async def test_raw_response_get_traffic_filtered(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.analytics.with_raw_response.get_traffic_filtered(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsGetTrafficFilteredResponse, analytics, path=["response"])

    @parametrize
    async def test_streaming_response_get_traffic_filtered(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.analytics.with_streaming_response.get_traffic_filtered(
            resolution="daily",
            start="2024-04-13T00:00:00+01:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsGetTrafficFilteredResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

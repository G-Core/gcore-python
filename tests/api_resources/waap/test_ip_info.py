# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.waap import (
    WaapIPInfo,
    WaapIPDDOSInfoModel,
    IPInfoGetTopURLsResponse,
    IPInfoGetTopUserAgentsResponse,
    IPInfoGetBlockedRequestsResponse,
    IPInfoGetTopUserSessionsResponse,
    IPInfoGetAttackTimeSeriesResponse,
    IPInfoListAttackedCountriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPInfo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_attack_time_series(self, client: Gcore) -> None:
        ip_info = client.waap.ip_info.get_attack_time_series(
            ip="192.168.1.1",
        )
        assert_matches_type(IPInfoGetAttackTimeSeriesResponse, ip_info, path=["response"])

    @parametrize
    def test_raw_response_get_attack_time_series(self, client: Gcore) -> None:
        response = client.waap.ip_info.with_raw_response.get_attack_time_series(
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = response.parse()
        assert_matches_type(IPInfoGetAttackTimeSeriesResponse, ip_info, path=["response"])

    @parametrize
    def test_streaming_response_get_attack_time_series(self, client: Gcore) -> None:
        with client.waap.ip_info.with_streaming_response.get_attack_time_series(
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = response.parse()
            assert_matches_type(IPInfoGetAttackTimeSeriesResponse, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_blocked_requests(self, client: Gcore) -> None:
        ip_info = client.waap.ip_info.get_blocked_requests(
            domain_id=1,
            ip="192.168.1.1",
        )
        assert_matches_type(IPInfoGetBlockedRequestsResponse, ip_info, path=["response"])

    @parametrize
    def test_raw_response_get_blocked_requests(self, client: Gcore) -> None:
        response = client.waap.ip_info.with_raw_response.get_blocked_requests(
            domain_id=1,
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = response.parse()
        assert_matches_type(IPInfoGetBlockedRequestsResponse, ip_info, path=["response"])

    @parametrize
    def test_streaming_response_get_blocked_requests(self, client: Gcore) -> None:
        with client.waap.ip_info.with_streaming_response.get_blocked_requests(
            domain_id=1,
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = response.parse()
            assert_matches_type(IPInfoGetBlockedRequestsResponse, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_ddos_attack_series(self, client: Gcore) -> None:
        ip_info = client.waap.ip_info.get_ddos_attack_series(
            ip="192.168.1.1",
        )
        assert_matches_type(WaapIPDDOSInfoModel, ip_info, path=["response"])

    @parametrize
    def test_raw_response_get_ddos_attack_series(self, client: Gcore) -> None:
        response = client.waap.ip_info.with_raw_response.get_ddos_attack_series(
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = response.parse()
        assert_matches_type(WaapIPDDOSInfoModel, ip_info, path=["response"])

    @parametrize
    def test_streaming_response_get_ddos_attack_series(self, client: Gcore) -> None:
        with client.waap.ip_info.with_streaming_response.get_ddos_attack_series(
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = response.parse()
            assert_matches_type(WaapIPDDOSInfoModel, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_ip_info(self, client: Gcore) -> None:
        ip_info = client.waap.ip_info.get_ip_info(
            ip="192.168.1.1",
        )
        assert_matches_type(WaapIPInfo, ip_info, path=["response"])

    @parametrize
    def test_raw_response_get_ip_info(self, client: Gcore) -> None:
        response = client.waap.ip_info.with_raw_response.get_ip_info(
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = response.parse()
        assert_matches_type(WaapIPInfo, ip_info, path=["response"])

    @parametrize
    def test_streaming_response_get_ip_info(self, client: Gcore) -> None:
        with client.waap.ip_info.with_streaming_response.get_ip_info(
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = response.parse()
            assert_matches_type(WaapIPInfo, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_top_urls(self, client: Gcore) -> None:
        ip_info = client.waap.ip_info.get_top_urls(
            domain_id=1,
            ip="192.168.1.1",
        )
        assert_matches_type(IPInfoGetTopURLsResponse, ip_info, path=["response"])

    @parametrize
    def test_raw_response_get_top_urls(self, client: Gcore) -> None:
        response = client.waap.ip_info.with_raw_response.get_top_urls(
            domain_id=1,
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = response.parse()
        assert_matches_type(IPInfoGetTopURLsResponse, ip_info, path=["response"])

    @parametrize
    def test_streaming_response_get_top_urls(self, client: Gcore) -> None:
        with client.waap.ip_info.with_streaming_response.get_top_urls(
            domain_id=1,
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = response.parse()
            assert_matches_type(IPInfoGetTopURLsResponse, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_top_user_agents(self, client: Gcore) -> None:
        ip_info = client.waap.ip_info.get_top_user_agents(
            domain_id=1,
            ip="192.168.1.1",
        )
        assert_matches_type(IPInfoGetTopUserAgentsResponse, ip_info, path=["response"])

    @parametrize
    def test_raw_response_get_top_user_agents(self, client: Gcore) -> None:
        response = client.waap.ip_info.with_raw_response.get_top_user_agents(
            domain_id=1,
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = response.parse()
        assert_matches_type(IPInfoGetTopUserAgentsResponse, ip_info, path=["response"])

    @parametrize
    def test_streaming_response_get_top_user_agents(self, client: Gcore) -> None:
        with client.waap.ip_info.with_streaming_response.get_top_user_agents(
            domain_id=1,
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = response.parse()
            assert_matches_type(IPInfoGetTopUserAgentsResponse, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_top_user_sessions(self, client: Gcore) -> None:
        ip_info = client.waap.ip_info.get_top_user_sessions(
            domain_id=1,
            ip="192.168.1.1",
        )
        assert_matches_type(IPInfoGetTopUserSessionsResponse, ip_info, path=["response"])

    @parametrize
    def test_raw_response_get_top_user_sessions(self, client: Gcore) -> None:
        response = client.waap.ip_info.with_raw_response.get_top_user_sessions(
            domain_id=1,
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = response.parse()
        assert_matches_type(IPInfoGetTopUserSessionsResponse, ip_info, path=["response"])

    @parametrize
    def test_streaming_response_get_top_user_sessions(self, client: Gcore) -> None:
        with client.waap.ip_info.with_streaming_response.get_top_user_sessions(
            domain_id=1,
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = response.parse()
            assert_matches_type(IPInfoGetTopUserSessionsResponse, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_attacked_countries(self, client: Gcore) -> None:
        ip_info = client.waap.ip_info.list_attacked_countries(
            ip="192.168.1.1",
        )
        assert_matches_type(IPInfoListAttackedCountriesResponse, ip_info, path=["response"])

    @parametrize
    def test_raw_response_list_attacked_countries(self, client: Gcore) -> None:
        response = client.waap.ip_info.with_raw_response.list_attacked_countries(
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = response.parse()
        assert_matches_type(IPInfoListAttackedCountriesResponse, ip_info, path=["response"])

    @parametrize
    def test_streaming_response_list_attacked_countries(self, client: Gcore) -> None:
        with client.waap.ip_info.with_streaming_response.list_attacked_countries(
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = response.parse()
            assert_matches_type(IPInfoListAttackedCountriesResponse, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIPInfo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_attack_time_series(self, async_client: AsyncGcore) -> None:
        ip_info = await async_client.waap.ip_info.get_attack_time_series(
            ip="192.168.1.1",
        )
        assert_matches_type(IPInfoGetAttackTimeSeriesResponse, ip_info, path=["response"])

    @parametrize
    async def test_raw_response_get_attack_time_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.ip_info.with_raw_response.get_attack_time_series(
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = await response.parse()
        assert_matches_type(IPInfoGetAttackTimeSeriesResponse, ip_info, path=["response"])

    @parametrize
    async def test_streaming_response_get_attack_time_series(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.ip_info.with_streaming_response.get_attack_time_series(
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = await response.parse()
            assert_matches_type(IPInfoGetAttackTimeSeriesResponse, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_blocked_requests(self, async_client: AsyncGcore) -> None:
        ip_info = await async_client.waap.ip_info.get_blocked_requests(
            domain_id=1,
            ip="192.168.1.1",
        )
        assert_matches_type(IPInfoGetBlockedRequestsResponse, ip_info, path=["response"])

    @parametrize
    async def test_raw_response_get_blocked_requests(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.ip_info.with_raw_response.get_blocked_requests(
            domain_id=1,
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = await response.parse()
        assert_matches_type(IPInfoGetBlockedRequestsResponse, ip_info, path=["response"])

    @parametrize
    async def test_streaming_response_get_blocked_requests(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.ip_info.with_streaming_response.get_blocked_requests(
            domain_id=1,
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = await response.parse()
            assert_matches_type(IPInfoGetBlockedRequestsResponse, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_ddos_attack_series(self, async_client: AsyncGcore) -> None:
        ip_info = await async_client.waap.ip_info.get_ddos_attack_series(
            ip="192.168.1.1",
        )
        assert_matches_type(WaapIPDDOSInfoModel, ip_info, path=["response"])

    @parametrize
    async def test_raw_response_get_ddos_attack_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.ip_info.with_raw_response.get_ddos_attack_series(
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = await response.parse()
        assert_matches_type(WaapIPDDOSInfoModel, ip_info, path=["response"])

    @parametrize
    async def test_streaming_response_get_ddos_attack_series(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.ip_info.with_streaming_response.get_ddos_attack_series(
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = await response.parse()
            assert_matches_type(WaapIPDDOSInfoModel, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_ip_info(self, async_client: AsyncGcore) -> None:
        ip_info = await async_client.waap.ip_info.get_ip_info(
            ip="192.168.1.1",
        )
        assert_matches_type(WaapIPInfo, ip_info, path=["response"])

    @parametrize
    async def test_raw_response_get_ip_info(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.ip_info.with_raw_response.get_ip_info(
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = await response.parse()
        assert_matches_type(WaapIPInfo, ip_info, path=["response"])

    @parametrize
    async def test_streaming_response_get_ip_info(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.ip_info.with_streaming_response.get_ip_info(
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = await response.parse()
            assert_matches_type(WaapIPInfo, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_top_urls(self, async_client: AsyncGcore) -> None:
        ip_info = await async_client.waap.ip_info.get_top_urls(
            domain_id=1,
            ip="192.168.1.1",
        )
        assert_matches_type(IPInfoGetTopURLsResponse, ip_info, path=["response"])

    @parametrize
    async def test_raw_response_get_top_urls(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.ip_info.with_raw_response.get_top_urls(
            domain_id=1,
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = await response.parse()
        assert_matches_type(IPInfoGetTopURLsResponse, ip_info, path=["response"])

    @parametrize
    async def test_streaming_response_get_top_urls(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.ip_info.with_streaming_response.get_top_urls(
            domain_id=1,
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = await response.parse()
            assert_matches_type(IPInfoGetTopURLsResponse, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_top_user_agents(self, async_client: AsyncGcore) -> None:
        ip_info = await async_client.waap.ip_info.get_top_user_agents(
            domain_id=1,
            ip="192.168.1.1",
        )
        assert_matches_type(IPInfoGetTopUserAgentsResponse, ip_info, path=["response"])

    @parametrize
    async def test_raw_response_get_top_user_agents(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.ip_info.with_raw_response.get_top_user_agents(
            domain_id=1,
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = await response.parse()
        assert_matches_type(IPInfoGetTopUserAgentsResponse, ip_info, path=["response"])

    @parametrize
    async def test_streaming_response_get_top_user_agents(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.ip_info.with_streaming_response.get_top_user_agents(
            domain_id=1,
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = await response.parse()
            assert_matches_type(IPInfoGetTopUserAgentsResponse, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_top_user_sessions(self, async_client: AsyncGcore) -> None:
        ip_info = await async_client.waap.ip_info.get_top_user_sessions(
            domain_id=1,
            ip="192.168.1.1",
        )
        assert_matches_type(IPInfoGetTopUserSessionsResponse, ip_info, path=["response"])

    @parametrize
    async def test_raw_response_get_top_user_sessions(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.ip_info.with_raw_response.get_top_user_sessions(
            domain_id=1,
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = await response.parse()
        assert_matches_type(IPInfoGetTopUserSessionsResponse, ip_info, path=["response"])

    @parametrize
    async def test_streaming_response_get_top_user_sessions(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.ip_info.with_streaming_response.get_top_user_sessions(
            domain_id=1,
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = await response.parse()
            assert_matches_type(IPInfoGetTopUserSessionsResponse, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_attacked_countries(self, async_client: AsyncGcore) -> None:
        ip_info = await async_client.waap.ip_info.list_attacked_countries(
            ip="192.168.1.1",
        )
        assert_matches_type(IPInfoListAttackedCountriesResponse, ip_info, path=["response"])

    @parametrize
    async def test_raw_response_list_attacked_countries(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.ip_info.with_raw_response.list_attacked_countries(
            ip="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_info = await response.parse()
        assert_matches_type(IPInfoListAttackedCountriesResponse, ip_info, path=["response"])

    @parametrize
    async def test_streaming_response_list_attacked_countries(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.ip_info.with_streaming_response.list_attacked_countries(
            ip="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_info = await response.parse()
            assert_matches_type(IPInfoListAttackedCountriesResponse, ip_info, path=["response"])

        assert cast(Any, response.is_closed) is True

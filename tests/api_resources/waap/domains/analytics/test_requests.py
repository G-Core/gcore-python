# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.waap import WaapRequestDetails, WaapRequestSummary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        request = client.waap.domains.analytics.requests.list(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[WaapRequestSummary], request, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        request = client.waap.domains.analytics.requests.list(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            actions=["allow"],
            countries=["Mv"],
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ip=".:",
            limit=0,
            offset=0,
            ordering="ordering",
            reference_id="2c02efDd09B3BA1AEaDd3dCAa7aC7A37",
            security_rule_name="security_rule_name",
            status_code=100,
            traffic_types=["policy_allowed"],
        )
        assert_matches_type(SyncOffsetPage[WaapRequestSummary], request, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.waap.domains.analytics.requests.with_raw_response.list(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(SyncOffsetPage[WaapRequestSummary], request, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.waap.domains.analytics.requests.with_streaming_response.list(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(SyncOffsetPage[WaapRequestSummary], request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        request = client.waap.domains.analytics.requests.get(
            request_id="request_id",
            domain_id=0,
        )
        assert_matches_type(WaapRequestDetails, request, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.waap.domains.analytics.requests.with_raw_response.get(
            request_id="request_id",
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(WaapRequestDetails, request, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.waap.domains.analytics.requests.with_streaming_response.get(
            request_id="request_id",
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(WaapRequestDetails, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.waap.domains.analytics.requests.with_raw_response.get(
                request_id="",
                domain_id=0,
            )


class TestAsyncRequests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        request = await async_client.waap.domains.analytics.requests.list(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[WaapRequestSummary], request, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        request = await async_client.waap.domains.analytics.requests.list(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            actions=["allow"],
            countries=["Mv"],
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ip=".:",
            limit=0,
            offset=0,
            ordering="ordering",
            reference_id="2c02efDd09B3BA1AEaDd3dCAa7aC7A37",
            security_rule_name="security_rule_name",
            status_code=100,
            traffic_types=["policy_allowed"],
        )
        assert_matches_type(AsyncOffsetPage[WaapRequestSummary], request, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.analytics.requests.with_raw_response.list(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapRequestSummary], request, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.analytics.requests.with_streaming_response.list(
            domain_id=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapRequestSummary], request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        request = await async_client.waap.domains.analytics.requests.get(
            request_id="request_id",
            domain_id=0,
        )
        assert_matches_type(WaapRequestDetails, request, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.analytics.requests.with_raw_response.get(
            request_id="request_id",
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(WaapRequestDetails, request, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.analytics.requests.with_streaming_response.get(
            request_id="request_id",
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(WaapRequestDetails, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.waap.domains.analytics.requests.with_raw_response.get(
                request_id="",
                domain_id=0,
            )

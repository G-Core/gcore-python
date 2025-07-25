# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.types.cloud import UsageReport

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsageReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        usage_report = client.cloud.usage_reports.get(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        )
        assert_matches_type(UsageReport, usage_report, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Gcore) -> None:
        usage_report = client.cloud.usage_reports.get(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
            enable_last_day=False,
            limit=10,
            offset=0,
            projects=[16, 17, 18, 19, 20],
            regions=[1, 2, 3],
            schema_filter={
                "field": "flavor",
                "type": "instance",
                "values": ["g1-standard-1-2"],
            },
            sorting=[
                {
                    "billing_value": "asc",
                    "first_seen": "asc",
                    "last_name": "asc",
                    "last_seen": "asc",
                    "project": "asc",
                    "region": "asc",
                    "type": "asc",
                }
            ],
            tags={
                "conditions": [
                    {
                        "key": "os_version",
                        "strict": True,
                        "value": "22.04",
                    },
                    {
                        "key": "os_version",
                        "strict": True,
                        "value": "23.04",
                    },
                ],
                "condition_type": "OR",
            },
            types=["egress_traffic", "instance"],
        )
        assert_matches_type(UsageReport, usage_report, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.usage_reports.with_raw_response.get(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_report = response.parse()
        assert_matches_type(UsageReport, usage_report, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.usage_reports.with_streaming_response.get(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_report = response.parse()
            assert_matches_type(UsageReport, usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsageReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        usage_report = await async_client.cloud.usage_reports.get(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        )
        assert_matches_type(UsageReport, usage_report, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncGcore) -> None:
        usage_report = await async_client.cloud.usage_reports.get(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
            enable_last_day=False,
            limit=10,
            offset=0,
            projects=[16, 17, 18, 19, 20],
            regions=[1, 2, 3],
            schema_filter={
                "field": "flavor",
                "type": "instance",
                "values": ["g1-standard-1-2"],
            },
            sorting=[
                {
                    "billing_value": "asc",
                    "first_seen": "asc",
                    "last_name": "asc",
                    "last_seen": "asc",
                    "project": "asc",
                    "region": "asc",
                    "type": "asc",
                }
            ],
            tags={
                "conditions": [
                    {
                        "key": "os_version",
                        "strict": True,
                        "value": "22.04",
                    },
                    {
                        "key": "os_version",
                        "strict": True,
                        "value": "23.04",
                    },
                ],
                "condition_type": "OR",
            },
            types=["egress_traffic", "instance"],
        )
        assert_matches_type(UsageReport, usage_report, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.usage_reports.with_raw_response.get(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_report = await response.parse()
        assert_matches_type(UsageReport, usage_report, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.usage_reports.with_streaming_response.get(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_report = await response.parse()
            assert_matches_type(UsageReport, usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.types.cloud import (
    CostReportDetailed,
    CostReportAggregated,
    CostReportAggregatedMonthly,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCostReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_aggregated(self, client: Gcore) -> None:
        cost_report = client.cloud.cost_reports.get_aggregated(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        )
        assert_matches_type(CostReportAggregated, cost_report, path=["response"])

    @parametrize
    def test_method_get_aggregated_with_all_params(self, client: Gcore) -> None:
        cost_report = client.cloud.cost_reports.get_aggregated(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
            enable_last_day=False,
            projects=[16, 17, 18, 19, 20],
            regions=[1, 2, 3],
            response_format="csv_totals",
            rounding=True,
            schema_filter={
                "field": "flavor",
                "type": "instance",
                "values": ["g1-standard-1-2"],
            },
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
        assert_matches_type(CostReportAggregated, cost_report, path=["response"])

    @parametrize
    def test_raw_response_get_aggregated(self, client: Gcore) -> None:
        response = client.cloud.cost_reports.with_raw_response.get_aggregated(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost_report = response.parse()
        assert_matches_type(CostReportAggregated, cost_report, path=["response"])

    @parametrize
    def test_streaming_response_get_aggregated(self, client: Gcore) -> None:
        with client.cloud.cost_reports.with_streaming_response.get_aggregated(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost_report = response.parse()
            assert_matches_type(CostReportAggregated, cost_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_aggregated_monthly(self, client: Gcore) -> None:
        cost_report = client.cloud.cost_reports.get_aggregated_monthly()
        assert_matches_type(CostReportAggregatedMonthly, cost_report, path=["response"])

    @parametrize
    def test_method_get_aggregated_monthly_with_all_params(self, client: Gcore) -> None:
        cost_report = client.cloud.cost_reports.get_aggregated_monthly(
            regions=[1, 2, 3],
            response_format="csv_totals",
            rounding=True,
            schema_filter={
                "field": "flavor",
                "type": "instance",
                "values": ["g1-standard-1-2"],
            },
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
            time_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            time_to=parse_datetime("2019-12-27T18:11:19.117Z"),
            types=["egress_traffic", "instance"],
            year_month="2024-08",
        )
        assert_matches_type(CostReportAggregatedMonthly, cost_report, path=["response"])

    @parametrize
    def test_raw_response_get_aggregated_monthly(self, client: Gcore) -> None:
        response = client.cloud.cost_reports.with_raw_response.get_aggregated_monthly()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost_report = response.parse()
        assert_matches_type(CostReportAggregatedMonthly, cost_report, path=["response"])

    @parametrize
    def test_streaming_response_get_aggregated_monthly(self, client: Gcore) -> None:
        with client.cloud.cost_reports.with_streaming_response.get_aggregated_monthly() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost_report = response.parse()
            assert_matches_type(CostReportAggregatedMonthly, cost_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_detailed(self, client: Gcore) -> None:
        cost_report = client.cloud.cost_reports.get_detailed(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        )
        assert_matches_type(CostReportDetailed, cost_report, path=["response"])

    @parametrize
    def test_method_get_detailed_with_all_params(self, client: Gcore) -> None:
        cost_report = client.cloud.cost_reports.get_detailed(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
            enable_last_day=False,
            limit=10,
            offset=0,
            projects=[16, 17, 18, 19, 20],
            regions=[1, 2, 3],
            response_format="csv_records",
            rounding=True,
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
        assert_matches_type(CostReportDetailed, cost_report, path=["response"])

    @parametrize
    def test_raw_response_get_detailed(self, client: Gcore) -> None:
        response = client.cloud.cost_reports.with_raw_response.get_detailed(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost_report = response.parse()
        assert_matches_type(CostReportDetailed, cost_report, path=["response"])

    @parametrize
    def test_streaming_response_get_detailed(self, client: Gcore) -> None:
        with client.cloud.cost_reports.with_streaming_response.get_detailed(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost_report = response.parse()
            assert_matches_type(CostReportDetailed, cost_report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCostReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_aggregated(self, async_client: AsyncGcore) -> None:
        cost_report = await async_client.cloud.cost_reports.get_aggregated(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        )
        assert_matches_type(CostReportAggregated, cost_report, path=["response"])

    @parametrize
    async def test_method_get_aggregated_with_all_params(self, async_client: AsyncGcore) -> None:
        cost_report = await async_client.cloud.cost_reports.get_aggregated(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
            enable_last_day=False,
            projects=[16, 17, 18, 19, 20],
            regions=[1, 2, 3],
            response_format="csv_totals",
            rounding=True,
            schema_filter={
                "field": "flavor",
                "type": "instance",
                "values": ["g1-standard-1-2"],
            },
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
        assert_matches_type(CostReportAggregated, cost_report, path=["response"])

    @parametrize
    async def test_raw_response_get_aggregated(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.cost_reports.with_raw_response.get_aggregated(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost_report = await response.parse()
        assert_matches_type(CostReportAggregated, cost_report, path=["response"])

    @parametrize
    async def test_streaming_response_get_aggregated(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.cost_reports.with_streaming_response.get_aggregated(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost_report = await response.parse()
            assert_matches_type(CostReportAggregated, cost_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_aggregated_monthly(self, async_client: AsyncGcore) -> None:
        cost_report = await async_client.cloud.cost_reports.get_aggregated_monthly()
        assert_matches_type(CostReportAggregatedMonthly, cost_report, path=["response"])

    @parametrize
    async def test_method_get_aggregated_monthly_with_all_params(self, async_client: AsyncGcore) -> None:
        cost_report = await async_client.cloud.cost_reports.get_aggregated_monthly(
            regions=[1, 2, 3],
            response_format="csv_totals",
            rounding=True,
            schema_filter={
                "field": "flavor",
                "type": "instance",
                "values": ["g1-standard-1-2"],
            },
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
            time_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            time_to=parse_datetime("2019-12-27T18:11:19.117Z"),
            types=["egress_traffic", "instance"],
            year_month="2024-08",
        )
        assert_matches_type(CostReportAggregatedMonthly, cost_report, path=["response"])

    @parametrize
    async def test_raw_response_get_aggregated_monthly(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.cost_reports.with_raw_response.get_aggregated_monthly()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost_report = await response.parse()
        assert_matches_type(CostReportAggregatedMonthly, cost_report, path=["response"])

    @parametrize
    async def test_streaming_response_get_aggregated_monthly(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.cost_reports.with_streaming_response.get_aggregated_monthly() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost_report = await response.parse()
            assert_matches_type(CostReportAggregatedMonthly, cost_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_detailed(self, async_client: AsyncGcore) -> None:
        cost_report = await async_client.cloud.cost_reports.get_detailed(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        )
        assert_matches_type(CostReportDetailed, cost_report, path=["response"])

    @parametrize
    async def test_method_get_detailed_with_all_params(self, async_client: AsyncGcore) -> None:
        cost_report = await async_client.cloud.cost_reports.get_detailed(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
            enable_last_day=False,
            limit=10,
            offset=0,
            projects=[16, 17, 18, 19, 20],
            regions=[1, 2, 3],
            response_format="csv_records",
            rounding=True,
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
        assert_matches_type(CostReportDetailed, cost_report, path=["response"])

    @parametrize
    async def test_raw_response_get_detailed(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.cost_reports.with_raw_response.get_detailed(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost_report = await response.parse()
        assert_matches_type(CostReportDetailed, cost_report, path=["response"])

    @parametrize
    async def test_streaming_response_get_detailed(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.cost_reports.with_streaming_response.get_detailed(
            time_from=parse_datetime("2023-01-01T00:00:00Z"),
            time_to=parse_datetime("2023-02-01T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost_report = await response.parse()
            assert_matches_type(CostReportDetailed, cost_report, path=["response"])

        assert cast(Any, response.is_closed) is True

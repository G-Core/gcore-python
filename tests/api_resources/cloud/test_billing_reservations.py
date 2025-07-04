# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_date, parse_datetime
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import BillingReservation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBillingReservations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        billing_reservation = client.cloud.billing_reservations.list()
        assert_matches_type(SyncOffsetPage[BillingReservation], billing_reservation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        billing_reservation = client.cloud.billing_reservations.list(
            activated_from=parse_date("2019-12-27"),
            activated_to=parse_date("2019-12-27"),
            created_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_to=parse_datetime("2019-12-27T18:11:19.117Z"),
            deactivated_from=parse_date("2019-12-27"),
            deactivated_to=parse_date("2019-12-27"),
            limit=1,
            metric_name="metric_name",
            offset=0,
            order_by="active_from.asc",
            region_id=0,
            status=["ACTIVATED"],
        )
        assert_matches_type(SyncOffsetPage[BillingReservation], billing_reservation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.billing_reservations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_reservation = response.parse()
        assert_matches_type(SyncOffsetPage[BillingReservation], billing_reservation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.billing_reservations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_reservation = response.parse()
            assert_matches_type(SyncOffsetPage[BillingReservation], billing_reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        billing_reservation = client.cloud.billing_reservations.get(
            0,
        )
        assert_matches_type(BillingReservation, billing_reservation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.billing_reservations.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_reservation = response.parse()
        assert_matches_type(BillingReservation, billing_reservation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.billing_reservations.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_reservation = response.parse()
            assert_matches_type(BillingReservation, billing_reservation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBillingReservations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        billing_reservation = await async_client.cloud.billing_reservations.list()
        assert_matches_type(AsyncOffsetPage[BillingReservation], billing_reservation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        billing_reservation = await async_client.cloud.billing_reservations.list(
            activated_from=parse_date("2019-12-27"),
            activated_to=parse_date("2019-12-27"),
            created_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_to=parse_datetime("2019-12-27T18:11:19.117Z"),
            deactivated_from=parse_date("2019-12-27"),
            deactivated_to=parse_date("2019-12-27"),
            limit=1,
            metric_name="metric_name",
            offset=0,
            order_by="active_from.asc",
            region_id=0,
            status=["ACTIVATED"],
        )
        assert_matches_type(AsyncOffsetPage[BillingReservation], billing_reservation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.billing_reservations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_reservation = await response.parse()
        assert_matches_type(AsyncOffsetPage[BillingReservation], billing_reservation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.billing_reservations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_reservation = await response.parse()
            assert_matches_type(AsyncOffsetPage[BillingReservation], billing_reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        billing_reservation = await async_client.cloud.billing_reservations.get(
            0,
        )
        assert_matches_type(BillingReservation, billing_reservation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.billing_reservations.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_reservation = await response.parse()
        assert_matches_type(BillingReservation, billing_reservation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.billing_reservations.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_reservation = await response.parse()
            assert_matches_type(BillingReservation, billing_reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

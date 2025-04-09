# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.quotas import RegionalQuotas

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegional:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Gcore) -> None:
        regional = client.cloud.quotas.regional.retrieve(
            client_id=3,
            region_id=1,
        )
        assert_matches_type(RegionalQuotas, regional, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gcore) -> None:
        response = client.cloud.quotas.regional.with_raw_response.retrieve(
            client_id=3,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regional = response.parse()
        assert_matches_type(RegionalQuotas, regional, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gcore) -> None:
        with client.cloud.quotas.regional.with_streaming_response.retrieve(
            client_id=3,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regional = response.parse()
            assert_matches_type(RegionalQuotas, regional, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRegional:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGcore) -> None:
        regional = await async_client.cloud.quotas.regional.retrieve(
            client_id=3,
            region_id=1,
        )
        assert_matches_type(RegionalQuotas, regional, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.quotas.regional.with_raw_response.retrieve(
            client_id=3,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regional = await response.parse()
        assert_matches_type(RegionalQuotas, regional, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.quotas.regional.with_streaming_response.retrieve(
            client_id=3,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regional = await response.parse()
            assert_matches_type(RegionalQuotas, regional, path=["response"])

        assert cast(Any, response.is_closed) is True

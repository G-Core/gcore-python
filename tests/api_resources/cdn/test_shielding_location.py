# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn import ShieldingLocation
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShieldingLocation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        shielding_location = client.cdn.shielding_location.list()
        assert_matches_type(SyncOffsetPage[ShieldingLocation], shielding_location, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        shielding_location = client.cdn.shielding_location.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[ShieldingLocation], shielding_location, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.shielding_location.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shielding_location = response.parse()
        assert_matches_type(SyncOffsetPage[ShieldingLocation], shielding_location, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.shielding_location.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shielding_location = response.parse()
            assert_matches_type(SyncOffsetPage[ShieldingLocation], shielding_location, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShieldingLocation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        shielding_location = await async_client.cdn.shielding_location.list()
        assert_matches_type(AsyncOffsetPage[ShieldingLocation], shielding_location, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        shielding_location = await async_client.cdn.shielding_location.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[ShieldingLocation], shielding_location, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.shielding_location.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shielding_location = await response.parse()
        assert_matches_type(AsyncOffsetPage[ShieldingLocation], shielding_location, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.shielding_location.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shielding_location = await response.parse()
            assert_matches_type(AsyncOffsetPage[ShieldingLocation], shielding_location, path=["response"])

        assert cast(Any, response.is_closed) is True

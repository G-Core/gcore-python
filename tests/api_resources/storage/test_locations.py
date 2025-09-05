# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.storage import LocationListResponse

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        with pytest.warns(DeprecationWarning):
            location = client.storage.locations.list()

        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.storage.locations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with pytest.warns(DeprecationWarning):
            with client.storage.locations.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                location = response.parse()
                assert_matches_type(LocationListResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLocations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        with pytest.warns(DeprecationWarning):
            location = await async_client.storage.locations.list()

        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.storage.locations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.storage.locations.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                location = await response.parse()
                assert_matches_type(LocationListResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

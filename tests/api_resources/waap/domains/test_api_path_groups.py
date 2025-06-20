# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.waap.domains import APIPathGroupListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIPathGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        api_path_group = client.waap.domains.api_path_groups.list(
            0,
        )
        assert_matches_type(APIPathGroupListResponse, api_path_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.waap.domains.api_path_groups.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_path_group = response.parse()
        assert_matches_type(APIPathGroupListResponse, api_path_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.waap.domains.api_path_groups.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_path_group = response.parse()
            assert_matches_type(APIPathGroupListResponse, api_path_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIPathGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        api_path_group = await async_client.waap.domains.api_path_groups.list(
            0,
        )
        assert_matches_type(APIPathGroupListResponse, api_path_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_path_groups.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_path_group = await response.parse()
        assert_matches_type(APIPathGroupListResponse, api_path_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_path_groups.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_path_group = await response.parse()
            assert_matches_type(APIPathGroupListResponse, api_path_group, path=["response"])

        assert cast(Any, response.is_closed) is True

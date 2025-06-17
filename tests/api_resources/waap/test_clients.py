# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.waap import ClientMeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClients:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_me(self, client: Gcore) -> None:
        client_ = client.waap.clients.me()
        assert_matches_type(ClientMeResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_me(self, client: Gcore) -> None:
        response = client.waap.clients.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ClientMeResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_me(self, client: Gcore) -> None:
        with client.waap.clients.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ClientMeResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClients:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_me(self, async_client: AsyncGcore) -> None:
        client = await async_client.waap.clients.me()
        assert_matches_type(ClientMeResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_me(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.clients.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ClientMeResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_me(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.clients.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ClientMeResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

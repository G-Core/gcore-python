# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.fastedge import Binary, BinaryListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBinaries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        binary = client.fastedge.binaries.list()
        assert_matches_type(BinaryListResponse, binary, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.fastedge.binaries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binary = response.parse()
        assert_matches_type(BinaryListResponse, binary, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.fastedge.binaries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binary = response.parse()
            assert_matches_type(BinaryListResponse, binary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        binary = client.fastedge.binaries.delete(
            0,
        )
        assert binary is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.fastedge.binaries.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binary = response.parse()
        assert binary is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.fastedge.binaries.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binary = response.parse()
            assert binary is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        binary = client.fastedge.binaries.get(
            0,
        )
        assert_matches_type(Binary, binary, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.fastedge.binaries.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binary = response.parse()
        assert_matches_type(Binary, binary, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.fastedge.binaries.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binary = response.parse()
            assert_matches_type(Binary, binary, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBinaries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        binary = await async_client.fastedge.binaries.list()
        assert_matches_type(BinaryListResponse, binary, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.binaries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binary = await response.parse()
        assert_matches_type(BinaryListResponse, binary, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.binaries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binary = await response.parse()
            assert_matches_type(BinaryListResponse, binary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        binary = await async_client.fastedge.binaries.delete(
            0,
        )
        assert binary is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.binaries.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binary = await response.parse()
        assert binary is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.binaries.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binary = await response.parse()
            assert binary is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        binary = await async_client.fastedge.binaries.get(
            0,
        )
        assert_matches_type(Binary, binary, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.binaries.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binary = await response.parse()
        assert_matches_type(Binary, binary, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.binaries.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binary = await response.parse()
            assert_matches_type(Binary, binary, path=["response"])

        assert cast(Any, response.is_closed) is True

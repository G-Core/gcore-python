# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn import CDNAccount

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClientConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        client_config = client.cdn.client_config.update()
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        client_config = client.cdn.client_config.update(
            utilization_level=1111,
        )
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cdn.client_config.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_config = response.parse()
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cdn.client_config.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_config = response.parse()
            assert_matches_type(CDNAccount, client_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        client_config = client.cdn.client_config.get()
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cdn.client_config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_config = response.parse()
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cdn.client_config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_config = response.parse()
            assert_matches_type(CDNAccount, client_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        client_config = client.cdn.client_config.replace()
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        client_config = client.cdn.client_config.replace(
            utilization_level=1111,
        )
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.cdn.client_config.with_raw_response.replace()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_config = response.parse()
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.cdn.client_config.with_streaming_response.replace() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_config = response.parse()
            assert_matches_type(CDNAccount, client_config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClientConfig:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        client_config = await async_client.cdn.client_config.update()
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        client_config = await async_client.cdn.client_config.update(
            utilization_level=1111,
        )
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.client_config.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_config = await response.parse()
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.client_config.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_config = await response.parse()
            assert_matches_type(CDNAccount, client_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        client_config = await async_client.cdn.client_config.get()
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.client_config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_config = await response.parse()
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.client_config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_config = await response.parse()
            assert_matches_type(CDNAccount, client_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        client_config = await async_client.cdn.client_config.replace()
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        client_config = await async_client.cdn.client_config.replace(
            utilization_level=1111,
        )
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.client_config.with_raw_response.replace()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_config = await response.parse()
        assert_matches_type(CDNAccount, client_config, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.client_config.with_streaming_response.replace() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_config = await response.parse()
            assert_matches_type(CDNAccount, client_config, path=["response"])

        assert cast(Any, response.is_closed) is True

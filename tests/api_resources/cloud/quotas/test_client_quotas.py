# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.quotas import AllClientQuotas

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClientQuotas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Gcore) -> None:
        client_quota = client.cloud.quotas.client_quotas.retrieve()
        assert_matches_type(AllClientQuotas, client_quota, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gcore) -> None:
        response = client.cloud.quotas.client_quotas.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_quota = response.parse()
        assert_matches_type(AllClientQuotas, client_quota, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gcore) -> None:
        with client.cloud.quotas.client_quotas.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_quota = response.parse()
            assert_matches_type(AllClientQuotas, client_quota, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClientQuotas:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGcore) -> None:
        client_quota = await async_client.cloud.quotas.client_quotas.retrieve()
        assert_matches_type(AllClientQuotas, client_quota, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.quotas.client_quotas.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_quota = await response.parse()
        assert_matches_type(AllClientQuotas, client_quota, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.quotas.client_quotas.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_quota = await response.parse()
            assert_matches_type(AllClientQuotas, client_quota, path=["response"])

        assert cast(Any, response.is_closed) is True

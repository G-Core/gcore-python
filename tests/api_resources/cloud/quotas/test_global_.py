# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.quotas import GlobalQuotas

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGlobal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Gcore) -> None:
        global_ = client.cloud.quotas.global_.retrieve(
            3,
        )
        assert_matches_type(GlobalQuotas, global_, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gcore) -> None:
        response = client.cloud.quotas.global_.with_raw_response.retrieve(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ = response.parse()
        assert_matches_type(GlobalQuotas, global_, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gcore) -> None:
        with client.cloud.quotas.global_.with_streaming_response.retrieve(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ = response.parse()
            assert_matches_type(GlobalQuotas, global_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGlobal:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGcore) -> None:
        global_ = await async_client.cloud.quotas.global_.retrieve(
            3,
        )
        assert_matches_type(GlobalQuotas, global_, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.quotas.global_.with_raw_response.retrieve(
            3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ = await response.parse()
        assert_matches_type(GlobalQuotas, global_, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.quotas.global_.with_streaming_response.retrieve(
            3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ = await response.parse()
            assert_matches_type(GlobalQuotas, global_, path=["response"])

        assert cast(Any, response.is_closed) is True

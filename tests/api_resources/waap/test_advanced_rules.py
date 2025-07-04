# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.waap import WaapAdvancedRuleDescriptorList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdvancedRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        advanced_rule = client.waap.advanced_rules.list()
        assert_matches_type(WaapAdvancedRuleDescriptorList, advanced_rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.waap.advanced_rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advanced_rule = response.parse()
        assert_matches_type(WaapAdvancedRuleDescriptorList, advanced_rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.waap.advanced_rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advanced_rule = response.parse()
            assert_matches_type(WaapAdvancedRuleDescriptorList, advanced_rule, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdvancedRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        advanced_rule = await async_client.waap.advanced_rules.list()
        assert_matches_type(WaapAdvancedRuleDescriptorList, advanced_rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.advanced_rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advanced_rule = await response.parse()
        assert_matches_type(WaapAdvancedRuleDescriptorList, advanced_rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.advanced_rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advanced_rule = await response.parse()
            assert_matches_type(WaapAdvancedRuleDescriptorList, advanced_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

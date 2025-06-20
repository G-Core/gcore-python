# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.waap import WaapPolicyMode

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_toggle(self, client: Gcore) -> None:
        policy = client.waap.domains.policies.toggle(
            policy_id="policy_id",
            domain_id=0,
        )
        assert_matches_type(WaapPolicyMode, policy, path=["response"])

    @parametrize
    def test_raw_response_toggle(self, client: Gcore) -> None:
        response = client.waap.domains.policies.with_raw_response.toggle(
            policy_id="policy_id",
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(WaapPolicyMode, policy, path=["response"])

    @parametrize
    def test_streaming_response_toggle(self, client: Gcore) -> None:
        with client.waap.domains.policies.with_streaming_response.toggle(
            policy_id="policy_id",
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(WaapPolicyMode, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_toggle(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.waap.domains.policies.with_raw_response.toggle(
                policy_id="",
                domain_id=0,
            )


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_toggle(self, async_client: AsyncGcore) -> None:
        policy = await async_client.waap.domains.policies.toggle(
            policy_id="policy_id",
            domain_id=0,
        )
        assert_matches_type(WaapPolicyMode, policy, path=["response"])

    @parametrize
    async def test_raw_response_toggle(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.policies.with_raw_response.toggle(
            policy_id="policy_id",
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(WaapPolicyMode, policy, path=["response"])

    @parametrize
    async def test_streaming_response_toggle(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.policies.with_streaming_response.toggle(
            policy_id="policy_id",
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(WaapPolicyMode, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_toggle(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.waap.domains.policies.with_raw_response.toggle(
                policy_id="",
                domain_id=0,
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.waap.domains import (
    WaapPolicyOverride,
    WaapOwaspTopThreatsTarget,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicyOverrides:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        policy_override = client.waap.domains.policy_overrides.create(
            domain_id=1,
            enabled=True,
            name="x",
            target_ids=[1],
            target_type="detector",
        )
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        policy_override = client.waap.domains.policy_overrides.create(
            domain_id=1,
            enabled=True,
            name="x",
            target_ids=[1],
            target_type="detector",
            conditions=[
                {
                    "country": {
                        "country_code": ["Mv"],
                        "negation": True,
                    },
                    "header": {
                        "header": "Origin",
                        "value": "value",
                        "match_type": "Exact",
                        "negation": True,
                    },
                    "header_exists": {
                        "header": "Origin",
                        "negation": True,
                    },
                    "http_method": {
                        "http_method": "CONNECT",
                        "negation": True,
                    },
                    "ip": {
                        "ip_address": "ip_address",
                        "negation": True,
                    },
                    "ip_range": {
                        "lower_bound": "lower_bound",
                        "upper_bound": "upper_bound",
                        "negation": True,
                    },
                    "ja3": {
                        "ja3_fingerprints": ["e7d705a3286e19ea42f587b344ee6865"],
                        "negation": True,
                    },
                    "ja4": {
                        "ja4_fingerprints": ["t13d3113h2_e8f1e7e78f70_ce5650b735ce"],
                        "negation": True,
                    },
                    "organization": {
                        "organization": "UptimeRobot s.r.o",
                        "negation": True,
                    },
                    "url": {
                        "url": "/wp-admin/",
                        "match_type": "Exact",
                        "negation": True,
                    },
                    "user_agent": {
                        "user_agent": "curl/",
                        "match_type": "Exact",
                        "negation": True,
                    },
                }
            ],
            description="description",
            request_id="210b9798eb53baa4e69d31c1071cf03d-852383",
        )
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.waap.domains.policy_overrides.with_raw_response.create(
            domain_id=1,
            enabled=True,
            name="x",
            target_ids=[1],
            target_type="detector",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_override = response.parse()
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.waap.domains.policy_overrides.with_streaming_response.create(
            domain_id=1,
            enabled=True,
            name="x",
            target_ids=[1],
            target_type="detector",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_override = response.parse()
            assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        policy_override = client.waap.domains.policy_overrides.update(
            policy_override_id=1,
            domain_id=1,
        )
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        policy_override = client.waap.domains.policy_overrides.update(
            policy_override_id=1,
            domain_id=1,
            conditions=[
                {
                    "country": {
                        "country_code": ["Mv"],
                        "negation": True,
                    },
                    "header": {
                        "header": "Origin",
                        "value": "value",
                        "match_type": "Exact",
                        "negation": True,
                    },
                    "header_exists": {
                        "header": "Origin",
                        "negation": True,
                    },
                    "http_method": {
                        "http_method": "CONNECT",
                        "negation": True,
                    },
                    "ip": {
                        "ip_address": "ip_address",
                        "negation": True,
                    },
                    "ip_range": {
                        "lower_bound": "lower_bound",
                        "upper_bound": "upper_bound",
                        "negation": True,
                    },
                    "ja3": {
                        "ja3_fingerprints": ["e7d705a3286e19ea42f587b344ee6865"],
                        "negation": True,
                    },
                    "ja4": {
                        "ja4_fingerprints": ["t13d3113h2_e8f1e7e78f70_ce5650b735ce"],
                        "negation": True,
                    },
                    "organization": {
                        "organization": "UptimeRobot s.r.o",
                        "negation": True,
                    },
                    "url": {
                        "url": "/wp-admin/",
                        "match_type": "Exact",
                        "negation": True,
                    },
                    "user_agent": {
                        "user_agent": "curl/",
                        "match_type": "Exact",
                        "negation": True,
                    },
                }
            ],
            description="description",
            enabled=True,
            name="x",
        )
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.waap.domains.policy_overrides.with_raw_response.update(
            policy_override_id=1,
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_override = response.parse()
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.waap.domains.policy_overrides.with_streaming_response.update(
            policy_override_id=1,
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_override = response.parse()
            assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        policy_override = client.waap.domains.policy_overrides.list(
            domain_id=1,
        )
        assert_matches_type(SyncOffsetPage[WaapPolicyOverride], policy_override, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        policy_override = client.waap.domains.policy_overrides.list(
            domain_id=1,
            enabled=True,
            limit=0,
            offset=0,
            ordering="id",
            search="x",
            target_type="detector",
        )
        assert_matches_type(SyncOffsetPage[WaapPolicyOverride], policy_override, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.waap.domains.policy_overrides.with_raw_response.list(
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_override = response.parse()
        assert_matches_type(SyncOffsetPage[WaapPolicyOverride], policy_override, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.waap.domains.policy_overrides.with_streaming_response.list(
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_override = response.parse()
            assert_matches_type(SyncOffsetPage[WaapPolicyOverride], policy_override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        policy_override = client.waap.domains.policy_overrides.delete(
            policy_override_id=1,
            domain_id=1,
        )
        assert policy_override is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.waap.domains.policy_overrides.with_raw_response.delete(
            policy_override_id=1,
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_override = response.parse()
        assert policy_override is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.waap.domains.policy_overrides.with_streaming_response.delete(
            policy_override_id=1,
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_override = response.parse()
            assert policy_override is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        policy_override = client.waap.domains.policy_overrides.get(
            policy_override_id=1,
            domain_id=1,
        )
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.waap.domains.policy_overrides.with_raw_response.get(
            policy_override_id=1,
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_override = response.parse()
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.waap.domains.policy_overrides.with_streaming_response.get(
            policy_override_id=1,
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_override = response.parse()
            assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_owasp_top_threats_targets(self, client: Gcore) -> None:
        policy_override = client.waap.domains.policy_overrides.list_owasp_top_threats_targets(
            domain_id=1,
        )
        assert_matches_type(SyncOffsetPage[WaapOwaspTopThreatsTarget], policy_override, path=["response"])

    @parametrize
    def test_method_list_owasp_top_threats_targets_with_all_params(self, client: Gcore) -> None:
        policy_override = client.waap.domains.policy_overrides.list_owasp_top_threats_targets(
            domain_id=1,
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[WaapOwaspTopThreatsTarget], policy_override, path=["response"])

    @parametrize
    def test_raw_response_list_owasp_top_threats_targets(self, client: Gcore) -> None:
        response = client.waap.domains.policy_overrides.with_raw_response.list_owasp_top_threats_targets(
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_override = response.parse()
        assert_matches_type(SyncOffsetPage[WaapOwaspTopThreatsTarget], policy_override, path=["response"])

    @parametrize
    def test_streaming_response_list_owasp_top_threats_targets(self, client: Gcore) -> None:
        with client.waap.domains.policy_overrides.with_streaming_response.list_owasp_top_threats_targets(
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_override = response.parse()
            assert_matches_type(SyncOffsetPage[WaapOwaspTopThreatsTarget], policy_override, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPolicyOverrides:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        policy_override = await async_client.waap.domains.policy_overrides.create(
            domain_id=1,
            enabled=True,
            name="x",
            target_ids=[1],
            target_type="detector",
        )
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        policy_override = await async_client.waap.domains.policy_overrides.create(
            domain_id=1,
            enabled=True,
            name="x",
            target_ids=[1],
            target_type="detector",
            conditions=[
                {
                    "country": {
                        "country_code": ["Mv"],
                        "negation": True,
                    },
                    "header": {
                        "header": "Origin",
                        "value": "value",
                        "match_type": "Exact",
                        "negation": True,
                    },
                    "header_exists": {
                        "header": "Origin",
                        "negation": True,
                    },
                    "http_method": {
                        "http_method": "CONNECT",
                        "negation": True,
                    },
                    "ip": {
                        "ip_address": "ip_address",
                        "negation": True,
                    },
                    "ip_range": {
                        "lower_bound": "lower_bound",
                        "upper_bound": "upper_bound",
                        "negation": True,
                    },
                    "ja3": {
                        "ja3_fingerprints": ["e7d705a3286e19ea42f587b344ee6865"],
                        "negation": True,
                    },
                    "ja4": {
                        "ja4_fingerprints": ["t13d3113h2_e8f1e7e78f70_ce5650b735ce"],
                        "negation": True,
                    },
                    "organization": {
                        "organization": "UptimeRobot s.r.o",
                        "negation": True,
                    },
                    "url": {
                        "url": "/wp-admin/",
                        "match_type": "Exact",
                        "negation": True,
                    },
                    "user_agent": {
                        "user_agent": "curl/",
                        "match_type": "Exact",
                        "negation": True,
                    },
                }
            ],
            description="description",
            request_id="210b9798eb53baa4e69d31c1071cf03d-852383",
        )
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.policy_overrides.with_raw_response.create(
            domain_id=1,
            enabled=True,
            name="x",
            target_ids=[1],
            target_type="detector",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_override = await response.parse()
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.policy_overrides.with_streaming_response.create(
            domain_id=1,
            enabled=True,
            name="x",
            target_ids=[1],
            target_type="detector",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_override = await response.parse()
            assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        policy_override = await async_client.waap.domains.policy_overrides.update(
            policy_override_id=1,
            domain_id=1,
        )
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        policy_override = await async_client.waap.domains.policy_overrides.update(
            policy_override_id=1,
            domain_id=1,
            conditions=[
                {
                    "country": {
                        "country_code": ["Mv"],
                        "negation": True,
                    },
                    "header": {
                        "header": "Origin",
                        "value": "value",
                        "match_type": "Exact",
                        "negation": True,
                    },
                    "header_exists": {
                        "header": "Origin",
                        "negation": True,
                    },
                    "http_method": {
                        "http_method": "CONNECT",
                        "negation": True,
                    },
                    "ip": {
                        "ip_address": "ip_address",
                        "negation": True,
                    },
                    "ip_range": {
                        "lower_bound": "lower_bound",
                        "upper_bound": "upper_bound",
                        "negation": True,
                    },
                    "ja3": {
                        "ja3_fingerprints": ["e7d705a3286e19ea42f587b344ee6865"],
                        "negation": True,
                    },
                    "ja4": {
                        "ja4_fingerprints": ["t13d3113h2_e8f1e7e78f70_ce5650b735ce"],
                        "negation": True,
                    },
                    "organization": {
                        "organization": "UptimeRobot s.r.o",
                        "negation": True,
                    },
                    "url": {
                        "url": "/wp-admin/",
                        "match_type": "Exact",
                        "negation": True,
                    },
                    "user_agent": {
                        "user_agent": "curl/",
                        "match_type": "Exact",
                        "negation": True,
                    },
                }
            ],
            description="description",
            enabled=True,
            name="x",
        )
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.policy_overrides.with_raw_response.update(
            policy_override_id=1,
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_override = await response.parse()
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.policy_overrides.with_streaming_response.update(
            policy_override_id=1,
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_override = await response.parse()
            assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        policy_override = await async_client.waap.domains.policy_overrides.list(
            domain_id=1,
        )
        assert_matches_type(AsyncOffsetPage[WaapPolicyOverride], policy_override, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        policy_override = await async_client.waap.domains.policy_overrides.list(
            domain_id=1,
            enabled=True,
            limit=0,
            offset=0,
            ordering="id",
            search="x",
            target_type="detector",
        )
        assert_matches_type(AsyncOffsetPage[WaapPolicyOverride], policy_override, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.policy_overrides.with_raw_response.list(
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_override = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapPolicyOverride], policy_override, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.policy_overrides.with_streaming_response.list(
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_override = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapPolicyOverride], policy_override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        policy_override = await async_client.waap.domains.policy_overrides.delete(
            policy_override_id=1,
            domain_id=1,
        )
        assert policy_override is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.policy_overrides.with_raw_response.delete(
            policy_override_id=1,
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_override = await response.parse()
        assert policy_override is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.policy_overrides.with_streaming_response.delete(
            policy_override_id=1,
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_override = await response.parse()
            assert policy_override is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        policy_override = await async_client.waap.domains.policy_overrides.get(
            policy_override_id=1,
            domain_id=1,
        )
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.policy_overrides.with_raw_response.get(
            policy_override_id=1,
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_override = await response.parse()
        assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.policy_overrides.with_streaming_response.get(
            policy_override_id=1,
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_override = await response.parse()
            assert_matches_type(WaapPolicyOverride, policy_override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_owasp_top_threats_targets(self, async_client: AsyncGcore) -> None:
        policy_override = await async_client.waap.domains.policy_overrides.list_owasp_top_threats_targets(
            domain_id=1,
        )
        assert_matches_type(AsyncOffsetPage[WaapOwaspTopThreatsTarget], policy_override, path=["response"])

    @parametrize
    async def test_method_list_owasp_top_threats_targets_with_all_params(self, async_client: AsyncGcore) -> None:
        policy_override = await async_client.waap.domains.policy_overrides.list_owasp_top_threats_targets(
            domain_id=1,
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[WaapOwaspTopThreatsTarget], policy_override, path=["response"])

    @parametrize
    async def test_raw_response_list_owasp_top_threats_targets(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.policy_overrides.with_raw_response.list_owasp_top_threats_targets(
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_override = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapOwaspTopThreatsTarget], policy_override, path=["response"])

    @parametrize
    async def test_streaming_response_list_owasp_top_threats_targets(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.policy_overrides.with_streaming_response.list_owasp_top_threats_targets(
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_override = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapOwaspTopThreatsTarget], policy_override, path=["response"])

        assert cast(Any, response.is_closed) is True

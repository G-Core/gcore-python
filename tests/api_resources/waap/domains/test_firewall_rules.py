# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.waap import WaapFirewallRule

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFirewallRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        firewall_rule = client.waap.domains.firewall_rules.create(
            domain_id=0,
            action={},
            conditions=[{}],
            enabled=True,
            name="name",
        )
        assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        firewall_rule = client.waap.domains.firewall_rules.create(
            domain_id=0,
            action={
                "allow": {},
                "block": {
                    "action_duration": "12h",
                    "status_code": 403,
                },
            },
            conditions=[
                {
                    "ip": {
                        "ip_address": "192.168.1.1",
                        "negation": True,
                    },
                    "ip_range": {
                        "lower_bound": "192.168.1.1",
                        "upper_bound": "192.168.1.1",
                        "negation": True,
                    },
                }
            ],
            enabled=True,
            name="name",
            description="description",
        )
        assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.waap.domains.firewall_rules.with_raw_response.create(
            domain_id=0,
            action={},
            conditions=[{}],
            enabled=True,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = response.parse()
        assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.waap.domains.firewall_rules.with_streaming_response.create(
            domain_id=0,
            action={},
            conditions=[{}],
            enabled=True,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = response.parse()
            assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        firewall_rule = client.waap.domains.firewall_rules.update(
            rule_id=0,
            domain_id=0,
        )
        assert firewall_rule is None

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        firewall_rule = client.waap.domains.firewall_rules.update(
            rule_id=0,
            domain_id=0,
            action={
                "allow": {},
                "block": {
                    "action_duration": "12h",
                    "status_code": 403,
                },
            },
            conditions=[
                {
                    "ip": {
                        "ip_address": "192.168.1.1",
                        "negation": True,
                    },
                    "ip_range": {
                        "lower_bound": "192.168.1.1",
                        "upper_bound": "192.168.1.1",
                        "negation": True,
                    },
                }
            ],
            description="description",
            enabled=True,
            name="name",
        )
        assert firewall_rule is None

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.waap.domains.firewall_rules.with_raw_response.update(
            rule_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = response.parse()
        assert firewall_rule is None

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.waap.domains.firewall_rules.with_streaming_response.update(
            rule_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = response.parse()
            assert firewall_rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        firewall_rule = client.waap.domains.firewall_rules.list(
            domain_id=0,
        )
        assert_matches_type(SyncOffsetPage[WaapFirewallRule], firewall_rule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        firewall_rule = client.waap.domains.firewall_rules.list(
            domain_id=0,
            action="allow",
            description="description",
            enabled=True,
            limit=0,
            name="name",
            offset=0,
            ordering="-id",
        )
        assert_matches_type(SyncOffsetPage[WaapFirewallRule], firewall_rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.waap.domains.firewall_rules.with_raw_response.list(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = response.parse()
        assert_matches_type(SyncOffsetPage[WaapFirewallRule], firewall_rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.waap.domains.firewall_rules.with_streaming_response.list(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = response.parse()
            assert_matches_type(SyncOffsetPage[WaapFirewallRule], firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        firewall_rule = client.waap.domains.firewall_rules.delete(
            rule_id=0,
            domain_id=0,
        )
        assert firewall_rule is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.waap.domains.firewall_rules.with_raw_response.delete(
            rule_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = response.parse()
        assert firewall_rule is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.waap.domains.firewall_rules.with_streaming_response.delete(
            rule_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = response.parse()
            assert firewall_rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_multiple(self, client: Gcore) -> None:
        firewall_rule = client.waap.domains.firewall_rules.delete_multiple(
            domain_id=0,
            rule_ids=[0],
        )
        assert firewall_rule is None

    @parametrize
    def test_raw_response_delete_multiple(self, client: Gcore) -> None:
        response = client.waap.domains.firewall_rules.with_raw_response.delete_multiple(
            domain_id=0,
            rule_ids=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = response.parse()
        assert firewall_rule is None

    @parametrize
    def test_streaming_response_delete_multiple(self, client: Gcore) -> None:
        with client.waap.domains.firewall_rules.with_streaming_response.delete_multiple(
            domain_id=0,
            rule_ids=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = response.parse()
            assert firewall_rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        firewall_rule = client.waap.domains.firewall_rules.get(
            rule_id=0,
            domain_id=0,
        )
        assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.waap.domains.firewall_rules.with_raw_response.get(
            rule_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = response.parse()
        assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.waap.domains.firewall_rules.with_streaming_response.get(
            rule_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = response.parse()
            assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_toggle(self, client: Gcore) -> None:
        firewall_rule = client.waap.domains.firewall_rules.toggle(
            action="enable",
            domain_id=0,
            rule_id=0,
        )
        assert firewall_rule is None

    @parametrize
    def test_raw_response_toggle(self, client: Gcore) -> None:
        response = client.waap.domains.firewall_rules.with_raw_response.toggle(
            action="enable",
            domain_id=0,
            rule_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = response.parse()
        assert firewall_rule is None

    @parametrize
    def test_streaming_response_toggle(self, client: Gcore) -> None:
        with client.waap.domains.firewall_rules.with_streaming_response.toggle(
            action="enable",
            domain_id=0,
            rule_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = response.parse()
            assert firewall_rule is None

        assert cast(Any, response.is_closed) is True


class TestAsyncFirewallRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        firewall_rule = await async_client.waap.domains.firewall_rules.create(
            domain_id=0,
            action={},
            conditions=[{}],
            enabled=True,
            name="name",
        )
        assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        firewall_rule = await async_client.waap.domains.firewall_rules.create(
            domain_id=0,
            action={
                "allow": {},
                "block": {
                    "action_duration": "12h",
                    "status_code": 403,
                },
            },
            conditions=[
                {
                    "ip": {
                        "ip_address": "192.168.1.1",
                        "negation": True,
                    },
                    "ip_range": {
                        "lower_bound": "192.168.1.1",
                        "upper_bound": "192.168.1.1",
                        "negation": True,
                    },
                }
            ],
            enabled=True,
            name="name",
            description="description",
        )
        assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.firewall_rules.with_raw_response.create(
            domain_id=0,
            action={},
            conditions=[{}],
            enabled=True,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = await response.parse()
        assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.firewall_rules.with_streaming_response.create(
            domain_id=0,
            action={},
            conditions=[{}],
            enabled=True,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = await response.parse()
            assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        firewall_rule = await async_client.waap.domains.firewall_rules.update(
            rule_id=0,
            domain_id=0,
        )
        assert firewall_rule is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        firewall_rule = await async_client.waap.domains.firewall_rules.update(
            rule_id=0,
            domain_id=0,
            action={
                "allow": {},
                "block": {
                    "action_duration": "12h",
                    "status_code": 403,
                },
            },
            conditions=[
                {
                    "ip": {
                        "ip_address": "192.168.1.1",
                        "negation": True,
                    },
                    "ip_range": {
                        "lower_bound": "192.168.1.1",
                        "upper_bound": "192.168.1.1",
                        "negation": True,
                    },
                }
            ],
            description="description",
            enabled=True,
            name="name",
        )
        assert firewall_rule is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.firewall_rules.with_raw_response.update(
            rule_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = await response.parse()
        assert firewall_rule is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.firewall_rules.with_streaming_response.update(
            rule_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = await response.parse()
            assert firewall_rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        firewall_rule = await async_client.waap.domains.firewall_rules.list(
            domain_id=0,
        )
        assert_matches_type(AsyncOffsetPage[WaapFirewallRule], firewall_rule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        firewall_rule = await async_client.waap.domains.firewall_rules.list(
            domain_id=0,
            action="allow",
            description="description",
            enabled=True,
            limit=0,
            name="name",
            offset=0,
            ordering="-id",
        )
        assert_matches_type(AsyncOffsetPage[WaapFirewallRule], firewall_rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.firewall_rules.with_raw_response.list(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapFirewallRule], firewall_rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.firewall_rules.with_streaming_response.list(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapFirewallRule], firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        firewall_rule = await async_client.waap.domains.firewall_rules.delete(
            rule_id=0,
            domain_id=0,
        )
        assert firewall_rule is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.firewall_rules.with_raw_response.delete(
            rule_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = await response.parse()
        assert firewall_rule is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.firewall_rules.with_streaming_response.delete(
            rule_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = await response.parse()
            assert firewall_rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_multiple(self, async_client: AsyncGcore) -> None:
        firewall_rule = await async_client.waap.domains.firewall_rules.delete_multiple(
            domain_id=0,
            rule_ids=[0],
        )
        assert firewall_rule is None

    @parametrize
    async def test_raw_response_delete_multiple(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.firewall_rules.with_raw_response.delete_multiple(
            domain_id=0,
            rule_ids=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = await response.parse()
        assert firewall_rule is None

    @parametrize
    async def test_streaming_response_delete_multiple(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.firewall_rules.with_streaming_response.delete_multiple(
            domain_id=0,
            rule_ids=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = await response.parse()
            assert firewall_rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        firewall_rule = await async_client.waap.domains.firewall_rules.get(
            rule_id=0,
            domain_id=0,
        )
        assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.firewall_rules.with_raw_response.get(
            rule_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = await response.parse()
        assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.firewall_rules.with_streaming_response.get(
            rule_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = await response.parse()
            assert_matches_type(WaapFirewallRule, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_toggle(self, async_client: AsyncGcore) -> None:
        firewall_rule = await async_client.waap.domains.firewall_rules.toggle(
            action="enable",
            domain_id=0,
            rule_id=0,
        )
        assert firewall_rule is None

    @parametrize
    async def test_raw_response_toggle(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.firewall_rules.with_raw_response.toggle(
            action="enable",
            domain_id=0,
            rule_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = await response.parse()
        assert firewall_rule is None

    @parametrize
    async def test_streaming_response_toggle(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.firewall_rules.with_streaming_response.toggle(
            action="enable",
            domain_id=0,
            rule_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = await response.parse()
            assert firewall_rule is None

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import SecurityGroupRule

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        rule = client.cloud.security_groups.rules.create(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SecurityGroupRule, rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        rule = client.cloud.security_groups.rules.create(
            group_id="group_id",
            project_id=0,
            region_id=0,
            description="Some description",
            direction="ingress",
            ethertype="IPv4",
            port_range_max=80,
            port_range_min=80,
            protocol="tcp",
            remote_group_id="00000000-0000-4000-8000-000000000000",
            remote_ip_prefix="10.0.0.0/8",
        )
        assert_matches_type(SecurityGroupRule, rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.security_groups.rules.with_raw_response.create(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SecurityGroupRule, rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.security_groups.rules.with_streaming_response.create(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(SecurityGroupRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.cloud.security_groups.rules.with_raw_response.create(
                group_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        rule = client.cloud.security_groups.rules.delete(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
        )
        assert rule is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.security_groups.rules.with_raw_response.delete(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert rule is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.security_groups.rules.with_streaming_response.delete(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.cloud.security_groups.rules.with_raw_response.delete(
                rule_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        rule = client.cloud.security_groups.rules.replace(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
            direction="ingress",
            security_group_id="00000000-0000-4000-8000-000000000000",
        )
        assert_matches_type(SecurityGroupRule, rule, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        rule = client.cloud.security_groups.rules.replace(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
            direction="ingress",
            security_group_id="00000000-0000-4000-8000-000000000000",
            description="Some description",
            ethertype="IPv4",
            port_range_max=80,
            port_range_min=80,
            protocol="tcp",
            remote_group_id="00000000-0000-4000-8000-000000000000",
            remote_ip_prefix="10.0.0.0/8",
        )
        assert_matches_type(SecurityGroupRule, rule, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.cloud.security_groups.rules.with_raw_response.replace(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
            direction="ingress",
            security_group_id="00000000-0000-4000-8000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SecurityGroupRule, rule, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.cloud.security_groups.rules.with_streaming_response.replace(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
            direction="ingress",
            security_group_id="00000000-0000-4000-8000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(SecurityGroupRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.cloud.security_groups.rules.with_raw_response.replace(
                rule_id="",
                project_id=0,
                region_id=0,
                direction="ingress",
                security_group_id="00000000-0000-4000-8000-000000000000",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cloud.security_groups.rules.create(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SecurityGroupRule, rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cloud.security_groups.rules.create(
            group_id="group_id",
            project_id=0,
            region_id=0,
            description="Some description",
            direction="ingress",
            ethertype="IPv4",
            port_range_max=80,
            port_range_min=80,
            protocol="tcp",
            remote_group_id="00000000-0000-4000-8000-000000000000",
            remote_ip_prefix="10.0.0.0/8",
        )
        assert_matches_type(SecurityGroupRule, rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.security_groups.rules.with_raw_response.create(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(SecurityGroupRule, rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.security_groups.rules.with_streaming_response.create(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(SecurityGroupRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.cloud.security_groups.rules.with_raw_response.create(
                group_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cloud.security_groups.rules.delete(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
        )
        assert rule is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.security_groups.rules.with_raw_response.delete(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert rule is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.security_groups.rules.with_streaming_response.delete(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.cloud.security_groups.rules.with_raw_response.delete(
                rule_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cloud.security_groups.rules.replace(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
            direction="ingress",
            security_group_id="00000000-0000-4000-8000-000000000000",
        )
        assert_matches_type(SecurityGroupRule, rule, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cloud.security_groups.rules.replace(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
            direction="ingress",
            security_group_id="00000000-0000-4000-8000-000000000000",
            description="Some description",
            ethertype="IPv4",
            port_range_max=80,
            port_range_min=80,
            protocol="tcp",
            remote_group_id="00000000-0000-4000-8000-000000000000",
            remote_ip_prefix="10.0.0.0/8",
        )
        assert_matches_type(SecurityGroupRule, rule, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.security_groups.rules.with_raw_response.replace(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
            direction="ingress",
            security_group_id="00000000-0000-4000-8000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(SecurityGroupRule, rule, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.security_groups.rules.with_streaming_response.replace(
            rule_id="rule_id",
            project_id=0,
            region_id=0,
            direction="ingress",
            security_group_id="00000000-0000-4000-8000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(SecurityGroupRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.cloud.security_groups.rules.with_raw_response.replace(
                rule_id="",
                project_id=0,
                region_id=0,
                direction="ingress",
                security_group_id="00000000-0000-4000-8000-000000000000",
            )

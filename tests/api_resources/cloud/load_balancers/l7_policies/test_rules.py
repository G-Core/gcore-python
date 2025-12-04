# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import TaskIDList, LoadBalancerL7Rule, LoadBalancerL7RuleList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        rule = client.cloud.load_balancers.l7_policies.rules.create(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            compare_type="REGEX",
            type="PATH",
            value="/images*",
        )
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        rule = client.cloud.load_balancers.l7_policies.rules.create(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            compare_type="REGEX",
            type="PATH",
            value="/images*",
            invert=True,
            key="the name of the cookie or header to evaluate.",
            tags=["test_tag_1", "test_tag_2"],
        )
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.rules.with_raw_response.create(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            compare_type="REGEX",
            type="PATH",
            value="/images*",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.rules.with_streaming_response.create(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            compare_type="REGEX",
            type="PATH",
            value="/images*",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(TaskIDList, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.rules.with_raw_response.create(
                l7policy_id="",
                project_id=1,
                region_id=1,
                compare_type="REGEX",
                type="PATH",
                value="/images*",
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        rule = client.cloud.load_balancers.l7_policies.rules.list(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerL7RuleList, rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.rules.with_raw_response.list(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(LoadBalancerL7RuleList, rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.rules.with_streaming_response.list(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(LoadBalancerL7RuleList, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.rules.with_raw_response.list(
                l7policy_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        rule = client.cloud.load_balancers.l7_policies.rules.delete(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.rules.with_raw_response.delete(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.rules.with_streaming_response.delete(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(TaskIDList, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.rules.with_raw_response.delete(
                l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
                project_id=1,
                region_id=1,
                l7policy_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7rule_id` but received ''"):
            client.cloud.load_balancers.l7_policies.rules.with_raw_response.delete(
                l7rule_id="",
                project_id=1,
                region_id=1,
                l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        rule = client.cloud.load_balancers.l7_policies.rules.get(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )
        assert_matches_type(LoadBalancerL7Rule, rule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.rules.with_raw_response.get(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(LoadBalancerL7Rule, rule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.rules.with_streaming_response.get(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(LoadBalancerL7Rule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.rules.with_raw_response.get(
                l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
                project_id=1,
                region_id=1,
                l7policy_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7rule_id` but received ''"):
            client.cloud.load_balancers.l7_policies.rules.with_raw_response.get(
                l7rule_id="",
                project_id=1,
                region_id=1,
                l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            )

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        rule = client.cloud.load_balancers.l7_policies.rules.replace(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            compare_type="REGEX",
        )
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        rule = client.cloud.load_balancers.l7_policies.rules.replace(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            compare_type="REGEX",
            invert=True,
            key="the name of the cookie or header to evaluate.",
            tags=["test_tag_1", "test_tag_2"],
            type="PATH",
            value="/images*",
        )
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.rules.with_raw_response.replace(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            compare_type="REGEX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.rules.with_streaming_response.replace(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            compare_type="REGEX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(TaskIDList, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.rules.with_raw_response.replace(
                l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
                project_id=1,
                region_id=1,
                l7policy_id="",
                compare_type="REGEX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7rule_id` but received ''"):
            client.cloud.load_balancers.l7_policies.rules.with_raw_response.replace(
                l7rule_id="",
                project_id=1,
                region_id=1,
                l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
                compare_type="REGEX",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cloud.load_balancers.l7_policies.rules.create(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            compare_type="REGEX",
            type="PATH",
            value="/images*",
        )
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cloud.load_balancers.l7_policies.rules.create(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            compare_type="REGEX",
            type="PATH",
            value="/images*",
            invert=True,
            key="the name of the cookie or header to evaluate.",
            tags=["test_tag_1", "test_tag_2"],
        )
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.rules.with_raw_response.create(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            compare_type="REGEX",
            type="PATH",
            value="/images*",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.rules.with_streaming_response.create(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            compare_type="REGEX",
            type="PATH",
            value="/images*",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(TaskIDList, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.rules.with_raw_response.create(
                l7policy_id="",
                project_id=1,
                region_id=1,
                compare_type="REGEX",
                type="PATH",
                value="/images*",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cloud.load_balancers.l7_policies.rules.list(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerL7RuleList, rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.rules.with_raw_response.list(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(LoadBalancerL7RuleList, rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.rules.with_streaming_response.list(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(LoadBalancerL7RuleList, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.rules.with_raw_response.list(
                l7policy_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cloud.load_balancers.l7_policies.rules.delete(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.rules.with_raw_response.delete(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.rules.with_streaming_response.delete(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(TaskIDList, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.rules.with_raw_response.delete(
                l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
                project_id=1,
                region_id=1,
                l7policy_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7rule_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.rules.with_raw_response.delete(
                l7rule_id="",
                project_id=1,
                region_id=1,
                l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cloud.load_balancers.l7_policies.rules.get(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )
        assert_matches_type(LoadBalancerL7Rule, rule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.rules.with_raw_response.get(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(LoadBalancerL7Rule, rule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.rules.with_streaming_response.get(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(LoadBalancerL7Rule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.rules.with_raw_response.get(
                l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
                project_id=1,
                region_id=1,
                l7policy_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7rule_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.rules.with_raw_response.get(
                l7rule_id="",
                project_id=1,
                region_id=1,
                l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cloud.load_balancers.l7_policies.rules.replace(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            compare_type="REGEX",
        )
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cloud.load_balancers.l7_policies.rules.replace(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            compare_type="REGEX",
            invert=True,
            key="the name of the cookie or header to evaluate.",
            tags=["test_tag_1", "test_tag_2"],
            type="PATH",
            value="/images*",
        )
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.rules.with_raw_response.replace(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            compare_type="REGEX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(TaskIDList, rule, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.rules.with_streaming_response.replace(
            l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            compare_type="REGEX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(TaskIDList, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.rules.with_raw_response.replace(
                l7rule_id="023f2e34-7806-443b-bfae-16c324569a3d",
                project_id=1,
                region_id=1,
                l7policy_id="",
                compare_type="REGEX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7rule_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.rules.with_raw_response.replace(
                l7rule_id="",
                project_id=1,
                region_id=1,
                l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
                compare_type="REGEX",
            )

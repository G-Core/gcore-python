# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import TaskIDList, LoadBalancerL7Policy, LoadBalancerL7PolicyList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestL7Policies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.create(
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.create(
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            name="redirect-example.com",
            position=1,
            redirect_http_code=301,
            redirect_pool_id="redirect_pool_id",
            redirect_prefix="redirect_prefix",
            redirect_url="http://www.example.com",
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.create(
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.create(
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(LoadBalancerL7PolicyList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(LoadBalancerL7PolicyList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(LoadBalancerL7PolicyList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.delete(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.delete(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.delete(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.with_raw_response.delete(
                l7policy_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.get(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(LoadBalancerL7Policy, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.get(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(LoadBalancerL7Policy, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.get(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(LoadBalancerL7Policy, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.with_raw_response.get(
                l7policy_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.replace(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.replace(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
            name="redirect-images.example.com",
            position=1,
            redirect_http_code=301,
            redirect_pool_id="redirect_pool_id",
            redirect_prefix="redirect_prefix",
            redirect_url="http://images.example.com",
            tags=["updated_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.replace(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.replace(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.with_raw_response.replace(
                l7policy_id="",
                project_id=0,
                region_id=0,
                action="REDIRECT_TO_URL",
            )


class TestAsyncL7Policies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.create(
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.create(
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            name="redirect-example.com",
            position=1,
            redirect_http_code=301,
            redirect_pool_id="redirect_pool_id",
            redirect_prefix="redirect_prefix",
            redirect_url="http://www.example.com",
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.create(
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.create(
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(LoadBalancerL7PolicyList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(LoadBalancerL7PolicyList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(LoadBalancerL7PolicyList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.delete(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.delete(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.delete(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.with_raw_response.delete(
                l7policy_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.get(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(LoadBalancerL7Policy, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.get(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(LoadBalancerL7Policy, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.get(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(LoadBalancerL7Policy, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.with_raw_response.get(
                l7policy_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.replace(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.replace(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
            name="redirect-images.example.com",
            position=1,
            redirect_http_code=301,
            redirect_pool_id="redirect_pool_id",
            redirect_prefix="redirect_prefix",
            redirect_url="http://images.example.com",
            tags=["updated_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.replace(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.replace(
            l7policy_id="l7policy_id",
            project_id=0,
            region_id=0,
            action="REDIRECT_TO_URL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.with_raw_response.replace(
                l7policy_id="",
                project_id=0,
                region_id=0,
                action="REDIRECT_TO_URL",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import (
    LifecyclePolicy,
    LifecyclePolicyListResponse,
    LifecyclePolicyEstimateMaxUsageResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLifecyclePolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        lifecycle_policy = client.cloud.lifecycle_policies.create(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        lifecycle_policy = client.cloud.lifecycle_policies.create(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
            schedules=[
                {
                    "type": "cron",
                    "day": "5",
                    "day_of_week": "fri",
                    "hour": "0, 20",
                    "max_quantity": 2,
                    "minute": "30",
                    "month": "1",
                    "resource_name_template": "snapshot of volume {volume_id}",
                    "retention_time": {
                        "days": 0,
                        "hours": 2,
                        "minutes": 1,
                        "weeks": 0,
                    },
                    "timezone": "UTC",
                    "week": "1",
                }
            ],
            status="active",
            volume_ids=["3ed9e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.lifecycle_policies.with_raw_response.create(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.lifecycle_policies.with_streaming_response.create(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        lifecycle_policy = client.cloud.lifecycle_policies.update(
            policy_id=1,
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        lifecycle_policy = client.cloud.lifecycle_policies.update(
            policy_id=1,
            project_id=1,
            region_id=1,
            name="schedule_1",
            status="paused",
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.lifecycle_policies.with_raw_response.update(
            policy_id=1,
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.lifecycle_policies.with_streaming_response.update(
            policy_id=1,
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        lifecycle_policy = client.cloud.lifecycle_policies.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LifecyclePolicyListResponse, lifecycle_policy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.lifecycle_policies.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = response.parse()
        assert_matches_type(LifecyclePolicyListResponse, lifecycle_policy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.lifecycle_policies.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = response.parse()
            assert_matches_type(LifecyclePolicyListResponse, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        lifecycle_policy = client.cloud.lifecycle_policies.delete(
            policy_id=1,
            project_id=1,
            region_id=1,
        )
        assert lifecycle_policy is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.lifecycle_policies.with_raw_response.delete(
            policy_id=1,
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = response.parse()
        assert lifecycle_policy is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.lifecycle_policies.with_streaming_response.delete(
            policy_id=1,
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = response.parse()
            assert lifecycle_policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_schedules(self, client: Gcore) -> None:
        lifecycle_policy = client.cloud.lifecycle_policies.add_schedules(
            policy_id=1,
            project_id=1,
            region_id=1,
            schedules=[{"type": "cron"}, {"type": "interval"}],
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_raw_response_add_schedules(self, client: Gcore) -> None:
        response = client.cloud.lifecycle_policies.with_raw_response.add_schedules(
            policy_id=1,
            project_id=1,
            region_id=1,
            schedules=[{"type": "cron"}, {"type": "interval"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_streaming_response_add_schedules(self, client: Gcore) -> None:
        with client.cloud.lifecycle_policies.with_streaming_response.add_schedules(
            policy_id=1,
            project_id=1,
            region_id=1,
            schedules=[{"type": "cron"}, {"type": "interval"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_volumes(self, client: Gcore) -> None:
        lifecycle_policy = client.cloud.lifecycle_policies.add_volumes(
            policy_id=1,
            project_id=1,
            region_id=1,
            volume_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_raw_response_add_volumes(self, client: Gcore) -> None:
        response = client.cloud.lifecycle_policies.with_raw_response.add_volumes(
            policy_id=1,
            project_id=1,
            region_id=1,
            volume_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_streaming_response_add_volumes(self, client: Gcore) -> None:
        with client.cloud.lifecycle_policies.with_streaming_response.add_volumes(
            policy_id=1,
            project_id=1,
            region_id=1,
            volume_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_estimate_max_usage(self, client: Gcore) -> None:
        lifecycle_policy = client.cloud.lifecycle_policies.estimate_max_usage(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
        )
        assert_matches_type(LifecyclePolicyEstimateMaxUsageResponse, lifecycle_policy, path=["response"])

    @parametrize
    def test_method_estimate_max_usage_with_all_params(self, client: Gcore) -> None:
        lifecycle_policy = client.cloud.lifecycle_policies.estimate_max_usage(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
            schedules=[
                {
                    "type": "cron",
                    "day": "5",
                    "day_of_week": "fri",
                    "hour": "0, 20",
                    "max_quantity": 2,
                    "minute": "30",
                    "month": "1",
                    "resource_name_template": "snapshot of volume {volume_id}",
                    "retention_time": {
                        "days": 0,
                        "hours": 2,
                        "minutes": 1,
                        "weeks": 0,
                    },
                    "timezone": "UTC",
                    "week": "1",
                }
            ],
            status="active",
            volume_ids=["3ed9e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )
        assert_matches_type(LifecyclePolicyEstimateMaxUsageResponse, lifecycle_policy, path=["response"])

    @parametrize
    def test_raw_response_estimate_max_usage(self, client: Gcore) -> None:
        response = client.cloud.lifecycle_policies.with_raw_response.estimate_max_usage(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = response.parse()
        assert_matches_type(LifecyclePolicyEstimateMaxUsageResponse, lifecycle_policy, path=["response"])

    @parametrize
    def test_streaming_response_estimate_max_usage(self, client: Gcore) -> None:
        with client.cloud.lifecycle_policies.with_streaming_response.estimate_max_usage(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = response.parse()
            assert_matches_type(LifecyclePolicyEstimateMaxUsageResponse, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        lifecycle_policy = client.cloud.lifecycle_policies.get(
            policy_id=1,
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.lifecycle_policies.with_raw_response.get(
            policy_id=1,
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.lifecycle_policies.with_streaming_response.get(
            policy_id=1,
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove_schedules(self, client: Gcore) -> None:
        lifecycle_policy = client.cloud.lifecycle_policies.remove_schedules(
            policy_id=1,
            project_id=1,
            region_id=1,
            schedule_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_raw_response_remove_schedules(self, client: Gcore) -> None:
        response = client.cloud.lifecycle_policies.with_raw_response.remove_schedules(
            policy_id=1,
            project_id=1,
            region_id=1,
            schedule_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_streaming_response_remove_schedules(self, client: Gcore) -> None:
        with client.cloud.lifecycle_policies.with_streaming_response.remove_schedules(
            policy_id=1,
            project_id=1,
            region_id=1,
            schedule_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove_volumes(self, client: Gcore) -> None:
        lifecycle_policy = client.cloud.lifecycle_policies.remove_volumes(
            policy_id=1,
            project_id=1,
            region_id=1,
            volume_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_raw_response_remove_volumes(self, client: Gcore) -> None:
        response = client.cloud.lifecycle_policies.with_raw_response.remove_volumes(
            policy_id=1,
            project_id=1,
            region_id=1,
            volume_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    def test_streaming_response_remove_volumes(self, client: Gcore) -> None:
        with client.cloud.lifecycle_policies.with_streaming_response.remove_volumes(
            policy_id=1,
            project_id=1,
            region_id=1,
            volume_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLifecyclePolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        lifecycle_policy = await async_client.cloud.lifecycle_policies.create(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        lifecycle_policy = await async_client.cloud.lifecycle_policies.create(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
            schedules=[
                {
                    "type": "cron",
                    "day": "5",
                    "day_of_week": "fri",
                    "hour": "0, 20",
                    "max_quantity": 2,
                    "minute": "30",
                    "month": "1",
                    "resource_name_template": "snapshot of volume {volume_id}",
                    "retention_time": {
                        "days": 0,
                        "hours": 2,
                        "minutes": 1,
                        "weeks": 0,
                    },
                    "timezone": "UTC",
                    "week": "1",
                }
            ],
            status="active",
            volume_ids=["3ed9e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.lifecycle_policies.with_raw_response.create(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = await response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.lifecycle_policies.with_streaming_response.create(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = await response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        lifecycle_policy = await async_client.cloud.lifecycle_policies.update(
            policy_id=1,
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        lifecycle_policy = await async_client.cloud.lifecycle_policies.update(
            policy_id=1,
            project_id=1,
            region_id=1,
            name="schedule_1",
            status="paused",
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.lifecycle_policies.with_raw_response.update(
            policy_id=1,
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = await response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.lifecycle_policies.with_streaming_response.update(
            policy_id=1,
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = await response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        lifecycle_policy = await async_client.cloud.lifecycle_policies.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LifecyclePolicyListResponse, lifecycle_policy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.lifecycle_policies.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = await response.parse()
        assert_matches_type(LifecyclePolicyListResponse, lifecycle_policy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.lifecycle_policies.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = await response.parse()
            assert_matches_type(LifecyclePolicyListResponse, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        lifecycle_policy = await async_client.cloud.lifecycle_policies.delete(
            policy_id=1,
            project_id=1,
            region_id=1,
        )
        assert lifecycle_policy is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.lifecycle_policies.with_raw_response.delete(
            policy_id=1,
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = await response.parse()
        assert lifecycle_policy is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.lifecycle_policies.with_streaming_response.delete(
            policy_id=1,
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = await response.parse()
            assert lifecycle_policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_schedules(self, async_client: AsyncGcore) -> None:
        lifecycle_policy = await async_client.cloud.lifecycle_policies.add_schedules(
            policy_id=1,
            project_id=1,
            region_id=1,
            schedules=[{"type": "cron"}, {"type": "interval"}],
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_raw_response_add_schedules(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.lifecycle_policies.with_raw_response.add_schedules(
            policy_id=1,
            project_id=1,
            region_id=1,
            schedules=[{"type": "cron"}, {"type": "interval"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = await response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_streaming_response_add_schedules(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.lifecycle_policies.with_streaming_response.add_schedules(
            policy_id=1,
            project_id=1,
            region_id=1,
            schedules=[{"type": "cron"}, {"type": "interval"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = await response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_volumes(self, async_client: AsyncGcore) -> None:
        lifecycle_policy = await async_client.cloud.lifecycle_policies.add_volumes(
            policy_id=1,
            project_id=1,
            region_id=1,
            volume_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_raw_response_add_volumes(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.lifecycle_policies.with_raw_response.add_volumes(
            policy_id=1,
            project_id=1,
            region_id=1,
            volume_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = await response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_streaming_response_add_volumes(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.lifecycle_policies.with_streaming_response.add_volumes(
            policy_id=1,
            project_id=1,
            region_id=1,
            volume_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = await response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_estimate_max_usage(self, async_client: AsyncGcore) -> None:
        lifecycle_policy = await async_client.cloud.lifecycle_policies.estimate_max_usage(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
        )
        assert_matches_type(LifecyclePolicyEstimateMaxUsageResponse, lifecycle_policy, path=["response"])

    @parametrize
    async def test_method_estimate_max_usage_with_all_params(self, async_client: AsyncGcore) -> None:
        lifecycle_policy = await async_client.cloud.lifecycle_policies.estimate_max_usage(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
            schedules=[
                {
                    "type": "cron",
                    "day": "5",
                    "day_of_week": "fri",
                    "hour": "0, 20",
                    "max_quantity": 2,
                    "minute": "30",
                    "month": "1",
                    "resource_name_template": "snapshot of volume {volume_id}",
                    "retention_time": {
                        "days": 0,
                        "hours": 2,
                        "minutes": 1,
                        "weeks": 0,
                    },
                    "timezone": "UTC",
                    "week": "1",
                }
            ],
            status="active",
            volume_ids=["3ed9e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )
        assert_matches_type(LifecyclePolicyEstimateMaxUsageResponse, lifecycle_policy, path=["response"])

    @parametrize
    async def test_raw_response_estimate_max_usage(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.lifecycle_policies.with_raw_response.estimate_max_usage(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = await response.parse()
        assert_matches_type(LifecyclePolicyEstimateMaxUsageResponse, lifecycle_policy, path=["response"])

    @parametrize
    async def test_streaming_response_estimate_max_usage(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.lifecycle_policies.with_streaming_response.estimate_max_usage(
            project_id=1,
            region_id=1,
            action="volume_snapshot",
            name="schedule_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = await response.parse()
            assert_matches_type(LifecyclePolicyEstimateMaxUsageResponse, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        lifecycle_policy = await async_client.cloud.lifecycle_policies.get(
            policy_id=1,
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.lifecycle_policies.with_raw_response.get(
            policy_id=1,
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = await response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.lifecycle_policies.with_streaming_response.get(
            policy_id=1,
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = await response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove_schedules(self, async_client: AsyncGcore) -> None:
        lifecycle_policy = await async_client.cloud.lifecycle_policies.remove_schedules(
            policy_id=1,
            project_id=1,
            region_id=1,
            schedule_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_raw_response_remove_schedules(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.lifecycle_policies.with_raw_response.remove_schedules(
            policy_id=1,
            project_id=1,
            region_id=1,
            schedule_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = await response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_streaming_response_remove_schedules(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.lifecycle_policies.with_streaming_response.remove_schedules(
            policy_id=1,
            project_id=1,
            region_id=1,
            schedule_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = await response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove_volumes(self, async_client: AsyncGcore) -> None:
        lifecycle_policy = await async_client.cloud.lifecycle_policies.remove_volumes(
            policy_id=1,
            project_id=1,
            region_id=1,
            volume_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_raw_response_remove_volumes(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.lifecycle_policies.with_raw_response.remove_volumes(
            policy_id=1,
            project_id=1,
            region_id=1,
            volume_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lifecycle_policy = await response.parse()
        assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

    @parametrize
    async def test_streaming_response_remove_volumes(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.lifecycle_policies.with_streaming_response.remove_volumes(
            policy_id=1,
            project_id=1,
            region_id=1,
            volume_ids=["1488e2ce-f906-47fb-ba32-c25a3f63df4f"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lifecycle_policy = await response.parse()
            assert_matches_type(LifecyclePolicy, lifecycle_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

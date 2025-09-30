# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn.logs_uploader import (
    LogsUploaderPolicy,
    LogsUploaderPolicyList,
    PolicyListFieldsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        policy = client.cdn.logs_uploader.policies.create()
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        policy = client.cdn.logs_uploader.policies.create(
            date_format="[02/Jan/2006:15:04:05 -0700]",
            description="New policy",
            field_delimiter=",",
            field_separator=";",
            fields=["remote_addr", "status"],
            file_name_template="{{YYYY}}_{{MM}}_{{DD}}_{{HH}}_{{mm}}_{{ss}}_access.log.gz",
            format_type="flvproxy",
            include_empty_logs=True,
            include_shield_logs=True,
            name="Policy",
            retry_interval_minutes=32,
            rotate_interval_minutes=32,
            rotate_threshold_lines=5000,
            rotate_threshold_mb=252,
            tags={},
        )
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.policies.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.policies.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        policy = client.cdn.logs_uploader.policies.update(
            id=0,
        )
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        policy = client.cdn.logs_uploader.policies.update(
            id=0,
            date_format="[02/Jan/2006:15:04:05 -0700]",
            description="New policy",
            field_delimiter=",",
            field_separator=";",
            fields=["remote_addr", "status"],
            file_name_template="{{YYYY}}_{{MM}}_{{DD}}_{{HH}}_{{mm}}_{{ss}}_access.log.gz",
            format_type="flvproxy",
            include_empty_logs=True,
            include_shield_logs=True,
            name="Policy",
            retry_interval_minutes=32,
            rotate_interval_minutes=32,
            rotate_threshold_lines=5000,
            rotate_threshold_mb=252,
            tags={},
        )
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.policies.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.policies.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        policy = client.cdn.logs_uploader.policies.list()
        assert_matches_type(LogsUploaderPolicyList, policy, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        policy = client.cdn.logs_uploader.policies.list(
            config_ids=[0],
            search="search",
        )
        assert_matches_type(LogsUploaderPolicyList, policy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(LogsUploaderPolicyList, policy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(LogsUploaderPolicyList, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        policy = client.cdn.logs_uploader.policies.delete(
            0,
        )
        assert policy is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.policies.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert policy is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.policies.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        policy = client.cdn.logs_uploader.policies.get(
            0,
        )
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.policies.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.policies.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_fields(self, client: Gcore) -> None:
        policy = client.cdn.logs_uploader.policies.list_fields()
        assert_matches_type(PolicyListFieldsResponse, policy, path=["response"])

    @parametrize
    def test_raw_response_list_fields(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.policies.with_raw_response.list_fields()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(PolicyListFieldsResponse, policy, path=["response"])

    @parametrize
    def test_streaming_response_list_fields(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.policies.with_streaming_response.list_fields() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(PolicyListFieldsResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        policy = client.cdn.logs_uploader.policies.replace(
            id=0,
        )
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        policy = client.cdn.logs_uploader.policies.replace(
            id=0,
            date_format="[02/Jan/2006:15:04:05 -0700]",
            description="New policy",
            field_delimiter=",",
            field_separator=";",
            fields=["remote_addr", "status"],
            file_name_template="{{YYYY}}_{{MM}}_{{DD}}_{{HH}}_{{mm}}_{{ss}}_access.log.gz",
            format_type="flvproxy",
            include_empty_logs=True,
            include_shield_logs=True,
            name="Policy",
            retry_interval_minutes=32,
            rotate_interval_minutes=32,
            rotate_threshold_lines=5000,
            rotate_threshold_mb=252,
            tags={},
        )
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.cdn.logs_uploader.policies.with_raw_response.replace(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.cdn.logs_uploader.policies.with_streaming_response.replace(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        policy = await async_client.cdn.logs_uploader.policies.create()
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        policy = await async_client.cdn.logs_uploader.policies.create(
            date_format="[02/Jan/2006:15:04:05 -0700]",
            description="New policy",
            field_delimiter=",",
            field_separator=";",
            fields=["remote_addr", "status"],
            file_name_template="{{YYYY}}_{{MM}}_{{DD}}_{{HH}}_{{mm}}_{{ss}}_access.log.gz",
            format_type="flvproxy",
            include_empty_logs=True,
            include_shield_logs=True,
            name="Policy",
            retry_interval_minutes=32,
            rotate_interval_minutes=32,
            rotate_threshold_lines=5000,
            rotate_threshold_mb=252,
            tags={},
        )
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.policies.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.policies.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        policy = await async_client.cdn.logs_uploader.policies.update(
            id=0,
        )
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        policy = await async_client.cdn.logs_uploader.policies.update(
            id=0,
            date_format="[02/Jan/2006:15:04:05 -0700]",
            description="New policy",
            field_delimiter=",",
            field_separator=";",
            fields=["remote_addr", "status"],
            file_name_template="{{YYYY}}_{{MM}}_{{DD}}_{{HH}}_{{mm}}_{{ss}}_access.log.gz",
            format_type="flvproxy",
            include_empty_logs=True,
            include_shield_logs=True,
            name="Policy",
            retry_interval_minutes=32,
            rotate_interval_minutes=32,
            rotate_threshold_lines=5000,
            rotate_threshold_mb=252,
            tags={},
        )
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.policies.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.policies.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        policy = await async_client.cdn.logs_uploader.policies.list()
        assert_matches_type(LogsUploaderPolicyList, policy, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        policy = await async_client.cdn.logs_uploader.policies.list(
            config_ids=[0],
            search="search",
        )
        assert_matches_type(LogsUploaderPolicyList, policy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(LogsUploaderPolicyList, policy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(LogsUploaderPolicyList, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        policy = await async_client.cdn.logs_uploader.policies.delete(
            0,
        )
        assert policy is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.policies.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert policy is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.policies.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        policy = await async_client.cdn.logs_uploader.policies.get(
            0,
        )
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.policies.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.policies.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_fields(self, async_client: AsyncGcore) -> None:
        policy = await async_client.cdn.logs_uploader.policies.list_fields()
        assert_matches_type(PolicyListFieldsResponse, policy, path=["response"])

    @parametrize
    async def test_raw_response_list_fields(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.policies.with_raw_response.list_fields()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(PolicyListFieldsResponse, policy, path=["response"])

    @parametrize
    async def test_streaming_response_list_fields(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.policies.with_streaming_response.list_fields() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(PolicyListFieldsResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        policy = await async_client.cdn.logs_uploader.policies.replace(
            id=0,
        )
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        policy = await async_client.cdn.logs_uploader.policies.replace(
            id=0,
            date_format="[02/Jan/2006:15:04:05 -0700]",
            description="New policy",
            field_delimiter=",",
            field_separator=";",
            fields=["remote_addr", "status"],
            file_name_template="{{YYYY}}_{{MM}}_{{DD}}_{{HH}}_{{mm}}_{{ss}}_access.log.gz",
            format_type="flvproxy",
            include_empty_logs=True,
            include_shield_logs=True,
            name="Policy",
            retry_interval_minutes=32,
            rotate_interval_minutes=32,
            rotate_threshold_lines=5000,
            rotate_threshold_mb=252,
            tags={},
        )
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs_uploader.policies.with_raw_response.replace(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs_uploader.policies.with_streaming_response.replace(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(LogsUploaderPolicy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

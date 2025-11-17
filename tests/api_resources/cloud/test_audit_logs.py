# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import AuditLogEntry

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        audit_log = client.cloud.audit_logs.list()
        assert_matches_type(SyncOffsetPage[AuditLogEntry], audit_log, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        audit_log = client.cloud.audit_logs.list(
            action_type=["activate", "delete"],
            api_group=["ai_cluster", "image"],
            from_timestamp=parse_datetime("2019-11-14T10:30:32Z"),
            limit=1000,
            offset=0,
            order_by="asc",
            project_id=[1, 2, 3],
            region_id=[1, 2, 3],
            resource_id=["string"],
            search_field="default",
            sorting="asc",
            source_user_ips=["203.0.113.42", "192.168.1.100"],
            to_timestamp=parse_datetime("2019-11-14T10:30:32Z"),
            user_agents=["Mozilla/5.0", "MyApp/1.0.0"],
        )
        assert_matches_type(SyncOffsetPage[AuditLogEntry], audit_log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.audit_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(SyncOffsetPage[AuditLogEntry], audit_log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.audit_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(SyncOffsetPage[AuditLogEntry], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuditLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        audit_log = await async_client.cloud.audit_logs.list()
        assert_matches_type(AsyncOffsetPage[AuditLogEntry], audit_log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        audit_log = await async_client.cloud.audit_logs.list(
            action_type=["activate", "delete"],
            api_group=["ai_cluster", "image"],
            from_timestamp=parse_datetime("2019-11-14T10:30:32Z"),
            limit=1000,
            offset=0,
            order_by="asc",
            project_id=[1, 2, 3],
            region_id=[1, 2, 3],
            resource_id=["string"],
            search_field="default",
            sorting="asc",
            source_user_ips=["203.0.113.42", "192.168.1.100"],
            to_timestamp=parse_datetime("2019-11-14T10:30:32Z"),
            user_agents=["Mozilla/5.0", "MyApp/1.0.0"],
        )
        assert_matches_type(AsyncOffsetPage[AuditLogEntry], audit_log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.audit_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(AsyncOffsetPage[AuditLogEntry], audit_log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.audit_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(AsyncOffsetPage[AuditLogEntry], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

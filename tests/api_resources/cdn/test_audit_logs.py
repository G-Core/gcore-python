# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn import CdnAuditLogEntry
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        audit_log = client.cdn.audit_logs.list()
        assert_matches_type(SyncOffsetPage[CdnAuditLogEntry], audit_log, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        audit_log = client.cdn.audit_logs.list(
            client_id=0,
            limit=0,
            max_requested_at="max_requested_at",
            method="method",
            min_requested_at="min_requested_at",
            offset=0,
            path="path",
            remote_ip_address="remote_ip_address",
            status_code=0,
            token_id=0,
            user_id=0,
        )
        assert_matches_type(SyncOffsetPage[CdnAuditLogEntry], audit_log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.audit_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(SyncOffsetPage[CdnAuditLogEntry], audit_log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.audit_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(SyncOffsetPage[CdnAuditLogEntry], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        audit_log = client.cdn.audit_logs.get(
            0,
        )
        assert_matches_type(CdnAuditLogEntry, audit_log, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cdn.audit_logs.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(CdnAuditLogEntry, audit_log, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cdn.audit_logs.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(CdnAuditLogEntry, audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuditLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        audit_log = await async_client.cdn.audit_logs.list()
        assert_matches_type(AsyncOffsetPage[CdnAuditLogEntry], audit_log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        audit_log = await async_client.cdn.audit_logs.list(
            client_id=0,
            limit=0,
            max_requested_at="max_requested_at",
            method="method",
            min_requested_at="min_requested_at",
            offset=0,
            path="path",
            remote_ip_address="remote_ip_address",
            status_code=0,
            token_id=0,
            user_id=0,
        )
        assert_matches_type(AsyncOffsetPage[CdnAuditLogEntry], audit_log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.audit_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(AsyncOffsetPage[CdnAuditLogEntry], audit_log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.audit_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(AsyncOffsetPage[CdnAuditLogEntry], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        audit_log = await async_client.cdn.audit_logs.get(
            0,
        )
        assert_matches_type(CdnAuditLogEntry, audit_log, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.audit_logs.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(CdnAuditLogEntry, audit_log, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.audit_logs.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(CdnAuditLogEntry, audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

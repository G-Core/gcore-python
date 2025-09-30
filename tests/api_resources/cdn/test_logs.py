# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from gcore.pagination import SyncOffsetPageCdnLogs, AsyncOffsetPageCdnLogs
from gcore.types.cdn.cdn_log_entry import Data

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        log = client.cdn.logs.list(
            from_="from",
            to="to",
        )
        assert_matches_type(SyncOffsetPageCdnLogs[Data], log, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        log = client.cdn.logs.list(
            from_="from",
            to="to",
            cache_status_eq="cache_status__eq",
            cache_status_in="cache_status__in",
            cache_status_ne="cache_status__ne",
            cache_status_not_in="cache_status__not_in",
            client_ip_eq="client_ip__eq",
            client_ip_in="client_ip__in",
            client_ip_ne="client_ip__ne",
            client_ip_not_in="client_ip__not_in",
            cname_contains="cname__contains",
            cname_eq="cname__eq",
            cname_in="cname__in",
            cname_ne="cname__ne",
            cname_not_in="cname__not_in",
            datacenter_eq="datacenter__eq",
            datacenter_in="datacenter__in",
            datacenter_ne="datacenter__ne",
            datacenter_not_in="datacenter__not_in",
            fields="fields",
            limit=1,
            method_eq="method__eq",
            method_in="method__in",
            method_ne="method__ne",
            method_not_in="method__not_in",
            offset=0,
            ordering="ordering",
            resource_id_eq=0,
            resource_id_gt=0,
            resource_id_gte=0,
            resource_id_in="resource_id__in",
            resource_id_lt=0,
            resource_id_lte=0,
            resource_id_ne=0,
            resource_id_not_in="resource_id__not_in",
            size_eq=0,
            size_gt=0,
            size_gte=0,
            size_in="size__in",
            size_lt=0,
            size_lte=0,
            size_ne=0,
            size_not_in="size__not_in",
            status_eq=0,
            status_gt=0,
            status_gte=0,
            status_in="status__in",
            status_lt=0,
            status_lte=0,
            status_ne=0,
            status_not_in="status__not_in",
        )
        assert_matches_type(SyncOffsetPageCdnLogs[Data], log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.logs.with_raw_response.list(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(SyncOffsetPageCdnLogs[Data], log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.logs.with_streaming_response.list(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(SyncOffsetPageCdnLogs[Data], log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Gcore, respx_mock: MockRouter) -> None:
        respx_mock.get("/cdn/advanced/v1/logs/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        log = client.cdn.logs.download(
            format="format",
            from_="from",
            to="to",
        )
        assert log.is_closed
        assert log.json() == {"foo": "bar"}
        assert cast(Any, log.is_closed) is True
        assert isinstance(log, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_with_all_params(self, client: Gcore, respx_mock: MockRouter) -> None:
        respx_mock.get("/cdn/advanced/v1/logs/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        log = client.cdn.logs.download(
            format="format",
            from_="from",
            to="to",
            cache_status_eq="cache_status__eq",
            cache_status_in="cache_status__in",
            cache_status_ne="cache_status__ne",
            cache_status_not_in="cache_status__not_in",
            client_ip_eq="client_ip__eq",
            client_ip_in="client_ip__in",
            client_ip_ne="client_ip__ne",
            client_ip_not_in="client_ip__not_in",
            cname_contains="cname__contains",
            cname_eq="cname__eq",
            cname_in="cname__in",
            cname_ne="cname__ne",
            cname_not_in="cname__not_in",
            datacenter_eq="datacenter__eq",
            datacenter_in="datacenter__in",
            datacenter_ne="datacenter__ne",
            datacenter_not_in="datacenter__not_in",
            fields="fields",
            limit=10000,
            method_eq="method__eq",
            method_in="method__in",
            method_ne="method__ne",
            method_not_in="method__not_in",
            offset=0,
            resource_id_eq=0,
            resource_id_gt=0,
            resource_id_gte=0,
            resource_id_in="resource_id__in",
            resource_id_lt=0,
            resource_id_lte=0,
            resource_id_ne=0,
            resource_id_not_in="resource_id__not_in",
            size_eq=0,
            size_gt=0,
            size_gte=0,
            size_in="size__in",
            size_lt=0,
            size_lte=0,
            size_ne=0,
            size_not_in="size__not_in",
            sort="sort",
            status_eq=0,
            status_gt=0,
            status_gte=0,
            status_in="status__in",
            status_lt=0,
            status_lte=0,
            status_ne=0,
            status_not_in="status__not_in",
        )
        assert log.is_closed
        assert log.json() == {"foo": "bar"}
        assert cast(Any, log.is_closed) is True
        assert isinstance(log, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Gcore, respx_mock: MockRouter) -> None:
        respx_mock.get("/cdn/advanced/v1/logs/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        log = client.cdn.logs.with_raw_response.download(
            format="format",
            from_="from",
            to="to",
        )

        assert log.is_closed is True
        assert log.http_request.headers.get("X-Stainless-Lang") == "python"
        assert log.json() == {"foo": "bar"}
        assert isinstance(log, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Gcore, respx_mock: MockRouter) -> None:
        respx_mock.get("/cdn/advanced/v1/logs/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cdn.logs.with_streaming_response.download(
            format="format",
            from_="from",
            to="to",
        ) as log:
            assert not log.is_closed
            assert log.http_request.headers.get("X-Stainless-Lang") == "python"

            assert log.json() == {"foo": "bar"}
            assert cast(Any, log.is_closed) is True
            assert isinstance(log, StreamedBinaryAPIResponse)

        assert cast(Any, log.is_closed) is True


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        log = await async_client.cdn.logs.list(
            from_="from",
            to="to",
        )
        assert_matches_type(AsyncOffsetPageCdnLogs[Data], log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        log = await async_client.cdn.logs.list(
            from_="from",
            to="to",
            cache_status_eq="cache_status__eq",
            cache_status_in="cache_status__in",
            cache_status_ne="cache_status__ne",
            cache_status_not_in="cache_status__not_in",
            client_ip_eq="client_ip__eq",
            client_ip_in="client_ip__in",
            client_ip_ne="client_ip__ne",
            client_ip_not_in="client_ip__not_in",
            cname_contains="cname__contains",
            cname_eq="cname__eq",
            cname_in="cname__in",
            cname_ne="cname__ne",
            cname_not_in="cname__not_in",
            datacenter_eq="datacenter__eq",
            datacenter_in="datacenter__in",
            datacenter_ne="datacenter__ne",
            datacenter_not_in="datacenter__not_in",
            fields="fields",
            limit=1,
            method_eq="method__eq",
            method_in="method__in",
            method_ne="method__ne",
            method_not_in="method__not_in",
            offset=0,
            ordering="ordering",
            resource_id_eq=0,
            resource_id_gt=0,
            resource_id_gte=0,
            resource_id_in="resource_id__in",
            resource_id_lt=0,
            resource_id_lte=0,
            resource_id_ne=0,
            resource_id_not_in="resource_id__not_in",
            size_eq=0,
            size_gt=0,
            size_gte=0,
            size_in="size__in",
            size_lt=0,
            size_lte=0,
            size_ne=0,
            size_not_in="size__not_in",
            status_eq=0,
            status_gt=0,
            status_gte=0,
            status_in="status__in",
            status_lt=0,
            status_lte=0,
            status_ne=0,
            status_not_in="status__not_in",
        )
        assert_matches_type(AsyncOffsetPageCdnLogs[Data], log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.logs.with_raw_response.list(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(AsyncOffsetPageCdnLogs[Data], log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.logs.with_streaming_response.list(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(AsyncOffsetPageCdnLogs[Data], log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncGcore, respx_mock: MockRouter) -> None:
        respx_mock.get("/cdn/advanced/v1/logs/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        log = await async_client.cdn.logs.download(
            format="format",
            from_="from",
            to="to",
        )
        assert log.is_closed
        assert await log.json() == {"foo": "bar"}
        assert cast(Any, log.is_closed) is True
        assert isinstance(log, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_with_all_params(self, async_client: AsyncGcore, respx_mock: MockRouter) -> None:
        respx_mock.get("/cdn/advanced/v1/logs/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        log = await async_client.cdn.logs.download(
            format="format",
            from_="from",
            to="to",
            cache_status_eq="cache_status__eq",
            cache_status_in="cache_status__in",
            cache_status_ne="cache_status__ne",
            cache_status_not_in="cache_status__not_in",
            client_ip_eq="client_ip__eq",
            client_ip_in="client_ip__in",
            client_ip_ne="client_ip__ne",
            client_ip_not_in="client_ip__not_in",
            cname_contains="cname__contains",
            cname_eq="cname__eq",
            cname_in="cname__in",
            cname_ne="cname__ne",
            cname_not_in="cname__not_in",
            datacenter_eq="datacenter__eq",
            datacenter_in="datacenter__in",
            datacenter_ne="datacenter__ne",
            datacenter_not_in="datacenter__not_in",
            fields="fields",
            limit=10000,
            method_eq="method__eq",
            method_in="method__in",
            method_ne="method__ne",
            method_not_in="method__not_in",
            offset=0,
            resource_id_eq=0,
            resource_id_gt=0,
            resource_id_gte=0,
            resource_id_in="resource_id__in",
            resource_id_lt=0,
            resource_id_lte=0,
            resource_id_ne=0,
            resource_id_not_in="resource_id__not_in",
            size_eq=0,
            size_gt=0,
            size_gte=0,
            size_in="size__in",
            size_lt=0,
            size_lte=0,
            size_ne=0,
            size_not_in="size__not_in",
            sort="sort",
            status_eq=0,
            status_gt=0,
            status_gte=0,
            status_in="status__in",
            status_lt=0,
            status_lte=0,
            status_ne=0,
            status_not_in="status__not_in",
        )
        assert log.is_closed
        assert await log.json() == {"foo": "bar"}
        assert cast(Any, log.is_closed) is True
        assert isinstance(log, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncGcore, respx_mock: MockRouter) -> None:
        respx_mock.get("/cdn/advanced/v1/logs/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        log = await async_client.cdn.logs.with_raw_response.download(
            format="format",
            from_="from",
            to="to",
        )

        assert log.is_closed is True
        assert log.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await log.json() == {"foo": "bar"}
        assert isinstance(log, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncGcore, respx_mock: MockRouter) -> None:
        respx_mock.get("/cdn/advanced/v1/logs/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cdn.logs.with_streaming_response.download(
            format="format",
            from_="from",
            to="to",
        ) as log:
            assert not log.is_closed
            assert log.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await log.json() == {"foo": "bar"}
            assert cast(Any, log.is_closed) is True
            assert isinstance(log, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, log.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import (
    TaskIDList,
    ReservedFixedIP,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReservedFixedIPs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            type="external",
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            type="external",
            ip_family="dual",
            is_vip=False,
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.with_raw_response.create(
            project_id=0,
            region_id=0,
            type="external",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = response.parse()
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.with_streaming_response.create(
            project_id=0,
            region_id=0,
            type="external",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = response.parse()
            assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="subnet",
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="subnet",
            is_vip=False,
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.with_raw_response.create(
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="subnet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = response.parse()
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.with_streaming_response.create(
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="subnet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = response.parse()
            assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="any_subnet",
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="any_subnet",
            ip_family="dual",
            is_vip=False,
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.with_raw_response.create(
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="any_subnet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = response.parse()
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.with_streaming_response.create(
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="any_subnet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = response.parse()
            assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_4(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="ip_address",
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="ip_address",
            is_vip=False,
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_raw_response_create_overload_4(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.with_raw_response.create(
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="ip_address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = response.parse()
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_4(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.with_streaming_response.create(
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="ip_address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = response.parse()
            assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_5(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            port_id="77f1394f-2a18-4686-a2eb-acea25146374",
            type="port",
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_raw_response_create_overload_5(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.with_raw_response.create(
            project_id=0,
            region_id=0,
            port_id="77f1394f-2a18-4686-a2eb-acea25146374",
            type="port",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = response.parse()
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_5(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.with_streaming_response.create(
            project_id=0,
            region_id=0,
            port_id="77f1394f-2a18-4686-a2eb-acea25146374",
            type="port",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = response.parse()
            assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.update(
            port_id="port_id",
            project_id=0,
            region_id=0,
            is_vip=True,
        )
        assert_matches_type(ReservedFixedIP, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.with_raw_response.update(
            port_id="port_id",
            project_id=0,
            region_id=0,
            is_vip=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = response.parse()
        assert_matches_type(ReservedFixedIP, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.with_streaming_response.update(
            port_id="port_id",
            project_id=0,
            region_id=0,
            is_vip=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = response.parse()
            assert_matches_type(ReservedFixedIP, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.reserved_fixed_ips.with_raw_response.update(
                port_id="",
                project_id=0,
                region_id=0,
                is_vip=True,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SyncOffsetPage[ReservedFixedIP], reserved_fixed_ip, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.list(
            project_id=0,
            region_id=0,
            available_only=True,
            device_id="device_id",
            external_only=True,
            internal_only=True,
            ip_address="ip_address",
            limit=0,
            offset=0,
            order_by="order_by",
            vip_only=True,
        )
        assert_matches_type(SyncOffsetPage[ReservedFixedIP], reserved_fixed_ip, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = response.parse()
        assert_matches_type(SyncOffsetPage[ReservedFixedIP], reserved_fixed_ip, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = response.parse()
            assert_matches_type(SyncOffsetPage[ReservedFixedIP], reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.delete(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.with_raw_response.delete(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = response.parse()
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.with_streaming_response.delete(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = response.parse()
            assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.reserved_fixed_ips.with_raw_response.delete(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        reserved_fixed_ip = client.cloud.reserved_fixed_ips.get(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ReservedFixedIP, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.with_raw_response.get(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = response.parse()
        assert_matches_type(ReservedFixedIP, reserved_fixed_ip, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.with_streaming_response.get(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = response.parse()
            assert_matches_type(ReservedFixedIP, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.reserved_fixed_ips.with_raw_response.get(
                port_id="",
                project_id=0,
                region_id=0,
            )


class TestAsyncReservedFixedIPs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            type="external",
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            type="external",
            ip_family="dual",
            is_vip=False,
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.with_raw_response.create(
            project_id=0,
            region_id=0,
            type="external",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = await response.parse()
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.with_streaming_response.create(
            project_id=0,
            region_id=0,
            type="external",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = await response.parse()
            assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="subnet",
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="subnet",
            is_vip=False,
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.with_raw_response.create(
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="subnet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = await response.parse()
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.with_streaming_response.create(
            project_id=0,
            region_id=0,
            subnet_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="subnet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = await response.parse()
            assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="any_subnet",
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="any_subnet",
            ip_family="dual",
            is_vip=False,
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.with_raw_response.create(
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="any_subnet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = await response.parse()
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.with_streaming_response.create(
            project_id=0,
            region_id=0,
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="any_subnet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = await response.parse()
            assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="ip_address",
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="ip_address",
            is_vip=False,
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.with_raw_response.create(
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="ip_address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = await response.parse()
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.with_streaming_response.create(
            project_id=0,
            region_id=0,
            ip_address="192.168.123.20",
            network_id="e3c6ee77-48cb-416b-b204-11b492cc776e3",
            type="ip_address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = await response.parse()
            assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.create(
            project_id=0,
            region_id=0,
            port_id="77f1394f-2a18-4686-a2eb-acea25146374",
            type="port",
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.with_raw_response.create(
            project_id=0,
            region_id=0,
            port_id="77f1394f-2a18-4686-a2eb-acea25146374",
            type="port",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = await response.parse()
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.with_streaming_response.create(
            project_id=0,
            region_id=0,
            port_id="77f1394f-2a18-4686-a2eb-acea25146374",
            type="port",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = await response.parse()
            assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.update(
            port_id="port_id",
            project_id=0,
            region_id=0,
            is_vip=True,
        )
        assert_matches_type(ReservedFixedIP, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.with_raw_response.update(
            port_id="port_id",
            project_id=0,
            region_id=0,
            is_vip=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = await response.parse()
        assert_matches_type(ReservedFixedIP, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.with_streaming_response.update(
            port_id="port_id",
            project_id=0,
            region_id=0,
            is_vip=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = await response.parse()
            assert_matches_type(ReservedFixedIP, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.reserved_fixed_ips.with_raw_response.update(
                port_id="",
                project_id=0,
                region_id=0,
                is_vip=True,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(AsyncOffsetPage[ReservedFixedIP], reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.list(
            project_id=0,
            region_id=0,
            available_only=True,
            device_id="device_id",
            external_only=True,
            internal_only=True,
            ip_address="ip_address",
            limit=0,
            offset=0,
            order_by="order_by",
            vip_only=True,
        )
        assert_matches_type(AsyncOffsetPage[ReservedFixedIP], reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = await response.parse()
        assert_matches_type(AsyncOffsetPage[ReservedFixedIP], reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = await response.parse()
            assert_matches_type(AsyncOffsetPage[ReservedFixedIP], reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.delete(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.with_raw_response.delete(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = await response.parse()
        assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.with_streaming_response.delete(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = await response.parse()
            assert_matches_type(TaskIDList, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.reserved_fixed_ips.with_raw_response.delete(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        reserved_fixed_ip = await async_client.cloud.reserved_fixed_ips.get(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ReservedFixedIP, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.with_raw_response.get(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reserved_fixed_ip = await response.parse()
        assert_matches_type(ReservedFixedIP, reserved_fixed_ip, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.with_streaming_response.get(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reserved_fixed_ip = await response.parse()
            assert_matches_type(ReservedFixedIP, reserved_fixed_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.reserved_fixed_ips.with_raw_response.get(
                port_id="",
                project_id=0,
                region_id=0,
            )

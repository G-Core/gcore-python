# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import TaskIDList, NetworkInterface

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInterfaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        interface = client.cloud.instances.interfaces.list(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(SyncOffsetPage[NetworkInterface], interface, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        interface = client.cloud.instances.interfaces.list(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            limit=1000,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[NetworkInterface], interface, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.instances.interfaces.with_raw_response.list(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = response.parse()
        assert_matches_type(SyncOffsetPage[NetworkInterface], interface, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.instances.interfaces.with_streaming_response.list(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = response.parse()
            assert_matches_type(SyncOffsetPage[NetworkInterface], interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.interfaces.with_raw_response.list(
                instance_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_attach_overload_1(self, client: Gcore) -> None:
        interface = client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_method_attach_with_all_params_overload_1(self, client: Gcore) -> None:
        interface = client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            ddos_profile={
                "profile_template": 0,
                "fields": [
                    {
                        "base_field": 0,
                        "field_value": {},
                        "value": "value",
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="interface_name",
            ip_family="dual",
            port_group=0,
            security_groups=[{"id": "ae74714c-c380-48b4-87f8-758d656cdad6"}],
            type="external",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_raw_response_attach_overload_1(self, client: Gcore) -> None:
        response = client.cloud.instances.interfaces.with_raw_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = response.parse()
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_streaming_response_attach_overload_1(self, client: Gcore) -> None:
        with client.cloud.instances.interfaces.with_streaming_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = response.parse()
            assert_matches_type(TaskIDList, interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_attach_overload_1(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.interfaces.with_raw_response.attach(
                instance_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_attach_overload_2(self, client: Gcore) -> None:
        interface = client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_method_attach_with_all_params_overload_2(self, client: Gcore) -> None:
        interface = client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
            ddos_profile={
                "profile_template": 0,
                "fields": [
                    {
                        "base_field": 0,
                        "field_value": {},
                        "value": "value",
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="interface_name",
            port_group=0,
            security_groups=[{"id": "ae74714c-c380-48b4-87f8-758d656cdad6"}],
            type="subnet",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_raw_response_attach_overload_2(self, client: Gcore) -> None:
        response = client.cloud.instances.interfaces.with_raw_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = response.parse()
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_streaming_response_attach_overload_2(self, client: Gcore) -> None:
        with client.cloud.instances.interfaces.with_streaming_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = response.parse()
            assert_matches_type(TaskIDList, interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_attach_overload_2(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.interfaces.with_raw_response.attach(
                instance_id="",
                project_id=1,
                region_id=1,
                subnet_id="subnet_id",
            )

    @parametrize
    def test_method_attach_overload_3(self, client: Gcore) -> None:
        interface = client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            network_id="network_id",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_method_attach_with_all_params_overload_3(self, client: Gcore) -> None:
        interface = client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            network_id="network_id",
            ddos_profile={
                "profile_template": 0,
                "fields": [
                    {
                        "base_field": 0,
                        "field_value": {},
                        "value": "value",
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="interface_name",
            ip_family="dual",
            port_group=0,
            security_groups=[{"id": "ae74714c-c380-48b4-87f8-758d656cdad6"}],
            type="any_subnet",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_raw_response_attach_overload_3(self, client: Gcore) -> None:
        response = client.cloud.instances.interfaces.with_raw_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            network_id="network_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = response.parse()
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_streaming_response_attach_overload_3(self, client: Gcore) -> None:
        with client.cloud.instances.interfaces.with_streaming_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            network_id="network_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = response.parse()
            assert_matches_type(TaskIDList, interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_attach_overload_3(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.interfaces.with_raw_response.attach(
                instance_id="",
                project_id=1,
                region_id=1,
                network_id="network_id",
            )

    @parametrize
    def test_method_attach_overload_4(self, client: Gcore) -> None:
        interface = client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            port_id="port_id",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_method_attach_with_all_params_overload_4(self, client: Gcore) -> None:
        interface = client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            port_id="port_id",
            ddos_profile={
                "profile_template": 0,
                "fields": [
                    {
                        "base_field": 0,
                        "field_value": {},
                        "value": "value",
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="interface_name",
            port_group=0,
            security_groups=[{"id": "ae74714c-c380-48b4-87f8-758d656cdad6"}],
            type="reserved_fixed_ip",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_raw_response_attach_overload_4(self, client: Gcore) -> None:
        response = client.cloud.instances.interfaces.with_raw_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            port_id="port_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = response.parse()
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_streaming_response_attach_overload_4(self, client: Gcore) -> None:
        with client.cloud.instances.interfaces.with_streaming_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            port_id="port_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = response.parse()
            assert_matches_type(TaskIDList, interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_attach_overload_4(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.interfaces.with_raw_response.attach(
                instance_id="",
                project_id=1,
                region_id=1,
                port_id="port_id",
            )

    @parametrize
    def test_method_detach(self, client: Gcore) -> None:
        interface = client.cloud.instances.interfaces.detach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            ip_address="ip_address",
            port_id="port_id",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_raw_response_detach(self, client: Gcore) -> None:
        response = client.cloud.instances.interfaces.with_raw_response.detach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            ip_address="ip_address",
            port_id="port_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = response.parse()
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    def test_streaming_response_detach(self, client: Gcore) -> None:
        with client.cloud.instances.interfaces.with_streaming_response.detach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            ip_address="ip_address",
            port_id="port_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = response.parse()
            assert_matches_type(TaskIDList, interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_detach(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.interfaces.with_raw_response.detach(
                instance_id="",
                project_id=1,
                region_id=1,
                ip_address="ip_address",
                port_id="port_id",
            )


class TestAsyncInterfaces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        interface = await async_client.cloud.instances.interfaces.list(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(AsyncOffsetPage[NetworkInterface], interface, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        interface = await async_client.cloud.instances.interfaces.list(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            limit=1000,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[NetworkInterface], interface, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.interfaces.with_raw_response.list(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = await response.parse()
        assert_matches_type(AsyncOffsetPage[NetworkInterface], interface, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.interfaces.with_streaming_response.list(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = await response.parse()
            assert_matches_type(AsyncOffsetPage[NetworkInterface], interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.interfaces.with_raw_response.list(
                instance_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_attach_overload_1(self, async_client: AsyncGcore) -> None:
        interface = await async_client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_method_attach_with_all_params_overload_1(self, async_client: AsyncGcore) -> None:
        interface = await async_client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            ddos_profile={
                "profile_template": 0,
                "fields": [
                    {
                        "base_field": 0,
                        "field_value": {},
                        "value": "value",
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="interface_name",
            ip_family="dual",
            port_group=0,
            security_groups=[{"id": "ae74714c-c380-48b4-87f8-758d656cdad6"}],
            type="external",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_raw_response_attach_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.interfaces.with_raw_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = await response.parse()
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_streaming_response_attach_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.interfaces.with_streaming_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = await response.parse()
            assert_matches_type(TaskIDList, interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_attach_overload_1(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.interfaces.with_raw_response.attach(
                instance_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_attach_overload_2(self, async_client: AsyncGcore) -> None:
        interface = await async_client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_method_attach_with_all_params_overload_2(self, async_client: AsyncGcore) -> None:
        interface = await async_client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
            ddos_profile={
                "profile_template": 0,
                "fields": [
                    {
                        "base_field": 0,
                        "field_value": {},
                        "value": "value",
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="interface_name",
            port_group=0,
            security_groups=[{"id": "ae74714c-c380-48b4-87f8-758d656cdad6"}],
            type="subnet",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_raw_response_attach_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.interfaces.with_raw_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = await response.parse()
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_streaming_response_attach_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.interfaces.with_streaming_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = await response.parse()
            assert_matches_type(TaskIDList, interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_attach_overload_2(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.interfaces.with_raw_response.attach(
                instance_id="",
                project_id=1,
                region_id=1,
                subnet_id="subnet_id",
            )

    @parametrize
    async def test_method_attach_overload_3(self, async_client: AsyncGcore) -> None:
        interface = await async_client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            network_id="network_id",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_method_attach_with_all_params_overload_3(self, async_client: AsyncGcore) -> None:
        interface = await async_client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            network_id="network_id",
            ddos_profile={
                "profile_template": 0,
                "fields": [
                    {
                        "base_field": 0,
                        "field_value": {},
                        "value": "value",
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="interface_name",
            ip_family="dual",
            port_group=0,
            security_groups=[{"id": "ae74714c-c380-48b4-87f8-758d656cdad6"}],
            type="any_subnet",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_raw_response_attach_overload_3(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.interfaces.with_raw_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            network_id="network_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = await response.parse()
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_streaming_response_attach_overload_3(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.interfaces.with_streaming_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            network_id="network_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = await response.parse()
            assert_matches_type(TaskIDList, interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_attach_overload_3(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.interfaces.with_raw_response.attach(
                instance_id="",
                project_id=1,
                region_id=1,
                network_id="network_id",
            )

    @parametrize
    async def test_method_attach_overload_4(self, async_client: AsyncGcore) -> None:
        interface = await async_client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            port_id="port_id",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_method_attach_with_all_params_overload_4(self, async_client: AsyncGcore) -> None:
        interface = await async_client.cloud.instances.interfaces.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            port_id="port_id",
            ddos_profile={
                "profile_template": 0,
                "fields": [
                    {
                        "base_field": 0,
                        "field_value": {},
                        "value": "value",
                    }
                ],
                "profile_template_name": "profile_template_name",
            },
            interface_name="interface_name",
            port_group=0,
            security_groups=[{"id": "ae74714c-c380-48b4-87f8-758d656cdad6"}],
            type="reserved_fixed_ip",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_raw_response_attach_overload_4(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.interfaces.with_raw_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            port_id="port_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = await response.parse()
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_streaming_response_attach_overload_4(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.interfaces.with_streaming_response.attach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            port_id="port_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = await response.parse()
            assert_matches_type(TaskIDList, interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_attach_overload_4(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.interfaces.with_raw_response.attach(
                instance_id="",
                project_id=1,
                region_id=1,
                port_id="port_id",
            )

    @parametrize
    async def test_method_detach(self, async_client: AsyncGcore) -> None:
        interface = await async_client.cloud.instances.interfaces.detach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            ip_address="ip_address",
            port_id="port_id",
        )
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.interfaces.with_raw_response.detach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            ip_address="ip_address",
            port_id="port_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interface = await response.parse()
        assert_matches_type(TaskIDList, interface, path=["response"])

    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.interfaces.with_streaming_response.detach(
            instance_id="bf325375-9af6-4c8b-a2fc-7f6f4ca02e2e",
            project_id=1,
            region_id=1,
            ip_address="ip_address",
            port_id="port_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interface = await response.parse()
            assert_matches_type(TaskIDList, interface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_detach(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.interfaces.with_raw_response.detach(
                instance_id="",
                project_id=1,
                region_id=1,
                ip_address="ip_address",
                port_id="port_id",
            )

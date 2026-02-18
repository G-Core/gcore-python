# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import Subnet, TaskIDList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubnets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        subnet = client.cloud.networks.subnets.create(
            project_id=1,
            region_id=1,
            cidr="192.168.10.0/24",
            name="my subnet",
            network_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
        )
        assert_matches_type(TaskIDList, subnet, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        subnet = client.cloud.networks.subnets.create(
            project_id=1,
            region_id=1,
            cidr="192.168.10.0/24",
            name="my subnet",
            network_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
            connect_to_network_router=True,
            dns_nameservers=["8.8.4.4", "1.1.1.1"],
            enable_dhcp=True,
            gateway_ip="192.168.10.1",
            host_routes=[
                {
                    "destination": "10.0.3.0/24",
                    "nexthop": "10.0.0.13",
                }
            ],
            ip_version=4,
            router_id_to_connect="00000000-0000-4000-8000-000000000000",
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, subnet, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.networks.subnets.with_raw_response.create(
            project_id=1,
            region_id=1,
            cidr="192.168.10.0/24",
            name="my subnet",
            network_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subnet = response.parse()
        assert_matches_type(TaskIDList, subnet, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.networks.subnets.with_streaming_response.create(
            project_id=1,
            region_id=1,
            cidr="192.168.10.0/24",
            name="my subnet",
            network_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subnet = response.parse()
            assert_matches_type(TaskIDList, subnet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        subnet = client.cloud.networks.subnets.update(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Subnet, subnet, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        subnet = client.cloud.networks.subnets.update(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
            dns_nameservers=["8.8.4.4", "1.1.1.1"],
            enable_dhcp=True,
            gateway_ip="192.168.10.1",
            host_routes=[
                {
                    "destination": "10.0.3.0/24",
                    "nexthop": "10.0.0.13",
                }
            ],
            name="some_name",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(Subnet, subnet, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.networks.subnets.with_raw_response.update(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subnet = response.parse()
        assert_matches_type(Subnet, subnet, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.networks.subnets.with_streaming_response.update(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subnet = response.parse()
            assert_matches_type(Subnet, subnet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subnet_id` but received ''"):
            client.cloud.networks.subnets.with_raw_response.update(
                subnet_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        subnet = client.cloud.networks.subnets.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(SyncOffsetPage[Subnet], subnet, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        subnet = client.cloud.networks.subnets.list(
            project_id=1,
            region_id=1,
            limit=1000,
            network_id="b30d0de7-bca2-4c83-9c57-9e645bd2cc92",
            offset=0,
            order_by="name.asc",
            tag_key=["key1", "key2"],
            tag_key_value="tag_key_value",
        )
        assert_matches_type(SyncOffsetPage[Subnet], subnet, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.networks.subnets.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subnet = response.parse()
        assert_matches_type(SyncOffsetPage[Subnet], subnet, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.networks.subnets.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subnet = response.parse()
            assert_matches_type(SyncOffsetPage[Subnet], subnet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        subnet = client.cloud.networks.subnets.delete(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, subnet, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.networks.subnets.with_raw_response.delete(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subnet = response.parse()
        assert_matches_type(TaskIDList, subnet, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.networks.subnets.with_streaming_response.delete(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subnet = response.parse()
            assert_matches_type(TaskIDList, subnet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subnet_id` but received ''"):
            client.cloud.networks.subnets.with_raw_response.delete(
                subnet_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        subnet = client.cloud.networks.subnets.get(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Subnet, subnet, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.networks.subnets.with_raw_response.get(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subnet = response.parse()
        assert_matches_type(Subnet, subnet, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.networks.subnets.with_streaming_response.get(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subnet = response.parse()
            assert_matches_type(Subnet, subnet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subnet_id` but received ''"):
            client.cloud.networks.subnets.with_raw_response.get(
                subnet_id="",
                project_id=1,
                region_id=1,
            )


class TestAsyncSubnets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        subnet = await async_client.cloud.networks.subnets.create(
            project_id=1,
            region_id=1,
            cidr="192.168.10.0/24",
            name="my subnet",
            network_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
        )
        assert_matches_type(TaskIDList, subnet, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        subnet = await async_client.cloud.networks.subnets.create(
            project_id=1,
            region_id=1,
            cidr="192.168.10.0/24",
            name="my subnet",
            network_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
            connect_to_network_router=True,
            dns_nameservers=["8.8.4.4", "1.1.1.1"],
            enable_dhcp=True,
            gateway_ip="192.168.10.1",
            host_routes=[
                {
                    "destination": "10.0.3.0/24",
                    "nexthop": "10.0.0.13",
                }
            ],
            ip_version=4,
            router_id_to_connect="00000000-0000-4000-8000-000000000000",
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, subnet, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.subnets.with_raw_response.create(
            project_id=1,
            region_id=1,
            cidr="192.168.10.0/24",
            name="my subnet",
            network_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subnet = await response.parse()
        assert_matches_type(TaskIDList, subnet, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.subnets.with_streaming_response.create(
            project_id=1,
            region_id=1,
            cidr="192.168.10.0/24",
            name="my subnet",
            network_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subnet = await response.parse()
            assert_matches_type(TaskIDList, subnet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        subnet = await async_client.cloud.networks.subnets.update(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Subnet, subnet, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        subnet = await async_client.cloud.networks.subnets.update(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
            dns_nameservers=["8.8.4.4", "1.1.1.1"],
            enable_dhcp=True,
            gateway_ip="192.168.10.1",
            host_routes=[
                {
                    "destination": "10.0.3.0/24",
                    "nexthop": "10.0.0.13",
                }
            ],
            name="some_name",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(Subnet, subnet, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.subnets.with_raw_response.update(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subnet = await response.parse()
        assert_matches_type(Subnet, subnet, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.subnets.with_streaming_response.update(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subnet = await response.parse()
            assert_matches_type(Subnet, subnet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subnet_id` but received ''"):
            await async_client.cloud.networks.subnets.with_raw_response.update(
                subnet_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        subnet = await async_client.cloud.networks.subnets.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(AsyncOffsetPage[Subnet], subnet, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        subnet = await async_client.cloud.networks.subnets.list(
            project_id=1,
            region_id=1,
            limit=1000,
            network_id="b30d0de7-bca2-4c83-9c57-9e645bd2cc92",
            offset=0,
            order_by="name.asc",
            tag_key=["key1", "key2"],
            tag_key_value="tag_key_value",
        )
        assert_matches_type(AsyncOffsetPage[Subnet], subnet, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.subnets.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subnet = await response.parse()
        assert_matches_type(AsyncOffsetPage[Subnet], subnet, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.subnets.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subnet = await response.parse()
            assert_matches_type(AsyncOffsetPage[Subnet], subnet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        subnet = await async_client.cloud.networks.subnets.delete(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, subnet, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.subnets.with_raw_response.delete(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subnet = await response.parse()
        assert_matches_type(TaskIDList, subnet, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.subnets.with_streaming_response.delete(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subnet = await response.parse()
            assert_matches_type(TaskIDList, subnet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subnet_id` but received ''"):
            await async_client.cloud.networks.subnets.with_raw_response.delete(
                subnet_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        subnet = await async_client.cloud.networks.subnets.get(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Subnet, subnet, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.subnets.with_raw_response.get(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subnet = await response.parse()
        assert_matches_type(Subnet, subnet, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.subnets.with_streaming_response.get(
            subnet_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subnet = await response.parse()
            assert_matches_type(Subnet, subnet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subnet_id` but received ''"):
            await async_client.cloud.networks.subnets.with_raw_response.get(
                subnet_id="",
                project_id=1,
                region_id=1,
            )

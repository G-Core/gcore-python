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
    LoadBalancer,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLoadBalancers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        load_balancer = client.cloud.load_balancers.create(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        load_balancer = client.cloud.load_balancers.create(
            project_id=0,
            region_id=0,
            flavor="lb1-1-2",
            floating_ip={
                "existing_floating_id": "c64e5db1-5f1f-43ec-a8d9-5090df85b82d",
                "source": "existing",
            },
            listeners=[
                {
                    "name": "my_listener",
                    "protocol": "HTTP",
                    "protocol_port": 80,
                    "allowed_cidrs": ["10.0.0.0/8"],
                    "connection_limit": 100000,
                    "insert_x_forwarded": False,
                    "pools": [
                        {
                            "lb_algorithm": "LEAST_CONNECTIONS",
                            "name": "pool_name",
                            "protocol": "HTTP",
                            "ca_secret_id": "ca_secret_id",
                            "crl_secret_id": "crl_secret_id",
                            "healthmonitor": {
                                "delay": 10,
                                "max_retries": 3,
                                "timeout": 5,
                                "type": "HTTP",
                                "expected_codes": "200,301,302",
                                "http_method": "GET",
                                "max_retries_down": 3,
                                "url_path": "/",
                            },
                            "listener_id": "listener_id",
                            "loadbalancer_id": "bbb35f84-35cc-4b2f-84c2-a6a29bba68aa",
                            "members": [
                                {
                                    "address": "192.168.1.101",
                                    "protocol_port": 8000,
                                    "admin_state_up": True,
                                    "instance_id": "a7e7e8d6-0bf7-4ac9-8170-831b47ee2ba9",
                                    "monitor_address": "monitor_address",
                                    "monitor_port": 0,
                                    "subnet_id": "32283b0b-b560-4690-810c-f672cbb2e28d",
                                    "weight": 2,
                                },
                                {
                                    "address": "192.168.1.102",
                                    "protocol_port": 8000,
                                    "admin_state_up": True,
                                    "instance_id": "169942e0-9b53-42df-95ef-1a8b6525c2bd",
                                    "monitor_address": "monitor_address",
                                    "monitor_port": 0,
                                    "subnet_id": "32283b0b-b560-4690-810c-f672cbb2e28d",
                                    "weight": 4,
                                },
                            ],
                            "secret_id": "secret_id",
                            "session_persistence": {
                                "type": "APP_COOKIE",
                                "cookie_name": "cookie_name",
                                "persistence_granularity": "persistence_granularity",
                                "persistence_timeout": 0,
                            },
                            "timeout_client_data": 50000,
                            "timeout_member_connect": 50000,
                            "timeout_member_data": 0,
                        }
                    ],
                    "secret_id": "f2e734d0-fa2b-42c2-ad33-4c6db5101e00",
                    "sni_secret_id": ["f2e734d0-fa2b-42c2-ad33-4c6db5101e00", "eb121225-7ded-4ff3-ae1f-599e145dd7cb"],
                    "timeout_client_data": 50000,
                    "timeout_member_connect": 50000,
                    "timeout_member_data": 0,
                    "user_list": [
                        {
                            "encrypted_password": "$5$isRr.HJ1IrQP38.m$oViu3DJOpUG2ZsjCBtbITV3mqpxxbZfyWJojLPNSPO5",
                            "username": "admin",
                        }
                    ],
                }
            ],
            logging={
                "destination_region_id": 1,
                "enabled": True,
                "retention_policy": {"period": 45},
                "topic_name": "my-log-name",
            },
            name="new_load_balancer",
            name_template="lb_name_template",
            preferred_connectivity="L2",
            tags={"my-tag": "my-tag-value"},
            vip_ip_family="dual",
            vip_network_id="ac307687-31a4-4a11-a949-6bea1b2878f5",
            vip_port_id="ff83e13a-b256-4be2-ba5d-028d3f0ab450",
            vip_subnet_id="4e7802d3-5023-44b8-b298-7726558fddf4",
        )
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.with_raw_response.create(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.load_balancers.with_streaming_response.create(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(TaskIDList, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        load_balancer = client.cloud.load_balancers.update(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        load_balancer = client.cloud.load_balancers.update(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            logging={
                "destination_region_id": 1,
                "enabled": True,
                "retention_policy": {"period": 45},
                "topic_name": "my-log-name",
            },
            name="some_name",
            preferred_connectivity="L2",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.with_raw_response.update(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.load_balancers.with_streaming_response.update(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(LoadBalancer, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loadbalancer_id` but received ''"):
            client.cloud.load_balancers.with_raw_response.update(
                loadbalancer_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        load_balancer = client.cloud.load_balancers.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SyncOffsetPage[LoadBalancer], load_balancer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        load_balancer = client.cloud.load_balancers.list(
            project_id=0,
            region_id=0,
            assigned_floating=True,
            limit=0,
            logging_enabled=True,
            name="name",
            offset=0,
            order_by="order_by",
            show_stats=True,
            tag_key=["string"],
            tag_key_value="tag_key_value",
            with_ddos=True,
        )
        assert_matches_type(SyncOffsetPage[LoadBalancer], load_balancer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(SyncOffsetPage[LoadBalancer], load_balancer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.load_balancers.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(SyncOffsetPage[LoadBalancer], load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        load_balancer = client.cloud.load_balancers.delete(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.with_raw_response.delete(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.load_balancers.with_streaming_response.delete(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(TaskIDList, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loadbalancer_id` but received ''"):
            client.cloud.load_balancers.with_raw_response.delete(
                loadbalancer_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_failover(self, client: Gcore) -> None:
        load_balancer = client.cloud.load_balancers.failover(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    def test_method_failover_with_all_params(self, client: Gcore) -> None:
        load_balancer = client.cloud.load_balancers.failover(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            force=True,
        )
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    def test_raw_response_failover(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.with_raw_response.failover(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    def test_streaming_response_failover(self, client: Gcore) -> None:
        with client.cloud.load_balancers.with_streaming_response.failover(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(TaskIDList, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_failover(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loadbalancer_id` but received ''"):
            client.cloud.load_balancers.with_raw_response.failover(
                loadbalancer_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        load_balancer = client.cloud.load_balancers.get(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Gcore) -> None:
        load_balancer = client.cloud.load_balancers.get(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            show_stats=True,
            with_ddos=True,
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.with_raw_response.get(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.load_balancers.with_streaming_response.get(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(LoadBalancer, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loadbalancer_id` but received ''"):
            client.cloud.load_balancers.with_raw_response.get(
                loadbalancer_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_resize(self, client: Gcore) -> None:
        load_balancer = client.cloud.load_balancers.resize(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            flavor="lb1-2-4",
        )
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    def test_raw_response_resize(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.with_raw_response.resize(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            flavor="lb1-2-4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    def test_streaming_response_resize(self, client: Gcore) -> None:
        with client.cloud.load_balancers.with_streaming_response.resize(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            flavor="lb1-2-4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(TaskIDList, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resize(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loadbalancer_id` but received ''"):
            client.cloud.load_balancers.with_raw_response.resize(
                loadbalancer_id="",
                project_id=0,
                region_id=0,
                flavor="lb1-2-4",
            )


class TestAsyncLoadBalancers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        load_balancer = await async_client.cloud.load_balancers.create(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        load_balancer = await async_client.cloud.load_balancers.create(
            project_id=0,
            region_id=0,
            flavor="lb1-1-2",
            floating_ip={
                "existing_floating_id": "c64e5db1-5f1f-43ec-a8d9-5090df85b82d",
                "source": "existing",
            },
            listeners=[
                {
                    "name": "my_listener",
                    "protocol": "HTTP",
                    "protocol_port": 80,
                    "allowed_cidrs": ["10.0.0.0/8"],
                    "connection_limit": 100000,
                    "insert_x_forwarded": False,
                    "pools": [
                        {
                            "lb_algorithm": "LEAST_CONNECTIONS",
                            "name": "pool_name",
                            "protocol": "HTTP",
                            "ca_secret_id": "ca_secret_id",
                            "crl_secret_id": "crl_secret_id",
                            "healthmonitor": {
                                "delay": 10,
                                "max_retries": 3,
                                "timeout": 5,
                                "type": "HTTP",
                                "expected_codes": "200,301,302",
                                "http_method": "GET",
                                "max_retries_down": 3,
                                "url_path": "/",
                            },
                            "listener_id": "listener_id",
                            "loadbalancer_id": "bbb35f84-35cc-4b2f-84c2-a6a29bba68aa",
                            "members": [
                                {
                                    "address": "192.168.1.101",
                                    "protocol_port": 8000,
                                    "admin_state_up": True,
                                    "instance_id": "a7e7e8d6-0bf7-4ac9-8170-831b47ee2ba9",
                                    "monitor_address": "monitor_address",
                                    "monitor_port": 0,
                                    "subnet_id": "32283b0b-b560-4690-810c-f672cbb2e28d",
                                    "weight": 2,
                                },
                                {
                                    "address": "192.168.1.102",
                                    "protocol_port": 8000,
                                    "admin_state_up": True,
                                    "instance_id": "169942e0-9b53-42df-95ef-1a8b6525c2bd",
                                    "monitor_address": "monitor_address",
                                    "monitor_port": 0,
                                    "subnet_id": "32283b0b-b560-4690-810c-f672cbb2e28d",
                                    "weight": 4,
                                },
                            ],
                            "secret_id": "secret_id",
                            "session_persistence": {
                                "type": "APP_COOKIE",
                                "cookie_name": "cookie_name",
                                "persistence_granularity": "persistence_granularity",
                                "persistence_timeout": 0,
                            },
                            "timeout_client_data": 50000,
                            "timeout_member_connect": 50000,
                            "timeout_member_data": 0,
                        }
                    ],
                    "secret_id": "f2e734d0-fa2b-42c2-ad33-4c6db5101e00",
                    "sni_secret_id": ["f2e734d0-fa2b-42c2-ad33-4c6db5101e00", "eb121225-7ded-4ff3-ae1f-599e145dd7cb"],
                    "timeout_client_data": 50000,
                    "timeout_member_connect": 50000,
                    "timeout_member_data": 0,
                    "user_list": [
                        {
                            "encrypted_password": "$5$isRr.HJ1IrQP38.m$oViu3DJOpUG2ZsjCBtbITV3mqpxxbZfyWJojLPNSPO5",
                            "username": "admin",
                        }
                    ],
                }
            ],
            logging={
                "destination_region_id": 1,
                "enabled": True,
                "retention_policy": {"period": 45},
                "topic_name": "my-log-name",
            },
            name="new_load_balancer",
            name_template="lb_name_template",
            preferred_connectivity="L2",
            tags={"my-tag": "my-tag-value"},
            vip_ip_family="dual",
            vip_network_id="ac307687-31a4-4a11-a949-6bea1b2878f5",
            vip_port_id="ff83e13a-b256-4be2-ba5d-028d3f0ab450",
            vip_subnet_id="4e7802d3-5023-44b8-b298-7726558fddf4",
        )
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.with_raw_response.create(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.with_streaming_response.create(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(TaskIDList, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        load_balancer = await async_client.cloud.load_balancers.update(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        load_balancer = await async_client.cloud.load_balancers.update(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            logging={
                "destination_region_id": 1,
                "enabled": True,
                "retention_policy": {"period": 45},
                "topic_name": "my-log-name",
            },
            name="some_name",
            preferred_connectivity="L2",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.with_raw_response.update(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.with_streaming_response.update(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(LoadBalancer, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loadbalancer_id` but received ''"):
            await async_client.cloud.load_balancers.with_raw_response.update(
                loadbalancer_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        load_balancer = await async_client.cloud.load_balancers.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(AsyncOffsetPage[LoadBalancer], load_balancer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        load_balancer = await async_client.cloud.load_balancers.list(
            project_id=0,
            region_id=0,
            assigned_floating=True,
            limit=0,
            logging_enabled=True,
            name="name",
            offset=0,
            order_by="order_by",
            show_stats=True,
            tag_key=["string"],
            tag_key_value="tag_key_value",
            with_ddos=True,
        )
        assert_matches_type(AsyncOffsetPage[LoadBalancer], load_balancer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(AsyncOffsetPage[LoadBalancer], load_balancer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(AsyncOffsetPage[LoadBalancer], load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        load_balancer = await async_client.cloud.load_balancers.delete(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.with_raw_response.delete(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.with_streaming_response.delete(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(TaskIDList, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loadbalancer_id` but received ''"):
            await async_client.cloud.load_balancers.with_raw_response.delete(
                loadbalancer_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_failover(self, async_client: AsyncGcore) -> None:
        load_balancer = await async_client.cloud.load_balancers.failover(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    async def test_method_failover_with_all_params(self, async_client: AsyncGcore) -> None:
        load_balancer = await async_client.cloud.load_balancers.failover(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            force=True,
        )
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    async def test_raw_response_failover(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.with_raw_response.failover(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    async def test_streaming_response_failover(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.with_streaming_response.failover(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(TaskIDList, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_failover(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loadbalancer_id` but received ''"):
            await async_client.cloud.load_balancers.with_raw_response.failover(
                loadbalancer_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        load_balancer = await async_client.cloud.load_balancers.get(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncGcore) -> None:
        load_balancer = await async_client.cloud.load_balancers.get(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            show_stats=True,
            with_ddos=True,
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.with_raw_response.get(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.with_streaming_response.get(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(LoadBalancer, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loadbalancer_id` but received ''"):
            await async_client.cloud.load_balancers.with_raw_response.get(
                loadbalancer_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_resize(self, async_client: AsyncGcore) -> None:
        load_balancer = await async_client.cloud.load_balancers.resize(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            flavor="lb1-2-4",
        )
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    async def test_raw_response_resize(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.with_raw_response.resize(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            flavor="lb1-2-4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(TaskIDList, load_balancer, path=["response"])

    @parametrize
    async def test_streaming_response_resize(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.with_streaming_response.resize(
            loadbalancer_id="loadbalancer_id",
            project_id=0,
            region_id=0,
            flavor="lb1-2-4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(TaskIDList, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resize(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loadbalancer_id` but received ''"):
            await async_client.cloud.load_balancers.with_raw_response.resize(
                loadbalancer_id="",
                project_id=0,
                region_id=0,
                flavor="lb1-2-4",
            )

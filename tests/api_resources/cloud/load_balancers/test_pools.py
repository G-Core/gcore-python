# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import TaskIDList, LoadBalancerPool, LoadBalancerPoolList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        pool = client.cloud.load_balancers.pools.create(
            project_id=1,
            region_id=1,
            lb_algorithm="LEAST_CONNECTIONS",
            name="pool_name",
            protocol="HTTP",
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        pool = client.cloud.load_balancers.pools.create(
            project_id=1,
            region_id=1,
            lb_algorithm="LEAST_CONNECTIONS",
            name="pool_name",
            protocol="HTTP",
            ca_secret_id="ca_secret_id",
            crl_secret_id="crl_secret_id",
            healthmonitor={
                "delay": 10,
                "max_retries": 3,
                "timeout": 5,
                "type": "HTTP",
                "expected_codes": "200,301,302",
                "http_method": "GET",
                "max_retries_down": 3,
                "url_path": "/",
            },
            listener_id="listener_id",
            loadbalancer_id="bbb35f84-35cc-4b2f-84c2-a6a29bba68aa",
            members=[
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
            secret_id="secret_id",
            session_persistence={
                "type": "APP_COOKIE",
                "cookie_name": "cookie_name",
                "persistence_granularity": "persistence_granularity",
                "persistence_timeout": 0,
            },
            timeout_client_data=50000,
            timeout_member_connect=50000,
            timeout_member_data=0,
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.pools.with_raw_response.create(
            project_id=1,
            region_id=1,
            lb_algorithm="LEAST_CONNECTIONS",
            name="pool_name",
            protocol="HTTP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.load_balancers.pools.with_streaming_response.create(
            project_id=1,
            region_id=1,
            lb_algorithm="LEAST_CONNECTIONS",
            name="pool_name",
            protocol="HTTP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(TaskIDList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        pool = client.cloud.load_balancers.pools.update(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        pool = client.cloud.load_balancers.pools.update(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            ca_secret_id="ca_secret_id",
            crl_secret_id="crl_secret_id",
            healthmonitor={
                "delay": 10,
                "max_retries": 2,
                "timeout": 5,
                "expected_codes": "200,301,302",
                "http_method": "CONNECT",
                "max_retries_down": 2,
                "type": "HTTP",
                "url_path": "/",
            },
            lb_algorithm="LEAST_CONNECTIONS",
            members=[
                {
                    "address": "192.168.40.33",
                    "protocol_port": 80,
                    "admin_state_up": True,
                    "instance_id": "a7e7e8d6-0bf7-4ac9-8170-831b47ee2ba9",
                    "monitor_address": "monitor_address",
                    "monitor_port": 0,
                    "subnet_id": "32283b0b-b560-4690-810c-f672cbb2e28d",
                    "weight": 1,
                }
            ],
            name="new_pool_name",
            protocol="HTTP",
            secret_id="secret_id",
            session_persistence={
                "type": "APP_COOKIE",
                "cookie_name": "cookie_name",
                "persistence_granularity": "persistence_granularity",
                "persistence_timeout": 0,
            },
            timeout_client_data=50000,
            timeout_member_connect=50000,
            timeout_member_data=0,
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.pools.with_raw_response.update(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.load_balancers.pools.with_streaming_response.update(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(TaskIDList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.cloud.load_balancers.pools.with_raw_response.update(
                pool_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        pool = client.cloud.load_balancers.pools.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerPoolList, pool, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        pool = client.cloud.load_balancers.pools.list(
            project_id=1,
            region_id=1,
            details=True,
            listener_id="00000000-0000-4000-8000-000000000000",
            loadbalancer_id="00000000-0000-4000-8000-000000000000",
        )
        assert_matches_type(LoadBalancerPoolList, pool, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.pools.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(LoadBalancerPoolList, pool, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.load_balancers.pools.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(LoadBalancerPoolList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        pool = client.cloud.load_balancers.pools.delete(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.pools.with_raw_response.delete(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.load_balancers.pools.with_streaming_response.delete(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(TaskIDList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.cloud.load_balancers.pools.with_raw_response.delete(
                pool_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        pool = client.cloud.load_balancers.pools.get(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerPool, pool, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.pools.with_raw_response.get(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(LoadBalancerPool, pool, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.load_balancers.pools.with_streaming_response.get(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(LoadBalancerPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.cloud.load_balancers.pools.with_raw_response.get(
                pool_id="",
                project_id=1,
                region_id=1,
            )


class TestAsyncPools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.load_balancers.pools.create(
            project_id=1,
            region_id=1,
            lb_algorithm="LEAST_CONNECTIONS",
            name="pool_name",
            protocol="HTTP",
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.load_balancers.pools.create(
            project_id=1,
            region_id=1,
            lb_algorithm="LEAST_CONNECTIONS",
            name="pool_name",
            protocol="HTTP",
            ca_secret_id="ca_secret_id",
            crl_secret_id="crl_secret_id",
            healthmonitor={
                "delay": 10,
                "max_retries": 3,
                "timeout": 5,
                "type": "HTTP",
                "expected_codes": "200,301,302",
                "http_method": "GET",
                "max_retries_down": 3,
                "url_path": "/",
            },
            listener_id="listener_id",
            loadbalancer_id="bbb35f84-35cc-4b2f-84c2-a6a29bba68aa",
            members=[
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
            secret_id="secret_id",
            session_persistence={
                "type": "APP_COOKIE",
                "cookie_name": "cookie_name",
                "persistence_granularity": "persistence_granularity",
                "persistence_timeout": 0,
            },
            timeout_client_data=50000,
            timeout_member_connect=50000,
            timeout_member_data=0,
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.pools.with_raw_response.create(
            project_id=1,
            region_id=1,
            lb_algorithm="LEAST_CONNECTIONS",
            name="pool_name",
            protocol="HTTP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.pools.with_streaming_response.create(
            project_id=1,
            region_id=1,
            lb_algorithm="LEAST_CONNECTIONS",
            name="pool_name",
            protocol="HTTP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(TaskIDList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.load_balancers.pools.update(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.load_balancers.pools.update(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            ca_secret_id="ca_secret_id",
            crl_secret_id="crl_secret_id",
            healthmonitor={
                "delay": 10,
                "max_retries": 2,
                "timeout": 5,
                "expected_codes": "200,301,302",
                "http_method": "CONNECT",
                "max_retries_down": 2,
                "type": "HTTP",
                "url_path": "/",
            },
            lb_algorithm="LEAST_CONNECTIONS",
            members=[
                {
                    "address": "192.168.40.33",
                    "protocol_port": 80,
                    "admin_state_up": True,
                    "instance_id": "a7e7e8d6-0bf7-4ac9-8170-831b47ee2ba9",
                    "monitor_address": "monitor_address",
                    "monitor_port": 0,
                    "subnet_id": "32283b0b-b560-4690-810c-f672cbb2e28d",
                    "weight": 1,
                }
            ],
            name="new_pool_name",
            protocol="HTTP",
            secret_id="secret_id",
            session_persistence={
                "type": "APP_COOKIE",
                "cookie_name": "cookie_name",
                "persistence_granularity": "persistence_granularity",
                "persistence_timeout": 0,
            },
            timeout_client_data=50000,
            timeout_member_connect=50000,
            timeout_member_data=0,
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.pools.with_raw_response.update(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.pools.with_streaming_response.update(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(TaskIDList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.cloud.load_balancers.pools.with_raw_response.update(
                pool_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.load_balancers.pools.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerPoolList, pool, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.load_balancers.pools.list(
            project_id=1,
            region_id=1,
            details=True,
            listener_id="00000000-0000-4000-8000-000000000000",
            loadbalancer_id="00000000-0000-4000-8000-000000000000",
        )
        assert_matches_type(LoadBalancerPoolList, pool, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.pools.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(LoadBalancerPoolList, pool, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.pools.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(LoadBalancerPoolList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.load_balancers.pools.delete(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.pools.with_raw_response.delete(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(TaskIDList, pool, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.pools.with_streaming_response.delete(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(TaskIDList, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.cloud.load_balancers.pools.with_raw_response.delete(
                pool_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        pool = await async_client.cloud.load_balancers.pools.get(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerPool, pool, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.pools.with_raw_response.get(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(LoadBalancerPool, pool, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.pools.with_streaming_response.get(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(LoadBalancerPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.cloud.load_balancers.pools.with_raw_response.get(
                pool_id="",
                project_id=1,
                region_id=1,
            )

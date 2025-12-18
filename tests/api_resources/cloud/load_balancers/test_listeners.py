# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import TaskIDList, LoadBalancerListenerList, LoadBalancerListenerDetail

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestListeners:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        listener = client.cloud.load_balancers.listeners.create(
            project_id=1,
            region_id=1,
            load_balancer_id="30f4f55b-4a7c-48e0-9954-5cddfee216e7",
            name="my_listener",
            protocol="HTTP",
            protocol_port=80,
        )
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        listener = client.cloud.load_balancers.listeners.create(
            project_id=1,
            region_id=1,
            load_balancer_id="30f4f55b-4a7c-48e0-9954-5cddfee216e7",
            name="my_listener",
            protocol="HTTP",
            protocol_port=80,
            allowed_cidrs=["10.0.0.0/8"],
            connection_limit=100000,
            default_pool_id="00000000-0000-4000-8000-000000000000",
            insert_x_forwarded=False,
            secret_id="f2e734d0-fa2b-42c2-ad33-4c6db5101e00",
            sni_secret_id=["f2e734d0-fa2b-42c2-ad33-4c6db5101e00", "eb121225-7ded-4ff3-ae1f-599e145dd7cb"],
            timeout_client_data=50000,
            timeout_member_connect=50000,
            timeout_member_data=None,
            user_list=[
                {
                    "encrypted_password": "$5$isRr.HJ1IrQP38.m$oViu3DJOpUG2ZsjCBtbITV3mqpxxbZfyWJojLPNSPO5",
                    "username": "admin",
                }
            ],
        )
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.listeners.with_raw_response.create(
            project_id=1,
            region_id=1,
            load_balancer_id="30f4f55b-4a7c-48e0-9954-5cddfee216e7",
            name="my_listener",
            protocol="HTTP",
            protocol_port=80,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listener = response.parse()
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.load_balancers.listeners.with_streaming_response.create(
            project_id=1,
            region_id=1,
            load_balancer_id="30f4f55b-4a7c-48e0-9954-5cddfee216e7",
            name="my_listener",
            protocol="HTTP",
            protocol_port=80,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listener = response.parse()
            assert_matches_type(TaskIDList, listener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        listener = client.cloud.load_balancers.listeners.update(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        listener = client.cloud.load_balancers.listeners.update(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            allowed_cidrs=["10.0.0.0/8"],
            connection_limit=100000,
            name="new_listener_name",
            secret_id="af4a64e7-03ca-470f-9a09-b77d54c5abd8",
            sni_secret_id=["af4a64e7-03ca-470f-9a09-b77d54c5abd8", "12b43d95-d420-4c79-a883-49bf146cbdff"],
            timeout_client_data=50000,
            timeout_member_connect=50000,
            timeout_member_data=None,
            user_list=[
                {
                    "encrypted_password": "$5$isRr.HJ1IrQP38.m$oViu3DJOpUG2ZsjCBtbITV3mqpxxbZfyWJojLPNSPO5",
                    "username": "admin",
                }
            ],
        )
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.listeners.with_raw_response.update(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listener = response.parse()
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.load_balancers.listeners.with_streaming_response.update(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listener = response.parse()
            assert_matches_type(TaskIDList, listener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `listener_id` but received ''"):
            client.cloud.load_balancers.listeners.with_raw_response.update(
                listener_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        listener = client.cloud.load_balancers.listeners.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerListenerList, listener, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        listener = client.cloud.load_balancers.listeners.list(
            project_id=1,
            region_id=1,
            load_balancer_id="00000000-0000-4000-8000-000000000000",
            show_stats=True,
        )
        assert_matches_type(LoadBalancerListenerList, listener, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.listeners.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listener = response.parse()
        assert_matches_type(LoadBalancerListenerList, listener, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.load_balancers.listeners.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listener = response.parse()
            assert_matches_type(LoadBalancerListenerList, listener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        listener = client.cloud.load_balancers.listeners.delete(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        listener = client.cloud.load_balancers.listeners.delete(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            delete_default_pool=False,
        )
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.listeners.with_raw_response.delete(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listener = response.parse()
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.load_balancers.listeners.with_streaming_response.delete(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listener = response.parse()
            assert_matches_type(TaskIDList, listener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `listener_id` but received ''"):
            client.cloud.load_balancers.listeners.with_raw_response.delete(
                listener_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        listener = client.cloud.load_balancers.listeners.get(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerListenerDetail, listener, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Gcore) -> None:
        listener = client.cloud.load_balancers.listeners.get(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            show_stats=True,
        )
        assert_matches_type(LoadBalancerListenerDetail, listener, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.listeners.with_raw_response.get(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listener = response.parse()
        assert_matches_type(LoadBalancerListenerDetail, listener, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.load_balancers.listeners.with_streaming_response.get(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listener = response.parse()
            assert_matches_type(LoadBalancerListenerDetail, listener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `listener_id` but received ''"):
            client.cloud.load_balancers.listeners.with_raw_response.get(
                listener_id="",
                project_id=1,
                region_id=1,
            )


class TestAsyncListeners:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        listener = await async_client.cloud.load_balancers.listeners.create(
            project_id=1,
            region_id=1,
            load_balancer_id="30f4f55b-4a7c-48e0-9954-5cddfee216e7",
            name="my_listener",
            protocol="HTTP",
            protocol_port=80,
        )
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        listener = await async_client.cloud.load_balancers.listeners.create(
            project_id=1,
            region_id=1,
            load_balancer_id="30f4f55b-4a7c-48e0-9954-5cddfee216e7",
            name="my_listener",
            protocol="HTTP",
            protocol_port=80,
            allowed_cidrs=["10.0.0.0/8"],
            connection_limit=100000,
            default_pool_id="00000000-0000-4000-8000-000000000000",
            insert_x_forwarded=False,
            secret_id="f2e734d0-fa2b-42c2-ad33-4c6db5101e00",
            sni_secret_id=["f2e734d0-fa2b-42c2-ad33-4c6db5101e00", "eb121225-7ded-4ff3-ae1f-599e145dd7cb"],
            timeout_client_data=50000,
            timeout_member_connect=50000,
            timeout_member_data=None,
            user_list=[
                {
                    "encrypted_password": "$5$isRr.HJ1IrQP38.m$oViu3DJOpUG2ZsjCBtbITV3mqpxxbZfyWJojLPNSPO5",
                    "username": "admin",
                }
            ],
        )
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.listeners.with_raw_response.create(
            project_id=1,
            region_id=1,
            load_balancer_id="30f4f55b-4a7c-48e0-9954-5cddfee216e7",
            name="my_listener",
            protocol="HTTP",
            protocol_port=80,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listener = await response.parse()
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.listeners.with_streaming_response.create(
            project_id=1,
            region_id=1,
            load_balancer_id="30f4f55b-4a7c-48e0-9954-5cddfee216e7",
            name="my_listener",
            protocol="HTTP",
            protocol_port=80,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listener = await response.parse()
            assert_matches_type(TaskIDList, listener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        listener = await async_client.cloud.load_balancers.listeners.update(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        listener = await async_client.cloud.load_balancers.listeners.update(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            allowed_cidrs=["10.0.0.0/8"],
            connection_limit=100000,
            name="new_listener_name",
            secret_id="af4a64e7-03ca-470f-9a09-b77d54c5abd8",
            sni_secret_id=["af4a64e7-03ca-470f-9a09-b77d54c5abd8", "12b43d95-d420-4c79-a883-49bf146cbdff"],
            timeout_client_data=50000,
            timeout_member_connect=50000,
            timeout_member_data=None,
            user_list=[
                {
                    "encrypted_password": "$5$isRr.HJ1IrQP38.m$oViu3DJOpUG2ZsjCBtbITV3mqpxxbZfyWJojLPNSPO5",
                    "username": "admin",
                }
            ],
        )
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.listeners.with_raw_response.update(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listener = await response.parse()
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.listeners.with_streaming_response.update(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listener = await response.parse()
            assert_matches_type(TaskIDList, listener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `listener_id` but received ''"):
            await async_client.cloud.load_balancers.listeners.with_raw_response.update(
                listener_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        listener = await async_client.cloud.load_balancers.listeners.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerListenerList, listener, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        listener = await async_client.cloud.load_balancers.listeners.list(
            project_id=1,
            region_id=1,
            load_balancer_id="00000000-0000-4000-8000-000000000000",
            show_stats=True,
        )
        assert_matches_type(LoadBalancerListenerList, listener, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.listeners.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listener = await response.parse()
        assert_matches_type(LoadBalancerListenerList, listener, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.listeners.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listener = await response.parse()
            assert_matches_type(LoadBalancerListenerList, listener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        listener = await async_client.cloud.load_balancers.listeners.delete(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        listener = await async_client.cloud.load_balancers.listeners.delete(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            delete_default_pool=False,
        )
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.listeners.with_raw_response.delete(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listener = await response.parse()
        assert_matches_type(TaskIDList, listener, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.listeners.with_streaming_response.delete(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listener = await response.parse()
            assert_matches_type(TaskIDList, listener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `listener_id` but received ''"):
            await async_client.cloud.load_balancers.listeners.with_raw_response.delete(
                listener_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        listener = await async_client.cloud.load_balancers.listeners.get(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerListenerDetail, listener, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncGcore) -> None:
        listener = await async_client.cloud.load_balancers.listeners.get(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            show_stats=True,
        )
        assert_matches_type(LoadBalancerListenerDetail, listener, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.listeners.with_raw_response.get(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listener = await response.parse()
        assert_matches_type(LoadBalancerListenerDetail, listener, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.listeners.with_streaming_response.get(
            listener_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listener = await response.parse()
            assert_matches_type(LoadBalancerListenerDetail, listener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `listener_id` but received ''"):
            await async_client.cloud.load_balancers.listeners.with_raw_response.get(
                listener_id="",
                project_id=1,
                region_id=1,
            )

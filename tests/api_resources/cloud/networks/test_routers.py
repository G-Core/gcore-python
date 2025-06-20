# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import TaskIDList
from gcore.types.cloud.networks import (
    Router,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRouters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        router = client.cloud.networks.routers.create(
            project_id=0,
            region_id=0,
            name="my_wonderful_router",
        )
        assert_matches_type(TaskIDList, router, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        router = client.cloud.networks.routers.create(
            project_id=0,
            region_id=0,
            name="my_wonderful_router",
            external_gateway_info={
                "enable_snat": True,
                "type": "default",
            },
            interfaces=[
                {
                    "subnet_id": "3ed9e2ce-f906-47fb-ba32-c25a3f63df4f",
                    "type": "subnet",
                }
            ],
            routes=[
                {
                    "destination": "10.0.3.0/24",
                    "nexthop": "10.0.0.13",
                }
            ],
        )
        assert_matches_type(TaskIDList, router, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.networks.routers.with_raw_response.create(
            project_id=0,
            region_id=0,
            name="my_wonderful_router",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = response.parse()
        assert_matches_type(TaskIDList, router, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.networks.routers.with_streaming_response.create(
            project_id=0,
            region_id=0,
            name="my_wonderful_router",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = response.parse()
            assert_matches_type(TaskIDList, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        router = client.cloud.networks.routers.update(
            router_id="router_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        router = client.cloud.networks.routers.update(
            router_id="router_id",
            project_id=0,
            region_id=0,
            external_gateway_info={
                "network_id": "d7745dcf-b302-4795-9d61-6cc52487af48",
                "enable_snat": False,
                "type": "manual",
            },
            name="my_renamed_router",
            routes=[
                {
                    "destination": "10.0.3.0/24",
                    "nexthop": "10.0.0.13",
                }
            ],
        )
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.networks.routers.with_raw_response.update(
            router_id="router_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = response.parse()
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.networks.routers.with_streaming_response.update(
            router_id="router_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = response.parse()
            assert_matches_type(Router, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `router_id` but received ''"):
            client.cloud.networks.routers.with_raw_response.update(
                router_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        router = client.cloud.networks.routers.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SyncOffsetPage[Router], router, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        router = client.cloud.networks.routers.list(
            project_id=0,
            region_id=0,
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[Router], router, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.networks.routers.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = response.parse()
        assert_matches_type(SyncOffsetPage[Router], router, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.networks.routers.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = response.parse()
            assert_matches_type(SyncOffsetPage[Router], router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        router = client.cloud.networks.routers.delete(
            router_id="router_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, router, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.networks.routers.with_raw_response.delete(
            router_id="router_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = response.parse()
        assert_matches_type(TaskIDList, router, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.networks.routers.with_streaming_response.delete(
            router_id="router_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = response.parse()
            assert_matches_type(TaskIDList, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `router_id` but received ''"):
            client.cloud.networks.routers.with_raw_response.delete(
                router_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_attach_subnet(self, client: Gcore) -> None:
        router = client.cloud.networks.routers.attach_subnet(
            router_id="ccd5b925-e35c-4611-a511-67ab503104c8",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
        )
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    def test_method_attach_subnet_with_all_params(self, client: Gcore) -> None:
        router = client.cloud.networks.routers.attach_subnet(
            router_id="ccd5b925-e35c-4611-a511-67ab503104c8",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
            ip_address="ip_address",
        )
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    def test_raw_response_attach_subnet(self, client: Gcore) -> None:
        response = client.cloud.networks.routers.with_raw_response.attach_subnet(
            router_id="ccd5b925-e35c-4611-a511-67ab503104c8",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = response.parse()
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    def test_streaming_response_attach_subnet(self, client: Gcore) -> None:
        with client.cloud.networks.routers.with_streaming_response.attach_subnet(
            router_id="ccd5b925-e35c-4611-a511-67ab503104c8",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = response.parse()
            assert_matches_type(Router, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_attach_subnet(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `router_id` but received ''"):
            client.cloud.networks.routers.with_raw_response.attach_subnet(
                router_id="",
                project_id=1,
                region_id=1,
                subnet_id="subnet_id",
            )

    @parametrize
    def test_method_detach_subnet(self, client: Gcore) -> None:
        router = client.cloud.networks.routers.detach_subnet(
            router_id="router_id",
            project_id=0,
            region_id=0,
            subnet_id="subnet_id",
        )
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    def test_raw_response_detach_subnet(self, client: Gcore) -> None:
        response = client.cloud.networks.routers.with_raw_response.detach_subnet(
            router_id="router_id",
            project_id=0,
            region_id=0,
            subnet_id="subnet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = response.parse()
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    def test_streaming_response_detach_subnet(self, client: Gcore) -> None:
        with client.cloud.networks.routers.with_streaming_response.detach_subnet(
            router_id="router_id",
            project_id=0,
            region_id=0,
            subnet_id="subnet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = response.parse()
            assert_matches_type(Router, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_detach_subnet(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `router_id` but received ''"):
            client.cloud.networks.routers.with_raw_response.detach_subnet(
                router_id="",
                project_id=0,
                region_id=0,
                subnet_id="subnet_id",
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        router = client.cloud.networks.routers.get(
            router_id="router_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.networks.routers.with_raw_response.get(
            router_id="router_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = response.parse()
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.networks.routers.with_streaming_response.get(
            router_id="router_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = response.parse()
            assert_matches_type(Router, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `router_id` but received ''"):
            client.cloud.networks.routers.with_raw_response.get(
                router_id="",
                project_id=0,
                region_id=0,
            )


class TestAsyncRouters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        router = await async_client.cloud.networks.routers.create(
            project_id=0,
            region_id=0,
            name="my_wonderful_router",
        )
        assert_matches_type(TaskIDList, router, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        router = await async_client.cloud.networks.routers.create(
            project_id=0,
            region_id=0,
            name="my_wonderful_router",
            external_gateway_info={
                "enable_snat": True,
                "type": "default",
            },
            interfaces=[
                {
                    "subnet_id": "3ed9e2ce-f906-47fb-ba32-c25a3f63df4f",
                    "type": "subnet",
                }
            ],
            routes=[
                {
                    "destination": "10.0.3.0/24",
                    "nexthop": "10.0.0.13",
                }
            ],
        )
        assert_matches_type(TaskIDList, router, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.routers.with_raw_response.create(
            project_id=0,
            region_id=0,
            name="my_wonderful_router",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = await response.parse()
        assert_matches_type(TaskIDList, router, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.routers.with_streaming_response.create(
            project_id=0,
            region_id=0,
            name="my_wonderful_router",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = await response.parse()
            assert_matches_type(TaskIDList, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        router = await async_client.cloud.networks.routers.update(
            router_id="router_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        router = await async_client.cloud.networks.routers.update(
            router_id="router_id",
            project_id=0,
            region_id=0,
            external_gateway_info={
                "network_id": "d7745dcf-b302-4795-9d61-6cc52487af48",
                "enable_snat": False,
                "type": "manual",
            },
            name="my_renamed_router",
            routes=[
                {
                    "destination": "10.0.3.0/24",
                    "nexthop": "10.0.0.13",
                }
            ],
        )
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.routers.with_raw_response.update(
            router_id="router_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = await response.parse()
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.routers.with_streaming_response.update(
            router_id="router_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = await response.parse()
            assert_matches_type(Router, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `router_id` but received ''"):
            await async_client.cloud.networks.routers.with_raw_response.update(
                router_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        router = await async_client.cloud.networks.routers.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(AsyncOffsetPage[Router], router, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        router = await async_client.cloud.networks.routers.list(
            project_id=0,
            region_id=0,
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[Router], router, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.routers.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = await response.parse()
        assert_matches_type(AsyncOffsetPage[Router], router, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.routers.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = await response.parse()
            assert_matches_type(AsyncOffsetPage[Router], router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        router = await async_client.cloud.networks.routers.delete(
            router_id="router_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, router, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.routers.with_raw_response.delete(
            router_id="router_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = await response.parse()
        assert_matches_type(TaskIDList, router, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.routers.with_streaming_response.delete(
            router_id="router_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = await response.parse()
            assert_matches_type(TaskIDList, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `router_id` but received ''"):
            await async_client.cloud.networks.routers.with_raw_response.delete(
                router_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_attach_subnet(self, async_client: AsyncGcore) -> None:
        router = await async_client.cloud.networks.routers.attach_subnet(
            router_id="ccd5b925-e35c-4611-a511-67ab503104c8",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
        )
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    async def test_method_attach_subnet_with_all_params(self, async_client: AsyncGcore) -> None:
        router = await async_client.cloud.networks.routers.attach_subnet(
            router_id="ccd5b925-e35c-4611-a511-67ab503104c8",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
            ip_address="ip_address",
        )
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    async def test_raw_response_attach_subnet(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.routers.with_raw_response.attach_subnet(
            router_id="ccd5b925-e35c-4611-a511-67ab503104c8",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = await response.parse()
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    async def test_streaming_response_attach_subnet(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.routers.with_streaming_response.attach_subnet(
            router_id="ccd5b925-e35c-4611-a511-67ab503104c8",
            project_id=1,
            region_id=1,
            subnet_id="subnet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = await response.parse()
            assert_matches_type(Router, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_attach_subnet(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `router_id` but received ''"):
            await async_client.cloud.networks.routers.with_raw_response.attach_subnet(
                router_id="",
                project_id=1,
                region_id=1,
                subnet_id="subnet_id",
            )

    @parametrize
    async def test_method_detach_subnet(self, async_client: AsyncGcore) -> None:
        router = await async_client.cloud.networks.routers.detach_subnet(
            router_id="router_id",
            project_id=0,
            region_id=0,
            subnet_id="subnet_id",
        )
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    async def test_raw_response_detach_subnet(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.routers.with_raw_response.detach_subnet(
            router_id="router_id",
            project_id=0,
            region_id=0,
            subnet_id="subnet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = await response.parse()
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    async def test_streaming_response_detach_subnet(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.routers.with_streaming_response.detach_subnet(
            router_id="router_id",
            project_id=0,
            region_id=0,
            subnet_id="subnet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = await response.parse()
            assert_matches_type(Router, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_detach_subnet(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `router_id` but received ''"):
            await async_client.cloud.networks.routers.with_raw_response.detach_subnet(
                router_id="",
                project_id=0,
                region_id=0,
                subnet_id="subnet_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        router = await async_client.cloud.networks.routers.get(
            router_id="router_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.routers.with_raw_response.get(
            router_id="router_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        router = await response.parse()
        assert_matches_type(Router, router, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.routers.with_streaming_response.get(
            router_id="router_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            router = await response.parse()
            assert_matches_type(Router, router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `router_id` but received ''"):
            await async_client.cloud.networks.routers.with_raw_response.get(
                router_id="",
                project_id=0,
                region_id=0,
            )

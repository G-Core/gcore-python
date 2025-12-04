# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import TaskIDList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        member = client.cloud.load_balancers.pools.members.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            address="192.168.40.33",
            protocol_port=80,
        )
        assert_matches_type(TaskIDList, member, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        member = client.cloud.load_balancers.pools.members.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            address="192.168.40.33",
            protocol_port=80,
            admin_state_up=True,
            backup=True,
            instance_id="a7e7e8d6-0bf7-4ac9-8170-831b47ee2ba9",
            monitor_address="monitor_address",
            monitor_port=0,
            subnet_id="32283b0b-b560-4690-810c-f672cbb2e28d",
            weight=1,
        )
        assert_matches_type(TaskIDList, member, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.pools.members.with_raw_response.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            address="192.168.40.33",
            protocol_port=80,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(TaskIDList, member, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.load_balancers.pools.members.with_streaming_response.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            address="192.168.40.33",
            protocol_port=80,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(TaskIDList, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.cloud.load_balancers.pools.members.with_raw_response.create(
                pool_id="",
                project_id=1,
                region_id=1,
                address="192.168.40.33",
                protocol_port=80,
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        member = client.cloud.load_balancers.pools.members.delete(
            member_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            pool_id="00000000-0000-4000-8000-000000000000",
        )
        assert_matches_type(TaskIDList, member, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.pools.members.with_raw_response.delete(
            member_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            pool_id="00000000-0000-4000-8000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(TaskIDList, member, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.load_balancers.pools.members.with_streaming_response.delete(
            member_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            pool_id="00000000-0000-4000-8000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(TaskIDList, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.cloud.load_balancers.pools.members.with_raw_response.delete(
                member_id="00000000-0000-4000-8000-000000000000",
                project_id=1,
                region_id=1,
                pool_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.cloud.load_balancers.pools.members.with_raw_response.delete(
                member_id="",
                project_id=1,
                region_id=1,
                pool_id="00000000-0000-4000-8000-000000000000",
            )


class TestAsyncMembers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        member = await async_client.cloud.load_balancers.pools.members.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            address="192.168.40.33",
            protocol_port=80,
        )
        assert_matches_type(TaskIDList, member, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        member = await async_client.cloud.load_balancers.pools.members.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            address="192.168.40.33",
            protocol_port=80,
            admin_state_up=True,
            backup=True,
            instance_id="a7e7e8d6-0bf7-4ac9-8170-831b47ee2ba9",
            monitor_address="monitor_address",
            monitor_port=0,
            subnet_id="32283b0b-b560-4690-810c-f672cbb2e28d",
            weight=1,
        )
        assert_matches_type(TaskIDList, member, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.pools.members.with_raw_response.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            address="192.168.40.33",
            protocol_port=80,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(TaskIDList, member, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.pools.members.with_streaming_response.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            address="192.168.40.33",
            protocol_port=80,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(TaskIDList, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.cloud.load_balancers.pools.members.with_raw_response.create(
                pool_id="",
                project_id=1,
                region_id=1,
                address="192.168.40.33",
                protocol_port=80,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        member = await async_client.cloud.load_balancers.pools.members.delete(
            member_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            pool_id="00000000-0000-4000-8000-000000000000",
        )
        assert_matches_type(TaskIDList, member, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.pools.members.with_raw_response.delete(
            member_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            pool_id="00000000-0000-4000-8000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(TaskIDList, member, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.pools.members.with_streaming_response.delete(
            member_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            pool_id="00000000-0000-4000-8000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(TaskIDList, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.cloud.load_balancers.pools.members.with_raw_response.delete(
                member_id="00000000-0000-4000-8000-000000000000",
                project_id=1,
                region_id=1,
                pool_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.cloud.load_balancers.pools.members.with_raw_response.delete(
                member_id="",
                project_id=1,
                region_id=1,
                pool_id="00000000-0000-4000-8000-000000000000",
            )

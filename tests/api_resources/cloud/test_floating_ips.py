# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import (
    FloatingIP,
    TaskIDList,
    FloatingIPDetailed,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFloatingIPs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        floating_ip = client.cloud.floating_ips.create(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, floating_ip, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        floating_ip = client.cloud.floating_ips.create(
            project_id=1,
            region_id=1,
            fixed_ip_address="192.168.10.15",
            port_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, floating_ip, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.floating_ips.with_raw_response.create(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = response.parse()
        assert_matches_type(TaskIDList, floating_ip, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.floating_ips.with_streaming_response.create(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = response.parse()
            assert_matches_type(TaskIDList, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        floating_ip = client.cloud.floating_ips.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(SyncOffsetPage[FloatingIPDetailed], floating_ip, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        floating_ip = client.cloud.floating_ips.list(
            project_id=1,
            region_id=1,
            limit=1000,
            offset=0,
            tag_key=["key1", "key2"],
            tag_key_value="tag_key_value",
        )
        assert_matches_type(SyncOffsetPage[FloatingIPDetailed], floating_ip, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.floating_ips.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = response.parse()
        assert_matches_type(SyncOffsetPage[FloatingIPDetailed], floating_ip, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.floating_ips.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = response.parse()
            assert_matches_type(SyncOffsetPage[FloatingIPDetailed], floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        floating_ip = client.cloud.floating_ips.delete(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, floating_ip, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.floating_ips.with_raw_response.delete(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = response.parse()
        assert_matches_type(TaskIDList, floating_ip, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.floating_ips.with_streaming_response.delete(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = response.parse()
            assert_matches_type(TaskIDList, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip_id` but received ''"):
            client.cloud.floating_ips.with_raw_response.delete(
                floating_ip_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_assign(self, client: Gcore) -> None:
        floating_ip = client.cloud.floating_ips.assign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
            port_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
        )
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    def test_method_assign_with_all_params(self, client: Gcore) -> None:
        floating_ip = client.cloud.floating_ips.assign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
            port_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
            fixed_ip_address="192.168.10.15",
        )
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    def test_raw_response_assign(self, client: Gcore) -> None:
        response = client.cloud.floating_ips.with_raw_response.assign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
            port_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = response.parse()
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    def test_streaming_response_assign(self, client: Gcore) -> None:
        with client.cloud.floating_ips.with_streaming_response.assign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
            port_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = response.parse()
            assert_matches_type(FloatingIP, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_assign(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip_id` but received ''"):
            client.cloud.floating_ips.with_raw_response.assign(
                floating_ip_id="",
                project_id=0,
                region_id=0,
                port_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        floating_ip = client.cloud.floating_ips.get(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.floating_ips.with_raw_response.get(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = response.parse()
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.floating_ips.with_streaming_response.get(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = response.parse()
            assert_matches_type(FloatingIP, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip_id` but received ''"):
            client.cloud.floating_ips.with_raw_response.get(
                floating_ip_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_unassign(self, client: Gcore) -> None:
        floating_ip = client.cloud.floating_ips.unassign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    def test_raw_response_unassign(self, client: Gcore) -> None:
        response = client.cloud.floating_ips.with_raw_response.unassign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = response.parse()
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    def test_streaming_response_unassign(self, client: Gcore) -> None:
        with client.cloud.floating_ips.with_streaming_response.unassign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = response.parse()
            assert_matches_type(FloatingIP, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unassign(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip_id` but received ''"):
            client.cloud.floating_ips.with_raw_response.unassign(
                floating_ip_id="",
                project_id=0,
                region_id=0,
            )


class TestAsyncFloatingIPs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        floating_ip = await async_client.cloud.floating_ips.create(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, floating_ip, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        floating_ip = await async_client.cloud.floating_ips.create(
            project_id=1,
            region_id=1,
            fixed_ip_address="192.168.10.15",
            port_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, floating_ip, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.floating_ips.with_raw_response.create(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = await response.parse()
        assert_matches_type(TaskIDList, floating_ip, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.floating_ips.with_streaming_response.create(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = await response.parse()
            assert_matches_type(TaskIDList, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        floating_ip = await async_client.cloud.floating_ips.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(AsyncOffsetPage[FloatingIPDetailed], floating_ip, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        floating_ip = await async_client.cloud.floating_ips.list(
            project_id=1,
            region_id=1,
            limit=1000,
            offset=0,
            tag_key=["key1", "key2"],
            tag_key_value="tag_key_value",
        )
        assert_matches_type(AsyncOffsetPage[FloatingIPDetailed], floating_ip, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.floating_ips.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = await response.parse()
        assert_matches_type(AsyncOffsetPage[FloatingIPDetailed], floating_ip, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.floating_ips.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = await response.parse()
            assert_matches_type(AsyncOffsetPage[FloatingIPDetailed], floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        floating_ip = await async_client.cloud.floating_ips.delete(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, floating_ip, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.floating_ips.with_raw_response.delete(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = await response.parse()
        assert_matches_type(TaskIDList, floating_ip, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.floating_ips.with_streaming_response.delete(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = await response.parse()
            assert_matches_type(TaskIDList, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip_id` but received ''"):
            await async_client.cloud.floating_ips.with_raw_response.delete(
                floating_ip_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_assign(self, async_client: AsyncGcore) -> None:
        floating_ip = await async_client.cloud.floating_ips.assign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
            port_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
        )
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    async def test_method_assign_with_all_params(self, async_client: AsyncGcore) -> None:
        floating_ip = await async_client.cloud.floating_ips.assign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
            port_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
            fixed_ip_address="192.168.10.15",
        )
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    async def test_raw_response_assign(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.floating_ips.with_raw_response.assign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
            port_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = await response.parse()
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    async def test_streaming_response_assign(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.floating_ips.with_streaming_response.assign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
            port_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = await response.parse()
            assert_matches_type(FloatingIP, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_assign(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip_id` but received ''"):
            await async_client.cloud.floating_ips.with_raw_response.assign(
                floating_ip_id="",
                project_id=0,
                region_id=0,
                port_id="ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        floating_ip = await async_client.cloud.floating_ips.get(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.floating_ips.with_raw_response.get(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = await response.parse()
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.floating_ips.with_streaming_response.get(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = await response.parse()
            assert_matches_type(FloatingIP, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip_id` but received ''"):
            await async_client.cloud.floating_ips.with_raw_response.get(
                floating_ip_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_unassign(self, async_client: AsyncGcore) -> None:
        floating_ip = await async_client.cloud.floating_ips.unassign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    async def test_raw_response_unassign(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.floating_ips.with_raw_response.unassign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = await response.parse()
        assert_matches_type(FloatingIP, floating_ip, path=["response"])

    @parametrize
    async def test_streaming_response_unassign(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.floating_ips.with_streaming_response.unassign(
            floating_ip_id="floating_ip_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = await response.parse()
            assert_matches_type(FloatingIP, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unassign(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip_id` but received ''"):
            await async_client.cloud.floating_ips.with_raw_response.unassign(
                floating_ip_id="",
                project_id=0,
                region_id=0,
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import TaskIDList
from gcore.types.cloud.baremetal import BaremetalServer

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.create(
            project_id=1,
            region_id=1,
            flavor="bm2-hf-medium",
            interfaces=[{"type": "external"}],
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.create(
            project_id=1,
            region_id=1,
            flavor="bm2-hf-medium",
            interfaces=[
                {
                    "type": "external",
                    "interface_name": "eth0",
                    "ip_family": "ipv4",
                    "port_group": 0,
                }
            ],
            app_config={},
            apptemplate_id="apptemplate_id",
            ddos_profile={
                "profile_template": 123,
                "fields": [
                    {
                        "base_field": 10,
                        "field_name": "field_name",
                        "field_value": [45046, 45047],
                        "value": "value",
                    }
                ],
            },
            image_id="image_id",
            name="my-bare-metal",
            name_template="name_template",
            password="password",
            ssh_key_name="my-ssh-key",
            tags={"my-tag": "my-tag-value"},
            user_data="user_data",
            username="username",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.baremetal.servers.with_raw_response.create(
            project_id=1,
            region_id=1,
            flavor="bm2-hf-medium",
            interfaces=[{"type": "external"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.baremetal.servers.with_streaming_response.create(
            project_id=1,
            region_id=1,
            flavor="bm2-hf-medium",
            interfaces=[{"type": "external"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(SyncOffsetPage[BaremetalServer], server, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.list(
            project_id=1,
            region_id=1,
            changes_before=parse_datetime("2025-10-01T12:00:00Z"),
            changes_since=parse_datetime("2025-10-01T12:00:00Z"),
            flavor_id="bm2-hf-small",
            flavor_prefix="bm2-",
            include_k8s=True,
            ip="192.168.0.1",
            limit=1000,
            name="name",
            offset=0,
            only_isolated=True,
            only_with_fixed_external_ip=True,
            order_by="name.asc",
            profile_name="profile_name",
            protection_status="Active",
            status="ACTIVE",
            tag_key_value="tag_key_value",
            tag_value=["value1", "value2"],
            type_ddos_profile="advanced",
            uuid="b5b4d65d-945f-4b98-ab6f-332319c724ef",
            with_ddos=True,
            with_interfaces_name=True,
        )
        assert_matches_type(SyncOffsetPage[BaremetalServer], server, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.baremetal.servers.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(SyncOffsetPage[BaremetalServer], server, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.baremetal.servers.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(SyncOffsetPage[BaremetalServer], server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_rebuild(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.rebuild(
            server_id="server_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_method_rebuild_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.rebuild(
            server_id="server_id",
            project_id=0,
            region_id=0,
            image_id="b5b4d65d-945f-4b98-ab6f-332319c724ef",
            user_data="aGVsbG9fd29ybGQ=",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_rebuild(self, client: Gcore) -> None:
        response = client.cloud.baremetal.servers.with_raw_response.rebuild(
            server_id="server_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_rebuild(self, client: Gcore) -> None:
        with client.cloud.baremetal.servers.with_streaming_response.rebuild(
            server_id="server_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rebuild(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.cloud.baremetal.servers.with_raw_response.rebuild(
                server_id="",
                project_id=0,
                region_id=0,
            )


class TestAsyncServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.create(
            project_id=1,
            region_id=1,
            flavor="bm2-hf-medium",
            interfaces=[{"type": "external"}],
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.create(
            project_id=1,
            region_id=1,
            flavor="bm2-hf-medium",
            interfaces=[
                {
                    "type": "external",
                    "interface_name": "eth0",
                    "ip_family": "ipv4",
                    "port_group": 0,
                }
            ],
            app_config={},
            apptemplate_id="apptemplate_id",
            ddos_profile={
                "profile_template": 123,
                "fields": [
                    {
                        "base_field": 10,
                        "field_name": "field_name",
                        "field_value": [45046, 45047],
                        "value": "value",
                    }
                ],
            },
            image_id="image_id",
            name="my-bare-metal",
            name_template="name_template",
            password="password",
            ssh_key_name="my-ssh-key",
            tags={"my-tag": "my-tag-value"},
            user_data="user_data",
            username="username",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.baremetal.servers.with_raw_response.create(
            project_id=1,
            region_id=1,
            flavor="bm2-hf-medium",
            interfaces=[{"type": "external"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.baremetal.servers.with_streaming_response.create(
            project_id=1,
            region_id=1,
            flavor="bm2-hf-medium",
            interfaces=[{"type": "external"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(AsyncOffsetPage[BaremetalServer], server, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.list(
            project_id=1,
            region_id=1,
            changes_before=parse_datetime("2025-10-01T12:00:00Z"),
            changes_since=parse_datetime("2025-10-01T12:00:00Z"),
            flavor_id="bm2-hf-small",
            flavor_prefix="bm2-",
            include_k8s=True,
            ip="192.168.0.1",
            limit=1000,
            name="name",
            offset=0,
            only_isolated=True,
            only_with_fixed_external_ip=True,
            order_by="name.asc",
            profile_name="profile_name",
            protection_status="Active",
            status="ACTIVE",
            tag_key_value="tag_key_value",
            tag_value=["value1", "value2"],
            type_ddos_profile="advanced",
            uuid="b5b4d65d-945f-4b98-ab6f-332319c724ef",
            with_ddos=True,
            with_interfaces_name=True,
        )
        assert_matches_type(AsyncOffsetPage[BaremetalServer], server, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.baremetal.servers.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(AsyncOffsetPage[BaremetalServer], server, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.baremetal.servers.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(AsyncOffsetPage[BaremetalServer], server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_rebuild(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.rebuild(
            server_id="server_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_method_rebuild_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.rebuild(
            server_id="server_id",
            project_id=0,
            region_id=0,
            image_id="b5b4d65d-945f-4b98-ab6f-332319c724ef",
            user_data="aGVsbG9fd29ybGQ=",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_rebuild(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.baremetal.servers.with_raw_response.rebuild(
            server_id="server_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_rebuild(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.baremetal.servers.with_streaming_response.rebuild(
            server_id="server_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rebuild(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.cloud.baremetal.servers.with_raw_response.rebuild(
                server_id="",
                project_id=0,
                region_id=0,
            )

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
from gcore.types.cloud.baremetal import (
    BaremetalServer,
    ServerDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.create(
            project_id=1,
            flavor_name="bm2-hf-medium",
            image_id="2fa8c5b1-1234-4abc-9def-0123456789ab",
            interfaces=[{"port_id": "75757793-5e33-4eed-ab5d-9ed5030e57f7"}],
            region_id=7,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.create(
            project_id=1,
            flavor_name="bm2-hf-medium",
            image_id="2fa8c5b1-1234-4abc-9def-0123456789ab",
            interfaces=[
                {
                    "port_id": "75757793-5e33-4eed-ab5d-9ed5030e57f7",
                    "port_group": 0,
                }
            ],
            region_id=7,
            dry_run=True,
            name="bm-1",
            password="x",
            ssh_key_id="21b3c2d5-efe8-4367-99ff-86e1e060d27f",
            tags={"my-tag": "my-tag-value"},
            user_data="x",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.baremetal.servers.with_raw_response.create(
            project_id=1,
            flavor_name="bm2-hf-medium",
            image_id="2fa8c5b1-1234-4abc-9def-0123456789ab",
            interfaces=[{"port_id": "75757793-5e33-4eed-ab5d-9ed5030e57f7"}],
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.baremetal.servers.with_streaming_response.create(
            project_id=1,
            flavor_name="bm2-hf-medium",
            image_id="2fa8c5b1-1234-4abc-9def-0123456789ab",
            interfaces=[{"port_id": "75757793-5e33-4eed-ab5d-9ed5030e57f7"}],
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.update(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.update(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            dry_run=True,
            interfaces=[
                {
                    "port_id": "port_id",
                    "port_group": 0,
                }
            ],
            name="bm-1",
            tags={
                "my-tag": "my-tag-value",
                "my-tag-to-remove": None,
            },
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.baremetal.servers.with_raw_response.update(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.baremetal.servers.with_streaming_response.update(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.cloud.baremetal.servers.with_raw_response.update(
                server_id="",
                project_id=1,
            )

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.list(
            project_id=1,
        )
        assert_matches_type(SyncOffsetPage[BaremetalServer], server, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.list(
            project_id=1,
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            flavor_name={
                "contains": ["string"],
                "exact": ["string"],
                "prefix": ["string"],
                "suffix": ["string"],
            },
            ids=["string"],
            ip_address={
                "contains": ["string"],
                "exact": ["string"],
            },
            limit=1,
            managed=True,
            managed_by="k8s_cluster",
            managed_by_resource_ids=["string"],
            managed_by_resource_names=["string"],
            name={
                "contains": ["string"],
                "exact": ["string"],
                "prefix": ["string"],
                "suffix": ["string"],
            },
            network_ids=["string"],
            offset=0,
            order_by="created_at.asc",
            region_ids=[0],
            statuses=["active"],
            subnet_ids=["string"],
            tag_key={
                "contains": ["string"],
                "exact": ["string"],
                "prefix": ["string"],
                "suffix": ["string"],
            },
            tag_value={
                "contains": ["string"],
                "exact": ["string"],
                "prefix": ["string"],
                "suffix": ["string"],
            },
            tags={"env": ["prod"]},
            updated_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(SyncOffsetPage[BaremetalServer], server, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.baremetal.servers.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(SyncOffsetPage[BaremetalServer], server, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.baremetal.servers.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(SyncOffsetPage[BaremetalServer], server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.delete(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.delete(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            all_floating_ips=True,
            all_ports=True,
            dry_run=True,
            floating_ip_ids=["string"],
            port_ids=["string"],
        )
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.baremetal.servers.with_raw_response.delete(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.baremetal.servers.with_streaming_response.delete(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerDeleteResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.cloud.baremetal.servers.with_raw_response.delete(
                server_id="",
                project_id=1,
            )

    @parametrize
    def test_method_action(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.action(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_method_action_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.action(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
            dry_run=True,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_action(self, client: Gcore) -> None:
        response = client.cloud.baremetal.servers.with_raw_response.action(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_action(self, client: Gcore) -> None:
        with client.cloud.baremetal.servers.with_streaming_response.action(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_action(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.cloud.baremetal.servers.with_raw_response.action(
                server_id="",
                project_id=1,
                action="stop",
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.get(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(BaremetalServer, server, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.baremetal.servers.with_raw_response.get(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(BaremetalServer, server, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.baremetal.servers.with_streaming_response.get(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(BaremetalServer, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.cloud.baremetal.servers.with_raw_response.get(
                server_id="",
                project_id=1,
            )

    @parametrize
    def test_method_rebuild(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.rebuild(
            server_id="024a29e-b4b7-4c91-9a46-505be123d9f8",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_method_rebuild_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.baremetal.servers.rebuild(
            server_id="024a29e-b4b7-4c91-9a46-505be123d9f8",
            project_id=1,
            region_id=1,
            image_id="b5b4d65d-945f-4b98-ab6f-332319c724ef",
            user_data="aGVsbG9fd29ybGQ=",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_rebuild(self, client: Gcore) -> None:
        response = client.cloud.baremetal.servers.with_raw_response.rebuild(
            server_id="024a29e-b4b7-4c91-9a46-505be123d9f8",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_rebuild(self, client: Gcore) -> None:
        with client.cloud.baremetal.servers.with_streaming_response.rebuild(
            server_id="024a29e-b4b7-4c91-9a46-505be123d9f8",
            project_id=1,
            region_id=1,
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
                project_id=1,
                region_id=1,
            )


class TestAsyncServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.create(
            project_id=1,
            flavor_name="bm2-hf-medium",
            image_id="2fa8c5b1-1234-4abc-9def-0123456789ab",
            interfaces=[{"port_id": "75757793-5e33-4eed-ab5d-9ed5030e57f7"}],
            region_id=7,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.create(
            project_id=1,
            flavor_name="bm2-hf-medium",
            image_id="2fa8c5b1-1234-4abc-9def-0123456789ab",
            interfaces=[
                {
                    "port_id": "75757793-5e33-4eed-ab5d-9ed5030e57f7",
                    "port_group": 0,
                }
            ],
            region_id=7,
            dry_run=True,
            name="bm-1",
            password="x",
            ssh_key_id="21b3c2d5-efe8-4367-99ff-86e1e060d27f",
            tags={"my-tag": "my-tag-value"},
            user_data="x",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.baremetal.servers.with_raw_response.create(
            project_id=1,
            flavor_name="bm2-hf-medium",
            image_id="2fa8c5b1-1234-4abc-9def-0123456789ab",
            interfaces=[{"port_id": "75757793-5e33-4eed-ab5d-9ed5030e57f7"}],
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.baremetal.servers.with_streaming_response.create(
            project_id=1,
            flavor_name="bm2-hf-medium",
            image_id="2fa8c5b1-1234-4abc-9def-0123456789ab",
            interfaces=[{"port_id": "75757793-5e33-4eed-ab5d-9ed5030e57f7"}],
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.update(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.update(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            dry_run=True,
            interfaces=[
                {
                    "port_id": "port_id",
                    "port_group": 0,
                }
            ],
            name="bm-1",
            tags={
                "my-tag": "my-tag-value",
                "my-tag-to-remove": None,
            },
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.baremetal.servers.with_raw_response.update(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.baremetal.servers.with_streaming_response.update(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.cloud.baremetal.servers.with_raw_response.update(
                server_id="",
                project_id=1,
            )

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.list(
            project_id=1,
        )
        assert_matches_type(AsyncOffsetPage[BaremetalServer], server, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.list(
            project_id=1,
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            flavor_name={
                "contains": ["string"],
                "exact": ["string"],
                "prefix": ["string"],
                "suffix": ["string"],
            },
            ids=["string"],
            ip_address={
                "contains": ["string"],
                "exact": ["string"],
            },
            limit=1,
            managed=True,
            managed_by="k8s_cluster",
            managed_by_resource_ids=["string"],
            managed_by_resource_names=["string"],
            name={
                "contains": ["string"],
                "exact": ["string"],
                "prefix": ["string"],
                "suffix": ["string"],
            },
            network_ids=["string"],
            offset=0,
            order_by="created_at.asc",
            region_ids=[0],
            statuses=["active"],
            subnet_ids=["string"],
            tag_key={
                "contains": ["string"],
                "exact": ["string"],
                "prefix": ["string"],
                "suffix": ["string"],
            },
            tag_value={
                "contains": ["string"],
                "exact": ["string"],
                "prefix": ["string"],
                "suffix": ["string"],
            },
            tags={"env": ["prod"]},
            updated_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(AsyncOffsetPage[BaremetalServer], server, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.baremetal.servers.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(AsyncOffsetPage[BaremetalServer], server, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.baremetal.servers.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(AsyncOffsetPage[BaremetalServer], server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.delete(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.delete(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            all_floating_ips=True,
            all_ports=True,
            dry_run=True,
            floating_ip_ids=["string"],
            port_ids=["string"],
        )
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.baremetal.servers.with_raw_response.delete(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.baremetal.servers.with_streaming_response.delete(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerDeleteResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.cloud.baremetal.servers.with_raw_response.delete(
                server_id="",
                project_id=1,
            )

    @parametrize
    async def test_method_action(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.action(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_method_action_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.action(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
            dry_run=True,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_action(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.baremetal.servers.with_raw_response.action(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_action(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.baremetal.servers.with_streaming_response.action(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_action(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.cloud.baremetal.servers.with_raw_response.action(
                server_id="",
                project_id=1,
                action="stop",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.get(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(BaremetalServer, server, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.baremetal.servers.with_raw_response.get(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(BaremetalServer, server, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.baremetal.servers.with_streaming_response.get(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(BaremetalServer, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.cloud.baremetal.servers.with_raw_response.get(
                server_id="",
                project_id=1,
            )

    @parametrize
    async def test_method_rebuild(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.rebuild(
            server_id="024a29e-b4b7-4c91-9a46-505be123d9f8",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_method_rebuild_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.baremetal.servers.rebuild(
            server_id="024a29e-b4b7-4c91-9a46-505be123d9f8",
            project_id=1,
            region_id=1,
            image_id="b5b4d65d-945f-4b98-ab6f-332319c724ef",
            user_data="aGVsbG9fd29ybGQ=",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_rebuild(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.baremetal.servers.with_raw_response.rebuild(
            server_id="024a29e-b4b7-4c91-9a46-505be123d9f8",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_rebuild(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.baremetal.servers.with_streaming_response.rebuild(
            server_id="024a29e-b4b7-4c91-9a46-505be123d9f8",
            project_id=1,
            region_id=1,
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
                project_id=1,
                region_id=1,
            )

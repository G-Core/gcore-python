# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import (
    Instance,
    TaskIDList,
    InstanceDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        instance = client.cloud.instances.create(
            project_id=1,
            boot_volume_id="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            flavor_name="g2-standard-32-64",
            interfaces=[{"port_id": "bbbbbbbb-cccc-dddd-eeee-ffffffffffff"}],
            region_id=7,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        instance = client.cloud.instances.create(
            project_id=1,
            boot_volume_id="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            flavor_name="g2-standard-32-64",
            interfaces=[{"port_id": "bbbbbbbb-cccc-dddd-eeee-ffffffffffff"}],
            region_id=7,
            dry_run=True,
            data_volume_ids=["string"],
            name="web-1",
            password="x",
            placement_group_id="placement_group_id",
            ssh_key_id="ssh_key_id",
            tags={"foo": "my-tag-value"},
            user_data="x",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.create(
            project_id=1,
            boot_volume_id="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            flavor_name="g2-standard-32-64",
            interfaces=[{"port_id": "bbbbbbbb-cccc-dddd-eeee-ffffffffffff"}],
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.create(
            project_id=1,
            boot_volume_id="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            flavor_name="g2-standard-32-64",
            interfaces=[{"port_id": "bbbbbbbb-cccc-dddd-eeee-ffffffffffff"}],
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        instance = client.cloud.instances.update(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        instance = client.cloud.instances.update(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            dry_run=True,
            data_volume_ids=["string"],
            flavor_name="flavor_name",
            interfaces=[{"port_id": "port_id"}],
            name="name",
            placement_group_id="placement_group_id",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.update(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.update(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.update(
                instance_id="",
                project_id=1,
            )

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        instance = client.cloud.instances.list(
            project_id=1,
        )
        assert_matches_type(SyncOffsetPage[Instance], instance, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        instance = client.cloud.instances.list(
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
            security_group_ids=["string"],
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
        assert_matches_type(SyncOffsetPage[Instance], instance, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(SyncOffsetPage[Instance], instance, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(SyncOffsetPage[Instance], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        instance = client.cloud.instances.delete(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        instance = client.cloud.instances.delete(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            all_floating_ips=True,
            all_ports=True,
            all_volumes=True,
            dry_run=True,
            floating_ip_ids=["string"],
            port_ids=["string"],
            volume_ids=["string"],
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.delete(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.delete(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.delete(
                instance_id="",
                project_id=1,
            )

    @parametrize
    def test_method_action(self, client: Gcore) -> None:
        instance = client.cloud.instances.action(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_method_action_with_all_params(self, client: Gcore) -> None:
        instance = client.cloud.instances.action(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
            dry_run=True,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_raw_response_action(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.action(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_streaming_response_action(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.action(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_action(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.action(
                instance_id="",
                project_id=1,
                action="stop",
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        instance = client.cloud.instances.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(Instance, instance, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.get(
                instance_id="",
                project_id=1,
            )

    @parametrize
    def test_method_rebuild(self, client: Gcore) -> None:
        instance = client.cloud.instances.rebuild(
            instance_id="a314d566-2772-4124-a4c4-5688ab76b928",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_method_rebuild_with_all_params(self, client: Gcore) -> None:
        instance = client.cloud.instances.rebuild(
            instance_id="a314d566-2772-4124-a4c4-5688ab76b928",
            project_id=1,
            region_id=1,
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            ssh_key_name="my-ssh-key",
            user_data="user_data",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_raw_response_rebuild(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.rebuild(
            instance_id="a314d566-2772-4124-a4c4-5688ab76b928",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_streaming_response_rebuild(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.rebuild(
            instance_id="a314d566-2772-4124-a4c4-5688ab76b928",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rebuild(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.rebuild(
                instance_id="",
                project_id=1,
                region_id=1,
            )


class TestAsyncInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.create(
            project_id=1,
            boot_volume_id="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            flavor_name="g2-standard-32-64",
            interfaces=[{"port_id": "bbbbbbbb-cccc-dddd-eeee-ffffffffffff"}],
            region_id=7,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.create(
            project_id=1,
            boot_volume_id="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            flavor_name="g2-standard-32-64",
            interfaces=[{"port_id": "bbbbbbbb-cccc-dddd-eeee-ffffffffffff"}],
            region_id=7,
            dry_run=True,
            data_volume_ids=["string"],
            name="web-1",
            password="x",
            placement_group_id="placement_group_id",
            ssh_key_id="ssh_key_id",
            tags={"foo": "my-tag-value"},
            user_data="x",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.create(
            project_id=1,
            boot_volume_id="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            flavor_name="g2-standard-32-64",
            interfaces=[{"port_id": "bbbbbbbb-cccc-dddd-eeee-ffffffffffff"}],
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.create(
            project_id=1,
            boot_volume_id="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            flavor_name="g2-standard-32-64",
            interfaces=[{"port_id": "bbbbbbbb-cccc-dddd-eeee-ffffffffffff"}],
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.update(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.update(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            dry_run=True,
            data_volume_ids=["string"],
            flavor_name="flavor_name",
            interfaces=[{"port_id": "port_id"}],
            name="name",
            placement_group_id="placement_group_id",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.update(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.update(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.update(
                instance_id="",
                project_id=1,
            )

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.list(
            project_id=1,
        )
        assert_matches_type(AsyncOffsetPage[Instance], instance, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.list(
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
            security_group_ids=["string"],
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
        assert_matches_type(AsyncOffsetPage[Instance], instance, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(AsyncOffsetPage[Instance], instance, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(AsyncOffsetPage[Instance], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.delete(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.delete(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            all_floating_ips=True,
            all_ports=True,
            all_volumes=True,
            dry_run=True,
            floating_ip_ids=["string"],
            port_ids=["string"],
            volume_ids=["string"],
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.delete(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.delete(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.delete(
                instance_id="",
                project_id=1,
            )

    @parametrize
    async def test_method_action(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.action(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_method_action_with_all_params(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.action(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
            dry_run=True,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_raw_response_action(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.action(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_streaming_response_action(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.action(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            action="stop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_action(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.action(
                instance_id="",
                project_id=1,
                action="stop",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(Instance, instance, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.get(
                instance_id="",
                project_id=1,
            )

    @parametrize
    async def test_method_rebuild(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.rebuild(
            instance_id="a314d566-2772-4124-a4c4-5688ab76b928",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_method_rebuild_with_all_params(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.rebuild(
            instance_id="a314d566-2772-4124-a4c4-5688ab76b928",
            project_id=1,
            region_id=1,
            image_id="f01fd9a0-9548-48ba-82dc-a8c8b2d6f2f1",
            ssh_key_name="my-ssh-key",
            user_data="user_data",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_raw_response_rebuild(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.rebuild(
            instance_id="a314d566-2772-4124-a4c4-5688ab76b928",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_streaming_response_rebuild(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.rebuild(
            instance_id="a314d566-2772-4124-a4c4-5688ab76b928",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rebuild(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.rebuild(
                instance_id="",
                project_id=1,
                region_id=1,
            )

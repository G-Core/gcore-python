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
    Port,
    TaskIDList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPorts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        port = client.cloud.ports.create(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        port = client.cloud.ports.create(
            project_id=1,
            region_id=1,
            dry_run=True,
            allowed_address_pairs=[{"ip_address": "192.168.123.20"}],
            ip_assignments=[
                {
                    "subnet_id": "b39792c3-3160-4356-912e-ba396c95cdcf",
                    "ip_address": "192.168.123.20",
                }
            ],
            network_id="bc688791-f1b0-44eb-97d4-07697294b1e1",
            port_security_enabled=True,
            security_group_ids=["351b0dd7-ca09-431c-be53-935db3785067"],
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.ports.with_raw_response.create(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.ports.with_streaming_response.create(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert_matches_type(TaskIDList, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        port = client.cloud.ports.update(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        )
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        port = client.cloud.ports.update(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
            allowed_address_pairs=[{"ip_address": "192.168.123.20"}, {"ip_address": "192.168.0.0/17"}],
            ip_assignments=[
                {
                    "subnet_id": "b39792c3-3160-4356-912e-ba396c95cdcf",
                    "ip_address": "192.168.123.20",
                }
            ],
            port_security_enabled=True,
            security_group_ids=["351b0dd7-ca09-431c-be53-935db3785067"],
            tags={
                "my-tag": "my-tag-value",
                "my-tag-to-remove": None,
            },
        )
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.ports.with_raw_response.update(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.ports.with_streaming_response.update(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert_matches_type(TaskIDList, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.ports.with_raw_response.update(
                port_id="",
                project_id=1,
            )

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        port = client.cloud.ports.list(
            project_id=1,
        )
        assert_matches_type(SyncOffsetPage[Port], port, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        port = client.cloud.ports.list(
            project_id=1,
            attached=True,
            attached_to_resource_ids=["string"],
            attached_to_resource_types=["baremetal_server"],
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            ids=["string"],
            ip_address={
                "contains": ["string"],
                "exact": ["string"],
            },
            limit=1,
            managed=True,
            managed_by="file_share",
            managed_by_resource_ids=["string"],
            managed_by_resource_names=["string"],
            network_ids=["string"],
            offset=0,
            order_by="created_at.asc",
            public=True,
            region_ids=[0],
            security_group_ids=["string"],
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
        assert_matches_type(SyncOffsetPage[Port], port, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.ports.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert_matches_type(SyncOffsetPage[Port], port, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.ports.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert_matches_type(SyncOffsetPage[Port], port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        port = client.cloud.ports.delete(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        )
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.ports.with_raw_response.delete(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.ports.with_streaming_response.delete(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert_matches_type(TaskIDList, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.ports.with_raw_response.delete(
                port_id="",
                project_id=1,
            )

    @parametrize
    def test_method_convert(self, client: Gcore) -> None:
        port = client.cloud.ports.convert(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
            target_type="floating_ip",
        )
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    def test_raw_response_convert(self, client: Gcore) -> None:
        response = client.cloud.ports.with_raw_response.convert(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
            target_type="floating_ip",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    def test_streaming_response_convert(self, client: Gcore) -> None:
        with client.cloud.ports.with_streaming_response.convert(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
            target_type="floating_ip",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert_matches_type(TaskIDList, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_convert(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.ports.with_raw_response.convert(
                port_id="",
                project_id=1,
                target_type="floating_ip",
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        port = client.cloud.ports.get(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        )
        assert_matches_type(Port, port, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.ports.with_raw_response.get(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert_matches_type(Port, port, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.ports.with_streaming_response.get(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert_matches_type(Port, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.ports.with_raw_response.get(
                port_id="",
                project_id=1,
            )


class TestAsyncPorts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        port = await async_client.cloud.ports.create(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        port = await async_client.cloud.ports.create(
            project_id=1,
            region_id=1,
            dry_run=True,
            allowed_address_pairs=[{"ip_address": "192.168.123.20"}],
            ip_assignments=[
                {
                    "subnet_id": "b39792c3-3160-4356-912e-ba396c95cdcf",
                    "ip_address": "192.168.123.20",
                }
            ],
            network_id="bc688791-f1b0-44eb-97d4-07697294b1e1",
            port_security_enabled=True,
            security_group_ids=["351b0dd7-ca09-431c-be53-935db3785067"],
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.ports.with_raw_response.create(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.ports.with_streaming_response.create(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert_matches_type(TaskIDList, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        port = await async_client.cloud.ports.update(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        )
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        port = await async_client.cloud.ports.update(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
            allowed_address_pairs=[{"ip_address": "192.168.123.20"}, {"ip_address": "192.168.0.0/17"}],
            ip_assignments=[
                {
                    "subnet_id": "b39792c3-3160-4356-912e-ba396c95cdcf",
                    "ip_address": "192.168.123.20",
                }
            ],
            port_security_enabled=True,
            security_group_ids=["351b0dd7-ca09-431c-be53-935db3785067"],
            tags={
                "my-tag": "my-tag-value",
                "my-tag-to-remove": None,
            },
        )
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.ports.with_raw_response.update(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.ports.with_streaming_response.update(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert_matches_type(TaskIDList, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.ports.with_raw_response.update(
                port_id="",
                project_id=1,
            )

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        port = await async_client.cloud.ports.list(
            project_id=1,
        )
        assert_matches_type(AsyncOffsetPage[Port], port, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        port = await async_client.cloud.ports.list(
            project_id=1,
            attached=True,
            attached_to_resource_ids=["string"],
            attached_to_resource_types=["baremetal_server"],
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            ids=["string"],
            ip_address={
                "contains": ["string"],
                "exact": ["string"],
            },
            limit=1,
            managed=True,
            managed_by="file_share",
            managed_by_resource_ids=["string"],
            managed_by_resource_names=["string"],
            network_ids=["string"],
            offset=0,
            order_by="created_at.asc",
            public=True,
            region_ids=[0],
            security_group_ids=["string"],
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
        assert_matches_type(AsyncOffsetPage[Port], port, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.ports.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert_matches_type(AsyncOffsetPage[Port], port, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27612: the mock rejects arrays inside object query filters")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.ports.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert_matches_type(AsyncOffsetPage[Port], port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        port = await async_client.cloud.ports.delete(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        )
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.ports.with_raw_response.delete(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.ports.with_streaming_response.delete(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert_matches_type(TaskIDList, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.ports.with_raw_response.delete(
                port_id="",
                project_id=1,
            )

    @parametrize
    async def test_method_convert(self, async_client: AsyncGcore) -> None:
        port = await async_client.cloud.ports.convert(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
            target_type="floating_ip",
        )
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    async def test_raw_response_convert(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.ports.with_raw_response.convert(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
            target_type="floating_ip",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert_matches_type(TaskIDList, port, path=["response"])

    @parametrize
    async def test_streaming_response_convert(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.ports.with_streaming_response.convert(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
            target_type="floating_ip",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert_matches_type(TaskIDList, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_convert(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.ports.with_raw_response.convert(
                port_id="",
                project_id=1,
                target_type="floating_ip",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        port = await async_client.cloud.ports.get(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        )
        assert_matches_type(Port, port, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.ports.with_raw_response.get(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert_matches_type(Port, port, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.ports.with_streaming_response.get(
            port_id="1f0ca628-a73b-42c0-bdac-7b10d023e097",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert_matches_type(Port, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.ports.with_raw_response.get(
                port_id="",
                project_id=1,
            )

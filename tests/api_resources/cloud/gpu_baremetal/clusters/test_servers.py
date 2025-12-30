# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import Console, TaskIDList
from gcore.types.cloud.gpu_baremetal.clusters import (
    GPUBaremetalClusterServer,
    GPUBaremetalClusterServerV1,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal.clusters.servers.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(SyncOffsetPage[GPUBaremetalClusterServer], server, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal.clusters.servers.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            changed_before=parse_datetime("2025-10-01T12:00:00Z"),
            changed_since=parse_datetime("2025-10-01T12:00:00Z"),
            ip_address="237.84.2.178",
            limit=10,
            name="name",
            offset=0,
            order_by="created_at.asc",
            status="ACTIVE",
            uuids=["string"],
        )
        assert_matches_type(SyncOffsetPage[GPUBaremetalClusterServer], server, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.servers.with_raw_response.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(SyncOffsetPage[GPUBaremetalClusterServer], server, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.servers.with_streaming_response.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(SyncOffsetPage[GPUBaremetalClusterServer], server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal.clusters.servers.with_raw_response.list(
                cluster_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal.clusters.servers.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal.clusters.servers.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
            delete_floatings=True,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.servers.with_raw_response.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.servers.with_streaming_response.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            client.cloud.gpu_baremetal.clusters.servers.with_raw_response.delete(
                instance_id="instance_id",
                project_id=0,
                region_id=0,
                cluster_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.gpu_baremetal.clusters.servers.with_raw_response.delete(
                instance_id="",
                project_id=0,
                region_id=0,
                cluster_id="cluster_id",
            )

    @parametrize
    def test_method_get_console(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal.clusters.servers.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Console, server, path=["response"])

    @parametrize
    def test_raw_response_get_console(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.servers.with_raw_response.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(Console, server, path=["response"])

    @parametrize
    def test_streaming_response_get_console(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.servers.with_streaming_response.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(Console, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_console(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.gpu_baremetal.clusters.servers.with_raw_response.get_console(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_powercycle(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal.clusters.servers.powercycle(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServerV1, server, path=["response"])

    @parametrize
    def test_raw_response_powercycle(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.servers.with_raw_response.powercycle(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(GPUBaremetalClusterServerV1, server, path=["response"])

    @parametrize
    def test_streaming_response_powercycle(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.servers.with_streaming_response.powercycle(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(GPUBaremetalClusterServerV1, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_powercycle(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.gpu_baremetal.clusters.servers.with_raw_response.powercycle(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_reboot(self, client: Gcore) -> None:
        server = client.cloud.gpu_baremetal.clusters.servers.reboot(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServerV1, server, path=["response"])

    @parametrize
    def test_raw_response_reboot(self, client: Gcore) -> None:
        response = client.cloud.gpu_baremetal.clusters.servers.with_raw_response.reboot(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(GPUBaremetalClusterServerV1, server, path=["response"])

    @parametrize
    def test_streaming_response_reboot(self, client: Gcore) -> None:
        with client.cloud.gpu_baremetal.clusters.servers.with_streaming_response.reboot(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(GPUBaremetalClusterServerV1, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reboot(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.gpu_baremetal.clusters.servers.with_raw_response.reboot(
                instance_id="",
                project_id=0,
                region_id=0,
            )


class TestAsyncServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal.clusters.servers.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(AsyncOffsetPage[GPUBaremetalClusterServer], server, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal.clusters.servers.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
            changed_before=parse_datetime("2025-10-01T12:00:00Z"),
            changed_since=parse_datetime("2025-10-01T12:00:00Z"),
            ip_address="237.84.2.178",
            limit=10,
            name="name",
            offset=0,
            order_by="created_at.asc",
            status="ACTIVE",
            uuids=["string"],
        )
        assert_matches_type(AsyncOffsetPage[GPUBaremetalClusterServer], server, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.servers.with_raw_response.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(AsyncOffsetPage[GPUBaremetalClusterServer], server, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.servers.with_streaming_response.list(
            cluster_id="1aaaab48-10d0-46d9-80cc-85209284ceb4",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(AsyncOffsetPage[GPUBaremetalClusterServer], server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal.clusters.servers.with_raw_response.list(
                cluster_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal.clusters.servers.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal.clusters.servers.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
            delete_floatings=True,
        )
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.servers.with_raw_response.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(TaskIDList, server, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.servers.with_streaming_response.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            cluster_id="cluster_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(TaskIDList, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_id` but received ''"):
            await async_client.cloud.gpu_baremetal.clusters.servers.with_raw_response.delete(
                instance_id="instance_id",
                project_id=0,
                region_id=0,
                cluster_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.gpu_baremetal.clusters.servers.with_raw_response.delete(
                instance_id="",
                project_id=0,
                region_id=0,
                cluster_id="cluster_id",
            )

    @parametrize
    async def test_method_get_console(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal.clusters.servers.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Console, server, path=["response"])

    @parametrize
    async def test_raw_response_get_console(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.servers.with_raw_response.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(Console, server, path=["response"])

    @parametrize
    async def test_streaming_response_get_console(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.servers.with_streaming_response.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(Console, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_console(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.gpu_baremetal.clusters.servers.with_raw_response.get_console(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_powercycle(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal.clusters.servers.powercycle(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServerV1, server, path=["response"])

    @parametrize
    async def test_raw_response_powercycle(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.servers.with_raw_response.powercycle(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(GPUBaremetalClusterServerV1, server, path=["response"])

    @parametrize
    async def test_streaming_response_powercycle(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.servers.with_streaming_response.powercycle(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(GPUBaremetalClusterServerV1, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_powercycle(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.gpu_baremetal.clusters.servers.with_raw_response.powercycle(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_reboot(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.gpu_baremetal.clusters.servers.reboot(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(GPUBaremetalClusterServerV1, server, path=["response"])

    @parametrize
    async def test_raw_response_reboot(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_baremetal.clusters.servers.with_raw_response.reboot(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(GPUBaremetalClusterServerV1, server, path=["response"])

    @parametrize
    async def test_streaming_response_reboot(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_baremetal.clusters.servers.with_streaming_response.reboot(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(GPUBaremetalClusterServerV1, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reboot(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.gpu_baremetal.clusters.servers.with_raw_response.reboot(
                instance_id="",
                project_id=0,
                region_id=0,
            )

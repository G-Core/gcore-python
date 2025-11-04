# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import TaskIDList
from gcore.types.cloud.databases.postgres import (
    PostgresCluster,
    PostgresClusterShort,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClusters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        cluster = client.cloud.databases.postgres.clusters.create(
            project_id=0,
            region_id=0,
            cluster_name="3",
            flavor={
                "cpu": 1,
                "memory_gib": 1,
            },
            high_availability={"replication_mode": "sync"},
            network={
                "acl": ["92.33.34.127"],
                "network_type": "public",
            },
            pg_server_configuration={
                "pg_conf": "\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
                "version": "version",
            },
            storage={
                "size_gib": 100,
                "type": "ssd-hiiops",
            },
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        cluster = client.cloud.databases.postgres.clusters.create(
            project_id=0,
            region_id=0,
            cluster_name="3",
            flavor={
                "cpu": 1,
                "memory_gib": 1,
            },
            high_availability={"replication_mode": "sync"},
            network={
                "acl": ["92.33.34.127"],
                "network_type": "public",
            },
            pg_server_configuration={
                "pg_conf": "\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
                "version": "version",
                "pooler": {
                    "mode": "transaction",
                    "type": "pgbouncer",
                },
            },
            storage={
                "size_gib": 100,
                "type": "ssd-hiiops",
            },
            databases=[
                {
                    "name": "mydatabase",
                    "owner": "myuser",
                }
            ],
            users=[
                {
                    "name": "myuser",
                    "role_attributes": ["INHERIT"],
                }
            ],
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.databases.postgres.clusters.with_raw_response.create(
            project_id=0,
            region_id=0,
            cluster_name="3",
            flavor={
                "cpu": 1,
                "memory_gib": 1,
            },
            high_availability={"replication_mode": "sync"},
            network={
                "acl": ["92.33.34.127"],
                "network_type": "public",
            },
            pg_server_configuration={
                "pg_conf": "\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
                "version": "version",
            },
            storage={
                "size_gib": 100,
                "type": "ssd-hiiops",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.databases.postgres.clusters.with_streaming_response.create(
            project_id=0,
            region_id=0,
            cluster_name="3",
            flavor={
                "cpu": 1,
                "memory_gib": 1,
            },
            high_availability={"replication_mode": "sync"},
            network={
                "acl": ["92.33.34.127"],
                "network_type": "public",
            },
            pg_server_configuration={
                "pg_conf": "\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
                "version": "version",
            },
            storage={
                "size_gib": 100,
                "type": "ssd-hiiops",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        cluster = client.cloud.databases.postgres.clusters.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        cluster = client.cloud.databases.postgres.clusters.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            databases=[
                {
                    "name": "mydatabase",
                    "owner": "myuser",
                }
            ],
            flavor={
                "cpu": 1,
                "memory_gib": 1,
            },
            high_availability={"replication_mode": "sync"},
            network={
                "acl": ["92.33.34.127"],
                "network_type": "public",
            },
            pg_server_configuration={
                "pg_conf": "\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
                "pooler": {
                    "mode": "transaction",
                    "type": "pgbouncer",
                },
                "version": "15",
            },
            storage={"size_gib": 100},
            users=[
                {
                    "name": "myuser",
                    "role_attributes": ["INHERIT"],
                }
            ],
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.databases.postgres.clusters.with_raw_response.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.databases.postgres.clusters.with_streaming_response.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.databases.postgres.clusters.with_raw_response.update(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        cluster = client.cloud.databases.postgres.clusters.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SyncOffsetPage[PostgresClusterShort], cluster, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        cluster = client.cloud.databases.postgres.clusters.list(
            project_id=0,
            region_id=0,
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[PostgresClusterShort], cluster, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.databases.postgres.clusters.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(SyncOffsetPage[PostgresClusterShort], cluster, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.databases.postgres.clusters.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(SyncOffsetPage[PostgresClusterShort], cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        cluster = client.cloud.databases.postgres.clusters.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.databases.postgres.clusters.with_raw_response.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.databases.postgres.clusters.with_streaming_response.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.databases.postgres.clusters.with_raw_response.delete(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        cluster = client.cloud.databases.postgres.clusters.get(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(PostgresCluster, cluster, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.databases.postgres.clusters.with_raw_response.get(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(PostgresCluster, cluster, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.databases.postgres.clusters.with_streaming_response.get(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(PostgresCluster, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            client.cloud.databases.postgres.clusters.with_raw_response.get(
                cluster_name="",
                project_id=0,
                region_id=0,
            )


class TestAsyncClusters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.databases.postgres.clusters.create(
            project_id=0,
            region_id=0,
            cluster_name="3",
            flavor={
                "cpu": 1,
                "memory_gib": 1,
            },
            high_availability={"replication_mode": "sync"},
            network={
                "acl": ["92.33.34.127"],
                "network_type": "public",
            },
            pg_server_configuration={
                "pg_conf": "\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
                "version": "version",
            },
            storage={
                "size_gib": 100,
                "type": "ssd-hiiops",
            },
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.databases.postgres.clusters.create(
            project_id=0,
            region_id=0,
            cluster_name="3",
            flavor={
                "cpu": 1,
                "memory_gib": 1,
            },
            high_availability={"replication_mode": "sync"},
            network={
                "acl": ["92.33.34.127"],
                "network_type": "public",
            },
            pg_server_configuration={
                "pg_conf": "\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
                "version": "version",
                "pooler": {
                    "mode": "transaction",
                    "type": "pgbouncer",
                },
            },
            storage={
                "size_gib": 100,
                "type": "ssd-hiiops",
            },
            databases=[
                {
                    "name": "mydatabase",
                    "owner": "myuser",
                }
            ],
            users=[
                {
                    "name": "myuser",
                    "role_attributes": ["INHERIT"],
                }
            ],
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.databases.postgres.clusters.with_raw_response.create(
            project_id=0,
            region_id=0,
            cluster_name="3",
            flavor={
                "cpu": 1,
                "memory_gib": 1,
            },
            high_availability={"replication_mode": "sync"},
            network={
                "acl": ["92.33.34.127"],
                "network_type": "public",
            },
            pg_server_configuration={
                "pg_conf": "\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
                "version": "version",
            },
            storage={
                "size_gib": 100,
                "type": "ssd-hiiops",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.databases.postgres.clusters.with_streaming_response.create(
            project_id=0,
            region_id=0,
            cluster_name="3",
            flavor={
                "cpu": 1,
                "memory_gib": 1,
            },
            high_availability={"replication_mode": "sync"},
            network={
                "acl": ["92.33.34.127"],
                "network_type": "public",
            },
            pg_server_configuration={
                "pg_conf": "\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
                "version": "version",
            },
            storage={
                "size_gib": 100,
                "type": "ssd-hiiops",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.databases.postgres.clusters.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.databases.postgres.clusters.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
            databases=[
                {
                    "name": "mydatabase",
                    "owner": "myuser",
                }
            ],
            flavor={
                "cpu": 1,
                "memory_gib": 1,
            },
            high_availability={"replication_mode": "sync"},
            network={
                "acl": ["92.33.34.127"],
                "network_type": "public",
            },
            pg_server_configuration={
                "pg_conf": "\nlisten_addresses = 'localhost'\nport = 5432\nmax_connections = 100\nshared_buffers = 128MB\nlogging_collector = on",
                "pooler": {
                    "mode": "transaction",
                    "type": "pgbouncer",
                },
                "version": "15",
            },
            storage={"size_gib": 100},
            users=[
                {
                    "name": "myuser",
                    "role_attributes": ["INHERIT"],
                }
            ],
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.databases.postgres.clusters.with_raw_response.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.databases.postgres.clusters.with_streaming_response.update(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.databases.postgres.clusters.with_raw_response.update(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.databases.postgres.clusters.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(AsyncOffsetPage[PostgresClusterShort], cluster, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.databases.postgres.clusters.list(
            project_id=0,
            region_id=0,
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[PostgresClusterShort], cluster, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.databases.postgres.clusters.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(AsyncOffsetPage[PostgresClusterShort], cluster, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.databases.postgres.clusters.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(AsyncOffsetPage[PostgresClusterShort], cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.databases.postgres.clusters.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.databases.postgres.clusters.with_raw_response.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(TaskIDList, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.databases.postgres.clusters.with_streaming_response.delete(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(TaskIDList, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.databases.postgres.clusters.with_raw_response.delete(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        cluster = await async_client.cloud.databases.postgres.clusters.get(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(PostgresCluster, cluster, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.databases.postgres.clusters.with_raw_response.get(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(PostgresCluster, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.databases.postgres.clusters.with_streaming_response.get(
            cluster_name="cluster_name",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(PostgresCluster, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cluster_name` but received ''"):
            await async_client.cloud.databases.postgres.clusters.with_raw_response.get(
                cluster_name="",
                project_id=0,
                region_id=0,
            )

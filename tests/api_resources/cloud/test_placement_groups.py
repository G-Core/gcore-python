# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import TaskIDList, PlacementGroup, PlacementGroupList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlacementGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        placement_group = client.cloud.placement_groups.create(
            project_id=0,
            region_id=0,
            name="my-server-group",
            policy="anti-affinity",
        )
        assert_matches_type(PlacementGroup, placement_group, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.placement_groups.with_raw_response.create(
            project_id=0,
            region_id=0,
            name="my-server-group",
            policy="anti-affinity",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        placement_group = response.parse()
        assert_matches_type(PlacementGroup, placement_group, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.placement_groups.with_streaming_response.create(
            project_id=0,
            region_id=0,
            name="my-server-group",
            policy="anti-affinity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            placement_group = response.parse()
            assert_matches_type(PlacementGroup, placement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        placement_group = client.cloud.placement_groups.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(PlacementGroupList, placement_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.placement_groups.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        placement_group = response.parse()
        assert_matches_type(PlacementGroupList, placement_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.placement_groups.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            placement_group = response.parse()
            assert_matches_type(PlacementGroupList, placement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        placement_group = client.cloud.placement_groups.delete(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, placement_group, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.placement_groups.with_raw_response.delete(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        placement_group = response.parse()
        assert_matches_type(TaskIDList, placement_group, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.placement_groups.with_streaming_response.delete(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            placement_group = response.parse()
            assert_matches_type(TaskIDList, placement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.cloud.placement_groups.with_raw_response.delete(
                group_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        placement_group = client.cloud.placement_groups.get(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(PlacementGroup, placement_group, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.placement_groups.with_raw_response.get(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        placement_group = response.parse()
        assert_matches_type(PlacementGroup, placement_group, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.placement_groups.with_streaming_response.get(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            placement_group = response.parse()
            assert_matches_type(PlacementGroup, placement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.cloud.placement_groups.with_raw_response.get(
                group_id="",
                project_id=0,
                region_id=0,
            )


class TestAsyncPlacementGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        placement_group = await async_client.cloud.placement_groups.create(
            project_id=0,
            region_id=0,
            name="my-server-group",
            policy="anti-affinity",
        )
        assert_matches_type(PlacementGroup, placement_group, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.placement_groups.with_raw_response.create(
            project_id=0,
            region_id=0,
            name="my-server-group",
            policy="anti-affinity",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        placement_group = await response.parse()
        assert_matches_type(PlacementGroup, placement_group, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.placement_groups.with_streaming_response.create(
            project_id=0,
            region_id=0,
            name="my-server-group",
            policy="anti-affinity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            placement_group = await response.parse()
            assert_matches_type(PlacementGroup, placement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        placement_group = await async_client.cloud.placement_groups.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(PlacementGroupList, placement_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.placement_groups.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        placement_group = await response.parse()
        assert_matches_type(PlacementGroupList, placement_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.placement_groups.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            placement_group = await response.parse()
            assert_matches_type(PlacementGroupList, placement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        placement_group = await async_client.cloud.placement_groups.delete(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, placement_group, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.placement_groups.with_raw_response.delete(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        placement_group = await response.parse()
        assert_matches_type(TaskIDList, placement_group, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.placement_groups.with_streaming_response.delete(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            placement_group = await response.parse()
            assert_matches_type(TaskIDList, placement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.cloud.placement_groups.with_raw_response.delete(
                group_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        placement_group = await async_client.cloud.placement_groups.get(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(PlacementGroup, placement_group, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.placement_groups.with_raw_response.get(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        placement_group = await response.parse()
        assert_matches_type(PlacementGroup, placement_group, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.placement_groups.with_streaming_response.get(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            placement_group = await response.parse()
            assert_matches_type(PlacementGroup, placement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.cloud.placement_groups.with_raw_response.get(
                group_id="",
                project_id=0,
                region_id=0,
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.projects import (
    Project,
    V1ListResponse,
    V1DeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        v1 = client.cloud.projects.v1.create(
            name="New Project",
        )
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        v1 = client.cloud.projects.v1.create(
            name="New Project",
            client_id=3,
            description="Project description",
            state="ACTIVE",
        )
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.projects.v1.with_raw_response.create(
            name="New Project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.projects.v1.with_streaming_response.create(
            name="New Project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(Project, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gcore) -> None:
        v1 = client.cloud.projects.v1.retrieve(
            project_id=0,
        )
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gcore) -> None:
        response = client.cloud.projects.v1.with_raw_response.retrieve(
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gcore) -> None:
        with client.cloud.projects.v1.with_streaming_response.retrieve(
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(Project, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        v1 = client.cloud.projects.v1.update(
            project_id=0,
            name="New Project",
        )
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        v1 = client.cloud.projects.v1.update(
            project_id=0,
            name="New Project",
            description="Project description",
        )
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.projects.v1.with_raw_response.update(
            project_id=0,
            name="New Project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.projects.v1.with_streaming_response.update(
            project_id=0,
            name="New Project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(Project, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        v1 = client.cloud.projects.v1.list()
        assert_matches_type(V1ListResponse, v1, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        v1 = client.cloud.projects.v1.list(
            client_id=123,
            include_deleted=False,
            name="my-project",
            order_by=["created_at.asc"],
        )
        assert_matches_type(V1ListResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.projects.v1.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.projects.v1.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        v1 = client.cloud.projects.v1.delete(
            project_id=0,
        )
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.projects.v1.with_raw_response.delete(
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.projects.v1.with_streaming_response.delete(
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1DeleteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        v1 = await async_client.cloud.projects.v1.create(
            name="New Project",
        )
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        v1 = await async_client.cloud.projects.v1.create(
            name="New Project",
            client_id=3,
            description="Project description",
            state="ACTIVE",
        )
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.projects.v1.with_raw_response.create(
            name="New Project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.projects.v1.with_streaming_response.create(
            name="New Project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(Project, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGcore) -> None:
        v1 = await async_client.cloud.projects.v1.retrieve(
            project_id=0,
        )
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.projects.v1.with_raw_response.retrieve(
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.projects.v1.with_streaming_response.retrieve(
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(Project, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        v1 = await async_client.cloud.projects.v1.update(
            project_id=0,
            name="New Project",
        )
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        v1 = await async_client.cloud.projects.v1.update(
            project_id=0,
            name="New Project",
            description="Project description",
        )
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.projects.v1.with_raw_response.update(
            project_id=0,
            name="New Project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(Project, v1, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.projects.v1.with_streaming_response.update(
            project_id=0,
            name="New Project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(Project, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        v1 = await async_client.cloud.projects.v1.list()
        assert_matches_type(V1ListResponse, v1, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        v1 = await async_client.cloud.projects.v1.list(
            client_id=123,
            include_deleted=False,
            name="my-project",
            order_by=["created_at.asc"],
        )
        assert_matches_type(V1ListResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.projects.v1.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.projects.v1.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        v1 = await async_client.cloud.projects.v1.delete(
            project_id=0,
        )
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.projects.v1.with_raw_response.delete(
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.projects.v1.with_streaming_response.delete(
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1DeleteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

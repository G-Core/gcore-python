# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import Task

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        task = client.cloud.tasks.list()
        assert_matches_type(SyncOffsetPage[Task], task, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        task = client.cloud.tasks.list(
            from_timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_acknowledged=True,
            limit=100,
            offset=0,
            order_by="asc",
            project_id=[0, 0],
            region_id=[0, 0],
            sorting="asc",
            state=["ERROR", "FINISHED"],
            task_type="task_type",
            to_timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[Task], task, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(SyncOffsetPage[Task], task, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(SyncOffsetPage[Task], task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_acknowledge_all(self, client: Gcore) -> None:
        task = client.cloud.tasks.acknowledge_all()
        assert task is None

    @parametrize
    def test_method_acknowledge_all_with_all_params(self, client: Gcore) -> None:
        task = client.cloud.tasks.acknowledge_all(
            project_id=0,
            region_id=0,
        )
        assert task is None

    @parametrize
    def test_raw_response_acknowledge_all(self, client: Gcore) -> None:
        response = client.cloud.tasks.with_raw_response.acknowledge_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert task is None

    @parametrize
    def test_streaming_response_acknowledge_all(self, client: Gcore) -> None:
        with client.cloud.tasks.with_streaming_response.acknowledge_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert task is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_acknowledge_one(self, client: Gcore) -> None:
        task = client.cloud.tasks.acknowledge_one(
            "task_id",
        )
        assert_matches_type(Task, task, path=["response"])

    @parametrize
    def test_raw_response_acknowledge_one(self, client: Gcore) -> None:
        response = client.cloud.tasks.with_raw_response.acknowledge_one(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(Task, task, path=["response"])

    @parametrize
    def test_streaming_response_acknowledge_one(self, client: Gcore) -> None:
        with client.cloud.tasks.with_streaming_response.acknowledge_one(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(Task, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_acknowledge_one(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.cloud.tasks.with_raw_response.acknowledge_one(
                "",
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        task = client.cloud.tasks.get(
            "task_id",
        )
        assert_matches_type(Task, task, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.tasks.with_raw_response.get(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(Task, task, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.tasks.with_streaming_response.get(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(Task, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.cloud.tasks.with_raw_response.get(
                "",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        task = await async_client.cloud.tasks.list()
        assert_matches_type(AsyncOffsetPage[Task], task, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        task = await async_client.cloud.tasks.list(
            from_timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_acknowledged=True,
            limit=100,
            offset=0,
            order_by="asc",
            project_id=[0, 0],
            region_id=[0, 0],
            sorting="asc",
            state=["ERROR", "FINISHED"],
            task_type="task_type",
            to_timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[Task], task, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(AsyncOffsetPage[Task], task, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(AsyncOffsetPage[Task], task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_acknowledge_all(self, async_client: AsyncGcore) -> None:
        task = await async_client.cloud.tasks.acknowledge_all()
        assert task is None

    @parametrize
    async def test_method_acknowledge_all_with_all_params(self, async_client: AsyncGcore) -> None:
        task = await async_client.cloud.tasks.acknowledge_all(
            project_id=0,
            region_id=0,
        )
        assert task is None

    @parametrize
    async def test_raw_response_acknowledge_all(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.tasks.with_raw_response.acknowledge_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert task is None

    @parametrize
    async def test_streaming_response_acknowledge_all(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.tasks.with_streaming_response.acknowledge_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert task is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_acknowledge_one(self, async_client: AsyncGcore) -> None:
        task = await async_client.cloud.tasks.acknowledge_one(
            "task_id",
        )
        assert_matches_type(Task, task, path=["response"])

    @parametrize
    async def test_raw_response_acknowledge_one(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.tasks.with_raw_response.acknowledge_one(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(Task, task, path=["response"])

    @parametrize
    async def test_streaming_response_acknowledge_one(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.tasks.with_streaming_response.acknowledge_one(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(Task, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_acknowledge_one(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.cloud.tasks.with_raw_response.acknowledge_one(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        task = await async_client.cloud.tasks.get(
            "task_id",
        )
        assert_matches_type(Task, task, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.tasks.with_raw_response.get(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(Task, task, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.tasks.with_streaming_response.get(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(Task, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.cloud.tasks.with_raw_response.get(
                "",
            )

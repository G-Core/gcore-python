# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.streaming import (
    DirectoryBase,
    DirectoriesTree,
    DirectoryGetResponse,
)

try:
    import pydantic

    pydantic_v2 = hasattr(pydantic, "__version__") and pydantic.__version__.startswith("2.")
except ImportError:
    pydantic_v2 = False

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


@pytest.mark.skipif(not pydantic_v2, reason="Requires Pydantic v2")
class TestDirectories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        directory = client.streaming.directories.create(
            name="New series. Season 1",
        )
        assert_matches_type(DirectoryBase, directory, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        directory = client.streaming.directories.create(
            name="New series. Season 1",
            parent_id=100,
        )
        assert_matches_type(DirectoryBase, directory, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.streaming.directories.with_raw_response.create(
            name="New series. Season 1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(DirectoryBase, directory, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.streaming.directories.with_streaming_response.create(
            name="New series. Season 1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = response.parse()
            assert_matches_type(DirectoryBase, directory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        directory = client.streaming.directories.update(
            directory_id=0,
        )
        assert_matches_type(DirectoryBase, directory, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        directory = client.streaming.directories.update(
            directory_id=0,
            name="New series. Season 2",
            parent_id=0,
        )
        assert_matches_type(DirectoryBase, directory, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.streaming.directories.with_raw_response.update(
            directory_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(DirectoryBase, directory, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.streaming.directories.with_streaming_response.update(
            directory_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = response.parse()
            assert_matches_type(DirectoryBase, directory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        directory = client.streaming.directories.delete(
            0,
        )
        assert directory is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.streaming.directories.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert directory is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.streaming.directories.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = response.parse()
            assert directory is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        directory = client.streaming.directories.get(
            0,
        )
        assert_matches_type(DirectoryGetResponse, directory, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.streaming.directories.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(DirectoryGetResponse, directory, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.streaming.directories.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = response.parse()
            assert_matches_type(DirectoryGetResponse, directory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_tree(self, client: Gcore) -> None:
        directory = client.streaming.directories.get_tree()
        assert_matches_type(DirectoriesTree, directory, path=["response"])

    @parametrize
    def test_raw_response_get_tree(self, client: Gcore) -> None:
        response = client.streaming.directories.with_raw_response.get_tree()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(DirectoriesTree, directory, path=["response"])

    @parametrize
    def test_streaming_response_get_tree(self, client: Gcore) -> None:
        with client.streaming.directories.with_streaming_response.get_tree() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = response.parse()
            assert_matches_type(DirectoriesTree, directory, path=["response"])

        assert cast(Any, response.is_closed) is True


@pytest.mark.skipif(not pydantic_v2, reason="Requires Pydantic v2")
class TestAsyncDirectories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        directory = await async_client.streaming.directories.create(
            name="New series. Season 1",
        )
        assert_matches_type(DirectoryBase, directory, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        directory = await async_client.streaming.directories.create(
            name="New series. Season 1",
            parent_id=100,
        )
        assert_matches_type(DirectoryBase, directory, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.directories.with_raw_response.create(
            name="New series. Season 1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = await response.parse()
        assert_matches_type(DirectoryBase, directory, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.directories.with_streaming_response.create(
            name="New series. Season 1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = await response.parse()
            assert_matches_type(DirectoryBase, directory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        directory = await async_client.streaming.directories.update(
            directory_id=0,
        )
        assert_matches_type(DirectoryBase, directory, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        directory = await async_client.streaming.directories.update(
            directory_id=0,
            name="New series. Season 2",
            parent_id=0,
        )
        assert_matches_type(DirectoryBase, directory, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.directories.with_raw_response.update(
            directory_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = await response.parse()
        assert_matches_type(DirectoryBase, directory, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.directories.with_streaming_response.update(
            directory_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = await response.parse()
            assert_matches_type(DirectoryBase, directory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        directory = await async_client.streaming.directories.delete(
            0,
        )
        assert directory is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.directories.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = await response.parse()
        assert directory is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.directories.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = await response.parse()
            assert directory is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        directory = await async_client.streaming.directories.get(
            0,
        )
        assert_matches_type(DirectoryGetResponse, directory, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.directories.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = await response.parse()
        assert_matches_type(DirectoryGetResponse, directory, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.directories.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = await response.parse()
            assert_matches_type(DirectoryGetResponse, directory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_tree(self, async_client: AsyncGcore) -> None:
        directory = await async_client.streaming.directories.get_tree()
        assert_matches_type(DirectoriesTree, directory, path=["response"])

    @parametrize
    async def test_raw_response_get_tree(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.directories.with_raw_response.get_tree()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = await response.parse()
        assert_matches_type(DirectoriesTree, directory, path=["response"])

    @parametrize
    async def test_streaming_response_get_tree(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.directories.with_streaming_response.get_tree() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = await response.parse()
            assert_matches_type(DirectoriesTree, directory, path=["response"])

        assert cast(Any, response.is_closed) is True

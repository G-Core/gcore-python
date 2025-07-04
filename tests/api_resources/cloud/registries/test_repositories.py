# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.registries import RegistryRepositoryList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRepositories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        repository = client.cloud.registries.repositories.list(
            registry_id=0,
            project_id=0,
            region_id=0,
        )
        assert_matches_type(RegistryRepositoryList, repository, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.registries.repositories.with_raw_response.list(
            registry_id=0,
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repository = response.parse()
        assert_matches_type(RegistryRepositoryList, repository, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.registries.repositories.with_streaming_response.list(
            registry_id=0,
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repository = response.parse()
            assert_matches_type(RegistryRepositoryList, repository, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        repository = client.cloud.registries.repositories.delete(
            repository_name="repository_name",
            project_id=0,
            region_id=0,
            registry_id=0,
        )
        assert repository is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.registries.repositories.with_raw_response.delete(
            repository_name="repository_name",
            project_id=0,
            region_id=0,
            registry_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repository = response.parse()
        assert repository is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.registries.repositories.with_streaming_response.delete(
            repository_name="repository_name",
            project_id=0,
            region_id=0,
            registry_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repository = response.parse()
            assert repository is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_name` but received ''"):
            client.cloud.registries.repositories.with_raw_response.delete(
                repository_name="",
                project_id=0,
                region_id=0,
                registry_id=0,
            )


class TestAsyncRepositories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        repository = await async_client.cloud.registries.repositories.list(
            registry_id=0,
            project_id=0,
            region_id=0,
        )
        assert_matches_type(RegistryRepositoryList, repository, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.repositories.with_raw_response.list(
            registry_id=0,
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repository = await response.parse()
        assert_matches_type(RegistryRepositoryList, repository, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.repositories.with_streaming_response.list(
            registry_id=0,
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repository = await response.parse()
            assert_matches_type(RegistryRepositoryList, repository, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        repository = await async_client.cloud.registries.repositories.delete(
            repository_name="repository_name",
            project_id=0,
            region_id=0,
            registry_id=0,
        )
        assert repository is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.repositories.with_raw_response.delete(
            repository_name="repository_name",
            project_id=0,
            region_id=0,
            registry_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repository = await response.parse()
        assert repository is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.repositories.with_streaming_response.delete(
            repository_name="repository_name",
            project_id=0,
            region_id=0,
            registry_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repository = await response.parse()
            assert repository is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_name` but received ''"):
            await async_client.cloud.registries.repositories.with_raw_response.delete(
                repository_name="",
                project_id=0,
                region_id=0,
                registry_id=0,
            )

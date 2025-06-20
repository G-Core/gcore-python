# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.registries import RegistryArtifactList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArtifacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        artifact = client.cloud.registries.artifacts.list(
            repository_name="repository_name",
            project_id=0,
            region_id=0,
            registry_id=0,
        )
        assert_matches_type(RegistryArtifactList, artifact, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.registries.artifacts.with_raw_response.list(
            repository_name="repository_name",
            project_id=0,
            region_id=0,
            registry_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(RegistryArtifactList, artifact, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.registries.artifacts.with_streaming_response.list(
            repository_name="repository_name",
            project_id=0,
            region_id=0,
            registry_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(RegistryArtifactList, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_name` but received ''"):
            client.cloud.registries.artifacts.with_raw_response.list(
                repository_name="",
                project_id=0,
                region_id=0,
                registry_id=0,
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        artifact = client.cloud.registries.artifacts.delete(
            digest="digest",
            project_id=0,
            region_id=0,
            registry_id=0,
            repository_name="repository_name",
        )
        assert artifact is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.registries.artifacts.with_raw_response.delete(
            digest="digest",
            project_id=0,
            region_id=0,
            registry_id=0,
            repository_name="repository_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert artifact is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.registries.artifacts.with_streaming_response.delete(
            digest="digest",
            project_id=0,
            region_id=0,
            registry_id=0,
            repository_name="repository_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert artifact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_name` but received ''"):
            client.cloud.registries.artifacts.with_raw_response.delete(
                digest="digest",
                project_id=0,
                region_id=0,
                registry_id=0,
                repository_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `digest` but received ''"):
            client.cloud.registries.artifacts.with_raw_response.delete(
                digest="",
                project_id=0,
                region_id=0,
                registry_id=0,
                repository_name="repository_name",
            )


class TestAsyncArtifacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        artifact = await async_client.cloud.registries.artifacts.list(
            repository_name="repository_name",
            project_id=0,
            region_id=0,
            registry_id=0,
        )
        assert_matches_type(RegistryArtifactList, artifact, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.artifacts.with_raw_response.list(
            repository_name="repository_name",
            project_id=0,
            region_id=0,
            registry_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(RegistryArtifactList, artifact, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.artifacts.with_streaming_response.list(
            repository_name="repository_name",
            project_id=0,
            region_id=0,
            registry_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(RegistryArtifactList, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_name` but received ''"):
            await async_client.cloud.registries.artifacts.with_raw_response.list(
                repository_name="",
                project_id=0,
                region_id=0,
                registry_id=0,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        artifact = await async_client.cloud.registries.artifacts.delete(
            digest="digest",
            project_id=0,
            region_id=0,
            registry_id=0,
            repository_name="repository_name",
        )
        assert artifact is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.artifacts.with_raw_response.delete(
            digest="digest",
            project_id=0,
            region_id=0,
            registry_id=0,
            repository_name="repository_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert artifact is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.artifacts.with_streaming_response.delete(
            digest="digest",
            project_id=0,
            region_id=0,
            registry_id=0,
            repository_name="repository_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert artifact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_name` but received ''"):
            await async_client.cloud.registries.artifacts.with_raw_response.delete(
                digest="digest",
                project_id=0,
                region_id=0,
                registry_id=0,
                repository_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `digest` but received ''"):
            await async_client.cloud.registries.artifacts.with_raw_response.delete(
                digest="",
                project_id=0,
                region_id=0,
                registry_id=0,
                repository_name="repository_name",
            )

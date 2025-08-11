# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud.inference import (
    InferenceRegistryCredentials,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegistryCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        registry_credential = client.cloud.inference.registry_credentials.create(
            project_id=1,
            name="docker-io",
            password="password",
            registry_url="registry.example.com",
            username="username",
        )
        assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.inference.registry_credentials.with_raw_response.create(
            project_id=1,
            name="docker-io",
            password="password",
            registry_url="registry.example.com",
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry_credential = response.parse()
        assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.inference.registry_credentials.with_streaming_response.create(
            project_id=1,
            name="docker-io",
            password="password",
            registry_url="registry.example.com",
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry_credential = response.parse()
            assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        registry_credential = client.cloud.inference.registry_credentials.list(
            project_id=1,
        )
        assert_matches_type(SyncOffsetPage[InferenceRegistryCredentials], registry_credential, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        registry_credential = client.cloud.inference.registry_credentials.list(
            project_id=1,
            limit=1000,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[InferenceRegistryCredentials], registry_credential, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.inference.registry_credentials.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry_credential = response.parse()
        assert_matches_type(SyncOffsetPage[InferenceRegistryCredentials], registry_credential, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.inference.registry_credentials.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry_credential = response.parse()
            assert_matches_type(SyncOffsetPage[InferenceRegistryCredentials], registry_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        registry_credential = client.cloud.inference.registry_credentials.delete(
            credential_name="docker-io",
            project_id=1,
        )
        assert registry_credential is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.inference.registry_credentials.with_raw_response.delete(
            credential_name="docker-io",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry_credential = response.parse()
        assert registry_credential is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.inference.registry_credentials.with_streaming_response.delete(
            credential_name="docker-io",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry_credential = response.parse()
            assert registry_credential is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_name` but received ''"):
            client.cloud.inference.registry_credentials.with_raw_response.delete(
                credential_name="",
                project_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        registry_credential = client.cloud.inference.registry_credentials.get(
            credential_name="docker-io",
            project_id=1,
        )
        assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.inference.registry_credentials.with_raw_response.get(
            credential_name="docker-io",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry_credential = response.parse()
        assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.inference.registry_credentials.with_streaming_response.get(
            credential_name="docker-io",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry_credential = response.parse()
            assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_name` but received ''"):
            client.cloud.inference.registry_credentials.with_raw_response.get(
                credential_name="",
                project_id=1,
            )

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        registry_credential = client.cloud.inference.registry_credentials.replace(
            credential_name="docker-io",
            project_id=1,
            password="password",
            registry_url="registry.example.com",
            username="username",
        )
        assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.cloud.inference.registry_credentials.with_raw_response.replace(
            credential_name="docker-io",
            project_id=1,
            password="password",
            registry_url="registry.example.com",
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry_credential = response.parse()
        assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.cloud.inference.registry_credentials.with_streaming_response.replace(
            credential_name="docker-io",
            project_id=1,
            password="password",
            registry_url="registry.example.com",
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry_credential = response.parse()
            assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_name` but received ''"):
            client.cloud.inference.registry_credentials.with_raw_response.replace(
                credential_name="",
                project_id=1,
                password="password",
                registry_url="registry.example.com",
                username="username",
            )


class TestAsyncRegistryCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        registry_credential = await async_client.cloud.inference.registry_credentials.create(
            project_id=1,
            name="docker-io",
            password="password",
            registry_url="registry.example.com",
            username="username",
        )
        assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.registry_credentials.with_raw_response.create(
            project_id=1,
            name="docker-io",
            password="password",
            registry_url="registry.example.com",
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry_credential = await response.parse()
        assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.registry_credentials.with_streaming_response.create(
            project_id=1,
            name="docker-io",
            password="password",
            registry_url="registry.example.com",
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry_credential = await response.parse()
            assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        registry_credential = await async_client.cloud.inference.registry_credentials.list(
            project_id=1,
        )
        assert_matches_type(AsyncOffsetPage[InferenceRegistryCredentials], registry_credential, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        registry_credential = await async_client.cloud.inference.registry_credentials.list(
            project_id=1,
            limit=1000,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[InferenceRegistryCredentials], registry_credential, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.registry_credentials.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry_credential = await response.parse()
        assert_matches_type(AsyncOffsetPage[InferenceRegistryCredentials], registry_credential, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.registry_credentials.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry_credential = await response.parse()
            assert_matches_type(AsyncOffsetPage[InferenceRegistryCredentials], registry_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        registry_credential = await async_client.cloud.inference.registry_credentials.delete(
            credential_name="docker-io",
            project_id=1,
        )
        assert registry_credential is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.registry_credentials.with_raw_response.delete(
            credential_name="docker-io",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry_credential = await response.parse()
        assert registry_credential is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.registry_credentials.with_streaming_response.delete(
            credential_name="docker-io",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry_credential = await response.parse()
            assert registry_credential is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_name` but received ''"):
            await async_client.cloud.inference.registry_credentials.with_raw_response.delete(
                credential_name="",
                project_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        registry_credential = await async_client.cloud.inference.registry_credentials.get(
            credential_name="docker-io",
            project_id=1,
        )
        assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.registry_credentials.with_raw_response.get(
            credential_name="docker-io",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry_credential = await response.parse()
        assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.registry_credentials.with_streaming_response.get(
            credential_name="docker-io",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry_credential = await response.parse()
            assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_name` but received ''"):
            await async_client.cloud.inference.registry_credentials.with_raw_response.get(
                credential_name="",
                project_id=1,
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        registry_credential = await async_client.cloud.inference.registry_credentials.replace(
            credential_name="docker-io",
            project_id=1,
            password="password",
            registry_url="registry.example.com",
            username="username",
        )
        assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.registry_credentials.with_raw_response.replace(
            credential_name="docker-io",
            project_id=1,
            password="password",
            registry_url="registry.example.com",
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry_credential = await response.parse()
        assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.registry_credentials.with_streaming_response.replace(
            credential_name="docker-io",
            project_id=1,
            password="password",
            registry_url="registry.example.com",
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry_credential = await response.parse()
            assert_matches_type(InferenceRegistryCredentials, registry_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_name` but received ''"):
            await async_client.cloud.inference.registry_credentials.with_raw_response.replace(
                credential_name="",
                project_id=1,
                password="password",
                registry_url="registry.example.com",
                username="username",
            )

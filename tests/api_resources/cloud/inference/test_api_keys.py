# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud.inference import (
    InferenceAPIKey,
    InferenceAPIKeyCreate,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        api_key = client.cloud.inference.api_keys.create(
            project_id=1,
            name="my-api-key",
        )
        assert_matches_type(InferenceAPIKeyCreate, api_key, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        api_key = client.cloud.inference.api_keys.create(
            project_id=1,
            name="my-api-key",
            description="This key is used for accessing the inference service.",
            expires_at="2024-10-01T12:00:00Z",
        )
        assert_matches_type(InferenceAPIKeyCreate, api_key, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.inference.api_keys.with_raw_response.create(
            project_id=1,
            name="my-api-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(InferenceAPIKeyCreate, api_key, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.inference.api_keys.with_streaming_response.create(
            project_id=1,
            name="my-api-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(InferenceAPIKeyCreate, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        api_key = client.cloud.inference.api_keys.update(
            api_key_name="aws-dev",
            project_id=1,
        )
        assert_matches_type(InferenceAPIKey, api_key, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        api_key = client.cloud.inference.api_keys.update(
            api_key_name="aws-dev",
            project_id=1,
            description="This key is used for accessing the inference service.",
        )
        assert_matches_type(InferenceAPIKey, api_key, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.inference.api_keys.with_raw_response.update(
            api_key_name="aws-dev",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(InferenceAPIKey, api_key, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.inference.api_keys.with_streaming_response.update(
            api_key_name="aws-dev",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(InferenceAPIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_name` but received ''"):
            client.cloud.inference.api_keys.with_raw_response.update(
                api_key_name="",
                project_id=1,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        api_key = client.cloud.inference.api_keys.list(
            project_id=1,
        )
        assert_matches_type(SyncOffsetPage[InferenceAPIKey], api_key, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        api_key = client.cloud.inference.api_keys.list(
            project_id=1,
            limit=100,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[InferenceAPIKey], api_key, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.inference.api_keys.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(SyncOffsetPage[InferenceAPIKey], api_key, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.inference.api_keys.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(SyncOffsetPage[InferenceAPIKey], api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        api_key = client.cloud.inference.api_keys.delete(
            api_key_name="aws-dev",
            project_id=1,
        )
        assert api_key is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.inference.api_keys.with_raw_response.delete(
            api_key_name="aws-dev",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert api_key is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.inference.api_keys.with_streaming_response.delete(
            api_key_name="aws-dev",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert api_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_name` but received ''"):
            client.cloud.inference.api_keys.with_raw_response.delete(
                api_key_name="",
                project_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        api_key = client.cloud.inference.api_keys.get(
            api_key_name="aws-dev",
            project_id=1,
        )
        assert_matches_type(InferenceAPIKey, api_key, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.inference.api_keys.with_raw_response.get(
            api_key_name="aws-dev",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(InferenceAPIKey, api_key, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.inference.api_keys.with_streaming_response.get(
            api_key_name="aws-dev",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(InferenceAPIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_name` but received ''"):
            client.cloud.inference.api_keys.with_raw_response.get(
                api_key_name="",
                project_id=1,
            )


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        api_key = await async_client.cloud.inference.api_keys.create(
            project_id=1,
            name="my-api-key",
        )
        assert_matches_type(InferenceAPIKeyCreate, api_key, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        api_key = await async_client.cloud.inference.api_keys.create(
            project_id=1,
            name="my-api-key",
            description="This key is used for accessing the inference service.",
            expires_at="2024-10-01T12:00:00Z",
        )
        assert_matches_type(InferenceAPIKeyCreate, api_key, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.api_keys.with_raw_response.create(
            project_id=1,
            name="my-api-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(InferenceAPIKeyCreate, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.api_keys.with_streaming_response.create(
            project_id=1,
            name="my-api-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(InferenceAPIKeyCreate, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        api_key = await async_client.cloud.inference.api_keys.update(
            api_key_name="aws-dev",
            project_id=1,
        )
        assert_matches_type(InferenceAPIKey, api_key, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        api_key = await async_client.cloud.inference.api_keys.update(
            api_key_name="aws-dev",
            project_id=1,
            description="This key is used for accessing the inference service.",
        )
        assert_matches_type(InferenceAPIKey, api_key, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.api_keys.with_raw_response.update(
            api_key_name="aws-dev",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(InferenceAPIKey, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.api_keys.with_streaming_response.update(
            api_key_name="aws-dev",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(InferenceAPIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_name` but received ''"):
            await async_client.cloud.inference.api_keys.with_raw_response.update(
                api_key_name="",
                project_id=1,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        api_key = await async_client.cloud.inference.api_keys.list(
            project_id=1,
        )
        assert_matches_type(AsyncOffsetPage[InferenceAPIKey], api_key, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        api_key = await async_client.cloud.inference.api_keys.list(
            project_id=1,
            limit=100,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[InferenceAPIKey], api_key, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.api_keys.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(AsyncOffsetPage[InferenceAPIKey], api_key, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.api_keys.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(AsyncOffsetPage[InferenceAPIKey], api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        api_key = await async_client.cloud.inference.api_keys.delete(
            api_key_name="aws-dev",
            project_id=1,
        )
        assert api_key is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.api_keys.with_raw_response.delete(
            api_key_name="aws-dev",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert api_key is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.api_keys.with_streaming_response.delete(
            api_key_name="aws-dev",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert api_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_name` but received ''"):
            await async_client.cloud.inference.api_keys.with_raw_response.delete(
                api_key_name="",
                project_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        api_key = await async_client.cloud.inference.api_keys.get(
            api_key_name="aws-dev",
            project_id=1,
        )
        assert_matches_type(InferenceAPIKey, api_key, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.api_keys.with_raw_response.get(
            api_key_name="aws-dev",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(InferenceAPIKey, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.api_keys.with_streaming_response.get(
            api_key_name="aws-dev",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(InferenceAPIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_name` but received ''"):
            await async_client.cloud.inference.api_keys.with_raw_response.get(
                api_key_name="",
                project_id=1,
            )

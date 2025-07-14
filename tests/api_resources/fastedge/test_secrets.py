# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.fastedge import (
    Secret,
    SecretListResponse,
    SecretCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        secret = client.fastedge.secrets.create(
            name="name",
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        secret = client.fastedge.secrets.create(
            name="name",
            comment="comment",
            secret_slots=[
                {
                    "slot": 0,
                    "value": "value",
                }
            ],
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.fastedge.secrets.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.fastedge.secrets.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretCreateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        secret = client.fastedge.secrets.update(
            id=0,
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        secret = client.fastedge.secrets.update(
            id=0,
            comment="comment",
            name="name",
            secret_slots=[
                {
                    "slot": 0,
                    "value": "value",
                }
            ],
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.fastedge.secrets.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.fastedge.secrets.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        secret = client.fastedge.secrets.list()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        secret = client.fastedge.secrets.list(
            app_id=0,
            secret_name="secret_name",
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.fastedge.secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.fastedge.secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        secret = client.fastedge.secrets.delete(
            id=0,
        )
        assert secret is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        secret = client.fastedge.secrets.delete(
            id=0,
            force=True,
        )
        assert secret is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.fastedge.secrets.with_raw_response.delete(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert secret is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.fastedge.secrets.with_streaming_response.delete(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        secret = client.fastedge.secrets.get(
            0,
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.fastedge.secrets.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.fastedge.secrets.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        secret = client.fastedge.secrets.replace(
            id=0,
            name="name",
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        secret = client.fastedge.secrets.replace(
            id=0,
            name="name",
            comment="comment",
            secret_slots=[
                {
                    "slot": 0,
                    "value": "value",
                }
            ],
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.fastedge.secrets.with_raw_response.replace(
            id=0,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.fastedge.secrets.with_streaming_response.replace(
            id=0,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        secret = await async_client.fastedge.secrets.create(
            name="name",
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        secret = await async_client.fastedge.secrets.create(
            name="name",
            comment="comment",
            secret_slots=[
                {
                    "slot": 0,
                    "value": "value",
                }
            ],
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.secrets.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.secrets.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretCreateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        secret = await async_client.fastedge.secrets.update(
            id=0,
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        secret = await async_client.fastedge.secrets.update(
            id=0,
            comment="comment",
            name="name",
            secret_slots=[
                {
                    "slot": 0,
                    "value": "value",
                }
            ],
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.secrets.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.secrets.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        secret = await async_client.fastedge.secrets.list()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        secret = await async_client.fastedge.secrets.list(
            app_id=0,
            secret_name="secret_name",
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        secret = await async_client.fastedge.secrets.delete(
            id=0,
        )
        assert secret is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        secret = await async_client.fastedge.secrets.delete(
            id=0,
            force=True,
        )
        assert secret is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.secrets.with_raw_response.delete(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert secret is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.secrets.with_streaming_response.delete(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        secret = await async_client.fastedge.secrets.get(
            0,
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.secrets.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.secrets.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        secret = await async_client.fastedge.secrets.replace(
            id=0,
            name="name",
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        secret = await async_client.fastedge.secrets.replace(
            id=0,
            name="name",
            comment="comment",
            secret_slots=[
                {
                    "slot": 0,
                    "value": "value",
                }
            ],
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.fastedge.secrets.with_raw_response.replace(
            id=0,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.fastedge.secrets.with_streaming_response.replace(
            id=0,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

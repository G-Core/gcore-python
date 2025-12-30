# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.iam import APIToken, APITokenList, APITokenCreated

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPITokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        api_token = client.iam.api_tokens.create(
            client_id=0,
            client_user={},
            exp_date="2021-01-01 12:00:00+00:00",
            name="My token",
        )
        assert_matches_type(APITokenCreated, api_token, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        api_token = client.iam.api_tokens.create(
            client_id=0,
            client_user={
                "role": {
                    "id": 1,
                    "name": "Administrators",
                }
            },
            exp_date="2021-01-01 12:00:00+00:00",
            name="My token",
            description="It's my token",
        )
        assert_matches_type(APITokenCreated, api_token, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.iam.api_tokens.with_raw_response.create(
            client_id=0,
            client_user={},
            exp_date="2021-01-01 12:00:00+00:00",
            name="My token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_token = response.parse()
        assert_matches_type(APITokenCreated, api_token, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.iam.api_tokens.with_streaming_response.create(
            client_id=0,
            client_user={},
            exp_date="2021-01-01 12:00:00+00:00",
            name="My token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_token = response.parse()
            assert_matches_type(APITokenCreated, api_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        api_token = client.iam.api_tokens.list(
            client_id=0,
        )
        assert_matches_type(APITokenList, api_token, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        api_token = client.iam.api_tokens.list(
            client_id=0,
            deleted=True,
            issued_by=0,
            not_issued_by=0,
            role="role",
        )
        assert_matches_type(APITokenList, api_token, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.iam.api_tokens.with_raw_response.list(
            client_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_token = response.parse()
        assert_matches_type(APITokenList, api_token, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.iam.api_tokens.with_streaming_response.list(
            client_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_token = response.parse()
            assert_matches_type(APITokenList, api_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        api_token = client.iam.api_tokens.delete(
            token_id=0,
            client_id=0,
        )
        assert api_token is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.iam.api_tokens.with_raw_response.delete(
            token_id=0,
            client_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_token = response.parse()
        assert api_token is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.iam.api_tokens.with_streaming_response.delete(
            token_id=0,
            client_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_token = response.parse()
            assert api_token is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        api_token = client.iam.api_tokens.get(
            token_id=0,
            client_id=0,
        )
        assert_matches_type(APIToken, api_token, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.iam.api_tokens.with_raw_response.get(
            token_id=0,
            client_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_token = response.parse()
        assert_matches_type(APIToken, api_token, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.iam.api_tokens.with_streaming_response.get(
            token_id=0,
            client_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_token = response.parse()
            assert_matches_type(APIToken, api_token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPITokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        api_token = await async_client.iam.api_tokens.create(
            client_id=0,
            client_user={},
            exp_date="2021-01-01 12:00:00+00:00",
            name="My token",
        )
        assert_matches_type(APITokenCreated, api_token, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        api_token = await async_client.iam.api_tokens.create(
            client_id=0,
            client_user={
                "role": {
                    "id": 1,
                    "name": "Administrators",
                }
            },
            exp_date="2021-01-01 12:00:00+00:00",
            name="My token",
            description="It's my token",
        )
        assert_matches_type(APITokenCreated, api_token, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.iam.api_tokens.with_raw_response.create(
            client_id=0,
            client_user={},
            exp_date="2021-01-01 12:00:00+00:00",
            name="My token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_token = await response.parse()
        assert_matches_type(APITokenCreated, api_token, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.iam.api_tokens.with_streaming_response.create(
            client_id=0,
            client_user={},
            exp_date="2021-01-01 12:00:00+00:00",
            name="My token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_token = await response.parse()
            assert_matches_type(APITokenCreated, api_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        api_token = await async_client.iam.api_tokens.list(
            client_id=0,
        )
        assert_matches_type(APITokenList, api_token, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        api_token = await async_client.iam.api_tokens.list(
            client_id=0,
            deleted=True,
            issued_by=0,
            not_issued_by=0,
            role="role",
        )
        assert_matches_type(APITokenList, api_token, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.iam.api_tokens.with_raw_response.list(
            client_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_token = await response.parse()
        assert_matches_type(APITokenList, api_token, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.iam.api_tokens.with_streaming_response.list(
            client_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_token = await response.parse()
            assert_matches_type(APITokenList, api_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        api_token = await async_client.iam.api_tokens.delete(
            token_id=0,
            client_id=0,
        )
        assert api_token is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.iam.api_tokens.with_raw_response.delete(
            token_id=0,
            client_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_token = await response.parse()
        assert api_token is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.iam.api_tokens.with_streaming_response.delete(
            token_id=0,
            client_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_token = await response.parse()
            assert api_token is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        api_token = await async_client.iam.api_tokens.get(
            token_id=0,
            client_id=0,
        )
        assert_matches_type(APIToken, api_token, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.iam.api_tokens.with_raw_response.get(
            token_id=0,
            client_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_token = await response.parse()
        assert_matches_type(APIToken, api_token, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.iam.api_tokens.with_streaming_response.get(
            token_id=0,
            client_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_token = await response.parse()
            assert_matches_type(APIToken, api_token, path=["response"])

        assert cast(Any, response.is_closed) is True

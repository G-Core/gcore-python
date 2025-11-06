# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.security import (
    ClientProfile,
    ProfileListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        profile = client.security.profiles.create(
            fields=[{"base_field": 1}],
            profile_template=1,
            site="GNC",
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        profile = client.security.profiles.create(
            fields=[
                {
                    "base_field": 1,
                    "field_value": {},
                }
            ],
            profile_template=1,
            site="GNC",
            ip_address="123.43.2.10",
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.security.profiles.with_raw_response.create(
            fields=[{"base_field": 1}],
            profile_template=1,
            site="GNC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.security.profiles.with_streaming_response.create(
            fields=[{"base_field": 1}],
            profile_template=1,
            site="GNC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ClientProfile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        profile = client.security.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        profile = client.security.profiles.list(
            exclude_empty_address=True,
            include_deleted=True,
            ip_address="ip_address",
            site="ED",
        )
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.security.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.security.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        profile = client.security.profiles.delete(
            0,
        )
        assert profile is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.security.profiles.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert profile is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.security.profiles.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        profile = client.security.profiles.get(
            0,
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.security.profiles.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.security.profiles.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ClientProfile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_recreate(self, client: Gcore) -> None:
        profile = client.security.profiles.recreate(
            id=0,
            fields=[{"base_field": 1}],
            profile_template=1,
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    def test_method_recreate_with_all_params(self, client: Gcore) -> None:
        profile = client.security.profiles.recreate(
            id=0,
            fields=[
                {
                    "base_field": 1,
                    "field_value": {},
                }
            ],
            profile_template=1,
            ip_address="ip_address",
            site="ED",
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    def test_raw_response_recreate(self, client: Gcore) -> None:
        response = client.security.profiles.with_raw_response.recreate(
            id=0,
            fields=[{"base_field": 1}],
            profile_template=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    def test_streaming_response_recreate(self, client: Gcore) -> None:
        with client.security.profiles.with_streaming_response.recreate(
            id=0,
            fields=[{"base_field": 1}],
            profile_template=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ClientProfile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        profile = client.security.profiles.replace(
            id=0,
            fields=[{"base_field": 1}],
            profile_template=1,
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        profile = client.security.profiles.replace(
            id=0,
            fields=[
                {
                    "base_field": 1,
                    "field_value": {},
                }
            ],
            profile_template=1,
            ip_address="ip_address",
            site="ED",
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.security.profiles.with_raw_response.replace(
            id=0,
            fields=[{"base_field": 1}],
            profile_template=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.security.profiles.with_streaming_response.replace(
            id=0,
            fields=[{"base_field": 1}],
            profile_template=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ClientProfile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        profile = await async_client.security.profiles.create(
            fields=[{"base_field": 1}],
            profile_template=1,
            site="GNC",
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        profile = await async_client.security.profiles.create(
            fields=[
                {
                    "base_field": 1,
                    "field_value": {},
                }
            ],
            profile_template=1,
            site="GNC",
            ip_address="123.43.2.10",
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.security.profiles.with_raw_response.create(
            fields=[{"base_field": 1}],
            profile_template=1,
            site="GNC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.security.profiles.with_streaming_response.create(
            fields=[{"base_field": 1}],
            profile_template=1,
            site="GNC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ClientProfile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        profile = await async_client.security.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        profile = await async_client.security.profiles.list(
            exclude_empty_address=True,
            include_deleted=True,
            ip_address="ip_address",
            site="ED",
        )
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.security.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.security.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        profile = await async_client.security.profiles.delete(
            0,
        )
        assert profile is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.security.profiles.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert profile is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.security.profiles.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        profile = await async_client.security.profiles.get(
            0,
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.security.profiles.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.security.profiles.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ClientProfile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_recreate(self, async_client: AsyncGcore) -> None:
        profile = await async_client.security.profiles.recreate(
            id=0,
            fields=[{"base_field": 1}],
            profile_template=1,
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    async def test_method_recreate_with_all_params(self, async_client: AsyncGcore) -> None:
        profile = await async_client.security.profiles.recreate(
            id=0,
            fields=[
                {
                    "base_field": 1,
                    "field_value": {},
                }
            ],
            profile_template=1,
            ip_address="ip_address",
            site="ED",
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    async def test_raw_response_recreate(self, async_client: AsyncGcore) -> None:
        response = await async_client.security.profiles.with_raw_response.recreate(
            id=0,
            fields=[{"base_field": 1}],
            profile_template=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    async def test_streaming_response_recreate(self, async_client: AsyncGcore) -> None:
        async with async_client.security.profiles.with_streaming_response.recreate(
            id=0,
            fields=[{"base_field": 1}],
            profile_template=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ClientProfile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        profile = await async_client.security.profiles.replace(
            id=0,
            fields=[{"base_field": 1}],
            profile_template=1,
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        profile = await async_client.security.profiles.replace(
            id=0,
            fields=[
                {
                    "base_field": 1,
                    "field_value": {},
                }
            ],
            profile_template=1,
            ip_address="ip_address",
            site="ED",
        )
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.security.profiles.with_raw_response.replace(
            id=0,
            fields=[{"base_field": 1}],
            profile_template=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ClientProfile, profile, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.security.profiles.with_streaming_response.replace(
            id=0,
            fields=[{"base_field": 1}],
            profile_template=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ClientProfile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

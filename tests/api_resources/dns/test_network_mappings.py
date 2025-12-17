# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.dns import (
    DNSNetworkMapping,
    NetworkMappingListResponse,
    NetworkMappingCreateResponse,
    NetworkMappingImportResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNetworkMappings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        network_mapping = client.dns.network_mappings.create()
        assert_matches_type(NetworkMappingCreateResponse, network_mapping, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        network_mapping = client.dns.network_mappings.create(
            mapping=[
                {
                    "cidr4": ["string"],
                    "cidr6": ["string"],
                    "tags": ["string"],
                }
            ],
            name="name",
        )
        assert_matches_type(NetworkMappingCreateResponse, network_mapping, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.dns.network_mappings.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = response.parse()
        assert_matches_type(NetworkMappingCreateResponse, network_mapping, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.dns.network_mappings.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = response.parse()
            assert_matches_type(NetworkMappingCreateResponse, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        network_mapping = client.dns.network_mappings.list()
        assert_matches_type(NetworkMappingListResponse, network_mapping, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        network_mapping = client.dns.network_mappings.list(
            limit=0,
            offset=0,
            order_by="order_by",
            order_direction="asc",
        )
        assert_matches_type(NetworkMappingListResponse, network_mapping, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.dns.network_mappings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = response.parse()
        assert_matches_type(NetworkMappingListResponse, network_mapping, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.dns.network_mappings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = response.parse()
            assert_matches_type(NetworkMappingListResponse, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        network_mapping = client.dns.network_mappings.delete(
            0,
        )
        assert_matches_type(object, network_mapping, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.dns.network_mappings.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = response.parse()
        assert_matches_type(object, network_mapping, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.dns.network_mappings.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = response.parse()
            assert_matches_type(object, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        network_mapping = client.dns.network_mappings.get(
            0,
        )
        assert_matches_type(DNSNetworkMapping, network_mapping, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.dns.network_mappings.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = response.parse()
        assert_matches_type(DNSNetworkMapping, network_mapping, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.dns.network_mappings.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = response.parse()
            assert_matches_type(DNSNetworkMapping, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_name(self, client: Gcore) -> None:
        network_mapping = client.dns.network_mappings.get_by_name(
            "name",
        )
        assert_matches_type(DNSNetworkMapping, network_mapping, path=["response"])

    @parametrize
    def test_raw_response_get_by_name(self, client: Gcore) -> None:
        response = client.dns.network_mappings.with_raw_response.get_by_name(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = response.parse()
        assert_matches_type(DNSNetworkMapping, network_mapping, path=["response"])

    @parametrize
    def test_streaming_response_get_by_name(self, client: Gcore) -> None:
        with client.dns.network_mappings.with_streaming_response.get_by_name(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = response.parse()
            assert_matches_type(DNSNetworkMapping, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_name(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.dns.network_mappings.with_raw_response.get_by_name(
                "",
            )

    @parametrize
    def test_method_import(self, client: Gcore) -> None:
        network_mapping = client.dns.network_mappings.import_()
        assert_matches_type(NetworkMappingImportResponse, network_mapping, path=["response"])

    @parametrize
    def test_raw_response_import(self, client: Gcore) -> None:
        response = client.dns.network_mappings.with_raw_response.import_()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = response.parse()
        assert_matches_type(NetworkMappingImportResponse, network_mapping, path=["response"])

    @parametrize
    def test_streaming_response_import(self, client: Gcore) -> None:
        with client.dns.network_mappings.with_streaming_response.import_() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = response.parse()
            assert_matches_type(NetworkMappingImportResponse, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        network_mapping = client.dns.network_mappings.replace(
            id=0,
        )
        assert_matches_type(object, network_mapping, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        network_mapping = client.dns.network_mappings.replace(
            id=0,
            mapping=[
                {
                    "cidr4": ["string"],
                    "cidr6": ["string"],
                    "tags": ["string"],
                }
            ],
            name="name",
        )
        assert_matches_type(object, network_mapping, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.dns.network_mappings.with_raw_response.replace(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = response.parse()
        assert_matches_type(object, network_mapping, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.dns.network_mappings.with_streaming_response.replace(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = response.parse()
            assert_matches_type(object, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNetworkMappings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        network_mapping = await async_client.dns.network_mappings.create()
        assert_matches_type(NetworkMappingCreateResponse, network_mapping, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        network_mapping = await async_client.dns.network_mappings.create(
            mapping=[
                {
                    "cidr4": ["string"],
                    "cidr6": ["string"],
                    "tags": ["string"],
                }
            ],
            name="name",
        )
        assert_matches_type(NetworkMappingCreateResponse, network_mapping, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.network_mappings.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = await response.parse()
        assert_matches_type(NetworkMappingCreateResponse, network_mapping, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.network_mappings.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = await response.parse()
            assert_matches_type(NetworkMappingCreateResponse, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        network_mapping = await async_client.dns.network_mappings.list()
        assert_matches_type(NetworkMappingListResponse, network_mapping, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        network_mapping = await async_client.dns.network_mappings.list(
            limit=0,
            offset=0,
            order_by="order_by",
            order_direction="asc",
        )
        assert_matches_type(NetworkMappingListResponse, network_mapping, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.network_mappings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = await response.parse()
        assert_matches_type(NetworkMappingListResponse, network_mapping, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.network_mappings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = await response.parse()
            assert_matches_type(NetworkMappingListResponse, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        network_mapping = await async_client.dns.network_mappings.delete(
            0,
        )
        assert_matches_type(object, network_mapping, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.network_mappings.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = await response.parse()
        assert_matches_type(object, network_mapping, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.network_mappings.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = await response.parse()
            assert_matches_type(object, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        network_mapping = await async_client.dns.network_mappings.get(
            0,
        )
        assert_matches_type(DNSNetworkMapping, network_mapping, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.network_mappings.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = await response.parse()
        assert_matches_type(DNSNetworkMapping, network_mapping, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.network_mappings.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = await response.parse()
            assert_matches_type(DNSNetworkMapping, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_name(self, async_client: AsyncGcore) -> None:
        network_mapping = await async_client.dns.network_mappings.get_by_name(
            "name",
        )
        assert_matches_type(DNSNetworkMapping, network_mapping, path=["response"])

    @parametrize
    async def test_raw_response_get_by_name(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.network_mappings.with_raw_response.get_by_name(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = await response.parse()
        assert_matches_type(DNSNetworkMapping, network_mapping, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_name(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.network_mappings.with_streaming_response.get_by_name(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = await response.parse()
            assert_matches_type(DNSNetworkMapping, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_name(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.dns.network_mappings.with_raw_response.get_by_name(
                "",
            )

    @parametrize
    async def test_method_import(self, async_client: AsyncGcore) -> None:
        network_mapping = await async_client.dns.network_mappings.import_()
        assert_matches_type(NetworkMappingImportResponse, network_mapping, path=["response"])

    @parametrize
    async def test_raw_response_import(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.network_mappings.with_raw_response.import_()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = await response.parse()
        assert_matches_type(NetworkMappingImportResponse, network_mapping, path=["response"])

    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.network_mappings.with_streaming_response.import_() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = await response.parse()
            assert_matches_type(NetworkMappingImportResponse, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        network_mapping = await async_client.dns.network_mappings.replace(
            id=0,
        )
        assert_matches_type(object, network_mapping, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        network_mapping = await async_client.dns.network_mappings.replace(
            id=0,
            mapping=[
                {
                    "cidr4": ["string"],
                    "cidr6": ["string"],
                    "tags": ["string"],
                }
            ],
            name="name",
        )
        assert_matches_type(object, network_mapping, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.network_mappings.with_raw_response.replace(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_mapping = await response.parse()
        assert_matches_type(object, network_mapping, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.network_mappings.with_streaming_response.replace(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_mapping = await response.parse()
            assert_matches_type(object, network_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

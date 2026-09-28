# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn import (
    Alias,
    AliasDetail,
    AliasCertificateStatus,
    AliasCreateMultipleResponse,
    AliasDeleteMultipleResponse,
)
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAliases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        alias = client.cdn.aliases.create(
            cname="shop.customer.com",
            resource_id=4567,
        )
        assert_matches_type(Alias, alias, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        alias = client.cdn.aliases.create(
            cname="shop.customer.com",
            resource_id=4567,
            active=True,
            automated=True,
            ssl_id=890,
        )
        assert_matches_type(Alias, alias, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cdn.aliases.with_raw_response.create(
            cname="shop.customer.com",
            resource_id=4567,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = response.parse()
        assert_matches_type(Alias, alias, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cdn.aliases.with_streaming_response.create(
            cname="shop.customer.com",
            resource_id=4567,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = response.parse()
            assert_matches_type(Alias, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        alias = client.cdn.aliases.update(
            alias_id=0,
        )
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        alias = client.cdn.aliases.update(
            alias_id=0,
            active=False,
            automated=True,
            ssl_id=891,
        )
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cdn.aliases.with_raw_response.update(
            alias_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = response.parse()
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cdn.aliases.with_streaming_response.update(
            alias_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = response.parse()
            assert_matches_type(AliasDetail, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        alias = client.cdn.aliases.list()
        assert_matches_type(SyncOffsetPage[Alias], alias, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        alias = client.cdn.aliases.list(
            automated=True,
            cname="cname",
            cname_endswith="cname_endswith",
            cname_startswith="cname_startswith",
            limit=1,
            offset=0,
            ordering="ordering",
            resource_id=0,
            resource_id_in="resource_id__in",
            search="search",
            ssl_id=0,
            ssl_status="issued",
            ssl_status_in="ssl_status__in",
            ssl_validity_not_after_gte="ssl_validity_not_after_gte",
            ssl_validity_not_after_lte="ssl_validity_not_after_lte",
            status="active",
            status_in="status__in",
        )
        assert_matches_type(SyncOffsetPage[Alias], alias, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.aliases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = response.parse()
        assert_matches_type(SyncOffsetPage[Alias], alias, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.aliases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = response.parse()
            assert_matches_type(SyncOffsetPage[Alias], alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        alias = client.cdn.aliases.delete(
            0,
        )
        assert alias is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cdn.aliases.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = response.parse()
        assert alias is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cdn.aliases.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = response.parse()
            assert alias is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_multiple(self, client: Gcore) -> None:
        alias = client.cdn.aliases.create_multiple(
            items=[{"cname": "shop.customer.com"}],
            resource_id=4567,
        )
        assert_matches_type(AliasCreateMultipleResponse, alias, path=["response"])

    @parametrize
    def test_raw_response_create_multiple(self, client: Gcore) -> None:
        response = client.cdn.aliases.with_raw_response.create_multiple(
            items=[{"cname": "shop.customer.com"}],
            resource_id=4567,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = response.parse()
        assert_matches_type(AliasCreateMultipleResponse, alias, path=["response"])

    @parametrize
    def test_streaming_response_create_multiple(self, client: Gcore) -> None:
        with client.cdn.aliases.with_streaming_response.create_multiple(
            items=[{"cname": "shop.customer.com"}],
            resource_id=4567,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = response.parse()
            assert_matches_type(AliasCreateMultipleResponse, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_multiple(self, client: Gcore) -> None:
        alias = client.cdn.aliases.delete_multiple()
        assert_matches_type(AliasDeleteMultipleResponse, alias, path=["response"])

    @parametrize
    def test_method_delete_multiple_with_all_params(self, client: Gcore) -> None:
        alias = client.cdn.aliases.delete_multiple(
            cnames=["a.customer.com", "b.customer.com"],
            ids=[1, 2, 3],
        )
        assert_matches_type(AliasDeleteMultipleResponse, alias, path=["response"])

    @parametrize
    def test_raw_response_delete_multiple(self, client: Gcore) -> None:
        response = client.cdn.aliases.with_raw_response.delete_multiple()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = response.parse()
        assert_matches_type(AliasDeleteMultipleResponse, alias, path=["response"])

    @parametrize
    def test_streaming_response_delete_multiple(self, client: Gcore) -> None:
        with client.cdn.aliases.with_streaming_response.delete_multiple() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = response.parse()
            assert_matches_type(AliasDeleteMultipleResponse, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        alias = client.cdn.aliases.get(
            0,
        )
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cdn.aliases.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = response.parse()
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cdn.aliases.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = response.parse()
            assert_matches_type(AliasDetail, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_certificate_status(self, client: Gcore) -> None:
        alias = client.cdn.aliases.get_certificate_status(
            0,
        )
        assert_matches_type(AliasCertificateStatus, alias, path=["response"])

    @parametrize
    def test_raw_response_get_certificate_status(self, client: Gcore) -> None:
        response = client.cdn.aliases.with_raw_response.get_certificate_status(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = response.parse()
        assert_matches_type(AliasCertificateStatus, alias, path=["response"])

    @parametrize
    def test_streaming_response_get_certificate_status(self, client: Gcore) -> None:
        with client.cdn.aliases.with_streaming_response.get_certificate_status(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = response.parse()
            assert_matches_type(AliasCertificateStatus, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retry_certificate(self, client: Gcore) -> None:
        alias = client.cdn.aliases.retry_certificate(
            0,
        )
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    def test_raw_response_retry_certificate(self, client: Gcore) -> None:
        response = client.cdn.aliases.with_raw_response.retry_certificate(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = response.parse()
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    def test_streaming_response_retry_certificate(self, client: Gcore) -> None:
        with client.cdn.aliases.with_streaming_response.retry_certificate(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = response.parse()
            assert_matches_type(AliasDetail, alias, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAliases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        alias = await async_client.cdn.aliases.create(
            cname="shop.customer.com",
            resource_id=4567,
        )
        assert_matches_type(Alias, alias, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        alias = await async_client.cdn.aliases.create(
            cname="shop.customer.com",
            resource_id=4567,
            active=True,
            automated=True,
            ssl_id=890,
        )
        assert_matches_type(Alias, alias, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.aliases.with_raw_response.create(
            cname="shop.customer.com",
            resource_id=4567,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = await response.parse()
        assert_matches_type(Alias, alias, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.aliases.with_streaming_response.create(
            cname="shop.customer.com",
            resource_id=4567,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = await response.parse()
            assert_matches_type(Alias, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        alias = await async_client.cdn.aliases.update(
            alias_id=0,
        )
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        alias = await async_client.cdn.aliases.update(
            alias_id=0,
            active=False,
            automated=True,
            ssl_id=891,
        )
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.aliases.with_raw_response.update(
            alias_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = await response.parse()
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.aliases.with_streaming_response.update(
            alias_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = await response.parse()
            assert_matches_type(AliasDetail, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        alias = await async_client.cdn.aliases.list()
        assert_matches_type(AsyncOffsetPage[Alias], alias, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        alias = await async_client.cdn.aliases.list(
            automated=True,
            cname="cname",
            cname_endswith="cname_endswith",
            cname_startswith="cname_startswith",
            limit=1,
            offset=0,
            ordering="ordering",
            resource_id=0,
            resource_id_in="resource_id__in",
            search="search",
            ssl_id=0,
            ssl_status="issued",
            ssl_status_in="ssl_status__in",
            ssl_validity_not_after_gte="ssl_validity_not_after_gte",
            ssl_validity_not_after_lte="ssl_validity_not_after_lte",
            status="active",
            status_in="status__in",
        )
        assert_matches_type(AsyncOffsetPage[Alias], alias, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.aliases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = await response.parse()
        assert_matches_type(AsyncOffsetPage[Alias], alias, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.aliases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = await response.parse()
            assert_matches_type(AsyncOffsetPage[Alias], alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        alias = await async_client.cdn.aliases.delete(
            0,
        )
        assert alias is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.aliases.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = await response.parse()
        assert alias is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.aliases.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = await response.parse()
            assert alias is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_multiple(self, async_client: AsyncGcore) -> None:
        alias = await async_client.cdn.aliases.create_multiple(
            items=[{"cname": "shop.customer.com"}],
            resource_id=4567,
        )
        assert_matches_type(AliasCreateMultipleResponse, alias, path=["response"])

    @parametrize
    async def test_raw_response_create_multiple(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.aliases.with_raw_response.create_multiple(
            items=[{"cname": "shop.customer.com"}],
            resource_id=4567,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = await response.parse()
        assert_matches_type(AliasCreateMultipleResponse, alias, path=["response"])

    @parametrize
    async def test_streaming_response_create_multiple(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.aliases.with_streaming_response.create_multiple(
            items=[{"cname": "shop.customer.com"}],
            resource_id=4567,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = await response.parse()
            assert_matches_type(AliasCreateMultipleResponse, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_multiple(self, async_client: AsyncGcore) -> None:
        alias = await async_client.cdn.aliases.delete_multiple()
        assert_matches_type(AliasDeleteMultipleResponse, alias, path=["response"])

    @parametrize
    async def test_method_delete_multiple_with_all_params(self, async_client: AsyncGcore) -> None:
        alias = await async_client.cdn.aliases.delete_multiple(
            cnames=["a.customer.com", "b.customer.com"],
            ids=[1, 2, 3],
        )
        assert_matches_type(AliasDeleteMultipleResponse, alias, path=["response"])

    @parametrize
    async def test_raw_response_delete_multiple(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.aliases.with_raw_response.delete_multiple()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = await response.parse()
        assert_matches_type(AliasDeleteMultipleResponse, alias, path=["response"])

    @parametrize
    async def test_streaming_response_delete_multiple(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.aliases.with_streaming_response.delete_multiple() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = await response.parse()
            assert_matches_type(AliasDeleteMultipleResponse, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        alias = await async_client.cdn.aliases.get(
            0,
        )
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.aliases.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = await response.parse()
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.aliases.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = await response.parse()
            assert_matches_type(AliasDetail, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_certificate_status(self, async_client: AsyncGcore) -> None:
        alias = await async_client.cdn.aliases.get_certificate_status(
            0,
        )
        assert_matches_type(AliasCertificateStatus, alias, path=["response"])

    @parametrize
    async def test_raw_response_get_certificate_status(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.aliases.with_raw_response.get_certificate_status(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = await response.parse()
        assert_matches_type(AliasCertificateStatus, alias, path=["response"])

    @parametrize
    async def test_streaming_response_get_certificate_status(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.aliases.with_streaming_response.get_certificate_status(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = await response.parse()
            assert_matches_type(AliasCertificateStatus, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retry_certificate(self, async_client: AsyncGcore) -> None:
        alias = await async_client.cdn.aliases.retry_certificate(
            0,
        )
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    async def test_raw_response_retry_certificate(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.aliases.with_raw_response.retry_certificate(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = await response.parse()
        assert_matches_type(AliasDetail, alias, path=["response"])

    @parametrize
    async def test_streaming_response_retry_certificate(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.aliases.with_streaming_response.retry_certificate(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = await response.parse()
            assert_matches_type(AliasDetail, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

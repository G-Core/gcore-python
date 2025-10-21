# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn import (
    AwsRegions,
    CdnAccount,
    AlibabaRegions,
    CdnAccountLimits,
    CdnAvailableFeatures,
    CdnListPurgeStatusesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCdn:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_account_limits(self, client: Gcore) -> None:
        cdn = client.cdn.get_account_limits()
        assert_matches_type(CdnAccountLimits, cdn, path=["response"])

    @parametrize
    def test_raw_response_get_account_limits(self, client: Gcore) -> None:
        response = client.cdn.with_raw_response.get_account_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = response.parse()
        assert_matches_type(CdnAccountLimits, cdn, path=["response"])

    @parametrize
    def test_streaming_response_get_account_limits(self, client: Gcore) -> None:
        with client.cdn.with_streaming_response.get_account_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = response.parse()
            assert_matches_type(CdnAccountLimits, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_account_overview(self, client: Gcore) -> None:
        cdn = client.cdn.get_account_overview()
        assert_matches_type(CdnAccount, cdn, path=["response"])

    @parametrize
    def test_raw_response_get_account_overview(self, client: Gcore) -> None:
        response = client.cdn.with_raw_response.get_account_overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = response.parse()
        assert_matches_type(CdnAccount, cdn, path=["response"])

    @parametrize
    def test_streaming_response_get_account_overview(self, client: Gcore) -> None:
        with client.cdn.with_streaming_response.get_account_overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = response.parse()
            assert_matches_type(CdnAccount, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_available_features(self, client: Gcore) -> None:
        cdn = client.cdn.get_available_features()
        assert_matches_type(CdnAvailableFeatures, cdn, path=["response"])

    @parametrize
    def test_raw_response_get_available_features(self, client: Gcore) -> None:
        response = client.cdn.with_raw_response.get_available_features()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = response.parse()
        assert_matches_type(CdnAvailableFeatures, cdn, path=["response"])

    @parametrize
    def test_streaming_response_get_available_features(self, client: Gcore) -> None:
        with client.cdn.with_streaming_response.get_available_features() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = response.parse()
            assert_matches_type(CdnAvailableFeatures, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_alibaba_regions(self, client: Gcore) -> None:
        cdn = client.cdn.list_alibaba_regions()
        assert_matches_type(AlibabaRegions, cdn, path=["response"])

    @parametrize
    def test_raw_response_list_alibaba_regions(self, client: Gcore) -> None:
        response = client.cdn.with_raw_response.list_alibaba_regions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = response.parse()
        assert_matches_type(AlibabaRegions, cdn, path=["response"])

    @parametrize
    def test_streaming_response_list_alibaba_regions(self, client: Gcore) -> None:
        with client.cdn.with_streaming_response.list_alibaba_regions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = response.parse()
            assert_matches_type(AlibabaRegions, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_aws_regions(self, client: Gcore) -> None:
        cdn = client.cdn.list_aws_regions()
        assert_matches_type(AwsRegions, cdn, path=["response"])

    @parametrize
    def test_raw_response_list_aws_regions(self, client: Gcore) -> None:
        response = client.cdn.with_raw_response.list_aws_regions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = response.parse()
        assert_matches_type(AwsRegions, cdn, path=["response"])

    @parametrize
    def test_streaming_response_list_aws_regions(self, client: Gcore) -> None:
        with client.cdn.with_streaming_response.list_aws_regions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = response.parse()
            assert_matches_type(AwsRegions, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_purge_statuses(self, client: Gcore) -> None:
        cdn = client.cdn.list_purge_statuses()
        assert_matches_type(CdnListPurgeStatusesResponse, cdn, path=["response"])

    @parametrize
    def test_method_list_purge_statuses_with_all_params(self, client: Gcore) -> None:
        cdn = client.cdn.list_purge_statuses(
            cname="cname",
            from_created="from_created",
            limit=100,
            offset=0,
            purge_type="purge_type",
            status="status",
            to_created="to_created",
        )
        assert_matches_type(CdnListPurgeStatusesResponse, cdn, path=["response"])

    @parametrize
    def test_raw_response_list_purge_statuses(self, client: Gcore) -> None:
        response = client.cdn.with_raw_response.list_purge_statuses()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = response.parse()
        assert_matches_type(CdnListPurgeStatusesResponse, cdn, path=["response"])

    @parametrize
    def test_streaming_response_list_purge_statuses(self, client: Gcore) -> None:
        with client.cdn.with_streaming_response.list_purge_statuses() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = response.parse()
            assert_matches_type(CdnListPurgeStatusesResponse, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_account(self, client: Gcore) -> None:
        cdn = client.cdn.update_account()
        assert_matches_type(CdnAccount, cdn, path=["response"])

    @parametrize
    def test_method_update_account_with_all_params(self, client: Gcore) -> None:
        cdn = client.cdn.update_account(
            utilization_level=1111,
        )
        assert_matches_type(CdnAccount, cdn, path=["response"])

    @parametrize
    def test_raw_response_update_account(self, client: Gcore) -> None:
        response = client.cdn.with_raw_response.update_account()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = response.parse()
        assert_matches_type(CdnAccount, cdn, path=["response"])

    @parametrize
    def test_streaming_response_update_account(self, client: Gcore) -> None:
        with client.cdn.with_streaming_response.update_account() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = response.parse()
            assert_matches_type(CdnAccount, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCdn:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_account_limits(self, async_client: AsyncGcore) -> None:
        cdn = await async_client.cdn.get_account_limits()
        assert_matches_type(CdnAccountLimits, cdn, path=["response"])

    @parametrize
    async def test_raw_response_get_account_limits(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.with_raw_response.get_account_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = await response.parse()
        assert_matches_type(CdnAccountLimits, cdn, path=["response"])

    @parametrize
    async def test_streaming_response_get_account_limits(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.with_streaming_response.get_account_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = await response.parse()
            assert_matches_type(CdnAccountLimits, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_account_overview(self, async_client: AsyncGcore) -> None:
        cdn = await async_client.cdn.get_account_overview()
        assert_matches_type(CdnAccount, cdn, path=["response"])

    @parametrize
    async def test_raw_response_get_account_overview(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.with_raw_response.get_account_overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = await response.parse()
        assert_matches_type(CdnAccount, cdn, path=["response"])

    @parametrize
    async def test_streaming_response_get_account_overview(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.with_streaming_response.get_account_overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = await response.parse()
            assert_matches_type(CdnAccount, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_available_features(self, async_client: AsyncGcore) -> None:
        cdn = await async_client.cdn.get_available_features()
        assert_matches_type(CdnAvailableFeatures, cdn, path=["response"])

    @parametrize
    async def test_raw_response_get_available_features(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.with_raw_response.get_available_features()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = await response.parse()
        assert_matches_type(CdnAvailableFeatures, cdn, path=["response"])

    @parametrize
    async def test_streaming_response_get_available_features(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.with_streaming_response.get_available_features() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = await response.parse()
            assert_matches_type(CdnAvailableFeatures, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_alibaba_regions(self, async_client: AsyncGcore) -> None:
        cdn = await async_client.cdn.list_alibaba_regions()
        assert_matches_type(AlibabaRegions, cdn, path=["response"])

    @parametrize
    async def test_raw_response_list_alibaba_regions(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.with_raw_response.list_alibaba_regions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = await response.parse()
        assert_matches_type(AlibabaRegions, cdn, path=["response"])

    @parametrize
    async def test_streaming_response_list_alibaba_regions(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.with_streaming_response.list_alibaba_regions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = await response.parse()
            assert_matches_type(AlibabaRegions, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_aws_regions(self, async_client: AsyncGcore) -> None:
        cdn = await async_client.cdn.list_aws_regions()
        assert_matches_type(AwsRegions, cdn, path=["response"])

    @parametrize
    async def test_raw_response_list_aws_regions(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.with_raw_response.list_aws_regions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = await response.parse()
        assert_matches_type(AwsRegions, cdn, path=["response"])

    @parametrize
    async def test_streaming_response_list_aws_regions(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.with_streaming_response.list_aws_regions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = await response.parse()
            assert_matches_type(AwsRegions, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_purge_statuses(self, async_client: AsyncGcore) -> None:
        cdn = await async_client.cdn.list_purge_statuses()
        assert_matches_type(CdnListPurgeStatusesResponse, cdn, path=["response"])

    @parametrize
    async def test_method_list_purge_statuses_with_all_params(self, async_client: AsyncGcore) -> None:
        cdn = await async_client.cdn.list_purge_statuses(
            cname="cname",
            from_created="from_created",
            limit=100,
            offset=0,
            purge_type="purge_type",
            status="status",
            to_created="to_created",
        )
        assert_matches_type(CdnListPurgeStatusesResponse, cdn, path=["response"])

    @parametrize
    async def test_raw_response_list_purge_statuses(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.with_raw_response.list_purge_statuses()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = await response.parse()
        assert_matches_type(CdnListPurgeStatusesResponse, cdn, path=["response"])

    @parametrize
    async def test_streaming_response_list_purge_statuses(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.with_streaming_response.list_purge_statuses() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = await response.parse()
            assert_matches_type(CdnListPurgeStatusesResponse, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_account(self, async_client: AsyncGcore) -> None:
        cdn = await async_client.cdn.update_account()
        assert_matches_type(CdnAccount, cdn, path=["response"])

    @parametrize
    async def test_method_update_account_with_all_params(self, async_client: AsyncGcore) -> None:
        cdn = await async_client.cdn.update_account(
            utilization_level=1111,
        )
        assert_matches_type(CdnAccount, cdn, path=["response"])

    @parametrize
    async def test_raw_response_update_account(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.with_raw_response.update_account()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdn = await response.parse()
        assert_matches_type(CdnAccount, cdn, path=["response"])

    @parametrize
    async def test_streaming_response_update_account(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.with_streaming_response.update_account() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdn = await response.parse()
            assert_matches_type(CdnAccount, cdn, path=["response"])

        assert cast(Any, response.is_closed) is True

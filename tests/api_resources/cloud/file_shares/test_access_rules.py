# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.file_shares import AccessRule, AccessRuleList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        access_rule = client.cloud.file_shares.access_rules.create(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            access_mode="ro",
            ip_address="192.168.1.1",
        )
        assert_matches_type(AccessRule, access_rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.file_shares.access_rules.with_raw_response.create(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            access_mode="ro",
            ip_address="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(AccessRule, access_rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.file_shares.access_rules.with_streaming_response.create(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            access_mode="ro",
            ip_address="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(AccessRule, access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            client.cloud.file_shares.access_rules.with_raw_response.create(
                file_share_id="",
                project_id=1,
                region_id=1,
                access_mode="ro",
                ip_address="192.168.1.1",
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        access_rule = client.cloud.file_shares.access_rules.list(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(AccessRuleList, access_rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.file_shares.access_rules.with_raw_response.list(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(AccessRuleList, access_rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.file_shares.access_rules.with_streaming_response.list(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(AccessRuleList, access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            client.cloud.file_shares.access_rules.with_raw_response.list(
                file_share_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        access_rule = client.cloud.file_shares.access_rules.delete(
            access_rule_id="4f09d7dd-f1f8-4352-b015-741b2192db47",
            project_id=1,
            region_id=1,
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
        )
        assert access_rule is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.file_shares.access_rules.with_raw_response.delete(
            access_rule_id="4f09d7dd-f1f8-4352-b015-741b2192db47",
            project_id=1,
            region_id=1,
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert access_rule is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.file_shares.access_rules.with_streaming_response.delete(
            access_rule_id="4f09d7dd-f1f8-4352-b015-741b2192db47",
            project_id=1,
            region_id=1,
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert access_rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            client.cloud.file_shares.access_rules.with_raw_response.delete(
                access_rule_id="4f09d7dd-f1f8-4352-b015-741b2192db47",
                project_id=1,
                region_id=1,
                file_share_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_rule_id` but received ''"):
            client.cloud.file_shares.access_rules.with_raw_response.delete(
                access_rule_id="",
                project_id=1,
                region_id=1,
                file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            )


class TestAsyncAccessRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        access_rule = await async_client.cloud.file_shares.access_rules.create(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            access_mode="ro",
            ip_address="192.168.1.1",
        )
        assert_matches_type(AccessRule, access_rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.file_shares.access_rules.with_raw_response.create(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            access_mode="ro",
            ip_address="192.168.1.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(AccessRule, access_rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.file_shares.access_rules.with_streaming_response.create(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
            access_mode="ro",
            ip_address="192.168.1.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(AccessRule, access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            await async_client.cloud.file_shares.access_rules.with_raw_response.create(
                file_share_id="",
                project_id=1,
                region_id=1,
                access_mode="ro",
                ip_address="192.168.1.1",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        access_rule = await async_client.cloud.file_shares.access_rules.list(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(AccessRuleList, access_rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.file_shares.access_rules.with_raw_response.list(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(AccessRuleList, access_rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.file_shares.access_rules.with_streaming_response.list(
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(AccessRuleList, access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            await async_client.cloud.file_shares.access_rules.with_raw_response.list(
                file_share_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        access_rule = await async_client.cloud.file_shares.access_rules.delete(
            access_rule_id="4f09d7dd-f1f8-4352-b015-741b2192db47",
            project_id=1,
            region_id=1,
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
        )
        assert access_rule is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.file_shares.access_rules.with_raw_response.delete(
            access_rule_id="4f09d7dd-f1f8-4352-b015-741b2192db47",
            project_id=1,
            region_id=1,
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert access_rule is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.file_shares.access_rules.with_streaming_response.delete(
            access_rule_id="4f09d7dd-f1f8-4352-b015-741b2192db47",
            project_id=1,
            region_id=1,
            file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert access_rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_share_id` but received ''"):
            await async_client.cloud.file_shares.access_rules.with_raw_response.delete(
                access_rule_id="4f09d7dd-f1f8-4352-b015-741b2192db47",
                project_id=1,
                region_id=1,
                file_share_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_rule_id` but received ''"):
            await async_client.cloud.file_shares.access_rules.with_raw_response.delete(
                access_rule_id="",
                project_id=1,
                region_id=1,
                file_share_id="bd8c47ee-e565-4e26-8840-b537e6827b08",
            )

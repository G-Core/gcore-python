# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn import (
    OriginGroups,
    OriginGroupsList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOriginGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.create(
            name="YourOriginGroup",
            sources=[{}, {}],
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.create(
            name="YourOriginGroup",
            sources=[
                {
                    "backup": False,
                    "enabled": True,
                    "source": "yourwebsite.com",
                },
                {
                    "backup": True,
                    "enabled": True,
                    "source": "1.2.3.4:5500",
                },
            ],
            auth_type="none",
            proxy_next_upstream=["error", "timeout", "invalid_header", "http_500", "http_502", "http_503", "http_504"],
            use_next=True,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Gcore) -> None:
        response = client.cdn.origin_groups.with_raw_response.create(
            name="YourOriginGroup",
            sources=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gcore) -> None:
        with client.cdn.origin_groups.with_streaming_response.create(
            name="YourOriginGroup",
            sources=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.create(
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.create(
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
                "s3_region": "us-east-2",
                "s3_storage_hostname": "s3_storage_hostname",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
            proxy_next_upstream=["error", "timeout", "invalid_header", "http_500", "http_502", "http_503", "http_504"],
            use_next=True,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Gcore) -> None:
        response = client.cdn.origin_groups.with_raw_response.create(
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gcore) -> None:
        with client.cdn.origin_groups.with_streaming_response.create(
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_1(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.update(
            origin_group_id=0,
            name="YourOriginGroup",
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.update(
            origin_group_id=0,
            name="YourOriginGroup",
            auth_type="none",
            path="",
            proxy_next_upstream=["error", "timeout", "invalid_header", "http_500", "http_502", "http_503", "http_504"],
            sources=[
                {
                    "backup": False,
                    "enabled": True,
                    "source": "yourdomain.com",
                }
            ],
            use_next=True,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Gcore) -> None:
        response = client.cdn.origin_groups.with_raw_response.update(
            origin_group_id=0,
            name="YourOriginGroup",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Gcore) -> None:
        with client.cdn.origin_groups.with_streaming_response.update(
            origin_group_id=0,
            name="YourOriginGroup",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_2(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.update(
            origin_group_id=0,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.update(
            origin_group_id=0,
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
                "s3_region": "us-east-2",
                "s3_storage_hostname": "s3_storage_hostname",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
            path="",
            proxy_next_upstream=["error", "timeout", "invalid_header", "http_500", "http_502", "http_503", "http_504"],
            use_next=True,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Gcore) -> None:
        response = client.cdn.origin_groups.with_raw_response.update(
            origin_group_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Gcore) -> None:
        with client.cdn.origin_groups.with_streaming_response.update(
            origin_group_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.list()
        assert_matches_type(OriginGroupsList, origin_group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.list(
            has_related_resources=True,
            name="name",
            sources="sources",
        )
        assert_matches_type(OriginGroupsList, origin_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.origin_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = response.parse()
        assert_matches_type(OriginGroupsList, origin_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.origin_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = response.parse()
            assert_matches_type(OriginGroupsList, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.delete(
            0,
        )
        assert origin_group is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cdn.origin_groups.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = response.parse()
        assert origin_group is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cdn.origin_groups.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = response.parse()
            assert origin_group is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.get(
            0,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cdn.origin_groups.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cdn.origin_groups.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace_overload_1(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.replace(
            origin_group_id=0,
            auth_type="none",
            name="YourOriginGroup",
            path="",
            sources=[{}],
            use_next=True,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_method_replace_with_all_params_overload_1(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.replace(
            origin_group_id=0,
            auth_type="none",
            name="YourOriginGroup",
            path="",
            sources=[
                {
                    "backup": False,
                    "enabled": True,
                    "source": "yourdomain.com",
                }
            ],
            use_next=True,
            proxy_next_upstream=["error", "timeout", "invalid_header", "http_500", "http_502", "http_503", "http_504"],
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_raw_response_replace_overload_1(self, client: Gcore) -> None:
        response = client.cdn.origin_groups.with_raw_response.replace(
            origin_group_id=0,
            auth_type="none",
            name="YourOriginGroup",
            path="",
            sources=[{}],
            use_next=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_streaming_response_replace_overload_1(self, client: Gcore) -> None:
        with client.cdn.origin_groups.with_streaming_response.replace(
            origin_group_id=0,
            auth_type="none",
            name="YourOriginGroup",
            path="",
            sources=[{}],
            use_next=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace_overload_2(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.replace(
            origin_group_id=0,
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
            path="",
            use_next=True,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_method_replace_with_all_params_overload_2(self, client: Gcore) -> None:
        origin_group = client.cdn.origin_groups.replace(
            origin_group_id=0,
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
                "s3_region": "us-east-2",
                "s3_storage_hostname": "s3_storage_hostname",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
            path="",
            use_next=True,
            proxy_next_upstream=["error", "timeout", "invalid_header", "http_500", "http_502", "http_503", "http_504"],
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_raw_response_replace_overload_2(self, client: Gcore) -> None:
        response = client.cdn.origin_groups.with_raw_response.replace(
            origin_group_id=0,
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
            path="",
            use_next=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    def test_streaming_response_replace_overload_2(self, client: Gcore) -> None:
        with client.cdn.origin_groups.with_streaming_response.replace(
            origin_group_id=0,
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
            path="",
            use_next=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOriginGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.create(
            name="YourOriginGroup",
            sources=[{}, {}],
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.create(
            name="YourOriginGroup",
            sources=[
                {
                    "backup": False,
                    "enabled": True,
                    "source": "yourwebsite.com",
                },
                {
                    "backup": True,
                    "enabled": True,
                    "source": "1.2.3.4:5500",
                },
            ],
            auth_type="none",
            proxy_next_upstream=["error", "timeout", "invalid_header", "http_500", "http_502", "http_503", "http_504"],
            use_next=True,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.origin_groups.with_raw_response.create(
            name="YourOriginGroup",
            sources=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = await response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.origin_groups.with_streaming_response.create(
            name="YourOriginGroup",
            sources=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = await response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.create(
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.create(
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
                "s3_region": "us-east-2",
                "s3_storage_hostname": "s3_storage_hostname",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
            proxy_next_upstream=["error", "timeout", "invalid_header", "http_500", "http_502", "http_503", "http_504"],
            use_next=True,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.origin_groups.with_raw_response.create(
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = await response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.origin_groups.with_streaming_response.create(
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = await response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.update(
            origin_group_id=0,
            name="YourOriginGroup",
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.update(
            origin_group_id=0,
            name="YourOriginGroup",
            auth_type="none",
            path="",
            proxy_next_upstream=["error", "timeout", "invalid_header", "http_500", "http_502", "http_503", "http_504"],
            sources=[
                {
                    "backup": False,
                    "enabled": True,
                    "source": "yourdomain.com",
                }
            ],
            use_next=True,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.origin_groups.with_raw_response.update(
            origin_group_id=0,
            name="YourOriginGroup",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = await response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.origin_groups.with_streaming_response.update(
            origin_group_id=0,
            name="YourOriginGroup",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = await response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.update(
            origin_group_id=0,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.update(
            origin_group_id=0,
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
                "s3_region": "us-east-2",
                "s3_storage_hostname": "s3_storage_hostname",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
            path="",
            proxy_next_upstream=["error", "timeout", "invalid_header", "http_500", "http_502", "http_503", "http_504"],
            use_next=True,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.origin_groups.with_raw_response.update(
            origin_group_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = await response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.origin_groups.with_streaming_response.update(
            origin_group_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = await response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.list()
        assert_matches_type(OriginGroupsList, origin_group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.list(
            has_related_resources=True,
            name="name",
            sources="sources",
        )
        assert_matches_type(OriginGroupsList, origin_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.origin_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = await response.parse()
        assert_matches_type(OriginGroupsList, origin_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.origin_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = await response.parse()
            assert_matches_type(OriginGroupsList, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.delete(
            0,
        )
        assert origin_group is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.origin_groups.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = await response.parse()
        assert origin_group is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.origin_groups.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = await response.parse()
            assert origin_group is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.get(
            0,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.origin_groups.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = await response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.origin_groups.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = await response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace_overload_1(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.replace(
            origin_group_id=0,
            auth_type="none",
            name="YourOriginGroup",
            path="",
            sources=[{}],
            use_next=True,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params_overload_1(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.replace(
            origin_group_id=0,
            auth_type="none",
            name="YourOriginGroup",
            path="",
            sources=[
                {
                    "backup": False,
                    "enabled": True,
                    "source": "yourdomain.com",
                }
            ],
            use_next=True,
            proxy_next_upstream=["error", "timeout", "invalid_header", "http_500", "http_502", "http_503", "http_504"],
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_raw_response_replace_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.origin_groups.with_raw_response.replace(
            origin_group_id=0,
            auth_type="none",
            name="YourOriginGroup",
            path="",
            sources=[{}],
            use_next=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = await response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_streaming_response_replace_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.origin_groups.with_streaming_response.replace(
            origin_group_id=0,
            auth_type="none",
            name="YourOriginGroup",
            path="",
            sources=[{}],
            use_next=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = await response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace_overload_2(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.replace(
            origin_group_id=0,
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
            path="",
            use_next=True,
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params_overload_2(self, async_client: AsyncGcore) -> None:
        origin_group = await async_client.cdn.origin_groups.replace(
            origin_group_id=0,
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
                "s3_region": "us-east-2",
                "s3_storage_hostname": "s3_storage_hostname",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
            path="",
            use_next=True,
            proxy_next_upstream=["error", "timeout", "invalid_header", "http_500", "http_502", "http_503", "http_504"],
        )
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_raw_response_replace_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.origin_groups.with_raw_response.replace(
            origin_group_id=0,
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
            path="",
            use_next=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_group = await response.parse()
        assert_matches_type(OriginGroups, origin_group, path=["response"])

    @parametrize
    async def test_streaming_response_replace_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.origin_groups.with_streaming_response.replace(
            origin_group_id=0,
            auth={
                "s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
                "s3_bucket_name": "bucket_name",
                "s3_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "s3_type": "amazon",
            },
            auth_type="awsSignatureV4",
            name="YourOriginGroup",
            path="",
            use_next=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_group = await response.parse()
            assert_matches_type(OriginGroups, origin_group, path=["response"])

        assert cast(Any, response.is_closed) is True

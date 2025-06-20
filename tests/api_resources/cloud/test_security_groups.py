# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import (
    SecurityGroup,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecurityGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        security_group = client.cloud.security_groups.create(
            project_id=0,
            region_id=0,
            security_group={"name": "my_security_group"},
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        security_group = client.cloud.security_groups.create(
            project_id=0,
            region_id=0,
            security_group={
                "name": "my_security_group",
                "description": "Some description",
                "security_group_rules": [
                    {
                        "description": "Some description",
                        "direction": "ingress",
                        "ethertype": "IPv4",
                        "port_range_max": 80,
                        "port_range_min": 80,
                        "protocol": "tcp",
                        "remote_group_id": "00000000-0000-4000-8000-000000000000",
                        "remote_ip_prefix": "10.0.0.0/8",
                    }
                ],
                "tags": {"my-tag": "bar"},
            },
            instances=["00000000-0000-4000-8000-000000000000"],
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.security_groups.with_raw_response.create(
            project_id=0,
            region_id=0,
            security_group={"name": "my_security_group"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = response.parse()
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.security_groups.with_streaming_response.create(
            project_id=0,
            region_id=0,
            security_group={"name": "my_security_group"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = response.parse()
            assert_matches_type(SecurityGroup, security_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        security_group = client.cloud.security_groups.update(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        security_group = client.cloud.security_groups.update(
            group_id="group_id",
            project_id=0,
            region_id=0,
            changed_rules=[
                {
                    "action": "delete",
                    "description": "Some description",
                    "direction": "egress",
                    "ethertype": "IPv4",
                    "port_range_max": 80,
                    "port_range_min": 80,
                    "protocol": "tcp",
                    "remote_group_id": "00000000-0000-4000-8000-000000000000",
                    "remote_ip_prefix": "10.0.0.0/8",
                    "security_group_rule_id": "00000000-0000-4000-8000-000000000000",
                }
            ],
            name="some_name",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.security_groups.with_raw_response.update(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = response.parse()
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.security_groups.with_streaming_response.update(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = response.parse()
            assert_matches_type(SecurityGroup, security_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.cloud.security_groups.with_raw_response.update(
                group_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        security_group = client.cloud.security_groups.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SyncOffsetPage[SecurityGroup], security_group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        security_group = client.cloud.security_groups.list(
            project_id=0,
            region_id=0,
            limit=0,
            offset=0,
            tag_key=["string"],
            tag_key_value="tag_key_value",
        )
        assert_matches_type(SyncOffsetPage[SecurityGroup], security_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.security_groups.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = response.parse()
        assert_matches_type(SyncOffsetPage[SecurityGroup], security_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.security_groups.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = response.parse()
            assert_matches_type(SyncOffsetPage[SecurityGroup], security_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        security_group = client.cloud.security_groups.delete(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert security_group is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.security_groups.with_raw_response.delete(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = response.parse()
        assert security_group is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.security_groups.with_streaming_response.delete(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = response.parse()
            assert security_group is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.cloud.security_groups.with_raw_response.delete(
                group_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_copy(self, client: Gcore) -> None:
        security_group = client.cloud.security_groups.copy(
            group_id="group_id",
            project_id=0,
            region_id=0,
            name="some_name",
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    def test_raw_response_copy(self, client: Gcore) -> None:
        response = client.cloud.security_groups.with_raw_response.copy(
            group_id="group_id",
            project_id=0,
            region_id=0,
            name="some_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = response.parse()
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    def test_streaming_response_copy(self, client: Gcore) -> None:
        with client.cloud.security_groups.with_streaming_response.copy(
            group_id="group_id",
            project_id=0,
            region_id=0,
            name="some_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = response.parse()
            assert_matches_type(SecurityGroup, security_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_copy(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.cloud.security_groups.with_raw_response.copy(
                group_id="",
                project_id=0,
                region_id=0,
                name="some_name",
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        security_group = client.cloud.security_groups.get(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.security_groups.with_raw_response.get(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = response.parse()
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.security_groups.with_streaming_response.get(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = response.parse()
            assert_matches_type(SecurityGroup, security_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.cloud.security_groups.with_raw_response.get(
                group_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_revert_to_default(self, client: Gcore) -> None:
        security_group = client.cloud.security_groups.revert_to_default(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    def test_raw_response_revert_to_default(self, client: Gcore) -> None:
        response = client.cloud.security_groups.with_raw_response.revert_to_default(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = response.parse()
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    def test_streaming_response_revert_to_default(self, client: Gcore) -> None:
        with client.cloud.security_groups.with_streaming_response.revert_to_default(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = response.parse()
            assert_matches_type(SecurityGroup, security_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revert_to_default(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.cloud.security_groups.with_raw_response.revert_to_default(
                group_id="",
                project_id=0,
                region_id=0,
            )


class TestAsyncSecurityGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        security_group = await async_client.cloud.security_groups.create(
            project_id=0,
            region_id=0,
            security_group={"name": "my_security_group"},
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        security_group = await async_client.cloud.security_groups.create(
            project_id=0,
            region_id=0,
            security_group={
                "name": "my_security_group",
                "description": "Some description",
                "security_group_rules": [
                    {
                        "description": "Some description",
                        "direction": "ingress",
                        "ethertype": "IPv4",
                        "port_range_max": 80,
                        "port_range_min": 80,
                        "protocol": "tcp",
                        "remote_group_id": "00000000-0000-4000-8000-000000000000",
                        "remote_ip_prefix": "10.0.0.0/8",
                    }
                ],
                "tags": {"my-tag": "bar"},
            },
            instances=["00000000-0000-4000-8000-000000000000"],
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.security_groups.with_raw_response.create(
            project_id=0,
            region_id=0,
            security_group={"name": "my_security_group"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = await response.parse()
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.security_groups.with_streaming_response.create(
            project_id=0,
            region_id=0,
            security_group={"name": "my_security_group"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = await response.parse()
            assert_matches_type(SecurityGroup, security_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        security_group = await async_client.cloud.security_groups.update(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        security_group = await async_client.cloud.security_groups.update(
            group_id="group_id",
            project_id=0,
            region_id=0,
            changed_rules=[
                {
                    "action": "delete",
                    "description": "Some description",
                    "direction": "egress",
                    "ethertype": "IPv4",
                    "port_range_max": 80,
                    "port_range_min": 80,
                    "protocol": "tcp",
                    "remote_group_id": "00000000-0000-4000-8000-000000000000",
                    "remote_ip_prefix": "10.0.0.0/8",
                    "security_group_rule_id": "00000000-0000-4000-8000-000000000000",
                }
            ],
            name="some_name",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.security_groups.with_raw_response.update(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = await response.parse()
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.security_groups.with_streaming_response.update(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = await response.parse()
            assert_matches_type(SecurityGroup, security_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.cloud.security_groups.with_raw_response.update(
                group_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        security_group = await async_client.cloud.security_groups.list(
            project_id=0,
            region_id=0,
        )
        assert_matches_type(AsyncOffsetPage[SecurityGroup], security_group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        security_group = await async_client.cloud.security_groups.list(
            project_id=0,
            region_id=0,
            limit=0,
            offset=0,
            tag_key=["string"],
            tag_key_value="tag_key_value",
        )
        assert_matches_type(AsyncOffsetPage[SecurityGroup], security_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.security_groups.with_raw_response.list(
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = await response.parse()
        assert_matches_type(AsyncOffsetPage[SecurityGroup], security_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.security_groups.with_streaming_response.list(
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = await response.parse()
            assert_matches_type(AsyncOffsetPage[SecurityGroup], security_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        security_group = await async_client.cloud.security_groups.delete(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert security_group is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.security_groups.with_raw_response.delete(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = await response.parse()
        assert security_group is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.security_groups.with_streaming_response.delete(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = await response.parse()
            assert security_group is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.cloud.security_groups.with_raw_response.delete(
                group_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_copy(self, async_client: AsyncGcore) -> None:
        security_group = await async_client.cloud.security_groups.copy(
            group_id="group_id",
            project_id=0,
            region_id=0,
            name="some_name",
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    async def test_raw_response_copy(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.security_groups.with_raw_response.copy(
            group_id="group_id",
            project_id=0,
            region_id=0,
            name="some_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = await response.parse()
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    async def test_streaming_response_copy(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.security_groups.with_streaming_response.copy(
            group_id="group_id",
            project_id=0,
            region_id=0,
            name="some_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = await response.parse()
            assert_matches_type(SecurityGroup, security_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_copy(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.cloud.security_groups.with_raw_response.copy(
                group_id="",
                project_id=0,
                region_id=0,
                name="some_name",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        security_group = await async_client.cloud.security_groups.get(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.security_groups.with_raw_response.get(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = await response.parse()
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.security_groups.with_streaming_response.get(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = await response.parse()
            assert_matches_type(SecurityGroup, security_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.cloud.security_groups.with_raw_response.get(
                group_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_revert_to_default(self, async_client: AsyncGcore) -> None:
        security_group = await async_client.cloud.security_groups.revert_to_default(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    async def test_raw_response_revert_to_default(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.security_groups.with_raw_response.revert_to_default(
            group_id="group_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_group = await response.parse()
        assert_matches_type(SecurityGroup, security_group, path=["response"])

    @parametrize
    async def test_streaming_response_revert_to_default(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.security_groups.with_streaming_response.revert_to_default(
            group_id="group_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_group = await response.parse()
            assert_matches_type(SecurityGroup, security_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revert_to_default(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.cloud.security_groups.with_raw_response.revert_to_default(
                group_id="",
                project_id=0,
                region_id=0,
            )

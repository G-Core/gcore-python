# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import SSHKey, SSHKeyCreated

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSSHKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        ssh_key = client.cloud.ssh_keys.create(
            project_id=1,
            name="my-ssh-key",
        )
        assert_matches_type(SSHKeyCreated, ssh_key, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        ssh_key = client.cloud.ssh_keys.create(
            project_id=1,
            name="my-ssh-key",
            public_key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIjxL6g1II8NsO8odvBwGKvq2Dx/h/xrvsV9b9LVIYKm my-username@my-hostname",
            shared_in_project=True,
        )
        assert_matches_type(SSHKeyCreated, ssh_key, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.ssh_keys.with_raw_response.create(
            project_id=1,
            name="my-ssh-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = response.parse()
        assert_matches_type(SSHKeyCreated, ssh_key, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.ssh_keys.with_streaming_response.create(
            project_id=1,
            name="my-ssh-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = response.parse()
            assert_matches_type(SSHKeyCreated, ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        ssh_key = client.cloud.ssh_keys.update(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
            shared_in_project=True,
        )
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.ssh_keys.with_raw_response.update(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
            shared_in_project=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = response.parse()
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.ssh_keys.with_streaming_response.update(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
            shared_in_project=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = response.parse()
            assert_matches_type(SSHKey, ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ssh_key_id` but received ''"):
            client.cloud.ssh_keys.with_raw_response.update(
                ssh_key_id="",
                project_id=1,
                shared_in_project=True,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        ssh_key = client.cloud.ssh_keys.list(
            project_id=1,
        )
        assert_matches_type(SyncOffsetPage[SSHKey], ssh_key, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        ssh_key = client.cloud.ssh_keys.list(
            project_id=1,
            limit=100,
            offset=0,
            order_by="created_at.desc",
        )
        assert_matches_type(SyncOffsetPage[SSHKey], ssh_key, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.ssh_keys.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = response.parse()
        assert_matches_type(SyncOffsetPage[SSHKey], ssh_key, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.ssh_keys.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = response.parse()
            assert_matches_type(SyncOffsetPage[SSHKey], ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        ssh_key = client.cloud.ssh_keys.delete(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
        )
        assert ssh_key is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.ssh_keys.with_raw_response.delete(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = response.parse()
        assert ssh_key is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.ssh_keys.with_streaming_response.delete(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = response.parse()
            assert ssh_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ssh_key_id` but received ''"):
            client.cloud.ssh_keys.with_raw_response.delete(
                ssh_key_id="",
                project_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        ssh_key = client.cloud.ssh_keys.get(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
        )
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.ssh_keys.with_raw_response.get(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = response.parse()
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.ssh_keys.with_streaming_response.get(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = response.parse()
            assert_matches_type(SSHKey, ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ssh_key_id` but received ''"):
            client.cloud.ssh_keys.with_raw_response.get(
                ssh_key_id="",
                project_id=1,
            )


class TestAsyncSSHKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        ssh_key = await async_client.cloud.ssh_keys.create(
            project_id=1,
            name="my-ssh-key",
        )
        assert_matches_type(SSHKeyCreated, ssh_key, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        ssh_key = await async_client.cloud.ssh_keys.create(
            project_id=1,
            name="my-ssh-key",
            public_key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIjxL6g1II8NsO8odvBwGKvq2Dx/h/xrvsV9b9LVIYKm my-username@my-hostname",
            shared_in_project=True,
        )
        assert_matches_type(SSHKeyCreated, ssh_key, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.ssh_keys.with_raw_response.create(
            project_id=1,
            name="my-ssh-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = await response.parse()
        assert_matches_type(SSHKeyCreated, ssh_key, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.ssh_keys.with_streaming_response.create(
            project_id=1,
            name="my-ssh-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = await response.parse()
            assert_matches_type(SSHKeyCreated, ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        ssh_key = await async_client.cloud.ssh_keys.update(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
            shared_in_project=True,
        )
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.ssh_keys.with_raw_response.update(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
            shared_in_project=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = await response.parse()
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.ssh_keys.with_streaming_response.update(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
            shared_in_project=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = await response.parse()
            assert_matches_type(SSHKey, ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ssh_key_id` but received ''"):
            await async_client.cloud.ssh_keys.with_raw_response.update(
                ssh_key_id="",
                project_id=1,
                shared_in_project=True,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        ssh_key = await async_client.cloud.ssh_keys.list(
            project_id=1,
        )
        assert_matches_type(AsyncOffsetPage[SSHKey], ssh_key, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        ssh_key = await async_client.cloud.ssh_keys.list(
            project_id=1,
            limit=100,
            offset=0,
            order_by="created_at.desc",
        )
        assert_matches_type(AsyncOffsetPage[SSHKey], ssh_key, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.ssh_keys.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = await response.parse()
        assert_matches_type(AsyncOffsetPage[SSHKey], ssh_key, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.ssh_keys.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = await response.parse()
            assert_matches_type(AsyncOffsetPage[SSHKey], ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        ssh_key = await async_client.cloud.ssh_keys.delete(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
        )
        assert ssh_key is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.ssh_keys.with_raw_response.delete(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = await response.parse()
        assert ssh_key is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.ssh_keys.with_streaming_response.delete(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = await response.parse()
            assert ssh_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ssh_key_id` but received ''"):
            await async_client.cloud.ssh_keys.with_raw_response.delete(
                ssh_key_id="",
                project_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        ssh_key = await async_client.cloud.ssh_keys.get(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
        )
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.ssh_keys.with_raw_response.get(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssh_key = await response.parse()
        assert_matches_type(SSHKey, ssh_key, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.ssh_keys.with_streaming_response.get(
            ssh_key_id="36a7a97a-0672-4911-8f2b-92cd4e5b0d91",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssh_key = await response.parse()
            assert_matches_type(SSHKey, ssh_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ssh_key_id` but received ''"):
            await async_client.cloud.ssh_keys.with_raw_response.get(
                ssh_key_id="",
                project_id=1,
            )

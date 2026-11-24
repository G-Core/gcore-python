# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import Console

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConsole:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        console = client.cloud.instances.console.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(Console, console, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Gcore) -> None:
        console = client.cloud.instances.console.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            console_type="novnc",
        )
        assert_matches_type(Console, console, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.instances.console.with_raw_response.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        console = response.parse()
        assert_matches_type(Console, console, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.instances.console.with_streaming_response.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            console = response.parse()
            assert_matches_type(Console, console, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.console.with_raw_response.get(
                instance_id="",
                project_id=1,
            )


class TestAsyncConsole:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        console = await async_client.cloud.instances.console.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(Console, console, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncGcore) -> None:
        console = await async_client.cloud.instances.console.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
            console_type="novnc",
        )
        assert_matches_type(Console, console, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.console.with_raw_response.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        console = await response.parse()
        assert_matches_type(Console, console, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.console.with_streaming_response.get(
            instance_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            console = await response.parse()
            assert_matches_type(Console, console, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.console.with_raw_response.get(
                instance_id="",
                project_id=1,
            )

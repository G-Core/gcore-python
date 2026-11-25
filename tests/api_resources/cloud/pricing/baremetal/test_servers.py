# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import ServerPrice

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        server = client.cloud.pricing.baremetal.servers.get(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(ServerPrice, server, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.pricing.baremetal.servers.with_raw_response.get(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerPrice, server, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.pricing.baremetal.servers.with_streaming_response.get(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerPrice, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.cloud.pricing.baremetal.servers.with_raw_response.get(
                server_id="",
                project_id=1,
            )

    @parametrize
    def test_method_preview(self, client: Gcore) -> None:
        server = client.cloud.pricing.baremetal.servers.preview(
            project_id=1,
            flavor_name="g2-standard-4-8",
            region_id=7,
        )
        assert_matches_type(ServerPrice, server, path=["response"])

    @parametrize
    def test_method_preview_with_all_params(self, client: Gcore) -> None:
        server = client.cloud.pricing.baremetal.servers.preview(
            project_id=1,
            flavor_name="g2-standard-4-8",
            region_id=7,
            interfaces=[
                {
                    "port_id": "port_id",
                    "floating_ip": {"floating_ip_id": "floating_ip_id"},
                }
            ],
        )
        assert_matches_type(ServerPrice, server, path=["response"])

    @parametrize
    def test_raw_response_preview(self, client: Gcore) -> None:
        response = client.cloud.pricing.baremetal.servers.with_raw_response.preview(
            project_id=1,
            flavor_name="g2-standard-4-8",
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerPrice, server, path=["response"])

    @parametrize
    def test_streaming_response_preview(self, client: Gcore) -> None:
        with client.cloud.pricing.baremetal.servers.with_streaming_response.preview(
            project_id=1,
            flavor_name="g2-standard-4-8",
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerPrice, server, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.pricing.baremetal.servers.get(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )
        assert_matches_type(ServerPrice, server, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.pricing.baremetal.servers.with_raw_response.get(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerPrice, server, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.pricing.baremetal.servers.with_streaming_response.get(
            server_id="6c6aa80f-4234-4678-9abc-def012345678",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerPrice, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.cloud.pricing.baremetal.servers.with_raw_response.get(
                server_id="",
                project_id=1,
            )

    @parametrize
    async def test_method_preview(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.pricing.baremetal.servers.preview(
            project_id=1,
            flavor_name="g2-standard-4-8",
            region_id=7,
        )
        assert_matches_type(ServerPrice, server, path=["response"])

    @parametrize
    async def test_method_preview_with_all_params(self, async_client: AsyncGcore) -> None:
        server = await async_client.cloud.pricing.baremetal.servers.preview(
            project_id=1,
            flavor_name="g2-standard-4-8",
            region_id=7,
            interfaces=[
                {
                    "port_id": "port_id",
                    "floating_ip": {"floating_ip_id": "floating_ip_id"},
                }
            ],
        )
        assert_matches_type(ServerPrice, server, path=["response"])

    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.pricing.baremetal.servers.with_raw_response.preview(
            project_id=1,
            flavor_name="g2-standard-4-8",
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerPrice, server, path=["response"])

    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.pricing.baremetal.servers.with_streaming_response.preview(
            project_id=1,
            flavor_name="g2-standard-4-8",
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerPrice, server, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import PortPrice

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPorts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_preview(self, client: Gcore) -> None:
        port = client.cloud.pricing.ports.preview(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(PortPrice, port, path=["response"])

    @parametrize
    def test_method_preview_with_all_params(self, client: Gcore) -> None:
        port = client.cloud.pricing.ports.preview(
            project_id=1,
            region_id=1,
            ip_assignments=[
                {
                    "subnet_id": "b39792c3-3160-4356-912e-ba396c95cdcf",
                    "ip_address": "192.168.123.20",
                }
            ],
            network_id="bc688791-f1b0-44eb-97d4-07697294b1e1",
        )
        assert_matches_type(PortPrice, port, path=["response"])

    @parametrize
    def test_raw_response_preview(self, client: Gcore) -> None:
        response = client.cloud.pricing.ports.with_raw_response.preview(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert_matches_type(PortPrice, port, path=["response"])

    @parametrize
    def test_streaming_response_preview(self, client: Gcore) -> None:
        with client.cloud.pricing.ports.with_streaming_response.preview(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert_matches_type(PortPrice, port, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPorts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_preview(self, async_client: AsyncGcore) -> None:
        port = await async_client.cloud.pricing.ports.preview(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(PortPrice, port, path=["response"])

    @parametrize
    async def test_method_preview_with_all_params(self, async_client: AsyncGcore) -> None:
        port = await async_client.cloud.pricing.ports.preview(
            project_id=1,
            region_id=1,
            ip_assignments=[
                {
                    "subnet_id": "b39792c3-3160-4356-912e-ba396c95cdcf",
                    "ip_address": "192.168.123.20",
                }
            ],
            network_id="bc688791-f1b0-44eb-97d4-07697294b1e1",
        )
        assert_matches_type(PortPrice, port, path=["response"])

    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.pricing.ports.with_raw_response.preview(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert_matches_type(PortPrice, port, path=["response"])

    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.pricing.ports.with_streaming_response.preview(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert_matches_type(PortPrice, port, path=["response"])

        assert cast(Any, response.is_closed) is True

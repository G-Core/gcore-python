# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud.reserved_fixed_ips.vip import (
    ConnectedPortList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectedPorts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        connected_port = client.cloud.reserved_fixed_ips.vip.connected_ports.list(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.vip.connected_ports.with_raw_response.list(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_port = response.parse()
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.vip.connected_ports.with_streaming_response.list(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_port = response.parse()
            assert_matches_type(ConnectedPortList, connected_port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.reserved_fixed_ips.vip.connected_ports.with_raw_response.list(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_add(self, client: Gcore) -> None:
        connected_port = client.cloud.reserved_fixed_ips.vip.connected_ports.add(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Gcore) -> None:
        connected_port = client.cloud.reserved_fixed_ips.vip.connected_ports.add(
            port_id="port_id",
            project_id=0,
            region_id=0,
            port_ids=["351b0dd7-ca09-431c-be53-935db3785067", "bc688791-f1b0-44eb-97d4-07697294b1e1"],
        )
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.vip.connected_ports.with_raw_response.add(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_port = response.parse()
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.vip.connected_ports.with_streaming_response.add(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_port = response.parse()
            assert_matches_type(ConnectedPortList, connected_port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.reserved_fixed_ips.vip.connected_ports.with_raw_response.add(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        connected_port = client.cloud.reserved_fixed_ips.vip.connected_ports.replace(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        connected_port = client.cloud.reserved_fixed_ips.vip.connected_ports.replace(
            port_id="port_id",
            project_id=0,
            region_id=0,
            port_ids=["351b0dd7-ca09-431c-be53-935db3785067", "bc688791-f1b0-44eb-97d4-07697294b1e1"],
        )
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.vip.connected_ports.with_raw_response.replace(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_port = response.parse()
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.vip.connected_ports.with_streaming_response.replace(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_port = response.parse()
            assert_matches_type(ConnectedPortList, connected_port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.reserved_fixed_ips.vip.connected_ports.with_raw_response.replace(
                port_id="",
                project_id=0,
                region_id=0,
            )


class TestAsyncConnectedPorts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        connected_port = await async_client.cloud.reserved_fixed_ips.vip.connected_ports.list(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.vip.connected_ports.with_raw_response.list(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_port = await response.parse()
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.vip.connected_ports.with_streaming_response.list(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_port = await response.parse()
            assert_matches_type(ConnectedPortList, connected_port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.reserved_fixed_ips.vip.connected_ports.with_raw_response.list(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_add(self, async_client: AsyncGcore) -> None:
        connected_port = await async_client.cloud.reserved_fixed_ips.vip.connected_ports.add(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncGcore) -> None:
        connected_port = await async_client.cloud.reserved_fixed_ips.vip.connected_ports.add(
            port_id="port_id",
            project_id=0,
            region_id=0,
            port_ids=["351b0dd7-ca09-431c-be53-935db3785067", "bc688791-f1b0-44eb-97d4-07697294b1e1"],
        )
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.vip.connected_ports.with_raw_response.add(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_port = await response.parse()
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.vip.connected_ports.with_streaming_response.add(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_port = await response.parse()
            assert_matches_type(ConnectedPortList, connected_port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.reserved_fixed_ips.vip.connected_ports.with_raw_response.add(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        connected_port = await async_client.cloud.reserved_fixed_ips.vip.connected_ports.replace(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        connected_port = await async_client.cloud.reserved_fixed_ips.vip.connected_ports.replace(
            port_id="port_id",
            project_id=0,
            region_id=0,
            port_ids=["351b0dd7-ca09-431c-be53-935db3785067", "bc688791-f1b0-44eb-97d4-07697294b1e1"],
        )
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.vip.connected_ports.with_raw_response.replace(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_port = await response.parse()
        assert_matches_type(ConnectedPortList, connected_port, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.vip.connected_ports.with_streaming_response.replace(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_port = await response.parse()
            assert_matches_type(ConnectedPortList, connected_port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.reserved_fixed_ips.vip.connected_ports.with_raw_response.replace(
                port_id="",
                project_id=0,
                region_id=0,
            )

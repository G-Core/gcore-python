# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import ReservedFixedIP
from gcore.types.cloud.reserved_fixed_ips import (
    CandidatePortList,
    ConnectedPortList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVip:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_candidate_ports(self, client: Gcore) -> None:
        vip = client.cloud.reserved_fixed_ips.vip.list_candidate_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(CandidatePortList, vip, path=["response"])

    @parametrize
    def test_raw_response_list_candidate_ports(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.vip.with_raw_response.list_candidate_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vip = response.parse()
        assert_matches_type(CandidatePortList, vip, path=["response"])

    @parametrize
    def test_streaming_response_list_candidate_ports(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.vip.with_streaming_response.list_candidate_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vip = response.parse()
            assert_matches_type(CandidatePortList, vip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_candidate_ports(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.reserved_fixed_ips.vip.with_raw_response.list_candidate_ports(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_list_connected_ports(self, client: Gcore) -> None:
        vip = client.cloud.reserved_fixed_ips.vip.list_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    def test_raw_response_list_connected_ports(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.vip.with_raw_response.list_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vip = response.parse()
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    def test_streaming_response_list_connected_ports(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.vip.with_streaming_response.list_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vip = response.parse()
            assert_matches_type(ConnectedPortList, vip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_connected_ports(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.reserved_fixed_ips.vip.with_raw_response.list_connected_ports(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_replace_connected_ports(self, client: Gcore) -> None:
        vip = client.cloud.reserved_fixed_ips.vip.replace_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    def test_method_replace_connected_ports_with_all_params(self, client: Gcore) -> None:
        vip = client.cloud.reserved_fixed_ips.vip.replace_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
            port_ids=["351b0dd7-ca09-431c-be53-935db3785067", "bc688791-f1b0-44eb-97d4-07697294b1e1"],
        )
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    def test_raw_response_replace_connected_ports(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.vip.with_raw_response.replace_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vip = response.parse()
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    def test_streaming_response_replace_connected_ports(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.vip.with_streaming_response.replace_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vip = response.parse()
            assert_matches_type(ConnectedPortList, vip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace_connected_ports(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.reserved_fixed_ips.vip.with_raw_response.replace_connected_ports(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_toggle(self, client: Gcore) -> None:
        vip = client.cloud.reserved_fixed_ips.vip.toggle(
            port_id="port_id",
            project_id=0,
            region_id=0,
            is_vip=True,
        )
        assert_matches_type(ReservedFixedIP, vip, path=["response"])

    @parametrize
    def test_raw_response_toggle(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.vip.with_raw_response.toggle(
            port_id="port_id",
            project_id=0,
            region_id=0,
            is_vip=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vip = response.parse()
        assert_matches_type(ReservedFixedIP, vip, path=["response"])

    @parametrize
    def test_streaming_response_toggle(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.vip.with_streaming_response.toggle(
            port_id="port_id",
            project_id=0,
            region_id=0,
            is_vip=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vip = response.parse()
            assert_matches_type(ReservedFixedIP, vip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_toggle(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.reserved_fixed_ips.vip.with_raw_response.toggle(
                port_id="",
                project_id=0,
                region_id=0,
                is_vip=True,
            )

    @parametrize
    def test_method_update_connected_ports(self, client: Gcore) -> None:
        vip = client.cloud.reserved_fixed_ips.vip.update_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    def test_method_update_connected_ports_with_all_params(self, client: Gcore) -> None:
        vip = client.cloud.reserved_fixed_ips.vip.update_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
            port_ids=["351b0dd7-ca09-431c-be53-935db3785067", "bc688791-f1b0-44eb-97d4-07697294b1e1"],
        )
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    def test_raw_response_update_connected_ports(self, client: Gcore) -> None:
        response = client.cloud.reserved_fixed_ips.vip.with_raw_response.update_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vip = response.parse()
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    def test_streaming_response_update_connected_ports(self, client: Gcore) -> None:
        with client.cloud.reserved_fixed_ips.vip.with_streaming_response.update_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vip = response.parse()
            assert_matches_type(ConnectedPortList, vip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_connected_ports(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.reserved_fixed_ips.vip.with_raw_response.update_connected_ports(
                port_id="",
                project_id=0,
                region_id=0,
            )


class TestAsyncVip:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list_candidate_ports(self, async_client: AsyncGcore) -> None:
        vip = await async_client.cloud.reserved_fixed_ips.vip.list_candidate_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(CandidatePortList, vip, path=["response"])

    @parametrize
    async def test_raw_response_list_candidate_ports(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.vip.with_raw_response.list_candidate_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vip = await response.parse()
        assert_matches_type(CandidatePortList, vip, path=["response"])

    @parametrize
    async def test_streaming_response_list_candidate_ports(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.vip.with_streaming_response.list_candidate_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vip = await response.parse()
            assert_matches_type(CandidatePortList, vip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_candidate_ports(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.reserved_fixed_ips.vip.with_raw_response.list_candidate_ports(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_list_connected_ports(self, async_client: AsyncGcore) -> None:
        vip = await async_client.cloud.reserved_fixed_ips.vip.list_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    async def test_raw_response_list_connected_ports(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.vip.with_raw_response.list_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vip = await response.parse()
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    async def test_streaming_response_list_connected_ports(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.vip.with_streaming_response.list_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vip = await response.parse()
            assert_matches_type(ConnectedPortList, vip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_connected_ports(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.reserved_fixed_ips.vip.with_raw_response.list_connected_ports(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_replace_connected_ports(self, async_client: AsyncGcore) -> None:
        vip = await async_client.cloud.reserved_fixed_ips.vip.replace_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    async def test_method_replace_connected_ports_with_all_params(self, async_client: AsyncGcore) -> None:
        vip = await async_client.cloud.reserved_fixed_ips.vip.replace_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
            port_ids=["351b0dd7-ca09-431c-be53-935db3785067", "bc688791-f1b0-44eb-97d4-07697294b1e1"],
        )
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    async def test_raw_response_replace_connected_ports(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.vip.with_raw_response.replace_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vip = await response.parse()
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    async def test_streaming_response_replace_connected_ports(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.vip.with_streaming_response.replace_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vip = await response.parse()
            assert_matches_type(ConnectedPortList, vip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace_connected_ports(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.reserved_fixed_ips.vip.with_raw_response.replace_connected_ports(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_toggle(self, async_client: AsyncGcore) -> None:
        vip = await async_client.cloud.reserved_fixed_ips.vip.toggle(
            port_id="port_id",
            project_id=0,
            region_id=0,
            is_vip=True,
        )
        assert_matches_type(ReservedFixedIP, vip, path=["response"])

    @parametrize
    async def test_raw_response_toggle(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.vip.with_raw_response.toggle(
            port_id="port_id",
            project_id=0,
            region_id=0,
            is_vip=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vip = await response.parse()
        assert_matches_type(ReservedFixedIP, vip, path=["response"])

    @parametrize
    async def test_streaming_response_toggle(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.vip.with_streaming_response.toggle(
            port_id="port_id",
            project_id=0,
            region_id=0,
            is_vip=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vip = await response.parse()
            assert_matches_type(ReservedFixedIP, vip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_toggle(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.reserved_fixed_ips.vip.with_raw_response.toggle(
                port_id="",
                project_id=0,
                region_id=0,
                is_vip=True,
            )

    @parametrize
    async def test_method_update_connected_ports(self, async_client: AsyncGcore) -> None:
        vip = await async_client.cloud.reserved_fixed_ips.vip.update_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    async def test_method_update_connected_ports_with_all_params(self, async_client: AsyncGcore) -> None:
        vip = await async_client.cloud.reserved_fixed_ips.vip.update_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
            port_ids=["351b0dd7-ca09-431c-be53-935db3785067", "bc688791-f1b0-44eb-97d4-07697294b1e1"],
        )
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    async def test_raw_response_update_connected_ports(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.reserved_fixed_ips.vip.with_raw_response.update_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vip = await response.parse()
        assert_matches_type(ConnectedPortList, vip, path=["response"])

    @parametrize
    async def test_streaming_response_update_connected_ports(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.reserved_fixed_ips.vip.with_streaming_response.update_connected_ports(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vip = await response.parse()
            assert_matches_type(ConnectedPortList, vip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_connected_ports(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.reserved_fixed_ips.vip.with_raw_response.update_connected_ports(
                port_id="",
                project_id=0,
                region_id=0,
            )

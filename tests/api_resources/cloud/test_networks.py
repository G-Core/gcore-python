# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import (
    Network,
    TaskIDList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNetworks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        network = client.cloud.networks.create(
            project_id=1,
            region_id=1,
            name="my network",
        )
        assert_matches_type(TaskIDList, network, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        network = client.cloud.networks.create(
            project_id=1,
            region_id=1,
            name="my network",
            create_router=True,
            tags={"my-tag": "my-tag-value"},
            type="vxlan",
        )
        assert_matches_type(TaskIDList, network, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.networks.with_raw_response.create(
            project_id=1,
            region_id=1,
            name="my network",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = response.parse()
        assert_matches_type(TaskIDList, network, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.networks.with_streaming_response.create(
            project_id=1,
            region_id=1,
            name="my network",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = response.parse()
            assert_matches_type(TaskIDList, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        network = client.cloud.networks.update(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Network, network, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        network = client.cloud.networks.update(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
            name="some_name",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(Network, network, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.networks.with_raw_response.update(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = response.parse()
        assert_matches_type(Network, network, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.networks.with_streaming_response.update(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = response.parse()
            assert_matches_type(Network, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network_id` but received ''"):
            client.cloud.networks.with_raw_response.update(
                network_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        network = client.cloud.networks.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(SyncOffsetPage[Network], network, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        network = client.cloud.networks.list(
            project_id=1,
            region_id=1,
            limit=1000,
            name="my-network",
            offset=0,
            order_by="created_at.desc",
            tag_key=["key1", "key2"],
            tag_key_value="tag_key_value",
        )
        assert_matches_type(SyncOffsetPage[Network], network, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.networks.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = response.parse()
        assert_matches_type(SyncOffsetPage[Network], network, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.networks.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = response.parse()
            assert_matches_type(SyncOffsetPage[Network], network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        network = client.cloud.networks.delete(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, network, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.networks.with_raw_response.delete(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = response.parse()
        assert_matches_type(TaskIDList, network, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.networks.with_streaming_response.delete(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = response.parse()
            assert_matches_type(TaskIDList, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network_id` but received ''"):
            client.cloud.networks.with_raw_response.delete(
                network_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        network = client.cloud.networks.get(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Network, network, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.networks.with_raw_response.get(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = response.parse()
        assert_matches_type(Network, network, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.networks.with_streaming_response.get(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = response.parse()
            assert_matches_type(Network, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network_id` but received ''"):
            client.cloud.networks.with_raw_response.get(
                network_id="",
                project_id=1,
                region_id=1,
            )


class TestAsyncNetworks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        network = await async_client.cloud.networks.create(
            project_id=1,
            region_id=1,
            name="my network",
        )
        assert_matches_type(TaskIDList, network, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        network = await async_client.cloud.networks.create(
            project_id=1,
            region_id=1,
            name="my network",
            create_router=True,
            tags={"my-tag": "my-tag-value"},
            type="vxlan",
        )
        assert_matches_type(TaskIDList, network, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.with_raw_response.create(
            project_id=1,
            region_id=1,
            name="my network",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = await response.parse()
        assert_matches_type(TaskIDList, network, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.with_streaming_response.create(
            project_id=1,
            region_id=1,
            name="my network",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = await response.parse()
            assert_matches_type(TaskIDList, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        network = await async_client.cloud.networks.update(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Network, network, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        network = await async_client.cloud.networks.update(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
            name="some_name",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(Network, network, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.with_raw_response.update(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = await response.parse()
        assert_matches_type(Network, network, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.with_streaming_response.update(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = await response.parse()
            assert_matches_type(Network, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network_id` but received ''"):
            await async_client.cloud.networks.with_raw_response.update(
                network_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        network = await async_client.cloud.networks.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(AsyncOffsetPage[Network], network, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        network = await async_client.cloud.networks.list(
            project_id=1,
            region_id=1,
            limit=1000,
            name="my-network",
            offset=0,
            order_by="created_at.desc",
            tag_key=["key1", "key2"],
            tag_key_value="tag_key_value",
        )
        assert_matches_type(AsyncOffsetPage[Network], network, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = await response.parse()
        assert_matches_type(AsyncOffsetPage[Network], network, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = await response.parse()
            assert_matches_type(AsyncOffsetPage[Network], network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        network = await async_client.cloud.networks.delete(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, network, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.with_raw_response.delete(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = await response.parse()
        assert_matches_type(TaskIDList, network, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.with_streaming_response.delete(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = await response.parse()
            assert_matches_type(TaskIDList, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network_id` but received ''"):
            await async_client.cloud.networks.with_raw_response.delete(
                network_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        network = await async_client.cloud.networks.get(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Network, network, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.networks.with_raw_response.get(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = await response.parse()
        assert_matches_type(Network, network, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.networks.with_streaming_response.get(
            network_id="b39792c3-3160-4356-912e-ba396c95cdcf",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = await response.parse()
            assert_matches_type(Network, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network_id` but received ''"):
            await async_client.cloud.networks.with_raw_response.get(
                network_id="",
                project_id=1,
                region_id=1,
            )

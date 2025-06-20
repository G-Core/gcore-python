# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import TaskIDList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHealthMonitors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        health_monitor = client.cloud.load_balancers.pools.health_monitors.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            delay=10,
            max_retries=2,
            api_timeout=5,
            type="HTTP",
        )
        assert_matches_type(TaskIDList, health_monitor, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        health_monitor = client.cloud.load_balancers.pools.health_monitors.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            delay=10,
            max_retries=2,
            api_timeout=5,
            type="HTTP",
            expected_codes="200,301,302",
            http_method="CONNECT",
            max_retries_down=2,
            url_path="/",
        )
        assert_matches_type(TaskIDList, health_monitor, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.pools.health_monitors.with_raw_response.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            delay=10,
            max_retries=2,
            api_timeout=5,
            type="HTTP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health_monitor = response.parse()
        assert_matches_type(TaskIDList, health_monitor, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.load_balancers.pools.health_monitors.with_streaming_response.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            delay=10,
            max_retries=2,
            api_timeout=5,
            type="HTTP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health_monitor = response.parse()
            assert_matches_type(TaskIDList, health_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.cloud.load_balancers.pools.health_monitors.with_raw_response.create(
                pool_id="",
                project_id=1,
                region_id=1,
                delay=10,
                max_retries=2,
                api_timeout=5,
                type="HTTP",
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        health_monitor = client.cloud.load_balancers.pools.health_monitors.delete(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert health_monitor is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.pools.health_monitors.with_raw_response.delete(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health_monitor = response.parse()
        assert health_monitor is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.load_balancers.pools.health_monitors.with_streaming_response.delete(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health_monitor = response.parse()
            assert health_monitor is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.cloud.load_balancers.pools.health_monitors.with_raw_response.delete(
                pool_id="",
                project_id=1,
                region_id=1,
            )


class TestAsyncHealthMonitors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        health_monitor = await async_client.cloud.load_balancers.pools.health_monitors.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            delay=10,
            max_retries=2,
            api_timeout=5,
            type="HTTP",
        )
        assert_matches_type(TaskIDList, health_monitor, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        health_monitor = await async_client.cloud.load_balancers.pools.health_monitors.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            delay=10,
            max_retries=2,
            api_timeout=5,
            type="HTTP",
            expected_codes="200,301,302",
            http_method="CONNECT",
            max_retries_down=2,
            url_path="/",
        )
        assert_matches_type(TaskIDList, health_monitor, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.pools.health_monitors.with_raw_response.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            delay=10,
            max_retries=2,
            api_timeout=5,
            type="HTTP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health_monitor = await response.parse()
        assert_matches_type(TaskIDList, health_monitor, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.pools.health_monitors.with_streaming_response.create(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
            delay=10,
            max_retries=2,
            api_timeout=5,
            type="HTTP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health_monitor = await response.parse()
            assert_matches_type(TaskIDList, health_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.cloud.load_balancers.pools.health_monitors.with_raw_response.create(
                pool_id="",
                project_id=1,
                region_id=1,
                delay=10,
                max_retries=2,
                api_timeout=5,
                type="HTTP",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        health_monitor = await async_client.cloud.load_balancers.pools.health_monitors.delete(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )
        assert health_monitor is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.pools.health_monitors.with_raw_response.delete(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health_monitor = await response.parse()
        assert health_monitor is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.pools.health_monitors.with_streaming_response.delete(
            pool_id="00000000-0000-4000-8000-000000000000",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health_monitor = await response.parse()
            assert health_monitor is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.cloud.load_balancers.pools.health_monitors.with_raw_response.delete(
                pool_id="",
                project_id=1,
                region_id=1,
            )

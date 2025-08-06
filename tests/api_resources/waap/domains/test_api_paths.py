# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.waap.domains import WaapAPIPath

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIPaths:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        api_path = client.waap.domains.api_paths.create(
            domain_id=1,
            http_scheme="HTTP",
            method="GET",
            path="/api/v1/paths/{path_id}",
        )
        assert_matches_type(WaapAPIPath, api_path, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        api_path = client.waap.domains.api_paths.create(
            domain_id=1,
            http_scheme="HTTP",
            method="GET",
            path="/api/v1/paths/{path_id}",
            api_groups=["accounts", "internal"],
            api_version="v1",
            tags=["sensitivedataurl", "highriskurl"],
        )
        assert_matches_type(WaapAPIPath, api_path, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.waap.domains.api_paths.with_raw_response.create(
            domain_id=1,
            http_scheme="HTTP",
            method="GET",
            path="/api/v1/paths/{path_id}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_path = response.parse()
        assert_matches_type(WaapAPIPath, api_path, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.waap.domains.api_paths.with_streaming_response.create(
            domain_id=1,
            http_scheme="HTTP",
            method="GET",
            path="/api/v1/paths/{path_id}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_path = response.parse()
            assert_matches_type(WaapAPIPath, api_path, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        api_path = client.waap.domains.api_paths.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        )
        assert api_path is None

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        api_path = client.waap.domains.api_paths.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
            api_groups=["accounts", "internal"],
            path="/api/v1/paths/{path_id}",
            status="CONFIRMED_API",
            tags=["sensitivedataurl", "highriskurl"],
        )
        assert api_path is None

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.waap.domains.api_paths.with_raw_response.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_path = response.parse()
        assert api_path is None

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.waap.domains.api_paths.with_streaming_response.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_path = response.parse()
            assert api_path is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.waap.domains.api_paths.with_raw_response.update(
                path_id="",
                domain_id=1,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        api_path = client.waap.domains.api_paths.list(
            domain_id=1,
        )
        assert_matches_type(SyncOffsetPage[WaapAPIPath], api_path, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        api_path = client.waap.domains.api_paths.list(
            domain_id=1,
            api_group="api_group",
            api_version="api_version",
            http_scheme="HTTP",
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            limit=0,
            method="GET",
            offset=0,
            ordering="id",
            path="path",
            source="API_DESCRIPTION_FILE",
            status=["CONFIRMED_API", "POTENTIAL_API"],
        )
        assert_matches_type(SyncOffsetPage[WaapAPIPath], api_path, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.waap.domains.api_paths.with_raw_response.list(
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_path = response.parse()
        assert_matches_type(SyncOffsetPage[WaapAPIPath], api_path, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.waap.domains.api_paths.with_streaming_response.list(
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_path = response.parse()
            assert_matches_type(SyncOffsetPage[WaapAPIPath], api_path, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        api_path = client.waap.domains.api_paths.delete(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        )
        assert api_path is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.waap.domains.api_paths.with_raw_response.delete(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_path = response.parse()
        assert api_path is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.waap.domains.api_paths.with_streaming_response.delete(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_path = response.parse()
            assert api_path is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.waap.domains.api_paths.with_raw_response.delete(
                path_id="",
                domain_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        api_path = client.waap.domains.api_paths.get(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        )
        assert_matches_type(WaapAPIPath, api_path, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.waap.domains.api_paths.with_raw_response.get(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_path = response.parse()
        assert_matches_type(WaapAPIPath, api_path, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.waap.domains.api_paths.with_streaming_response.get(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_path = response.parse()
            assert_matches_type(WaapAPIPath, api_path, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.waap.domains.api_paths.with_raw_response.get(
                path_id="",
                domain_id=1,
            )


class TestAsyncAPIPaths:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        api_path = await async_client.waap.domains.api_paths.create(
            domain_id=1,
            http_scheme="HTTP",
            method="GET",
            path="/api/v1/paths/{path_id}",
        )
        assert_matches_type(WaapAPIPath, api_path, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        api_path = await async_client.waap.domains.api_paths.create(
            domain_id=1,
            http_scheme="HTTP",
            method="GET",
            path="/api/v1/paths/{path_id}",
            api_groups=["accounts", "internal"],
            api_version="v1",
            tags=["sensitivedataurl", "highriskurl"],
        )
        assert_matches_type(WaapAPIPath, api_path, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_paths.with_raw_response.create(
            domain_id=1,
            http_scheme="HTTP",
            method="GET",
            path="/api/v1/paths/{path_id}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_path = await response.parse()
        assert_matches_type(WaapAPIPath, api_path, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_paths.with_streaming_response.create(
            domain_id=1,
            http_scheme="HTTP",
            method="GET",
            path="/api/v1/paths/{path_id}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_path = await response.parse()
            assert_matches_type(WaapAPIPath, api_path, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        api_path = await async_client.waap.domains.api_paths.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        )
        assert api_path is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        api_path = await async_client.waap.domains.api_paths.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
            api_groups=["accounts", "internal"],
            path="/api/v1/paths/{path_id}",
            status="CONFIRMED_API",
            tags=["sensitivedataurl", "highriskurl"],
        )
        assert api_path is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_paths.with_raw_response.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_path = await response.parse()
        assert api_path is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_paths.with_streaming_response.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_path = await response.parse()
            assert api_path is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.waap.domains.api_paths.with_raw_response.update(
                path_id="",
                domain_id=1,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        api_path = await async_client.waap.domains.api_paths.list(
            domain_id=1,
        )
        assert_matches_type(AsyncOffsetPage[WaapAPIPath], api_path, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        api_path = await async_client.waap.domains.api_paths.list(
            domain_id=1,
            api_group="api_group",
            api_version="api_version",
            http_scheme="HTTP",
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            limit=0,
            method="GET",
            offset=0,
            ordering="id",
            path="path",
            source="API_DESCRIPTION_FILE",
            status=["CONFIRMED_API", "POTENTIAL_API"],
        )
        assert_matches_type(AsyncOffsetPage[WaapAPIPath], api_path, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_paths.with_raw_response.list(
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_path = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapAPIPath], api_path, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_paths.with_streaming_response.list(
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_path = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapAPIPath], api_path, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        api_path = await async_client.waap.domains.api_paths.delete(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        )
        assert api_path is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_paths.with_raw_response.delete(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_path = await response.parse()
        assert api_path is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_paths.with_streaming_response.delete(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_path = await response.parse()
            assert api_path is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.waap.domains.api_paths.with_raw_response.delete(
                path_id="",
                domain_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        api_path = await async_client.waap.domains.api_paths.get(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        )
        assert_matches_type(WaapAPIPath, api_path, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.api_paths.with_raw_response.get(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_path = await response.parse()
        assert_matches_type(WaapAPIPath, api_path, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.api_paths.with_streaming_response.get(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_path = await response.parse()
            assert_matches_type(WaapAPIPath, api_path, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.waap.domains.api_paths.with_raw_response.get(
                path_id="",
                domain_id=1,
            )

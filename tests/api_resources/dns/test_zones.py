# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.types.dns import (
    ZoneGetResponse,
    ZoneListResponse,
    ZoneCreateResponse,
    ZoneExportResponse,
    ZoneImportResponse,
    ZoneGetStatisticsResponse,
    ZoneCheckDelegationStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestZones:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        zone = client.dns.zones.create(
            name="example.com",
        )
        assert_matches_type(ZoneCreateResponse, zone, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        zone = client.dns.zones.create(
            name="example.com",
            contact="contact",
            enabled=True,
            expiry=0,
            meta={"foo": {}},
            nx_ttl=0,
            primary_server="primary_server",
            refresh=0,
            retry=0,
            serial=0,
        )
        assert_matches_type(ZoneCreateResponse, zone, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.dns.zones.with_raw_response.create(
            name="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(ZoneCreateResponse, zone, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.dns.zones.with_streaming_response.create(
            name="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(ZoneCreateResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        zone = client.dns.zones.list()
        assert_matches_type(ZoneListResponse, zone, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        zone = client.dns.zones.list(
            id=[0],
            case_sensitive=True,
            client_id=[0],
            dynamic=True,
            enabled=True,
            exact_match=True,
            healthcheck=True,
            iam_reseller_id=[0],
            limit=0,
            name=["string"],
            offset=0,
            order_by="order_by",
            order_direction="asc",
            reseller_id=[0],
            status="status",
            updated_at_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ZoneListResponse, zone, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.dns.zones.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(ZoneListResponse, zone, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.dns.zones.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(ZoneListResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        zone = client.dns.zones.delete(
            "name",
        )
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.dns.zones.with_raw_response.delete(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.dns.zones.with_streaming_response.delete(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(object, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.dns.zones.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_check_delegation_status(self, client: Gcore) -> None:
        zone = client.dns.zones.check_delegation_status(
            "name",
        )
        assert_matches_type(ZoneCheckDelegationStatusResponse, zone, path=["response"])

    @parametrize
    def test_raw_response_check_delegation_status(self, client: Gcore) -> None:
        response = client.dns.zones.with_raw_response.check_delegation_status(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(ZoneCheckDelegationStatusResponse, zone, path=["response"])

    @parametrize
    def test_streaming_response_check_delegation_status(self, client: Gcore) -> None:
        with client.dns.zones.with_streaming_response.check_delegation_status(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(ZoneCheckDelegationStatusResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_check_delegation_status(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.dns.zones.with_raw_response.check_delegation_status(
                "",
            )

    @parametrize
    def test_method_disable(self, client: Gcore) -> None:
        zone = client.dns.zones.disable(
            "name",
        )
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    def test_raw_response_disable(self, client: Gcore) -> None:
        response = client.dns.zones.with_raw_response.disable(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    def test_streaming_response_disable(self, client: Gcore) -> None:
        with client.dns.zones.with_streaming_response.disable(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(object, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disable(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.dns.zones.with_raw_response.disable(
                "",
            )

    @parametrize
    def test_method_enable(self, client: Gcore) -> None:
        zone = client.dns.zones.enable(
            "name",
        )
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    def test_raw_response_enable(self, client: Gcore) -> None:
        response = client.dns.zones.with_raw_response.enable(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    def test_streaming_response_enable(self, client: Gcore) -> None:
        with client.dns.zones.with_streaming_response.enable(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(object, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_enable(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.dns.zones.with_raw_response.enable(
                "",
            )

    @parametrize
    def test_method_export(self, client: Gcore) -> None:
        zone = client.dns.zones.export(
            "zoneName",
        )
        assert_matches_type(ZoneExportResponse, zone, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Gcore) -> None:
        response = client.dns.zones.with_raw_response.export(
            "zoneName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(ZoneExportResponse, zone, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Gcore) -> None:
        with client.dns.zones.with_streaming_response.export(
            "zoneName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(ZoneExportResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_export(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            client.dns.zones.with_raw_response.export(
                "",
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        zone = client.dns.zones.get(
            "name",
        )
        assert_matches_type(ZoneGetResponse, zone, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.dns.zones.with_raw_response.get(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(ZoneGetResponse, zone, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.dns.zones.with_streaming_response.get(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(ZoneGetResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.dns.zones.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_get_statistics(self, client: Gcore) -> None:
        zone = client.dns.zones.get_statistics(
            name="name",
        )
        assert_matches_type(ZoneGetStatisticsResponse, zone, path=["response"])

    @parametrize
    def test_method_get_statistics_with_all_params(self, client: Gcore) -> None:
        zone = client.dns.zones.get_statistics(
            name="name",
            from_=0,
            granularity="granularity",
            record_type="record_type",
            to=0,
        )
        assert_matches_type(ZoneGetStatisticsResponse, zone, path=["response"])

    @parametrize
    def test_raw_response_get_statistics(self, client: Gcore) -> None:
        response = client.dns.zones.with_raw_response.get_statistics(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(ZoneGetStatisticsResponse, zone, path=["response"])

    @parametrize
    def test_streaming_response_get_statistics(self, client: Gcore) -> None:
        with client.dns.zones.with_streaming_response.get_statistics(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(ZoneGetStatisticsResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_statistics(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.dns.zones.with_raw_response.get_statistics(
                name="",
            )

    @parametrize
    def test_method_import(self, client: Gcore) -> None:
        zone = client.dns.zones.import_(
            zone_name="zoneName",
        )
        assert_matches_type(ZoneImportResponse, zone, path=["response"])

    @parametrize
    def test_method_import_with_all_params(self, client: Gcore) -> None:
        zone = client.dns.zones.import_(
            zone_name="zoneName",
            body={},
        )
        assert_matches_type(ZoneImportResponse, zone, path=["response"])

    @parametrize
    def test_raw_response_import(self, client: Gcore) -> None:
        response = client.dns.zones.with_raw_response.import_(
            zone_name="zoneName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(ZoneImportResponse, zone, path=["response"])

    @parametrize
    def test_streaming_response_import(self, client: Gcore) -> None:
        with client.dns.zones.with_streaming_response.import_(
            zone_name="zoneName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(ZoneImportResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_import(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            client.dns.zones.with_raw_response.import_(
                zone_name="",
            )

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        zone = client.dns.zones.replace(
            path_name="name",
            body_name="example.com",
        )
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        zone = client.dns.zones.replace(
            path_name="name",
            body_name="example.com",
            contact="contact",
            enabled=True,
            expiry=0,
            meta={"foo": {}},
            nx_ttl=0,
            primary_server="primary_server",
            refresh=0,
            retry=0,
            serial=0,
        )
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.dns.zones.with_raw_response.replace(
            path_name="name",
            body_name="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.dns.zones.with_streaming_response.replace(
            path_name="name",
            body_name="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(object, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            client.dns.zones.with_raw_response.replace(
                path_name="",
                body_name="example.com",
            )


class TestAsyncZones:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.create(
            name="example.com",
        )
        assert_matches_type(ZoneCreateResponse, zone, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.create(
            name="example.com",
            contact="contact",
            enabled=True,
            expiry=0,
            meta={"foo": {}},
            nx_ttl=0,
            primary_server="primary_server",
            refresh=0,
            retry=0,
            serial=0,
        )
        assert_matches_type(ZoneCreateResponse, zone, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.with_raw_response.create(
            name="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(ZoneCreateResponse, zone, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.with_streaming_response.create(
            name="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(ZoneCreateResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.list()
        assert_matches_type(ZoneListResponse, zone, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.list(
            id=[0],
            case_sensitive=True,
            client_id=[0],
            dynamic=True,
            enabled=True,
            exact_match=True,
            healthcheck=True,
            iam_reseller_id=[0],
            limit=0,
            name=["string"],
            offset=0,
            order_by="order_by",
            order_direction="asc",
            reseller_id=[0],
            status="status",
            updated_at_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ZoneListResponse, zone, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(ZoneListResponse, zone, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(ZoneListResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.delete(
            "name",
        )
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.with_raw_response.delete(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.with_streaming_response.delete(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(object, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.dns.zones.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_check_delegation_status(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.check_delegation_status(
            "name",
        )
        assert_matches_type(ZoneCheckDelegationStatusResponse, zone, path=["response"])

    @parametrize
    async def test_raw_response_check_delegation_status(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.with_raw_response.check_delegation_status(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(ZoneCheckDelegationStatusResponse, zone, path=["response"])

    @parametrize
    async def test_streaming_response_check_delegation_status(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.with_streaming_response.check_delegation_status(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(ZoneCheckDelegationStatusResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_check_delegation_status(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.dns.zones.with_raw_response.check_delegation_status(
                "",
            )

    @parametrize
    async def test_method_disable(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.disable(
            "name",
        )
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.with_raw_response.disable(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.with_streaming_response.disable(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(object, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disable(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.dns.zones.with_raw_response.disable(
                "",
            )

    @parametrize
    async def test_method_enable(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.enable(
            "name",
        )
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.with_raw_response.enable(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.with_streaming_response.enable(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(object, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_enable(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.dns.zones.with_raw_response.enable(
                "",
            )

    @parametrize
    async def test_method_export(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.export(
            "zoneName",
        )
        assert_matches_type(ZoneExportResponse, zone, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.with_raw_response.export(
            "zoneName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(ZoneExportResponse, zone, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.with_streaming_response.export(
            "zoneName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(ZoneExportResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_export(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            await async_client.dns.zones.with_raw_response.export(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.get(
            "name",
        )
        assert_matches_type(ZoneGetResponse, zone, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.with_raw_response.get(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(ZoneGetResponse, zone, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.with_streaming_response.get(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(ZoneGetResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.dns.zones.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_get_statistics(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.get_statistics(
            name="name",
        )
        assert_matches_type(ZoneGetStatisticsResponse, zone, path=["response"])

    @parametrize
    async def test_method_get_statistics_with_all_params(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.get_statistics(
            name="name",
            from_=0,
            granularity="granularity",
            record_type="record_type",
            to=0,
        )
        assert_matches_type(ZoneGetStatisticsResponse, zone, path=["response"])

    @parametrize
    async def test_raw_response_get_statistics(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.with_raw_response.get_statistics(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(ZoneGetStatisticsResponse, zone, path=["response"])

    @parametrize
    async def test_streaming_response_get_statistics(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.with_streaming_response.get_statistics(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(ZoneGetStatisticsResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_statistics(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.dns.zones.with_raw_response.get_statistics(
                name="",
            )

    @parametrize
    async def test_method_import(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.import_(
            zone_name="zoneName",
        )
        assert_matches_type(ZoneImportResponse, zone, path=["response"])

    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.import_(
            zone_name="zoneName",
            body={},
        )
        assert_matches_type(ZoneImportResponse, zone, path=["response"])

    @parametrize
    async def test_raw_response_import(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.with_raw_response.import_(
            zone_name="zoneName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(ZoneImportResponse, zone, path=["response"])

    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.with_streaming_response.import_(
            zone_name="zoneName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(ZoneImportResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_import(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            await async_client.dns.zones.with_raw_response.import_(
                zone_name="",
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.replace(
            path_name="name",
            body_name="example.com",
        )
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        zone = await async_client.dns.zones.replace(
            path_name="name",
            body_name="example.com",
            contact="contact",
            enabled=True,
            expiry=0,
            meta={"foo": {}},
            nx_ttl=0,
            primary_server="primary_server",
            refresh=0,
            retry=0,
            serial=0,
        )
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.with_raw_response.replace(
            path_name="name",
            body_name="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(object, zone, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.with_streaming_response.replace(
            path_name="name",
            body_name="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(object, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            await async_client.dns.zones.with_raw_response.replace(
                path_name="",
                body_name="example.com",
            )

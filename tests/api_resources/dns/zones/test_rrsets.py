# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.dns.zones import (
    DNSOutputRrset,
    RrsetListResponse,
    RrsetGetFailoverLogsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRrsets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        rrset = client.dns.zones.rrsets.create(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[{"content": [{}]}],
        )
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        rrset = client.dns.zones.rrsets.create(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[
                {
                    "content": [{}],
                    "enabled": True,
                    "meta": {"foo": {}},
                }
            ],
            meta={},
            pickers=[
                {
                    "type": "geodns",
                    "limit": 0,
                    "strict": True,
                }
            ],
            ttl=0,
        )
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.dns.zones.rrsets.with_raw_response.create(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[{"content": [{}]}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rrset = response.parse()
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.dns.zones.rrsets.with_streaming_response.create(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[{"content": [{}]}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rrset = response.parse()
            assert_matches_type(DNSOutputRrset, rrset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            client.dns.zones.rrsets.with_raw_response.create(
                rrset_type="rrsetType",
                zone_name="",
                rrset_name="rrsetName",
                resource_records=[{"content": [{}]}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_name` but received ''"):
            client.dns.zones.rrsets.with_raw_response.create(
                rrset_type="rrsetType",
                zone_name="zoneName",
                rrset_name="",
                resource_records=[{"content": [{}]}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_type` but received ''"):
            client.dns.zones.rrsets.with_raw_response.create(
                rrset_type="",
                zone_name="zoneName",
                rrset_name="rrsetName",
                resource_records=[{"content": [{}]}],
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        rrset = client.dns.zones.rrsets.list(
            zone_name="zoneName",
        )
        assert_matches_type(RrsetListResponse, rrset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        rrset = client.dns.zones.rrsets.list(
            zone_name="zoneName",
            limit=0,
            offset=0,
            order_by="order_by",
            order_direction="asc",
        )
        assert_matches_type(RrsetListResponse, rrset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.dns.zones.rrsets.with_raw_response.list(
            zone_name="zoneName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rrset = response.parse()
        assert_matches_type(RrsetListResponse, rrset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.dns.zones.rrsets.with_streaming_response.list(
            zone_name="zoneName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rrset = response.parse()
            assert_matches_type(RrsetListResponse, rrset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            client.dns.zones.rrsets.with_raw_response.list(
                zone_name="",
            )

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        rrset = client.dns.zones.rrsets.delete(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        )
        assert_matches_type(object, rrset, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.dns.zones.rrsets.with_raw_response.delete(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rrset = response.parse()
        assert_matches_type(object, rrset, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.dns.zones.rrsets.with_streaming_response.delete(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rrset = response.parse()
            assert_matches_type(object, rrset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            client.dns.zones.rrsets.with_raw_response.delete(
                rrset_type="rrsetType",
                zone_name="",
                rrset_name="rrsetName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_name` but received ''"):
            client.dns.zones.rrsets.with_raw_response.delete(
                rrset_type="rrsetType",
                zone_name="zoneName",
                rrset_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_type` but received ''"):
            client.dns.zones.rrsets.with_raw_response.delete(
                rrset_type="",
                zone_name="zoneName",
                rrset_name="rrsetName",
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        rrset = client.dns.zones.rrsets.get(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        )
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.dns.zones.rrsets.with_raw_response.get(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rrset = response.parse()
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.dns.zones.rrsets.with_streaming_response.get(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rrset = response.parse()
            assert_matches_type(DNSOutputRrset, rrset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            client.dns.zones.rrsets.with_raw_response.get(
                rrset_type="rrsetType",
                zone_name="",
                rrset_name="rrsetName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_name` but received ''"):
            client.dns.zones.rrsets.with_raw_response.get(
                rrset_type="rrsetType",
                zone_name="zoneName",
                rrset_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_type` but received ''"):
            client.dns.zones.rrsets.with_raw_response.get(
                rrset_type="",
                zone_name="zoneName",
                rrset_name="rrsetName",
            )

    @parametrize
    def test_method_get_failover_logs(self, client: Gcore) -> None:
        rrset = client.dns.zones.rrsets.get_failover_logs(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        )
        assert_matches_type(RrsetGetFailoverLogsResponse, rrset, path=["response"])

    @parametrize
    def test_method_get_failover_logs_with_all_params(self, client: Gcore) -> None:
        rrset = client.dns.zones.rrsets.get_failover_logs(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            limit=0,
            offset=0,
        )
        assert_matches_type(RrsetGetFailoverLogsResponse, rrset, path=["response"])

    @parametrize
    def test_raw_response_get_failover_logs(self, client: Gcore) -> None:
        response = client.dns.zones.rrsets.with_raw_response.get_failover_logs(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rrset = response.parse()
        assert_matches_type(RrsetGetFailoverLogsResponse, rrset, path=["response"])

    @parametrize
    def test_streaming_response_get_failover_logs(self, client: Gcore) -> None:
        with client.dns.zones.rrsets.with_streaming_response.get_failover_logs(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rrset = response.parse()
            assert_matches_type(RrsetGetFailoverLogsResponse, rrset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_failover_logs(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            client.dns.zones.rrsets.with_raw_response.get_failover_logs(
                rrset_type="rrsetType",
                zone_name="",
                rrset_name="rrsetName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_name` but received ''"):
            client.dns.zones.rrsets.with_raw_response.get_failover_logs(
                rrset_type="rrsetType",
                zone_name="zoneName",
                rrset_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_type` but received ''"):
            client.dns.zones.rrsets.with_raw_response.get_failover_logs(
                rrset_type="",
                zone_name="zoneName",
                rrset_name="rrsetName",
            )

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        rrset = client.dns.zones.rrsets.replace(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[{"content": [{}]}],
        )
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        rrset = client.dns.zones.rrsets.replace(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[
                {
                    "content": [{}],
                    "enabled": True,
                    "meta": {"foo": {}},
                }
            ],
            meta={},
            pickers=[
                {
                    "type": "geodns",
                    "limit": 0,
                    "strict": True,
                }
            ],
            ttl=0,
        )
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.dns.zones.rrsets.with_raw_response.replace(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[{"content": [{}]}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rrset = response.parse()
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.dns.zones.rrsets.with_streaming_response.replace(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[{"content": [{}]}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rrset = response.parse()
            assert_matches_type(DNSOutputRrset, rrset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            client.dns.zones.rrsets.with_raw_response.replace(
                rrset_type="rrsetType",
                zone_name="",
                rrset_name="rrsetName",
                resource_records=[{"content": [{}]}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_name` but received ''"):
            client.dns.zones.rrsets.with_raw_response.replace(
                rrset_type="rrsetType",
                zone_name="zoneName",
                rrset_name="",
                resource_records=[{"content": [{}]}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_type` but received ''"):
            client.dns.zones.rrsets.with_raw_response.replace(
                rrset_type="",
                zone_name="zoneName",
                rrset_name="rrsetName",
                resource_records=[{"content": [{}]}],
            )


class TestAsyncRrsets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        rrset = await async_client.dns.zones.rrsets.create(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[{"content": [{}]}],
        )
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        rrset = await async_client.dns.zones.rrsets.create(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[
                {
                    "content": [{}],
                    "enabled": True,
                    "meta": {"foo": {}},
                }
            ],
            meta={},
            pickers=[
                {
                    "type": "geodns",
                    "limit": 0,
                    "strict": True,
                }
            ],
            ttl=0,
        )
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.rrsets.with_raw_response.create(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[{"content": [{}]}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rrset = await response.parse()
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.rrsets.with_streaming_response.create(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[{"content": [{}]}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rrset = await response.parse()
            assert_matches_type(DNSOutputRrset, rrset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.create(
                rrset_type="rrsetType",
                zone_name="",
                rrset_name="rrsetName",
                resource_records=[{"content": [{}]}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_name` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.create(
                rrset_type="rrsetType",
                zone_name="zoneName",
                rrset_name="",
                resource_records=[{"content": [{}]}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_type` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.create(
                rrset_type="",
                zone_name="zoneName",
                rrset_name="rrsetName",
                resource_records=[{"content": [{}]}],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        rrset = await async_client.dns.zones.rrsets.list(
            zone_name="zoneName",
        )
        assert_matches_type(RrsetListResponse, rrset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        rrset = await async_client.dns.zones.rrsets.list(
            zone_name="zoneName",
            limit=0,
            offset=0,
            order_by="order_by",
            order_direction="asc",
        )
        assert_matches_type(RrsetListResponse, rrset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.rrsets.with_raw_response.list(
            zone_name="zoneName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rrset = await response.parse()
        assert_matches_type(RrsetListResponse, rrset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.rrsets.with_streaming_response.list(
            zone_name="zoneName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rrset = await response.parse()
            assert_matches_type(RrsetListResponse, rrset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.list(
                zone_name="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        rrset = await async_client.dns.zones.rrsets.delete(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        )
        assert_matches_type(object, rrset, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.rrsets.with_raw_response.delete(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rrset = await response.parse()
        assert_matches_type(object, rrset, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.rrsets.with_streaming_response.delete(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rrset = await response.parse()
            assert_matches_type(object, rrset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.delete(
                rrset_type="rrsetType",
                zone_name="",
                rrset_name="rrsetName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_name` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.delete(
                rrset_type="rrsetType",
                zone_name="zoneName",
                rrset_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_type` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.delete(
                rrset_type="",
                zone_name="zoneName",
                rrset_name="rrsetName",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        rrset = await async_client.dns.zones.rrsets.get(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        )
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.rrsets.with_raw_response.get(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rrset = await response.parse()
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.rrsets.with_streaming_response.get(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rrset = await response.parse()
            assert_matches_type(DNSOutputRrset, rrset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.get(
                rrset_type="rrsetType",
                zone_name="",
                rrset_name="rrsetName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_name` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.get(
                rrset_type="rrsetType",
                zone_name="zoneName",
                rrset_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_type` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.get(
                rrset_type="",
                zone_name="zoneName",
                rrset_name="rrsetName",
            )

    @parametrize
    async def test_method_get_failover_logs(self, async_client: AsyncGcore) -> None:
        rrset = await async_client.dns.zones.rrsets.get_failover_logs(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        )
        assert_matches_type(RrsetGetFailoverLogsResponse, rrset, path=["response"])

    @parametrize
    async def test_method_get_failover_logs_with_all_params(self, async_client: AsyncGcore) -> None:
        rrset = await async_client.dns.zones.rrsets.get_failover_logs(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            limit=0,
            offset=0,
        )
        assert_matches_type(RrsetGetFailoverLogsResponse, rrset, path=["response"])

    @parametrize
    async def test_raw_response_get_failover_logs(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.rrsets.with_raw_response.get_failover_logs(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rrset = await response.parse()
        assert_matches_type(RrsetGetFailoverLogsResponse, rrset, path=["response"])

    @parametrize
    async def test_streaming_response_get_failover_logs(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.rrsets.with_streaming_response.get_failover_logs(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rrset = await response.parse()
            assert_matches_type(RrsetGetFailoverLogsResponse, rrset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_failover_logs(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.get_failover_logs(
                rrset_type="rrsetType",
                zone_name="",
                rrset_name="rrsetName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_name` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.get_failover_logs(
                rrset_type="rrsetType",
                zone_name="zoneName",
                rrset_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_type` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.get_failover_logs(
                rrset_type="",
                zone_name="zoneName",
                rrset_name="rrsetName",
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        rrset = await async_client.dns.zones.rrsets.replace(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[{"content": [{}]}],
        )
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        rrset = await async_client.dns.zones.rrsets.replace(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[
                {
                    "content": [{}],
                    "enabled": True,
                    "meta": {"foo": {}},
                }
            ],
            meta={},
            pickers=[
                {
                    "type": "geodns",
                    "limit": 0,
                    "strict": True,
                }
            ],
            ttl=0,
        )
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.rrsets.with_raw_response.replace(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[{"content": [{}]}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rrset = await response.parse()
        assert_matches_type(DNSOutputRrset, rrset, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.rrsets.with_streaming_response.replace(
            rrset_type="rrsetType",
            zone_name="zoneName",
            rrset_name="rrsetName",
            resource_records=[{"content": [{}]}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rrset = await response.parse()
            assert_matches_type(DNSOutputRrset, rrset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_name` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.replace(
                rrset_type="rrsetType",
                zone_name="",
                rrset_name="rrsetName",
                resource_records=[{"content": [{}]}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_name` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.replace(
                rrset_type="rrsetType",
                zone_name="zoneName",
                rrset_name="",
                resource_records=[{"content": [{}]}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rrset_type` but received ''"):
            await async_client.dns.zones.rrsets.with_raw_response.replace(
                rrset_type="",
                zone_name="zoneName",
                rrset_name="rrsetName",
                resource_records=[{"content": [{}]}],
            )

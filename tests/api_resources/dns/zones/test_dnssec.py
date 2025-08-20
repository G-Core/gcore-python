# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.dns.zones import DnssecGetResponse, DnssecUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDnssec:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        dnssec = client.dns.zones.dnssec.update(
            name="name",
        )
        assert_matches_type(DnssecUpdateResponse, dnssec, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        dnssec = client.dns.zones.dnssec.update(
            name="name",
            enabled=True,
        )
        assert_matches_type(DnssecUpdateResponse, dnssec, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.dns.zones.dnssec.with_raw_response.update(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dnssec = response.parse()
        assert_matches_type(DnssecUpdateResponse, dnssec, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.dns.zones.dnssec.with_streaming_response.update(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dnssec = response.parse()
            assert_matches_type(DnssecUpdateResponse, dnssec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.dns.zones.dnssec.with_raw_response.update(
                name="",
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        dnssec = client.dns.zones.dnssec.get(
            "name",
        )
        assert_matches_type(DnssecGetResponse, dnssec, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.dns.zones.dnssec.with_raw_response.get(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dnssec = response.parse()
        assert_matches_type(DnssecGetResponse, dnssec, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.dns.zones.dnssec.with_streaming_response.get(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dnssec = response.parse()
            assert_matches_type(DnssecGetResponse, dnssec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.dns.zones.dnssec.with_raw_response.get(
                "",
            )


class TestAsyncDnssec:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        dnssec = await async_client.dns.zones.dnssec.update(
            name="name",
        )
        assert_matches_type(DnssecUpdateResponse, dnssec, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        dnssec = await async_client.dns.zones.dnssec.update(
            name="name",
            enabled=True,
        )
        assert_matches_type(DnssecUpdateResponse, dnssec, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.dnssec.with_raw_response.update(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dnssec = await response.parse()
        assert_matches_type(DnssecUpdateResponse, dnssec, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.dnssec.with_streaming_response.update(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dnssec = await response.parse()
            assert_matches_type(DnssecUpdateResponse, dnssec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.dns.zones.dnssec.with_raw_response.update(
                name="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        dnssec = await async_client.dns.zones.dnssec.get(
            "name",
        )
        assert_matches_type(DnssecGetResponse, dnssec, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.dns.zones.dnssec.with_raw_response.get(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dnssec = await response.parse()
        assert_matches_type(DnssecGetResponse, dnssec, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.dns.zones.dnssec.with_streaming_response.get(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dnssec = await response.parse()
            assert_matches_type(DnssecGetResponse, dnssec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.dns.zones.dnssec.with_raw_response.get(
                "",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.types.cdn import (
    CaCertificate,
)
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrustedCaCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        trusted_ca_certificate = client.cdn.trusted_ca_certificates.create(
            name="Example CA cert",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
        )
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cdn.trusted_ca_certificates.with_raw_response.create(
            name="Example CA cert",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = response.parse()
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cdn.trusted_ca_certificates.with_streaming_response.create(
            name="Example CA cert",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = response.parse()
            assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        trusted_ca_certificate = client.cdn.trusted_ca_certificates.list()
        assert_matches_type(SyncOffsetPage[CaCertificate], trusted_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        trusted_ca_certificate = client.cdn.trusted_ca_certificates.list(
            automated=True,
            limit=1,
            offset=0,
            resource_id=0,
            validity_not_after_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[CaCertificate], trusted_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.trusted_ca_certificates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = response.parse()
        assert_matches_type(SyncOffsetPage[CaCertificate], trusted_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.trusted_ca_certificates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = response.parse()
            assert_matches_type(SyncOffsetPage[CaCertificate], trusted_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        trusted_ca_certificate = client.cdn.trusted_ca_certificates.delete(
            0,
        )
        assert trusted_ca_certificate is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cdn.trusted_ca_certificates.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = response.parse()
        assert trusted_ca_certificate is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cdn.trusted_ca_certificates.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = response.parse()
            assert trusted_ca_certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        trusted_ca_certificate = client.cdn.trusted_ca_certificates.get(
            0,
        )
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cdn.trusted_ca_certificates.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = response.parse()
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cdn.trusted_ca_certificates.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = response.parse()
            assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        trusted_ca_certificate = client.cdn.trusted_ca_certificates.replace(
            id=0,
            name="Example CA cert 2",
        )
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.cdn.trusted_ca_certificates.with_raw_response.replace(
            id=0,
            name="Example CA cert 2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = response.parse()
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.cdn.trusted_ca_certificates.with_streaming_response.replace(
            id=0,
            name="Example CA cert 2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = response.parse()
            assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTrustedCaCertificates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        trusted_ca_certificate = await async_client.cdn.trusted_ca_certificates.create(
            name="Example CA cert",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
        )
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.trusted_ca_certificates.with_raw_response.create(
            name="Example CA cert",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = await response.parse()
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.trusted_ca_certificates.with_streaming_response.create(
            name="Example CA cert",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = await response.parse()
            assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        trusted_ca_certificate = await async_client.cdn.trusted_ca_certificates.list()
        assert_matches_type(AsyncOffsetPage[CaCertificate], trusted_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        trusted_ca_certificate = await async_client.cdn.trusted_ca_certificates.list(
            automated=True,
            limit=1,
            offset=0,
            resource_id=0,
            validity_not_after_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[CaCertificate], trusted_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.trusted_ca_certificates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = await response.parse()
        assert_matches_type(AsyncOffsetPage[CaCertificate], trusted_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.trusted_ca_certificates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = await response.parse()
            assert_matches_type(AsyncOffsetPage[CaCertificate], trusted_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        trusted_ca_certificate = await async_client.cdn.trusted_ca_certificates.delete(
            0,
        )
        assert trusted_ca_certificate is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.trusted_ca_certificates.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = await response.parse()
        assert trusted_ca_certificate is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.trusted_ca_certificates.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = await response.parse()
            assert trusted_ca_certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        trusted_ca_certificate = await async_client.cdn.trusted_ca_certificates.get(
            0,
        )
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.trusted_ca_certificates.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = await response.parse()
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.trusted_ca_certificates.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = await response.parse()
            assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        trusted_ca_certificate = await async_client.cdn.trusted_ca_certificates.replace(
            id=0,
            name="Example CA cert 2",
        )
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.trusted_ca_certificates.with_raw_response.replace(
            id=0,
            name="Example CA cert 2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = await response.parse()
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.trusted_ca_certificates.with_streaming_response.replace(
            id=0,
            name="Example CA cert 2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = await response.parse()
            assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

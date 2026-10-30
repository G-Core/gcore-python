# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.types.cdn import (
    SslDetail,
    SslRequestStatus,
    SslCertificateUsage,
)
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.create(
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.create(
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
            automated=False,
            validate_root_ca=True,
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.create(
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.create(
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(SslDetail, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.create(
            automated=True,
            name="Example 2",
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.create(
            automated=True,
            name="Example 2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.create(
            automated=True,
            name="Example 2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(SslDetail, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.list()
        assert_matches_type(SyncOffsetPage[SslDetail], certificate, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.list(
            automated=True,
            limit=1,
            offset=0,
            resource_id=0,
            validity_not_after_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[SslDetail], certificate, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(SyncOffsetPage[SslDetail], certificate, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(SyncOffsetPage[SslDetail], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.delete(
            0,
        )
        assert certificate is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert certificate is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_force_retry(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.force_retry(
            0,
        )
        assert certificate is None

    @parametrize
    def test_raw_response_force_retry(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.force_retry(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert certificate is None

    @parametrize
    def test_streaming_response_force_retry(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.force_retry(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.get(
            0,
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(SslDetail, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_status(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.get_status(
            cert_id=0,
        )
        assert_matches_type(SslRequestStatus, certificate, path=["response"])

    @parametrize
    def test_method_get_status_with_all_params(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.get_status(
            cert_id=0,
            exclude=["string"],
        )
        assert_matches_type(SslRequestStatus, certificate, path=["response"])

    @parametrize
    def test_raw_response_get_status(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.get_status(
            cert_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(SslRequestStatus, certificate, path=["response"])

    @parametrize
    def test_streaming_response_get_status(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.get_status(
            cert_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(SslRequestStatus, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_usage(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.get_usage(
            0,
        )
        assert_matches_type(SslCertificateUsage, certificate, path=["response"])

    @parametrize
    def test_raw_response_get_usage(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.get_usage(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(SslCertificateUsage, certificate, path=["response"])

    @parametrize
    def test_streaming_response_get_usage(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.get_usage(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(SslCertificateUsage, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_renew(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.renew(
            0,
        )
        assert certificate is None

    @parametrize
    def test_raw_response_renew(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.renew(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert certificate is None

    @parametrize
    def test_streaming_response_renew(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.renew(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.replace(
            ssl_id=0,
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.replace(
            ssl_id=0,
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
            automated=False,
            validate_root_ca=True,
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.replace(
            ssl_id=0,
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.replace(
            ssl_id=0,
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(SslDetail, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCertificates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.create(
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.create(
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
            automated=False,
            validate_root_ca=True,
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.create(
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.create(
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(SslDetail, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.create(
            automated=True,
            name="Example 2",
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.create(
            automated=True,
            name="Example 2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.create(
            automated=True,
            name="Example 2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(SslDetail, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.list()
        assert_matches_type(AsyncOffsetPage[SslDetail], certificate, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.list(
            automated=True,
            limit=1,
            offset=0,
            resource_id=0,
            validity_not_after_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[SslDetail], certificate, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(AsyncOffsetPage[SslDetail], certificate, path=["response"])

    @pytest.mark.skip(reason="GCLOUD2-27616: Prism mock serves bare-array list; SDK expects paginated OffsetPage")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(AsyncOffsetPage[SslDetail], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.delete(
            0,
        )
        assert certificate is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert certificate is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_force_retry(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.force_retry(
            0,
        )
        assert certificate is None

    @parametrize
    async def test_raw_response_force_retry(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.force_retry(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert certificate is None

    @parametrize
    async def test_streaming_response_force_retry(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.force_retry(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.get(
            0,
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(SslDetail, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_status(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.get_status(
            cert_id=0,
        )
        assert_matches_type(SslRequestStatus, certificate, path=["response"])

    @parametrize
    async def test_method_get_status_with_all_params(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.get_status(
            cert_id=0,
            exclude=["string"],
        )
        assert_matches_type(SslRequestStatus, certificate, path=["response"])

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.get_status(
            cert_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(SslRequestStatus, certificate, path=["response"])

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.get_status(
            cert_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(SslRequestStatus, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_usage(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.get_usage(
            0,
        )
        assert_matches_type(SslCertificateUsage, certificate, path=["response"])

    @parametrize
    async def test_raw_response_get_usage(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.get_usage(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(SslCertificateUsage, certificate, path=["response"])

    @parametrize
    async def test_streaming_response_get_usage(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.get_usage(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(SslCertificateUsage, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_renew(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.renew(
            0,
        )
        assert certificate is None

    @parametrize
    async def test_raw_response_renew(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.renew(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert certificate is None

    @parametrize
    async def test_streaming_response_renew(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.renew(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.replace(
            ssl_id=0,
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.replace(
            ssl_id=0,
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
            automated=False,
            validate_root_ca=True,
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.replace(
            ssl_id=0,
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.replace(
            ssl_id=0,
            name="Example 1",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIBbDCCAROgAwIBAgIUQJOOtM8WkOwi9fIMzL0RQttr/JQwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0yNzAxMDEwMDAwMDBaMBYxFDASBgNVBAMMC2V4YW1wbGUu\nY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFPjFz3rezjBUAKZXDcGcZKwl\npcCQmREWxCDWDh1D1PnWoEGmg/eaTpi0j2XsyLeLZYqwkxwcXobnic3cHo4kRKMr\nMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5jb22CD3d3dy5leGFtcGxlLmNvbTAKBggq\nhkjOPQQDAgNHADBEAiALUtTb/Vd2mJb0Ig36VkIpWej3Ufux/EBCY7BNdDNQ4gIg\nfxZsfN96JxEXETedb1Grr1f/6GYPxUnGkKB4Rjj9aTc=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIBbTCCARKgAwIBAgIULDeBmErpf2HbicPq8M/WK6fUZxEwCgYIKoZIzj0EAwIw\nKjETMBEGA1UECgwKRXhhbXBsZSBDQTETMBEGA1UEAwwKRXhhbXBsZSBDQTAeFw0y\nNjAxMDEwMDAwMDBaFw0zNjAxMDEwMDAwMDBaMCoxEzARBgNVBAoMCkV4YW1wbGUg\nQ0ExEzARBgNVBAMMCkV4YW1wbGUgQ0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\nAATdtaj2FA1AUBTNxVPfCeuuJWY6D1SQTtCNT3vbakavfJu+QISYQcc0Tbtudl5s\nv6mQPTiVlKOzi5NSWYn9F8YwoxYwFDASBgNVHRMBAf8ECDAGAQH/AgEAMAoGCCqG\nSM49BAMCA0kAMEYCIQD4GWDCyoYDx48b49W/R6ox5K2Dx37otAqQCSeB96moHAIh\nAKAUFyIRFL4HQ1Y3jEELs8TvC2554gcPQKitr0S0wM1g\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQguJC0fwVmXvhkj9fY\nCTAWhTxcAv4/tcUV+7Qhbvac5WGhRANCAAQU+MXPet7OMFQAplcNwZxkrCWlwJCZ\nERbEINYOHUPU+dagQaaD95pOmLSPZezIt4tlirCTHBxehueJzdwejiRE\n-----END PRIVATE KEY-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(SslDetail, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

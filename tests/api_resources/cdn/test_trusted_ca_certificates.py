# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn import (
    CaCertificate,
    CaCertificateList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrustedCaCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        trusted_ca_certificate = client.cdn.trusted_ca_certificates.create(
            name="Example CA cert",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIC0zCCAbugAwIBAgICA+gwDQYJKoZIhvcNAQELBQAwFjEUMBIGA1UEAwwLZXhh\nbXBsZS5jb20wHhcNMjAwNjI2MTIwMzUzWhcNMjEwNjI2MTIwMzUzWjAWMRQwEgYD\nVQQDDAtleGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\nAN4nnSfTsMEnfPgL7rkbImxZAQoND+bpPoX8q16iXZz3fFfqdRk+uEIpU3Brleeg\np0zrrT2eI3+c2h/PRod0Fam4TO6EcfwuboUFzV3j6yw6aWdfBjWZsWBR/FoqWLYq\nb3UejN7yiTYNSiIy3zVpi9pnFM8N8qT+VGBrRDGef2v9JCzhsSSU7wAYM5HKZTp+\nWHojjiyB2hOYqft7A2WlTEDmHFa5UcPHMRZKATUYI1T2TRVqLlSiE2mJ3dFRXGM2\nZAS33J0NVUjkx3w8RmJ7DNflEFJt/6IXdfaokVgfza7LFarrQFQP/YURXEeJT7jm\nDvKpZ/a8wu3ve6N4ykC+CBsCAwEAAaMrMCkwDwYDVR0TBAgwBgEB/wIBADAWBgNV\nHREEDzANggtleGFtcGxlLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEAovxY5lm89Eod\nL8CH3dZzIH7nv8MXtwgpv2vth4PDq2btLS8xrqm2SsA/cV+DsbDjh5CxQLoDX+8V\ng8NtY+ipOE0hdJAUo7UVlsxuAY4frkmLL1/RwpjZg+Z2NAxpR7xGWgoMn7CH481w\nAOBypAuCxcfcyyAOttdS+YMRJnpL6z8/C3W0LGkNOs26Qhu1/U8lfz1f9F4XummD\nu2SCmJsAd1PrL1shsyh4HtmFjuY698aTjYUDUleAnx7ytrGlZuLOIeoQi7tcsLJJ\nTPMbxTLgGN2HEkdJerFRBNViuWvqioEyYlzZ3MshOCR2wsL4wrXrCF0Y3cNOYcIh\nZ8z+wUAP2g==\n-----END CERTIFICATE-----\n",
        )
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cdn.trusted_ca_certificates.with_raw_response.create(
            name="Example CA cert",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIC0zCCAbugAwIBAgICA+gwDQYJKoZIhvcNAQELBQAwFjEUMBIGA1UEAwwLZXhh\nbXBsZS5jb20wHhcNMjAwNjI2MTIwMzUzWhcNMjEwNjI2MTIwMzUzWjAWMRQwEgYD\nVQQDDAtleGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\nAN4nnSfTsMEnfPgL7rkbImxZAQoND+bpPoX8q16iXZz3fFfqdRk+uEIpU3Brleeg\np0zrrT2eI3+c2h/PRod0Fam4TO6EcfwuboUFzV3j6yw6aWdfBjWZsWBR/FoqWLYq\nb3UejN7yiTYNSiIy3zVpi9pnFM8N8qT+VGBrRDGef2v9JCzhsSSU7wAYM5HKZTp+\nWHojjiyB2hOYqft7A2WlTEDmHFa5UcPHMRZKATUYI1T2TRVqLlSiE2mJ3dFRXGM2\nZAS33J0NVUjkx3w8RmJ7DNflEFJt/6IXdfaokVgfza7LFarrQFQP/YURXEeJT7jm\nDvKpZ/a8wu3ve6N4ykC+CBsCAwEAAaMrMCkwDwYDVR0TBAgwBgEB/wIBADAWBgNV\nHREEDzANggtleGFtcGxlLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEAovxY5lm89Eod\nL8CH3dZzIH7nv8MXtwgpv2vth4PDq2btLS8xrqm2SsA/cV+DsbDjh5CxQLoDX+8V\ng8NtY+ipOE0hdJAUo7UVlsxuAY4frkmLL1/RwpjZg+Z2NAxpR7xGWgoMn7CH481w\nAOBypAuCxcfcyyAOttdS+YMRJnpL6z8/C3W0LGkNOs26Qhu1/U8lfz1f9F4XummD\nu2SCmJsAd1PrL1shsyh4HtmFjuY698aTjYUDUleAnx7ytrGlZuLOIeoQi7tcsLJJ\nTPMbxTLgGN2HEkdJerFRBNViuWvqioEyYlzZ3MshOCR2wsL4wrXrCF0Y3cNOYcIh\nZ8z+wUAP2g==\n-----END CERTIFICATE-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = response.parse()
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cdn.trusted_ca_certificates.with_streaming_response.create(
            name="Example CA cert",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIC0zCCAbugAwIBAgICA+gwDQYJKoZIhvcNAQELBQAwFjEUMBIGA1UEAwwLZXhh\nbXBsZS5jb20wHhcNMjAwNjI2MTIwMzUzWhcNMjEwNjI2MTIwMzUzWjAWMRQwEgYD\nVQQDDAtleGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\nAN4nnSfTsMEnfPgL7rkbImxZAQoND+bpPoX8q16iXZz3fFfqdRk+uEIpU3Brleeg\np0zrrT2eI3+c2h/PRod0Fam4TO6EcfwuboUFzV3j6yw6aWdfBjWZsWBR/FoqWLYq\nb3UejN7yiTYNSiIy3zVpi9pnFM8N8qT+VGBrRDGef2v9JCzhsSSU7wAYM5HKZTp+\nWHojjiyB2hOYqft7A2WlTEDmHFa5UcPHMRZKATUYI1T2TRVqLlSiE2mJ3dFRXGM2\nZAS33J0NVUjkx3w8RmJ7DNflEFJt/6IXdfaokVgfza7LFarrQFQP/YURXEeJT7jm\nDvKpZ/a8wu3ve6N4ykC+CBsCAwEAAaMrMCkwDwYDVR0TBAgwBgEB/wIBADAWBgNV\nHREEDzANggtleGFtcGxlLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEAovxY5lm89Eod\nL8CH3dZzIH7nv8MXtwgpv2vth4PDq2btLS8xrqm2SsA/cV+DsbDjh5CxQLoDX+8V\ng8NtY+ipOE0hdJAUo7UVlsxuAY4frkmLL1/RwpjZg+Z2NAxpR7xGWgoMn7CH481w\nAOBypAuCxcfcyyAOttdS+YMRJnpL6z8/C3W0LGkNOs26Qhu1/U8lfz1f9F4XummD\nu2SCmJsAd1PrL1shsyh4HtmFjuY698aTjYUDUleAnx7ytrGlZuLOIeoQi7tcsLJJ\nTPMbxTLgGN2HEkdJerFRBNViuWvqioEyYlzZ3MshOCR2wsL4wrXrCF0Y3cNOYcIh\nZ8z+wUAP2g==\n-----END CERTIFICATE-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = response.parse()
            assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        trusted_ca_certificate = client.cdn.trusted_ca_certificates.list()
        assert_matches_type(CaCertificateList, trusted_ca_certificate, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        trusted_ca_certificate = client.cdn.trusted_ca_certificates.list(
            automated=True,
            resource_id=0,
            validity_not_after_lte="validity_not_after_lte",
        )
        assert_matches_type(CaCertificateList, trusted_ca_certificate, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.trusted_ca_certificates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = response.parse()
        assert_matches_type(CaCertificateList, trusted_ca_certificate, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.trusted_ca_certificates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = response.parse()
            assert_matches_type(CaCertificateList, trusted_ca_certificate, path=["response"])

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
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIC0zCCAbugAwIBAgICA+gwDQYJKoZIhvcNAQELBQAwFjEUMBIGA1UEAwwLZXhh\nbXBsZS5jb20wHhcNMjAwNjI2MTIwMzUzWhcNMjEwNjI2MTIwMzUzWjAWMRQwEgYD\nVQQDDAtleGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\nAN4nnSfTsMEnfPgL7rkbImxZAQoND+bpPoX8q16iXZz3fFfqdRk+uEIpU3Brleeg\np0zrrT2eI3+c2h/PRod0Fam4TO6EcfwuboUFzV3j6yw6aWdfBjWZsWBR/FoqWLYq\nb3UejN7yiTYNSiIy3zVpi9pnFM8N8qT+VGBrRDGef2v9JCzhsSSU7wAYM5HKZTp+\nWHojjiyB2hOYqft7A2WlTEDmHFa5UcPHMRZKATUYI1T2TRVqLlSiE2mJ3dFRXGM2\nZAS33J0NVUjkx3w8RmJ7DNflEFJt/6IXdfaokVgfza7LFarrQFQP/YURXEeJT7jm\nDvKpZ/a8wu3ve6N4ykC+CBsCAwEAAaMrMCkwDwYDVR0TBAgwBgEB/wIBADAWBgNV\nHREEDzANggtleGFtcGxlLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEAovxY5lm89Eod\nL8CH3dZzIH7nv8MXtwgpv2vth4PDq2btLS8xrqm2SsA/cV+DsbDjh5CxQLoDX+8V\ng8NtY+ipOE0hdJAUo7UVlsxuAY4frkmLL1/RwpjZg+Z2NAxpR7xGWgoMn7CH481w\nAOBypAuCxcfcyyAOttdS+YMRJnpL6z8/C3W0LGkNOs26Qhu1/U8lfz1f9F4XummD\nu2SCmJsAd1PrL1shsyh4HtmFjuY698aTjYUDUleAnx7ytrGlZuLOIeoQi7tcsLJJ\nTPMbxTLgGN2HEkdJerFRBNViuWvqioEyYlzZ3MshOCR2wsL4wrXrCF0Y3cNOYcIh\nZ8z+wUAP2g==\n-----END CERTIFICATE-----\n",
        )
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.trusted_ca_certificates.with_raw_response.create(
            name="Example CA cert",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIC0zCCAbugAwIBAgICA+gwDQYJKoZIhvcNAQELBQAwFjEUMBIGA1UEAwwLZXhh\nbXBsZS5jb20wHhcNMjAwNjI2MTIwMzUzWhcNMjEwNjI2MTIwMzUzWjAWMRQwEgYD\nVQQDDAtleGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\nAN4nnSfTsMEnfPgL7rkbImxZAQoND+bpPoX8q16iXZz3fFfqdRk+uEIpU3Brleeg\np0zrrT2eI3+c2h/PRod0Fam4TO6EcfwuboUFzV3j6yw6aWdfBjWZsWBR/FoqWLYq\nb3UejN7yiTYNSiIy3zVpi9pnFM8N8qT+VGBrRDGef2v9JCzhsSSU7wAYM5HKZTp+\nWHojjiyB2hOYqft7A2WlTEDmHFa5UcPHMRZKATUYI1T2TRVqLlSiE2mJ3dFRXGM2\nZAS33J0NVUjkx3w8RmJ7DNflEFJt/6IXdfaokVgfza7LFarrQFQP/YURXEeJT7jm\nDvKpZ/a8wu3ve6N4ykC+CBsCAwEAAaMrMCkwDwYDVR0TBAgwBgEB/wIBADAWBgNV\nHREEDzANggtleGFtcGxlLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEAovxY5lm89Eod\nL8CH3dZzIH7nv8MXtwgpv2vth4PDq2btLS8xrqm2SsA/cV+DsbDjh5CxQLoDX+8V\ng8NtY+ipOE0hdJAUo7UVlsxuAY4frkmLL1/RwpjZg+Z2NAxpR7xGWgoMn7CH481w\nAOBypAuCxcfcyyAOttdS+YMRJnpL6z8/C3W0LGkNOs26Qhu1/U8lfz1f9F4XummD\nu2SCmJsAd1PrL1shsyh4HtmFjuY698aTjYUDUleAnx7ytrGlZuLOIeoQi7tcsLJJ\nTPMbxTLgGN2HEkdJerFRBNViuWvqioEyYlzZ3MshOCR2wsL4wrXrCF0Y3cNOYcIh\nZ8z+wUAP2g==\n-----END CERTIFICATE-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = await response.parse()
        assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.trusted_ca_certificates.with_streaming_response.create(
            name="Example CA cert",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIC0zCCAbugAwIBAgICA+gwDQYJKoZIhvcNAQELBQAwFjEUMBIGA1UEAwwLZXhh\nbXBsZS5jb20wHhcNMjAwNjI2MTIwMzUzWhcNMjEwNjI2MTIwMzUzWjAWMRQwEgYD\nVQQDDAtleGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\nAN4nnSfTsMEnfPgL7rkbImxZAQoND+bpPoX8q16iXZz3fFfqdRk+uEIpU3Brleeg\np0zrrT2eI3+c2h/PRod0Fam4TO6EcfwuboUFzV3j6yw6aWdfBjWZsWBR/FoqWLYq\nb3UejN7yiTYNSiIy3zVpi9pnFM8N8qT+VGBrRDGef2v9JCzhsSSU7wAYM5HKZTp+\nWHojjiyB2hOYqft7A2WlTEDmHFa5UcPHMRZKATUYI1T2TRVqLlSiE2mJ3dFRXGM2\nZAS33J0NVUjkx3w8RmJ7DNflEFJt/6IXdfaokVgfza7LFarrQFQP/YURXEeJT7jm\nDvKpZ/a8wu3ve6N4ykC+CBsCAwEAAaMrMCkwDwYDVR0TBAgwBgEB/wIBADAWBgNV\nHREEDzANggtleGFtcGxlLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEAovxY5lm89Eod\nL8CH3dZzIH7nv8MXtwgpv2vth4PDq2btLS8xrqm2SsA/cV+DsbDjh5CxQLoDX+8V\ng8NtY+ipOE0hdJAUo7UVlsxuAY4frkmLL1/RwpjZg+Z2NAxpR7xGWgoMn7CH481w\nAOBypAuCxcfcyyAOttdS+YMRJnpL6z8/C3W0LGkNOs26Qhu1/U8lfz1f9F4XummD\nu2SCmJsAd1PrL1shsyh4HtmFjuY698aTjYUDUleAnx7ytrGlZuLOIeoQi7tcsLJJ\nTPMbxTLgGN2HEkdJerFRBNViuWvqioEyYlzZ3MshOCR2wsL4wrXrCF0Y3cNOYcIh\nZ8z+wUAP2g==\n-----END CERTIFICATE-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = await response.parse()
            assert_matches_type(CaCertificate, trusted_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        trusted_ca_certificate = await async_client.cdn.trusted_ca_certificates.list()
        assert_matches_type(CaCertificateList, trusted_ca_certificate, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        trusted_ca_certificate = await async_client.cdn.trusted_ca_certificates.list(
            automated=True,
            resource_id=0,
            validity_not_after_lte="validity_not_after_lte",
        )
        assert_matches_type(CaCertificateList, trusted_ca_certificate, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.trusted_ca_certificates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_ca_certificate = await response.parse()
        assert_matches_type(CaCertificateList, trusted_ca_certificate, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.trusted_ca_certificates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_ca_certificate = await response.parse()
            assert_matches_type(CaCertificateList, trusted_ca_certificate, path=["response"])

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

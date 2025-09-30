# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn import (
    SslDetail,
    SslDetailList,
    SslRequestStatus,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.create(
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
        )
        assert certificate is None

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.create(
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
            validate_root_ca=True,
        )
        assert certificate is None

    @parametrize
    def test_raw_response_create_overload_1(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.create(
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert certificate is None

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.create(
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.create(
            automated=True,
            name="New Let's Encrypt certificate",
        )
        assert certificate is None

    @parametrize
    def test_raw_response_create_overload_2(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.create(
            automated=True,
            name="New Let's Encrypt certificate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert certificate is None

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.create(
            automated=True,
            name="New Let's Encrypt certificate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.list()
        assert_matches_type(SslDetailList, certificate, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.list(
            automated=True,
            resource_id=0,
            validity_not_after_lte="validity_not_after_lte",
        )
        assert_matches_type(SslDetailList, certificate, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(SslDetailList, certificate, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(SslDetailList, certificate, path=["response"])

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
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        certificate = client.cdn.certificates.replace(
            ssl_id=0,
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
            validate_root_ca=True,
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.cdn.certificates.with_raw_response.replace(
            ssl_id=0,
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.cdn.certificates.with_streaming_response.replace(
            ssl_id=0,
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
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
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
        )
        assert certificate is None

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.create(
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
            validate_root_ca=True,
        )
        assert certificate is None

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.create(
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert certificate is None

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.create(
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.create(
            automated=True,
            name="New Let's Encrypt certificate",
        )
        assert certificate is None

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.create(
            automated=True,
            name="New Let's Encrypt certificate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert certificate is None

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.create(
            automated=True,
            name="New Let's Encrypt certificate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.list()
        assert_matches_type(SslDetailList, certificate, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.list(
            automated=True,
            resource_id=0,
            validity_not_after_lte="validity_not_after_lte",
        )
        assert_matches_type(SslDetailList, certificate, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(SslDetailList, certificate, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(SslDetailList, certificate, path=["response"])

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
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        certificate = await async_client.cdn.certificates.replace(
            ssl_id=0,
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
            validate_root_ca=True,
        )
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.certificates.with_raw_response.replace(
            ssl_id=0,
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(SslDetail, certificate, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.certificates.with_streaming_response.replace(
            ssl_id=0,
            name="New certificate",
            ssl_certificate="-----BEGIN CERTIFICATE-----\nMIIFWzCCBEOgAwIBAgISBK6qoNitg//89H/YJamujpWlMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODExMTMxMjQwMDJaFw0x\nOTAyMTExMjQwMDJaMBwxGjAYBgNVBAMTEWNkbjIudG50LWNsdWIuY29tMIIBIjAN\nBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaHExDEXNSf6ELS0WUR7qq8gs9cc\nxx99sM2zs3Jld0twPmuldkVNe5xte/Hj03r4SesfOBczR7pn+t60YujPvUQDN8lx\nWYpvRuetOneyf4gNPatwzR/W1GWGlahet1xPVYGrttqL4gCJeShIXvU4aCyzW941\nPt0wCs+bg9u+59fXFkigWrWJPkwbR7bJ14XTStYynMbYLfCg+VPeGWj3d8wOhQcf\nAD86o8TLTbVfK2BDXwS5S8Dgf5u8g+WvmVHYDIkYKCxcLj0jP61Y7uHoFbSg41oN\nA9yPOa+0cYxA7U702V2WjxbfIeATYtNLZvH17lk+DYlQl8q3MLwguqZdgwIDAQAB\niIqI2xquGONtHFDOKJvy1O2qYTVRtNRVZqhc1ol+mw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n",
            ssl_private_key="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcNCZiNNHfX2O\ndZpf12mv2rAZwqGZBAdpox0wntEPK3JciQ7ZRloLJeHuCNIJs9MidnH7Xk8zveju\nmab6HmfIzvMJAAm88OYWMFQRiYe1ggJEHMe7yYPQbtXwTqWDYdWmjPPma3Ujqqmb\nhmVX2rsYILD7cUjS+e0Ucfqx3QODQj/aujTt1rS0gFhJ0soY5m+C6VimPCx4Bjyw\n5rhtskJDRrfXxrIhVXOvSPFRyxDSfjt3win8vjhhZ3oFPWgrl9lVhn0zaB5hjDsd\n-----END PRIVATE KEY-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(SslDetail, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

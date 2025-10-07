# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cdn import (
    trusted_ca_certificate_list_params,
    trusted_ca_certificate_create_params,
    trusted_ca_certificate_replace_params,
)
from ..._base_client import make_request_options
from ...types.cdn.ca_certificate import CaCertificate
from ...types.cdn.ca_certificate_list import CaCertificateList

__all__ = ["TrustedCaCertificatesResource", "AsyncTrustedCaCertificatesResource"]


class TrustedCaCertificatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrustedCaCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return TrustedCaCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrustedCaCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return TrustedCaCertificatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        ssl_certificate: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaCertificate:
        """
        Add a trusted CA certificate to verify an origin.

        Enter all strings of the certificate in one string parameter. Each string should
        be separated by the "\n" symbol.

        Args:
          name: CA certificate name.

              It must be unique.

          ssl_certificate: Public part of the CA certificate.

              It must be in the PEM format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cdn/sslCertificates",
            body=maybe_transform(
                {
                    "name": name,
                    "ssl_certificate": ssl_certificate,
                },
                trusted_ca_certificate_create_params.TrustedCaCertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaCertificate,
        )

    def list(
        self,
        *,
        automated: bool | Omit = omit,
        resource_id: int | Omit = omit,
        validity_not_after_lte: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaCertificateList:
        """
        Get list of trusted CA certificates used to verify an origin.

        Args:
          automated: How the certificate was issued.

              Possible values:

              - **true** – Certificate was issued automatically.
              - **false** – Certificate was added by a user.

          resource_id: CDN resource ID for which the certificates are requested.

          validity_not_after_lte: Date and time when the certificate become untrusted (ISO 8601/RFC 3339 format,
              UTC.)

              Response will contain certificates valid until the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cdn/sslCertificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "automated": automated,
                        "resource_id": resource_id,
                        "validity_not_after_lte": validity_not_after_lte,
                    },
                    trusted_ca_certificate_list_params.TrustedCaCertificateListParams,
                ),
            ),
            cast_to=CaCertificateList,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete trusted CA certificate

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cdn/sslCertificates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaCertificate:
        """
        Get trusted CA certificate details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cdn/sslCertificates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaCertificate,
        )

    def replace(
        self,
        id: int,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaCertificate:
        """
        Change trusted CA certificate

        Args:
          name: CA certificate name.

              It must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/cdn/sslCertificates/{id}",
            body=maybe_transform(
                {"name": name}, trusted_ca_certificate_replace_params.TrustedCaCertificateReplaceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaCertificate,
        )


class AsyncTrustedCaCertificatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrustedCaCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrustedCaCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrustedCaCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncTrustedCaCertificatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        ssl_certificate: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaCertificate:
        """
        Add a trusted CA certificate to verify an origin.

        Enter all strings of the certificate in one string parameter. Each string should
        be separated by the "\n" symbol.

        Args:
          name: CA certificate name.

              It must be unique.

          ssl_certificate: Public part of the CA certificate.

              It must be in the PEM format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cdn/sslCertificates",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "ssl_certificate": ssl_certificate,
                },
                trusted_ca_certificate_create_params.TrustedCaCertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaCertificate,
        )

    async def list(
        self,
        *,
        automated: bool | Omit = omit,
        resource_id: int | Omit = omit,
        validity_not_after_lte: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaCertificateList:
        """
        Get list of trusted CA certificates used to verify an origin.

        Args:
          automated: How the certificate was issued.

              Possible values:

              - **true** – Certificate was issued automatically.
              - **false** – Certificate was added by a user.

          resource_id: CDN resource ID for which the certificates are requested.

          validity_not_after_lte: Date and time when the certificate become untrusted (ISO 8601/RFC 3339 format,
              UTC.)

              Response will contain certificates valid until the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cdn/sslCertificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "automated": automated,
                        "resource_id": resource_id,
                        "validity_not_after_lte": validity_not_after_lte,
                    },
                    trusted_ca_certificate_list_params.TrustedCaCertificateListParams,
                ),
            ),
            cast_to=CaCertificateList,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete trusted CA certificate

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cdn/sslCertificates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaCertificate:
        """
        Get trusted CA certificate details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cdn/sslCertificates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaCertificate,
        )

    async def replace(
        self,
        id: int,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaCertificate:
        """
        Change trusted CA certificate

        Args:
          name: CA certificate name.

              It must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/cdn/sslCertificates/{id}",
            body=await async_maybe_transform(
                {"name": name}, trusted_ca_certificate_replace_params.TrustedCaCertificateReplaceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaCertificate,
        )


class TrustedCaCertificatesResourceWithRawResponse:
    def __init__(self, trusted_ca_certificates: TrustedCaCertificatesResource) -> None:
        self._trusted_ca_certificates = trusted_ca_certificates

        self.create = to_raw_response_wrapper(
            trusted_ca_certificates.create,
        )
        self.list = to_raw_response_wrapper(
            trusted_ca_certificates.list,
        )
        self.delete = to_raw_response_wrapper(
            trusted_ca_certificates.delete,
        )
        self.get = to_raw_response_wrapper(
            trusted_ca_certificates.get,
        )
        self.replace = to_raw_response_wrapper(
            trusted_ca_certificates.replace,
        )


class AsyncTrustedCaCertificatesResourceWithRawResponse:
    def __init__(self, trusted_ca_certificates: AsyncTrustedCaCertificatesResource) -> None:
        self._trusted_ca_certificates = trusted_ca_certificates

        self.create = async_to_raw_response_wrapper(
            trusted_ca_certificates.create,
        )
        self.list = async_to_raw_response_wrapper(
            trusted_ca_certificates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            trusted_ca_certificates.delete,
        )
        self.get = async_to_raw_response_wrapper(
            trusted_ca_certificates.get,
        )
        self.replace = async_to_raw_response_wrapper(
            trusted_ca_certificates.replace,
        )


class TrustedCaCertificatesResourceWithStreamingResponse:
    def __init__(self, trusted_ca_certificates: TrustedCaCertificatesResource) -> None:
        self._trusted_ca_certificates = trusted_ca_certificates

        self.create = to_streamed_response_wrapper(
            trusted_ca_certificates.create,
        )
        self.list = to_streamed_response_wrapper(
            trusted_ca_certificates.list,
        )
        self.delete = to_streamed_response_wrapper(
            trusted_ca_certificates.delete,
        )
        self.get = to_streamed_response_wrapper(
            trusted_ca_certificates.get,
        )
        self.replace = to_streamed_response_wrapper(
            trusted_ca_certificates.replace,
        )


class AsyncTrustedCaCertificatesResourceWithStreamingResponse:
    def __init__(self, trusted_ca_certificates: AsyncTrustedCaCertificatesResource) -> None:
        self._trusted_ca_certificates = trusted_ca_certificates

        self.create = async_to_streamed_response_wrapper(
            trusted_ca_certificates.create,
        )
        self.list = async_to_streamed_response_wrapper(
            trusted_ca_certificates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            trusted_ca_certificates.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            trusted_ca_certificates.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            trusted_ca_certificates.replace,
        )

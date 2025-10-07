# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cdn import (
    certificate_list_params,
    certificate_create_params,
    certificate_replace_params,
    certificate_get_status_params,
)
from ..._base_client import make_request_options
from ...types.cdn.ssl_detail import SslDetail
from ...types.cdn.ssl_detail_list import SslDetailList
from ...types.cdn.ssl_request_status import SslRequestStatus

__all__ = ["CertificatesResource", "AsyncCertificatesResource"]


class CertificatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return CertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return CertificatesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        name: str,
        ssl_certificate: str,
        ssl_private_key: str,
        validate_root_ca: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add an SSL certificate for content delivery over HTTPS protocol.

        Enter all strings of the certificate(s) and the private key into one string
        parameter. Each certificate and the private key in chain should be separated by
        the "\n" symbol, as shown in the example.

        Additionally, you can add a Let's Encrypt certificate. In this case, certificate
        and private key will be generated automatically after attaching this certificate
        to your CDN resource.

        Args:
          name: SSL certificate name.

              It must be unique.

          ssl_certificate: Public part of the SSL certificate.

              All chain of the SSL certificate should be added.

          ssl_private_key: Private key of the SSL certificate.

          validate_root_ca: Defines whether to check the SSL certificate for a signature from a trusted
              certificate authority.

              Possible values:

              - **true** - SSL certificate must be verified to be signed by a trusted
                certificate authority.
              - **false** - SSL certificate will not be verified to be signed by a trusted
                certificate authority.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        automated: bool,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add an SSL certificate for content delivery over HTTPS protocol.

        Enter all strings of the certificate(s) and the private key into one string
        parameter. Each certificate and the private key in chain should be separated by
        the "\n" symbol, as shown in the example.

        Additionally, you can add a Let's Encrypt certificate. In this case, certificate
        and private key will be generated automatically after attaching this certificate
        to your CDN resource.

        Args:
          automated: Must be **true** to issue certificate automatically.

          name: SSL certificate name. It must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name", "ssl_certificate", "ssl_private_key"], ["automated", "name"])
    def create(
        self,
        *,
        name: str,
        ssl_certificate: str | Omit = omit,
        ssl_private_key: str | Omit = omit,
        validate_root_ca: bool | Omit = omit,
        automated: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cdn/sslData",
            body=maybe_transform(
                {
                    "name": name,
                    "ssl_certificate": ssl_certificate,
                    "ssl_private_key": ssl_private_key,
                    "validate_root_ca": validate_root_ca,
                    "automated": automated,
                },
                certificate_create_params.CertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> SslDetailList:
        """
        Get information about SSL certificates.

        Args:
          automated: How the SSL certificate was issued.

              Possible values:

              - **true** – Certificate was issued automatically.
              - **false** – Certificate was added by a user.

          resource_id: CDN resource ID for which certificates are requested.

          validity_not_after_lte: Date and time when the certificate become untrusted (ISO 8601/RFC 3339 format,
              UTC.)

              Response will contain only certificates valid until the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cdn/sslData",
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
                    certificate_list_params.CertificateListParams,
                ),
            ),
            cast_to=SslDetailList,
        )

    def delete(
        self,
        ssl_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete SSL certificate

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cdn/sslData/{ssl_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def force_retry(
        self,
        cert_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Force retry issuance of Let's Encrypt certificate if the previous attempt was
        failed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cdn/sslData/{cert_id}/force-retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        ssl_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SslDetail:
        """
        Get SSL certificate details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cdn/sslData/{ssl_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SslDetail,
        )

    def get_status(
        self,
        cert_id: int,
        *,
        exclude: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SslRequestStatus:
        """
        Get details about the latest Let's Encrypt certificate issuing attempt for the
        CDN resource. Returns attempts in all statuses.

        Args:
          exclude: Listed fields will be excluded from the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cdn/sslData/{cert_id}/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"exclude": exclude}, certificate_get_status_params.CertificateGetStatusParams),
            ),
            cast_to=SslRequestStatus,
        )

    def renew(
        self,
        cert_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Renew free Let's Encrypt certificate for the CDN resource.

        It can take up to
        fifteen minutes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cdn/sslData/{cert_id}/renew",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def replace(
        self,
        ssl_id: int,
        *,
        name: str,
        ssl_certificate: str,
        ssl_private_key: str,
        validate_root_ca: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SslDetail:
        """
        Change SSL certificate

        Args:
          name: SSL certificate name.

              It must be unique.

          ssl_certificate: Public part of the SSL certificate.

              All chain of the SSL certificate should be added.

          ssl_private_key: Private key of the SSL certificate.

          validate_root_ca: Defines whether to check the SSL certificate for a signature from a trusted
              certificate authority.

              Possible values:

              - **true** - SSL certificate must be verified to be signed by a trusted
                certificate authority.
              - **false** - SSL certificate will not be verified to be signed by a trusted
                certificate authority.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/cdn/sslData/{ssl_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "ssl_certificate": ssl_certificate,
                    "ssl_private_key": ssl_private_key,
                    "validate_root_ca": validate_root_ca,
                },
                certificate_replace_params.CertificateReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SslDetail,
        )


class AsyncCertificatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncCertificatesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        name: str,
        ssl_certificate: str,
        ssl_private_key: str,
        validate_root_ca: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add an SSL certificate for content delivery over HTTPS protocol.

        Enter all strings of the certificate(s) and the private key into one string
        parameter. Each certificate and the private key in chain should be separated by
        the "\n" symbol, as shown in the example.

        Additionally, you can add a Let's Encrypt certificate. In this case, certificate
        and private key will be generated automatically after attaching this certificate
        to your CDN resource.

        Args:
          name: SSL certificate name.

              It must be unique.

          ssl_certificate: Public part of the SSL certificate.

              All chain of the SSL certificate should be added.

          ssl_private_key: Private key of the SSL certificate.

          validate_root_ca: Defines whether to check the SSL certificate for a signature from a trusted
              certificate authority.

              Possible values:

              - **true** - SSL certificate must be verified to be signed by a trusted
                certificate authority.
              - **false** - SSL certificate will not be verified to be signed by a trusted
                certificate authority.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        automated: bool,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add an SSL certificate for content delivery over HTTPS protocol.

        Enter all strings of the certificate(s) and the private key into one string
        parameter. Each certificate and the private key in chain should be separated by
        the "\n" symbol, as shown in the example.

        Additionally, you can add a Let's Encrypt certificate. In this case, certificate
        and private key will be generated automatically after attaching this certificate
        to your CDN resource.

        Args:
          automated: Must be **true** to issue certificate automatically.

          name: SSL certificate name. It must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name", "ssl_certificate", "ssl_private_key"], ["automated", "name"])
    async def create(
        self,
        *,
        name: str,
        ssl_certificate: str | Omit = omit,
        ssl_private_key: str | Omit = omit,
        validate_root_ca: bool | Omit = omit,
        automated: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cdn/sslData",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "ssl_certificate": ssl_certificate,
                    "ssl_private_key": ssl_private_key,
                    "validate_root_ca": validate_root_ca,
                    "automated": automated,
                },
                certificate_create_params.CertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> SslDetailList:
        """
        Get information about SSL certificates.

        Args:
          automated: How the SSL certificate was issued.

              Possible values:

              - **true** – Certificate was issued automatically.
              - **false** – Certificate was added by a user.

          resource_id: CDN resource ID for which certificates are requested.

          validity_not_after_lte: Date and time when the certificate become untrusted (ISO 8601/RFC 3339 format,
              UTC.)

              Response will contain only certificates valid until the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cdn/sslData",
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
                    certificate_list_params.CertificateListParams,
                ),
            ),
            cast_to=SslDetailList,
        )

    async def delete(
        self,
        ssl_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete SSL certificate

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cdn/sslData/{ssl_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def force_retry(
        self,
        cert_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Force retry issuance of Let's Encrypt certificate if the previous attempt was
        failed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cdn/sslData/{cert_id}/force-retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        ssl_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SslDetail:
        """
        Get SSL certificate details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cdn/sslData/{ssl_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SslDetail,
        )

    async def get_status(
        self,
        cert_id: int,
        *,
        exclude: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SslRequestStatus:
        """
        Get details about the latest Let's Encrypt certificate issuing attempt for the
        CDN resource. Returns attempts in all statuses.

        Args:
          exclude: Listed fields will be excluded from the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cdn/sslData/{cert_id}/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"exclude": exclude}, certificate_get_status_params.CertificateGetStatusParams
                ),
            ),
            cast_to=SslRequestStatus,
        )

    async def renew(
        self,
        cert_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Renew free Let's Encrypt certificate for the CDN resource.

        It can take up to
        fifteen minutes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cdn/sslData/{cert_id}/renew",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def replace(
        self,
        ssl_id: int,
        *,
        name: str,
        ssl_certificate: str,
        ssl_private_key: str,
        validate_root_ca: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SslDetail:
        """
        Change SSL certificate

        Args:
          name: SSL certificate name.

              It must be unique.

          ssl_certificate: Public part of the SSL certificate.

              All chain of the SSL certificate should be added.

          ssl_private_key: Private key of the SSL certificate.

          validate_root_ca: Defines whether to check the SSL certificate for a signature from a trusted
              certificate authority.

              Possible values:

              - **true** - SSL certificate must be verified to be signed by a trusted
                certificate authority.
              - **false** - SSL certificate will not be verified to be signed by a trusted
                certificate authority.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/cdn/sslData/{ssl_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "ssl_certificate": ssl_certificate,
                    "ssl_private_key": ssl_private_key,
                    "validate_root_ca": validate_root_ca,
                },
                certificate_replace_params.CertificateReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SslDetail,
        )


class CertificatesResourceWithRawResponse:
    def __init__(self, certificates: CertificatesResource) -> None:
        self._certificates = certificates

        self.create = to_raw_response_wrapper(
            certificates.create,
        )
        self.list = to_raw_response_wrapper(
            certificates.list,
        )
        self.delete = to_raw_response_wrapper(
            certificates.delete,
        )
        self.force_retry = to_raw_response_wrapper(
            certificates.force_retry,
        )
        self.get = to_raw_response_wrapper(
            certificates.get,
        )
        self.get_status = to_raw_response_wrapper(
            certificates.get_status,
        )
        self.renew = to_raw_response_wrapper(
            certificates.renew,
        )
        self.replace = to_raw_response_wrapper(
            certificates.replace,
        )


class AsyncCertificatesResourceWithRawResponse:
    def __init__(self, certificates: AsyncCertificatesResource) -> None:
        self._certificates = certificates

        self.create = async_to_raw_response_wrapper(
            certificates.create,
        )
        self.list = async_to_raw_response_wrapper(
            certificates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            certificates.delete,
        )
        self.force_retry = async_to_raw_response_wrapper(
            certificates.force_retry,
        )
        self.get = async_to_raw_response_wrapper(
            certificates.get,
        )
        self.get_status = async_to_raw_response_wrapper(
            certificates.get_status,
        )
        self.renew = async_to_raw_response_wrapper(
            certificates.renew,
        )
        self.replace = async_to_raw_response_wrapper(
            certificates.replace,
        )


class CertificatesResourceWithStreamingResponse:
    def __init__(self, certificates: CertificatesResource) -> None:
        self._certificates = certificates

        self.create = to_streamed_response_wrapper(
            certificates.create,
        )
        self.list = to_streamed_response_wrapper(
            certificates.list,
        )
        self.delete = to_streamed_response_wrapper(
            certificates.delete,
        )
        self.force_retry = to_streamed_response_wrapper(
            certificates.force_retry,
        )
        self.get = to_streamed_response_wrapper(
            certificates.get,
        )
        self.get_status = to_streamed_response_wrapper(
            certificates.get_status,
        )
        self.renew = to_streamed_response_wrapper(
            certificates.renew,
        )
        self.replace = to_streamed_response_wrapper(
            certificates.replace,
        )


class AsyncCertificatesResourceWithStreamingResponse:
    def __init__(self, certificates: AsyncCertificatesResource) -> None:
        self._certificates = certificates

        self.create = async_to_streamed_response_wrapper(
            certificates.create,
        )
        self.list = async_to_streamed_response_wrapper(
            certificates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            certificates.delete,
        )
        self.force_retry = async_to_streamed_response_wrapper(
            certificates.force_retry,
        )
        self.get = async_to_streamed_response_wrapper(
            certificates.get,
        )
        self.get_status = async_to_streamed_response_wrapper(
            certificates.get_status,
        )
        self.renew = async_to_streamed_response_wrapper(
            certificates.renew,
        )
        self.replace = async_to_streamed_response_wrapper(
            certificates.replace,
        )

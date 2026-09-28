# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cdn import (
    alias_list_params,
    alias_create_params,
    alias_update_params,
    alias_create_multiple_params,
    alias_delete_multiple_params,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cdn.alias import Alias
from ...types.cdn.alias_detail import AliasDetail
from ...types.cdn.alias_certificate_status import AliasCertificateStatus
from ...types.cdn.alias_create_multiple_response import AliasCreateMultipleResponse
from ...types.cdn.alias_delete_multiple_response import AliasDeleteMultipleResponse

__all__ = ["AliasesResource", "AsyncAliasesResource"]


class AliasesResource(SyncAPIResource):
    """
    CDN aliases are hostnames you own that are served with the settings of one of your CDN resources, each with its own SSL certificate.
    """

    @cached_property
    def with_raw_response(self) -> AliasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AliasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AliasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AliasesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        cname: str,
        resource_id: int,
        active: bool | Omit = omit,
        automated: bool | Omit = omit,
        ssl_id: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Alias:
        """
        Create an alias: a hostname you own that is served with the settings of one of
        your CDN resources and with its own SSL certificate.

        By default, a Let's Encrypt certificate is issued for the alias automatically.
        Until the certificate is issued the alias stays in the `pending` status.

        To use your own certificate instead, pass its ID in `ssl_id`. The certificate
        must cover the alias hostname; a Let's Encrypt certificate issued for one of
        your CDN resources cannot be used. Such an alias becomes `active` immediately.

        The hostname must be unique across all CDN resources, additional CNAMEs and
        aliases.

        If Let's Encrypt validation for the hostname requires a delegation record, it is
        reported as `ssl_provisioning` when you get the alias.

        Args:
          cname: Alias hostname. Wildcard hostnames are not supported.

          resource_id: ID of the CDN resource whose settings the alias is served with.

          active: Whether the alias is enabled. Defaults to **true**. The alias is served once its
              certificate is ready.

          automated: How the alias certificate is managed. Defaults to **true** when `ssl_id` is
              omitted and to **false** when `ssl_id` is passed.

              Possible values:

              - **true** – A Let's Encrypt certificate is issued and renewed automatically.
                `ssl_id` must be omitted.
              - **false** – Your own certificate is served. `ssl_id` is required.

          ssl_id: ID of your own SSL certificate to serve for the alias. The certificate must
              cover the alias hostname. A Let's Encrypt certificate issued for one of your CDN
              resources cannot be used.

              Omit it to have a Let's Encrypt certificate issued automatically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cdn/aliases",
            body=maybe_transform(
                {
                    "cname": cname,
                    "resource_id": resource_id,
                    "active": active,
                    "automated": automated,
                    "ssl_id": ssl_id,
                },
                alias_create_params.AliasCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Alias,
        )

    def update(
        self,
        alias_id: int,
        *,
        active: bool | Omit = omit,
        automated: bool | Omit = omit,
        ssl_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AliasDetail:
        """Change an alias.

        The hostname and the CDN resource of an alias cannot be
        changed; delete the alias and create a new one instead.

        Set `active` to **false** to stop serving the alias; set it back to **true** to
        resume. Resuming an alias that has no valid certificate starts a new issuance
        attempt, which is rate-limited, so it cannot be combined with `automated` in one
        request.

        For an alias with your own certificate, pass a new certificate ID in `ssl_id` to
        replace it. The new certificate must cover the alias hostname.

        Pass `automated` to switch how the certificate is managed. Switching to your own
        certificate takes effect at once and the Let's Encrypt certificate issued for
        the alias is removed. Switching to a Let's Encrypt certificate starts an
        issuance attempt while your certificate keeps being served, and the alias starts
        serving the new certificate once it is issued; if the attempt fails, `status`
        becomes **`ssl_error`** and your certificate keeps being served. The certificate
        mode cannot be changed while the alias is paused — resume it first.

        Args:
          active: Whether the alias is enabled.

              Possible values:

              - **true** – The alias is enabled and is served once its certificate is ready.
              - **false** – The alias is paused and is not served.

          automated: How the alias certificate is managed. Change it to switch the alias between a
              Let's Encrypt certificate and your own. Cannot be changed while the alias is
              paused.

              Possible values:

              - **true** – Switch to a Let's Encrypt certificate. `ssl_id` must be omitted.
                The current certificate keeps being served until the new one is issued.
              - **false** – Switch to your own certificate. `ssl_id` is required and is served
                immediately.

          ssl_id: ID of your own SSL certificate to serve for the alias instead of the current
              one. The certificate must cover the alias hostname; a Let's Encrypt certificate
              issued for one of your CDN resources cannot be used. Available for an alias with
              `automated` set to **false**, and together with `automated` set to **false** to
              switch to your own certificate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/cdn/aliases/{alias_id}", alias_id=alias_id),
            body=maybe_transform(
                {
                    "active": active,
                    "automated": automated,
                    "ssl_id": ssl_id,
                },
                alias_update_params.AliasUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AliasDetail,
        )

    def list(
        self,
        *,
        automated: bool | Omit = omit,
        cname: str | Omit = omit,
        cname_endswith: str | Omit = omit,
        cname_startswith: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: str | Omit = omit,
        resource_id: int | Omit = omit,
        resource_id_in: str | Omit = omit,
        search: str | Omit = omit,
        ssl_id: int | Omit = omit,
        ssl_status: Optional[Literal["pending", "issued", "failed"]] | Omit = omit,
        ssl_status_in: str | Omit = omit,
        ssl_validity_not_after_gte: str | Omit = omit,
        ssl_validity_not_after_lte: str | Omit = omit,
        status: Literal["pending", "active", "ssl_issuing", "ssl_error", "inactive"] | Omit = omit,
        status_in: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[Alias]:
        """
        Get information about aliases.

        The response is always paginated.

        Args:
          automated: How the alias certificate is managed.

              Possible values:

              - **true** – Certificate is issued and renewed automatically.
              - **false** – Certificate was added by a user.

          cname: Hostname substring, case-insensitive.

          cname_endswith: Hostname suffix, case-insensitive.

          cname_startswith: Hostname prefix, case-insensitive.

          limit: Maximum number of items to return in the response. Cannot exceed 1000.

          offset: Number of items to skip from the beginning of the list.

          ordering: Field to sort by. Prefix with `-` for descending order.

              Possible values: `id`, `cname`, `status`, `created`, `updated`, `resource_id`.

          resource_id: CDN resource ID. Only aliases of this CDN resource are returned.

          resource_id_in: Comma-separated list of CDN resource IDs.

          search: Search by alias ID or hostname.

          ssl_id: SSL certificate ID. Only aliases linked to this certificate are returned.

          ssl_status: Certificate outcome.

          ssl_status_in: Comma-separated list of certificate outcomes.

          ssl_validity_not_after_gte: Only aliases whose served certificate expires at or after this date and time
              (ISO 8601/RFC 3339 format, UTC).

          ssl_validity_not_after_lte: Only aliases whose served certificate expires at or before this date and time
              (ISO 8601/RFC 3339 format, UTC).

          status: Alias status.

          status_in: Comma-separated list of alias statuses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cdn/aliases",
            page=SyncOffsetPage[Alias],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "automated": automated,
                        "cname": cname,
                        "cname_endswith": cname_endswith,
                        "cname_startswith": cname_startswith,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "resource_id": resource_id,
                        "resource_id_in": resource_id_in,
                        "search": search,
                        "ssl_id": ssl_id,
                        "ssl_status": ssl_status,
                        "ssl_status_in": ssl_status_in,
                        "ssl_validity_not_after_gte": ssl_validity_not_after_gte,
                        "ssl_validity_not_after_lte": ssl_validity_not_after_lte,
                        "status": status,
                        "status_in": status_in,
                    },
                    alias_list_params.AliasListParams,
                ),
            ),
            model=Alias,
        )

    def delete(
        self,
        alias_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an alias.

        The hostname stops being served and can be used again. A
        certificate you added yourself is not affected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/cdn/aliases/{alias_id}", alias_id=alias_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_multiple(
        self,
        *,
        items: Iterable[alias_create_multiple_params.Item],
        resource_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AliasCreateMultipleResponse:
        """
        Create up to 1000 aliases for one CDN resource in a single request.

        The request is atomic: if any item is invalid, nothing is created and the errors
        are returned per item, in the same order as the request items. An item whose
        hostname is already an alias of the same CDN resource is reported in `exists`
        and left unchanged.

        The aliases limit of your account is checked against the items that would be
        created.

        Args:
          items: Aliases to create.

          resource_id: ID of the CDN resource whose settings the aliases are served with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cdn/aliases/add",
            body=maybe_transform(
                {
                    "items": items,
                    "resource_id": resource_id,
                },
                alias_create_multiple_params.AliasCreateMultipleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AliasCreateMultipleResponse,
        )

    def delete_multiple(
        self,
        *,
        cnames: SequenceNotStr[str] | Omit = omit,
        ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AliasDeleteMultipleResponse:
        """
        Delete up to 1000 aliases in a single request, selected either by ID or by
        hostname.

        Aliases that are not found are reported in `not_found` and do not fail the
        request.

        Args:
          cnames: Hostnames of the aliases to delete.

          ids: IDs of the aliases to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cdn/aliases/remove",
            body=maybe_transform(
                {
                    "cnames": cnames,
                    "ids": ids,
                },
                alias_delete_multiple_params.AliasDeleteMultipleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AliasDeleteMultipleResponse,
        )

    def get(
        self,
        alias_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AliasDetail:
        """
        Get alias details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/cdn/aliases/{alias_id}", alias_id=alias_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AliasDetail,
        )

    def get_certificate_status(
        self,
        alias_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AliasCertificateStatus:
        """
        Get details about the latest Let's Encrypt certificate issuing attempt for an
        alias, including the CNAME records to create for domain validation. Returns
        attempts in all statuses.

        While the alias is switching to a Let's Encrypt certificate, the attempt for the
        new certificate is returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/cdn/aliases/{alias_id}/status", alias_id=alias_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AliasCertificateStatus,
        )

    def retry_certificate(
        self,
        alias_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AliasDetail:
        """
        Start a new Let's Encrypt certificate issuance attempt for an alias that has
        none running. Use it after an attempt has failed and `status` is
        **`ssl_error`**.

        The number of attempts you can start per hour is limited.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/cdn/aliases/{alias_id}/retry", alias_id=alias_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AliasDetail,
        )


class AsyncAliasesResource(AsyncAPIResource):
    """
    CDN aliases are hostnames you own that are served with the settings of one of your CDN resources, each with its own SSL certificate.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAliasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAliasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAliasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAliasesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        cname: str,
        resource_id: int,
        active: bool | Omit = omit,
        automated: bool | Omit = omit,
        ssl_id: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Alias:
        """
        Create an alias: a hostname you own that is served with the settings of one of
        your CDN resources and with its own SSL certificate.

        By default, a Let's Encrypt certificate is issued for the alias automatically.
        Until the certificate is issued the alias stays in the `pending` status.

        To use your own certificate instead, pass its ID in `ssl_id`. The certificate
        must cover the alias hostname; a Let's Encrypt certificate issued for one of
        your CDN resources cannot be used. Such an alias becomes `active` immediately.

        The hostname must be unique across all CDN resources, additional CNAMEs and
        aliases.

        If Let's Encrypt validation for the hostname requires a delegation record, it is
        reported as `ssl_provisioning` when you get the alias.

        Args:
          cname: Alias hostname. Wildcard hostnames are not supported.

          resource_id: ID of the CDN resource whose settings the alias is served with.

          active: Whether the alias is enabled. Defaults to **true**. The alias is served once its
              certificate is ready.

          automated: How the alias certificate is managed. Defaults to **true** when `ssl_id` is
              omitted and to **false** when `ssl_id` is passed.

              Possible values:

              - **true** – A Let's Encrypt certificate is issued and renewed automatically.
                `ssl_id` must be omitted.
              - **false** – Your own certificate is served. `ssl_id` is required.

          ssl_id: ID of your own SSL certificate to serve for the alias. The certificate must
              cover the alias hostname. A Let's Encrypt certificate issued for one of your CDN
              resources cannot be used.

              Omit it to have a Let's Encrypt certificate issued automatically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cdn/aliases",
            body=await async_maybe_transform(
                {
                    "cname": cname,
                    "resource_id": resource_id,
                    "active": active,
                    "automated": automated,
                    "ssl_id": ssl_id,
                },
                alias_create_params.AliasCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Alias,
        )

    async def update(
        self,
        alias_id: int,
        *,
        active: bool | Omit = omit,
        automated: bool | Omit = omit,
        ssl_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AliasDetail:
        """Change an alias.

        The hostname and the CDN resource of an alias cannot be
        changed; delete the alias and create a new one instead.

        Set `active` to **false** to stop serving the alias; set it back to **true** to
        resume. Resuming an alias that has no valid certificate starts a new issuance
        attempt, which is rate-limited, so it cannot be combined with `automated` in one
        request.

        For an alias with your own certificate, pass a new certificate ID in `ssl_id` to
        replace it. The new certificate must cover the alias hostname.

        Pass `automated` to switch how the certificate is managed. Switching to your own
        certificate takes effect at once and the Let's Encrypt certificate issued for
        the alias is removed. Switching to a Let's Encrypt certificate starts an
        issuance attempt while your certificate keeps being served, and the alias starts
        serving the new certificate once it is issued; if the attempt fails, `status`
        becomes **`ssl_error`** and your certificate keeps being served. The certificate
        mode cannot be changed while the alias is paused — resume it first.

        Args:
          active: Whether the alias is enabled.

              Possible values:

              - **true** – The alias is enabled and is served once its certificate is ready.
              - **false** – The alias is paused and is not served.

          automated: How the alias certificate is managed. Change it to switch the alias between a
              Let's Encrypt certificate and your own. Cannot be changed while the alias is
              paused.

              Possible values:

              - **true** – Switch to a Let's Encrypt certificate. `ssl_id` must be omitted.
                The current certificate keeps being served until the new one is issued.
              - **false** – Switch to your own certificate. `ssl_id` is required and is served
                immediately.

          ssl_id: ID of your own SSL certificate to serve for the alias instead of the current
              one. The certificate must cover the alias hostname; a Let's Encrypt certificate
              issued for one of your CDN resources cannot be used. Available for an alias with
              `automated` set to **false**, and together with `automated` set to **false** to
              switch to your own certificate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/cdn/aliases/{alias_id}", alias_id=alias_id),
            body=await async_maybe_transform(
                {
                    "active": active,
                    "automated": automated,
                    "ssl_id": ssl_id,
                },
                alias_update_params.AliasUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AliasDetail,
        )

    def list(
        self,
        *,
        automated: bool | Omit = omit,
        cname: str | Omit = omit,
        cname_endswith: str | Omit = omit,
        cname_startswith: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: str | Omit = omit,
        resource_id: int | Omit = omit,
        resource_id_in: str | Omit = omit,
        search: str | Omit = omit,
        ssl_id: int | Omit = omit,
        ssl_status: Optional[Literal["pending", "issued", "failed"]] | Omit = omit,
        ssl_status_in: str | Omit = omit,
        ssl_validity_not_after_gte: str | Omit = omit,
        ssl_validity_not_after_lte: str | Omit = omit,
        status: Literal["pending", "active", "ssl_issuing", "ssl_error", "inactive"] | Omit = omit,
        status_in: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Alias, AsyncOffsetPage[Alias]]:
        """
        Get information about aliases.

        The response is always paginated.

        Args:
          automated: How the alias certificate is managed.

              Possible values:

              - **true** – Certificate is issued and renewed automatically.
              - **false** – Certificate was added by a user.

          cname: Hostname substring, case-insensitive.

          cname_endswith: Hostname suffix, case-insensitive.

          cname_startswith: Hostname prefix, case-insensitive.

          limit: Maximum number of items to return in the response. Cannot exceed 1000.

          offset: Number of items to skip from the beginning of the list.

          ordering: Field to sort by. Prefix with `-` for descending order.

              Possible values: `id`, `cname`, `status`, `created`, `updated`, `resource_id`.

          resource_id: CDN resource ID. Only aliases of this CDN resource are returned.

          resource_id_in: Comma-separated list of CDN resource IDs.

          search: Search by alias ID or hostname.

          ssl_id: SSL certificate ID. Only aliases linked to this certificate are returned.

          ssl_status: Certificate outcome.

          ssl_status_in: Comma-separated list of certificate outcomes.

          ssl_validity_not_after_gte: Only aliases whose served certificate expires at or after this date and time
              (ISO 8601/RFC 3339 format, UTC).

          ssl_validity_not_after_lte: Only aliases whose served certificate expires at or before this date and time
              (ISO 8601/RFC 3339 format, UTC).

          status: Alias status.

          status_in: Comma-separated list of alias statuses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cdn/aliases",
            page=AsyncOffsetPage[Alias],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "automated": automated,
                        "cname": cname,
                        "cname_endswith": cname_endswith,
                        "cname_startswith": cname_startswith,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "resource_id": resource_id,
                        "resource_id_in": resource_id_in,
                        "search": search,
                        "ssl_id": ssl_id,
                        "ssl_status": ssl_status,
                        "ssl_status_in": ssl_status_in,
                        "ssl_validity_not_after_gte": ssl_validity_not_after_gte,
                        "ssl_validity_not_after_lte": ssl_validity_not_after_lte,
                        "status": status,
                        "status_in": status_in,
                    },
                    alias_list_params.AliasListParams,
                ),
            ),
            model=Alias,
        )

    async def delete(
        self,
        alias_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an alias.

        The hostname stops being served and can be used again. A
        certificate you added yourself is not affected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/cdn/aliases/{alias_id}", alias_id=alias_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_multiple(
        self,
        *,
        items: Iterable[alias_create_multiple_params.Item],
        resource_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AliasCreateMultipleResponse:
        """
        Create up to 1000 aliases for one CDN resource in a single request.

        The request is atomic: if any item is invalid, nothing is created and the errors
        are returned per item, in the same order as the request items. An item whose
        hostname is already an alias of the same CDN resource is reported in `exists`
        and left unchanged.

        The aliases limit of your account is checked against the items that would be
        created.

        Args:
          items: Aliases to create.

          resource_id: ID of the CDN resource whose settings the aliases are served with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cdn/aliases/add",
            body=await async_maybe_transform(
                {
                    "items": items,
                    "resource_id": resource_id,
                },
                alias_create_multiple_params.AliasCreateMultipleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AliasCreateMultipleResponse,
        )

    async def delete_multiple(
        self,
        *,
        cnames: SequenceNotStr[str] | Omit = omit,
        ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AliasDeleteMultipleResponse:
        """
        Delete up to 1000 aliases in a single request, selected either by ID or by
        hostname.

        Aliases that are not found are reported in `not_found` and do not fail the
        request.

        Args:
          cnames: Hostnames of the aliases to delete.

          ids: IDs of the aliases to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cdn/aliases/remove",
            body=await async_maybe_transform(
                {
                    "cnames": cnames,
                    "ids": ids,
                },
                alias_delete_multiple_params.AliasDeleteMultipleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AliasDeleteMultipleResponse,
        )

    async def get(
        self,
        alias_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AliasDetail:
        """
        Get alias details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/cdn/aliases/{alias_id}", alias_id=alias_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AliasDetail,
        )

    async def get_certificate_status(
        self,
        alias_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AliasCertificateStatus:
        """
        Get details about the latest Let's Encrypt certificate issuing attempt for an
        alias, including the CNAME records to create for domain validation. Returns
        attempts in all statuses.

        While the alias is switching to a Let's Encrypt certificate, the attempt for the
        new certificate is returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/cdn/aliases/{alias_id}/status", alias_id=alias_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AliasCertificateStatus,
        )

    async def retry_certificate(
        self,
        alias_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AliasDetail:
        """
        Start a new Let's Encrypt certificate issuance attempt for an alias that has
        none running. Use it after an attempt has failed and `status` is
        **`ssl_error`**.

        The number of attempts you can start per hour is limited.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/cdn/aliases/{alias_id}/retry", alias_id=alias_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AliasDetail,
        )


class AliasesResourceWithRawResponse:
    def __init__(self, aliases: AliasesResource) -> None:
        self._aliases = aliases

        self.create = to_raw_response_wrapper(
            aliases.create,
        )
        self.update = to_raw_response_wrapper(
            aliases.update,
        )
        self.list = to_raw_response_wrapper(
            aliases.list,
        )
        self.delete = to_raw_response_wrapper(
            aliases.delete,
        )
        self.create_multiple = to_raw_response_wrapper(
            aliases.create_multiple,
        )
        self.delete_multiple = to_raw_response_wrapper(
            aliases.delete_multiple,
        )
        self.get = to_raw_response_wrapper(
            aliases.get,
        )
        self.get_certificate_status = to_raw_response_wrapper(
            aliases.get_certificate_status,
        )
        self.retry_certificate = to_raw_response_wrapper(
            aliases.retry_certificate,
        )


class AsyncAliasesResourceWithRawResponse:
    def __init__(self, aliases: AsyncAliasesResource) -> None:
        self._aliases = aliases

        self.create = async_to_raw_response_wrapper(
            aliases.create,
        )
        self.update = async_to_raw_response_wrapper(
            aliases.update,
        )
        self.list = async_to_raw_response_wrapper(
            aliases.list,
        )
        self.delete = async_to_raw_response_wrapper(
            aliases.delete,
        )
        self.create_multiple = async_to_raw_response_wrapper(
            aliases.create_multiple,
        )
        self.delete_multiple = async_to_raw_response_wrapper(
            aliases.delete_multiple,
        )
        self.get = async_to_raw_response_wrapper(
            aliases.get,
        )
        self.get_certificate_status = async_to_raw_response_wrapper(
            aliases.get_certificate_status,
        )
        self.retry_certificate = async_to_raw_response_wrapper(
            aliases.retry_certificate,
        )


class AliasesResourceWithStreamingResponse:
    def __init__(self, aliases: AliasesResource) -> None:
        self._aliases = aliases

        self.create = to_streamed_response_wrapper(
            aliases.create,
        )
        self.update = to_streamed_response_wrapper(
            aliases.update,
        )
        self.list = to_streamed_response_wrapper(
            aliases.list,
        )
        self.delete = to_streamed_response_wrapper(
            aliases.delete,
        )
        self.create_multiple = to_streamed_response_wrapper(
            aliases.create_multiple,
        )
        self.delete_multiple = to_streamed_response_wrapper(
            aliases.delete_multiple,
        )
        self.get = to_streamed_response_wrapper(
            aliases.get,
        )
        self.get_certificate_status = to_streamed_response_wrapper(
            aliases.get_certificate_status,
        )
        self.retry_certificate = to_streamed_response_wrapper(
            aliases.retry_certificate,
        )


class AsyncAliasesResourceWithStreamingResponse:
    def __init__(self, aliases: AsyncAliasesResource) -> None:
        self._aliases = aliases

        self.create = async_to_streamed_response_wrapper(
            aliases.create,
        )
        self.update = async_to_streamed_response_wrapper(
            aliases.update,
        )
        self.list = async_to_streamed_response_wrapper(
            aliases.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            aliases.delete,
        )
        self.create_multiple = async_to_streamed_response_wrapper(
            aliases.create_multiple,
        )
        self.delete_multiple = async_to_streamed_response_wrapper(
            aliases.delete_multiple,
        )
        self.get = async_to_streamed_response_wrapper(
            aliases.get,
        )
        self.get_certificate_status = async_to_streamed_response_wrapper(
            aliases.get_certificate_status,
        )
        self.retry_certificate = async_to_streamed_response_wrapper(
            aliases.retry_certificate,
        )

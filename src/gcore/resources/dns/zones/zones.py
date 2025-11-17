# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from .dnssec import (
    DnssecResource,
    AsyncDnssecResource,
    DnssecResourceWithRawResponse,
    AsyncDnssecResourceWithRawResponse,
    DnssecResourceWithStreamingResponse,
    AsyncDnssecResourceWithStreamingResponse,
)
from .rrsets import (
    RrsetsResource,
    AsyncRrsetsResource,
    RrsetsResourceWithRawResponse,
    AsyncRrsetsResourceWithRawResponse,
    RrsetsResourceWithStreamingResponse,
    AsyncRrsetsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.dns import (
    zone_list_params,
    zone_create_params,
    zone_import_params,
    zone_replace_params,
    zone_get_statistics_params,
)
from ...._base_client import make_request_options
from ....types.dns.zone_get_response import ZoneGetResponse
from ....types.dns.zone_list_response import ZoneListResponse
from ....types.dns.zone_create_response import ZoneCreateResponse
from ....types.dns.zone_export_response import ZoneExportResponse
from ....types.dns.zone_import_response import ZoneImportResponse
from ....types.dns.zone_get_statistics_response import ZoneGetStatisticsResponse
from ....types.dns.zone_check_delegation_status_response import ZoneCheckDelegationStatusResponse

__all__ = ["ZonesResource", "AsyncZonesResource"]


class ZonesResource(SyncAPIResource):
    @cached_property
    def dnssec(self) -> DnssecResource:
        return DnssecResource(self._client)

    @cached_property
    def rrsets(self) -> RrsetsResource:
        return RrsetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ZonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ZonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ZonesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        contact: str | Omit = omit,
        enabled: bool | Omit = omit,
        expiry: int | Omit = omit,
        meta: Dict[str, object] | Omit = omit,
        nx_ttl: int | Omit = omit,
        primary_server: str | Omit = omit,
        refresh: int | Omit = omit,
        retry: int | Omit = omit,
        serial: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneCreateResponse:
        """
        Add DNS zone.

        Args:
          name: name of DNS zone

          contact: email address of the administrator responsible for this zone

          enabled: If a zone is disabled, then its records will not be resolved on dns servers

          expiry: number of seconds after which secondary name servers should stop answering
              request for this zone

          meta: arbitrarily data of zone in json format you can specify `webhook` url and
              `webhook_method` here webhook will get a map with three arrays: for created,
              updated and deleted rrsets `webhook_method` can be omitted, POST will be used by
              default

          nx_ttl: Time To Live of cache

          primary_server: primary master name server for zone

          refresh: number of seconds after which secondary name servers should query the master for
              the SOA record, to detect zone changes.

          retry: number of seconds after which secondary name servers should retry to request the
              serial number

          serial: Serial number for this zone or Timestamp of zone modification moment. If a
              secondary name server slaved to this one observes an increase in this number,
              the slave will assume that the zone has been updated and initiate a zone
              transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dns/v2/zones",
            body=maybe_transform(
                {
                    "name": name,
                    "contact": contact,
                    "enabled": enabled,
                    "expiry": expiry,
                    "meta": meta,
                    "nx_ttl": nx_ttl,
                    "primary_server": primary_server,
                    "refresh": refresh,
                    "retry": retry,
                    "serial": serial,
                },
                zone_create_params.ZoneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ZoneCreateResponse,
        )

    def list(
        self,
        *,
        id: Iterable[int] | Omit = omit,
        case_sensitive: bool | Omit = omit,
        client_id: Iterable[int] | Omit = omit,
        dynamic: bool | Omit = omit,
        enabled: bool | Omit = omit,
        exact_match: bool | Omit = omit,
        healthcheck: bool | Omit = omit,
        iam_reseller_id: Iterable[int] | Omit = omit,
        limit: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        order_direction: Literal["asc", "desc"] | Omit = omit,
        reseller_id: Iterable[int] | Omit = omit,
        status: str | Omit = omit,
        updated_at_from: Union[str, datetime] | Omit = omit,
        updated_at_to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneListResponse:
        """Show created zones with pagination managed by limit and offset params.

        All query
        params are optional.

        Args:
          id: to pass several ids `id=1&id=3&id=5...`

          client_id: to pass several `client_ids` `client_id=1&client_id=3&client_id=5...`

          dynamic: Zones with dynamic RRsets

          healthcheck: Zones with RRsets that have healthchecks

          limit: Max number of records in response

          name: to pass several names `name=first&name=second...`

          offset: Amount of records to skip before beginning to write in response.

          order_by: Field name to sort by

          order_direction: Ascending or descending order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dns/v2/zones",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "case_sensitive": case_sensitive,
                        "client_id": client_id,
                        "dynamic": dynamic,
                        "enabled": enabled,
                        "exact_match": exact_match,
                        "healthcheck": healthcheck,
                        "iam_reseller_id": iam_reseller_id,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "reseller_id": reseller_id,
                        "status": status,
                        "updated_at_from": updated_at_from,
                        "updated_at_to": updated_at_to,
                    },
                    zone_list_params.ZoneListParams,
                ),
            ),
            cast_to=ZoneListResponse,
        )

    def delete(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete DNS zone and its records and raws.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._delete(
            f"/dns/v2/zones/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def check_delegation_status(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneCheckDelegationStatusResponse:
        """Returns delegation status for specified domain name.

        This endpoint has rate
        limit.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/dns/v2/analyze/{name}/delegation-status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ZoneCheckDelegationStatusResponse,
        )

    def disable(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Disable DNS zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._patch(
            f"/dns/v2/zones/{name}/disable",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def enable(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Enable DNS zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._patch(
            f"/dns/v2/zones/{name}/enable",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def export(
        self,
        zone_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneExportResponse:
        """
        Export zone to bind9 format.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        return self._get(
            f"/dns/v2/zones/{zone_name}/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ZoneExportResponse,
        )

    def get(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneGetResponse:
        """
        Zone info by zone name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/dns/v2/zones/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ZoneGetResponse,
        )

    def get_statistics(
        self,
        name: str,
        *,
        from_: int | Omit = omit,
        granularity: str | Omit = omit,
        record_type: str | Omit = omit,
        to: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneGetStatisticsResponse:
        """
        Statistics of DNS zone in common and by record types.

        To get summary statistics for all zones use `all` instead of zone name in path.

        Note: Consumption statistics is updated in near real-time as a standard
        practice. However, the frequency of updates can vary, but they are typically
        available within a 30 minutes period. Exceptions, such as maintenance periods,
        may delay data beyond 30 minutes until servers resume and backfill missing
        statistics.

        Args:
          from_: Beginning of the requested time period (Unix Timestamp, UTC.)

              In a query string: &from=1709068637

          granularity: Granularity parameter string is a sequence of decimal numbers, each with
              optional fraction and a unit suffix, such as "300ms", "1.5h" or "2h45m".

              Valid time units are "s", "m", "h".

          record_type: DNS record type.

              Possible values:

              - A
              - AAAA
              - NS
              - CNAME
              - MX
              - TXT
              - SVCB
              - HTTPS

          to: End of the requested time period (Unix Timestamp, UTC.)

              In a query string: &to=1709673437

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/dns/v2/zones/{name}/statistics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "granularity": granularity,
                        "record_type": record_type,
                        "to": to,
                    },
                    zone_get_statistics_params.ZoneGetStatisticsParams,
                ),
            ),
            cast_to=ZoneGetStatisticsResponse,
        )

    def import_(
        self,
        zone_name: str,
        *,
        body: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneImportResponse:
        """Import zone in bind9 format.

        Args:
          body: Read reads up to len(p) bytes into p.

        It returns the number of bytes read (0 <=
              n <= len(p)) and any error encountered. Even if Read returns n < len(p), it may
              use all of p as scratch space during the call. If some data is available but not
              len(p) bytes, Read conventionally returns what is available instead of waiting
              for more.

              When Read encounters an error or end-of-file condition after successfully
              reading n > 0 bytes, it returns the number of bytes read. It may return the
              (non-nil) error from the same call or return the error (and n == 0) from a
              subsequent call. An instance of this general case is that a Reader returning a
              non-zero number of bytes at the end of the input stream may return either err ==
              EOF or err == nil. The next Read should return 0, EOF.

              Callers should always process the n > 0 bytes returned before considering the
              error err. Doing so correctly handles I/O errors that happen after reading some
              bytes and also both of the allowed EOF behaviors.

              If len(p) == 0, Read should always return n == 0. It may return a non-nil error
              if some error condition is known, such as EOF.

              Implementations of Read are discouraged from returning a zero byte count with a
              nil error, except when len(p) == 0. Callers should treat a return of 0 and nil
              as indicating that nothing happened; in particular it does not indicate EOF.

              Implementations must not retain p.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        return self._post(
            f"/dns/v2/zones/{zone_name}/import",
            body=maybe_transform(body, zone_import_params.ZoneImportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ZoneImportResponse,
        )

    def replace(
        self,
        path_name: str,
        *,
        body_name: str,
        contact: str | Omit = omit,
        enabled: bool | Omit = omit,
        expiry: int | Omit = omit,
        meta: Dict[str, object] | Omit = omit,
        nx_ttl: int | Omit = omit,
        primary_server: str | Omit = omit,
        refresh: int | Omit = omit,
        retry: int | Omit = omit,
        serial: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update DNS zone and SOA record.

        Args:
          body_name: name of DNS zone

          contact: email address of the administrator responsible for this zone

          enabled: If a zone is disabled, then its records will not be resolved on dns servers

          expiry: number of seconds after which secondary name servers should stop answering
              request for this zone

          meta: arbitrarily data of zone in json format you can specify `webhook` url and
              `webhook_method` here webhook will get a map with three arrays: for created,
              updated and deleted rrsets `webhook_method` can be omitted, POST will be used by
              default

          nx_ttl: Time To Live of cache

          primary_server: primary master name server for zone

          refresh: number of seconds after which secondary name servers should query the master for
              the SOA record, to detect zone changes.

          retry: number of seconds after which secondary name servers should retry to request the
              serial number

          serial: Serial number for this zone or Timestamp of zone modification moment. If a
              secondary name server slaved to this one observes an increase in this number,
              the slave will assume that the zone has been updated and initiate a zone
              transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_name:
            raise ValueError(f"Expected a non-empty value for `path_name` but received {path_name!r}")
        return self._put(
            f"/dns/v2/zones/{path_name}",
            body=maybe_transform(
                {
                    "body_name": body_name,
                    "contact": contact,
                    "enabled": enabled,
                    "expiry": expiry,
                    "meta": meta,
                    "nx_ttl": nx_ttl,
                    "primary_server": primary_server,
                    "refresh": refresh,
                    "retry": retry,
                    "serial": serial,
                },
                zone_replace_params.ZoneReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncZonesResource(AsyncAPIResource):
    @cached_property
    def dnssec(self) -> AsyncDnssecResource:
        return AsyncDnssecResource(self._client)

    @cached_property
    def rrsets(self) -> AsyncRrsetsResource:
        return AsyncRrsetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncZonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncZonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncZonesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        contact: str | Omit = omit,
        enabled: bool | Omit = omit,
        expiry: int | Omit = omit,
        meta: Dict[str, object] | Omit = omit,
        nx_ttl: int | Omit = omit,
        primary_server: str | Omit = omit,
        refresh: int | Omit = omit,
        retry: int | Omit = omit,
        serial: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneCreateResponse:
        """
        Add DNS zone.

        Args:
          name: name of DNS zone

          contact: email address of the administrator responsible for this zone

          enabled: If a zone is disabled, then its records will not be resolved on dns servers

          expiry: number of seconds after which secondary name servers should stop answering
              request for this zone

          meta: arbitrarily data of zone in json format you can specify `webhook` url and
              `webhook_method` here webhook will get a map with three arrays: for created,
              updated and deleted rrsets `webhook_method` can be omitted, POST will be used by
              default

          nx_ttl: Time To Live of cache

          primary_server: primary master name server for zone

          refresh: number of seconds after which secondary name servers should query the master for
              the SOA record, to detect zone changes.

          retry: number of seconds after which secondary name servers should retry to request the
              serial number

          serial: Serial number for this zone or Timestamp of zone modification moment. If a
              secondary name server slaved to this one observes an increase in this number,
              the slave will assume that the zone has been updated and initiate a zone
              transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dns/v2/zones",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "contact": contact,
                    "enabled": enabled,
                    "expiry": expiry,
                    "meta": meta,
                    "nx_ttl": nx_ttl,
                    "primary_server": primary_server,
                    "refresh": refresh,
                    "retry": retry,
                    "serial": serial,
                },
                zone_create_params.ZoneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ZoneCreateResponse,
        )

    async def list(
        self,
        *,
        id: Iterable[int] | Omit = omit,
        case_sensitive: bool | Omit = omit,
        client_id: Iterable[int] | Omit = omit,
        dynamic: bool | Omit = omit,
        enabled: bool | Omit = omit,
        exact_match: bool | Omit = omit,
        healthcheck: bool | Omit = omit,
        iam_reseller_id: Iterable[int] | Omit = omit,
        limit: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        order_direction: Literal["asc", "desc"] | Omit = omit,
        reseller_id: Iterable[int] | Omit = omit,
        status: str | Omit = omit,
        updated_at_from: Union[str, datetime] | Omit = omit,
        updated_at_to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneListResponse:
        """Show created zones with pagination managed by limit and offset params.

        All query
        params are optional.

        Args:
          id: to pass several ids `id=1&id=3&id=5...`

          client_id: to pass several `client_ids` `client_id=1&client_id=3&client_id=5...`

          dynamic: Zones with dynamic RRsets

          healthcheck: Zones with RRsets that have healthchecks

          limit: Max number of records in response

          name: to pass several names `name=first&name=second...`

          offset: Amount of records to skip before beginning to write in response.

          order_by: Field name to sort by

          order_direction: Ascending or descending order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dns/v2/zones",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "case_sensitive": case_sensitive,
                        "client_id": client_id,
                        "dynamic": dynamic,
                        "enabled": enabled,
                        "exact_match": exact_match,
                        "healthcheck": healthcheck,
                        "iam_reseller_id": iam_reseller_id,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "reseller_id": reseller_id,
                        "status": status,
                        "updated_at_from": updated_at_from,
                        "updated_at_to": updated_at_to,
                    },
                    zone_list_params.ZoneListParams,
                ),
            ),
            cast_to=ZoneListResponse,
        )

    async def delete(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete DNS zone and its records and raws.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._delete(
            f"/dns/v2/zones/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def check_delegation_status(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneCheckDelegationStatusResponse:
        """Returns delegation status for specified domain name.

        This endpoint has rate
        limit.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/dns/v2/analyze/{name}/delegation-status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ZoneCheckDelegationStatusResponse,
        )

    async def disable(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Disable DNS zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._patch(
            f"/dns/v2/zones/{name}/disable",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def enable(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Enable DNS zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._patch(
            f"/dns/v2/zones/{name}/enable",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def export(
        self,
        zone_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneExportResponse:
        """
        Export zone to bind9 format.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        return await self._get(
            f"/dns/v2/zones/{zone_name}/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ZoneExportResponse,
        )

    async def get(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneGetResponse:
        """
        Zone info by zone name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/dns/v2/zones/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ZoneGetResponse,
        )

    async def get_statistics(
        self,
        name: str,
        *,
        from_: int | Omit = omit,
        granularity: str | Omit = omit,
        record_type: str | Omit = omit,
        to: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneGetStatisticsResponse:
        """
        Statistics of DNS zone in common and by record types.

        To get summary statistics for all zones use `all` instead of zone name in path.

        Note: Consumption statistics is updated in near real-time as a standard
        practice. However, the frequency of updates can vary, but they are typically
        available within a 30 minutes period. Exceptions, such as maintenance periods,
        may delay data beyond 30 minutes until servers resume and backfill missing
        statistics.

        Args:
          from_: Beginning of the requested time period (Unix Timestamp, UTC.)

              In a query string: &from=1709068637

          granularity: Granularity parameter string is a sequence of decimal numbers, each with
              optional fraction and a unit suffix, such as "300ms", "1.5h" or "2h45m".

              Valid time units are "s", "m", "h".

          record_type: DNS record type.

              Possible values:

              - A
              - AAAA
              - NS
              - CNAME
              - MX
              - TXT
              - SVCB
              - HTTPS

          to: End of the requested time period (Unix Timestamp, UTC.)

              In a query string: &to=1709673437

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/dns/v2/zones/{name}/statistics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "granularity": granularity,
                        "record_type": record_type,
                        "to": to,
                    },
                    zone_get_statistics_params.ZoneGetStatisticsParams,
                ),
            ),
            cast_to=ZoneGetStatisticsResponse,
        )

    async def import_(
        self,
        zone_name: str,
        *,
        body: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneImportResponse:
        """Import zone in bind9 format.

        Args:
          body: Read reads up to len(p) bytes into p.

        It returns the number of bytes read (0 <=
              n <= len(p)) and any error encountered. Even if Read returns n < len(p), it may
              use all of p as scratch space during the call. If some data is available but not
              len(p) bytes, Read conventionally returns what is available instead of waiting
              for more.

              When Read encounters an error or end-of-file condition after successfully
              reading n > 0 bytes, it returns the number of bytes read. It may return the
              (non-nil) error from the same call or return the error (and n == 0) from a
              subsequent call. An instance of this general case is that a Reader returning a
              non-zero number of bytes at the end of the input stream may return either err ==
              EOF or err == nil. The next Read should return 0, EOF.

              Callers should always process the n > 0 bytes returned before considering the
              error err. Doing so correctly handles I/O errors that happen after reading some
              bytes and also both of the allowed EOF behaviors.

              If len(p) == 0, Read should always return n == 0. It may return a non-nil error
              if some error condition is known, such as EOF.

              Implementations of Read are discouraged from returning a zero byte count with a
              nil error, except when len(p) == 0. Callers should treat a return of 0 and nil
              as indicating that nothing happened; in particular it does not indicate EOF.

              Implementations must not retain p.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        return await self._post(
            f"/dns/v2/zones/{zone_name}/import",
            body=await async_maybe_transform(body, zone_import_params.ZoneImportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ZoneImportResponse,
        )

    async def replace(
        self,
        path_name: str,
        *,
        body_name: str,
        contact: str | Omit = omit,
        enabled: bool | Omit = omit,
        expiry: int | Omit = omit,
        meta: Dict[str, object] | Omit = omit,
        nx_ttl: int | Omit = omit,
        primary_server: str | Omit = omit,
        refresh: int | Omit = omit,
        retry: int | Omit = omit,
        serial: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update DNS zone and SOA record.

        Args:
          body_name: name of DNS zone

          contact: email address of the administrator responsible for this zone

          enabled: If a zone is disabled, then its records will not be resolved on dns servers

          expiry: number of seconds after which secondary name servers should stop answering
              request for this zone

          meta: arbitrarily data of zone in json format you can specify `webhook` url and
              `webhook_method` here webhook will get a map with three arrays: for created,
              updated and deleted rrsets `webhook_method` can be omitted, POST will be used by
              default

          nx_ttl: Time To Live of cache

          primary_server: primary master name server for zone

          refresh: number of seconds after which secondary name servers should query the master for
              the SOA record, to detect zone changes.

          retry: number of seconds after which secondary name servers should retry to request the
              serial number

          serial: Serial number for this zone or Timestamp of zone modification moment. If a
              secondary name server slaved to this one observes an increase in this number,
              the slave will assume that the zone has been updated and initiate a zone
              transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_name:
            raise ValueError(f"Expected a non-empty value for `path_name` but received {path_name!r}")
        return await self._put(
            f"/dns/v2/zones/{path_name}",
            body=await async_maybe_transform(
                {
                    "body_name": body_name,
                    "contact": contact,
                    "enabled": enabled,
                    "expiry": expiry,
                    "meta": meta,
                    "nx_ttl": nx_ttl,
                    "primary_server": primary_server,
                    "refresh": refresh,
                    "retry": retry,
                    "serial": serial,
                },
                zone_replace_params.ZoneReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ZonesResourceWithRawResponse:
    def __init__(self, zones: ZonesResource) -> None:
        self._zones = zones

        self.create = to_raw_response_wrapper(
            zones.create,
        )
        self.list = to_raw_response_wrapper(
            zones.list,
        )
        self.delete = to_raw_response_wrapper(
            zones.delete,
        )
        self.check_delegation_status = to_raw_response_wrapper(
            zones.check_delegation_status,
        )
        self.disable = to_raw_response_wrapper(
            zones.disable,
        )
        self.enable = to_raw_response_wrapper(
            zones.enable,
        )
        self.export = to_raw_response_wrapper(
            zones.export,
        )
        self.get = to_raw_response_wrapper(
            zones.get,
        )
        self.get_statistics = to_raw_response_wrapper(
            zones.get_statistics,
        )
        self.import_ = to_raw_response_wrapper(
            zones.import_,
        )
        self.replace = to_raw_response_wrapper(
            zones.replace,
        )

    @cached_property
    def dnssec(self) -> DnssecResourceWithRawResponse:
        return DnssecResourceWithRawResponse(self._zones.dnssec)

    @cached_property
    def rrsets(self) -> RrsetsResourceWithRawResponse:
        return RrsetsResourceWithRawResponse(self._zones.rrsets)


class AsyncZonesResourceWithRawResponse:
    def __init__(self, zones: AsyncZonesResource) -> None:
        self._zones = zones

        self.create = async_to_raw_response_wrapper(
            zones.create,
        )
        self.list = async_to_raw_response_wrapper(
            zones.list,
        )
        self.delete = async_to_raw_response_wrapper(
            zones.delete,
        )
        self.check_delegation_status = async_to_raw_response_wrapper(
            zones.check_delegation_status,
        )
        self.disable = async_to_raw_response_wrapper(
            zones.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            zones.enable,
        )
        self.export = async_to_raw_response_wrapper(
            zones.export,
        )
        self.get = async_to_raw_response_wrapper(
            zones.get,
        )
        self.get_statistics = async_to_raw_response_wrapper(
            zones.get_statistics,
        )
        self.import_ = async_to_raw_response_wrapper(
            zones.import_,
        )
        self.replace = async_to_raw_response_wrapper(
            zones.replace,
        )

    @cached_property
    def dnssec(self) -> AsyncDnssecResourceWithRawResponse:
        return AsyncDnssecResourceWithRawResponse(self._zones.dnssec)

    @cached_property
    def rrsets(self) -> AsyncRrsetsResourceWithRawResponse:
        return AsyncRrsetsResourceWithRawResponse(self._zones.rrsets)


class ZonesResourceWithStreamingResponse:
    def __init__(self, zones: ZonesResource) -> None:
        self._zones = zones

        self.create = to_streamed_response_wrapper(
            zones.create,
        )
        self.list = to_streamed_response_wrapper(
            zones.list,
        )
        self.delete = to_streamed_response_wrapper(
            zones.delete,
        )
        self.check_delegation_status = to_streamed_response_wrapper(
            zones.check_delegation_status,
        )
        self.disable = to_streamed_response_wrapper(
            zones.disable,
        )
        self.enable = to_streamed_response_wrapper(
            zones.enable,
        )
        self.export = to_streamed_response_wrapper(
            zones.export,
        )
        self.get = to_streamed_response_wrapper(
            zones.get,
        )
        self.get_statistics = to_streamed_response_wrapper(
            zones.get_statistics,
        )
        self.import_ = to_streamed_response_wrapper(
            zones.import_,
        )
        self.replace = to_streamed_response_wrapper(
            zones.replace,
        )

    @cached_property
    def dnssec(self) -> DnssecResourceWithStreamingResponse:
        return DnssecResourceWithStreamingResponse(self._zones.dnssec)

    @cached_property
    def rrsets(self) -> RrsetsResourceWithStreamingResponse:
        return RrsetsResourceWithStreamingResponse(self._zones.rrsets)


class AsyncZonesResourceWithStreamingResponse:
    def __init__(self, zones: AsyncZonesResource) -> None:
        self._zones = zones

        self.create = async_to_streamed_response_wrapper(
            zones.create,
        )
        self.list = async_to_streamed_response_wrapper(
            zones.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            zones.delete,
        )
        self.check_delegation_status = async_to_streamed_response_wrapper(
            zones.check_delegation_status,
        )
        self.disable = async_to_streamed_response_wrapper(
            zones.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            zones.enable,
        )
        self.export = async_to_streamed_response_wrapper(
            zones.export,
        )
        self.get = async_to_streamed_response_wrapper(
            zones.get,
        )
        self.get_statistics = async_to_streamed_response_wrapper(
            zones.get_statistics,
        )
        self.import_ = async_to_streamed_response_wrapper(
            zones.import_,
        )
        self.replace = async_to_streamed_response_wrapper(
            zones.replace,
        )

    @cached_property
    def dnssec(self) -> AsyncDnssecResourceWithStreamingResponse:
        return AsyncDnssecResourceWithStreamingResponse(self._zones.dnssec)

    @cached_property
    def rrsets(self) -> AsyncRrsetsResourceWithStreamingResponse:
        return AsyncRrsetsResourceWithStreamingResponse(self._zones.rrsets)

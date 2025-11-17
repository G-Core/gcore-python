# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.dns.zones import (
    rrset_list_params,
    rrset_create_params,
    rrset_replace_params,
    rrset_get_failover_logs_params,
)
from ....types.dns.zones.dns_output_rrset import DNSOutputRrset
from ....types.dns.zones.rrset_list_response import RrsetListResponse
from ....types.dns.zones.rrset_get_failover_logs_response import RrsetGetFailoverLogsResponse

__all__ = ["RrsetsResource", "AsyncRrsetsResource"]


class RrsetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RrsetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return RrsetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RrsetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return RrsetsResourceWithStreamingResponse(self)

    def create(
        self,
        rrset_type: str,
        *,
        zone_name: str,
        rrset_name: str,
        resource_records: Iterable[rrset_create_params.ResourceRecord],
        meta: Dict[str, object] | Omit = omit,
        pickers: Iterable[rrset_create_params.Picker] | Omit = omit,
        ttl: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSOutputRrset:
        """
        Add the RRSet to the zone specified by zoneName, RRSets can be configured to be
        either dynamic or static.

        ### Static RRsets

        Staticly configured RRSets provide DNS responses as is.

        ### Dynamic RRsets

        Dynamic RRSets have picker configuration defined thus it's possible to finely
        customize DNS response. Picking rules are defined on the RRSet level as a list
        of selectors, filters and mutators. Picker considers different resource records
        metadata, requestor IP, and other event-feeds like monitoring. Picker
        configuration is an ordered list defined by "pickers" attribute. Requestor IP is
        determined by EDNS Client Subnet (ECS) if defined, otherwise - by
        client/recursor IP. Selector pickers are used in the specified order until the
        first match, in case of match - all next selectors are bypassed. Filters or
        mutators are applied to the match according to the order they are specified.

        For example, sort records by proximity to user, shuffle based on weights and
        return not more than 3:

        `"pickers": [ { "type": "geodistance" }, { "type": "weighted_shuffle" }, { "type": "first_n", "limit": 3 } ]`

        #### geodns filter

        A resource record is included in the answer if resource record's metadata
        matches requestor info. For each resource record in RRSet, the following
        metadata is considered (in the order specified):

        - `ip` - list of network addresses in CIDR format, e.g.
          `["192.168.15.150/25", "2003:de:2016::/48"]`;
        - `asn` - list of autonomous system numbers, e.g. `[1234, 5678]`;
        - `regions` - list of region codes, e.g. `["de-bw", "de-by"]`;
        - `countries` - list of country codes, e.g. `["de", "lu", "lt"]`;
        - `continents` - list of continent codes, e.g.
          `["af", "an", "eu", "as", "na", "sa", "oc"]`.

        If there is a record (or multiple) with metadata matched IP, it's used as a
        response. If not - asn, then country and then continent are checked for a match.
        If there is no match, then the behaviour is defined by _strict_ parameter of the
        filter.

        Example: `"pickers": [ { "type": "geodns", "strict": true } ]`

        ##### Strict parameter

        `strict: true` means that if no records percolate through the geodns filter it
        returns no answers. `strict: false` means that if no records percolate through
        the geodns filter, all records are passed over.

        #### asn selector

        Resource records which ASN metadata matches ASN of the requestor are picked by
        this selector, and passed to the next non-selector picker, if there is no
        match - next configured picker starts with all records.

        Example: `"pickers": [ {"type": "asn"} ]`

        #### country selector

        Resource records which country metadata matches country of the requestor are
        picked by this selector, and passed to the next non-selector picker, if there is
        no match - next configured picker starts with all records.

        Example: `"pickers": [ { "type": "country" } ]`

        #### continent selector

        Resource records which continent metadata matches continent of the requestor are
        picked by this selector, and passed to the next non-selector picker, if there is
        no match - next configured picker starts with all records.

        Example: `"pickers": [ { "type": "continent" } ]`

        #### region selector

        Resource records which region metadata matches region of the requestor are
        picked by this selector, and passed to the next non-selector picker, if there is
        no match - next configured picker starts with all records. e.g. `fr-nor` for
        France/Normandy.

        Example: `"pickers": [ { "type": "region" } ]`

        #### ip selector

        Resource records which IP metadata matches IP of the requestor are picked by
        this selector, and passed to the next non-selector picker, if there is no
        match - next configured picker starts with all records. Maximum 100 subnets are
        allowed to specify in meta of RR.

        Example: `"pickers": [ { "type": "ip" } ]`

        #### default selector

        When enabled, records marked as default are selected:
        `"meta": {"default": true}`.

        Example:
        `"pickers": [ { "type": "geodns", "strict": false }, { "type": "default" }, { "type": "first_n", "limit": 2 } ]`

        #### geodistance mutator

        The resource records are rearranged in ascending order based on the distance (in
        meters) from requestor to the coordinates specified in latlong metadata.
        Distance is calculated using Haversine formula. The "nearest" to the user's IP
        RR goes first. The records without latlong metadata come last. e.g. for Berlin
        `[52.520008, 13.404954]`.;

        In this configuration the only "nearest" to the requestor record to be returned:
        `"pickers": [ { "type": "geodistance" }, { "type": "first_n", "limit": 1 } ]`

        #### `weighted_shuffle` mutator

        The resource records are rearranged in random order based on the `weight`
        metadata. Default weight (if not specified) is 50.

        Example: `"pickers": [ { "type": "weighted_shuffle" } ]`

        #### `first_n` filter

        Slices first N (N specified as a limit parameter value) resource records.

        Example: `"pickers": [ { "type": "first_n", "limit": 1 } ]` returns only the
        first resource record.

        ##### limit parameter

        Can be a positive value for a specific limit. Use zero or leave it blank to
        indicate no limits.

        Args:
          resource_records: List of resource record from rrset

          meta: Meta information for rrset

          pickers: Set of pickers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        if not rrset_name:
            raise ValueError(f"Expected a non-empty value for `rrset_name` but received {rrset_name!r}")
        if not rrset_type:
            raise ValueError(f"Expected a non-empty value for `rrset_type` but received {rrset_type!r}")
        return self._post(
            f"/dns/v2/zones/{zone_name}/{rrset_name}/{rrset_type}",
            body=maybe_transform(
                {
                    "resource_records": resource_records,
                    "meta": meta,
                    "pickers": pickers,
                    "ttl": ttl,
                },
                rrset_create_params.RrsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DNSOutputRrset,
        )

    def list(
        self,
        zone_name: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        order_direction: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RrsetListResponse:
        """
        List of RRset.

        Args:
          limit: Max number of records in response

          offset: Amount of records to skip before beginning to write in response.

          order_by: Field name to sort by

          order_direction: Ascending or descending order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        return self._get(
            f"/dns/v2/zones/{zone_name}/rrsets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "order_direction": order_direction,
                    },
                    rrset_list_params.RrsetListParams,
                ),
            ),
            cast_to=RrsetListResponse,
        )

    def delete(
        self,
        rrset_type: str,
        *,
        zone_name: str,
        rrset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete RRset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        if not rrset_name:
            raise ValueError(f"Expected a non-empty value for `rrset_name` but received {rrset_name!r}")
        if not rrset_type:
            raise ValueError(f"Expected a non-empty value for `rrset_type` but received {rrset_type!r}")
        return self._delete(
            f"/dns/v2/zones/{zone_name}/{rrset_name}/{rrset_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get(
        self,
        rrset_type: str,
        *,
        zone_name: str,
        rrset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSOutputRrset:
        """
        Particular RRset item info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        if not rrset_name:
            raise ValueError(f"Expected a non-empty value for `rrset_name` but received {rrset_name!r}")
        if not rrset_type:
            raise ValueError(f"Expected a non-empty value for `rrset_type` but received {rrset_type!r}")
        return self._get(
            f"/dns/v2/zones/{zone_name}/{rrset_name}/{rrset_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DNSOutputRrset,
        )

    def get_failover_logs(
        self,
        rrset_type: str,
        *,
        zone_name: str,
        rrset_name: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RrsetGetFailoverLogsResponse:
        """
        Get failover history for the RRset

        Args:
          limit: Max number of records in response

          offset: Amount of records to skip before beginning to write in response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        if not rrset_name:
            raise ValueError(f"Expected a non-empty value for `rrset_name` but received {rrset_name!r}")
        if not rrset_type:
            raise ValueError(f"Expected a non-empty value for `rrset_type` but received {rrset_type!r}")
        return self._get(
            f"/dns/v2/zones/{zone_name}/{rrset_name}/{rrset_type}/failover/log",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    rrset_get_failover_logs_params.RrsetGetFailoverLogsParams,
                ),
            ),
            cast_to=RrsetGetFailoverLogsResponse,
        )

    def replace(
        self,
        rrset_type: str,
        *,
        zone_name: str,
        rrset_name: str,
        resource_records: Iterable[rrset_replace_params.ResourceRecord],
        meta: Dict[str, object] | Omit = omit,
        pickers: Iterable[rrset_replace_params.Picker] | Omit = omit,
        ttl: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSOutputRrset:
        """
        Create/update RRset.

        Args:
          resource_records: List of resource record from rrset

          meta: Meta information for rrset

          pickers: Set of pickers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        if not rrset_name:
            raise ValueError(f"Expected a non-empty value for `rrset_name` but received {rrset_name!r}")
        if not rrset_type:
            raise ValueError(f"Expected a non-empty value for `rrset_type` but received {rrset_type!r}")
        return self._put(
            f"/dns/v2/zones/{zone_name}/{rrset_name}/{rrset_type}",
            body=maybe_transform(
                {
                    "resource_records": resource_records,
                    "meta": meta,
                    "pickers": pickers,
                    "ttl": ttl,
                },
                rrset_replace_params.RrsetReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DNSOutputRrset,
        )


class AsyncRrsetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRrsetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRrsetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRrsetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncRrsetsResourceWithStreamingResponse(self)

    async def create(
        self,
        rrset_type: str,
        *,
        zone_name: str,
        rrset_name: str,
        resource_records: Iterable[rrset_create_params.ResourceRecord],
        meta: Dict[str, object] | Omit = omit,
        pickers: Iterable[rrset_create_params.Picker] | Omit = omit,
        ttl: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSOutputRrset:
        """
        Add the RRSet to the zone specified by zoneName, RRSets can be configured to be
        either dynamic or static.

        ### Static RRsets

        Staticly configured RRSets provide DNS responses as is.

        ### Dynamic RRsets

        Dynamic RRSets have picker configuration defined thus it's possible to finely
        customize DNS response. Picking rules are defined on the RRSet level as a list
        of selectors, filters and mutators. Picker considers different resource records
        metadata, requestor IP, and other event-feeds like monitoring. Picker
        configuration is an ordered list defined by "pickers" attribute. Requestor IP is
        determined by EDNS Client Subnet (ECS) if defined, otherwise - by
        client/recursor IP. Selector pickers are used in the specified order until the
        first match, in case of match - all next selectors are bypassed. Filters or
        mutators are applied to the match according to the order they are specified.

        For example, sort records by proximity to user, shuffle based on weights and
        return not more than 3:

        `"pickers": [ { "type": "geodistance" }, { "type": "weighted_shuffle" }, { "type": "first_n", "limit": 3 } ]`

        #### geodns filter

        A resource record is included in the answer if resource record's metadata
        matches requestor info. For each resource record in RRSet, the following
        metadata is considered (in the order specified):

        - `ip` - list of network addresses in CIDR format, e.g.
          `["192.168.15.150/25", "2003:de:2016::/48"]`;
        - `asn` - list of autonomous system numbers, e.g. `[1234, 5678]`;
        - `regions` - list of region codes, e.g. `["de-bw", "de-by"]`;
        - `countries` - list of country codes, e.g. `["de", "lu", "lt"]`;
        - `continents` - list of continent codes, e.g.
          `["af", "an", "eu", "as", "na", "sa", "oc"]`.

        If there is a record (or multiple) with metadata matched IP, it's used as a
        response. If not - asn, then country and then continent are checked for a match.
        If there is no match, then the behaviour is defined by _strict_ parameter of the
        filter.

        Example: `"pickers": [ { "type": "geodns", "strict": true } ]`

        ##### Strict parameter

        `strict: true` means that if no records percolate through the geodns filter it
        returns no answers. `strict: false` means that if no records percolate through
        the geodns filter, all records are passed over.

        #### asn selector

        Resource records which ASN metadata matches ASN of the requestor are picked by
        this selector, and passed to the next non-selector picker, if there is no
        match - next configured picker starts with all records.

        Example: `"pickers": [ {"type": "asn"} ]`

        #### country selector

        Resource records which country metadata matches country of the requestor are
        picked by this selector, and passed to the next non-selector picker, if there is
        no match - next configured picker starts with all records.

        Example: `"pickers": [ { "type": "country" } ]`

        #### continent selector

        Resource records which continent metadata matches continent of the requestor are
        picked by this selector, and passed to the next non-selector picker, if there is
        no match - next configured picker starts with all records.

        Example: `"pickers": [ { "type": "continent" } ]`

        #### region selector

        Resource records which region metadata matches region of the requestor are
        picked by this selector, and passed to the next non-selector picker, if there is
        no match - next configured picker starts with all records. e.g. `fr-nor` for
        France/Normandy.

        Example: `"pickers": [ { "type": "region" } ]`

        #### ip selector

        Resource records which IP metadata matches IP of the requestor are picked by
        this selector, and passed to the next non-selector picker, if there is no
        match - next configured picker starts with all records. Maximum 100 subnets are
        allowed to specify in meta of RR.

        Example: `"pickers": [ { "type": "ip" } ]`

        #### default selector

        When enabled, records marked as default are selected:
        `"meta": {"default": true}`.

        Example:
        `"pickers": [ { "type": "geodns", "strict": false }, { "type": "default" }, { "type": "first_n", "limit": 2 } ]`

        #### geodistance mutator

        The resource records are rearranged in ascending order based on the distance (in
        meters) from requestor to the coordinates specified in latlong metadata.
        Distance is calculated using Haversine formula. The "nearest" to the user's IP
        RR goes first. The records without latlong metadata come last. e.g. for Berlin
        `[52.520008, 13.404954]`.;

        In this configuration the only "nearest" to the requestor record to be returned:
        `"pickers": [ { "type": "geodistance" }, { "type": "first_n", "limit": 1 } ]`

        #### `weighted_shuffle` mutator

        The resource records are rearranged in random order based on the `weight`
        metadata. Default weight (if not specified) is 50.

        Example: `"pickers": [ { "type": "weighted_shuffle" } ]`

        #### `first_n` filter

        Slices first N (N specified as a limit parameter value) resource records.

        Example: `"pickers": [ { "type": "first_n", "limit": 1 } ]` returns only the
        first resource record.

        ##### limit parameter

        Can be a positive value for a specific limit. Use zero or leave it blank to
        indicate no limits.

        Args:
          resource_records: List of resource record from rrset

          meta: Meta information for rrset

          pickers: Set of pickers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        if not rrset_name:
            raise ValueError(f"Expected a non-empty value for `rrset_name` but received {rrset_name!r}")
        if not rrset_type:
            raise ValueError(f"Expected a non-empty value for `rrset_type` but received {rrset_type!r}")
        return await self._post(
            f"/dns/v2/zones/{zone_name}/{rrset_name}/{rrset_type}",
            body=await async_maybe_transform(
                {
                    "resource_records": resource_records,
                    "meta": meta,
                    "pickers": pickers,
                    "ttl": ttl,
                },
                rrset_create_params.RrsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DNSOutputRrset,
        )

    async def list(
        self,
        zone_name: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        order_direction: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RrsetListResponse:
        """
        List of RRset.

        Args:
          limit: Max number of records in response

          offset: Amount of records to skip before beginning to write in response.

          order_by: Field name to sort by

          order_direction: Ascending or descending order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        return await self._get(
            f"/dns/v2/zones/{zone_name}/rrsets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "order_direction": order_direction,
                    },
                    rrset_list_params.RrsetListParams,
                ),
            ),
            cast_to=RrsetListResponse,
        )

    async def delete(
        self,
        rrset_type: str,
        *,
        zone_name: str,
        rrset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete RRset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        if not rrset_name:
            raise ValueError(f"Expected a non-empty value for `rrset_name` but received {rrset_name!r}")
        if not rrset_type:
            raise ValueError(f"Expected a non-empty value for `rrset_type` but received {rrset_type!r}")
        return await self._delete(
            f"/dns/v2/zones/{zone_name}/{rrset_name}/{rrset_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get(
        self,
        rrset_type: str,
        *,
        zone_name: str,
        rrset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSOutputRrset:
        """
        Particular RRset item info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        if not rrset_name:
            raise ValueError(f"Expected a non-empty value for `rrset_name` but received {rrset_name!r}")
        if not rrset_type:
            raise ValueError(f"Expected a non-empty value for `rrset_type` but received {rrset_type!r}")
        return await self._get(
            f"/dns/v2/zones/{zone_name}/{rrset_name}/{rrset_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DNSOutputRrset,
        )

    async def get_failover_logs(
        self,
        rrset_type: str,
        *,
        zone_name: str,
        rrset_name: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RrsetGetFailoverLogsResponse:
        """
        Get failover history for the RRset

        Args:
          limit: Max number of records in response

          offset: Amount of records to skip before beginning to write in response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        if not rrset_name:
            raise ValueError(f"Expected a non-empty value for `rrset_name` but received {rrset_name!r}")
        if not rrset_type:
            raise ValueError(f"Expected a non-empty value for `rrset_type` but received {rrset_type!r}")
        return await self._get(
            f"/dns/v2/zones/{zone_name}/{rrset_name}/{rrset_type}/failover/log",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    rrset_get_failover_logs_params.RrsetGetFailoverLogsParams,
                ),
            ),
            cast_to=RrsetGetFailoverLogsResponse,
        )

    async def replace(
        self,
        rrset_type: str,
        *,
        zone_name: str,
        rrset_name: str,
        resource_records: Iterable[rrset_replace_params.ResourceRecord],
        meta: Dict[str, object] | Omit = omit,
        pickers: Iterable[rrset_replace_params.Picker] | Omit = omit,
        ttl: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSOutputRrset:
        """
        Create/update RRset.

        Args:
          resource_records: List of resource record from rrset

          meta: Meta information for rrset

          pickers: Set of pickers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_name:
            raise ValueError(f"Expected a non-empty value for `zone_name` but received {zone_name!r}")
        if not rrset_name:
            raise ValueError(f"Expected a non-empty value for `rrset_name` but received {rrset_name!r}")
        if not rrset_type:
            raise ValueError(f"Expected a non-empty value for `rrset_type` but received {rrset_type!r}")
        return await self._put(
            f"/dns/v2/zones/{zone_name}/{rrset_name}/{rrset_type}",
            body=await async_maybe_transform(
                {
                    "resource_records": resource_records,
                    "meta": meta,
                    "pickers": pickers,
                    "ttl": ttl,
                },
                rrset_replace_params.RrsetReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DNSOutputRrset,
        )


class RrsetsResourceWithRawResponse:
    def __init__(self, rrsets: RrsetsResource) -> None:
        self._rrsets = rrsets

        self.create = to_raw_response_wrapper(
            rrsets.create,
        )
        self.list = to_raw_response_wrapper(
            rrsets.list,
        )
        self.delete = to_raw_response_wrapper(
            rrsets.delete,
        )
        self.get = to_raw_response_wrapper(
            rrsets.get,
        )
        self.get_failover_logs = to_raw_response_wrapper(
            rrsets.get_failover_logs,
        )
        self.replace = to_raw_response_wrapper(
            rrsets.replace,
        )


class AsyncRrsetsResourceWithRawResponse:
    def __init__(self, rrsets: AsyncRrsetsResource) -> None:
        self._rrsets = rrsets

        self.create = async_to_raw_response_wrapper(
            rrsets.create,
        )
        self.list = async_to_raw_response_wrapper(
            rrsets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rrsets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            rrsets.get,
        )
        self.get_failover_logs = async_to_raw_response_wrapper(
            rrsets.get_failover_logs,
        )
        self.replace = async_to_raw_response_wrapper(
            rrsets.replace,
        )


class RrsetsResourceWithStreamingResponse:
    def __init__(self, rrsets: RrsetsResource) -> None:
        self._rrsets = rrsets

        self.create = to_streamed_response_wrapper(
            rrsets.create,
        )
        self.list = to_streamed_response_wrapper(
            rrsets.list,
        )
        self.delete = to_streamed_response_wrapper(
            rrsets.delete,
        )
        self.get = to_streamed_response_wrapper(
            rrsets.get,
        )
        self.get_failover_logs = to_streamed_response_wrapper(
            rrsets.get_failover_logs,
        )
        self.replace = to_streamed_response_wrapper(
            rrsets.replace,
        )


class AsyncRrsetsResourceWithStreamingResponse:
    def __init__(self, rrsets: AsyncRrsetsResource) -> None:
        self._rrsets = rrsets

        self.create = async_to_streamed_response_wrapper(
            rrsets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            rrsets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rrsets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            rrsets.get,
        )
        self.get_failover_logs = async_to_streamed_response_wrapper(
            rrsets.get_failover_logs,
        )
        self.replace = async_to_streamed_response_wrapper(
            rrsets.replace,
        )

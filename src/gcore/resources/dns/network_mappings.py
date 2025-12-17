# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.dns import network_mapping_list_params, network_mapping_create_params, network_mapping_replace_params
from ..._base_client import make_request_options
from ...types.dns.dns_network_mapping import DNSNetworkMapping
from ...types.dns.dns_mapping_entry_param import DNSMappingEntryParam
from ...types.dns.network_mapping_list_response import NetworkMappingListResponse
from ...types.dns.network_mapping_create_response import NetworkMappingCreateResponse
from ...types.dns.network_mapping_import_response import NetworkMappingImportResponse

__all__ = ["NetworkMappingsResource", "AsyncNetworkMappingsResource"]


class NetworkMappingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NetworkMappingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return NetworkMappingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworkMappingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return NetworkMappingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        mapping: Iterable[DNSMappingEntryParam] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkMappingCreateResponse:
        """
        Create new network mapping.

        Example of request:

        ```
        curl --location --request POST 'https://api.gcore.com/dns/v2/network-mappings' \\
        --header 'Authorization: Bearer ...' \\
        --header 'Content-Type: application/json' \\
        --data-raw '{
        	"name": "test",
        	"mapping": [
        		{
        			"tags": [
        				"tag1"
        			],
        			"cidr4": [
        				"192.0.2.0/24",
        				"198.0.100.0/24"
        			]
        		},
        		{
        			"tags": [
        				"tag2",
        				"tag3"
        			],
        			"cidr4": [
        				"192.1.2.0/24",
        				"198.1.100.0/24"
        			],
        			"cidr6": [
        				"aa:10::/64"
        			]
        		}
        	]
        }'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dns/v2/network-mappings",
            body=maybe_transform(
                {
                    "mapping": mapping,
                    "name": name,
                },
                network_mapping_create_params.NetworkMappingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkMappingCreateResponse,
        )

    def list(
        self,
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
    ) -> NetworkMappingListResponse:
        """
        List of network mappings.

        Example of request:

        ```
         curl --location --request GET 'https://api.gcore.com/dns/v2/network-mappings' \\
         --header 'Authorization: Bearer ...'
        ```

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
        return self._get(
            "/dns/v2/network-mappings",
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
                    network_mapping_list_params.NetworkMappingListParams,
                ),
            ),
            cast_to=NetworkMappingListResponse,
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
    ) -> object:
        """
        Delete network mapping.

        Example of request:

        ```
        curl --location --request DELETE 'https://api.gcore.com/dns/v2/network-mappings/123' \\
        --header 'Authorization: Bearer ...'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/dns/v2/network-mappings/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
    ) -> DNSNetworkMapping:
        """
        Particular network mapping item info

        Example of request:

        ```
        curl --location --request GET 'https://api.gcore.com/dns/v2/network-mappings/123' \\
        --header 'Authorization: Bearer ...'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/dns/v2/network-mappings/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DNSNetworkMapping,
        )

    def get_by_name(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSNetworkMapping:
        """
        Get network mapping by name.

        Particular network mapping item info

        Example of request:

        ```
        curl --location --request GET 'https://api.gcore.com/dns/v2/network-mappings/test-mapping' \\
        --header 'Authorization: Bearer ...'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/dns/v2/network-mappings/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DNSNetworkMapping,
        )

    def import_(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkMappingImportResponse:
        """
        Import network mapping from YAML file.

        Note: A YAML file use spaces as indentation, tabs are not allowed. Example of
        input file:

        ```
          name: mapping_rule_1
          mapping:
              - tags:
                  - tag_name_1
                cidr4:
                  - 127.0.2.0/24
              - tags:
                  - tag_name_2
                  - tag_name_3
                cidr4:
                  - 128.0.1.0/24
                  - 128.0.2.0/24
                  - 128.0.3.0/24
                cidr6:
                  - ac:20::0/64
        ---
          name: mapping_rule_2
          mapping:
              - tags:
                  - my_network
                cidr4:
                  - 129.0.2.0/24
                cidr6:
                  - ac:20::0/64
        ```

        Example of request:

        ```
        curl --location --request POST 'https://api.gcore.com/dns/v2/network-mappings/import' \\
        --header 'Authorization: Bearer ...' \\
        --header 'Content-Type: text/plain' \\
        --data-raw 'name: mapping_rule_1
        mapping:
            - tags:
                - tag_name_1
              cidr4:
                - 127.0.2.0/24
            - tags:
                - tag_name_2
                - tag_name_3
              cidr4:
                - 128.0.1.0/24
                - 128.0.2.0/24
                - 128.0.3.0/24
              cidr6:
                - aa:10::/64
        ---
        name: mapping_rule_2
        mapping:
            - tags:
                - my_network
              cidr4:
                - 129.0.2.0/24
              cidr6:
                - ac:20::0/64'
        ```
        """
        return self._post(
            "/dns/v2/network-mappings/import",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkMappingImportResponse,
        )

    def replace(
        self,
        id: int,
        *,
        mapping: Iterable[DNSMappingEntryParam] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update network mapping (Note: name of network mapping cannot be changed)

        Example of request:

        ```
        curl --location --request PUT 'https://api.gcore.com/dns/v2/network-mappings/123' \\
        --header 'Authorization: Bearer ...' \\
        --header 'Content-Type: application/json' \\
        --data-raw '{
        	"name": "test-mapping",
        	"mapping": [
        		{
        			"tags": [
        				"tag1"
        			],
        			"cidr4": [
        				"192.0.2.0/24"
        			]
        		},
        		{
        			"tags": [
        				"tag2",
        				"tag3"
        			],
        			"cidr4": [
        				"192.1.2.0/24"
        			],
        			"cidr6": [
        				"aa:10::/64"
        			]
        		}
        	]
        }'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/dns/v2/network-mappings/{id}",
            body=maybe_transform(
                {
                    "mapping": mapping,
                    "name": name,
                },
                network_mapping_replace_params.NetworkMappingReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncNetworkMappingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNetworkMappingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworkMappingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworkMappingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncNetworkMappingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        mapping: Iterable[DNSMappingEntryParam] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkMappingCreateResponse:
        """
        Create new network mapping.

        Example of request:

        ```
        curl --location --request POST 'https://api.gcore.com/dns/v2/network-mappings' \\
        --header 'Authorization: Bearer ...' \\
        --header 'Content-Type: application/json' \\
        --data-raw '{
        	"name": "test",
        	"mapping": [
        		{
        			"tags": [
        				"tag1"
        			],
        			"cidr4": [
        				"192.0.2.0/24",
        				"198.0.100.0/24"
        			]
        		},
        		{
        			"tags": [
        				"tag2",
        				"tag3"
        			],
        			"cidr4": [
        				"192.1.2.0/24",
        				"198.1.100.0/24"
        			],
        			"cidr6": [
        				"aa:10::/64"
        			]
        		}
        	]
        }'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dns/v2/network-mappings",
            body=await async_maybe_transform(
                {
                    "mapping": mapping,
                    "name": name,
                },
                network_mapping_create_params.NetworkMappingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkMappingCreateResponse,
        )

    async def list(
        self,
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
    ) -> NetworkMappingListResponse:
        """
        List of network mappings.

        Example of request:

        ```
         curl --location --request GET 'https://api.gcore.com/dns/v2/network-mappings' \\
         --header 'Authorization: Bearer ...'
        ```

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
        return await self._get(
            "/dns/v2/network-mappings",
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
                    network_mapping_list_params.NetworkMappingListParams,
                ),
            ),
            cast_to=NetworkMappingListResponse,
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
    ) -> object:
        """
        Delete network mapping.

        Example of request:

        ```
        curl --location --request DELETE 'https://api.gcore.com/dns/v2/network-mappings/123' \\
        --header 'Authorization: Bearer ...'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/dns/v2/network-mappings/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
    ) -> DNSNetworkMapping:
        """
        Particular network mapping item info

        Example of request:

        ```
        curl --location --request GET 'https://api.gcore.com/dns/v2/network-mappings/123' \\
        --header 'Authorization: Bearer ...'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/dns/v2/network-mappings/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DNSNetworkMapping,
        )

    async def get_by_name(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSNetworkMapping:
        """
        Get network mapping by name.

        Particular network mapping item info

        Example of request:

        ```
        curl --location --request GET 'https://api.gcore.com/dns/v2/network-mappings/test-mapping' \\
        --header 'Authorization: Bearer ...'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/dns/v2/network-mappings/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DNSNetworkMapping,
        )

    async def import_(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkMappingImportResponse:
        """
        Import network mapping from YAML file.

        Note: A YAML file use spaces as indentation, tabs are not allowed. Example of
        input file:

        ```
          name: mapping_rule_1
          mapping:
              - tags:
                  - tag_name_1
                cidr4:
                  - 127.0.2.0/24
              - tags:
                  - tag_name_2
                  - tag_name_3
                cidr4:
                  - 128.0.1.0/24
                  - 128.0.2.0/24
                  - 128.0.3.0/24
                cidr6:
                  - ac:20::0/64
        ---
          name: mapping_rule_2
          mapping:
              - tags:
                  - my_network
                cidr4:
                  - 129.0.2.0/24
                cidr6:
                  - ac:20::0/64
        ```

        Example of request:

        ```
        curl --location --request POST 'https://api.gcore.com/dns/v2/network-mappings/import' \\
        --header 'Authorization: Bearer ...' \\
        --header 'Content-Type: text/plain' \\
        --data-raw 'name: mapping_rule_1
        mapping:
            - tags:
                - tag_name_1
              cidr4:
                - 127.0.2.0/24
            - tags:
                - tag_name_2
                - tag_name_3
              cidr4:
                - 128.0.1.0/24
                - 128.0.2.0/24
                - 128.0.3.0/24
              cidr6:
                - aa:10::/64
        ---
        name: mapping_rule_2
        mapping:
            - tags:
                - my_network
              cidr4:
                - 129.0.2.0/24
              cidr6:
                - ac:20::0/64'
        ```
        """
        return await self._post(
            "/dns/v2/network-mappings/import",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkMappingImportResponse,
        )

    async def replace(
        self,
        id: int,
        *,
        mapping: Iterable[DNSMappingEntryParam] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update network mapping (Note: name of network mapping cannot be changed)

        Example of request:

        ```
        curl --location --request PUT 'https://api.gcore.com/dns/v2/network-mappings/123' \\
        --header 'Authorization: Bearer ...' \\
        --header 'Content-Type: application/json' \\
        --data-raw '{
        	"name": "test-mapping",
        	"mapping": [
        		{
        			"tags": [
        				"tag1"
        			],
        			"cidr4": [
        				"192.0.2.0/24"
        			]
        		},
        		{
        			"tags": [
        				"tag2",
        				"tag3"
        			],
        			"cidr4": [
        				"192.1.2.0/24"
        			],
        			"cidr6": [
        				"aa:10::/64"
        			]
        		}
        	]
        }'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/dns/v2/network-mappings/{id}",
            body=await async_maybe_transform(
                {
                    "mapping": mapping,
                    "name": name,
                },
                network_mapping_replace_params.NetworkMappingReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class NetworkMappingsResourceWithRawResponse:
    def __init__(self, network_mappings: NetworkMappingsResource) -> None:
        self._network_mappings = network_mappings

        self.create = to_raw_response_wrapper(
            network_mappings.create,
        )
        self.list = to_raw_response_wrapper(
            network_mappings.list,
        )
        self.delete = to_raw_response_wrapper(
            network_mappings.delete,
        )
        self.get = to_raw_response_wrapper(
            network_mappings.get,
        )
        self.get_by_name = to_raw_response_wrapper(
            network_mappings.get_by_name,
        )
        self.import_ = to_raw_response_wrapper(
            network_mappings.import_,
        )
        self.replace = to_raw_response_wrapper(
            network_mappings.replace,
        )


class AsyncNetworkMappingsResourceWithRawResponse:
    def __init__(self, network_mappings: AsyncNetworkMappingsResource) -> None:
        self._network_mappings = network_mappings

        self.create = async_to_raw_response_wrapper(
            network_mappings.create,
        )
        self.list = async_to_raw_response_wrapper(
            network_mappings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            network_mappings.delete,
        )
        self.get = async_to_raw_response_wrapper(
            network_mappings.get,
        )
        self.get_by_name = async_to_raw_response_wrapper(
            network_mappings.get_by_name,
        )
        self.import_ = async_to_raw_response_wrapper(
            network_mappings.import_,
        )
        self.replace = async_to_raw_response_wrapper(
            network_mappings.replace,
        )


class NetworkMappingsResourceWithStreamingResponse:
    def __init__(self, network_mappings: NetworkMappingsResource) -> None:
        self._network_mappings = network_mappings

        self.create = to_streamed_response_wrapper(
            network_mappings.create,
        )
        self.list = to_streamed_response_wrapper(
            network_mappings.list,
        )
        self.delete = to_streamed_response_wrapper(
            network_mappings.delete,
        )
        self.get = to_streamed_response_wrapper(
            network_mappings.get,
        )
        self.get_by_name = to_streamed_response_wrapper(
            network_mappings.get_by_name,
        )
        self.import_ = to_streamed_response_wrapper(
            network_mappings.import_,
        )
        self.replace = to_streamed_response_wrapper(
            network_mappings.replace,
        )


class AsyncNetworkMappingsResourceWithStreamingResponse:
    def __init__(self, network_mappings: AsyncNetworkMappingsResource) -> None:
        self._network_mappings = network_mappings

        self.create = async_to_streamed_response_wrapper(
            network_mappings.create,
        )
        self.list = async_to_streamed_response_wrapper(
            network_mappings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            network_mappings.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            network_mappings.get,
        )
        self.get_by_name = async_to_streamed_response_wrapper(
            network_mappings.get_by_name,
        )
        self.import_ = async_to_streamed_response_wrapper(
            network_mappings.import_,
        )
        self.replace = async_to_streamed_response_wrapper(
            network_mappings.replace,
        )

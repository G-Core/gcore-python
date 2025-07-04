# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.cloud import floating_ip_list_params, floating_ip_assign_params, floating_ip_create_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cloud.floating_ip import FloatingIP
from ...types.cloud.task_id_list import TaskIDList
from ...types.cloud.floating_ip_detailed import FloatingIPDetailed

__all__ = ["FloatingIPsResource", "AsyncFloatingIPsResource"]


class FloatingIPsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FloatingIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return FloatingIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FloatingIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return FloatingIPsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        fixed_ip_address: Optional[str] | NotGiven = NOT_GIVEN,
        port_id: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create floating IP

        Args:
          project_id: Project ID

          region_id: Region ID

          fixed_ip_address: If the port has multiple IP addresses, a specific one can be selected using this
              field. If not specified, the first IP in the port's list will be used by
              default.

          port_id: If provided, the floating IP will be immediately attached to the specified port.

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._post(
            f"/cloud/v1/floatingips/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "fixed_ip_address": fixed_ip_address,
                    "port_id": port_id,
                    "tags": tags,
                },
                floating_ip_create_params.FloatingIPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        tag_key: List[str] | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[FloatingIPDetailed]:
        """
        List floating IPs

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Optional. Limit the number of returned items

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          tag_key: Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2

          tag_key_value: Optional. Filter by tag key-value pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/floatingips/{project_id}/{region_id}",
            page=SyncOffsetPage[FloatingIPDetailed],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                    },
                    floating_ip_list_params.FloatingIPListParams,
                ),
            ),
            model=FloatingIPDetailed,
        )

    def delete(
        self,
        floating_ip_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete floating IP

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not floating_ip_id:
            raise ValueError(f"Expected a non-empty value for `floating_ip_id` but received {floating_ip_id!r}")
        return self._delete(
            f"/cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def assign(
        self,
        floating_ip_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        fixed_ip_address: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FloatingIP:
        """
        Assign floating IP to instance or loadbalancer

        Args:
          port_id: Port ID

          fixed_ip_address: Fixed IP address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not floating_ip_id:
            raise ValueError(f"Expected a non-empty value for `floating_ip_id` but received {floating_ip_id!r}")
        return self._post(
            f"/cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}/assign",
            body=maybe_transform(
                {
                    "port_id": port_id,
                    "fixed_ip_address": fixed_ip_address,
                },
                floating_ip_assign_params.FloatingIPAssignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIP,
        )

    def get(
        self,
        floating_ip_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FloatingIP:
        """
        Get floating IP

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not floating_ip_id:
            raise ValueError(f"Expected a non-empty value for `floating_ip_id` but received {floating_ip_id!r}")
        return self._get(
            f"/cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIP,
        )

    def unassign(
        self,
        floating_ip_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FloatingIP:
        """
        Unassign floating IP

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not floating_ip_id:
            raise ValueError(f"Expected a non-empty value for `floating_ip_id` but received {floating_ip_id!r}")
        return self._post(
            f"/cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}/unassign",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIP,
        )


class AsyncFloatingIPsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFloatingIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFloatingIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFloatingIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncFloatingIPsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        fixed_ip_address: Optional[str] | NotGiven = NOT_GIVEN,
        port_id: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create floating IP

        Args:
          project_id: Project ID

          region_id: Region ID

          fixed_ip_address: If the port has multiple IP addresses, a specific one can be selected using this
              field. If not specified, the first IP in the port's list will be used by
              default.

          port_id: If provided, the floating IP will be immediately attached to the specified port.

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._post(
            f"/cloud/v1/floatingips/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "fixed_ip_address": fixed_ip_address,
                    "port_id": port_id,
                    "tags": tags,
                },
                floating_ip_create_params.FloatingIPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        tag_key: List[str] | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[FloatingIPDetailed, AsyncOffsetPage[FloatingIPDetailed]]:
        """
        List floating IPs

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Optional. Limit the number of returned items

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          tag_key: Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2

          tag_key_value: Optional. Filter by tag key-value pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/floatingips/{project_id}/{region_id}",
            page=AsyncOffsetPage[FloatingIPDetailed],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                    },
                    floating_ip_list_params.FloatingIPListParams,
                ),
            ),
            model=FloatingIPDetailed,
        )

    async def delete(
        self,
        floating_ip_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete floating IP

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not floating_ip_id:
            raise ValueError(f"Expected a non-empty value for `floating_ip_id` but received {floating_ip_id!r}")
        return await self._delete(
            f"/cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def assign(
        self,
        floating_ip_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        fixed_ip_address: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FloatingIP:
        """
        Assign floating IP to instance or loadbalancer

        Args:
          port_id: Port ID

          fixed_ip_address: Fixed IP address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not floating_ip_id:
            raise ValueError(f"Expected a non-empty value for `floating_ip_id` but received {floating_ip_id!r}")
        return await self._post(
            f"/cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}/assign",
            body=await async_maybe_transform(
                {
                    "port_id": port_id,
                    "fixed_ip_address": fixed_ip_address,
                },
                floating_ip_assign_params.FloatingIPAssignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIP,
        )

    async def get(
        self,
        floating_ip_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FloatingIP:
        """
        Get floating IP

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not floating_ip_id:
            raise ValueError(f"Expected a non-empty value for `floating_ip_id` but received {floating_ip_id!r}")
        return await self._get(
            f"/cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIP,
        )

    async def unassign(
        self,
        floating_ip_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FloatingIP:
        """
        Unassign floating IP

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not floating_ip_id:
            raise ValueError(f"Expected a non-empty value for `floating_ip_id` but received {floating_ip_id!r}")
        return await self._post(
            f"/cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}/unassign",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIP,
        )


class FloatingIPsResourceWithRawResponse:
    def __init__(self, floating_ips: FloatingIPsResource) -> None:
        self._floating_ips = floating_ips

        self.create = to_raw_response_wrapper(
            floating_ips.create,
        )
        self.list = to_raw_response_wrapper(
            floating_ips.list,
        )
        self.delete = to_raw_response_wrapper(
            floating_ips.delete,
        )
        self.assign = to_raw_response_wrapper(
            floating_ips.assign,
        )
        self.get = to_raw_response_wrapper(
            floating_ips.get,
        )
        self.unassign = to_raw_response_wrapper(
            floating_ips.unassign,
        )


class AsyncFloatingIPsResourceWithRawResponse:
    def __init__(self, floating_ips: AsyncFloatingIPsResource) -> None:
        self._floating_ips = floating_ips

        self.create = async_to_raw_response_wrapper(
            floating_ips.create,
        )
        self.list = async_to_raw_response_wrapper(
            floating_ips.list,
        )
        self.delete = async_to_raw_response_wrapper(
            floating_ips.delete,
        )
        self.assign = async_to_raw_response_wrapper(
            floating_ips.assign,
        )
        self.get = async_to_raw_response_wrapper(
            floating_ips.get,
        )
        self.unassign = async_to_raw_response_wrapper(
            floating_ips.unassign,
        )


class FloatingIPsResourceWithStreamingResponse:
    def __init__(self, floating_ips: FloatingIPsResource) -> None:
        self._floating_ips = floating_ips

        self.create = to_streamed_response_wrapper(
            floating_ips.create,
        )
        self.list = to_streamed_response_wrapper(
            floating_ips.list,
        )
        self.delete = to_streamed_response_wrapper(
            floating_ips.delete,
        )
        self.assign = to_streamed_response_wrapper(
            floating_ips.assign,
        )
        self.get = to_streamed_response_wrapper(
            floating_ips.get,
        )
        self.unassign = to_streamed_response_wrapper(
            floating_ips.unassign,
        )


class AsyncFloatingIPsResourceWithStreamingResponse:
    def __init__(self, floating_ips: AsyncFloatingIPsResource) -> None:
        self._floating_ips = floating_ips

        self.create = async_to_streamed_response_wrapper(
            floating_ips.create,
        )
        self.list = async_to_streamed_response_wrapper(
            floating_ips.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            floating_ips.delete,
        )
        self.assign = async_to_streamed_response_wrapper(
            floating_ips.assign,
        )
        self.get = async_to_streamed_response_wrapper(
            floating_ips.get,
        )
        self.unassign = async_to_streamed_response_wrapper(
            floating_ips.unassign,
        )

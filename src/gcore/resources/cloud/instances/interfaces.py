# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from .interfaces_custom import InterfacesResourceCustomMixin, AsyncInterfacesResourceCustomMixin
from ....types.cloud.instances import interface_list_params, interface_attach_params, interface_detach_params
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.network_interface import NetworkInterface
from ....types.cloud.interface_ip_family import InterfaceIPFamily

__all__ = ["InterfacesResource", "AsyncInterfacesResource"]


class InterfacesResource(InterfacesResourceCustomMixin, SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InterfacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return InterfacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InterfacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return InterfacesResourceWithStreamingResponse(self)

    def list(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[NetworkInterface]:
        """
        List all network interfaces attached to the specified instance.

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          limit: Limit the number of returned items

          offset: Offset value is used to exclude the first set of records from the result

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get_api_list(
            path_template(
                "/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/interfaces",
                project_id=project_id,
                region_id=region_id,
                instance_id=instance_id,
            ),
            page=SyncOffsetPage[NetworkInterface],
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
                    interface_list_params.InterfaceListParams,
                ),
            ),
            model=cast(Any, NetworkInterface),  # Union types cannot be passed in as arguments in the type system
        )

    @overload
    def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ddos_profile: Optional[interface_attach_params.AttachInterfaceExternalRequestSerializerDDOSProfile]
        | Omit = omit,
        interface_name: Optional[str] | Omit = omit,
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Optional[
            Iterable[interface_attach_params.AttachInterfaceExternalRequestSerializerSecurityGroup]
        ]
        | Omit = omit,
        type: Literal["external"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to instance

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name.

          port_group: Each group will be added to a separate trunk.

          security_groups: List of security group IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        ddos_profile: Optional[interface_attach_params.AttachInterfaceSubnetRequestSerializerDDOSProfile] | Omit = omit,
        interface_name: Optional[str] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Optional[Iterable[interface_attach_params.AttachInterfaceSubnetRequestSerializerSecurityGroup]]
        | Omit = omit,
        type: Literal["subnet"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to instance

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          subnet_id: Port will get an IP address from this subnet.

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name.

          port_group: Each group will be added to a separate trunk.

          security_groups: List of security group IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        network_id: str,
        ddos_profile: Optional[interface_attach_params.AttachInterfaceAnySubnetRequestSerializerDDOSProfile]
        | Omit = omit,
        interface_name: Optional[str] | Omit = omit,
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Optional[
            Iterable[interface_attach_params.AttachInterfaceAnySubnetRequestSerializerSecurityGroup]
        ]
        | Omit = omit,
        type: Literal["any_subnet"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to instance

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          network_id: Port will get an IP address in this network subnet.

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name.

          port_group: Each group will be added to a separate trunk.

          security_groups: List of security group IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        ddos_profile: Optional[interface_attach_params.AttachInterfaceReservedFixedIPRequestSerializerDDOSProfile]
        | Omit = omit,
        interface_name: Optional[str] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Optional[
            Iterable[interface_attach_params.AttachInterfaceReservedFixedIPRequestSerializerSecurityGroup]
        ]
        | Omit = omit,
        type: Literal["reserved_fixed_ip"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to instance

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          port_id: Port ID.

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name.

          port_group: Each group will be added to a separate trunk.

          security_groups: List of security group IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ddos_profile: Optional[interface_attach_params.AttachInterfaceExternalRequestSerializerDDOSProfile]
        | Optional[interface_attach_params.AttachInterfaceSubnetRequestSerializerDDOSProfile]
        | Optional[interface_attach_params.AttachInterfaceAnySubnetRequestSerializerDDOSProfile]
        | Optional[interface_attach_params.AttachInterfaceReservedFixedIPRequestSerializerDDOSProfile]
        | Omit = omit,
        interface_name: Optional[str] | Omit = omit,
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Optional[
            Iterable[interface_attach_params.AttachInterfaceExternalRequestSerializerSecurityGroup]
        ]
        | Omit = omit,
        type: Literal["external"]
        | Literal["subnet"]
        | Literal["any_subnet"]
        | Literal["reserved_fixed_ip"]
        | Omit = omit,
        subnet_id: str | Omit = omit,
        network_id: str | Omit = omit,
        port_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            path_template(
                "/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/attach_interface",
                project_id=project_id,
                region_id=region_id,
                instance_id=instance_id,
            ),
            body=maybe_transform(
                {
                    "ddos_profile": ddos_profile,
                    "interface_name": interface_name,
                    "ip_family": ip_family,
                    "port_group": port_group,
                    "security_groups": security_groups,
                    "type": type,
                    "subnet_id": subnet_id,
                    "network_id": network_id,
                    "port_id": port_id,
                },
                interface_attach_params.InterfaceAttachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def detach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ip_address: str,
        port_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Detach interface from instance

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          ip_address: IP address

          port_id: ID of the port

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            path_template(
                "/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/detach_interface",
                project_id=project_id,
                region_id=region_id,
                instance_id=instance_id,
            ),
            body=maybe_transform(
                {
                    "ip_address": ip_address,
                    "port_id": port_id,
                },
                interface_detach_params.InterfaceDetachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class AsyncInterfacesResource(AsyncInterfacesResourceCustomMixin, AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInterfacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInterfacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInterfacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncInterfacesResourceWithStreamingResponse(self)

    def list(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[NetworkInterface, AsyncOffsetPage[NetworkInterface]]:
        """
        List all network interfaces attached to the specified instance.

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          limit: Limit the number of returned items

          offset: Offset value is used to exclude the first set of records from the result

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get_api_list(
            path_template(
                "/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/interfaces",
                project_id=project_id,
                region_id=region_id,
                instance_id=instance_id,
            ),
            page=AsyncOffsetPage[NetworkInterface],
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
                    interface_list_params.InterfaceListParams,
                ),
            ),
            model=cast(Any, NetworkInterface),  # Union types cannot be passed in as arguments in the type system
        )

    @overload
    async def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ddos_profile: Optional[interface_attach_params.AttachInterfaceExternalRequestSerializerDDOSProfile]
        | Omit = omit,
        interface_name: Optional[str] | Omit = omit,
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Optional[
            Iterable[interface_attach_params.AttachInterfaceExternalRequestSerializerSecurityGroup]
        ]
        | Omit = omit,
        type: Literal["external"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to instance

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name.

          port_group: Each group will be added to a separate trunk.

          security_groups: List of security group IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        ddos_profile: Optional[interface_attach_params.AttachInterfaceSubnetRequestSerializerDDOSProfile] | Omit = omit,
        interface_name: Optional[str] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Optional[Iterable[interface_attach_params.AttachInterfaceSubnetRequestSerializerSecurityGroup]]
        | Omit = omit,
        type: Literal["subnet"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to instance

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          subnet_id: Port will get an IP address from this subnet.

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name.

          port_group: Each group will be added to a separate trunk.

          security_groups: List of security group IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        network_id: str,
        ddos_profile: Optional[interface_attach_params.AttachInterfaceAnySubnetRequestSerializerDDOSProfile]
        | Omit = omit,
        interface_name: Optional[str] | Omit = omit,
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Optional[
            Iterable[interface_attach_params.AttachInterfaceAnySubnetRequestSerializerSecurityGroup]
        ]
        | Omit = omit,
        type: Literal["any_subnet"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to instance

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          network_id: Port will get an IP address in this network subnet.

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name.

          port_group: Each group will be added to a separate trunk.

          security_groups: List of security group IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        ddos_profile: Optional[interface_attach_params.AttachInterfaceReservedFixedIPRequestSerializerDDOSProfile]
        | Omit = omit,
        interface_name: Optional[str] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Optional[
            Iterable[interface_attach_params.AttachInterfaceReservedFixedIPRequestSerializerSecurityGroup]
        ]
        | Omit = omit,
        type: Literal["reserved_fixed_ip"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Attach interface to instance

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          port_id: Port ID.

          ddos_profile: Advanced DDoS protection.

          interface_name: Interface name.

          port_group: Each group will be added to a separate trunk.

          security_groups: List of security group IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def attach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ddos_profile: Optional[interface_attach_params.AttachInterfaceExternalRequestSerializerDDOSProfile]
        | Optional[interface_attach_params.AttachInterfaceSubnetRequestSerializerDDOSProfile]
        | Optional[interface_attach_params.AttachInterfaceAnySubnetRequestSerializerDDOSProfile]
        | Optional[interface_attach_params.AttachInterfaceReservedFixedIPRequestSerializerDDOSProfile]
        | Omit = omit,
        interface_name: Optional[str] | Omit = omit,
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        port_group: int | Omit = omit,
        security_groups: Optional[
            Iterable[interface_attach_params.AttachInterfaceExternalRequestSerializerSecurityGroup]
        ]
        | Omit = omit,
        type: Literal["external"]
        | Literal["subnet"]
        | Literal["any_subnet"]
        | Literal["reserved_fixed_ip"]
        | Omit = omit,
        subnet_id: str | Omit = omit,
        network_id: str | Omit = omit,
        port_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            path_template(
                "/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/attach_interface",
                project_id=project_id,
                region_id=region_id,
                instance_id=instance_id,
            ),
            body=await async_maybe_transform(
                {
                    "ddos_profile": ddos_profile,
                    "interface_name": interface_name,
                    "ip_family": ip_family,
                    "port_group": port_group,
                    "security_groups": security_groups,
                    "type": type,
                    "subnet_id": subnet_id,
                    "network_id": network_id,
                    "port_id": port_id,
                },
                interface_attach_params.InterfaceAttachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def detach(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ip_address: str,
        port_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Detach interface from instance

        Args:
          project_id: Project ID

          region_id: Region ID

          instance_id: Instance ID

          ip_address: IP address

          port_id: ID of the port

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            path_template(
                "/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/detach_interface",
                project_id=project_id,
                region_id=region_id,
                instance_id=instance_id,
            ),
            body=await async_maybe_transform(
                {
                    "ip_address": ip_address,
                    "port_id": port_id,
                },
                interface_detach_params.InterfaceDetachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class InterfacesResourceWithRawResponse:
    def __init__(self, interfaces: InterfacesResource) -> None:
        self._interfaces = interfaces

        self.list = to_raw_response_wrapper(
            interfaces.list,
        )
        self.attach = to_raw_response_wrapper(
            interfaces.attach,
        )
        self.attach_and_poll = to_raw_response_wrapper(
            interfaces.attach_and_poll,
        )
        self.detach = to_raw_response_wrapper(
            interfaces.detach,
        )
        self.detach_and_poll = to_raw_response_wrapper(
            interfaces.detach_and_poll,
        )


class AsyncInterfacesResourceWithRawResponse:
    def __init__(self, interfaces: AsyncInterfacesResource) -> None:
        self._interfaces = interfaces

        self.list = async_to_raw_response_wrapper(
            interfaces.list,
        )
        self.attach = async_to_raw_response_wrapper(
            interfaces.attach,
        )
        self.attach_and_poll = async_to_raw_response_wrapper(
            interfaces.attach_and_poll,
        )
        self.detach = async_to_raw_response_wrapper(
            interfaces.detach,
        )
        self.detach_and_poll = async_to_raw_response_wrapper(
            interfaces.detach_and_poll,
        )


class InterfacesResourceWithStreamingResponse:
    def __init__(self, interfaces: InterfacesResource) -> None:
        self._interfaces = interfaces

        self.list = to_streamed_response_wrapper(
            interfaces.list,
        )
        self.attach = to_streamed_response_wrapper(
            interfaces.attach,
        )
        self.attach_and_poll = to_streamed_response_wrapper(
            interfaces.attach_and_poll,
        )
        self.detach = to_streamed_response_wrapper(
            interfaces.detach,
        )
        self.detach_and_poll = to_streamed_response_wrapper(
            interfaces.detach_and_poll,
        )


class AsyncInterfacesResourceWithStreamingResponse:
    def __init__(self, interfaces: AsyncInterfacesResource) -> None:
        self._interfaces = interfaces

        self.list = async_to_streamed_response_wrapper(
            interfaces.list,
        )
        self.attach = async_to_streamed_response_wrapper(
            interfaces.attach,
        )
        self.attach_and_poll = async_to_streamed_response_wrapper(
            interfaces.attach_and_poll,
        )
        self.detach = async_to_streamed_response_wrapper(
            interfaces.detach,
        )
        self.detach_and_poll = async_to_streamed_response_wrapper(
            interfaces.detach_and_poll,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import overload

import httpx

from .flavors import (
    FlavorsResource,
    AsyncFlavorsResource,
    FlavorsResourceWithRawResponse,
    AsyncFlavorsResourceWithRawResponse,
    FlavorsResourceWithStreamingResponse,
    AsyncFlavorsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloud.pricing import instance_preview_params
from .....types.cloud.server_price import ServerPrice

__all__ = ["InstancesResource", "AsyncInstancesResource"]


class InstancesResource(SyncAPIResource):
    @cached_property
    def flavors(self) -> FlavorsResource:
        return FlavorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> InstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return InstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return InstancesResourceWithStreamingResponse(self)

    def get(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerPrice:
        """Get the price of an existing instance.

        The price covers the flavor, the volumes,
        the external IP addresses and the floating IPs.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template(
                "/cloud/v1/projects/{project_id}/pricing/instances/{instance_id}",
                project_id=project_id,
                instance_id=instance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerPrice,
        )

    @overload
    def preview(
        self,
        *,
        project_id: int | None = None,
        flavor_name: str,
        region_id: int,
        boot_volume_id: str | Omit = omit,
        data_volume_ids: SequenceNotStr[str] | Omit = omit,
        interfaces: Iterable[instance_preview_params.InstancePricePreviewReferenceBodySerializerInterface]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerPrice:
        """Get the price of an instance before you create it.

        Send the same body that you
        send to create an instance. The API reads only the fields that change the price.
        The price includes the flavor, the volumes, the ports and the floating IPs. It
        also includes the existing volumes, ports and floating IPs that you attach.

        Args:
          project_id: Project ID.

          flavor_name: Flavor of the server.

          region_id: Region of the server.

          boot_volume_id: Existing boot volume. Omit it to price the server without a boot volume.

          data_volume_ids: Existing data volumes.

          interfaces: Ports in NIC order. An entry with `port_id` is an existing port, any other entry
              is a new one. Omit it to price the server without ports.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def preview(
        self,
        *,
        project_id: int | None = None,
        flavor_name: str,
        region_id: int,
        boot_volume: instance_preview_params.InstancePricePreviewWorkflowBodySerializerBootVolume | Omit = omit,
        data_volumes: Iterable[instance_preview_params.InstancePricePreviewWorkflowBodySerializerDataVolume]
        | Omit = omit,
        interfaces: Iterable[instance_preview_params.InstancePricePreviewWorkflowBodySerializerInterface] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerPrice:
        """Get the price of an instance before you create it.

        Send the same body that you
        send to create an instance. The API reads only the fields that change the price.
        The price includes the flavor, the volumes, the ports and the floating IPs. It
        also includes the existing volumes, ports and floating IPs that you attach.

        Args:
          project_id: Project ID.

          flavor_name: Flavor of the server.

          region_id: Region of the server.

          boot_volume: An entry with `volume_id` is an existing volume, any other entry is a new one.
              Omit it to price the server without a boot volume.

          data_volumes: An entry with `volume_id` is an existing volume, any other entry is a new one.

          interfaces: Ports in NIC order. An entry with `port_id` is an existing port, any other entry
              is a new one. Omit it to price the server without ports.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["flavor_name", "region_id"])
    def preview(
        self,
        *,
        project_id: int | None = None,
        flavor_name: str,
        region_id: int,
        boot_volume_id: str | Omit = omit,
        data_volume_ids: SequenceNotStr[str] | Omit = omit,
        interfaces: Iterable[instance_preview_params.InstancePricePreviewReferenceBodySerializerInterface]
        | Iterable[instance_preview_params.InstancePricePreviewWorkflowBodySerializerInterface]
        | Omit = omit,
        boot_volume: instance_preview_params.InstancePricePreviewWorkflowBodySerializerBootVolume | Omit = omit,
        data_volumes: Iterable[instance_preview_params.InstancePricePreviewWorkflowBodySerializerDataVolume]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerPrice:
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._post(
            path_template("/cloud/v1/projects/{project_id}/pricing/instances", project_id=project_id),
            body=maybe_transform(
                {
                    "flavor_name": flavor_name,
                    "region_id": region_id,
                    "boot_volume_id": boot_volume_id,
                    "data_volume_ids": data_volume_ids,
                    "interfaces": interfaces,
                    "boot_volume": boot_volume,
                    "data_volumes": data_volumes,
                },
                instance_preview_params.InstancePreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerPrice,
        )


class AsyncInstancesResource(AsyncAPIResource):
    @cached_property
    def flavors(self) -> AsyncFlavorsResource:
        return AsyncFlavorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncInstancesResourceWithStreamingResponse(self)

    async def get(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerPrice:
        """Get the price of an existing instance.

        The price covers the flavor, the volumes,
        the external IP addresses and the floating IPs.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template(
                "/cloud/v1/projects/{project_id}/pricing/instances/{instance_id}",
                project_id=project_id,
                instance_id=instance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerPrice,
        )

    @overload
    async def preview(
        self,
        *,
        project_id: int | None = None,
        flavor_name: str,
        region_id: int,
        boot_volume_id: str | Omit = omit,
        data_volume_ids: SequenceNotStr[str] | Omit = omit,
        interfaces: Iterable[instance_preview_params.InstancePricePreviewReferenceBodySerializerInterface]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerPrice:
        """Get the price of an instance before you create it.

        Send the same body that you
        send to create an instance. The API reads only the fields that change the price.
        The price includes the flavor, the volumes, the ports and the floating IPs. It
        also includes the existing volumes, ports and floating IPs that you attach.

        Args:
          project_id: Project ID.

          flavor_name: Flavor of the server.

          region_id: Region of the server.

          boot_volume_id: Existing boot volume. Omit it to price the server without a boot volume.

          data_volume_ids: Existing data volumes.

          interfaces: Ports in NIC order. An entry with `port_id` is an existing port, any other entry
              is a new one. Omit it to price the server without ports.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def preview(
        self,
        *,
        project_id: int | None = None,
        flavor_name: str,
        region_id: int,
        boot_volume: instance_preview_params.InstancePricePreviewWorkflowBodySerializerBootVolume | Omit = omit,
        data_volumes: Iterable[instance_preview_params.InstancePricePreviewWorkflowBodySerializerDataVolume]
        | Omit = omit,
        interfaces: Iterable[instance_preview_params.InstancePricePreviewWorkflowBodySerializerInterface] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerPrice:
        """Get the price of an instance before you create it.

        Send the same body that you
        send to create an instance. The API reads only the fields that change the price.
        The price includes the flavor, the volumes, the ports and the floating IPs. It
        also includes the existing volumes, ports and floating IPs that you attach.

        Args:
          project_id: Project ID.

          flavor_name: Flavor of the server.

          region_id: Region of the server.

          boot_volume: An entry with `volume_id` is an existing volume, any other entry is a new one.
              Omit it to price the server without a boot volume.

          data_volumes: An entry with `volume_id` is an existing volume, any other entry is a new one.

          interfaces: Ports in NIC order. An entry with `port_id` is an existing port, any other entry
              is a new one. Omit it to price the server without ports.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["flavor_name", "region_id"])
    async def preview(
        self,
        *,
        project_id: int | None = None,
        flavor_name: str,
        region_id: int,
        boot_volume_id: str | Omit = omit,
        data_volume_ids: SequenceNotStr[str] | Omit = omit,
        interfaces: Iterable[instance_preview_params.InstancePricePreviewReferenceBodySerializerInterface]
        | Iterable[instance_preview_params.InstancePricePreviewWorkflowBodySerializerInterface]
        | Omit = omit,
        boot_volume: instance_preview_params.InstancePricePreviewWorkflowBodySerializerBootVolume | Omit = omit,
        data_volumes: Iterable[instance_preview_params.InstancePricePreviewWorkflowBodySerializerDataVolume]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerPrice:
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return await self._post(
            path_template("/cloud/v1/projects/{project_id}/pricing/instances", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "flavor_name": flavor_name,
                    "region_id": region_id,
                    "boot_volume_id": boot_volume_id,
                    "data_volume_ids": data_volume_ids,
                    "interfaces": interfaces,
                    "boot_volume": boot_volume,
                    "data_volumes": data_volumes,
                },
                instance_preview_params.InstancePreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerPrice,
        )


class InstancesResourceWithRawResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.get = to_raw_response_wrapper(
            instances.get,
        )
        self.preview = to_raw_response_wrapper(
            instances.preview,
        )

    @cached_property
    def flavors(self) -> FlavorsResourceWithRawResponse:
        return FlavorsResourceWithRawResponse(self._instances.flavors)


class AsyncInstancesResourceWithRawResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.get = async_to_raw_response_wrapper(
            instances.get,
        )
        self.preview = async_to_raw_response_wrapper(
            instances.preview,
        )

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithRawResponse:
        return AsyncFlavorsResourceWithRawResponse(self._instances.flavors)


class InstancesResourceWithStreamingResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.get = to_streamed_response_wrapper(
            instances.get,
        )
        self.preview = to_streamed_response_wrapper(
            instances.preview,
        )

    @cached_property
    def flavors(self) -> FlavorsResourceWithStreamingResponse:
        return FlavorsResourceWithStreamingResponse(self._instances.flavors)


class AsyncInstancesResourceWithStreamingResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.get = async_to_streamed_response_wrapper(
            instances.get,
        )
        self.preview = async_to_streamed_response_wrapper(
            instances.preview,
        )

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithStreamingResponse:
        return AsyncFlavorsResourceWithStreamingResponse(self._instances.flavors)

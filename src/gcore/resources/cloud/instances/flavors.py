# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
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
from ....types.cloud.instances import flavor_list_params
from ....types.cloud.instances.instance_flavor import InstanceFlavor

__all__ = ["FlavorsResource", "AsyncFlavorsResource"]


class FlavorsResource(SyncAPIResource):
    """
    Instance flavors define the CPU, memory, and OS type of an instance, in all regions of the project.
    """

    @cached_property
    def with_raw_response(self) -> FlavorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return FlavorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlavorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return FlavorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        project_id: int | None = None,
        architectures: List[Literal["aarch64", "unknown", "x86_64"]] | Omit = omit,
        available: bool | Omit = omit,
        compatible_with_boot_volume_id: str | Omit = omit,
        compatible_with_image_id: str | Omit = omit,
        compatible_with_snapshot_id: str | Omit = omit,
        limit: int | Omit = omit,
        name: flavor_list_params.Name | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal[
            "name.asc",
            "name.desc",
            "ram_mib.asc",
            "ram_mib.desc",
            "region_id.asc",
            "region_id.desc",
            "vcpus.asc",
            "vcpus.desc",
        ]
        | Omit = omit,
        os_types: List[Literal["linux", "unknown", "windows"]] | Omit = omit,
        ram_mib: flavor_list_params.RamMib | Omit = omit,
        region_ids: Iterable[int] | Omit = omit,
        vcpus: flavor_list_params.Vcpus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[InstanceFlavor]:
        """
        List the virtual instance flavors available to the client, across all regions.

        Args:
          project_id: Project ID.

          architectures: Filter by flavor architecture type(s).

          available: Set to true to return only the available flavors. Set to false to return only
              the flavors that are disabled in their region or out of stock there. Omit it to
              return all flavors.

          compatible_with_boot_volume_id: Return only the flavors that can boot from this volume, from its image metadata.
              An unknown volume matches no flavor. A non-bootable volume or one without image
              metadata is a 400. At most one `compatible_with_`\\** parameter per request.

          compatible_with_image_id: Return only the flavors that can boot this image: its region, OS type and CPU
              architecture. An unknown image matches no flavor. At most one
              `compatible_with_`\\** parameter per request.

          compatible_with_snapshot_id: Return only the flavors that can boot from this snapshot, resolved through its
              parent volume's image metadata. An unknown snapshot matches no flavor. A parent
              volume with no image metadata is a 400. At most one `compatible_with_`\\**
              parameter per request.

          limit: Max items to return.

          name: Operator flavor name filter, e.g. name[prefix]=g2-.

          offset: Items to skip.

          order_by: Sort field and direction.

          os_types: Filter by flavor operating system(s).

          ram_mib: Range filter on RAM size in MiB.

          region_ids: Filter by region ID(s). Omit = all regions.

          vcpus: Range filter on virtual CPU count.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            path_template("/cloud/v1/projects/{project_id}/instances/flavors", project_id=project_id),
            page=SyncOffsetPage[InstanceFlavor],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "architectures": architectures,
                        "available": available,
                        "compatible_with_boot_volume_id": compatible_with_boot_volume_id,
                        "compatible_with_image_id": compatible_with_image_id,
                        "compatible_with_snapshot_id": compatible_with_snapshot_id,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "os_types": os_types,
                        "ram_mib": ram_mib,
                        "region_ids": region_ids,
                        "vcpus": vcpus,
                    },
                    flavor_list_params.FlavorListParams,
                ),
            ),
            model=InstanceFlavor,
        )


class AsyncFlavorsResource(AsyncAPIResource):
    """
    Instance flavors define the CPU, memory, and OS type of an instance, in all regions of the project.
    """

    @cached_property
    def with_raw_response(self) -> AsyncFlavorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlavorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlavorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncFlavorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        project_id: int | None = None,
        architectures: List[Literal["aarch64", "unknown", "x86_64"]] | Omit = omit,
        available: bool | Omit = omit,
        compatible_with_boot_volume_id: str | Omit = omit,
        compatible_with_image_id: str | Omit = omit,
        compatible_with_snapshot_id: str | Omit = omit,
        limit: int | Omit = omit,
        name: flavor_list_params.Name | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal[
            "name.asc",
            "name.desc",
            "ram_mib.asc",
            "ram_mib.desc",
            "region_id.asc",
            "region_id.desc",
            "vcpus.asc",
            "vcpus.desc",
        ]
        | Omit = omit,
        os_types: List[Literal["linux", "unknown", "windows"]] | Omit = omit,
        ram_mib: flavor_list_params.RamMib | Omit = omit,
        region_ids: Iterable[int] | Omit = omit,
        vcpus: flavor_list_params.Vcpus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InstanceFlavor, AsyncOffsetPage[InstanceFlavor]]:
        """
        List the virtual instance flavors available to the client, across all regions.

        Args:
          project_id: Project ID.

          architectures: Filter by flavor architecture type(s).

          available: Set to true to return only the available flavors. Set to false to return only
              the flavors that are disabled in their region or out of stock there. Omit it to
              return all flavors.

          compatible_with_boot_volume_id: Return only the flavors that can boot from this volume, from its image metadata.
              An unknown volume matches no flavor. A non-bootable volume or one without image
              metadata is a 400. At most one `compatible_with_`\\** parameter per request.

          compatible_with_image_id: Return only the flavors that can boot this image: its region, OS type and CPU
              architecture. An unknown image matches no flavor. At most one
              `compatible_with_`\\** parameter per request.

          compatible_with_snapshot_id: Return only the flavors that can boot from this snapshot, resolved through its
              parent volume's image metadata. An unknown snapshot matches no flavor. A parent
              volume with no image metadata is a 400. At most one `compatible_with_`\\**
              parameter per request.

          limit: Max items to return.

          name: Operator flavor name filter, e.g. name[prefix]=g2-.

          offset: Items to skip.

          order_by: Sort field and direction.

          os_types: Filter by flavor operating system(s).

          ram_mib: Range filter on RAM size in MiB.

          region_ids: Filter by region ID(s). Omit = all regions.

          vcpus: Range filter on virtual CPU count.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            path_template("/cloud/v1/projects/{project_id}/instances/flavors", project_id=project_id),
            page=AsyncOffsetPage[InstanceFlavor],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "architectures": architectures,
                        "available": available,
                        "compatible_with_boot_volume_id": compatible_with_boot_volume_id,
                        "compatible_with_image_id": compatible_with_image_id,
                        "compatible_with_snapshot_id": compatible_with_snapshot_id,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "os_types": os_types,
                        "ram_mib": ram_mib,
                        "region_ids": region_ids,
                        "vcpus": vcpus,
                    },
                    flavor_list_params.FlavorListParams,
                ),
            ),
            model=InstanceFlavor,
        )


class FlavorsResourceWithRawResponse:
    def __init__(self, flavors: FlavorsResource) -> None:
        self._flavors = flavors

        self.list = to_raw_response_wrapper(
            flavors.list,
        )


class AsyncFlavorsResourceWithRawResponse:
    def __init__(self, flavors: AsyncFlavorsResource) -> None:
        self._flavors = flavors

        self.list = async_to_raw_response_wrapper(
            flavors.list,
        )


class FlavorsResourceWithStreamingResponse:
    def __init__(self, flavors: FlavorsResource) -> None:
        self._flavors = flavors

        self.list = to_streamed_response_wrapper(
            flavors.list,
        )


class AsyncFlavorsResourceWithStreamingResponse:
    def __init__(self, flavors: AsyncFlavorsResource) -> None:
        self._flavors = flavors

        self.list = async_to_streamed_response_wrapper(
            flavors.list,
        )

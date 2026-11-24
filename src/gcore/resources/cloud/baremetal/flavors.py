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
from ....types.cloud.baremetal import flavor_list_params
from ....types.cloud.baremetal.baremetal_flavor import BaremetalFlavor

__all__ = ["FlavorsResource", "AsyncFlavorsResource"]


class FlavorsResource(SyncAPIResource):
    """
    Bare metal flavors define the CPU, memory, disks, and network cards of a bare metal server, in all regions of the project.
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
        compatible_with_image_id: str | Omit = omit,
        cpu_threads: flavor_list_params.CPUThreads | Omit = omit,
        limit: int | Omit = omit,
        name: flavor_list_params.Name | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal[
            "cpu_threads.asc",
            "cpu_threads.desc",
            "name.asc",
            "name.desc",
            "ram_mib.asc",
            "ram_mib.desc",
            "region_id.asc",
            "region_id.desc",
        ]
        | Omit = omit,
        os_types: List[Literal["linux", "unknown", "windows"]] | Omit = omit,
        ram_mib: flavor_list_params.RamMib | Omit = omit,
        region_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[BaremetalFlavor]:
        """
        Bare metal flavors available to the client in all regions, with buildable
        capacity and port support.

        Args:
          project_id: Project ID.

          architectures: Filter by flavor architecture type(s).

          compatible_with_image_id: Return only the flavors that can boot this image: its region, OS type and CPU
              architecture, minus the flavors registered as incompatible with its OS release.
              An unknown image matches no flavor.

          cpu_threads: Range filter on CPU thread count.

          limit: Max items to return.

          name: Operator flavor name filter, e.g. name[prefix]=bm2-.

          offset: Items to skip.

          order_by: Sort field and direction.

          os_types: Filter by flavor operating system(s).

          ram_mib: Range filter on RAM size in MiB.

          region_ids: Filter by region ID(s). Omit = all regions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            path_template("/cloud/v1/projects/{project_id}/baremetal/flavors", project_id=project_id),
            page=SyncOffsetPage[BaremetalFlavor],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "architectures": architectures,
                        "compatible_with_image_id": compatible_with_image_id,
                        "cpu_threads": cpu_threads,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "os_types": os_types,
                        "ram_mib": ram_mib,
                        "region_ids": region_ids,
                    },
                    flavor_list_params.FlavorListParams,
                ),
            ),
            model=BaremetalFlavor,
        )


class AsyncFlavorsResource(AsyncAPIResource):
    """
    Bare metal flavors define the CPU, memory, disks, and network cards of a bare metal server, in all regions of the project.
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
        compatible_with_image_id: str | Omit = omit,
        cpu_threads: flavor_list_params.CPUThreads | Omit = omit,
        limit: int | Omit = omit,
        name: flavor_list_params.Name | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal[
            "cpu_threads.asc",
            "cpu_threads.desc",
            "name.asc",
            "name.desc",
            "ram_mib.asc",
            "ram_mib.desc",
            "region_id.asc",
            "region_id.desc",
        ]
        | Omit = omit,
        os_types: List[Literal["linux", "unknown", "windows"]] | Omit = omit,
        ram_mib: flavor_list_params.RamMib | Omit = omit,
        region_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BaremetalFlavor, AsyncOffsetPage[BaremetalFlavor]]:
        """
        Bare metal flavors available to the client in all regions, with buildable
        capacity and port support.

        Args:
          project_id: Project ID.

          architectures: Filter by flavor architecture type(s).

          compatible_with_image_id: Return only the flavors that can boot this image: its region, OS type and CPU
              architecture, minus the flavors registered as incompatible with its OS release.
              An unknown image matches no flavor.

          cpu_threads: Range filter on CPU thread count.

          limit: Max items to return.

          name: Operator flavor name filter, e.g. name[prefix]=bm2-.

          offset: Items to skip.

          order_by: Sort field and direction.

          os_types: Filter by flavor operating system(s).

          ram_mib: Range filter on RAM size in MiB.

          region_ids: Filter by region ID(s). Omit = all regions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            path_template("/cloud/v1/projects/{project_id}/baremetal/flavors", project_id=project_id),
            page=AsyncOffsetPage[BaremetalFlavor],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "architectures": architectures,
                        "compatible_with_image_id": compatible_with_image_id,
                        "cpu_threads": cpu_threads,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "os_types": os_types,
                        "ram_mib": ram_mib,
                        "region_ids": region_ids,
                    },
                    flavor_list_params.FlavorListParams,
                ),
            ),
            model=BaremetalFlavor,
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

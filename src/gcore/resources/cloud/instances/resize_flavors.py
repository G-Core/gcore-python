# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.cloud.instances import resize_flavor_list_params
from ....types.cloud.instances.instance_flavor import InstanceFlavor

__all__ = ["ResizeFlavorsResource", "AsyncResizeFlavorsResource"]


class ResizeFlavorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResizeFlavorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ResizeFlavorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResizeFlavorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ResizeFlavorsResourceWithStreamingResponse(self)

    def list(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["name.asc", "name.desc", "ram_mib.asc", "ram_mib.desc", "vcpus.asc", "vcpus.desc"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[InstanceFlavor]:
        """
        Returns the flavors the instance can be resized to: the flavors in its region
        that keep its flavor family and network profile, without its current flavor. An
        empty list means there is nothing to resize to. A 400 means the instance cannot
        be resized at all.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          limit: Max items to return.

          offset: Items to skip.

          order_by: Sort field and direction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get_api_list(
            path_template(
                "/cloud/v1/projects/{project_id}/instances/{instance_id}/flavors",
                project_id=project_id,
                instance_id=instance_id,
            ),
            page=SyncOffsetPage[InstanceFlavor],
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
                    },
                    resize_flavor_list_params.ResizeFlavorListParams,
                ),
            ),
            model=InstanceFlavor,
        )


class AsyncResizeFlavorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResizeFlavorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResizeFlavorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResizeFlavorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncResizeFlavorsResourceWithStreamingResponse(self)

    def list(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["name.asc", "name.desc", "ram_mib.asc", "ram_mib.desc", "vcpus.asc", "vcpus.desc"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InstanceFlavor, AsyncOffsetPage[InstanceFlavor]]:
        """
        Returns the flavors the instance can be resized to: the flavors in its region
        that keep its flavor family and network profile, without its current flavor. An
        empty list means there is nothing to resize to. A 400 means the instance cannot
        be resized at all.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          limit: Max items to return.

          offset: Items to skip.

          order_by: Sort field and direction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get_api_list(
            path_template(
                "/cloud/v1/projects/{project_id}/instances/{instance_id}/flavors",
                project_id=project_id,
                instance_id=instance_id,
            ),
            page=AsyncOffsetPage[InstanceFlavor],
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
                    },
                    resize_flavor_list_params.ResizeFlavorListParams,
                ),
            ),
            model=InstanceFlavor,
        )


class ResizeFlavorsResourceWithRawResponse:
    def __init__(self, resize_flavors: ResizeFlavorsResource) -> None:
        self._resize_flavors = resize_flavors

        self.list = to_raw_response_wrapper(
            resize_flavors.list,
        )


class AsyncResizeFlavorsResourceWithRawResponse:
    def __init__(self, resize_flavors: AsyncResizeFlavorsResource) -> None:
        self._resize_flavors = resize_flavors

        self.list = async_to_raw_response_wrapper(
            resize_flavors.list,
        )


class ResizeFlavorsResourceWithStreamingResponse:
    def __init__(self, resize_flavors: ResizeFlavorsResource) -> None:
        self._resize_flavors = resize_flavors

        self.list = to_streamed_response_wrapper(
            resize_flavors.list,
        )


class AsyncResizeFlavorsResourceWithStreamingResponse:
    def __init__(self, resize_flavors: AsyncResizeFlavorsResource) -> None:
        self._resize_flavors = resize_flavors

        self.list = async_to_streamed_response_wrapper(
            resize_flavors.list,
        )

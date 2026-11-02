# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.cloud.volumes import type_list_params
from ....types.cloud.volumes.volume_type_list import VolumeTypeList

__all__ = ["TypesResource", "AsyncTypesResource"]


class TypesResource(SyncAPIResource):
    """
    Volume types describe the operations each type supports and its QoS profile, optionally limited to one region.
    """

    @cached_property
    def with_raw_response(self) -> TypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return TypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return TypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        region_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeTypeList:
        """Returns the capabilities and the QoS profile of each volume type, sorted by
        name.

        Use the capabilities to find which operations a volume supports before you
        send a request. Set `region_id` to get the capabilities in that region. Without
        it, the capabilities ignore region limits.

        Args:
          region_id: Region ID. If you set it, the list shows only the types that the region
              supports. The capabilities then also include the limits of that region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cloud/v1/volumes/types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region_id": region_id}, type_list_params.TypeListParams),
            ),
            cast_to=VolumeTypeList,
        )


class AsyncTypesResource(AsyncAPIResource):
    """
    Volume types describe the operations each type supports and its QoS profile, optionally limited to one region.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncTypesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        region_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeTypeList:
        """Returns the capabilities and the QoS profile of each volume type, sorted by
        name.

        Use the capabilities to find which operations a volume supports before you
        send a request. Set `region_id` to get the capabilities in that region. Without
        it, the capabilities ignore region limits.

        Args:
          region_id: Region ID. If you set it, the list shows only the types that the region
              supports. The capabilities then also include the limits of that region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cloud/v1/volumes/types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"region_id": region_id}, type_list_params.TypeListParams),
            ),
            cast_to=VolumeTypeList,
        )


class TypesResourceWithRawResponse:
    def __init__(self, types: TypesResource) -> None:
        self._types = types

        self.list = to_raw_response_wrapper(
            types.list,
        )


class AsyncTypesResourceWithRawResponse:
    def __init__(self, types: AsyncTypesResource) -> None:
        self._types = types

        self.list = async_to_raw_response_wrapper(
            types.list,
        )


class TypesResourceWithStreamingResponse:
    def __init__(self, types: TypesResource) -> None:
        self._types = types

        self.list = to_streamed_response_wrapper(
            types.list,
        )


class AsyncTypesResourceWithStreamingResponse:
    def __init__(self, types: AsyncTypesResource) -> None:
        self._types = types

        self.list = async_to_streamed_response_wrapper(
            types.list,
        )

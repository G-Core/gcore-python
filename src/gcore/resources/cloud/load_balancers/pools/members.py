# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.load_balancers.pools import member_add_params

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return MembersResourceWithStreamingResponse(self)

    def add(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        address: str,
        protocol_port: int,
        admin_state_up: Optional[bool] | NotGiven = NOT_GIVEN,
        instance_id: Optional[str] | NotGiven = NOT_GIVEN,
        monitor_address: Optional[str] | NotGiven = NOT_GIVEN,
        monitor_port: Optional[int] | NotGiven = NOT_GIVEN,
        subnet_id: Optional[str] | NotGiven = NOT_GIVEN,
        weight: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer pool member

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember/post/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember/post/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member'].post.parameters[1].schema"

          pool_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember/post/parameters/2/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member'].post.parameters[2].schema"

          address: '#/components/schemas/CreateLbPoolMemberSerializer/properties/address'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.address"

          protocol_port: '#/components/schemas/CreateLbPoolMemberSerializer/properties/protocol_port'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.protocol_port"

          admin_state_up: '#/components/schemas/CreateLbPoolMemberSerializer/properties/admin_state_up/anyOf/0'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.admin_state_up.anyOf[0]"

          instance_id: '#/components/schemas/CreateLbPoolMemberSerializer/properties/instance_id/anyOf/0'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.instance_id.anyOf[0]"

          monitor_address: '#/components/schemas/CreateLbPoolMemberSerializer/properties/monitor_address/anyOf/0'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.monitor_address.anyOf[0]"

          monitor_port: '#/components/schemas/CreateLbPoolMemberSerializer/properties/monitor_port/anyOf/0'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.monitor_port.anyOf[0]"

          subnet_id: '#/components/schemas/CreateLbPoolMemberSerializer/properties/subnet_id/anyOf/0'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.subnet_id.anyOf[0]"

          weight: '#/components/schemas/CreateLbPoolMemberSerializer/properties/weight/anyOf/0'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.weight.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._post(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member",
            body=maybe_transform(
                {
                    "address": address,
                    "protocol_port": protocol_port,
                    "admin_state_up": admin_state_up,
                    "instance_id": instance_id,
                    "monitor_address": monitor_address,
                    "monitor_port": monitor_port,
                    "subnet_id": subnet_id,
                    "weight": weight,
                },
                member_add_params.MemberAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def remove(
        self,
        member_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        pool_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete load balancer pool member

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember%2F%7Bmember_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member/{member_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember%2F%7Bmember_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member/{member_id}']['delete'].parameters[1].schema"

          pool_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember%2F%7Bmember_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member/{member_id}']['delete'].parameters[2].schema"

          member_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember%2F%7Bmember_id%7D/delete/parameters/3/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member/{member_id}']['delete'].parameters[3].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._delete(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class AsyncMembersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncMembersResourceWithStreamingResponse(self)

    async def add(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        address: str,
        protocol_port: int,
        admin_state_up: Optional[bool] | NotGiven = NOT_GIVEN,
        instance_id: Optional[str] | NotGiven = NOT_GIVEN,
        monitor_address: Optional[str] | NotGiven = NOT_GIVEN,
        monitor_port: Optional[int] | NotGiven = NOT_GIVEN,
        subnet_id: Optional[str] | NotGiven = NOT_GIVEN,
        weight: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer pool member

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember/post/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember/post/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member'].post.parameters[1].schema"

          pool_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember/post/parameters/2/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member'].post.parameters[2].schema"

          address: '#/components/schemas/CreateLbPoolMemberSerializer/properties/address'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.address"

          protocol_port: '#/components/schemas/CreateLbPoolMemberSerializer/properties/protocol_port'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.protocol_port"

          admin_state_up: '#/components/schemas/CreateLbPoolMemberSerializer/properties/admin_state_up/anyOf/0'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.admin_state_up.anyOf[0]"

          instance_id: '#/components/schemas/CreateLbPoolMemberSerializer/properties/instance_id/anyOf/0'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.instance_id.anyOf[0]"

          monitor_address: '#/components/schemas/CreateLbPoolMemberSerializer/properties/monitor_address/anyOf/0'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.monitor_address.anyOf[0]"

          monitor_port: '#/components/schemas/CreateLbPoolMemberSerializer/properties/monitor_port/anyOf/0'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.monitor_port.anyOf[0]"

          subnet_id: '#/components/schemas/CreateLbPoolMemberSerializer/properties/subnet_id/anyOf/0'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.subnet_id.anyOf[0]"

          weight: '#/components/schemas/CreateLbPoolMemberSerializer/properties/weight/anyOf/0'
              "$.components.schemas.CreateLbPoolMemberSerializer.properties.weight.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._post(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "protocol_port": protocol_port,
                    "admin_state_up": admin_state_up,
                    "instance_id": instance_id,
                    "monitor_address": monitor_address,
                    "monitor_port": monitor_port,
                    "subnet_id": subnet_id,
                    "weight": weight,
                },
                member_add_params.MemberAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def remove(
        self,
        member_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        pool_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete load balancer pool member

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember%2F%7Bmember_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member/{member_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember%2F%7Bmember_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member/{member_id}']['delete'].parameters[1].schema"

          pool_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember%2F%7Bmember_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member/{member_id}']['delete'].parameters[2].schema"

          member_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember%2F%7Bmember_id%7D/delete/parameters/3/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member/{member_id}']['delete'].parameters[3].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._delete(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.add = to_raw_response_wrapper(
            members.add,
        )
        self.remove = to_raw_response_wrapper(
            members.remove,
        )


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.add = async_to_raw_response_wrapper(
            members.add,
        )
        self.remove = async_to_raw_response_wrapper(
            members.remove,
        )


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.add = to_streamed_response_wrapper(
            members.add,
        )
        self.remove = to_streamed_response_wrapper(
            members.remove,
        )


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.add = async_to_streamed_response_wrapper(
            members.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            members.remove,
        )

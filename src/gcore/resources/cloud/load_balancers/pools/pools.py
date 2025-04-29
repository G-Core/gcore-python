# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
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
from .....types.cloud import LbAlgorithm, LbPoolProtocol
from .health_monitors import (
    HealthMonitorsResource,
    AsyncHealthMonitorsResource,
    HealthMonitorsResourceWithRawResponse,
    AsyncHealthMonitorsResourceWithRawResponse,
    HealthMonitorsResourceWithStreamingResponse,
    AsyncHealthMonitorsResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.cloud.lb_algorithm import LbAlgorithm
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.load_balancers import pool_list_params, pool_create_params, pool_update_params
from .....types.cloud.detailed_lb_pool import DetailedLbPool
from .....types.cloud.lb_pool_protocol import LbPoolProtocol
from .....types.cloud.detailed_lb_pool_list import DetailedLbPoolList

__all__ = ["PoolsResource", "AsyncPoolsResource"]


class PoolsResource(SyncAPIResource):
    @cached_property
    def health_monitors(self) -> HealthMonitorsResource:
        return HealthMonitorsResource(self._client)

    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def with_raw_response(self) -> PoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return PoolsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        lb_algorithm: LbAlgorithm,
        name: str,
        protocol: LbPoolProtocol,
        ca_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        crl_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        healthmonitor: Optional[pool_create_params.Healthmonitor] | NotGiven = NOT_GIVEN,
        listener_id: Optional[str] | NotGiven = NOT_GIVEN,
        loadbalancer_id: Optional[str] | NotGiven = NOT_GIVEN,
        members: Optional[Iterable[pool_create_params.Member]] | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_persistence: Optional[pool_create_params.SessionPersistence] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer pool

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].post.parameters[1].schema"

          lb_algorithm: '#/components/schemas/CreateLbPoolSerializer/properties/lb_algorithm'
              "$.components.schemas.CreateLbPoolSerializer.properties.lb_algorithm"

          name: '#/components/schemas/CreateLbPoolSerializer/properties/name'
              "$.components.schemas.CreateLbPoolSerializer.properties.name"

          protocol: '#/components/schemas/CreateLbPoolSerializer/properties/protocol'
              "$.components.schemas.CreateLbPoolSerializer.properties.protocol"

          ca_secret_id: '#/components/schemas/CreateLbPoolSerializer/properties/ca_secret_id/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.ca_secret_id.anyOf[0]"

          crl_secret_id: '#/components/schemas/CreateLbPoolSerializer/properties/crl_secret_id/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.crl_secret_id.anyOf[0]"

          healthmonitor: '#/components/schemas/CreateLbPoolSerializer/properties/healthmonitor/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.healthmonitor.anyOf[0]"

          listener_id: '#/components/schemas/CreateLbPoolSerializer/properties/listener_id/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.listener_id.anyOf[0]"

          loadbalancer_id: '#/components/schemas/CreateLbPoolSerializer/properties/loadbalancer_id/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.loadbalancer_id.anyOf[0]"

          members: '#/components/schemas/CreateLbPoolSerializer/properties/members/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.members.anyOf[0]"

          secret_id: '#/components/schemas/CreateLbPoolSerializer/properties/secret_id/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.secret_id.anyOf[0]"

          session_persistence: '#/components/schemas/CreateLbPoolSerializer/properties/session_persistence/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.session_persistence.anyOf[0]"

          timeout_client_data: '#/components/schemas/CreateLbPoolSerializer/properties/timeout_client_data/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.timeout_client_data.anyOf[0]"

          timeout_member_connect: '#/components/schemas/CreateLbPoolSerializer/properties/timeout_member_connect/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.timeout_member_connect.anyOf[0]"

          timeout_member_data: '#/components/schemas/CreateLbPoolSerializer/properties/timeout_member_data/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.timeout_member_data.anyOf[0]"

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
            f"/cloud/v1/lbpools/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "lb_algorithm": lb_algorithm,
                    "name": name,
                    "protocol": protocol,
                    "ca_secret_id": ca_secret_id,
                    "crl_secret_id": crl_secret_id,
                    "healthmonitor": healthmonitor,
                    "listener_id": listener_id,
                    "loadbalancer_id": loadbalancer_id,
                    "members": members,
                    "secret_id": secret_id,
                    "session_persistence": session_persistence,
                    "timeout_client_data": timeout_client_data,
                    "timeout_member_connect": timeout_member_connect,
                    "timeout_member_data": timeout_member_data,
                },
                pool_create_params.PoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ca_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        crl_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        healthmonitor: Optional[pool_update_params.Healthmonitor] | NotGiven = NOT_GIVEN,
        lb_algorithm: LbAlgorithm | NotGiven = NOT_GIVEN,
        members: Optional[Iterable[pool_update_params.Member]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        protocol: LbPoolProtocol | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_persistence: Optional[pool_update_params.SessionPersistence] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Changes provided here will overwrite existing load balancer pool settings.
        Undefined fields will be kept as is. Complex objects need to be specified fully,
        they will be overwritten.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].patch.parameters[1].schema"

          pool_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].patch.parameters[2].schema"

          ca_secret_id: '#/components/schemas/PatchLbPoolSerializer/properties/ca_secret_id/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.ca_secret_id.anyOf[0]"

          crl_secret_id: '#/components/schemas/PatchLbPoolSerializer/properties/crl_secret_id/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.crl_secret_id.anyOf[0]"

          healthmonitor: '#/components/schemas/PatchLbPoolSerializer/properties/healthmonitor/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.healthmonitor.anyOf[0]"

          lb_algorithm: '#/components/schemas/PatchLbPoolSerializer/properties/lb_algorithm'
              "$.components.schemas.PatchLbPoolSerializer.properties.lb_algorithm"

          members: '#/components/schemas/PatchLbPoolSerializer/properties/members/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.members.anyOf[0]"

          name: '#/components/schemas/PatchLbPoolSerializer/properties/name'
              "$.components.schemas.PatchLbPoolSerializer.properties.name"

          protocol: '#/components/schemas/PatchLbPoolSerializer/properties/protocol'
              "$.components.schemas.PatchLbPoolSerializer.properties.protocol"

          secret_id: '#/components/schemas/PatchLbPoolSerializer/properties/secret_id/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.secret_id.anyOf[0]"

          session_persistence: '#/components/schemas/PatchLbPoolSerializer/properties/session_persistence/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.session_persistence.anyOf[0]"

          timeout_client_data: '#/components/schemas/PatchLbPoolSerializer/properties/timeout_client_data/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.timeout_client_data.anyOf[0]"

          timeout_member_connect: '#/components/schemas/PatchLbPoolSerializer/properties/timeout_member_connect/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.timeout_member_connect.anyOf[0]"

          timeout_member_data: '#/components/schemas/PatchLbPoolSerializer/properties/timeout_member_data/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.timeout_member_data.anyOf[0]"

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
        return self._patch(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}",
            body=maybe_transform(
                {
                    "ca_secret_id": ca_secret_id,
                    "crl_secret_id": crl_secret_id,
                    "healthmonitor": healthmonitor,
                    "lb_algorithm": lb_algorithm,
                    "members": members,
                    "name": name,
                    "protocol": protocol,
                    "secret_id": secret_id,
                    "session_persistence": session_persistence,
                    "timeout_client_data": timeout_client_data,
                    "timeout_member_connect": timeout_member_connect,
                    "timeout_member_data": timeout_member_data,
                },
                pool_update_params.PoolUpdateParams,
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
        details: bool | NotGiven = NOT_GIVEN,
        listener_id: str | NotGiven = NOT_GIVEN,
        loadbalancer_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailedLbPoolList:
        """
        List load balancer pools

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].get.parameters[1].schema"

          details: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].get.parameters[2]"

          listener_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].get.parameters[3]"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].get.parameters[4]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get(
            f"/cloud/v1/lbpools/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "details": details,
                        "listener_id": listener_id,
                        "loadbalancer_id": loadbalancer_id,
                    },
                    pool_list_params.PoolListParams,
                ),
            ),
            cast_to=DetailedLbPoolList,
        )

    def delete(
        self,
        pool_id: str,
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
        Delete load balancer pool

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}']['delete'].parameters[1].schema"

          pool_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}']['delete'].parameters[2].schema"

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
        return self._delete(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailedLbPool:
        """
        Get load balancer pool

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].get.parameters[1].schema"

          pool_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].get.parameters[2].schema"

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
        return self._get(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailedLbPool,
        )


class AsyncPoolsResource(AsyncAPIResource):
    @cached_property
    def health_monitors(self) -> AsyncHealthMonitorsResource:
        return AsyncHealthMonitorsResource(self._client)

    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncPoolsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        lb_algorithm: LbAlgorithm,
        name: str,
        protocol: LbPoolProtocol,
        ca_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        crl_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        healthmonitor: Optional[pool_create_params.Healthmonitor] | NotGiven = NOT_GIVEN,
        listener_id: Optional[str] | NotGiven = NOT_GIVEN,
        loadbalancer_id: Optional[str] | NotGiven = NOT_GIVEN,
        members: Optional[Iterable[pool_create_params.Member]] | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_persistence: Optional[pool_create_params.SessionPersistence] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer pool

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].post.parameters[1].schema"

          lb_algorithm: '#/components/schemas/CreateLbPoolSerializer/properties/lb_algorithm'
              "$.components.schemas.CreateLbPoolSerializer.properties.lb_algorithm"

          name: '#/components/schemas/CreateLbPoolSerializer/properties/name'
              "$.components.schemas.CreateLbPoolSerializer.properties.name"

          protocol: '#/components/schemas/CreateLbPoolSerializer/properties/protocol'
              "$.components.schemas.CreateLbPoolSerializer.properties.protocol"

          ca_secret_id: '#/components/schemas/CreateLbPoolSerializer/properties/ca_secret_id/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.ca_secret_id.anyOf[0]"

          crl_secret_id: '#/components/schemas/CreateLbPoolSerializer/properties/crl_secret_id/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.crl_secret_id.anyOf[0]"

          healthmonitor: '#/components/schemas/CreateLbPoolSerializer/properties/healthmonitor/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.healthmonitor.anyOf[0]"

          listener_id: '#/components/schemas/CreateLbPoolSerializer/properties/listener_id/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.listener_id.anyOf[0]"

          loadbalancer_id: '#/components/schemas/CreateLbPoolSerializer/properties/loadbalancer_id/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.loadbalancer_id.anyOf[0]"

          members: '#/components/schemas/CreateLbPoolSerializer/properties/members/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.members.anyOf[0]"

          secret_id: '#/components/schemas/CreateLbPoolSerializer/properties/secret_id/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.secret_id.anyOf[0]"

          session_persistence: '#/components/schemas/CreateLbPoolSerializer/properties/session_persistence/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.session_persistence.anyOf[0]"

          timeout_client_data: '#/components/schemas/CreateLbPoolSerializer/properties/timeout_client_data/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.timeout_client_data.anyOf[0]"

          timeout_member_connect: '#/components/schemas/CreateLbPoolSerializer/properties/timeout_member_connect/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.timeout_member_connect.anyOf[0]"

          timeout_member_data: '#/components/schemas/CreateLbPoolSerializer/properties/timeout_member_data/anyOf/0'
              "$.components.schemas.CreateLbPoolSerializer.properties.timeout_member_data.anyOf[0]"

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
            f"/cloud/v1/lbpools/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "lb_algorithm": lb_algorithm,
                    "name": name,
                    "protocol": protocol,
                    "ca_secret_id": ca_secret_id,
                    "crl_secret_id": crl_secret_id,
                    "healthmonitor": healthmonitor,
                    "listener_id": listener_id,
                    "loadbalancer_id": loadbalancer_id,
                    "members": members,
                    "secret_id": secret_id,
                    "session_persistence": session_persistence,
                    "timeout_client_data": timeout_client_data,
                    "timeout_member_connect": timeout_member_connect,
                    "timeout_member_data": timeout_member_data,
                },
                pool_create_params.PoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ca_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        crl_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        healthmonitor: Optional[pool_update_params.Healthmonitor] | NotGiven = NOT_GIVEN,
        lb_algorithm: LbAlgorithm | NotGiven = NOT_GIVEN,
        members: Optional[Iterable[pool_update_params.Member]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        protocol: LbPoolProtocol | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_persistence: Optional[pool_update_params.SessionPersistence] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Changes provided here will overwrite existing load balancer pool settings.
        Undefined fields will be kept as is. Complex objects need to be specified fully,
        they will be overwritten.

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].patch.parameters[1].schema"

          pool_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].patch.parameters[2].schema"

          ca_secret_id: '#/components/schemas/PatchLbPoolSerializer/properties/ca_secret_id/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.ca_secret_id.anyOf[0]"

          crl_secret_id: '#/components/schemas/PatchLbPoolSerializer/properties/crl_secret_id/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.crl_secret_id.anyOf[0]"

          healthmonitor: '#/components/schemas/PatchLbPoolSerializer/properties/healthmonitor/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.healthmonitor.anyOf[0]"

          lb_algorithm: '#/components/schemas/PatchLbPoolSerializer/properties/lb_algorithm'
              "$.components.schemas.PatchLbPoolSerializer.properties.lb_algorithm"

          members: '#/components/schemas/PatchLbPoolSerializer/properties/members/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.members.anyOf[0]"

          name: '#/components/schemas/PatchLbPoolSerializer/properties/name'
              "$.components.schemas.PatchLbPoolSerializer.properties.name"

          protocol: '#/components/schemas/PatchLbPoolSerializer/properties/protocol'
              "$.components.schemas.PatchLbPoolSerializer.properties.protocol"

          secret_id: '#/components/schemas/PatchLbPoolSerializer/properties/secret_id/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.secret_id.anyOf[0]"

          session_persistence: '#/components/schemas/PatchLbPoolSerializer/properties/session_persistence/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.session_persistence.anyOf[0]"

          timeout_client_data: '#/components/schemas/PatchLbPoolSerializer/properties/timeout_client_data/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.timeout_client_data.anyOf[0]"

          timeout_member_connect: '#/components/schemas/PatchLbPoolSerializer/properties/timeout_member_connect/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.timeout_member_connect.anyOf[0]"

          timeout_member_data: '#/components/schemas/PatchLbPoolSerializer/properties/timeout_member_data/anyOf/0'
              "$.components.schemas.PatchLbPoolSerializer.properties.timeout_member_data.anyOf[0]"

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
        return await self._patch(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}",
            body=await async_maybe_transform(
                {
                    "ca_secret_id": ca_secret_id,
                    "crl_secret_id": crl_secret_id,
                    "healthmonitor": healthmonitor,
                    "lb_algorithm": lb_algorithm,
                    "members": members,
                    "name": name,
                    "protocol": protocol,
                    "secret_id": secret_id,
                    "session_persistence": session_persistence,
                    "timeout_client_data": timeout_client_data,
                    "timeout_member_connect": timeout_member_connect,
                    "timeout_member_data": timeout_member_data,
                },
                pool_update_params.PoolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        details: bool | NotGiven = NOT_GIVEN,
        listener_id: str | NotGiven = NOT_GIVEN,
        loadbalancer_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailedLbPoolList:
        """
        List load balancer pools

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].get.parameters[1].schema"

          details: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].get.parameters[2]"

          listener_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].get.parameters[3]"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].get.parameters[4]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._get(
            f"/cloud/v1/lbpools/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "details": details,
                        "listener_id": listener_id,
                        "loadbalancer_id": loadbalancer_id,
                    },
                    pool_list_params.PoolListParams,
                ),
            ),
            cast_to=DetailedLbPoolList,
        )

    async def delete(
        self,
        pool_id: str,
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
        Delete load balancer pool

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}']['delete'].parameters[1].schema"

          pool_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}']['delete'].parameters[2].schema"

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
        return await self._delete(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailedLbPool:
        """
        Get load balancer pool

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].get.parameters[1].schema"

          pool_id: '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].get.parameters[2].schema"

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
        return await self._get(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailedLbPool,
        )


class PoolsResourceWithRawResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

        self.create = to_raw_response_wrapper(
            pools.create,
        )
        self.update = to_raw_response_wrapper(
            pools.update,
        )
        self.list = to_raw_response_wrapper(
            pools.list,
        )
        self.delete = to_raw_response_wrapper(
            pools.delete,
        )
        self.get = to_raw_response_wrapper(
            pools.get,
        )

    @cached_property
    def health_monitors(self) -> HealthMonitorsResourceWithRawResponse:
        return HealthMonitorsResourceWithRawResponse(self._pools.health_monitors)

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._pools.members)


class AsyncPoolsResourceWithRawResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

        self.create = async_to_raw_response_wrapper(
            pools.create,
        )
        self.update = async_to_raw_response_wrapper(
            pools.update,
        )
        self.list = async_to_raw_response_wrapper(
            pools.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pools.delete,
        )
        self.get = async_to_raw_response_wrapper(
            pools.get,
        )

    @cached_property
    def health_monitors(self) -> AsyncHealthMonitorsResourceWithRawResponse:
        return AsyncHealthMonitorsResourceWithRawResponse(self._pools.health_monitors)

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._pools.members)


class PoolsResourceWithStreamingResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

        self.create = to_streamed_response_wrapper(
            pools.create,
        )
        self.update = to_streamed_response_wrapper(
            pools.update,
        )
        self.list = to_streamed_response_wrapper(
            pools.list,
        )
        self.delete = to_streamed_response_wrapper(
            pools.delete,
        )
        self.get = to_streamed_response_wrapper(
            pools.get,
        )

    @cached_property
    def health_monitors(self) -> HealthMonitorsResourceWithStreamingResponse:
        return HealthMonitorsResourceWithStreamingResponse(self._pools.health_monitors)

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._pools.members)


class AsyncPoolsResourceWithStreamingResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

        self.create = async_to_streamed_response_wrapper(
            pools.create,
        )
        self.update = async_to_streamed_response_wrapper(
            pools.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pools.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pools.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            pools.get,
        )

    @cached_property
    def health_monitors(self) -> AsyncHealthMonitorsResourceWithStreamingResponse:
        return AsyncHealthMonitorsResourceWithStreamingResponse(self._pools.health_monitors)

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._pools.members)

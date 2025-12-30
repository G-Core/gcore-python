# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncOffsetPage, AsyncOffsetPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.cloud.console import Console
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.gpu_baremetal.clusters import server_list_params, server_delete_params
from .....types.cloud.gpu_baremetal.clusters.gpu_baremetal_cluster_server import GPUBaremetalClusterServer
from .....types.cloud.gpu_baremetal.clusters.gpu_baremetal_cluster_server_v1 import GPUBaremetalClusterServerV1

__all__ = ["ServersResource", "AsyncServersResource"]


class ServersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ServersResourceWithStreamingResponse(self)

    def list(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        changed_before: Union[str, datetime] | Omit = omit,
        changed_since: Union[str, datetime] | Omit = omit,
        ip_address: str | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["created_at.asc", "created_at.desc", "status.asc", "status.desc"] | Omit = omit,
        status: Literal[
            "ACTIVE",
            "BUILD",
            "ERROR",
            "HARD_REBOOT",
            "MIGRATING",
            "PAUSED",
            "REBOOT",
            "REBUILD",
            "RESIZE",
            "REVERT_RESIZE",
            "SHELVED",
            "SHELVED_OFFLOADED",
            "SHUTOFF",
            "SOFT_DELETED",
            "SUSPENDED",
            "VERIFY_RESIZE",
        ]
        | Omit = omit,
        uuids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[GPUBaremetalClusterServer]:
        """List all servers in a bare metal GPU cluster.

        Results can be filtered and
        paginated.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          changed_before: Filters the results to include only servers whose last change timestamp is less
              than the specified datetime. Format: ISO 8601.

          changed_since: Filters the results to include only servers whose last change timestamp is
              greater than or equal to the specified datetime. Format: ISO 8601.

          ip_address: Filter servers by ip address.

          limit: Limit of items on a single page

          name: Filter servers by name. You can provide a full or partial name, servers with
              matching names will be returned. For example, entering 'test' will return all
              servers that contain 'test' in their name.

          offset: Offset in results list

          order_by: Order field

          status: Filters servers by status.

          uuids: Filter servers by uuid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return self._get_api_list(
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters/{cluster_id}/servers",
            page=SyncOffsetPage[GPUBaremetalClusterServer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "changed_before": changed_before,
                        "changed_since": changed_since,
                        "ip_address": ip_address,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "status": status,
                        "uuids": uuids,
                    },
                    server_list_params.ServerListParams,
                ),
            ),
            model=GPUBaremetalClusterServer,
        )

    def delete(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        delete_floatings: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Delete a specific node from a GPU cluster.

        The node must be in a state that
        allows deletion.

        Args:
          delete_floatings: Set False if you do not want to delete assigned floating IPs. By default, it's
              True.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._delete(
            f"/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"delete_floatings": delete_floatings}, server_delete_params.ServerDeleteParams),
            ),
            cast_to=TaskIDList,
        )


    def delete_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        delete_floatings: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a bare metal GPU server from cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            cluster_id=cluster_id,
            delete_floatings=delete_floatings,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )


    def get_console(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Console:
        """
        Get bare metal GPU cluster server console URL

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/get_console",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Console,
        )

    def powercycle(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalClusterServerV1:
        """
        Stops and then starts the server, effectively performing a hard reboot.

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/powercycle",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalClusterServerV1,
        )

    def reboot(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalClusterServerV1:
        """
        Reboot one bare metal GPU cluster server

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/reboot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalClusterServerV1,
        )


class AsyncServersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncServersResourceWithStreamingResponse(self)

    def list(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        changed_before: Union[str, datetime] | Omit = omit,
        changed_since: Union[str, datetime] | Omit = omit,
        ip_address: str | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["created_at.asc", "created_at.desc", "status.asc", "status.desc"] | Omit = omit,
        status: Literal[
            "ACTIVE",
            "BUILD",
            "ERROR",
            "HARD_REBOOT",
            "MIGRATING",
            "PAUSED",
            "REBOOT",
            "REBUILD",
            "RESIZE",
            "REVERT_RESIZE",
            "SHELVED",
            "SHELVED_OFFLOADED",
            "SHUTOFF",
            "SOFT_DELETED",
            "SUSPENDED",
            "VERIFY_RESIZE",
        ]
        | Omit = omit,
        uuids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[GPUBaremetalClusterServer, AsyncOffsetPage[GPUBaremetalClusterServer]]:
        """List all servers in a bare metal GPU cluster.

        Results can be filtered and
        paginated.

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_id: Cluster unique identifier

          changed_before: Filters the results to include only servers whose last change timestamp is less
              than the specified datetime. Format: ISO 8601.

          changed_since: Filters the results to include only servers whose last change timestamp is
              greater than or equal to the specified datetime. Format: ISO 8601.

          ip_address: Filter servers by ip address.

          limit: Limit of items on a single page

          name: Filter servers by name. You can provide a full or partial name, servers with
              matching names will be returned. For example, entering 'test' will return all
              servers that contain 'test' in their name.

          offset: Offset in results list

          order_by: Order field

          status: Filters servers by status.

          uuids: Filter servers by uuid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return self._get_api_list(
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters/{cluster_id}/servers",
            page=AsyncOffsetPage[GPUBaremetalClusterServer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "changed_before": changed_before,
                        "changed_since": changed_since,
                        "ip_address": ip_address,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "status": status,
                        "uuids": uuids,
                    },
                    server_list_params.ServerListParams,
                ),
            ),
            model=GPUBaremetalClusterServer,
        )

    async def delete(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        delete_floatings: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Delete a specific node from a GPU cluster.

        The node must be in a state that
        allows deletion.

        Args:
          delete_floatings: Set False if you do not want to delete assigned floating IPs. By default, it's
              True.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._delete(
            f"/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"delete_floatings": delete_floatings}, server_delete_params.ServerDeleteParams
                ),
            ),
            cast_to=TaskIDList,
        )


    async def delete_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        delete_floatings: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a bare metal GPU server from cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            cluster_id=cluster_id,
            delete_floatings=delete_floatings,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )


    async def get_console(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Console:
        """
        Get bare metal GPU cluster server console URL

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/get_console",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Console,
        )

    async def powercycle(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalClusterServerV1:
        """
        Stops and then starts the server, effectively performing a hard reboot.

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/powercycle",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalClusterServerV1,
        )

    async def reboot(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalClusterServerV1:
        """
        Reboot one bare metal GPU cluster server

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/reboot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUBaremetalClusterServerV1,
        )


class ServersResourceWithRawResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.list = to_raw_response_wrapper(
            servers.list,
        )
        self.delete = to_raw_response_wrapper(
            servers.delete,
        )
        self.get_console = to_raw_response_wrapper(
            servers.get_console,
        )
        self.powercycle = to_raw_response_wrapper(
            servers.powercycle,
        )
        self.reboot = to_raw_response_wrapper(
            servers.reboot,
        )
        self.delete_and_poll = to_raw_response_wrapper(
            servers.delete_and_poll,
        )


class AsyncServersResourceWithRawResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.list = async_to_raw_response_wrapper(
            servers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            servers.delete,
        )
        self.get_console = async_to_raw_response_wrapper(
            servers.get_console,
        )
        self.powercycle = async_to_raw_response_wrapper(
            servers.powercycle,
        )
        self.reboot = async_to_raw_response_wrapper(
            servers.reboot,
        )
        self.delete_and_poll = async_to_raw_response_wrapper(
            servers.delete_and_poll,
        )


class ServersResourceWithStreamingResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.list = to_streamed_response_wrapper(
            servers.list,
        )
        self.delete = to_streamed_response_wrapper(
            servers.delete,
        )
        self.get_console = to_streamed_response_wrapper(
            servers.get_console,
        )
        self.powercycle = to_streamed_response_wrapper(
            servers.powercycle,
        )
        self.reboot = to_streamed_response_wrapper(
            servers.reboot,
        )
        self.delete_and_poll = to_streamed_response_wrapper(
            servers.delete_and_poll,
        )


class AsyncServersResourceWithStreamingResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.list = async_to_streamed_response_wrapper(
            servers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            servers.delete,
        )
        self.get_console = async_to_streamed_response_wrapper(
            servers.get_console,
        )
        self.powercycle = async_to_streamed_response_wrapper(
            servers.powercycle,
        )
        self.reboot = async_to_streamed_response_wrapper(
            servers.reboot,
        )
        self.delete_and_poll = async_to_streamed_response_wrapper(
            servers.delete_and_poll,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import time
from typing import List, Union, Iterable, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import is_given, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.cloud import task_list_params, task_acknowledge_all_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cloud.task import Task

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def poll(
        self,
        task_id: str,
        *,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | NotGiven = NOT_GIVEN,
    ) -> Task:
        if not is_given(polling_interval_seconds):
            polling_interval_seconds = cast(int, self._client.cloud_polling_interval_seconds)
        # Ensure the polling interval is at least 1 second
        polling_interval_seconds = max(1, polling_interval_seconds)

        if not is_given(polling_timeout_seconds):
            polling_timeout_seconds = cast(int, self._client.cloud_polling_timeout_seconds)

        if polling_timeout_seconds <= polling_interval_seconds:
            raise ValueError(
                f"`polling_timeout_seconds` must be greater than `polling_interval_seconds` ({polling_interval_seconds})"
            )

        end_time = time.time() + polling_timeout_seconds
        while time.time() <= end_time:
            task = self.get(
                task_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            if task.state == "ERROR":
                raise ValueError(task.error or f"Task {task_id} failed")
            elif task.state == "FINISHED":
                return task
            self._sleep(polling_interval_seconds)

        raise TimeoutError(f"Timed out waiting for task {task_id}")

    def list(
        self,
        *,
        from_timestamp: Union[str, datetime] | Omit = omit,
        is_acknowledged: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["asc", "desc"] | Omit = omit,
        project_id: Iterable[int] | Omit = omit,
        region_id: Iterable[int] | Omit = omit,
        sorting: Literal["asc", "desc"] | Omit = omit,
        state: List[Literal["ERROR", "FINISHED", "NEW", "RUNNING"]] | Omit = omit,
        task_type: str | Omit = omit,
        to_timestamp: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[Task]:
        """List tasks

        Args:
          from_timestamp: ISO formatted datetime string.

        Filter the tasks by creation date greater than or
              equal to `from_timestamp`

          is_acknowledged: Filter the tasks by their acknowledgement status

          limit: Limit the number of returned tasks. Falls back to default of 10 if not
              specified. Limited by max limit value of 1000

          offset: Offset value is used to exclude the first set of records from the result

          order_by: Sorting by creation date. Oldest first, or most recent first

          project_id: The project ID to filter the tasks by project. Supports multiple values of kind
              key=value1&key=value2

          region_id: The region ID to filter the tasks by region. Supports multiple values of kind
              key=value1&key=value2

          sorting: (DEPRECATED Use '`order_by`' instead) Sorting by creation date. Oldest first, or
              most recent first

          state: Filter the tasks by state. Supports multiple values of kind
              key=value1&key=value2

          task_type: Filter the tasks by their type one of ['`activate_ddos_profile`',
              '`attach_bm_to_reserved_fixed_ip`', '`attach_vm_interface`',
              '`attach_vm_to_reserved_fixed_ip`', '`attach_volume`',
              '`create_ai_cluster_gpu`', '`create_bm`', '`create_caas_container`',
              '`create_dbaas_postgres_cluster`', '`create_ddos_profile`',
              '`create_faas_function`', '`create_faas_namespace`', '`create_fip`',
              '`create_gpu_virtual_cluster`', '`create_image`',
              '`create_inference_application`', '`create_inference_instance`',
              '`create_k8s_cluster_pool_v2`', '`create_k8s_cluster_v2`', '`create_l7policy`',
              '`create_l7rule`', '`create_lblistener`', '`create_lbmember`',
              '`create_lbpool`', '`create_lbpool_health_monitor`', '`create_loadbalancer`',
              '`create_network`', '`create_reserved_fixed_ip`', '`create_router`',
              '`create_secret`', '`create_servergroup`', '`create_sfs`', '`create_snapshot`',
              '`create_subnet`', '`create_vm`', '`create_volume`',
              '`deactivate_ddos_profile`', '`delete_ai_cluster_gpu`',
              '`delete_caas_container`', '`delete_dbaas_postgres_cluster`',
              '`delete_ddos_profile`', '`delete_faas_function`', '`delete_faas_namespace`',
              '`delete_fip`', '`delete_gpu_virtual_cluster`', '`delete_gpu_virtual_server`',
              '`delete_image`', '`delete_inference_application`',
              '`delete_inference_instance`', '`delete_k8s_cluster_pool_v2`',
              '`delete_k8s_cluster_v2`', '`delete_l7policy`', '`delete_l7rule`',
              '`delete_lblistener`', '`delete_lbmember`', '`delete_lbmetadata`',
              '`delete_lbpool`', '`delete_loadbalancer`', '`delete_network`',
              '`delete_project`', '`delete_reserved_fixed_ip`', '`delete_router`',
              '`delete_secret`', '`delete_servergroup`', '`delete_sfs`', '`delete_snapshot`',
              '`delete_subnet`', '`delete_vm`', '`delete_volume`', '`detach_vm_interface`',
              '`detach_volume`', '`download_image`', '`downscale_ai_cluster_gpu`',
              '`downscale_gpu_virtual_cluster`', '`extend_sfs`', '`extend_volume`',
              '`failover_loadbalancer`', '`hard_reboot_gpu_baremetal_server`',
              '`hard_reboot_gpu_virtual_cluster`', '`hard_reboot_gpu_virtual_server`',
              '`hard_reboot_vm`', '`patch_caas_container`', '`patch_dbaas_postgres_cluster`',
              '`patch_faas_function`', '`patch_faas_namespace`', '`patch_lblistener`',
              '`patch_lbpool`', '`put_into_server_group`', '`put_l7rule`', '`rebuild_bm`',
              '`rebuild_gpu_baremetal_node`', '`remove_from_server_group`',
              '`replace_lbmetadata`', '`resize_k8s_cluster_v2`', '`resize_loadbalancer`',
              '`resize_vm`', '`resume_vm`', '`revert_volume`',
              '`soft_reboot_gpu_baremetal_server`', '`soft_reboot_gpu_virtual_cluster`',
              '`soft_reboot_gpu_virtual_server`', '`soft_reboot_vm`',
              '`start_gpu_baremetal_server`', '`start_gpu_virtual_cluster`',
              '`start_gpu_virtual_server`', '`start_vm`', '`stop_gpu_baremetal_server`',
              '`stop_gpu_virtual_cluster`', '`stop_gpu_virtual_server`', '`stop_vm`',
              '`suspend_vm`', '`sync_private_flavors`', '`update_ddos_profile`',
              '`update_inference_application`', '`update_inference_instance`',
              '`update_k8s_cluster_v2`', '`update_l7policy`', '`update_lbmetadata`',
              '`update_port_allowed_address_pairs`', '`update_sfs`',
              '`update_tags_gpu_virtual_cluster`', '`upgrade_k8s_cluster_v2`',
              '`upscale_ai_cluster_gpu`', '`upscale_gpu_virtual_cluster`']

          to_timestamp: ISO formatted datetime string. Filter the tasks by creation date less than or
              equal to `to_timestamp`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cloud/v1/tasks",
            page=SyncOffsetPage[Task],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_timestamp": from_timestamp,
                        "is_acknowledged": is_acknowledged,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "project_id": project_id,
                        "region_id": region_id,
                        "sorting": sorting,
                        "state": state,
                        "task_type": task_type,
                        "to_timestamp": to_timestamp,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            model=Task,
        )

    def acknowledge_all(
        self,
        *,
        project_id: int | Omit = omit,
        region_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Acknowledge all tasks

        Args:
          project_id: Project ID

          region_id: Region ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cloud/v1/tasks/acknowledge_all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "project_id": project_id,
                        "region_id": region_id,
                    },
                    task_acknowledge_all_params.TaskAcknowledgeAllParams,
                ),
            ),
            cast_to=NoneType,
        )

    def acknowledge_one(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Acknowledge one task

        Args:
          task_id: Task ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._post(
            f"/cloud/v1/tasks/{task_id}/acknowledge",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Task,
        )

    def get(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Get task

        Args:
          task_id: Task ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            f"/cloud/v1/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Task,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def poll(
        self,
        task_id: str,
        *,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | NotGiven = NOT_GIVEN,
    ) -> Task:
        if not is_given(polling_interval_seconds):
            polling_interval_seconds = cast(int, self._client.cloud_polling_interval_seconds)
        # Ensure the polling interval is at least 1 second
        polling_interval_seconds = max(1, polling_interval_seconds)

        if not is_given(polling_timeout_seconds):
            polling_timeout_seconds = cast(int, self._client.cloud_polling_timeout_seconds)

        if polling_timeout_seconds <= polling_interval_seconds:
            raise ValueError(
                f"`polling_timeout_seconds` must be greater than `polling_interval_seconds` ({polling_interval_seconds})"
            )

        end_time = time.time() + polling_timeout_seconds
        while time.time() <= end_time:
            task = await self.get(
                task_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            if task.state == "ERROR":
                raise ValueError(task.error or f"Task {task_id} failed")
            elif task.state == "FINISHED":
                return task
            await self._sleep(polling_interval_seconds)

        raise TimeoutError(f"Timed out waiting for task {task_id}")

    def list(
        self,
        *,
        from_timestamp: Union[str, datetime] | Omit = omit,
        is_acknowledged: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["asc", "desc"] | Omit = omit,
        project_id: Iterable[int] | Omit = omit,
        region_id: Iterable[int] | Omit = omit,
        sorting: Literal["asc", "desc"] | Omit = omit,
        state: List[Literal["ERROR", "FINISHED", "NEW", "RUNNING"]] | Omit = omit,
        task_type: str | Omit = omit,
        to_timestamp: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Task, AsyncOffsetPage[Task]]:
        """List tasks

        Args:
          from_timestamp: ISO formatted datetime string.

        Filter the tasks by creation date greater than or
              equal to `from_timestamp`

          is_acknowledged: Filter the tasks by their acknowledgement status

          limit: Limit the number of returned tasks. Falls back to default of 10 if not
              specified. Limited by max limit value of 1000

          offset: Offset value is used to exclude the first set of records from the result

          order_by: Sorting by creation date. Oldest first, or most recent first

          project_id: The project ID to filter the tasks by project. Supports multiple values of kind
              key=value1&key=value2

          region_id: The region ID to filter the tasks by region. Supports multiple values of kind
              key=value1&key=value2

          sorting: (DEPRECATED Use '`order_by`' instead) Sorting by creation date. Oldest first, or
              most recent first

          state: Filter the tasks by state. Supports multiple values of kind
              key=value1&key=value2

          task_type: Filter the tasks by their type one of ['`activate_ddos_profile`',
              '`attach_bm_to_reserved_fixed_ip`', '`attach_vm_interface`',
              '`attach_vm_to_reserved_fixed_ip`', '`attach_volume`',
              '`create_ai_cluster_gpu`', '`create_bm`', '`create_caas_container`',
              '`create_dbaas_postgres_cluster`', '`create_ddos_profile`',
              '`create_faas_function`', '`create_faas_namespace`', '`create_fip`',
              '`create_gpu_virtual_cluster`', '`create_image`',
              '`create_inference_application`', '`create_inference_instance`',
              '`create_k8s_cluster_pool_v2`', '`create_k8s_cluster_v2`', '`create_l7policy`',
              '`create_l7rule`', '`create_lblistener`', '`create_lbmember`',
              '`create_lbpool`', '`create_lbpool_health_monitor`', '`create_loadbalancer`',
              '`create_network`', '`create_reserved_fixed_ip`', '`create_router`',
              '`create_secret`', '`create_servergroup`', '`create_sfs`', '`create_snapshot`',
              '`create_subnet`', '`create_vm`', '`create_volume`',
              '`deactivate_ddos_profile`', '`delete_ai_cluster_gpu`',
              '`delete_caas_container`', '`delete_dbaas_postgres_cluster`',
              '`delete_ddos_profile`', '`delete_faas_function`', '`delete_faas_namespace`',
              '`delete_fip`', '`delete_gpu_virtual_cluster`', '`delete_gpu_virtual_server`',
              '`delete_image`', '`delete_inference_application`',
              '`delete_inference_instance`', '`delete_k8s_cluster_pool_v2`',
              '`delete_k8s_cluster_v2`', '`delete_l7policy`', '`delete_l7rule`',
              '`delete_lblistener`', '`delete_lbmember`', '`delete_lbmetadata`',
              '`delete_lbpool`', '`delete_loadbalancer`', '`delete_network`',
              '`delete_project`', '`delete_reserved_fixed_ip`', '`delete_router`',
              '`delete_secret`', '`delete_servergroup`', '`delete_sfs`', '`delete_snapshot`',
              '`delete_subnet`', '`delete_vm`', '`delete_volume`', '`detach_vm_interface`',
              '`detach_volume`', '`download_image`', '`downscale_ai_cluster_gpu`',
              '`downscale_gpu_virtual_cluster`', '`extend_sfs`', '`extend_volume`',
              '`failover_loadbalancer`', '`hard_reboot_gpu_baremetal_server`',
              '`hard_reboot_gpu_virtual_cluster`', '`hard_reboot_gpu_virtual_server`',
              '`hard_reboot_vm`', '`patch_caas_container`', '`patch_dbaas_postgres_cluster`',
              '`patch_faas_function`', '`patch_faas_namespace`', '`patch_lblistener`',
              '`patch_lbpool`', '`put_into_server_group`', '`put_l7rule`', '`rebuild_bm`',
              '`rebuild_gpu_baremetal_node`', '`remove_from_server_group`',
              '`replace_lbmetadata`', '`resize_k8s_cluster_v2`', '`resize_loadbalancer`',
              '`resize_vm`', '`resume_vm`', '`revert_volume`',
              '`soft_reboot_gpu_baremetal_server`', '`soft_reboot_gpu_virtual_cluster`',
              '`soft_reboot_gpu_virtual_server`', '`soft_reboot_vm`',
              '`start_gpu_baremetal_server`', '`start_gpu_virtual_cluster`',
              '`start_gpu_virtual_server`', '`start_vm`', '`stop_gpu_baremetal_server`',
              '`stop_gpu_virtual_cluster`', '`stop_gpu_virtual_server`', '`stop_vm`',
              '`suspend_vm`', '`sync_private_flavors`', '`update_ddos_profile`',
              '`update_inference_application`', '`update_inference_instance`',
              '`update_k8s_cluster_v2`', '`update_l7policy`', '`update_lbmetadata`',
              '`update_port_allowed_address_pairs`', '`update_sfs`',
              '`update_tags_gpu_virtual_cluster`', '`upgrade_k8s_cluster_v2`',
              '`upscale_ai_cluster_gpu`', '`upscale_gpu_virtual_cluster`']

          to_timestamp: ISO formatted datetime string. Filter the tasks by creation date less than or
              equal to `to_timestamp`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cloud/v1/tasks",
            page=AsyncOffsetPage[Task],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_timestamp": from_timestamp,
                        "is_acknowledged": is_acknowledged,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "project_id": project_id,
                        "region_id": region_id,
                        "sorting": sorting,
                        "state": state,
                        "task_type": task_type,
                        "to_timestamp": to_timestamp,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            model=Task,
        )

    async def acknowledge_all(
        self,
        *,
        project_id: int | Omit = omit,
        region_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Acknowledge all tasks

        Args:
          project_id: Project ID

          region_id: Region ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cloud/v1/tasks/acknowledge_all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "project_id": project_id,
                        "region_id": region_id,
                    },
                    task_acknowledge_all_params.TaskAcknowledgeAllParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def acknowledge_one(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Acknowledge one task

        Args:
          task_id: Task ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._post(
            f"/cloud/v1/tasks/{task_id}/acknowledge",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Task,
        )

    async def get(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Get task

        Args:
          task_id: Task ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            f"/cloud/v1/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Task,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.list = to_raw_response_wrapper(
            tasks.list,
        )
        self.acknowledge_all = to_raw_response_wrapper(
            tasks.acknowledge_all,
        )
        self.acknowledge_one = to_raw_response_wrapper(
            tasks.acknowledge_one,
        )
        self.get = to_raw_response_wrapper(
            tasks.get,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.list = async_to_raw_response_wrapper(
            tasks.list,
        )
        self.acknowledge_all = async_to_raw_response_wrapper(
            tasks.acknowledge_all,
        )
        self.acknowledge_one = async_to_raw_response_wrapper(
            tasks.acknowledge_one,
        )
        self.get = async_to_raw_response_wrapper(
            tasks.get,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.list = to_streamed_response_wrapper(
            tasks.list,
        )
        self.acknowledge_all = to_streamed_response_wrapper(
            tasks.acknowledge_all,
        )
        self.acknowledge_one = to_streamed_response_wrapper(
            tasks.acknowledge_one,
        )
        self.get = to_streamed_response_wrapper(
            tasks.get,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.acknowledge_all = async_to_streamed_response_wrapper(
            tasks.acknowledge_all,
        )
        self.acknowledge_one = async_to_streamed_response_wrapper(
            tasks.acknowledge_one,
        )
        self.get = async_to_streamed_response_wrapper(
            tasks.get,
        )

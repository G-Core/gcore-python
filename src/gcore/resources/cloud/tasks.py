# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
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

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        from_timestamp: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        is_acknowledged: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        project_id: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        region_id: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        sorting: Optional[Literal["asc", "desc"]] | NotGiven = NOT_GIVEN,
        state: Optional[List[Literal["ERROR", "FINISHED", "NEW", "RUNNING"]]] | NotGiven = NOT_GIVEN,
        task_type: Optional[str] | NotGiven = NOT_GIVEN,
        to_timestamp: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[Task]:
        """
        List tasks

        Args:
          from_timestamp: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/0/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[0].schema.anyOf[0]"

          is_acknowledged: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/1/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[1].schema.anyOf[0]"

          limit: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/2'
              "$.paths['/cloud/v1/tasks'].get.parameters[2]"

          offset: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/3'
              "$.paths['/cloud/v1/tasks'].get.parameters[3]"

          project_id: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/4/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[4].schema.anyOf[0]"

          region_id: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/5/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[5].schema.anyOf[0]"

          sorting: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/6/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[6].schema.anyOf[0]"

          state: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/7/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[7].schema.anyOf[0]"

          task_type: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/8/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[8].schema.anyOf[0]"

          to_timestamp: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/9/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[9].schema.anyOf[0]"

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
        project_id: Optional[int] | NotGiven = NOT_GIVEN,
        region_id: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Acknowledge all client tasks in project or region

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Ftasks%2Facknowledge_all/post/parameters/0/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks/acknowledge_all'].post.parameters[0].schema.anyOf[0]"

          region_id: '#/paths/%2Fcloud%2Fv1%2Ftasks%2Facknowledge_all/post/parameters/1/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks/acknowledge_all'].post.parameters[1].schema.anyOf[0]"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Task:
        """
        Acknowledge one task on project scope

        Args:
          task_id: '#/paths/%2Fcloud%2Fv1%2Ftasks%2F%7Btask_id%7D%2Facknowledge/post/parameters/0/schema'
              "$.paths['/cloud/v1/tasks/{task_id}/acknowledge'].post.parameters[0].schema"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Task:
        """
        Get task

        Args:
          task_id: '#/paths/%2Fcloud%2Fv1%2Ftasks%2F%7Btask_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/tasks/{task_id}'].get.parameters[0].schema"

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

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        from_timestamp: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        is_acknowledged: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        project_id: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        region_id: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        sorting: Optional[Literal["asc", "desc"]] | NotGiven = NOT_GIVEN,
        state: Optional[List[Literal["ERROR", "FINISHED", "NEW", "RUNNING"]]] | NotGiven = NOT_GIVEN,
        task_type: Optional[str] | NotGiven = NOT_GIVEN,
        to_timestamp: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Task, AsyncOffsetPage[Task]]:
        """
        List tasks

        Args:
          from_timestamp: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/0/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[0].schema.anyOf[0]"

          is_acknowledged: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/1/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[1].schema.anyOf[0]"

          limit: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/2'
              "$.paths['/cloud/v1/tasks'].get.parameters[2]"

          offset: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/3'
              "$.paths['/cloud/v1/tasks'].get.parameters[3]"

          project_id: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/4/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[4].schema.anyOf[0]"

          region_id: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/5/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[5].schema.anyOf[0]"

          sorting: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/6/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[6].schema.anyOf[0]"

          state: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/7/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[7].schema.anyOf[0]"

          task_type: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/8/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[8].schema.anyOf[0]"

          to_timestamp: '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/9/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks'].get.parameters[9].schema.anyOf[0]"

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
        project_id: Optional[int] | NotGiven = NOT_GIVEN,
        region_id: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Acknowledge all client tasks in project or region

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Ftasks%2Facknowledge_all/post/parameters/0/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks/acknowledge_all'].post.parameters[0].schema.anyOf[0]"

          region_id: '#/paths/%2Fcloud%2Fv1%2Ftasks%2Facknowledge_all/post/parameters/1/schema/anyOf/0'
              "$.paths['/cloud/v1/tasks/acknowledge_all'].post.parameters[1].schema.anyOf[0]"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Task:
        """
        Acknowledge one task on project scope

        Args:
          task_id: '#/paths/%2Fcloud%2Fv1%2Ftasks%2F%7Btask_id%7D%2Facknowledge/post/parameters/0/schema'
              "$.paths['/cloud/v1/tasks/{task_id}/acknowledge'].post.parameters[0].schema"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Task:
        """
        Get task

        Args:
          task_id: '#/paths/%2Fcloud%2Fv1%2Ftasks%2F%7Btask_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/tasks/{task_id}'].get.parameters[0].schema"

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

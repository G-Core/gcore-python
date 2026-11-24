# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloud.console import Console
from ....types.cloud.instances import console_get_params

__all__ = ["ConsoleResource", "AsyncConsoleResource"]


class ConsoleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConsoleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ConsoleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsoleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ConsoleResourceWithStreamingResponse(self)

    def get(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        console_type: Literal["novnc", "spice"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Console:
        """Returns a URL that gives access to the remote console of an instance.

        The API
        finds the region of the instance from its ID.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          console_type: Console type that you expect. If you omit it, you get the first available type
              in this order: `novnc`, `spice`.

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
                "/cloud/v1/projects/{project_id}/instances/{instance_id}/console",
                project_id=project_id,
                instance_id=instance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"console_type": console_type}, console_get_params.ConsoleGetParams),
            ),
            cast_to=Console,
        )


class AsyncConsoleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConsoleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConsoleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsoleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncConsoleResourceWithStreamingResponse(self)

    async def get(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        console_type: Literal["novnc", "spice"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Console:
        """Returns a URL that gives access to the remote console of an instance.

        The API
        finds the region of the instance from its ID.

        Args:
          project_id: Project ID.

          instance_id: Instance ID.

          console_type: Console type that you expect. If you omit it, you get the first available type
              in this order: `novnc`, `spice`.

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
                "/cloud/v1/projects/{project_id}/instances/{instance_id}/console",
                project_id=project_id,
                instance_id=instance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"console_type": console_type}, console_get_params.ConsoleGetParams),
            ),
            cast_to=Console,
        )


class ConsoleResourceWithRawResponse:
    def __init__(self, console: ConsoleResource) -> None:
        self._console = console

        self.get = to_raw_response_wrapper(
            console.get,
        )


class AsyncConsoleResourceWithRawResponse:
    def __init__(self, console: AsyncConsoleResource) -> None:
        self._console = console

        self.get = async_to_raw_response_wrapper(
            console.get,
        )


class ConsoleResourceWithStreamingResponse:
    def __init__(self, console: ConsoleResource) -> None:
        self._console = console

        self.get = to_streamed_response_wrapper(
            console.get,
        )


class AsyncConsoleResourceWithStreamingResponse:
    def __init__(self, console: AsyncConsoleResource) -> None:
        self._console = console

        self.get = async_to_streamed_response_wrapper(
            console.get,
        )

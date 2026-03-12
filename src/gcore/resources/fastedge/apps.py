# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPageFastedgeApps, AsyncOffsetPageFastedgeApps
from ..._base_client import AsyncPaginator, make_request_options
from ...types.fastedge import app_list_params, app_create_params
from ...types.fastedge.app_short import AppShort

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    """
    FastEdge applications combine a WebAssembly binary with configuration, environment variables, and secrets for deployment at the CDN edge.
    """

    @cached_property
    def with_raw_response(self) -> AppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AppsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        binary: int | Omit = omit,
        comment: str | Omit = omit,
        debug: bool | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        log: Optional[Literal["kafka", "none"]] | Omit = omit,
        name: str | Omit = omit,
        rsp_headers: Dict[str, str] | Omit = omit,
        secrets: Dict[str, app_create_params.Secrets] | Omit = omit,
        status: int | Omit = omit,
        stores: Dict[str, app_create_params.Stores] | Omit = omit,
        template: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppShort:
        """Create a new edge application from a WebAssembly binary.

        The app is configured
        with execution limits, environment variables, and network assignments. Apps
        start in draft status (0) and must be explicitly enabled to receive traffic.

        Args:
          binary: ID of the WebAssembly binary to deploy

          comment: Optional human-readable description of the application's purpose

          debug: Enable verbose debug logging for 30 minutes. Automatically expires to prevent
              performance impact.

          env: Environment variables

          log: Logging channel. Use 'kafka' to enable log collection (queryable via API), or
              'none' to disable logging.

          name: Unique application name (alphanumeric, hyphens allowed)

          rsp_headers: Extra headers to add to the response

          secrets: Application secrets

          status:
              Status code:
              0 - draft (inactive)
              1 - enabled
              2 - disabled
              5 - suspended

          stores: Application edge stores

          template: Template ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fastedge/v1/apps",
            body=maybe_transform(
                {
                    "binary": binary,
                    "comment": comment,
                    "debug": debug,
                    "env": env,
                    "log": log,
                    "name": name,
                    "rsp_headers": rsp_headers,
                    "secrets": secrets,
                    "status": status,
                    "stores": stores,
                    "template": template,
                },
                app_create_params.AppCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppShort,
        )

    def list(
        self,
        *,
        api_type: Literal["wasi-http", "proxy-wasm"] | Omit = omit,
        binary: int | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal[
            "name",
            "-name",
            "status",
            "-status",
            "id",
            "-id",
            "template",
            "-template",
            "binary",
            "-binary",
            "plan",
            "-plan",
        ]
        | Omit = omit,
        plan: int | Omit = omit,
        status: int | Omit = omit,
        template: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPageFastedgeApps[AppShort]:
        """
        Retrieve a paginated list of applications owned by the authenticated client.
        Results can be filtered by name, API type, status, template, binary, or plan,
        and sorted by various fields.

        Args:
          api_type:
              API type:
              wasi-http - WASI with HTTP entry point
              proxy-wasm - Proxy-Wasm app, callable from CDN

          binary: Filter by binary ID (shows apps using this binary)

          limit: Maximum number of results to return

          name: Filter by application name (case-insensitive partial match)

          offset: Number of results to skip for pagination

          ordering: Sort order. Use - prefix for descending (e.g., -name sorts by name descending)

          plan: Filter by plan ID

          status:
              Status code:
              0 - draft (inactive)
              1 - enabled
              2 - disabled
              3 - hourly call limit exceeded
              4 - daily call limit exceeded
              5 - suspended

          template: Filter by template ID (shows apps created from this template)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/fastedge/v1/apps",
            page=SyncOffsetPageFastedgeApps[AppShort],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "api_type": api_type,
                        "binary": binary,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                        "plan": plan,
                        "status": status,
                        "template": template,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            model=AppShort,
        )


class AsyncAppsResource(AsyncAPIResource):
    """
    FastEdge applications combine a WebAssembly binary with configuration, environment variables, and secrets for deployment at the CDN edge.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAppsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        binary: int | Omit = omit,
        comment: str | Omit = omit,
        debug: bool | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        log: Optional[Literal["kafka", "none"]] | Omit = omit,
        name: str | Omit = omit,
        rsp_headers: Dict[str, str] | Omit = omit,
        secrets: Dict[str, app_create_params.Secrets] | Omit = omit,
        status: int | Omit = omit,
        stores: Dict[str, app_create_params.Stores] | Omit = omit,
        template: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppShort:
        """Create a new edge application from a WebAssembly binary.

        The app is configured
        with execution limits, environment variables, and network assignments. Apps
        start in draft status (0) and must be explicitly enabled to receive traffic.

        Args:
          binary: ID of the WebAssembly binary to deploy

          comment: Optional human-readable description of the application's purpose

          debug: Enable verbose debug logging for 30 minutes. Automatically expires to prevent
              performance impact.

          env: Environment variables

          log: Logging channel. Use 'kafka' to enable log collection (queryable via API), or
              'none' to disable logging.

          name: Unique application name (alphanumeric, hyphens allowed)

          rsp_headers: Extra headers to add to the response

          secrets: Application secrets

          status:
              Status code:
              0 - draft (inactive)
              1 - enabled
              2 - disabled
              5 - suspended

          stores: Application edge stores

          template: Template ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fastedge/v1/apps",
            body=await async_maybe_transform(
                {
                    "binary": binary,
                    "comment": comment,
                    "debug": debug,
                    "env": env,
                    "log": log,
                    "name": name,
                    "rsp_headers": rsp_headers,
                    "secrets": secrets,
                    "status": status,
                    "stores": stores,
                    "template": template,
                },
                app_create_params.AppCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppShort,
        )

    def list(
        self,
        *,
        api_type: Literal["wasi-http", "proxy-wasm"] | Omit = omit,
        binary: int | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal[
            "name",
            "-name",
            "status",
            "-status",
            "id",
            "-id",
            "template",
            "-template",
            "binary",
            "-binary",
            "plan",
            "-plan",
        ]
        | Omit = omit,
        plan: int | Omit = omit,
        status: int | Omit = omit,
        template: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AppShort, AsyncOffsetPageFastedgeApps[AppShort]]:
        """
        Retrieve a paginated list of applications owned by the authenticated client.
        Results can be filtered by name, API type, status, template, binary, or plan,
        and sorted by various fields.

        Args:
          api_type:
              API type:
              wasi-http - WASI with HTTP entry point
              proxy-wasm - Proxy-Wasm app, callable from CDN

          binary: Filter by binary ID (shows apps using this binary)

          limit: Maximum number of results to return

          name: Filter by application name (case-insensitive partial match)

          offset: Number of results to skip for pagination

          ordering: Sort order. Use - prefix for descending (e.g., -name sorts by name descending)

          plan: Filter by plan ID

          status:
              Status code:
              0 - draft (inactive)
              1 - enabled
              2 - disabled
              3 - hourly call limit exceeded
              4 - daily call limit exceeded
              5 - suspended

          template: Filter by template ID (shows apps created from this template)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/fastedge/v1/apps",
            page=AsyncOffsetPageFastedgeApps[AppShort],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "api_type": api_type,
                        "binary": binary,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                        "plan": plan,
                        "status": status,
                        "template": template,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            model=AppShort,
        )


class AppsResourceWithRawResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.create = to_raw_response_wrapper(
            apps.create,
        )
        self.list = to_raw_response_wrapper(
            apps.list,
        )


class AsyncAppsResourceWithRawResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.create = async_to_raw_response_wrapper(
            apps.create,
        )
        self.list = async_to_raw_response_wrapper(
            apps.list,
        )


class AppsResourceWithStreamingResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.create = to_streamed_response_wrapper(
            apps.create,
        )
        self.list = to_streamed_response_wrapper(
            apps.list,
        )


class AsyncAppsResourceWithStreamingResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.create = async_to_streamed_response_wrapper(
            apps.create,
        )
        self.list = async_to_streamed_response_wrapper(
            apps.list,
        )

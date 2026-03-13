# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPageFastedgeApps, AsyncOffsetPageFastedgeApps
from ...._base_client import AsyncPaginator, make_request_options
from ....types.fastedge import app_list_params, app_create_params, app_update_params, app_replace_params
from ....types.fastedge.app import App
from ....types.fastedge.app_short import AppShort

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    """
    FastEdge applications combine a WebAssembly binary with configuration, environment variables, and secrets for deployment at the CDN edge.
    """

    @cached_property
    def logs(self) -> LogsResource:
        """
        Apps are descriptions of edge apps, that reference the binary and may contain app-specific settings, such as environment variables.
        """
        return LogsResource(self._client)

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

    def update(
        self,
        app_id: int,
        *,
        binary: int | Omit = omit,
        comment: str | Omit = omit,
        debug: bool | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        log: Optional[Literal["kafka", "none"]] | Omit = omit,
        name: str | Omit = omit,
        rsp_headers: Dict[str, str] | Omit = omit,
        secrets: Dict[str, app_update_params.Secrets] | Omit = omit,
        status: int | Omit = omit,
        stores: Dict[str, app_update_params.Stores] | Omit = omit,
        template: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppShort:
        """Partially update an application's configuration.

        Only the fields provided in the
        request body will be modified; others remain unchanged.

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
        return self._patch(
            f"/fastedge/v1/apps/{app_id}",
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
                app_update_params.AppUpdateParams,
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

    def delete(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Permanently delete an application and remove it from all edge networks.

        This
        action cannot be undone. The associated binary is not deleted and can be reused.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/fastedge/v1/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> App:
        """
        Retrieve complete configuration and metadata for a specific application.
        Includes binary reference, plan limits, environment variables, and current
        status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/fastedge/v1/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=App,
        )

    def replace(
        self,
        app_id: int,
        *,
        body: app_replace_params.Body | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppShort:
        """Replace the complete configuration of an existing application.

        All fields must
        be provided - use PATCH for partial updates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/fastedge/v1/apps/{app_id}",
            body=maybe_transform(body, app_replace_params.AppReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppShort,
        )


class AsyncAppsResource(AsyncAPIResource):
    """
    FastEdge applications combine a WebAssembly binary with configuration, environment variables, and secrets for deployment at the CDN edge.
    """

    @cached_property
    def logs(self) -> AsyncLogsResource:
        """
        Apps are descriptions of edge apps, that reference the binary and may contain app-specific settings, such as environment variables.
        """
        return AsyncLogsResource(self._client)

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

    async def update(
        self,
        app_id: int,
        *,
        binary: int | Omit = omit,
        comment: str | Omit = omit,
        debug: bool | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        log: Optional[Literal["kafka", "none"]] | Omit = omit,
        name: str | Omit = omit,
        rsp_headers: Dict[str, str] | Omit = omit,
        secrets: Dict[str, app_update_params.Secrets] | Omit = omit,
        status: int | Omit = omit,
        stores: Dict[str, app_update_params.Stores] | Omit = omit,
        template: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppShort:
        """Partially update an application's configuration.

        Only the fields provided in the
        request body will be modified; others remain unchanged.

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
        return await self._patch(
            f"/fastedge/v1/apps/{app_id}",
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
                app_update_params.AppUpdateParams,
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

    async def delete(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Permanently delete an application and remove it from all edge networks.

        This
        action cannot be undone. The associated binary is not deleted and can be reused.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/fastedge/v1/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> App:
        """
        Retrieve complete configuration and metadata for a specific application.
        Includes binary reference, plan limits, environment variables, and current
        status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/fastedge/v1/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=App,
        )

    async def replace(
        self,
        app_id: int,
        *,
        body: app_replace_params.Body | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppShort:
        """Replace the complete configuration of an existing application.

        All fields must
        be provided - use PATCH for partial updates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/fastedge/v1/apps/{app_id}",
            body=await async_maybe_transform(body, app_replace_params.AppReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppShort,
        )


class AppsResourceWithRawResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.create = to_raw_response_wrapper(
            apps.create,
        )
        self.update = to_raw_response_wrapper(
            apps.update,
        )
        self.list = to_raw_response_wrapper(
            apps.list,
        )
        self.delete = to_raw_response_wrapper(
            apps.delete,
        )
        self.get = to_raw_response_wrapper(
            apps.get,
        )
        self.replace = to_raw_response_wrapper(
            apps.replace,
        )

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        """
        Apps are descriptions of edge apps, that reference the binary and may contain app-specific settings, such as environment variables.
        """
        return LogsResourceWithRawResponse(self._apps.logs)


class AsyncAppsResourceWithRawResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.create = async_to_raw_response_wrapper(
            apps.create,
        )
        self.update = async_to_raw_response_wrapper(
            apps.update,
        )
        self.list = async_to_raw_response_wrapper(
            apps.list,
        )
        self.delete = async_to_raw_response_wrapper(
            apps.delete,
        )
        self.get = async_to_raw_response_wrapper(
            apps.get,
        )
        self.replace = async_to_raw_response_wrapper(
            apps.replace,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        """
        Apps are descriptions of edge apps, that reference the binary and may contain app-specific settings, such as environment variables.
        """
        return AsyncLogsResourceWithRawResponse(self._apps.logs)


class AppsResourceWithStreamingResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.create = to_streamed_response_wrapper(
            apps.create,
        )
        self.update = to_streamed_response_wrapper(
            apps.update,
        )
        self.list = to_streamed_response_wrapper(
            apps.list,
        )
        self.delete = to_streamed_response_wrapper(
            apps.delete,
        )
        self.get = to_streamed_response_wrapper(
            apps.get,
        )
        self.replace = to_streamed_response_wrapper(
            apps.replace,
        )

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        """
        Apps are descriptions of edge apps, that reference the binary and may contain app-specific settings, such as environment variables.
        """
        return LogsResourceWithStreamingResponse(self._apps.logs)


class AsyncAppsResourceWithStreamingResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.create = async_to_streamed_response_wrapper(
            apps.create,
        )
        self.update = async_to_streamed_response_wrapper(
            apps.update,
        )
        self.list = async_to_streamed_response_wrapper(
            apps.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            apps.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            apps.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            apps.replace,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        Apps are descriptions of edge apps, that reference the binary and may contain app-specific settings, such as environment variables.
        """
        return AsyncLogsResourceWithStreamingResponse(self._apps.logs)

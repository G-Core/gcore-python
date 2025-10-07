# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

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
from ...._base_client import make_request_options
from ....types.cdn.logs_uploader import (
    config_list_params,
    config_create_params,
    config_update_params,
    config_replace_params,
)
from ....types.cdn.logs_uploader_validation import LogsUploaderValidation
from ....types.cdn.logs_uploader.logs_uploader_config import LogsUploaderConfig
from ....types.cdn.logs_uploader.logs_uploader_config_list import LogsUploaderConfigList

__all__ = ["ConfigsResource", "AsyncConfigsResource"]


class ConfigsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ConfigsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        policy: int,
        target: int,
        enabled: bool | Omit = omit,
        for_all_resources: bool | Omit = omit,
        resources: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderConfig:
        """
        Create logs uploader config.

        Args:
          name: Name of the config.

          policy: ID of the policy that should be assigned to given config.

          target: ID of the target to which logs should be uploaded.

          enabled: Enables or disables the config.

          for_all_resources: If set to true, the config will be applied to all CDN resources. If set to
              false, the config will be applied to the resources specified in the `resources`
              field.

          resources: List of resource IDs to which the config should be applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cdn/logs_uploader/configs",
            body=maybe_transform(
                {
                    "name": name,
                    "policy": policy,
                    "target": target,
                    "enabled": enabled,
                    "for_all_resources": for_all_resources,
                    "resources": resources,
                },
                config_create_params.ConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderConfig,
        )

    def update(
        self,
        id: int,
        *,
        enabled: bool | Omit = omit,
        for_all_resources: bool | Omit = omit,
        name: str | Omit = omit,
        policy: int | Omit = omit,
        resources: Iterable[int] | Omit = omit,
        target: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderConfig:
        """
        Change logs uploader config partially.

        Args:
          enabled: Enables or disables the config.

          for_all_resources: If set to true, the config will be applied to all CDN resources. If set to
              false, the config will be applied to the resources specified in the `resources`
              field.

          name: Name of the config.

          policy: ID of the policy that should be assigned to given config.

          resources: List of resource IDs to which the config should be applied.

          target: ID of the target to which logs should be uploaded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/cdn/logs_uploader/configs/{id}",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "for_all_resources": for_all_resources,
                    "name": name,
                    "policy": policy,
                    "resources": resources,
                    "target": target,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderConfig,
        )

    def list(
        self,
        *,
        resource_ids: Iterable[int] | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderConfigList:
        """
        Get list of logs uploader configs.

        Args:
          resource_ids: Filter by ids of CDN resources that are assigned to given config.

          search: Search by config name or id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cdn/logs_uploader/configs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resource_ids": resource_ids,
                        "search": search,
                    },
                    config_list_params.ConfigListParams,
                ),
            ),
            cast_to=LogsUploaderConfigList,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the logs uploader config from the system permanently.

        Notes:

        - **Irreversibility**: This action is irreversible. Once deleted, the logs
          uploader config cannot be recovered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cdn/logs_uploader/configs/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderConfig:
        """
        Get information about logs uploader config.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cdn/logs_uploader/configs/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderConfig,
        )

    def replace(
        self,
        id: int,
        *,
        name: str,
        policy: int,
        target: int,
        enabled: bool | Omit = omit,
        for_all_resources: bool | Omit = omit,
        resources: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderConfig:
        """
        Change logs uploader config.

        Args:
          name: Name of the config.

          policy: ID of the policy that should be assigned to given config.

          target: ID of the target to which logs should be uploaded.

          enabled: Enables or disables the config.

          for_all_resources: If set to true, the config will be applied to all CDN resources. If set to
              false, the config will be applied to the resources specified in the `resources`
              field.

          resources: List of resource IDs to which the config should be applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/cdn/logs_uploader/configs/{id}",
            body=maybe_transform(
                {
                    "name": name,
                    "policy": policy,
                    "target": target,
                    "enabled": enabled,
                    "for_all_resources": for_all_resources,
                    "resources": resources,
                },
                config_replace_params.ConfigReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderConfig,
        )

    def validate(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderValidation:
        """
        Validate logs uploader config.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/cdn/logs_uploader/configs/{id}/validate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderValidation,
        )


class AsyncConfigsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncConfigsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        policy: int,
        target: int,
        enabled: bool | Omit = omit,
        for_all_resources: bool | Omit = omit,
        resources: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderConfig:
        """
        Create logs uploader config.

        Args:
          name: Name of the config.

          policy: ID of the policy that should be assigned to given config.

          target: ID of the target to which logs should be uploaded.

          enabled: Enables or disables the config.

          for_all_resources: If set to true, the config will be applied to all CDN resources. If set to
              false, the config will be applied to the resources specified in the `resources`
              field.

          resources: List of resource IDs to which the config should be applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cdn/logs_uploader/configs",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "policy": policy,
                    "target": target,
                    "enabled": enabled,
                    "for_all_resources": for_all_resources,
                    "resources": resources,
                },
                config_create_params.ConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderConfig,
        )

    async def update(
        self,
        id: int,
        *,
        enabled: bool | Omit = omit,
        for_all_resources: bool | Omit = omit,
        name: str | Omit = omit,
        policy: int | Omit = omit,
        resources: Iterable[int] | Omit = omit,
        target: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderConfig:
        """
        Change logs uploader config partially.

        Args:
          enabled: Enables or disables the config.

          for_all_resources: If set to true, the config will be applied to all CDN resources. If set to
              false, the config will be applied to the resources specified in the `resources`
              field.

          name: Name of the config.

          policy: ID of the policy that should be assigned to given config.

          resources: List of resource IDs to which the config should be applied.

          target: ID of the target to which logs should be uploaded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/cdn/logs_uploader/configs/{id}",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "for_all_resources": for_all_resources,
                    "name": name,
                    "policy": policy,
                    "resources": resources,
                    "target": target,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderConfig,
        )

    async def list(
        self,
        *,
        resource_ids: Iterable[int] | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderConfigList:
        """
        Get list of logs uploader configs.

        Args:
          resource_ids: Filter by ids of CDN resources that are assigned to given config.

          search: Search by config name or id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cdn/logs_uploader/configs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "resource_ids": resource_ids,
                        "search": search,
                    },
                    config_list_params.ConfigListParams,
                ),
            ),
            cast_to=LogsUploaderConfigList,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the logs uploader config from the system permanently.

        Notes:

        - **Irreversibility**: This action is irreversible. Once deleted, the logs
          uploader config cannot be recovered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cdn/logs_uploader/configs/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderConfig:
        """
        Get information about logs uploader config.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cdn/logs_uploader/configs/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderConfig,
        )

    async def replace(
        self,
        id: int,
        *,
        name: str,
        policy: int,
        target: int,
        enabled: bool | Omit = omit,
        for_all_resources: bool | Omit = omit,
        resources: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderConfig:
        """
        Change logs uploader config.

        Args:
          name: Name of the config.

          policy: ID of the policy that should be assigned to given config.

          target: ID of the target to which logs should be uploaded.

          enabled: Enables or disables the config.

          for_all_resources: If set to true, the config will be applied to all CDN resources. If set to
              false, the config will be applied to the resources specified in the `resources`
              field.

          resources: List of resource IDs to which the config should be applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/cdn/logs_uploader/configs/{id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "policy": policy,
                    "target": target,
                    "enabled": enabled,
                    "for_all_resources": for_all_resources,
                    "resources": resources,
                },
                config_replace_params.ConfigReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderConfig,
        )

    async def validate(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderValidation:
        """
        Validate logs uploader config.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/cdn/logs_uploader/configs/{id}/validate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderValidation,
        )


class ConfigsResourceWithRawResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

        self.create = to_raw_response_wrapper(
            configs.create,
        )
        self.update = to_raw_response_wrapper(
            configs.update,
        )
        self.list = to_raw_response_wrapper(
            configs.list,
        )
        self.delete = to_raw_response_wrapper(
            configs.delete,
        )
        self.get = to_raw_response_wrapper(
            configs.get,
        )
        self.replace = to_raw_response_wrapper(
            configs.replace,
        )
        self.validate = to_raw_response_wrapper(
            configs.validate,
        )


class AsyncConfigsResourceWithRawResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

        self.create = async_to_raw_response_wrapper(
            configs.create,
        )
        self.update = async_to_raw_response_wrapper(
            configs.update,
        )
        self.list = async_to_raw_response_wrapper(
            configs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            configs.delete,
        )
        self.get = async_to_raw_response_wrapper(
            configs.get,
        )
        self.replace = async_to_raw_response_wrapper(
            configs.replace,
        )
        self.validate = async_to_raw_response_wrapper(
            configs.validate,
        )


class ConfigsResourceWithStreamingResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

        self.create = to_streamed_response_wrapper(
            configs.create,
        )
        self.update = to_streamed_response_wrapper(
            configs.update,
        )
        self.list = to_streamed_response_wrapper(
            configs.list,
        )
        self.delete = to_streamed_response_wrapper(
            configs.delete,
        )
        self.get = to_streamed_response_wrapper(
            configs.get,
        )
        self.replace = to_streamed_response_wrapper(
            configs.replace,
        )
        self.validate = to_streamed_response_wrapper(
            configs.validate,
        )


class AsyncConfigsResourceWithStreamingResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

        self.create = async_to_streamed_response_wrapper(
            configs.create,
        )
        self.update = async_to_streamed_response_wrapper(
            configs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            configs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            configs.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            configs.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            configs.replace,
        )
        self.validate = async_to_streamed_response_wrapper(
            configs.validate,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cdn.logs_uploader import (
    target_list_params,
    target_create_params,
    target_update_params,
    target_replace_params,
)
from ....types.cdn.logs_uploader_validation import LogsUploaderValidation
from ....types.cdn.logs_uploader.logs_uploader_target import LogsUploaderTarget

__all__ = ["TargetsResource", "AsyncTargetsResource"]


class TargetsResource(SyncAPIResource):
    """
    Logs uploader targets define destinations for CDN log delivery, such as S3 buckets or SFTP servers, with associated authentication and configuration settings.
    """

    @cached_property
    def with_raw_response(self) -> TargetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return TargetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TargetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return TargetsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetS3GcoreConfig,
        storage_type: Literal["s3_gcore"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          config: Config for the `s3_gcore` storage type.

          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetS3AmazonConfig,
        storage_type: Literal["s3_amazon"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetS3OssConfig,
        storage_type: Literal["s3_oss"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetS3OtherConfig,
        storage_type: Literal["s3_other"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetS3V1Config,
        storage_type: Literal["s3_v1"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetFtpConfig,
        storage_type: Literal["ftp"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetSftpConfig,
        storage_type: Literal["sftp"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetHTTPConfig,
        storage_type: Literal["http"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetAzureBlobConfig,
        storage_type: Literal["azure_blob"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetSlsConfig,
        storage_type: Literal["sls"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["config", "storage_type"])
    def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetS3GcoreConfig
        | target_create_params.CreateLogsUploaderTargetS3AmazonConfig
        | target_create_params.CreateLogsUploaderTargetS3OssConfig
        | target_create_params.CreateLogsUploaderTargetS3OtherConfig
        | target_create_params.CreateLogsUploaderTargetS3V1Config
        | target_create_params.CreateLogsUploaderTargetFtpConfig
        | target_create_params.CreateLogsUploaderTargetSftpConfig
        | target_create_params.CreateLogsUploaderTargetHTTPConfig
        | target_create_params.CreateLogsUploaderTargetAzureBlobConfig
        | target_create_params.CreateLogsUploaderTargetSlsConfig,
        storage_type: Literal["s3_gcore"]
        | Literal["s3_amazon"]
        | Literal["s3_oss"]
        | Literal["s3_other"]
        | Literal["s3_v1"]
        | Literal["ftp"]
        | Literal["sftp"]
        | Literal["http"]
        | Literal["azure_blob"]
        | Literal["sls"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        return cast(
            LogsUploaderTarget,
            self._post(
                "/cdn/logs_uploader/targets",
                body=maybe_transform(
                    {
                        "config": config,
                        "storage_type": storage_type,
                        "description": description,
                        "name": name,
                    },
                    target_create_params.TargetCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, LogsUploaderTarget
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        id: int,
        *,
        config: target_update_params.Config | Omit = omit,
        description: str | Omit = omit,
        name: str | Omit = omit,
        storage_type: Literal[
            "s3_gcore", "s3_amazon", "s3_oss", "s3_other", "s3_v1", "ftp", "sftp", "http", "azure_blob", "sls"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target partially.

        Args:
          config: Config for specific storage type.

          description: Description of the target.

          name: Name of the target.

          storage_type: Type of storage for logs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            LogsUploaderTarget,
            self._patch(
                path_template("/cdn/logs_uploader/targets/{id}", id=id),
                body=maybe_transform(
                    {
                        "config": config,
                        "description": description,
                        "name": name,
                        "storage_type": storage_type,
                    },
                    target_update_params.TargetUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, LogsUploaderTarget
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        config_ids: Iterable[int] | Omit = omit,
        limit: int | Omit = 1000,  # CDN API only envelopes when limit>=1; default so list() always paginates
        offset: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[LogsUploaderTarget]:
        """
        Get list of logs uploader targets.

        Args:
          config_ids: Filter by ids of related logs uploader configs that use given target.

          limit: Maximum number of items to return in the response. Cannot exceed 1000.

          offset: Number of items to skip from the beginning of the list.

          search: Search by target name or id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cdn/logs_uploader/targets",
            page=SyncOffsetPage[LogsUploaderTarget],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "config_ids": config_ids,
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                    },
                    target_list_params.TargetListParams,
                ),
            ),
            model=cast(Any, LogsUploaderTarget),  # Union types cannot be passed in as arguments in the type system
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
        Delete the logs uploader target from the system permanently.

        Notes:

        - **Irreversibility**: This action is irreversible. Once deleted, the logs
          uploader target cannot be recovered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/cdn/logs_uploader/targets/{id}", id=id),
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
    ) -> LogsUploaderTarget:
        """
        Get information about logs uploader target.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            LogsUploaderTarget,
            self._get(
                path_template("/cdn/logs_uploader/targets/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, LogsUploaderTarget
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetS3GcoreConfig,
        storage_type: Literal["s3_gcore"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          config: Config for the `s3_gcore` storage type.

          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetS3AmazonConfig,
        storage_type: Literal["s3_amazon"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetS3OssConfig,
        storage_type: Literal["s3_oss"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetS3OtherConfig,
        storage_type: Literal["s3_other"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetS3V1Config,
        storage_type: Literal["s3_v1"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetFtpConfig,
        storage_type: Literal["ftp"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetSftpConfig,
        storage_type: Literal["sftp"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetHTTPConfig,
        storage_type: Literal["http"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetAzureBlobConfig,
        storage_type: Literal["azure_blob"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetSlsConfig,
        storage_type: Literal["sls"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["config", "storage_type"])
    def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetS3GcoreConfig
        | target_replace_params.PutLogsUploaderTargetS3AmazonConfig
        | target_replace_params.PutLogsUploaderTargetS3OssConfig
        | target_replace_params.PutLogsUploaderTargetS3OtherConfig
        | target_replace_params.PutLogsUploaderTargetS3V1Config
        | target_replace_params.PutLogsUploaderTargetFtpConfig
        | target_replace_params.PutLogsUploaderTargetSftpConfig
        | target_replace_params.PutLogsUploaderTargetHTTPConfig
        | target_replace_params.PutLogsUploaderTargetAzureBlobConfig
        | target_replace_params.PutLogsUploaderTargetSlsConfig,
        storage_type: Literal["s3_gcore"]
        | Literal["s3_amazon"]
        | Literal["s3_oss"]
        | Literal["s3_other"]
        | Literal["s3_v1"]
        | Literal["ftp"]
        | Literal["sftp"]
        | Literal["http"]
        | Literal["azure_blob"]
        | Literal["sls"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        return cast(
            LogsUploaderTarget,
            self._put(
                path_template("/cdn/logs_uploader/targets/{id}", id=id),
                body=maybe_transform(
                    {
                        "config": config,
                        "storage_type": storage_type,
                        "description": description,
                        "name": name,
                    },
                    target_replace_params.TargetReplaceParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, LogsUploaderTarget
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        Validate logs uploader target.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/cdn/logs_uploader/targets/{id}/validate", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderValidation,
        )


class AsyncTargetsResource(AsyncAPIResource):
    """
    Logs uploader targets define destinations for CDN log delivery, such as S3 buckets or SFTP servers, with associated authentication and configuration settings.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTargetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTargetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTargetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncTargetsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetS3GcoreConfig,
        storage_type: Literal["s3_gcore"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          config: Config for the `s3_gcore` storage type.

          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetS3AmazonConfig,
        storage_type: Literal["s3_amazon"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetS3OssConfig,
        storage_type: Literal["s3_oss"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetS3OtherConfig,
        storage_type: Literal["s3_other"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetS3V1Config,
        storage_type: Literal["s3_v1"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetFtpConfig,
        storage_type: Literal["ftp"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetSftpConfig,
        storage_type: Literal["sftp"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetHTTPConfig,
        storage_type: Literal["http"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetAzureBlobConfig,
        storage_type: Literal["azure_blob"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetSlsConfig,
        storage_type: Literal["sls"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Create logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["config", "storage_type"])
    async def create(
        self,
        *,
        config: target_create_params.CreateLogsUploaderTargetS3GcoreConfig
        | target_create_params.CreateLogsUploaderTargetS3AmazonConfig
        | target_create_params.CreateLogsUploaderTargetS3OssConfig
        | target_create_params.CreateLogsUploaderTargetS3OtherConfig
        | target_create_params.CreateLogsUploaderTargetS3V1Config
        | target_create_params.CreateLogsUploaderTargetFtpConfig
        | target_create_params.CreateLogsUploaderTargetSftpConfig
        | target_create_params.CreateLogsUploaderTargetHTTPConfig
        | target_create_params.CreateLogsUploaderTargetAzureBlobConfig
        | target_create_params.CreateLogsUploaderTargetSlsConfig,
        storage_type: Literal["s3_gcore"]
        | Literal["s3_amazon"]
        | Literal["s3_oss"]
        | Literal["s3_other"]
        | Literal["s3_v1"]
        | Literal["ftp"]
        | Literal["sftp"]
        | Literal["http"]
        | Literal["azure_blob"]
        | Literal["sls"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        return cast(
            LogsUploaderTarget,
            await self._post(
                "/cdn/logs_uploader/targets",
                body=await async_maybe_transform(
                    {
                        "config": config,
                        "storage_type": storage_type,
                        "description": description,
                        "name": name,
                    },
                    target_create_params.TargetCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, LogsUploaderTarget
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        id: int,
        *,
        config: target_update_params.Config | Omit = omit,
        description: str | Omit = omit,
        name: str | Omit = omit,
        storage_type: Literal[
            "s3_gcore", "s3_amazon", "s3_oss", "s3_other", "s3_v1", "ftp", "sftp", "http", "azure_blob", "sls"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target partially.

        Args:
          config: Config for specific storage type.

          description: Description of the target.

          name: Name of the target.

          storage_type: Type of storage for logs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            LogsUploaderTarget,
            await self._patch(
                path_template("/cdn/logs_uploader/targets/{id}", id=id),
                body=await async_maybe_transform(
                    {
                        "config": config,
                        "description": description,
                        "name": name,
                        "storage_type": storage_type,
                    },
                    target_update_params.TargetUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, LogsUploaderTarget
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        config_ids: Iterable[int] | Omit = omit,
        limit: int | Omit = 1000,  # CDN API only envelopes when limit>=1; default so list() always paginates
        offset: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LogsUploaderTarget, AsyncOffsetPage[LogsUploaderTarget]]:
        """
        Get list of logs uploader targets.

        Args:
          config_ids: Filter by ids of related logs uploader configs that use given target.

          limit: Maximum number of items to return in the response. Cannot exceed 1000.

          offset: Number of items to skip from the beginning of the list.

          search: Search by target name or id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cdn/logs_uploader/targets",
            page=AsyncOffsetPage[LogsUploaderTarget],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "config_ids": config_ids,
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                    },
                    target_list_params.TargetListParams,
                ),
            ),
            model=cast(Any, LogsUploaderTarget),  # Union types cannot be passed in as arguments in the type system
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
        Delete the logs uploader target from the system permanently.

        Notes:

        - **Irreversibility**: This action is irreversible. Once deleted, the logs
          uploader target cannot be recovered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/cdn/logs_uploader/targets/{id}", id=id),
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
    ) -> LogsUploaderTarget:
        """
        Get information about logs uploader target.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            LogsUploaderTarget,
            await self._get(
                path_template("/cdn/logs_uploader/targets/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, LogsUploaderTarget
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetS3GcoreConfig,
        storage_type: Literal["s3_gcore"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          config: Config for the `s3_gcore` storage type.

          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetS3AmazonConfig,
        storage_type: Literal["s3_amazon"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetS3OssConfig,
        storage_type: Literal["s3_oss"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetS3OtherConfig,
        storage_type: Literal["s3_other"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetS3V1Config,
        storage_type: Literal["s3_v1"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetFtpConfig,
        storage_type: Literal["ftp"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetSftpConfig,
        storage_type: Literal["sftp"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetHTTPConfig,
        storage_type: Literal["http"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetAzureBlobConfig,
        storage_type: Literal["azure_blob"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetSlsConfig,
        storage_type: Literal["sls"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        """
        Change logs uploader target.

        Args:
          storage_type: Type of storage for logs.

          description: Description of the target.

          name: Name of the target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["config", "storage_type"])
    async def replace(
        self,
        id: int,
        *,
        config: target_replace_params.PutLogsUploaderTargetS3GcoreConfig
        | target_replace_params.PutLogsUploaderTargetS3AmazonConfig
        | target_replace_params.PutLogsUploaderTargetS3OssConfig
        | target_replace_params.PutLogsUploaderTargetS3OtherConfig
        | target_replace_params.PutLogsUploaderTargetS3V1Config
        | target_replace_params.PutLogsUploaderTargetFtpConfig
        | target_replace_params.PutLogsUploaderTargetSftpConfig
        | target_replace_params.PutLogsUploaderTargetHTTPConfig
        | target_replace_params.PutLogsUploaderTargetAzureBlobConfig
        | target_replace_params.PutLogsUploaderTargetSlsConfig,
        storage_type: Literal["s3_gcore"]
        | Literal["s3_amazon"]
        | Literal["s3_oss"]
        | Literal["s3_other"]
        | Literal["s3_v1"]
        | Literal["ftp"]
        | Literal["sftp"]
        | Literal["http"]
        | Literal["azure_blob"]
        | Literal["sls"],
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderTarget:
        return cast(
            LogsUploaderTarget,
            await self._put(
                path_template("/cdn/logs_uploader/targets/{id}", id=id),
                body=await async_maybe_transform(
                    {
                        "config": config,
                        "storage_type": storage_type,
                        "description": description,
                        "name": name,
                    },
                    target_replace_params.TargetReplaceParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, LogsUploaderTarget
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        Validate logs uploader target.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/cdn/logs_uploader/targets/{id}/validate", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderValidation,
        )


class TargetsResourceWithRawResponse:
    def __init__(self, targets: TargetsResource) -> None:
        self._targets = targets

        self.create = to_raw_response_wrapper(
            targets.create,
        )
        self.update = to_raw_response_wrapper(
            targets.update,
        )
        self.list = to_raw_response_wrapper(
            targets.list,
        )
        self.delete = to_raw_response_wrapper(
            targets.delete,
        )
        self.get = to_raw_response_wrapper(
            targets.get,
        )
        self.replace = to_raw_response_wrapper(
            targets.replace,
        )
        self.validate = to_raw_response_wrapper(
            targets.validate,
        )


class AsyncTargetsResourceWithRawResponse:
    def __init__(self, targets: AsyncTargetsResource) -> None:
        self._targets = targets

        self.create = async_to_raw_response_wrapper(
            targets.create,
        )
        self.update = async_to_raw_response_wrapper(
            targets.update,
        )
        self.list = async_to_raw_response_wrapper(
            targets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            targets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            targets.get,
        )
        self.replace = async_to_raw_response_wrapper(
            targets.replace,
        )
        self.validate = async_to_raw_response_wrapper(
            targets.validate,
        )


class TargetsResourceWithStreamingResponse:
    def __init__(self, targets: TargetsResource) -> None:
        self._targets = targets

        self.create = to_streamed_response_wrapper(
            targets.create,
        )
        self.update = to_streamed_response_wrapper(
            targets.update,
        )
        self.list = to_streamed_response_wrapper(
            targets.list,
        )
        self.delete = to_streamed_response_wrapper(
            targets.delete,
        )
        self.get = to_streamed_response_wrapper(
            targets.get,
        )
        self.replace = to_streamed_response_wrapper(
            targets.replace,
        )
        self.validate = to_streamed_response_wrapper(
            targets.validate,
        )


class AsyncTargetsResourceWithStreamingResponse:
    def __init__(self, targets: AsyncTargetsResource) -> None:
        self._targets = targets

        self.create = async_to_streamed_response_wrapper(
            targets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            targets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            targets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            targets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            targets.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            targets.replace,
        )
        self.validate = async_to_streamed_response_wrapper(
            targets.validate,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
    policy_list_params,
    policy_create_params,
    policy_update_params,
    policy_replace_params,
)
from ....types.cdn.logs_uploader.logs_uploader_policy import LogsUploaderPolicy
from ....types.cdn.logs_uploader.logs_uploader_policy_list import LogsUploaderPolicyList
from ....types.cdn.logs_uploader.policy_list_fields_response import PolicyListFieldsResponse

__all__ = ["PoliciesResource", "AsyncPoliciesResource"]


class PoliciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        date_format: str | Omit = omit,
        description: str | Omit = omit,
        field_delimiter: str | Omit = omit,
        field_separator: str | Omit = omit,
        fields: SequenceNotStr[str] | Omit = omit,
        file_name_template: str | Omit = omit,
        format_type: str | Omit = omit,
        include_empty_logs: bool | Omit = omit,
        include_shield_logs: bool | Omit = omit,
        name: str | Omit = omit,
        retry_interval_minutes: int | Omit = omit,
        rotate_interval_minutes: int | Omit = omit,
        rotate_threshold_lines: int | Omit = omit,
        rotate_threshold_mb: Optional[int] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderPolicy:
        """
        Create logs uploader policy.

        Args:
          date_format: Date format for logs.

          description: Description of the policy.

          field_delimiter: Field delimiter for logs.

          field_separator: Field separator for logs.

          fields: List of fields to include in logs.

          file_name_template: Template for log file name.

          format_type: Format type for logs.

          include_empty_logs: Include empty logs in the upload.

          include_shield_logs: Include logs from origin shielding in the upload.

          name: Name of the policy.

          retry_interval_minutes: Interval in minutes to retry failed uploads.

          rotate_interval_minutes: Interval in minutes to rotate logs.

          rotate_threshold_lines: Threshold in lines to rotate logs.

          rotate_threshold_mb: Threshold in MB to rotate logs.

          tags: Tags allow for dynamic decoration of logs by adding predefined fields to the log
              format. These tags serve as customizable key-value pairs that can be included in
              log entries to enhance context and readability.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cdn/logs_uploader/policies",
            body=maybe_transform(
                {
                    "date_format": date_format,
                    "description": description,
                    "field_delimiter": field_delimiter,
                    "field_separator": field_separator,
                    "fields": fields,
                    "file_name_template": file_name_template,
                    "format_type": format_type,
                    "include_empty_logs": include_empty_logs,
                    "include_shield_logs": include_shield_logs,
                    "name": name,
                    "retry_interval_minutes": retry_interval_minutes,
                    "rotate_interval_minutes": rotate_interval_minutes,
                    "rotate_threshold_lines": rotate_threshold_lines,
                    "rotate_threshold_mb": rotate_threshold_mb,
                    "tags": tags,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderPolicy,
        )

    def update(
        self,
        id: int,
        *,
        date_format: str | Omit = omit,
        description: str | Omit = omit,
        field_delimiter: str | Omit = omit,
        field_separator: str | Omit = omit,
        fields: SequenceNotStr[str] | Omit = omit,
        file_name_template: str | Omit = omit,
        format_type: str | Omit = omit,
        include_empty_logs: bool | Omit = omit,
        include_shield_logs: bool | Omit = omit,
        name: str | Omit = omit,
        retry_interval_minutes: int | Omit = omit,
        rotate_interval_minutes: int | Omit = omit,
        rotate_threshold_lines: int | Omit = omit,
        rotate_threshold_mb: Optional[int] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderPolicy:
        """
        Change logs uploader policy partially.

        Args:
          date_format: Date format for logs.

          description: Description of the policy.

          field_delimiter: Field delimiter for logs.

          field_separator: Field separator for logs.

          fields: List of fields to include in logs.

          file_name_template: Template for log file name.

          format_type: Format type for logs.

          include_empty_logs: Include empty logs in the upload.

          include_shield_logs: Include logs from origin shielding in the upload.

          name: Name of the policy.

          retry_interval_minutes: Interval in minutes to retry failed uploads.

          rotate_interval_minutes: Interval in minutes to rotate logs.

          rotate_threshold_lines: Threshold in lines to rotate logs.

          rotate_threshold_mb: Threshold in MB to rotate logs.

          tags: Tags allow for dynamic decoration of logs by adding predefined fields to the log
              format. These tags serve as customizable key-value pairs that can be included in
              log entries to enhance context and readability.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/cdn/logs_uploader/policies/{id}",
            body=maybe_transform(
                {
                    "date_format": date_format,
                    "description": description,
                    "field_delimiter": field_delimiter,
                    "field_separator": field_separator,
                    "fields": fields,
                    "file_name_template": file_name_template,
                    "format_type": format_type,
                    "include_empty_logs": include_empty_logs,
                    "include_shield_logs": include_shield_logs,
                    "name": name,
                    "retry_interval_minutes": retry_interval_minutes,
                    "rotate_interval_minutes": rotate_interval_minutes,
                    "rotate_threshold_lines": rotate_threshold_lines,
                    "rotate_threshold_mb": rotate_threshold_mb,
                    "tags": tags,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderPolicy,
        )

    def list(
        self,
        *,
        config_ids: Iterable[int] | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderPolicyList:
        """
        Get list of logs uploader policies.

        Args:
          config_ids: Filter by ids of related logs uploader configs that use given policy.

          search: Search by policy name or id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cdn/logs_uploader/policies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "config_ids": config_ids,
                        "search": search,
                    },
                    policy_list_params.PolicyListParams,
                ),
            ),
            cast_to=LogsUploaderPolicyList,
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
        Delete the logs uploader policy from the system permanently.

        Notes:

        - **Irreversibility**: This action is irreversible. Once deleted, the logs
          uploader policy cannot be recovered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cdn/logs_uploader/policies/{id}",
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
    ) -> LogsUploaderPolicy:
        """
        Get information about logs uploader policy.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cdn/logs_uploader/policies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderPolicy,
        )

    def list_fields(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyListFieldsResponse:
        """Get list of available fields for logs uploader policy."""
        return self._get(
            "/cdn/logs_uploader/policies/fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyListFieldsResponse,
        )

    def replace(
        self,
        id: int,
        *,
        date_format: str | Omit = omit,
        description: str | Omit = omit,
        field_delimiter: str | Omit = omit,
        field_separator: str | Omit = omit,
        fields: SequenceNotStr[str] | Omit = omit,
        file_name_template: str | Omit = omit,
        format_type: str | Omit = omit,
        include_empty_logs: bool | Omit = omit,
        include_shield_logs: bool | Omit = omit,
        name: str | Omit = omit,
        retry_interval_minutes: int | Omit = omit,
        rotate_interval_minutes: int | Omit = omit,
        rotate_threshold_lines: int | Omit = omit,
        rotate_threshold_mb: Optional[int] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderPolicy:
        """
        Change logs uploader policy.

        Args:
          date_format: Date format for logs.

          description: Description of the policy.

          field_delimiter: Field delimiter for logs.

          field_separator: Field separator for logs.

          fields: List of fields to include in logs.

          file_name_template: Template for log file name.

          format_type: Format type for logs.

          include_empty_logs: Include empty logs in the upload.

          include_shield_logs: Include logs from origin shielding in the upload.

          name: Name of the policy.

          retry_interval_minutes: Interval in minutes to retry failed uploads.

          rotate_interval_minutes: Interval in minutes to rotate logs.

          rotate_threshold_lines: Threshold in lines to rotate logs.

          rotate_threshold_mb: Threshold in MB to rotate logs.

          tags: Tags allow for dynamic decoration of logs by adding predefined fields to the log
              format. These tags serve as customizable key-value pairs that can be included in
              log entries to enhance context and readability.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/cdn/logs_uploader/policies/{id}",
            body=maybe_transform(
                {
                    "date_format": date_format,
                    "description": description,
                    "field_delimiter": field_delimiter,
                    "field_separator": field_separator,
                    "fields": fields,
                    "file_name_template": file_name_template,
                    "format_type": format_type,
                    "include_empty_logs": include_empty_logs,
                    "include_shield_logs": include_shield_logs,
                    "name": name,
                    "retry_interval_minutes": retry_interval_minutes,
                    "rotate_interval_minutes": rotate_interval_minutes,
                    "rotate_threshold_lines": rotate_threshold_lines,
                    "rotate_threshold_mb": rotate_threshold_mb,
                    "tags": tags,
                },
                policy_replace_params.PolicyReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderPolicy,
        )


class AsyncPoliciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        date_format: str | Omit = omit,
        description: str | Omit = omit,
        field_delimiter: str | Omit = omit,
        field_separator: str | Omit = omit,
        fields: SequenceNotStr[str] | Omit = omit,
        file_name_template: str | Omit = omit,
        format_type: str | Omit = omit,
        include_empty_logs: bool | Omit = omit,
        include_shield_logs: bool | Omit = omit,
        name: str | Omit = omit,
        retry_interval_minutes: int | Omit = omit,
        rotate_interval_minutes: int | Omit = omit,
        rotate_threshold_lines: int | Omit = omit,
        rotate_threshold_mb: Optional[int] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderPolicy:
        """
        Create logs uploader policy.

        Args:
          date_format: Date format for logs.

          description: Description of the policy.

          field_delimiter: Field delimiter for logs.

          field_separator: Field separator for logs.

          fields: List of fields to include in logs.

          file_name_template: Template for log file name.

          format_type: Format type for logs.

          include_empty_logs: Include empty logs in the upload.

          include_shield_logs: Include logs from origin shielding in the upload.

          name: Name of the policy.

          retry_interval_minutes: Interval in minutes to retry failed uploads.

          rotate_interval_minutes: Interval in minutes to rotate logs.

          rotate_threshold_lines: Threshold in lines to rotate logs.

          rotate_threshold_mb: Threshold in MB to rotate logs.

          tags: Tags allow for dynamic decoration of logs by adding predefined fields to the log
              format. These tags serve as customizable key-value pairs that can be included in
              log entries to enhance context and readability.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cdn/logs_uploader/policies",
            body=await async_maybe_transform(
                {
                    "date_format": date_format,
                    "description": description,
                    "field_delimiter": field_delimiter,
                    "field_separator": field_separator,
                    "fields": fields,
                    "file_name_template": file_name_template,
                    "format_type": format_type,
                    "include_empty_logs": include_empty_logs,
                    "include_shield_logs": include_shield_logs,
                    "name": name,
                    "retry_interval_minutes": retry_interval_minutes,
                    "rotate_interval_minutes": rotate_interval_minutes,
                    "rotate_threshold_lines": rotate_threshold_lines,
                    "rotate_threshold_mb": rotate_threshold_mb,
                    "tags": tags,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderPolicy,
        )

    async def update(
        self,
        id: int,
        *,
        date_format: str | Omit = omit,
        description: str | Omit = omit,
        field_delimiter: str | Omit = omit,
        field_separator: str | Omit = omit,
        fields: SequenceNotStr[str] | Omit = omit,
        file_name_template: str | Omit = omit,
        format_type: str | Omit = omit,
        include_empty_logs: bool | Omit = omit,
        include_shield_logs: bool | Omit = omit,
        name: str | Omit = omit,
        retry_interval_minutes: int | Omit = omit,
        rotate_interval_minutes: int | Omit = omit,
        rotate_threshold_lines: int | Omit = omit,
        rotate_threshold_mb: Optional[int] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderPolicy:
        """
        Change logs uploader policy partially.

        Args:
          date_format: Date format for logs.

          description: Description of the policy.

          field_delimiter: Field delimiter for logs.

          field_separator: Field separator for logs.

          fields: List of fields to include in logs.

          file_name_template: Template for log file name.

          format_type: Format type for logs.

          include_empty_logs: Include empty logs in the upload.

          include_shield_logs: Include logs from origin shielding in the upload.

          name: Name of the policy.

          retry_interval_minutes: Interval in minutes to retry failed uploads.

          rotate_interval_minutes: Interval in minutes to rotate logs.

          rotate_threshold_lines: Threshold in lines to rotate logs.

          rotate_threshold_mb: Threshold in MB to rotate logs.

          tags: Tags allow for dynamic decoration of logs by adding predefined fields to the log
              format. These tags serve as customizable key-value pairs that can be included in
              log entries to enhance context and readability.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/cdn/logs_uploader/policies/{id}",
            body=await async_maybe_transform(
                {
                    "date_format": date_format,
                    "description": description,
                    "field_delimiter": field_delimiter,
                    "field_separator": field_separator,
                    "fields": fields,
                    "file_name_template": file_name_template,
                    "format_type": format_type,
                    "include_empty_logs": include_empty_logs,
                    "include_shield_logs": include_shield_logs,
                    "name": name,
                    "retry_interval_minutes": retry_interval_minutes,
                    "rotate_interval_minutes": rotate_interval_minutes,
                    "rotate_threshold_lines": rotate_threshold_lines,
                    "rotate_threshold_mb": rotate_threshold_mb,
                    "tags": tags,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderPolicy,
        )

    async def list(
        self,
        *,
        config_ids: Iterable[int] | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderPolicyList:
        """
        Get list of logs uploader policies.

        Args:
          config_ids: Filter by ids of related logs uploader configs that use given policy.

          search: Search by policy name or id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cdn/logs_uploader/policies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "config_ids": config_ids,
                        "search": search,
                    },
                    policy_list_params.PolicyListParams,
                ),
            ),
            cast_to=LogsUploaderPolicyList,
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
        Delete the logs uploader policy from the system permanently.

        Notes:

        - **Irreversibility**: This action is irreversible. Once deleted, the logs
          uploader policy cannot be recovered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cdn/logs_uploader/policies/{id}",
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
    ) -> LogsUploaderPolicy:
        """
        Get information about logs uploader policy.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cdn/logs_uploader/policies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderPolicy,
        )

    async def list_fields(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyListFieldsResponse:
        """Get list of available fields for logs uploader policy."""
        return await self._get(
            "/cdn/logs_uploader/policies/fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyListFieldsResponse,
        )

    async def replace(
        self,
        id: int,
        *,
        date_format: str | Omit = omit,
        description: str | Omit = omit,
        field_delimiter: str | Omit = omit,
        field_separator: str | Omit = omit,
        fields: SequenceNotStr[str] | Omit = omit,
        file_name_template: str | Omit = omit,
        format_type: str | Omit = omit,
        include_empty_logs: bool | Omit = omit,
        include_shield_logs: bool | Omit = omit,
        name: str | Omit = omit,
        retry_interval_minutes: int | Omit = omit,
        rotate_interval_minutes: int | Omit = omit,
        rotate_threshold_lines: int | Omit = omit,
        rotate_threshold_mb: Optional[int] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsUploaderPolicy:
        """
        Change logs uploader policy.

        Args:
          date_format: Date format for logs.

          description: Description of the policy.

          field_delimiter: Field delimiter for logs.

          field_separator: Field separator for logs.

          fields: List of fields to include in logs.

          file_name_template: Template for log file name.

          format_type: Format type for logs.

          include_empty_logs: Include empty logs in the upload.

          include_shield_logs: Include logs from origin shielding in the upload.

          name: Name of the policy.

          retry_interval_minutes: Interval in minutes to retry failed uploads.

          rotate_interval_minutes: Interval in minutes to rotate logs.

          rotate_threshold_lines: Threshold in lines to rotate logs.

          rotate_threshold_mb: Threshold in MB to rotate logs.

          tags: Tags allow for dynamic decoration of logs by adding predefined fields to the log
              format. These tags serve as customizable key-value pairs that can be included in
              log entries to enhance context and readability.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/cdn/logs_uploader/policies/{id}",
            body=await async_maybe_transform(
                {
                    "date_format": date_format,
                    "description": description,
                    "field_delimiter": field_delimiter,
                    "field_separator": field_separator,
                    "fields": fields,
                    "file_name_template": file_name_template,
                    "format_type": format_type,
                    "include_empty_logs": include_empty_logs,
                    "include_shield_logs": include_shield_logs,
                    "name": name,
                    "retry_interval_minutes": retry_interval_minutes,
                    "rotate_interval_minutes": rotate_interval_minutes,
                    "rotate_threshold_lines": rotate_threshold_lines,
                    "rotate_threshold_mb": rotate_threshold_mb,
                    "tags": tags,
                },
                policy_replace_params.PolicyReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogsUploaderPolicy,
        )


class PoliciesResourceWithRawResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_raw_response_wrapper(
            policies.create,
        )
        self.update = to_raw_response_wrapper(
            policies.update,
        )
        self.list = to_raw_response_wrapper(
            policies.list,
        )
        self.delete = to_raw_response_wrapper(
            policies.delete,
        )
        self.get = to_raw_response_wrapper(
            policies.get,
        )
        self.list_fields = to_raw_response_wrapper(
            policies.list_fields,
        )
        self.replace = to_raw_response_wrapper(
            policies.replace,
        )


class AsyncPoliciesResourceWithRawResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_raw_response_wrapper(
            policies.create,
        )
        self.update = async_to_raw_response_wrapper(
            policies.update,
        )
        self.list = async_to_raw_response_wrapper(
            policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            policies.delete,
        )
        self.get = async_to_raw_response_wrapper(
            policies.get,
        )
        self.list_fields = async_to_raw_response_wrapper(
            policies.list_fields,
        )
        self.replace = async_to_raw_response_wrapper(
            policies.replace,
        )


class PoliciesResourceWithStreamingResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_streamed_response_wrapper(
            policies.create,
        )
        self.update = to_streamed_response_wrapper(
            policies.update,
        )
        self.list = to_streamed_response_wrapper(
            policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            policies.delete,
        )
        self.get = to_streamed_response_wrapper(
            policies.get,
        )
        self.list_fields = to_streamed_response_wrapper(
            policies.list_fields,
        )
        self.replace = to_streamed_response_wrapper(
            policies.replace,
        )


class AsyncPoliciesResourceWithStreamingResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_streamed_response_wrapper(
            policies.create,
        )
        self.update = async_to_streamed_response_wrapper(
            policies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            policies.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            policies.get,
        )
        self.list_fields = async_to_streamed_response_wrapper(
            policies.list_fields,
        )
        self.replace = async_to_streamed_response_wrapper(
            policies.replace,
        )

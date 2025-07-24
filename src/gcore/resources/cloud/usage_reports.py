# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cloud import usage_report_get_params
from ..._base_client import make_request_options
from ...types.cloud.usage_report import UsageReport

__all__ = ["UsageReportsResource", "AsyncUsageReportsResource"]


class UsageReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return UsageReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return UsageReportsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        time_from: Union[str, datetime],
        time_to: Union[str, datetime],
        enable_last_day: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        projects: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        regions: Iterable[int] | NotGiven = NOT_GIVEN,
        schema_filter: usage_report_get_params.SchemaFilter | NotGiven = NOT_GIVEN,
        sorting: Iterable[usage_report_get_params.Sorting] | NotGiven = NOT_GIVEN,
        tags: usage_report_get_params.Tags | NotGiven = NOT_GIVEN,
        types: List[
            Literal[
                "ai_cluster",
                "ai_virtual_cluster",
                "backup",
                "baremetal",
                "basic_vm",
                "containers",
                "dbaas_postgresql_connection_pooler",
                "dbaas_postgresql_cpu",
                "dbaas_postgresql_memory",
                "dbaas_postgresql_public_network",
                "dbaas_postgresql_volume",
                "egress_traffic",
                "external_ip",
                "file_share",
                "floatingip",
                "functions",
                "functions_calls",
                "functions_traffic",
                "image",
                "inference",
                "instance",
                "load_balancer",
                "log_index",
                "snapshot",
                "volume",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageReport:
        """Receiving data from the past hour might lead to incomplete statistics.

        For the
        most accurate data, we recommend accessing the statistics after at least one
        hour. Typically, updates are available within a 24-hour period, although the
        frequency can vary. Maintenance periods or other exceptions may cause delays,
        potentially extending beyond 24 hours until the servers are back online and the
        missing data is filled in.

        Args:
          time_from: The start date of the report period (ISO 8601). The report starts from the
              beginning of this day.

          time_to: The end date of the report period (ISO 8601). The report ends just before the
              beginning of this day.

          enable_last_day: Expenses for the last specified day are taken into account. As the default,
              False.

          limit: The response resources limit. Defaults to 10.

          offset: The response resources offset.

          projects: List of project IDs

          regions: List of region IDs.

          schema_filter: Extended filter for field filtering.

          sorting: List of sorting filters (JSON objects) fields: project. directions: asc, desc.

          tags: Filter by tags

          types: List of resource types to be filtered in the report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cloud/v1/usage_report",
            body=maybe_transform(
                {
                    "time_from": time_from,
                    "time_to": time_to,
                    "enable_last_day": enable_last_day,
                    "limit": limit,
                    "offset": offset,
                    "projects": projects,
                    "regions": regions,
                    "schema_filter": schema_filter,
                    "sorting": sorting,
                    "tags": tags,
                    "types": types,
                },
                usage_report_get_params.UsageReportGetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageReport,
        )


class AsyncUsageReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncUsageReportsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        time_from: Union[str, datetime],
        time_to: Union[str, datetime],
        enable_last_day: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        projects: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        regions: Iterable[int] | NotGiven = NOT_GIVEN,
        schema_filter: usage_report_get_params.SchemaFilter | NotGiven = NOT_GIVEN,
        sorting: Iterable[usage_report_get_params.Sorting] | NotGiven = NOT_GIVEN,
        tags: usage_report_get_params.Tags | NotGiven = NOT_GIVEN,
        types: List[
            Literal[
                "ai_cluster",
                "ai_virtual_cluster",
                "backup",
                "baremetal",
                "basic_vm",
                "containers",
                "dbaas_postgresql_connection_pooler",
                "dbaas_postgresql_cpu",
                "dbaas_postgresql_memory",
                "dbaas_postgresql_public_network",
                "dbaas_postgresql_volume",
                "egress_traffic",
                "external_ip",
                "file_share",
                "floatingip",
                "functions",
                "functions_calls",
                "functions_traffic",
                "image",
                "inference",
                "instance",
                "load_balancer",
                "log_index",
                "snapshot",
                "volume",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageReport:
        """Receiving data from the past hour might lead to incomplete statistics.

        For the
        most accurate data, we recommend accessing the statistics after at least one
        hour. Typically, updates are available within a 24-hour period, although the
        frequency can vary. Maintenance periods or other exceptions may cause delays,
        potentially extending beyond 24 hours until the servers are back online and the
        missing data is filled in.

        Args:
          time_from: The start date of the report period (ISO 8601). The report starts from the
              beginning of this day.

          time_to: The end date of the report period (ISO 8601). The report ends just before the
              beginning of this day.

          enable_last_day: Expenses for the last specified day are taken into account. As the default,
              False.

          limit: The response resources limit. Defaults to 10.

          offset: The response resources offset.

          projects: List of project IDs

          regions: List of region IDs.

          schema_filter: Extended filter for field filtering.

          sorting: List of sorting filters (JSON objects) fields: project. directions: asc, desc.

          tags: Filter by tags

          types: List of resource types to be filtered in the report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cloud/v1/usage_report",
            body=await async_maybe_transform(
                {
                    "time_from": time_from,
                    "time_to": time_to,
                    "enable_last_day": enable_last_day,
                    "limit": limit,
                    "offset": offset,
                    "projects": projects,
                    "regions": regions,
                    "schema_filter": schema_filter,
                    "sorting": sorting,
                    "tags": tags,
                    "types": types,
                },
                usage_report_get_params.UsageReportGetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageReport,
        )


class UsageReportsResourceWithRawResponse:
    def __init__(self, usage_reports: UsageReportsResource) -> None:
        self._usage_reports = usage_reports

        self.get = to_raw_response_wrapper(
            usage_reports.get,
        )


class AsyncUsageReportsResourceWithRawResponse:
    def __init__(self, usage_reports: AsyncUsageReportsResource) -> None:
        self._usage_reports = usage_reports

        self.get = async_to_raw_response_wrapper(
            usage_reports.get,
        )


class UsageReportsResourceWithStreamingResponse:
    def __init__(self, usage_reports: UsageReportsResource) -> None:
        self._usage_reports = usage_reports

        self.get = to_streamed_response_wrapper(
            usage_reports.get,
        )


class AsyncUsageReportsResourceWithStreamingResponse:
    def __init__(self, usage_reports: AsyncUsageReportsResource) -> None:
        self._usage_reports = usage_reports

        self.get = async_to_streamed_response_wrapper(
            usage_reports.get,
        )

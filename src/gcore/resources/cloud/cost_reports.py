# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
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
from ...types.cloud import (
    cost_report_get_detailed_params,
    cost_report_get_aggregated_params,
    cost_report_get_aggregated_monthly_params,
)
from ..._base_client import make_request_options
from ...types.cloud.cost_report_detailed import CostReportDetailed
from ...types.cloud.cost_report_aggregated import CostReportAggregated
from ...types.cloud.cost_report_aggregated_monthly import CostReportAggregatedMonthly

__all__ = ["CostReportsResource", "AsyncCostReportsResource"]


class CostReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CostReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return CostReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CostReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return CostReportsResourceWithStreamingResponse(self)

    def get_aggregated(
        self,
        *,
        time_from: Union[str, datetime],
        time_to: Union[str, datetime],
        enable_last_day: bool | NotGiven = NOT_GIVEN,
        projects: Iterable[int] | NotGiven = NOT_GIVEN,
        regions: Iterable[int] | NotGiven = NOT_GIVEN,
        response_format: Literal["csv_totals", "json"] | NotGiven = NOT_GIVEN,
        rounding: bool | NotGiven = NOT_GIVEN,
        schema_filter: cost_report_get_aggregated_params.SchemaFilter | NotGiven = NOT_GIVEN,
        tags: cost_report_get_aggregated_params.Tags | NotGiven = NOT_GIVEN,
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
    ) -> CostReportAggregated:
        """Get cost report totals (aggregated costs) for a given period.

        Requested period
        should not exceed 31 days. Note: This report assumes there are no active commit
        features in the billing plan. If there are active commit features (pre-paid
        resources) in your plan, use /v1/`reservation_cost_report`/totals, as the
        results from this report will not be accurate. Receiving data from the past hour
        might lead to incomplete statistics. For the most accurate data, we recommend
        accessing the statistics after at least one hour. Typically, updates are
        available within a 24-hour period, although the frequency can vary. Maintenance
        periods or other exceptions may cause delays, potentially extending beyond 24
        hours until the servers are back online and the missing data is filled in.

        Args:
          time_from: The start date of the report period (ISO 8601). The report starts from the
              beginning of this day.

          time_to: The end date of the report period (ISO 8601). The report ends just before the
              beginning of this day.

          enable_last_day: Expenses for the last specified day are taken into account. As the default,
              False.

          projects: List of project IDs

          regions: List of region IDs.

          response_format: Format of the response (csv or json).

          rounding: Round cost values to 5 decimal places. When false, returns full precision.

          schema_filter: Extended filter for field filtering.

          tags: Filter by tags

          types: List of resource types to be filtered in the report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cloud/v1/cost_report/totals",
            body=maybe_transform(
                {
                    "time_from": time_from,
                    "time_to": time_to,
                    "enable_last_day": enable_last_day,
                    "projects": projects,
                    "regions": regions,
                    "response_format": response_format,
                    "rounding": rounding,
                    "schema_filter": schema_filter,
                    "tags": tags,
                    "types": types,
                },
                cost_report_get_aggregated_params.CostReportGetAggregatedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CostReportAggregated,
        )

    def get_aggregated_monthly(
        self,
        *,
        time_from: Union[str, datetime],
        time_to: Union[str, datetime],
        regions: Iterable[int] | NotGiven = NOT_GIVEN,
        response_format: Literal["csv_totals", "json"] | NotGiven = NOT_GIVEN,
        rounding: bool | NotGiven = NOT_GIVEN,
        schema_filter: cost_report_get_aggregated_monthly_params.SchemaFilter | NotGiven = NOT_GIVEN,
        tags: cost_report_get_aggregated_monthly_params.Tags | NotGiven = NOT_GIVEN,
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
    ) -> CostReportAggregatedMonthly:
        """
        Retrieve a detailed cost report totals for a specified month, which includes
        both commit and pay-as-you-go (overcommit) prices. Additionally, it provides the
        spent billing units (e.g., hours or GB) for resources. The "`time_to`" parameter
        represents all days in the specified month. Receiving data from the past hour
        might lead to incomplete statistics. For the most accurate data, we recommend
        accessing the statistics after at least one hour. Typically, updates are
        available within a 24-hour period, although the frequency can vary. Maintenance
        periods or other exceptions may cause delays, potentially extending beyond 24
        hours until the servers are back online and the missing data is filled in.

        Args:
          time_from: Beginning of the period: YYYY-mm

          time_to: End of the period: YYYY-mm

          regions: List of region IDs.

          response_format: Format of the response (`csv_totals` or json).

          rounding: Round cost values to 5 decimal places. When false, returns full precision.

          schema_filter: Extended filter for field filtering.

          tags: Filter by tags

          types: List of resource types to be filtered in the report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cloud/v1/reservation_cost_report/totals",
            body=maybe_transform(
                {
                    "time_from": time_from,
                    "time_to": time_to,
                    "regions": regions,
                    "response_format": response_format,
                    "rounding": rounding,
                    "schema_filter": schema_filter,
                    "tags": tags,
                    "types": types,
                },
                cost_report_get_aggregated_monthly_params.CostReportGetAggregatedMonthlyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CostReportAggregatedMonthly,
        )

    def get_detailed(
        self,
        *,
        time_from: Union[str, datetime],
        time_to: Union[str, datetime],
        enable_last_day: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        projects: Iterable[int] | NotGiven = NOT_GIVEN,
        regions: Iterable[int] | NotGiven = NOT_GIVEN,
        response_format: Literal["csv_records", "json"] | NotGiven = NOT_GIVEN,
        rounding: bool | NotGiven = NOT_GIVEN,
        schema_filter: cost_report_get_detailed_params.SchemaFilter | NotGiven = NOT_GIVEN,
        sorting: Iterable[cost_report_get_detailed_params.Sorting] | NotGiven = NOT_GIVEN,
        tags: cost_report_get_detailed_params.Tags | NotGiven = NOT_GIVEN,
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
    ) -> CostReportDetailed:
        """Get a detailed cost report for a given period and specific resources.

        Requested
        period should not exceed 31 days. Note: This report assumes there are no active
        commit features in the billing plan. If there are active commit features
        (pre-paid resources) in your plan, use /v1/`reservation_cost_report`/totals, as
        the results from this report will not be accurate. Receiving data from the past
        hour might lead to incomplete statistics. For the most accurate data, we
        recommend accessing the statistics after at least one hour. Typically, updates
        are available within a 24-hour period, although the frequency can vary.
        Maintenance periods or other exceptions may cause delays, potentially extending
        beyond 24 hours until the servers are back online and the missing data is filled
        in.

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

          response_format: Format of the response (csv or json).

          rounding: Round cost values to 5 decimal places. When false, returns full precision.

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
            "/cloud/v1/cost_report/resources",
            body=maybe_transform(
                {
                    "time_from": time_from,
                    "time_to": time_to,
                    "enable_last_day": enable_last_day,
                    "limit": limit,
                    "offset": offset,
                    "projects": projects,
                    "regions": regions,
                    "response_format": response_format,
                    "rounding": rounding,
                    "schema_filter": schema_filter,
                    "sorting": sorting,
                    "tags": tags,
                    "types": types,
                },
                cost_report_get_detailed_params.CostReportGetDetailedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CostReportDetailed,
        )


class AsyncCostReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCostReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCostReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCostReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncCostReportsResourceWithStreamingResponse(self)

    async def get_aggregated(
        self,
        *,
        time_from: Union[str, datetime],
        time_to: Union[str, datetime],
        enable_last_day: bool | NotGiven = NOT_GIVEN,
        projects: Iterable[int] | NotGiven = NOT_GIVEN,
        regions: Iterable[int] | NotGiven = NOT_GIVEN,
        response_format: Literal["csv_totals", "json"] | NotGiven = NOT_GIVEN,
        rounding: bool | NotGiven = NOT_GIVEN,
        schema_filter: cost_report_get_aggregated_params.SchemaFilter | NotGiven = NOT_GIVEN,
        tags: cost_report_get_aggregated_params.Tags | NotGiven = NOT_GIVEN,
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
    ) -> CostReportAggregated:
        """Get cost report totals (aggregated costs) for a given period.

        Requested period
        should not exceed 31 days. Note: This report assumes there are no active commit
        features in the billing plan. If there are active commit features (pre-paid
        resources) in your plan, use /v1/`reservation_cost_report`/totals, as the
        results from this report will not be accurate. Receiving data from the past hour
        might lead to incomplete statistics. For the most accurate data, we recommend
        accessing the statistics after at least one hour. Typically, updates are
        available within a 24-hour period, although the frequency can vary. Maintenance
        periods or other exceptions may cause delays, potentially extending beyond 24
        hours until the servers are back online and the missing data is filled in.

        Args:
          time_from: The start date of the report period (ISO 8601). The report starts from the
              beginning of this day.

          time_to: The end date of the report period (ISO 8601). The report ends just before the
              beginning of this day.

          enable_last_day: Expenses for the last specified day are taken into account. As the default,
              False.

          projects: List of project IDs

          regions: List of region IDs.

          response_format: Format of the response (csv or json).

          rounding: Round cost values to 5 decimal places. When false, returns full precision.

          schema_filter: Extended filter for field filtering.

          tags: Filter by tags

          types: List of resource types to be filtered in the report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cloud/v1/cost_report/totals",
            body=await async_maybe_transform(
                {
                    "time_from": time_from,
                    "time_to": time_to,
                    "enable_last_day": enable_last_day,
                    "projects": projects,
                    "regions": regions,
                    "response_format": response_format,
                    "rounding": rounding,
                    "schema_filter": schema_filter,
                    "tags": tags,
                    "types": types,
                },
                cost_report_get_aggregated_params.CostReportGetAggregatedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CostReportAggregated,
        )

    async def get_aggregated_monthly(
        self,
        *,
        time_from: Union[str, datetime],
        time_to: Union[str, datetime],
        regions: Iterable[int] | NotGiven = NOT_GIVEN,
        response_format: Literal["csv_totals", "json"] | NotGiven = NOT_GIVEN,
        rounding: bool | NotGiven = NOT_GIVEN,
        schema_filter: cost_report_get_aggregated_monthly_params.SchemaFilter | NotGiven = NOT_GIVEN,
        tags: cost_report_get_aggregated_monthly_params.Tags | NotGiven = NOT_GIVEN,
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
    ) -> CostReportAggregatedMonthly:
        """
        Retrieve a detailed cost report totals for a specified month, which includes
        both commit and pay-as-you-go (overcommit) prices. Additionally, it provides the
        spent billing units (e.g., hours or GB) for resources. The "`time_to`" parameter
        represents all days in the specified month. Receiving data from the past hour
        might lead to incomplete statistics. For the most accurate data, we recommend
        accessing the statistics after at least one hour. Typically, updates are
        available within a 24-hour period, although the frequency can vary. Maintenance
        periods or other exceptions may cause delays, potentially extending beyond 24
        hours until the servers are back online and the missing data is filled in.

        Args:
          time_from: Beginning of the period: YYYY-mm

          time_to: End of the period: YYYY-mm

          regions: List of region IDs.

          response_format: Format of the response (`csv_totals` or json).

          rounding: Round cost values to 5 decimal places. When false, returns full precision.

          schema_filter: Extended filter for field filtering.

          tags: Filter by tags

          types: List of resource types to be filtered in the report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cloud/v1/reservation_cost_report/totals",
            body=await async_maybe_transform(
                {
                    "time_from": time_from,
                    "time_to": time_to,
                    "regions": regions,
                    "response_format": response_format,
                    "rounding": rounding,
                    "schema_filter": schema_filter,
                    "tags": tags,
                    "types": types,
                },
                cost_report_get_aggregated_monthly_params.CostReportGetAggregatedMonthlyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CostReportAggregatedMonthly,
        )

    async def get_detailed(
        self,
        *,
        time_from: Union[str, datetime],
        time_to: Union[str, datetime],
        enable_last_day: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        projects: Iterable[int] | NotGiven = NOT_GIVEN,
        regions: Iterable[int] | NotGiven = NOT_GIVEN,
        response_format: Literal["csv_records", "json"] | NotGiven = NOT_GIVEN,
        rounding: bool | NotGiven = NOT_GIVEN,
        schema_filter: cost_report_get_detailed_params.SchemaFilter | NotGiven = NOT_GIVEN,
        sorting: Iterable[cost_report_get_detailed_params.Sorting] | NotGiven = NOT_GIVEN,
        tags: cost_report_get_detailed_params.Tags | NotGiven = NOT_GIVEN,
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
    ) -> CostReportDetailed:
        """Get a detailed cost report for a given period and specific resources.

        Requested
        period should not exceed 31 days. Note: This report assumes there are no active
        commit features in the billing plan. If there are active commit features
        (pre-paid resources) in your plan, use /v1/`reservation_cost_report`/totals, as
        the results from this report will not be accurate. Receiving data from the past
        hour might lead to incomplete statistics. For the most accurate data, we
        recommend accessing the statistics after at least one hour. Typically, updates
        are available within a 24-hour period, although the frequency can vary.
        Maintenance periods or other exceptions may cause delays, potentially extending
        beyond 24 hours until the servers are back online and the missing data is filled
        in.

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

          response_format: Format of the response (csv or json).

          rounding: Round cost values to 5 decimal places. When false, returns full precision.

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
            "/cloud/v1/cost_report/resources",
            body=await async_maybe_transform(
                {
                    "time_from": time_from,
                    "time_to": time_to,
                    "enable_last_day": enable_last_day,
                    "limit": limit,
                    "offset": offset,
                    "projects": projects,
                    "regions": regions,
                    "response_format": response_format,
                    "rounding": rounding,
                    "schema_filter": schema_filter,
                    "sorting": sorting,
                    "tags": tags,
                    "types": types,
                },
                cost_report_get_detailed_params.CostReportGetDetailedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CostReportDetailed,
        )


class CostReportsResourceWithRawResponse:
    def __init__(self, cost_reports: CostReportsResource) -> None:
        self._cost_reports = cost_reports

        self.get_aggregated = to_raw_response_wrapper(
            cost_reports.get_aggregated,
        )
        self.get_aggregated_monthly = to_raw_response_wrapper(
            cost_reports.get_aggregated_monthly,
        )
        self.get_detailed = to_raw_response_wrapper(
            cost_reports.get_detailed,
        )


class AsyncCostReportsResourceWithRawResponse:
    def __init__(self, cost_reports: AsyncCostReportsResource) -> None:
        self._cost_reports = cost_reports

        self.get_aggregated = async_to_raw_response_wrapper(
            cost_reports.get_aggregated,
        )
        self.get_aggregated_monthly = async_to_raw_response_wrapper(
            cost_reports.get_aggregated_monthly,
        )
        self.get_detailed = async_to_raw_response_wrapper(
            cost_reports.get_detailed,
        )


class CostReportsResourceWithStreamingResponse:
    def __init__(self, cost_reports: CostReportsResource) -> None:
        self._cost_reports = cost_reports

        self.get_aggregated = to_streamed_response_wrapper(
            cost_reports.get_aggregated,
        )
        self.get_aggregated_monthly = to_streamed_response_wrapper(
            cost_reports.get_aggregated_monthly,
        )
        self.get_detailed = to_streamed_response_wrapper(
            cost_reports.get_detailed,
        )


class AsyncCostReportsResourceWithStreamingResponse:
    def __init__(self, cost_reports: AsyncCostReportsResource) -> None:
        self._cost_reports = cost_reports

        self.get_aggregated = async_to_streamed_response_wrapper(
            cost_reports.get_aggregated,
        )
        self.get_aggregated_monthly = async_to_streamed_response_wrapper(
            cost_reports.get_aggregated_monthly,
        )
        self.get_detailed = async_to_streamed_response_wrapper(
            cost_reports.get_detailed,
        )

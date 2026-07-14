# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.security import event_list_params
from ...types.security.event_log import EventLog
from ...types.security.client_view import ClientView

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        alert_type: Optional[Literal["ddos_alert", "rtbh_alert"]] | Omit = omit,
        date_from: Union[Union[str, datetime], str] | Omit = omit,
        date_to: Union[Union[str, datetime], str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal[
            "attack_start_time",
            "-attack_start_time",
            "attack_power_bps",
            "-attack_power_bps",
            "attack_power_pps",
            "-attack_power_pps",
            "number_of_ip_involved_in_attack",
            "-number_of_ip_involved_in_attack",
            "alert_type",
            "-alert_type",
        ]
        | Omit = omit,
        targeted_ip_addresses: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[ClientView]:
        """
        Event Logs Clients View

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/security/notifier/v1/event_logs",
            page=SyncOffsetPage[ClientView],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "alert_type": alert_type,
                        "date_from": date_from,
                        "date_to": date_to,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "targeted_ip_addresses": targeted_ip_addresses,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=ClientView,
        )

    def get(
        self,
        event_log_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventLog:
        """
        Event Log Detail View

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_log_id:
            raise ValueError(f"Expected a non-empty value for `event_log_id` but received {event_log_id!r}")
        return self._get(
            path_template("/security/notifier/v1/event_logs/{event_log_id}", event_log_id=event_log_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventLog,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        alert_type: Optional[Literal["ddos_alert", "rtbh_alert"]] | Omit = omit,
        date_from: Union[Union[str, datetime], str] | Omit = omit,
        date_to: Union[Union[str, datetime], str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal[
            "attack_start_time",
            "-attack_start_time",
            "attack_power_bps",
            "-attack_power_bps",
            "attack_power_pps",
            "-attack_power_pps",
            "number_of_ip_involved_in_attack",
            "-number_of_ip_involved_in_attack",
            "alert_type",
            "-alert_type",
        ]
        | Omit = omit,
        targeted_ip_addresses: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ClientView, AsyncOffsetPage[ClientView]]:
        """
        Event Logs Clients View

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/security/notifier/v1/event_logs",
            page=AsyncOffsetPage[ClientView],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "alert_type": alert_type,
                        "date_from": date_from,
                        "date_to": date_to,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "targeted_ip_addresses": targeted_ip_addresses,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=ClientView,
        )

    async def get(
        self,
        event_log_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventLog:
        """
        Event Log Detail View

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_log_id:
            raise ValueError(f"Expected a non-empty value for `event_log_id` but received {event_log_id!r}")
        return await self._get(
            path_template("/security/notifier/v1/event_logs/{event_log_id}", event_log_id=event_log_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventLog,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_raw_response_wrapper(
            events.list,
        )
        self.get = to_raw_response_wrapper(
            events.get,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_raw_response_wrapper(
            events.list,
        )
        self.get = async_to_raw_response_wrapper(
            events.get,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_streamed_response_wrapper(
            events.list,
        )
        self.get = to_streamed_response_wrapper(
            events.get,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
        self.get = async_to_streamed_response_wrapper(
            events.get,
        )

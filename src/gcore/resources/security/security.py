# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .profiles import (
    ProfilesResource,
    AsyncProfilesResource,
    ProfilesResourceWithRawResponse,
    AsyncProfilesResourceWithRawResponse,
    ProfilesResourceWithStreamingResponse,
    AsyncProfilesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .bgp_announces import (
    BgpAnnouncesResource,
    AsyncBgpAnnouncesResource,
    BgpAnnouncesResourceWithRawResponse,
    AsyncBgpAnnouncesResourceWithRawResponse,
    BgpAnnouncesResourceWithStreamingResponse,
    AsyncBgpAnnouncesResourceWithStreamingResponse,
)
from .profile_templates import (
    ProfileTemplatesResource,
    AsyncProfileTemplatesResource,
    ProfileTemplatesResourceWithRawResponse,
    AsyncProfileTemplatesResourceWithRawResponse,
    ProfileTemplatesResourceWithStreamingResponse,
    AsyncProfileTemplatesResourceWithStreamingResponse,
)

__all__ = ["SecurityResource", "AsyncSecurityResource"]


class SecurityResource(SyncAPIResource):
    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def bgp_announces(self) -> BgpAnnouncesResource:
        return BgpAnnouncesResource(self._client)

    @cached_property
    def profile_templates(self) -> ProfileTemplatesResource:
        return ProfileTemplatesResource(self._client)

    @cached_property
    def profiles(self) -> ProfilesResource:
        return ProfilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return SecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return SecurityResourceWithStreamingResponse(self)


class AsyncSecurityResource(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def bgp_announces(self) -> AsyncBgpAnnouncesResource:
        return AsyncBgpAnnouncesResource(self._client)

    @cached_property
    def profile_templates(self) -> AsyncProfileTemplatesResource:
        return AsyncProfileTemplatesResource(self._client)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        return AsyncProfilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncSecurityResourceWithStreamingResponse(self)


class SecurityResourceWithRawResponse:
    def __init__(self, security: SecurityResource) -> None:
        self._security = security

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._security.events)

    @cached_property
    def bgp_announces(self) -> BgpAnnouncesResourceWithRawResponse:
        return BgpAnnouncesResourceWithRawResponse(self._security.bgp_announces)

    @cached_property
    def profile_templates(self) -> ProfileTemplatesResourceWithRawResponse:
        return ProfileTemplatesResourceWithRawResponse(self._security.profile_templates)

    @cached_property
    def profiles(self) -> ProfilesResourceWithRawResponse:
        return ProfilesResourceWithRawResponse(self._security.profiles)


class AsyncSecurityResourceWithRawResponse:
    def __init__(self, security: AsyncSecurityResource) -> None:
        self._security = security

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._security.events)

    @cached_property
    def bgp_announces(self) -> AsyncBgpAnnouncesResourceWithRawResponse:
        return AsyncBgpAnnouncesResourceWithRawResponse(self._security.bgp_announces)

    @cached_property
    def profile_templates(self) -> AsyncProfileTemplatesResourceWithRawResponse:
        return AsyncProfileTemplatesResourceWithRawResponse(self._security.profile_templates)

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithRawResponse:
        return AsyncProfilesResourceWithRawResponse(self._security.profiles)


class SecurityResourceWithStreamingResponse:
    def __init__(self, security: SecurityResource) -> None:
        self._security = security

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._security.events)

    @cached_property
    def bgp_announces(self) -> BgpAnnouncesResourceWithStreamingResponse:
        return BgpAnnouncesResourceWithStreamingResponse(self._security.bgp_announces)

    @cached_property
    def profile_templates(self) -> ProfileTemplatesResourceWithStreamingResponse:
        return ProfileTemplatesResourceWithStreamingResponse(self._security.profile_templates)

    @cached_property
    def profiles(self) -> ProfilesResourceWithStreamingResponse:
        return ProfilesResourceWithStreamingResponse(self._security.profiles)


class AsyncSecurityResourceWithStreamingResponse:
    def __init__(self, security: AsyncSecurityResource) -> None:
        self._security = security

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._security.events)

    @cached_property
    def bgp_announces(self) -> AsyncBgpAnnouncesResourceWithStreamingResponse:
        return AsyncBgpAnnouncesResourceWithStreamingResponse(self._security.bgp_announces)

    @cached_property
    def profile_templates(self) -> AsyncProfileTemplatesResourceWithStreamingResponse:
        return AsyncProfileTemplatesResourceWithStreamingResponse(self._security.profile_templates)

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithStreamingResponse:
        return AsyncProfilesResourceWithStreamingResponse(self._security.profiles)

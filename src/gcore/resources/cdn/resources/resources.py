# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, overload

import httpx

from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from .shield import (
    ShieldResource,
    AsyncShieldResource,
    ShieldResourceWithRawResponse,
    AsyncShieldResourceWithRawResponse,
    ShieldResourceWithStreamingResponse,
    AsyncShieldResourceWithStreamingResponse,
)
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
from ....types.cdn import (
    resource_list_params,
    resource_purge_params,
    resource_create_params,
    resource_update_params,
    resource_replace_params,
    resource_prefetch_params,
)
from ...._base_client import make_request_options
from ....types.cdn.cdn_resource import CdnResource
from ....types.cdn.cdn_resource_list import CdnResourceList

__all__ = ["ResourcesResource", "AsyncResourcesResource"]


class ResourcesResource(SyncAPIResource):
    @cached_property
    def shield(self) -> ShieldResource:
        return ShieldResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ResourcesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        cname: str,
        origin: str,
        origin_group: int,
        active: bool | Omit = omit,
        description: str | Omit = omit,
        name: Optional[str] | Omit = omit,
        options: resource_create_params.Options | Omit = omit,
        origin_protocol: Literal["HTTP", "HTTPS", "MATCH"] | Omit = omit,
        primary_resource: Optional[int] | Omit = omit,
        proxy_ssl_ca: Optional[int] | Omit = omit,
        proxy_ssl_data: Optional[int] | Omit = omit,
        proxy_ssl_enabled: bool | Omit = omit,
        secondary_hostnames: SequenceNotStr[str] | Omit = omit,
        ssl_data: Optional[int] | Omit = omit,
        ssl_enabled: bool | Omit = omit,
        waap_api_domain_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResource:
        """
        Create CDN resource

        Args:
          cname: Delivery domains that will be used for content delivery through a CDN.

              Delivery domains should be added to your DNS settings.

          origin: IP address or domain name of the origin and the port, if custom port is used.

              You can use either the `origin` or `originGroup` parameter in the request.

          origin_group: Origin group ID with which the CDN resource is associated.

              You can use either the `origin` or `originGroup` parameter in the request.

          active: Enables or disables a CDN resource.

              Possible values:

              - **true** - CDN resource is active. Content is being delivered.
              - **false** - CDN resource is deactivated. Content is not being delivered.

          description: Optional comment describing the CDN resource.

          name: CDN resource name.

          options: List of options that can be configured for the CDN resource.

              In case of `null` value the option is not added to the CDN resource. Option may
              inherit its value from the global account settings.

          origin_protocol: Protocol used by CDN servers to request content from an origin source.

              Possible values:

              - **HTTPS** - CDN servers will connect to the origin via HTTPS.
              - **HTTP** - CDN servers will connect to the origin via HTTP.
              - **MATCH** - connection protocol will be chosen automatically (content on the
                origin source should be available for the CDN both through HTTP and HTTPS).

              If protocol is not specified, HTTP is used to connect to an origin server.

          primary_resource: ID of the main CDN resource which has a shared caching zone with a reserve CDN
              resource.

              If the parameter is not empty, then the current CDN resource is the reserve. You
              cannot change some options, create rules, set up origin shielding, or use the
              reserve CDN resource for Streaming.

          proxy_ssl_ca: ID of the trusted CA certificate used to verify an origin.

              It can be used only with `"proxy_ssl_enabled": true`.

          proxy_ssl_data: ID of the SSL certificate used to verify an origin.

              It can be used only with `"proxy_ssl_enabled": true`.

          proxy_ssl_enabled: Enables or disables SSL certificate validation of the origin server before
              completing any connection.

              Possible values:

              - **true** - Origin SSL certificate validation is enabled.
              - **false** - Origin SSL certificate validation is disabled.

          secondary_hostnames: Additional delivery domains (CNAMEs) that will be used to deliver content via
              the CDN.

              Up to ten additional CNAMEs are possible.

          ssl_data: ID of the SSL certificate linked to the CDN resource.

              Can be used only with `"sslEnabled": true`.

          ssl_enabled: Defines whether the HTTPS protocol enabled for content delivery.

              Possible values:

              - **true** - HTTPS is enabled.
              - **false** - HTTPS is disabled.

          waap_api_domain_enabled: Defines whether the associated WAAP Domain is identified as an API Domain.

              Possible values:

              - **true** - The associated WAAP Domain is designated as an API Domain.
              - **false** - The associated WAAP Domain is not designated as an API Domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cdn/resources",
            body=maybe_transform(
                {
                    "cname": cname,
                    "origin": origin,
                    "origin_group": origin_group,
                    "active": active,
                    "description": description,
                    "name": name,
                    "options": options,
                    "origin_protocol": origin_protocol,
                    "primary_resource": primary_resource,
                    "proxy_ssl_ca": proxy_ssl_ca,
                    "proxy_ssl_data": proxy_ssl_data,
                    "proxy_ssl_enabled": proxy_ssl_enabled,
                    "secondary_hostnames": secondary_hostnames,
                    "ssl_data": ssl_data,
                    "ssl_enabled": ssl_enabled,
                    "waap_api_domain_enabled": waap_api_domain_enabled,
                },
                resource_create_params.ResourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResource,
        )

    def update(
        self,
        resource_id: int,
        *,
        active: bool | Omit = omit,
        description: str | Omit = omit,
        name: Optional[str] | Omit = omit,
        options: resource_update_params.Options | Omit = omit,
        origin_group: int | Omit = omit,
        origin_protocol: Literal["HTTP", "HTTPS", "MATCH"] | Omit = omit,
        proxy_ssl_ca: Optional[int] | Omit = omit,
        proxy_ssl_data: Optional[int] | Omit = omit,
        proxy_ssl_enabled: bool | Omit = omit,
        secondary_hostnames: SequenceNotStr[str] | Omit = omit,
        ssl_data: Optional[int] | Omit = omit,
        ssl_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResource:
        """
        Change CDN resource

        Args:
          active: Enables or disables a CDN resource.

              Possible values:

              - **true** - CDN resource is active. Content is being delivered.
              - **false** - CDN resource is deactivated. Content is not being delivered.

          description: Optional comment describing the CDN resource.

          name: CDN resource name.

          options: List of options that can be configured for the CDN resource.

              In case of `null` value the option is not added to the CDN resource. Option may
              inherit its value from the global account settings.

          origin_group: Origin group ID with which the CDN resource is associated.

              You can use either the `origin` or `originGroup` parameter in the request.

          origin_protocol: Protocol used by CDN servers to request content from an origin source.

              Possible values:

              - **HTTPS** - CDN servers will connect to the origin via HTTPS.
              - **HTTP** - CDN servers will connect to the origin via HTTP.
              - **MATCH** - connection protocol will be chosen automatically (content on the
                origin source should be available for the CDN both through HTTP and HTTPS).

              If protocol is not specified, HTTP is used to connect to an origin server.

          proxy_ssl_ca: ID of the trusted CA certificate used to verify an origin.

              It can be used only with `"proxy_ssl_enabled": true`.

          proxy_ssl_data: ID of the SSL certificate used to verify an origin.

              It can be used only with `"proxy_ssl_enabled": true`.

          proxy_ssl_enabled: Enables or disables SSL certificate validation of the origin server before
              completing any connection.

              Possible values:

              - **true** - Origin SSL certificate validation is enabled.
              - **false** - Origin SSL certificate validation is disabled.

          secondary_hostnames: Additional delivery domains (CNAMEs) that will be used to deliver content via
              the CDN.

              Up to ten additional CNAMEs are possible.

          ssl_data: ID of the SSL certificate linked to the CDN resource.

              Can be used only with `"sslEnabled": true`.

          ssl_enabled: Defines whether the HTTPS protocol enabled for content delivery.

              Possible values:

              - **true** - HTTPS is enabled.
              - **false** - HTTPS is disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/cdn/resources/{resource_id}",
            body=maybe_transform(
                {
                    "active": active,
                    "description": description,
                    "name": name,
                    "options": options,
                    "origin_group": origin_group,
                    "origin_protocol": origin_protocol,
                    "proxy_ssl_ca": proxy_ssl_ca,
                    "proxy_ssl_data": proxy_ssl_data,
                    "proxy_ssl_enabled": proxy_ssl_enabled,
                    "secondary_hostnames": secondary_hostnames,
                    "ssl_data": ssl_data,
                    "ssl_enabled": ssl_enabled,
                },
                resource_update_params.ResourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResource,
        )

    def list(
        self,
        *,
        cname: str | Omit = omit,
        deleted: bool | Omit = omit,
        enabled: bool | Omit = omit,
        max_created: str | Omit = omit,
        min_created: str | Omit = omit,
        origin_group: int | Omit = omit,
        rules: str | Omit = omit,
        secondary_hostnames: str | Omit = omit,
        shield_dc: str | Omit = omit,
        shielded: bool | Omit = omit,
        ssl_data: int | Omit = omit,
        ssl_data_in: int | Omit = omit,
        ssl_enabled: bool | Omit = omit,
        status: Literal["active", "processed", "suspended", "deleted"] | Omit = omit,
        suspend: bool | Omit = omit,
        vp_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResourceList:
        """
        Get information about all CDN resources in your account.

        Args:
          cname: Delivery domain (CNAME) of the CDN resource.

          deleted: Defines whether a CDN resource has been deleted.

              Possible values:

              - **true** - CDN resource has been deleted.
              - **false** - CDN resource has not been deleted.

          enabled: Enables or disables a CDN resource change by a user.

              Possible values:

              - **true** - CDN resource is enabled.
              - **false** - CDN resource is disabled.

          max_created: Most recent date of CDN resource creation for which CDN resources should be
              returned (ISO 8601/RFC 3339 format, UTC.)

          min_created: Earliest date of CDN resource creation for which CDN resources should be
              returned (ISO 8601/RFC 3339 format, UTC.)

          origin_group: Origin group ID.

          rules: Rule name or pattern.

          secondary_hostnames: Additional delivery domains (CNAMEs) of the CDN resource.

          shield_dc: Name of the origin shielding data center location.

          shielded: Defines whether origin shielding is enabled for the CDN resource.

              Possible values:

              - **true** - Origin shielding is enabled for the CDN resource.
              - **false** - Origin shielding is disabled for the CDN resource.

          ssl_data: SSL certificate ID.

          ssl_data_in: SSL certificates IDs.

              Example:

              - ?`sslData_in`=1643,1644,1652

          ssl_enabled: Defines whether the HTTPS protocol is enabled for content delivery.

              Possible values:

              - **true** - HTTPS protocol is enabled for CDN resource.
              - **false** - HTTPS protocol is disabled for CDN resource.

          status: CDN resource status.

          suspend: Defines whether the CDN resource was automatically suspended by the system.

              Possible values:

              - **true** - CDN resource is selected for automatic suspension in the next 7
                days.
              - **false** - CDN resource is not selected for automatic suspension.

          vp_enabled: Defines whether the CDN resource is integrated with the Streaming platform.

              Possible values:

              - **true** - CDN resource is used for Streaming platform.
              - **false** - CDN resource is not used for Streaming platform.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cdn/resources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cname": cname,
                        "deleted": deleted,
                        "enabled": enabled,
                        "max_created": max_created,
                        "min_created": min_created,
                        "origin_group": origin_group,
                        "rules": rules,
                        "secondary_hostnames": secondary_hostnames,
                        "shield_dc": shield_dc,
                        "shielded": shielded,
                        "ssl_data": ssl_data,
                        "ssl_data_in": ssl_data_in,
                        "ssl_enabled": ssl_enabled,
                        "status": status,
                        "suspend": suspend,
                        "vp_enabled": vp_enabled,
                    },
                    resource_list_params.ResourceListParams,
                ),
            ),
            cast_to=CdnResourceList,
        )

    def delete(
        self,
        resource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the CDN resource from the system permanently.

        Notes:

        - **Deactivation Requirement**: Set the `active` attribute to `false` before
          deletion.
        - **Statistics Availability**: Statistics will be available for **365 days**
          after deletion through the
          [statistics endpoints](/docs/api-reference/cdn/cdn-statistics/cdn-resource-statistics).
        - **Irreversibility**: This action is irreversible. Once deleted, the CDN
          resource cannot be recovered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cdn/resources/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        resource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResource:
        """
        Get CDN resource details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cdn/resources/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResource,
        )

    def prefetch(
        self,
        resource_id: int,
        *,
        paths: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Pre-populate files to a CDN cache before users requests.

        Prefetch is recommended
        only for files that **more than 200 MB** and **less than 5 GB**.

        You can make one prefetch request for a CDN resource per minute. One request for
        prefetch may content only up to 100 paths to files.

        The time of procedure depends on the number and size of the files.

        If you need to update files stored in the CDN, first purge these files and then
        prefetch.

        Args:
          paths: Paths to files that should be pre-populated to the CDN.

              Paths to the files should be specified without a domain name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cdn/resources/{resource_id}/prefetch",
            body=maybe_transform({"paths": paths}, resource_prefetch_params.ResourcePrefetchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def prevalidate_ssl_le_certificate(
        self,
        resource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Check whether a Let's Encrypt certificate can be issued for the CDN resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cdn/resources/{resource_id}/ssl/le/pre-validate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    def purge(
        self,
        resource_id: int,
        *,
        urls: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete cache from CDN servers.

        This is necessary to update CDN content.

        We have different limits for different purge types:

        - **Purge all cache** - One purge request for a CDN resource per minute.
        - **Purge by URL** - Two purge requests for a CDN resource per minute. One purge
          request is limited to 100 URLs.
        - **Purge by pattern** - One purge request for a CDN resource per minute. One
          purge request is limited to 10 patterns.

        Args:
          urls: **Purge by URL** clears the cache of a specific files. This purge type is
              recommended.

              Specify file URLs including query strings. URLs should start with / without a
              domain name.

              Purge by URL depends on the following CDN options:

              1. "vary response header" is used. If your origin serves variants of the same
                 content depending on the Vary HTTP response header, purge by URL will delete
                 only one version of the file.
              2. "slice" is used. If you update several files in the origin without clearing
                 the CDN cache, purge by URL will delete only the first slice (with bytes=0…
                 .)
              3. "ignoreQueryString" is used. Don’t specify parameters in the purge request.
              4. "`query_params_blacklist`" is used. Only files with the listed in the option
                 parameters will be cached as different objects. Files with other parameters
                 will be cached as one object. In this case, specify the listed parameters in
                 the Purge request. Don't specify other parameters.
              5. "`query_params_whitelist`" is used. Files with listed in the option
                 parameters will be cached as one object. Files with other parameters will be
                 cached as different objects. In this case, specify other parameters (if any)
                 besides the ones listed in the purge request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def purge(
        self,
        resource_id: int,
        *,
        paths: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete cache from CDN servers.

        This is necessary to update CDN content.

        We have different limits for different purge types:

        - **Purge all cache** - One purge request for a CDN resource per minute.
        - **Purge by URL** - Two purge requests for a CDN resource per minute. One purge
          request is limited to 100 URLs.
        - **Purge by pattern** - One purge request for a CDN resource per minute. One
          purge request is limited to 10 patterns.

        Args:
          paths: **Purge by pattern** clears the cache that matches the pattern.

              Use _ operator, which replaces any number of symbols in your path. It's
              important to note that wildcard usage (_) is permitted only at the end of a
              pattern.

              Query string added to any patterns will be ignored, and purge request will be
              processed as if there weren't any parameters.

              Purge by pattern is recursive. Both /path and /path* will result in recursive
              purging, meaning all content under the specified path will be affected. As such,
              using the pattern /path* is functionally equivalent to simply using /path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def purge(
        self,
        resource_id: int,
        *,
        paths: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete cache from CDN servers.

        This is necessary to update CDN content.

        We have different limits for different purge types:

        - **Purge all cache** - One purge request for a CDN resource per minute.
        - **Purge by URL** - Two purge requests for a CDN resource per minute. One purge
          request is limited to 100 URLs.
        - **Purge by pattern** - One purge request for a CDN resource per minute. One
          purge request is limited to 10 patterns.

        Args:
          paths: **Purge all cache** clears the entire cache for the CDN resource.

              Specify an empty array to purge all content for the resource.

              When you purge all assets, CDN servers request content from your origin server
              and cause a high load. Therefore, we recommend to use purge by URL for large
              content quantities.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def purge(
        self,
        resource_id: int,
        *,
        urls: SequenceNotStr[str] | Omit = omit,
        paths: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cdn/resources/{resource_id}/purge",
            body=maybe_transform(
                {
                    "urls": urls,
                    "paths": paths,
                },
                resource_purge_params.ResourcePurgeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def replace(
        self,
        resource_id: int,
        *,
        origin_group: int,
        active: bool | Omit = omit,
        description: str | Omit = omit,
        name: Optional[str] | Omit = omit,
        options: resource_replace_params.Options | Omit = omit,
        origin_protocol: Literal["HTTP", "HTTPS", "MATCH"] | Omit = omit,
        proxy_ssl_ca: Optional[int] | Omit = omit,
        proxy_ssl_data: Optional[int] | Omit = omit,
        proxy_ssl_enabled: bool | Omit = omit,
        secondary_hostnames: SequenceNotStr[str] | Omit = omit,
        ssl_data: Optional[int] | Omit = omit,
        ssl_enabled: bool | Omit = omit,
        waap_api_domain_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResource:
        """
        Change CDN resource

        Args:
          origin_group: Origin group ID with which the CDN resource is associated.

              You can use either the `origin` or `originGroup` parameter in the request.

          active: Enables or disables a CDN resource.

              Possible values:

              - **true** - CDN resource is active. Content is being delivered.
              - **false** - CDN resource is deactivated. Content is not being delivered.

          description: Optional comment describing the CDN resource.

          name: CDN resource name.

          options: List of options that can be configured for the CDN resource.

              In case of `null` value the option is not added to the CDN resource. Option may
              inherit its value from the global account settings.

          origin_protocol: Protocol used by CDN servers to request content from an origin source.

              Possible values:

              - **HTTPS** - CDN servers will connect to the origin via HTTPS.
              - **HTTP** - CDN servers will connect to the origin via HTTP.
              - **MATCH** - connection protocol will be chosen automatically (content on the
                origin source should be available for the CDN both through HTTP and HTTPS).

              If protocol is not specified, HTTP is used to connect to an origin server.

          proxy_ssl_ca: ID of the trusted CA certificate used to verify an origin.

              It can be used only with `"proxy_ssl_enabled": true`.

          proxy_ssl_data: ID of the SSL certificate used to verify an origin.

              It can be used only with `"proxy_ssl_enabled": true`.

          proxy_ssl_enabled: Enables or disables SSL certificate validation of the origin server before
              completing any connection.

              Possible values:

              - **true** - Origin SSL certificate validation is enabled.
              - **false** - Origin SSL certificate validation is disabled.

          secondary_hostnames: Additional delivery domains (CNAMEs) that will be used to deliver content via
              the CDN.

              Up to ten additional CNAMEs are possible.

          ssl_data: ID of the SSL certificate linked to the CDN resource.

              Can be used only with `"sslEnabled": true`.

          ssl_enabled: Defines whether the HTTPS protocol enabled for content delivery.

              Possible values:

              - **true** - HTTPS is enabled.
              - **false** - HTTPS is disabled.

          waap_api_domain_enabled: Defines whether the associated WAAP Domain is identified as an API Domain.

              Possible values:

              - **true** - The associated WAAP Domain is designated as an API Domain.
              - **false** - The associated WAAP Domain is not designated as an API Domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/cdn/resources/{resource_id}",
            body=maybe_transform(
                {
                    "origin_group": origin_group,
                    "active": active,
                    "description": description,
                    "name": name,
                    "options": options,
                    "origin_protocol": origin_protocol,
                    "proxy_ssl_ca": proxy_ssl_ca,
                    "proxy_ssl_data": proxy_ssl_data,
                    "proxy_ssl_enabled": proxy_ssl_enabled,
                    "secondary_hostnames": secondary_hostnames,
                    "ssl_data": ssl_data,
                    "ssl_enabled": ssl_enabled,
                    "waap_api_domain_enabled": waap_api_domain_enabled,
                },
                resource_replace_params.ResourceReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResource,
        )


class AsyncResourcesResource(AsyncAPIResource):
    @cached_property
    def shield(self) -> AsyncShieldResource:
        return AsyncShieldResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncResourcesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        cname: str,
        origin: str,
        origin_group: int,
        active: bool | Omit = omit,
        description: str | Omit = omit,
        name: Optional[str] | Omit = omit,
        options: resource_create_params.Options | Omit = omit,
        origin_protocol: Literal["HTTP", "HTTPS", "MATCH"] | Omit = omit,
        primary_resource: Optional[int] | Omit = omit,
        proxy_ssl_ca: Optional[int] | Omit = omit,
        proxy_ssl_data: Optional[int] | Omit = omit,
        proxy_ssl_enabled: bool | Omit = omit,
        secondary_hostnames: SequenceNotStr[str] | Omit = omit,
        ssl_data: Optional[int] | Omit = omit,
        ssl_enabled: bool | Omit = omit,
        waap_api_domain_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResource:
        """
        Create CDN resource

        Args:
          cname: Delivery domains that will be used for content delivery through a CDN.

              Delivery domains should be added to your DNS settings.

          origin: IP address or domain name of the origin and the port, if custom port is used.

              You can use either the `origin` or `originGroup` parameter in the request.

          origin_group: Origin group ID with which the CDN resource is associated.

              You can use either the `origin` or `originGroup` parameter in the request.

          active: Enables or disables a CDN resource.

              Possible values:

              - **true** - CDN resource is active. Content is being delivered.
              - **false** - CDN resource is deactivated. Content is not being delivered.

          description: Optional comment describing the CDN resource.

          name: CDN resource name.

          options: List of options that can be configured for the CDN resource.

              In case of `null` value the option is not added to the CDN resource. Option may
              inherit its value from the global account settings.

          origin_protocol: Protocol used by CDN servers to request content from an origin source.

              Possible values:

              - **HTTPS** - CDN servers will connect to the origin via HTTPS.
              - **HTTP** - CDN servers will connect to the origin via HTTP.
              - **MATCH** - connection protocol will be chosen automatically (content on the
                origin source should be available for the CDN both through HTTP and HTTPS).

              If protocol is not specified, HTTP is used to connect to an origin server.

          primary_resource: ID of the main CDN resource which has a shared caching zone with a reserve CDN
              resource.

              If the parameter is not empty, then the current CDN resource is the reserve. You
              cannot change some options, create rules, set up origin shielding, or use the
              reserve CDN resource for Streaming.

          proxy_ssl_ca: ID of the trusted CA certificate used to verify an origin.

              It can be used only with `"proxy_ssl_enabled": true`.

          proxy_ssl_data: ID of the SSL certificate used to verify an origin.

              It can be used only with `"proxy_ssl_enabled": true`.

          proxy_ssl_enabled: Enables or disables SSL certificate validation of the origin server before
              completing any connection.

              Possible values:

              - **true** - Origin SSL certificate validation is enabled.
              - **false** - Origin SSL certificate validation is disabled.

          secondary_hostnames: Additional delivery domains (CNAMEs) that will be used to deliver content via
              the CDN.

              Up to ten additional CNAMEs are possible.

          ssl_data: ID of the SSL certificate linked to the CDN resource.

              Can be used only with `"sslEnabled": true`.

          ssl_enabled: Defines whether the HTTPS protocol enabled for content delivery.

              Possible values:

              - **true** - HTTPS is enabled.
              - **false** - HTTPS is disabled.

          waap_api_domain_enabled: Defines whether the associated WAAP Domain is identified as an API Domain.

              Possible values:

              - **true** - The associated WAAP Domain is designated as an API Domain.
              - **false** - The associated WAAP Domain is not designated as an API Domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cdn/resources",
            body=await async_maybe_transform(
                {
                    "cname": cname,
                    "origin": origin,
                    "origin_group": origin_group,
                    "active": active,
                    "description": description,
                    "name": name,
                    "options": options,
                    "origin_protocol": origin_protocol,
                    "primary_resource": primary_resource,
                    "proxy_ssl_ca": proxy_ssl_ca,
                    "proxy_ssl_data": proxy_ssl_data,
                    "proxy_ssl_enabled": proxy_ssl_enabled,
                    "secondary_hostnames": secondary_hostnames,
                    "ssl_data": ssl_data,
                    "ssl_enabled": ssl_enabled,
                    "waap_api_domain_enabled": waap_api_domain_enabled,
                },
                resource_create_params.ResourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResource,
        )

    async def update(
        self,
        resource_id: int,
        *,
        active: bool | Omit = omit,
        description: str | Omit = omit,
        name: Optional[str] | Omit = omit,
        options: resource_update_params.Options | Omit = omit,
        origin_group: int | Omit = omit,
        origin_protocol: Literal["HTTP", "HTTPS", "MATCH"] | Omit = omit,
        proxy_ssl_ca: Optional[int] | Omit = omit,
        proxy_ssl_data: Optional[int] | Omit = omit,
        proxy_ssl_enabled: bool | Omit = omit,
        secondary_hostnames: SequenceNotStr[str] | Omit = omit,
        ssl_data: Optional[int] | Omit = omit,
        ssl_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResource:
        """
        Change CDN resource

        Args:
          active: Enables or disables a CDN resource.

              Possible values:

              - **true** - CDN resource is active. Content is being delivered.
              - **false** - CDN resource is deactivated. Content is not being delivered.

          description: Optional comment describing the CDN resource.

          name: CDN resource name.

          options: List of options that can be configured for the CDN resource.

              In case of `null` value the option is not added to the CDN resource. Option may
              inherit its value from the global account settings.

          origin_group: Origin group ID with which the CDN resource is associated.

              You can use either the `origin` or `originGroup` parameter in the request.

          origin_protocol: Protocol used by CDN servers to request content from an origin source.

              Possible values:

              - **HTTPS** - CDN servers will connect to the origin via HTTPS.
              - **HTTP** - CDN servers will connect to the origin via HTTP.
              - **MATCH** - connection protocol will be chosen automatically (content on the
                origin source should be available for the CDN both through HTTP and HTTPS).

              If protocol is not specified, HTTP is used to connect to an origin server.

          proxy_ssl_ca: ID of the trusted CA certificate used to verify an origin.

              It can be used only with `"proxy_ssl_enabled": true`.

          proxy_ssl_data: ID of the SSL certificate used to verify an origin.

              It can be used only with `"proxy_ssl_enabled": true`.

          proxy_ssl_enabled: Enables or disables SSL certificate validation of the origin server before
              completing any connection.

              Possible values:

              - **true** - Origin SSL certificate validation is enabled.
              - **false** - Origin SSL certificate validation is disabled.

          secondary_hostnames: Additional delivery domains (CNAMEs) that will be used to deliver content via
              the CDN.

              Up to ten additional CNAMEs are possible.

          ssl_data: ID of the SSL certificate linked to the CDN resource.

              Can be used only with `"sslEnabled": true`.

          ssl_enabled: Defines whether the HTTPS protocol enabled for content delivery.

              Possible values:

              - **true** - HTTPS is enabled.
              - **false** - HTTPS is disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/cdn/resources/{resource_id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "description": description,
                    "name": name,
                    "options": options,
                    "origin_group": origin_group,
                    "origin_protocol": origin_protocol,
                    "proxy_ssl_ca": proxy_ssl_ca,
                    "proxy_ssl_data": proxy_ssl_data,
                    "proxy_ssl_enabled": proxy_ssl_enabled,
                    "secondary_hostnames": secondary_hostnames,
                    "ssl_data": ssl_data,
                    "ssl_enabled": ssl_enabled,
                },
                resource_update_params.ResourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResource,
        )

    async def list(
        self,
        *,
        cname: str | Omit = omit,
        deleted: bool | Omit = omit,
        enabled: bool | Omit = omit,
        max_created: str | Omit = omit,
        min_created: str | Omit = omit,
        origin_group: int | Omit = omit,
        rules: str | Omit = omit,
        secondary_hostnames: str | Omit = omit,
        shield_dc: str | Omit = omit,
        shielded: bool | Omit = omit,
        ssl_data: int | Omit = omit,
        ssl_data_in: int | Omit = omit,
        ssl_enabled: bool | Omit = omit,
        status: Literal["active", "processed", "suspended", "deleted"] | Omit = omit,
        suspend: bool | Omit = omit,
        vp_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResourceList:
        """
        Get information about all CDN resources in your account.

        Args:
          cname: Delivery domain (CNAME) of the CDN resource.

          deleted: Defines whether a CDN resource has been deleted.

              Possible values:

              - **true** - CDN resource has been deleted.
              - **false** - CDN resource has not been deleted.

          enabled: Enables or disables a CDN resource change by a user.

              Possible values:

              - **true** - CDN resource is enabled.
              - **false** - CDN resource is disabled.

          max_created: Most recent date of CDN resource creation for which CDN resources should be
              returned (ISO 8601/RFC 3339 format, UTC.)

          min_created: Earliest date of CDN resource creation for which CDN resources should be
              returned (ISO 8601/RFC 3339 format, UTC.)

          origin_group: Origin group ID.

          rules: Rule name or pattern.

          secondary_hostnames: Additional delivery domains (CNAMEs) of the CDN resource.

          shield_dc: Name of the origin shielding data center location.

          shielded: Defines whether origin shielding is enabled for the CDN resource.

              Possible values:

              - **true** - Origin shielding is enabled for the CDN resource.
              - **false** - Origin shielding is disabled for the CDN resource.

          ssl_data: SSL certificate ID.

          ssl_data_in: SSL certificates IDs.

              Example:

              - ?`sslData_in`=1643,1644,1652

          ssl_enabled: Defines whether the HTTPS protocol is enabled for content delivery.

              Possible values:

              - **true** - HTTPS protocol is enabled for CDN resource.
              - **false** - HTTPS protocol is disabled for CDN resource.

          status: CDN resource status.

          suspend: Defines whether the CDN resource was automatically suspended by the system.

              Possible values:

              - **true** - CDN resource is selected for automatic suspension in the next 7
                days.
              - **false** - CDN resource is not selected for automatic suspension.

          vp_enabled: Defines whether the CDN resource is integrated with the Streaming platform.

              Possible values:

              - **true** - CDN resource is used for Streaming platform.
              - **false** - CDN resource is not used for Streaming platform.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cdn/resources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cname": cname,
                        "deleted": deleted,
                        "enabled": enabled,
                        "max_created": max_created,
                        "min_created": min_created,
                        "origin_group": origin_group,
                        "rules": rules,
                        "secondary_hostnames": secondary_hostnames,
                        "shield_dc": shield_dc,
                        "shielded": shielded,
                        "ssl_data": ssl_data,
                        "ssl_data_in": ssl_data_in,
                        "ssl_enabled": ssl_enabled,
                        "status": status,
                        "suspend": suspend,
                        "vp_enabled": vp_enabled,
                    },
                    resource_list_params.ResourceListParams,
                ),
            ),
            cast_to=CdnResourceList,
        )

    async def delete(
        self,
        resource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the CDN resource from the system permanently.

        Notes:

        - **Deactivation Requirement**: Set the `active` attribute to `false` before
          deletion.
        - **Statistics Availability**: Statistics will be available for **365 days**
          after deletion through the
          [statistics endpoints](/docs/api-reference/cdn/cdn-statistics/cdn-resource-statistics).
        - **Irreversibility**: This action is irreversible. Once deleted, the CDN
          resource cannot be recovered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cdn/resources/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        resource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResource:
        """
        Get CDN resource details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cdn/resources/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResource,
        )

    async def prefetch(
        self,
        resource_id: int,
        *,
        paths: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Pre-populate files to a CDN cache before users requests.

        Prefetch is recommended
        only for files that **more than 200 MB** and **less than 5 GB**.

        You can make one prefetch request for a CDN resource per minute. One request for
        prefetch may content only up to 100 paths to files.

        The time of procedure depends on the number and size of the files.

        If you need to update files stored in the CDN, first purge these files and then
        prefetch.

        Args:
          paths: Paths to files that should be pre-populated to the CDN.

              Paths to the files should be specified without a domain name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cdn/resources/{resource_id}/prefetch",
            body=await async_maybe_transform({"paths": paths}, resource_prefetch_params.ResourcePrefetchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def prevalidate_ssl_le_certificate(
        self,
        resource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Check whether a Let's Encrypt certificate can be issued for the CDN resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cdn/resources/{resource_id}/ssl/le/pre-validate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    async def purge(
        self,
        resource_id: int,
        *,
        urls: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete cache from CDN servers.

        This is necessary to update CDN content.

        We have different limits for different purge types:

        - **Purge all cache** - One purge request for a CDN resource per minute.
        - **Purge by URL** - Two purge requests for a CDN resource per minute. One purge
          request is limited to 100 URLs.
        - **Purge by pattern** - One purge request for a CDN resource per minute. One
          purge request is limited to 10 patterns.

        Args:
          urls: **Purge by URL** clears the cache of a specific files. This purge type is
              recommended.

              Specify file URLs including query strings. URLs should start with / without a
              domain name.

              Purge by URL depends on the following CDN options:

              1. "vary response header" is used. If your origin serves variants of the same
                 content depending on the Vary HTTP response header, purge by URL will delete
                 only one version of the file.
              2. "slice" is used. If you update several files in the origin without clearing
                 the CDN cache, purge by URL will delete only the first slice (with bytes=0…
                 .)
              3. "ignoreQueryString" is used. Don’t specify parameters in the purge request.
              4. "`query_params_blacklist`" is used. Only files with the listed in the option
                 parameters will be cached as different objects. Files with other parameters
                 will be cached as one object. In this case, specify the listed parameters in
                 the Purge request. Don't specify other parameters.
              5. "`query_params_whitelist`" is used. Files with listed in the option
                 parameters will be cached as one object. Files with other parameters will be
                 cached as different objects. In this case, specify other parameters (if any)
                 besides the ones listed in the purge request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def purge(
        self,
        resource_id: int,
        *,
        paths: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete cache from CDN servers.

        This is necessary to update CDN content.

        We have different limits for different purge types:

        - **Purge all cache** - One purge request for a CDN resource per minute.
        - **Purge by URL** - Two purge requests for a CDN resource per minute. One purge
          request is limited to 100 URLs.
        - **Purge by pattern** - One purge request for a CDN resource per minute. One
          purge request is limited to 10 patterns.

        Args:
          paths: **Purge by pattern** clears the cache that matches the pattern.

              Use _ operator, which replaces any number of symbols in your path. It's
              important to note that wildcard usage (_) is permitted only at the end of a
              pattern.

              Query string added to any patterns will be ignored, and purge request will be
              processed as if there weren't any parameters.

              Purge by pattern is recursive. Both /path and /path* will result in recursive
              purging, meaning all content under the specified path will be affected. As such,
              using the pattern /path* is functionally equivalent to simply using /path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def purge(
        self,
        resource_id: int,
        *,
        paths: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete cache from CDN servers.

        This is necessary to update CDN content.

        We have different limits for different purge types:

        - **Purge all cache** - One purge request for a CDN resource per minute.
        - **Purge by URL** - Two purge requests for a CDN resource per minute. One purge
          request is limited to 100 URLs.
        - **Purge by pattern** - One purge request for a CDN resource per minute. One
          purge request is limited to 10 patterns.

        Args:
          paths: **Purge all cache** clears the entire cache for the CDN resource.

              Specify an empty array to purge all content for the resource.

              When you purge all assets, CDN servers request content from your origin server
              and cause a high load. Therefore, we recommend to use purge by URL for large
              content quantities.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def purge(
        self,
        resource_id: int,
        *,
        urls: SequenceNotStr[str] | Omit = omit,
        paths: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cdn/resources/{resource_id}/purge",
            body=await async_maybe_transform(
                {
                    "urls": urls,
                    "paths": paths,
                },
                resource_purge_params.ResourcePurgeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def replace(
        self,
        resource_id: int,
        *,
        origin_group: int,
        active: bool | Omit = omit,
        description: str | Omit = omit,
        name: Optional[str] | Omit = omit,
        options: resource_replace_params.Options | Omit = omit,
        origin_protocol: Literal["HTTP", "HTTPS", "MATCH"] | Omit = omit,
        proxy_ssl_ca: Optional[int] | Omit = omit,
        proxy_ssl_data: Optional[int] | Omit = omit,
        proxy_ssl_enabled: bool | Omit = omit,
        secondary_hostnames: SequenceNotStr[str] | Omit = omit,
        ssl_data: Optional[int] | Omit = omit,
        ssl_enabled: bool | Omit = omit,
        waap_api_domain_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResource:
        """
        Change CDN resource

        Args:
          origin_group: Origin group ID with which the CDN resource is associated.

              You can use either the `origin` or `originGroup` parameter in the request.

          active: Enables or disables a CDN resource.

              Possible values:

              - **true** - CDN resource is active. Content is being delivered.
              - **false** - CDN resource is deactivated. Content is not being delivered.

          description: Optional comment describing the CDN resource.

          name: CDN resource name.

          options: List of options that can be configured for the CDN resource.

              In case of `null` value the option is not added to the CDN resource. Option may
              inherit its value from the global account settings.

          origin_protocol: Protocol used by CDN servers to request content from an origin source.

              Possible values:

              - **HTTPS** - CDN servers will connect to the origin via HTTPS.
              - **HTTP** - CDN servers will connect to the origin via HTTP.
              - **MATCH** - connection protocol will be chosen automatically (content on the
                origin source should be available for the CDN both through HTTP and HTTPS).

              If protocol is not specified, HTTP is used to connect to an origin server.

          proxy_ssl_ca: ID of the trusted CA certificate used to verify an origin.

              It can be used only with `"proxy_ssl_enabled": true`.

          proxy_ssl_data: ID of the SSL certificate used to verify an origin.

              It can be used only with `"proxy_ssl_enabled": true`.

          proxy_ssl_enabled: Enables or disables SSL certificate validation of the origin server before
              completing any connection.

              Possible values:

              - **true** - Origin SSL certificate validation is enabled.
              - **false** - Origin SSL certificate validation is disabled.

          secondary_hostnames: Additional delivery domains (CNAMEs) that will be used to deliver content via
              the CDN.

              Up to ten additional CNAMEs are possible.

          ssl_data: ID of the SSL certificate linked to the CDN resource.

              Can be used only with `"sslEnabled": true`.

          ssl_enabled: Defines whether the HTTPS protocol enabled for content delivery.

              Possible values:

              - **true** - HTTPS is enabled.
              - **false** - HTTPS is disabled.

          waap_api_domain_enabled: Defines whether the associated WAAP Domain is identified as an API Domain.

              Possible values:

              - **true** - The associated WAAP Domain is designated as an API Domain.
              - **false** - The associated WAAP Domain is not designated as an API Domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/cdn/resources/{resource_id}",
            body=await async_maybe_transform(
                {
                    "origin_group": origin_group,
                    "active": active,
                    "description": description,
                    "name": name,
                    "options": options,
                    "origin_protocol": origin_protocol,
                    "proxy_ssl_ca": proxy_ssl_ca,
                    "proxy_ssl_data": proxy_ssl_data,
                    "proxy_ssl_enabled": proxy_ssl_enabled,
                    "secondary_hostnames": secondary_hostnames,
                    "ssl_data": ssl_data,
                    "ssl_enabled": ssl_enabled,
                    "waap_api_domain_enabled": waap_api_domain_enabled,
                },
                resource_replace_params.ResourceReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResource,
        )


class ResourcesResourceWithRawResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

        self.create = to_raw_response_wrapper(
            resources.create,
        )
        self.update = to_raw_response_wrapper(
            resources.update,
        )
        self.list = to_raw_response_wrapper(
            resources.list,
        )
        self.delete = to_raw_response_wrapper(
            resources.delete,
        )
        self.get = to_raw_response_wrapper(
            resources.get,
        )
        self.prefetch = to_raw_response_wrapper(
            resources.prefetch,
        )
        self.prevalidate_ssl_le_certificate = to_raw_response_wrapper(
            resources.prevalidate_ssl_le_certificate,
        )
        self.purge = to_raw_response_wrapper(
            resources.purge,
        )
        self.replace = to_raw_response_wrapper(
            resources.replace,
        )

    @cached_property
    def shield(self) -> ShieldResourceWithRawResponse:
        return ShieldResourceWithRawResponse(self._resources.shield)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._resources.rules)


class AsyncResourcesResourceWithRawResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

        self.create = async_to_raw_response_wrapper(
            resources.create,
        )
        self.update = async_to_raw_response_wrapper(
            resources.update,
        )
        self.list = async_to_raw_response_wrapper(
            resources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            resources.delete,
        )
        self.get = async_to_raw_response_wrapper(
            resources.get,
        )
        self.prefetch = async_to_raw_response_wrapper(
            resources.prefetch,
        )
        self.prevalidate_ssl_le_certificate = async_to_raw_response_wrapper(
            resources.prevalidate_ssl_le_certificate,
        )
        self.purge = async_to_raw_response_wrapper(
            resources.purge,
        )
        self.replace = async_to_raw_response_wrapper(
            resources.replace,
        )

    @cached_property
    def shield(self) -> AsyncShieldResourceWithRawResponse:
        return AsyncShieldResourceWithRawResponse(self._resources.shield)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._resources.rules)


class ResourcesResourceWithStreamingResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

        self.create = to_streamed_response_wrapper(
            resources.create,
        )
        self.update = to_streamed_response_wrapper(
            resources.update,
        )
        self.list = to_streamed_response_wrapper(
            resources.list,
        )
        self.delete = to_streamed_response_wrapper(
            resources.delete,
        )
        self.get = to_streamed_response_wrapper(
            resources.get,
        )
        self.prefetch = to_streamed_response_wrapper(
            resources.prefetch,
        )
        self.prevalidate_ssl_le_certificate = to_streamed_response_wrapper(
            resources.prevalidate_ssl_le_certificate,
        )
        self.purge = to_streamed_response_wrapper(
            resources.purge,
        )
        self.replace = to_streamed_response_wrapper(
            resources.replace,
        )

    @cached_property
    def shield(self) -> ShieldResourceWithStreamingResponse:
        return ShieldResourceWithStreamingResponse(self._resources.shield)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._resources.rules)


class AsyncResourcesResourceWithStreamingResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

        self.create = async_to_streamed_response_wrapper(
            resources.create,
        )
        self.update = async_to_streamed_response_wrapper(
            resources.update,
        )
        self.list = async_to_streamed_response_wrapper(
            resources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            resources.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            resources.get,
        )
        self.prefetch = async_to_streamed_response_wrapper(
            resources.prefetch,
        )
        self.prevalidate_ssl_le_certificate = async_to_streamed_response_wrapper(
            resources.prevalidate_ssl_le_certificate,
        )
        self.purge = async_to_streamed_response_wrapper(
            resources.purge,
        )
        self.replace = async_to_streamed_response_wrapper(
            resources.replace,
        )

    @cached_property
    def shield(self) -> AsyncShieldResourceWithStreamingResponse:
        return AsyncShieldResourceWithStreamingResponse(self._resources.shield)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._resources.rules)

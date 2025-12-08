# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "RuleTemplateUpdateParams",
    "Options",
    "OptionsAllowedHTTPMethods",
    "OptionsBotProtection",
    "OptionsBotProtectionBotChallenge",
    "OptionsBrotliCompression",
    "OptionsBrowserCacheSettings",
    "OptionsCacheHTTPHeaders",
    "OptionsCors",
    "OptionsCountryACL",
    "OptionsDisableCache",
    "OptionsDisableProxyForceRanges",
    "OptionsEdgeCacheSettings",
    "OptionsFastedge",
    "OptionsFastedgeOnRequestBody",
    "OptionsFastedgeOnRequestHeaders",
    "OptionsFastedgeOnResponseBody",
    "OptionsFastedgeOnResponseHeaders",
    "OptionsFetchCompressed",
    "OptionsFollowOriginRedirect",
    "OptionsForceReturn",
    "OptionsForceReturnTimeInterval",
    "OptionsForwardHostHeader",
    "OptionsGzipOn",
    "OptionsHostHeader",
    "OptionsIgnoreCookie",
    "OptionsIgnoreQueryString",
    "OptionsImageStack",
    "OptionsIPAddressACL",
    "OptionsLimitBandwidth",
    "OptionsProxyCacheKey",
    "OptionsProxyCacheMethodsSet",
    "OptionsProxyConnectTimeout",
    "OptionsProxyReadTimeout",
    "OptionsQueryParamsBlacklist",
    "OptionsQueryParamsWhitelist",
    "OptionsQueryStringForwarding",
    "OptionsRedirectHTTPToHTTPS",
    "OptionsRedirectHTTPSToHTTP",
    "OptionsReferrerACL",
    "OptionsRequestLimiter",
    "OptionsResponseHeadersHidingPolicy",
    "OptionsRewrite",
    "OptionsSecureKey",
    "OptionsSlice",
    "OptionsSni",
    "OptionsStale",
    "OptionsStaticResponseHeaders",
    "OptionsStaticResponseHeadersValue",
    "OptionsStaticHeaders",
    "OptionsStaticRequestHeaders",
    "OptionsUserAgentACL",
    "OptionsWaap",
    "OptionsWebsockets",
]


class RuleTemplateUpdateParams(TypedDict, total=False):
    name: str
    """Rule template name."""

    options: Options
    """List of options that can be configured for the rule.

    In case of `null` value the option is not added to the rule. Option inherits its
    value from the CDN resource settings.
    """

    override_origin_protocol: Annotated[
        Optional[Literal["HTTPS", "HTTP", "MATCH"]], PropertyInfo(alias="overrideOriginProtocol")
    ]
    """
    Sets a protocol other than the one specified in the CDN resource settings to
    connect to the origin.

    Possible values:

    - **HTTPS** - CDN servers connect to origin via HTTPS protocol.
    - **HTTP** - CDN servers connect to origin via HTTP protocol.
    - **MATCH** - Connection protocol is chosen automatically; in this case, content
      on origin source should be available for the CDN both through HTTP and HTTPS
      protocols.
    - **null** - `originProtocol` setting is inherited from the CDN resource
      settings.
    """

    rule: str
    """Path to the file or folder for which the rule will be applied.

    The rule is applied if the requested URI matches the rule path.

    We add a leading forward slash to any rule path. Specify a path without a
    forward slash.
    """

    rule_type: Annotated[int, PropertyInfo(alias="ruleType")]
    """Rule type.

    Possible values:

    - **Type 0** - Regular expression. Must start with '^/' or '/'.
    - **Type 1** - Regular expression. Note that for this rule type we automatically
      add / to each rule pattern before your regular expression. This type is
      **legacy**, please use Type 0.
    """

    weight: int
    """Rule execution order: from lowest (1) to highest.

    If requested URI matches multiple rules, the one higher in the order of the
    rules will be applied.
    """


class OptionsAllowedHTTPMethods(TypedDict, total=False):
    """HTTP methods allowed for content requests from the CDN."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[List[Literal["GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]]]


class OptionsBotProtectionBotChallenge(TypedDict, total=False):
    """Controls the bot challenge module state."""

    enabled: bool
    """Possible values:

    - **true** - Bot challenge is enabled.
    - **false** - Bot challenge is disabled.
    """


class OptionsBotProtection(TypedDict, total=False):
    """
    Allows to prevent online services from overloading and ensure your business workflow running smoothly.
    """

    bot_challenge: Required[OptionsBotProtectionBotChallenge]
    """Controls the bot challenge module state."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class OptionsBrotliCompression(TypedDict, total=False):
    """Compresses content with Brotli on the CDN side.

    CDN servers will request only uncompressed content from the origin.

    Notes:

    1. CDN only supports "Brotli compression" when the "origin shielding" feature is activated.
    2. If a precache server is not active for a CDN resource, no compression occurs, even if the option is enabled.
    3. `brotli_compression` is not supported with `fetch_compressed` or `slice` options enabled.
    4. `fetch_compressed` option in CDN resource settings overrides `brotli_compression` in rules. If you enabled `fetch_compressed` in CDN resource and want to enable `brotli_compression` in a rule, you must specify `fetch_compressed:false` in the rule.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[
        List[
            Literal[
                "application/javascript",
                "application/json",
                "application/vnd.ms-fontobject",
                "application/wasm",
                "application/x-font-ttf",
                "application/x-javascript",
                "application/xml",
                "application/xml+rss",
                "image/svg+xml",
                "image/x-icon",
                "text/css",
                "text/html",
                "text/javascript",
                "text/plain",
                "text/xml",
            ]
        ]
    ]
    """Allows to select the content types you want to compress.

    `text/html` is a mandatory content type.
    """


class OptionsBrowserCacheSettings(TypedDict, total=False):
    """Cache expiration time for users browsers in seconds.

    Cache expiration time is applied to the following response codes: 200, 201, 204, 206, 301, 302, 303, 304, 307, 308.

    Responses with other codes will not be cached.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[str]
    """Set the cache expiration time to '0s' to disable caching.

    The maximum duration is any equivalent to `1y`.
    """


class OptionsCacheHTTPHeaders(TypedDict, total=False):
    """**Legacy option**. Use the `response_headers_hiding_policy` option instead.

    HTTP Headers that must be included in the response.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[SequenceNotStr[str]]


class OptionsCors(TypedDict, total=False):
    """Enables or disables CORS (Cross-Origin Resource Sharing) header support.

    CORS header support allows the CDN to add the Access-Control-Allow-Origin header to a response to a browser.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[SequenceNotStr[str]]
    """Value of the Access-Control-Allow-Origin header.

    Possible values:

    - **Adds \\** as the Access-Control-Allow-Origin header value** - Content will be
      uploaded for requests from any domain. `"value": ["*"]`
    - **Adds "$`http_origin`" as the Access-Control-Allow-Origin header value if the
      origin matches one of the listed domains** - Content will be uploaded only for
      requests from the domains specified in the field.
      `"value": ["domain.com", "second.dom.com"]`
    - **Adds "$`http_origin`" as the Access-Control-Allow-Origin header value** -
      Content will be uploaded for requests from any domain, and the domain from
      which the request was sent will be added to the "Access-Control-Allow-Origin"
      header in the response. `"value": ["$http_origin"]`
    """

    always: bool
    """
    Defines whether the Access-Control-Allow-Origin header should be added to a
    response from CDN regardless of response code.

    Possible values:

    - **true** - Header will be added to a response regardless of response code.
    - **false** - Header will only be added to responses with codes: 200, 201, 204,
      206, 301, 302, 303, 304, 307, 308.
    """


class OptionsCountryACL(TypedDict, total=False):
    """Enables control access to content for specified countries."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    excepted_values: Required[SequenceNotStr[str]]
    """List of countries according to ISO-3166-1.

    The meaning of the parameter depends on `policy_type` value:

    - **allow** - List of countries for which access is prohibited.
    - **deny** - List of countries for which access is allowed.
    """

    policy_type: Required[Literal["allow", "deny"]]
    """Defines the type of CDN resource access policy.

    Possible values:

    - **allow** - Access is allowed for all the countries except for those specified
      in `excepted_values` field.
    - **deny** - Access is denied for all the countries except for those specified
      in `excepted_values` field.
    """


class OptionsDisableCache(TypedDict, total=False):
    """**Legacy option**. Use the `edge_cache_settings` option instead.

    Allows the complete disabling of content caching.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[bool]
    """Possible values:

    - **true** - content caching is disabled.
    - **false** - content caching is enabled.
    """


class OptionsDisableProxyForceRanges(TypedDict, total=False):
    """Allows 206 responses regardless of the settings of an origin source."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[bool]
    """Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class OptionsEdgeCacheSettings(TypedDict, total=False):
    """Cache expiration time for CDN servers.

    `value` and `default` fields cannot be used simultaneously.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    custom_values: Dict[str, str]
    """
    A MAP object representing the caching time in seconds for a response with a
    specific response code.

    These settings have a higher priority than the `value` field.

    - Use `any` key to specify caching time for all response codes.
    - Use `0s` value to disable caching for a specific response code.
    """

    default: str
    """Enables content caching according to the origin cache settings.

    The value is applied to the following response codes 200, 201, 204, 206, 301,
    302, 303, 304, 307, 308, if an origin server does not have caching HTTP headers.

    Responses with other codes will not be cached.

    The maximum duration is any equivalent to `1y`.
    """

    value: str
    """Caching time.

    The value is applied to the following response codes: 200, 206, 301, 302.
    Responses with codes 4xx, 5xx will not be cached.

    Use `0s` to disable caching.

    The maximum duration is any equivalent to `1y`.
    """


class OptionsFastedgeOnRequestBody(TypedDict, total=False):
    """
    Allows to configure FastEdge application that will be called to handle request body as soon as CDN receives incoming HTTP request.
    """

    app_id: Required[str]
    """The ID of the application in FastEdge."""

    enabled: bool
    """
    Determines if the FastEdge application should be called whenever HTTP request
    headers are received.
    """

    execute_on_edge: bool
    """Determines if the request should be executed at the edge nodes."""

    execute_on_shield: bool
    """Determines if the request should be executed at the shield nodes."""

    interrupt_on_error: bool
    """Determines if the request execution should be interrupted when an error occurs."""


class OptionsFastedgeOnRequestHeaders(TypedDict, total=False):
    """
    Allows to configure FastEdge application that will be called to handle request headers as soon as CDN receives incoming HTTP request.
    """

    app_id: Required[str]
    """The ID of the application in FastEdge."""

    enabled: bool
    """
    Determines if the FastEdge application should be called whenever HTTP request
    headers are received.
    """

    execute_on_edge: bool
    """Determines if the request should be executed at the edge nodes."""

    execute_on_shield: bool
    """Determines if the request should be executed at the shield nodes."""

    interrupt_on_error: bool
    """Determines if the request execution should be interrupted when an error occurs."""


class OptionsFastedgeOnResponseBody(TypedDict, total=False):
    """
    Allows to configure FastEdge application that will be called to handle response body before CDN sends the HTTP response.
    """

    app_id: Required[str]
    """The ID of the application in FastEdge."""

    enabled: bool
    """
    Determines if the FastEdge application should be called whenever HTTP request
    headers are received.
    """

    execute_on_edge: bool
    """Determines if the request should be executed at the edge nodes."""

    execute_on_shield: bool
    """Determines if the request should be executed at the shield nodes."""

    interrupt_on_error: bool
    """Determines if the request execution should be interrupted when an error occurs."""


class OptionsFastedgeOnResponseHeaders(TypedDict, total=False):
    """
    Allows to configure FastEdge application that will be called to handle response headers before CDN sends the HTTP response.
    """

    app_id: Required[str]
    """The ID of the application in FastEdge."""

    enabled: bool
    """
    Determines if the FastEdge application should be called whenever HTTP request
    headers are received.
    """

    execute_on_edge: bool
    """Determines if the request should be executed at the edge nodes."""

    execute_on_shield: bool
    """Determines if the request should be executed at the shield nodes."""

    interrupt_on_error: bool
    """Determines if the request execution should be interrupted when an error occurs."""


class OptionsFastedge(TypedDict, total=False):
    """
    Allows to configure FastEdge app to be called on different request/response phases.

    Note: At least one of `on_request_headers`, `on_request_body`, `on_response_headers`, or `on_response_body` must be specified.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    on_request_body: OptionsFastedgeOnRequestBody
    """
    Allows to configure FastEdge application that will be called to handle request
    body as soon as CDN receives incoming HTTP request.
    """

    on_request_headers: OptionsFastedgeOnRequestHeaders
    """
    Allows to configure FastEdge application that will be called to handle request
    headers as soon as CDN receives incoming HTTP request.
    """

    on_response_body: OptionsFastedgeOnResponseBody
    """
    Allows to configure FastEdge application that will be called to handle response
    body before CDN sends the HTTP response.
    """

    on_response_headers: OptionsFastedgeOnResponseHeaders
    """
    Allows to configure FastEdge application that will be called to handle response
    headers before CDN sends the HTTP response.
    """


class OptionsFetchCompressed(TypedDict, total=False):
    """Makes the CDN request compressed content from the origin.

    The origin server should support compression. CDN servers will not decompress your content even if a user browser does not accept compression.

    Notes:

    1. `fetch_compressed` is not supported with `gzipON` or `brotli_compression` or `slice` options enabled.
    2. `fetch_compressed` overrides `gzipON` and `brotli_compression` in rule. If you enable it in CDN resource and want to use `gzipON` and `brotli_compression` in a rule, you have to specify `"fetch_compressed": false` in the rule.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[bool]
    """Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class OptionsFollowOriginRedirect(TypedDict, total=False):
    """
    Enables redirection from origin.
    If the origin server returns a redirect, the option allows the CDN to pull the requested content from the origin server that was returned in the redirect.
    """

    codes: Required[Iterable[Literal[301, 302, 303, 307, 308]]]
    """Redirect status code that the origin server returns.

    To serve up to date content to end users, you will need to purge the cache after
    managing the option.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class OptionsForceReturnTimeInterval(TypedDict, total=False):
    """Controls the time at which a custom HTTP response code should be applied.

    By default, a custom HTTP response code is applied at any time.
    """

    end_time: Required[str]
    """Time until which a custom HTTP response code should be applied.

    Indicated in 24-hour format.
    """

    start_time: Required[str]
    """Time from which a custom HTTP response code should be applied.

    Indicated in 24-hour format.
    """

    time_zone: str
    """Time zone used to calculate time."""


class OptionsForceReturn(TypedDict, total=False):
    """Applies custom HTTP response codes for CDN content.

    The following codes are reserved by our system and cannot be specified in this option: 408, 444, 477, 494, 495, 496, 497, 499.
    """

    body: Required[str]
    """URL for redirection or text."""

    code: Required[int]
    """Status code value."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    time_interval: Optional[OptionsForceReturnTimeInterval]
    """Controls the time at which a custom HTTP response code should be applied.

    By default, a custom HTTP response code is applied at any time.
    """


class OptionsForwardHostHeader(TypedDict, total=False):
    """Forwards the Host header from a end-user request to an origin server.

    `hostHeader` and `forward_host_header` options cannot be enabled simultaneously.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[bool]
    """Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class OptionsGzipOn(TypedDict, total=False):
    """Compresses content with gzip on the CDN end.

    CDN servers will request only uncompressed content from the origin.

    Notes:

    1. Compression with gzip is not supported with `fetch_compressed` or `slice` options enabled.
    2. `fetch_compressed` option in CDN resource settings overrides `gzipON` in rules. If you enable `fetch_compressed` in CDN resource and want to enable `gzipON` in rules, you need to specify `"fetch_compressed":false` for rules.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[bool]
    """Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class OptionsHostHeader(TypedDict, total=False):
    """
    Sets the Host header that CDN servers use when request content from an origin server.
    Your server must be able to process requests with the chosen header.

    If the option is `null`, the Host Header value is equal to first CNAME.

    `hostHeader` and `forward_host_header` options cannot be enabled simultaneously.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[str]
    """Host Header value."""


class OptionsIgnoreCookie(TypedDict, total=False):
    """
    Defines whether the files with the Set-Cookies header are cached as one file or as different ones.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[bool]
    """Possible values:

    - **true** - Option is enabled, files with cookies are cached as one file.
    - **false** - Option is disabled, files with cookies are cached as different
      files.
    """


class OptionsIgnoreQueryString(TypedDict, total=False):
    """
    How a file with different query strings is cached: either as one object (option is enabled) or as different objects (option is disabled.)

    `ignoreQueryString`, `query_params_whitelist` and `query_params_blacklist` options cannot be enabled simultaneously.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[bool]
    """Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class OptionsImageStack(TypedDict, total=False):
    """
    Transforms JPG and PNG images (for example, resize or crop) and automatically converts them to WebP or AVIF format.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    avif_enabled: bool
    """Enables or disables automatic conversion of JPEG and PNG images to AVI format."""

    png_lossless: bool
    """Enables or disables compression without quality loss for PNG format."""

    quality: int
    """Defines quality settings for JPG and PNG images.

    The higher the value, the better the image quality, and the larger the file size
    after conversion.
    """

    webp_enabled: bool
    """Enables or disables automatic conversion of JPEG and PNG images to WebP format."""


class OptionsIPAddressACL(TypedDict, total=False):
    """Controls access to the CDN resource content for specific IP addresses.

    If you want to use IPs from our CDN servers IP list for IP ACL configuration, you have to independently monitor their relevance.
    We recommend you use a script for automatically update IP ACL. [Read more.](/docs/api-reference/cdn/ip-addresses-list/get-cdn-servers-ip-addresses)
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    excepted_values: Required[SequenceNotStr[str]]
    """List of IP addresses with a subnet mask.

    The meaning of the parameter depends on `policy_type` value:

    - **allow** - List of IP addresses for which access is prohibited.
    - **deny** - List of IP addresses for which access is allowed.

    Examples:

    - `192.168.3.2/32`
    - `2a03:d000:2980:7::8/128`
    """

    policy_type: Required[Literal["allow", "deny"]]
    """IP access policy type.

    Possible values:

    - **allow** - Allow access to all IPs except IPs specified in
      "`excepted_values`" field.
    - **deny** - Deny access to all IPs except IPs specified in "`excepted_values`"
      field.
    """


class OptionsLimitBandwidth(TypedDict, total=False):
    """Allows to control the download speed per connection."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    limit_type: Required[Literal["static", "dynamic"]]
    """Method of controlling the download speed per connection.

    Possible values:

    - **static** - Use speed and buffer fields to set the download speed limit.
    - **dynamic** - Use query strings **speed** and **buffer** to set the download
      speed limit.

    For example, when requesting content at the link

    ```
    http://cdn.example.com/video.mp4?speed=50k&buffer=500k
    ```

    the download speed will be limited to 50kB/s after 500 kB.
    """

    buffer: int
    """Amount of downloaded data after which the user will be rate limited."""

    speed: int
    """Maximum download speed per connection."""


class OptionsProxyCacheKey(TypedDict, total=False):
    """Allows you to modify your cache key.

    If omitted, the default value is `$request_uri`.

    Combine the specified variables to create a key for caching.
    - **$`request_uri`**
    - **$scheme**
    - **$uri**

    **Warning**: Enabling and changing this option can invalidate your current cache and affect the cache hit ratio. Furthermore, the "Purge by pattern" option will not work.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[str]
    """Key for caching."""


class OptionsProxyCacheMethodsSet(TypedDict, total=False):
    """Caching for POST requests along with default GET and HEAD."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[bool]
    """Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class OptionsProxyConnectTimeout(TypedDict, total=False):
    """The time limit for establishing a connection with the origin."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[str]
    """Timeout value in seconds.

    Supported range: **1s - 5s**.
    """


class OptionsProxyReadTimeout(TypedDict, total=False):
    """
    The time limit for receiving a partial response from the origin.
    If no response is received within this time, the connection will be closed.

    **Note:**
    When used with a WebSocket connection, this option supports values only in the range 1–20 seconds (instead of the usual 1–30 seconds).
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[str]
    """Timeout value in seconds.

    Supported range: **1s - 30s**.
    """


class OptionsQueryParamsBlacklist(TypedDict, total=False):
    """
    Files with the specified query parameters are cached as one object, files with other parameters are cached as different objects.

    `ignoreQueryString`, `query_params_whitelist` and `query_params_blacklist` options cannot be enabled simultaneously.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[SequenceNotStr[str]]
    """List of query parameters."""


class OptionsQueryParamsWhitelist(TypedDict, total=False):
    """
    Files with the specified query parameters are cached as different objects, files with other parameters are cached as one object.

    `ignoreQueryString`, `query_params_whitelist` and `query_params_blacklist` options cannot be enabled simultaneously.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[SequenceNotStr[str]]
    """List of query parameters."""


class OptionsQueryStringForwarding(TypedDict, total=False):
    """
    The Query String Forwarding feature allows for the seamless transfer of parameters embedded in playlist files to the corresponding media chunk files.
    This functionality ensures that specific attributes, such as authentication tokens or tracking information, are consistently passed along from the playlist manifest to the individual media segments.
    This is particularly useful for maintaining continuity in security, analytics, and any other parameter-based operations across the entire media delivery workflow.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    forward_from_file_types: Required[SequenceNotStr[str]]
    """
    The `forward_from_files_types` field specifies the types of playlist files from
    which parameters will be extracted and forwarded. This typically includes
    formats that list multiple media chunk references, such as HLS and DASH
    playlists. Parameters associated with these playlist files (like query strings
    or headers) will be propagated to the chunks they reference.
    """

    forward_to_file_types: Required[SequenceNotStr[str]]
    """
    The field specifies the types of media chunk files to which parameters,
    extracted from playlist files, will be forwarded. These refer to the actual
    segments of media content that are delivered to viewers. Ensuring the correct
    parameters are forwarded to these files is crucial for maintaining the integrity
    of the streaming session.
    """

    forward_except_keys: SequenceNotStr[str]
    """
    The `forward_except_keys` field provides a mechanism to exclude specific
    parameters from being forwarded from playlist files to media chunk files. By
    listing certain keys in this field, you can ensure that these parameters are
    omitted during the forwarding process. This is particularly useful for
    preventing sensitive or irrelevant information from being included in requests
    for media chunks, thereby enhancing security and optimizing performance.
    """

    forward_only_keys: SequenceNotStr[str]
    """
    The `forward_only_keys` field allows for granular control over which specific
    parameters are forwarded from playlist files to media chunk files. By specifying
    certain keys, only those parameters will be propagated, ensuring that only
    relevant information is passed along. This is particularly useful for security
    and performance optimization, as it prevents unnecessary or sensitive data from
    being included in requests for media chunks.
    """


class OptionsRedirectHTTPToHTTPS(TypedDict, total=False):
    """Enables redirect from HTTP to HTTPS.

    `redirect_http_to_https` and `redirect_https_to_http` options cannot be enabled simultaneously.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[bool]
    """Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class OptionsRedirectHTTPSToHTTP(TypedDict, total=False):
    """Enables redirect from HTTPS to HTTP.

    `redirect_http_to_https` and `redirect_https_to_http` options cannot be enabled simultaneously.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[bool]
    """Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class OptionsReferrerACL(TypedDict, total=False):
    """Controls access to the CDN resource content for specified domain names."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    excepted_values: Required[SequenceNotStr[str]]
    """
    List of domain names or wildcard domains (without protocol: `http://` or
    `https://`.)

    The meaning of the parameter depends on `policy_type` value:

    - **allow** - List of domain names for which access is prohibited.
    - **deny** - List of IP domain names for which access is allowed.

    Examples:

    - `example.com`
    - `*.example.com`
    """

    policy_type: Required[Literal["allow", "deny"]]
    """Policy type.

    Possible values:

    - **allow** - Allow access to all domain names except the domain names specified
      in `excepted_values` field.
    - **deny** - Deny access to all domain names except the domain names specified
      in `excepted_values` field.
    """


class OptionsRequestLimiter(TypedDict, total=False):
    """Option allows to limit the amount of HTTP requests."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    rate: Required[int]
    """Maximum request rate."""

    rate_unit: Literal["r/s", "r/m"]
    """Units of measurement for the `rate` field.

    Possible values:

    - **r/s** - Requests per second.
    - **r/m** - Requests per minute.

    If the rate is less than one request per second, it is specified in request per
    minute (r/m.)
    """


class OptionsResponseHeadersHidingPolicy(TypedDict, total=False):
    """Hides HTTP headers from an origin server in the CDN response."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    excepted: Required[SequenceNotStr[str]]
    """List of HTTP headers.

    Parameter meaning depends on the value of the `mode` field:

    - **show** - List of HTTP headers to hide from response.
    - **hide** - List of HTTP headers to include in response. Other HTTP headers
      will be hidden.

    The following headers are required and cannot be hidden from response:

    - `Connection`
    - `Content-Length`
    - `Content-Type`
    - `Date`
    - `Server`
    """

    mode: Required[Literal["hide", "show"]]
    """How HTTP headers are hidden from the response.

    Possible values:

    - **show** - Hide only HTTP headers listed in the `excepted` field.
    - **hide** - Hide all HTTP headers except headers listed in the "excepted"
      field.
    """


class OptionsRewrite(TypedDict, total=False):
    """Changes and redirects requests from the CDN to the origin.

    It operates according to the [Nginx](https://nginx.org/en/docs/http/ngx_http_rewrite_module.html#rewrite) configuration.
    """

    body: Required[str]
    """Path for the Rewrite option.

    Example:

    - `/(.*) /media/$1`
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    flag: Literal["break", "last", "redirect", "permanent"]
    """Flag for the Rewrite option.

    Possible values:

    - **last** - Stop processing the current set of `ngx_http_rewrite_module`
      directives and start a search for a new location matching changed URI.
    - **break** - Stop processing the current set of the Rewrite option.
    - **redirect** - Return a temporary redirect with the 302 code; used when a
      replacement string does not start with `http://`, `https://`, or `$scheme`.
    - **permanent** - Return a permanent redirect with the 301 code.
    """


class OptionsSecureKey(TypedDict, total=False):
    """Configures access with tokenized URLs.

    This makes impossible to access content without a valid (unexpired) token.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    key: Required[Optional[str]]
    """Key generated on your side that will be used for URL signing."""

    type: Literal[0, 2]
    """Type of URL signing.

    Possible types:

    - **Type 0** - Includes end user IP to secure token generation.
    - **Type 2** - Excludes end user IP from secure token generation.
    """


class OptionsSlice(TypedDict, total=False):
    """
    Requests and caches files larger than 10 MB in parts (no larger than 10 MB per part.) This reduces time to first byte.

    The option is based on the [Slice](https://nginx.org/en/docs/http/ngx_http_slice_module.html) module.

    Notes:

    1. Origin must support HTTP Range requests.
    2. Not supported with `gzipON`, `brotli_compression` or `fetch_compressed` options enabled.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[bool]
    """Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class OptionsSni(TypedDict, total=False):
    """
    The hostname that is added to SNI requests from CDN servers to the origin server via HTTPS.

    SNI is generally only required if your origin uses shared hosting or does not have a dedicated IP address.
    If the origin server presents multiple certificates, SNI allows the origin server to know which certificate to use for the connection.

    The option works only if `originProtocol` parameter is `HTTPS` or `MATCH`.
    """

    custom_hostname: Required[str]
    """Custom SNI hostname.

    It is required if `sni_type` is set to custom.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    sni_type: Literal["dynamic", "custom"]
    """SNI (Server Name Indication) type.

    Possible values:

    - **dynamic** - SNI hostname depends on `hostHeader` and `forward_host_header`
      options. It has several possible combinations:
    - If the `hostHeader` option is enabled and specified, SNI hostname matches the
      Host header.
    - If the `forward_host_header` option is enabled and has true value, SNI
      hostname matches the Host header used in the request made to a CDN.
    - If the `hostHeader` and `forward_host_header` options are disabled, SNI
      hostname matches the primary CNAME.
    - **custom** - custom SNI hostname is in use.
    """


class OptionsStale(TypedDict, total=False):
    """Serves stale cached content in case of origin unavailability."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[
        List[
            Literal[
                "error",
                "http_403",
                "http_404",
                "http_429",
                "http_500",
                "http_502",
                "http_503",
                "http_504",
                "invalid_header",
                "timeout",
                "updating",
            ]
        ]
    ]
    """Defines list of errors for which "Always online" option is applied."""


class OptionsStaticResponseHeadersValue(TypedDict, total=False):
    name: Required[str]
    """HTTP Header name.

    Restrictions:

    - Maximum 128 symbols.
    - Latin letters (A-Z, a-z,) numbers (0-9,) dashes, and underscores only.
    """

    value: Required[SequenceNotStr[str]]
    """Header value.

    Restrictions:

    - Maximum 512 symbols.
    - Letters (a-z), numbers (0-9), spaces, and symbols (`~!@#%%^&\\**()-\\__=+
      /|\";:?.,><{}[]).
    - Must start with a letter, number, asterisk or {.
    - Multiple values can be added.
    """

    always: bool
    """
    Defines whether the header will be added to a response from CDN regardless of
    response code.

    Possible values:

    - **true** - Header will be added to a response from CDN regardless of response
      code.
    - **false** - Header will be added only to the following response codes: 200,
      201, 204, 206, 301, 302, 303, 304, 307, 308.
    """


class OptionsStaticResponseHeaders(TypedDict, total=False):
    """Custom HTTP Headers that a CDN server adds to a response."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[Iterable[OptionsStaticResponseHeadersValue]]


class OptionsStaticHeaders(TypedDict, total=False):
    """**Legacy option**. Use the `static_response_headers` option instead.

    Custom HTTP Headers that a CDN server adds to response. Up to fifty custom HTTP Headers can be specified. May contain a header with multiple values.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[object]
    """A MAP for static headers in a format of `header_name: header_value`.

    Restrictions:

    - **Header name** - Maximum 128 symbols, may contain Latin letters (A-Z, a-z),
      numbers (0-9), dashes, and underscores.
    - **Header value** - Maximum 512 symbols, may contain letters (a-z), numbers
      (0-9), spaces, and symbols (`~!@#%%^&\\**()-\\__=+ /|\";:?.,><{}[]). Must start
      with a letter, number, asterisk or {.
    """


class OptionsStaticRequestHeaders(TypedDict, total=False):
    """Custom HTTP Headers for a CDN server to add to request.

    Up to fifty custom HTTP Headers can be specified.
    """

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[Dict[str, str]]
    """A MAP for static headers in a format of `header_name: header_value`.

    Restrictions:

    - **Header name** - Maximum 255 symbols, may contain Latin letters (A-Z, a-z),
      numbers (0-9), dashes, and underscores.
    - **Header value** - Maximum 512 symbols, may contain letters (a-z), numbers
      (0-9), spaces, and symbols (`~!@#%%^&\\**()-\\__=+ /|\";:?.,><{}[]). Must start
      with a letter, number, asterisk or {.
    """


class OptionsUserAgentACL(TypedDict, total=False):
    """Controls access to the content for specified User-Agents."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    excepted_values: Required[SequenceNotStr[str]]
    """List of User-Agents that will be allowed/denied.

    The meaning of the parameter depends on `policy_type`:

    - **allow** - List of User-Agents for which access is prohibited.
    - **deny** - List of User-Agents for which access is allowed.

    Use an empty string `""` to allow/deny access when the User-Agent header is
    empty.
    """

    policy_type: Required[Literal["allow", "deny"]]
    """User-Agents policy type.

    Possible values:

    - **allow** - Allow access for all User-Agents except specified in
      `excepted_values` field.
    - **deny** - Deny access for all User-Agents except specified in
      `excepted_values` field.
    """


class OptionsWaap(TypedDict, total=False):
    """Allows to enable WAAP (Web Application and API Protection)."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[bool]
    """Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class OptionsWebsockets(TypedDict, total=False):
    """Enables or disables WebSockets connections to an origin server."""

    enabled: Required[bool]
    """Controls the option state.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """

    value: Required[bool]
    """Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class Options(TypedDict, total=False):
    """List of options that can be configured for the rule.

    In case of `null` value the option is not added to the rule.
    Option inherits its value from the CDN resource settings.
    """

    allowed_http_methods: Annotated[Optional[OptionsAllowedHTTPMethods], PropertyInfo(alias="allowedHttpMethods")]
    """HTTP methods allowed for content requests from the CDN."""

    bot_protection: Optional[OptionsBotProtection]
    """
    Allows to prevent online services from overloading and ensure your business
    workflow running smoothly.
    """

    brotli_compression: Optional[OptionsBrotliCompression]
    """Compresses content with Brotli on the CDN side.

    CDN servers will request only uncompressed content from the origin.

    Notes:

    1. CDN only supports "Brotli compression" when the "origin shielding" feature is
       activated.
    2. If a precache server is not active for a CDN resource, no compression occurs,
       even if the option is enabled.
    3. `brotli_compression` is not supported with `fetch_compressed` or `slice`
       options enabled.
    4. `fetch_compressed` option in CDN resource settings overrides
       `brotli_compression` in rules. If you enabled `fetch_compressed` in CDN
       resource and want to enable `brotli_compression` in a rule, you must specify
       `fetch_compressed:false` in the rule.
    """

    browser_cache_settings: Optional[OptionsBrowserCacheSettings]
    """Cache expiration time for users browsers in seconds.

    Cache expiration time is applied to the following response codes: 200, 201, 204,
    206, 301, 302, 303, 304, 307, 308.

    Responses with other codes will not be cached.
    """

    cache_http_headers: Optional[OptionsCacheHTTPHeaders]
    """**Legacy option**. Use the `response_headers_hiding_policy` option instead.

    HTTP Headers that must be included in the response.
    """

    cors: Optional[OptionsCors]
    """Enables or disables CORS (Cross-Origin Resource Sharing) header support.

    CORS header support allows the CDN to add the Access-Control-Allow-Origin header
    to a response to a browser.
    """

    country_acl: Optional[OptionsCountryACL]
    """Enables control access to content for specified countries."""

    disable_cache: Optional[OptionsDisableCache]
    """**Legacy option**. Use the `edge_cache_settings` option instead.

    Allows the complete disabling of content caching.
    """

    disable_proxy_force_ranges: Optional[OptionsDisableProxyForceRanges]
    """Allows 206 responses regardless of the settings of an origin source."""

    edge_cache_settings: Optional[OptionsEdgeCacheSettings]
    """Cache expiration time for CDN servers.

    `value` and `default` fields cannot be used simultaneously.
    """

    fastedge: Optional[OptionsFastedge]
    """
    Allows to configure FastEdge app to be called on different request/response
    phases.

    Note: At least one of `on_request_headers`, `on_request_body`,
    `on_response_headers`, or `on_response_body` must be specified.
    """

    fetch_compressed: Optional[OptionsFetchCompressed]
    """Makes the CDN request compressed content from the origin.

    The origin server should support compression. CDN servers will not decompress
    your content even if a user browser does not accept compression.

    Notes:

    1. `fetch_compressed` is not supported with `gzipON` or `brotli_compression` or
       `slice` options enabled.
    2. `fetch_compressed` overrides `gzipON` and `brotli_compression` in rule. If
       you enable it in CDN resource and want to use `gzipON` and
       `brotli_compression` in a rule, you have to specify
       `"fetch_compressed": false` in the rule.
    """

    follow_origin_redirect: Optional[OptionsFollowOriginRedirect]
    """
    Enables redirection from origin. If the origin server returns a redirect, the
    option allows the CDN to pull the requested content from the origin server that
    was returned in the redirect.
    """

    force_return: Optional[OptionsForceReturn]
    """Applies custom HTTP response codes for CDN content.

    The following codes are reserved by our system and cannot be specified in this
    option: 408, 444, 477, 494, 495, 496, 497, 499.
    """

    forward_host_header: Optional[OptionsForwardHostHeader]
    """Forwards the Host header from a end-user request to an origin server.

    `hostHeader` and `forward_host_header` options cannot be enabled simultaneously.
    """

    gzip_on: Annotated[Optional[OptionsGzipOn], PropertyInfo(alias="gzipOn")]
    """Compresses content with gzip on the CDN end.

    CDN servers will request only uncompressed content from the origin.

    Notes:

    1. Compression with gzip is not supported with `fetch_compressed` or `slice`
       options enabled.
    2. `fetch_compressed` option in CDN resource settings overrides `gzipON` in
       rules. If you enable `fetch_compressed` in CDN resource and want to enable
       `gzipON` in rules, you need to specify `"fetch_compressed":false` for rules.
    """

    host_header: Annotated[Optional[OptionsHostHeader], PropertyInfo(alias="hostHeader")]
    """
    Sets the Host header that CDN servers use when request content from an origin
    server. Your server must be able to process requests with the chosen header.

    If the option is `null`, the Host Header value is equal to first CNAME.

    `hostHeader` and `forward_host_header` options cannot be enabled simultaneously.
    """

    ignore_cookie: Optional[OptionsIgnoreCookie]
    """
    Defines whether the files with the Set-Cookies header are cached as one file or
    as different ones.
    """

    ignore_query_string: Annotated[Optional[OptionsIgnoreQueryString], PropertyInfo(alias="ignoreQueryString")]
    """
    How a file with different query strings is cached: either as one object (option
    is enabled) or as different objects (option is disabled.)

    `ignoreQueryString`, `query_params_whitelist` and `query_params_blacklist`
    options cannot be enabled simultaneously.
    """

    image_stack: Optional[OptionsImageStack]
    """
    Transforms JPG and PNG images (for example, resize or crop) and automatically
    converts them to WebP or AVIF format.
    """

    ip_address_acl: Optional[OptionsIPAddressACL]
    """Controls access to the CDN resource content for specific IP addresses.

    If you want to use IPs from our CDN servers IP list for IP ACL configuration,
    you have to independently monitor their relevance. We recommend you use a script
    for automatically update IP ACL.
    [Read more.](/docs/api-reference/cdn/ip-addresses-list/get-cdn-servers-ip-addresses)
    """

    limit_bandwidth: Optional[OptionsLimitBandwidth]
    """Allows to control the download speed per connection."""

    proxy_cache_key: Optional[OptionsProxyCacheKey]
    """Allows you to modify your cache key.

    If omitted, the default value is `$request_uri`.

    Combine the specified variables to create a key for caching.

    - **$`request_uri`**
    - **$scheme**
    - **$uri**

    **Warning**: Enabling and changing this option can invalidate your current cache
    and affect the cache hit ratio. Furthermore, the "Purge by pattern" option will
    not work.
    """

    proxy_cache_methods_set: Optional[OptionsProxyCacheMethodsSet]
    """Caching for POST requests along with default GET and HEAD."""

    proxy_connect_timeout: Optional[OptionsProxyConnectTimeout]
    """The time limit for establishing a connection with the origin."""

    proxy_read_timeout: Optional[OptionsProxyReadTimeout]
    """
    The time limit for receiving a partial response from the origin. If no response
    is received within this time, the connection will be closed.

    **Note:** When used with a WebSocket connection, this option supports values
    only in the range 1–20 seconds (instead of the usual 1–30 seconds).
    """

    query_params_blacklist: Optional[OptionsQueryParamsBlacklist]
    """
    Files with the specified query parameters are cached as one object, files with
    other parameters are cached as different objects.

    `ignoreQueryString`, `query_params_whitelist` and `query_params_blacklist`
    options cannot be enabled simultaneously.
    """

    query_params_whitelist: Optional[OptionsQueryParamsWhitelist]
    """
    Files with the specified query parameters are cached as different objects, files
    with other parameters are cached as one object.

    `ignoreQueryString`, `query_params_whitelist` and `query_params_blacklist`
    options cannot be enabled simultaneously.
    """

    query_string_forwarding: Optional[OptionsQueryStringForwarding]
    """
    The Query String Forwarding feature allows for the seamless transfer of
    parameters embedded in playlist files to the corresponding media chunk files.
    This functionality ensures that specific attributes, such as authentication
    tokens or tracking information, are consistently passed along from the playlist
    manifest to the individual media segments. This is particularly useful for
    maintaining continuity in security, analytics, and any other parameter-based
    operations across the entire media delivery workflow.
    """

    redirect_http_to_https: Optional[OptionsRedirectHTTPToHTTPS]
    """Enables redirect from HTTP to HTTPS.

    `redirect_http_to_https` and `redirect_https_to_http` options cannot be enabled
    simultaneously.
    """

    redirect_https_to_http: Optional[OptionsRedirectHTTPSToHTTP]
    """Enables redirect from HTTPS to HTTP.

    `redirect_http_to_https` and `redirect_https_to_http` options cannot be enabled
    simultaneously.
    """

    referrer_acl: Optional[OptionsReferrerACL]
    """Controls access to the CDN resource content for specified domain names."""

    request_limiter: Optional[OptionsRequestLimiter]
    """Option allows to limit the amount of HTTP requests."""

    response_headers_hiding_policy: Optional[OptionsResponseHeadersHidingPolicy]
    """Hides HTTP headers from an origin server in the CDN response."""

    rewrite: Optional[OptionsRewrite]
    """Changes and redirects requests from the CDN to the origin.

    It operates according to the
    [Nginx](https://nginx.org/en/docs/http/ngx_http_rewrite_module.html#rewrite)
    configuration.
    """

    secure_key: Optional[OptionsSecureKey]
    """Configures access with tokenized URLs.

    This makes impossible to access content without a valid (unexpired) token.
    """

    slice: Optional[OptionsSlice]
    """
    Requests and caches files larger than 10 MB in parts (no larger than 10 MB per
    part.) This reduces time to first byte.

    The option is based on the
    [Slice](https://nginx.org/en/docs/http/ngx_http_slice_module.html) module.

    Notes:

    1. Origin must support HTTP Range requests.
    2. Not supported with `gzipON`, `brotli_compression` or `fetch_compressed`
       options enabled.
    """

    sni: Optional[OptionsSni]
    """
    The hostname that is added to SNI requests from CDN servers to the origin server
    via HTTPS.

    SNI is generally only required if your origin uses shared hosting or does not
    have a dedicated IP address. If the origin server presents multiple
    certificates, SNI allows the origin server to know which certificate to use for
    the connection.

    The option works only if `originProtocol` parameter is `HTTPS` or `MATCH`.
    """

    stale: Optional[OptionsStale]
    """Serves stale cached content in case of origin unavailability."""

    static_response_headers: Optional[OptionsStaticResponseHeaders]
    """Custom HTTP Headers that a CDN server adds to a response."""

    static_headers: Annotated[Optional[OptionsStaticHeaders], PropertyInfo(alias="staticHeaders")]
    """**Legacy option**. Use the `static_response_headers` option instead.

    Custom HTTP Headers that a CDN server adds to response. Up to fifty custom HTTP
    Headers can be specified. May contain a header with multiple values.
    """

    static_request_headers: Annotated[Optional[OptionsStaticRequestHeaders], PropertyInfo(alias="staticRequestHeaders")]
    """Custom HTTP Headers for a CDN server to add to request.

    Up to fifty custom HTTP Headers can be specified.
    """

    user_agent_acl: Optional[OptionsUserAgentACL]
    """Controls access to the content for specified User-Agents."""

    waap: Optional[OptionsWaap]
    """Allows to enable WAAP (Web Application and API Protection)."""

    websockets: Optional[OptionsWebsockets]
    """Enables or disables WebSockets connections to an origin server."""

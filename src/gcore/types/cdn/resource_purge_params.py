# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ResourcePurgeParams", "PurgeByURL", "PurgeByPattern", "PurgeAllCache"]


class PurgeByURL(TypedDict, total=False):
    urls: SequenceNotStr[str]
    """**Purge by URL** clears the cache of a specific files.

    This purge type is recommended.

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
    """


class PurgeByPattern(TypedDict, total=False):
    paths: SequenceNotStr[str]
    """**Purge by pattern** clears the cache that matches the pattern.

    Use _ operator, which replaces any number of symbols in your path. It's
    important to note that wildcard usage (_) is permitted only at the end of a
    pattern.

    Query string added to any patterns will be ignored, and purge request will be
    processed as if there weren't any parameters.

    Purge by pattern is recursive. Both /path and /path* will result in recursive
    purging, meaning all content under the specified path will be affected. As such,
    using the pattern /path* is functionally equivalent to simply using /path.
    """


class PurgeAllCache(TypedDict, total=False):
    paths: SequenceNotStr[str]
    """**Purge all cache** clears the entire cache for the CDN resource.

    Specify an empty array to purge all content for the resource.

    When you purge all assets, CDN servers request content from your origin server
    and cause a high load. Therefore, we recommend to use purge by URL for large
    content quantities.
    """


ResourcePurgeParams: TypeAlias = Union[PurgeByURL, PurgeByPattern, PurgeAllCache]

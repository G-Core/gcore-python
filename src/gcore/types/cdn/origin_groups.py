# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["OriginGroups", "NoneAuth", "NoneAuthSource", "AwsSignatureV4", "AwsSignatureV4Auth"]


class NoneAuthSource(BaseModel):
    backup: Optional[bool] = None
    """
    Defines whether the origin is a backup, meaning that it will not be used until
    one of active origins become unavailable.

    Possible values:

    - **true** - Origin is a backup.
    - **false** - Origin is not a backup.
    """

    enabled: Optional[bool] = None
    """Enables or disables an origin source in the origin group.

    Possible values:

    - **true** - Origin is enabled and the CDN uses it to pull content.
    - **false** - Origin is disabled and the CDN does not use it to pull content.

    Origin group must contain at least one enabled origin.
    """

    source: Optional[str] = None
    """IP address or domain name of the origin and the port, if custom port is used."""


class NoneAuth(BaseModel):
    id: Optional[int] = None
    """Origin group ID."""

    auth_type: Optional[str] = None
    """Origin authentication type.

    Possible values:

    - **none** - Used for public origins.
    - **awsSignatureV4** - Used for S3 storage.
    """

    has_related_resources: Optional[bool] = None
    """Defines whether the origin group has related CDN resources.

    Possible values:

    - **true** - Origin group has related CDN resources.
    - **false** - Origin group does not have related CDN resources.
    """

    name: Optional[str] = None
    """Origin group name."""

    path: Optional[str] = None
    """Parameter is **deprecated**."""

    proxy_next_upstream: Optional[List[str]] = None
    """Defines cases when the request should be passed on to the next origin.

    Possible values:

    - **error** - an error occurred while establishing a connection with the origin,
      passing a request to it, or reading the response header
    - **timeout** - a timeout has occurred while establishing a connection with the
      origin, passing a request to it, or reading the response header
    - **`invalid_header`** - a origin returned an empty or invalid response
    - **`http_403`** - a origin returned a response with the code 403
    - **`http_404`** - a origin returned a response with the code 404
    - **`http_429`** - a origin returned a response with the code 429
    - **`http_500`** - a origin returned a response with the code 500
    - **`http_502`** - a origin returned a response with the code 502
    - **`http_503`** - a origin returned a response with the code 503
    - **`http_504`** - a origin returned a response with the code 504
    """

    sources: Optional[List[NoneAuthSource]] = None
    """List of origin sources in the origin group."""

    use_next: Optional[bool] = None
    """
    Defines whether to use the next origin from the origin group if origin responds
    with the cases specified in `proxy_next_upstream`. If you enable it, you must
    specify cases in `proxy_next_upstream`.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


class AwsSignatureV4Auth(BaseModel):
    """Credentials to access the private bucket."""

    s3_access_key_id: str
    """Access key ID for the S3 account.

    Restrictions:

    - Latin letters (A-Z, a-z), numbers (0-9), colon, dash, and underscore.
    - From 3 to 512 characters.
    """

    s3_bucket_name: str
    """S3 bucket name.

    Restrictions:

    - Maximum 128 characters.
    """

    s3_secret_access_key: str
    """Secret access key for the S3 account.

    Restrictions:

    - Latin letters (A-Z, a-z), numbers (0-9), pluses, slashes, dashes, colons and
      underscores.
    - If "`s3_type`": amazon, length should be 40 characters.
    - If "`s3_type`": other, length should be from 16 to 255 characters.
    """

    s3_type: str
    """Storage type compatible with S3.

    Possible values:

    - **amazon** – AWS S3 storage.
    - **other** – Other (not AWS) S3 compatible storage.
    """

    s3_region: Optional[str] = None
    """S3 storage region.

    The parameter is required, if "`s3_type`": amazon.
    """

    s3_storage_hostname: Optional[str] = None
    """S3 storage hostname.

    The parameter is required, if "`s3_type`": other.
    """


class AwsSignatureV4(BaseModel):
    id: Optional[int] = None
    """Origin group ID."""

    auth: Optional[AwsSignatureV4Auth] = None
    """Credentials to access the private bucket."""

    auth_type: Optional[str] = None
    """Authentication type.

    **awsSignatureV4** value is used for S3 storage.
    """

    has_related_resources: Optional[bool] = None
    """Defines whether the origin group has related CDN resources.

    Possible values:

    - **true** - Origin group has related CDN resources.
    - **false** - Origin group does not have related CDN resources.
    """

    name: Optional[str] = None
    """Origin group name."""

    path: Optional[str] = None
    """Parameter is **deprecated**."""

    proxy_next_upstream: Optional[List[str]] = None
    """Defines cases when the request should be passed on to the next origin.

    Possible values:

    - **error** - an error occurred while establishing a connection with the origin,
      passing a request to it, or reading the response header
    - **timeout** - a timeout has occurred while establishing a connection with the
      origin, passing a request to it, or reading the response header
    - **`invalid_header`** - a origin returned an empty or invalid response
    - **`http_403`** - a origin returned a response with the code 403
    - **`http_404`** - a origin returned a response with the code 404
    - **`http_429`** - a origin returned a response with the code 429
    - **`http_500`** - a origin returned a response with the code 500
    - **`http_502`** - a origin returned a response with the code 502
    - **`http_503`** - a origin returned a response with the code 503
    - **`http_504`** - a origin returned a response with the code 504
    """

    use_next: Optional[bool] = None
    """
    Defines whether to use the next origin from the origin group if origin responds
    with the cases specified in `proxy_next_upstream`. If you enable it, you must
    specify cases in `proxy_next_upstream`.

    Possible values:

    - **true** - Option is enabled.
    - **false** - Option is disabled.
    """


OriginGroups: TypeAlias = Union[NoneAuth, AwsSignatureV4]

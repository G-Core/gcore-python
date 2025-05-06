# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    name: Required[str]
    """Secret name"""

    payload: Required[str]
    """Secret payload.

    For HTTPS-terminated load balancing, provide base64 encoded conents of a PKCS12
    file. The PKCS12 file is the combined TLS certificate, key, and intermediate
    certificate chain obtained from an external certificate authority. The file can
    be created via openssl, e.g.'openssl pkcs12 -export -inkey server.key -in
    server.crt -certfile ca-chain.crt -passout pass: -out server.p12'The key and
    certificate should be PEM-encoded, and the intermediate certificate chain should
    be multiple PEM-encoded certs concatenated together
    """

    payload_content_encoding: Required[Literal["base64"]]
    """The encoding used for the payload to be able to include it in the JSON request.

    Currently only base64 is supported
    """

    payload_content_type: Required[str]
    """The media type for the content of the payload"""

    secret_type: Required[Literal["certificate", "opaque", "passphrase", "private", "public", "symmetric"]]
    """Secret type.

    symmetric - Used for storing byte arrays such as keys suitable for symmetric
    encryption; public - Used for storing the public key of an asymmetric keypair;
    private - Used for storing the private key of an asymmetric keypair;
    passphrase - Used for storing plain text passphrases; certificate - Used for
    storing cryptographic certificates such as X.509 certificates; opaque - Used for
    backwards compatibility with previous versions of the API
    """

    algorithm: Optional[str]
    """Metadata provided by a user or system for informational purposes."""

    bit_length: Optional[int]
    """Metadata provided by a user or system for informational purposes.

    Value must be greater than zero.
    """

    expiration: Optional[str]
    """Datetime when the secret will expire."""

    mode: Optional[str]
    """Metadata provided by a user or system for informational purposes."""

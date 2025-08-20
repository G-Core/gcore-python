# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["DnssecGetResponse"]


class DnssecGetResponse(BaseModel):
    algorithm: Optional[str] = None
    """Specifies the algorithm used for the key."""

    digest: Optional[str] = None
    """Represents the hashed value of the DS record."""

    digest_algorithm: Optional[str] = None
    """Specifies the algorithm used to generate the digest."""

    digest_type: Optional[str] = None
    """Specifies the type of the digest algorithm used."""

    ds: Optional[str] = None
    """Represents the complete DS record."""

    flags: Optional[int] = None
    """Represents the flag for DNSSEC record."""

    key_tag: Optional[int] = None
    """Represents the identifier of the DNSKEY record."""

    key_type: Optional[str] = None
    """Specifies the type of the key used in the algorithm."""

    public_key: Optional[str] = None
    """Represents the public key used in the DS record."""

    uuid: Optional[str] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RrsetCreateParams", "ResourceRecord", "Picker"]


class RrsetCreateParams(TypedDict, total=False):
    zone_name: Required[Annotated[str, PropertyInfo(alias="zoneName")]]

    rrset_name: Required[Annotated[str, PropertyInfo(alias="rrsetName")]]

    resource_records: Required[Iterable[ResourceRecord]]
    """List of resource record from rrset"""

    meta: Dict[str, object]
    """Meta information for rrset"""

    pickers: Iterable[Picker]
    """Set of pickers"""

    ttl: int


class ResourceRecord(TypedDict, total=False):
    """nolint: lll"""

    content: Required[Iterable[object]]
    """
    Content of resource record The exact length of the array depends on the type of
    rrset, each individual record parameter must be a separate element of the array.
    For example

    - SRV-record: `[100, 1, 5061, "example.com"]`
    - CNAME-record: `[ "the.target.domain" ]`
    - A-record: `[ "1.2.3.4", "5.6.7.8" ]`
    - AAAA-record: `[ "2001:db8::1", "2001:db8::2" ]`
    - MX-record: `[ "mail1.example.com", "mail2.example.com" ]`
    - SVCB/HTTPS-record:
      `[ 1, ".", ["alpn", "h3", "h2"], [ "port", 1443 ], [ "ipv4hint", "10.0.0.1" ], [ "ech", "AEn+DQBFKwAgACABWIHUGj4u+PIggYXcR5JF0gYk3dCRioBW8uJq9H4mKAAIAAEAAQABAANAEnB1YmxpYy50bHMtZWNoLmRldgAA" ] ]`
    """

    enabled: bool

    meta: Dict[str, object]
    """
    This meta will be used to decide which resource record should pass through
    filters from the filter set
    """


class Picker(TypedDict, total=False):
    type: Required[
        Literal[
            "geodns",
            "asn",
            "country",
            "continent",
            "region",
            "ip",
            "geodistance",
            "weighted_shuffle",
            "default",
            "first_n",
        ]
    ]
    """Filter type"""

    limit: int
    """
    Limits the number of records returned by the filter Can be a positive value for
    a specific limit. Use zero or leave it blank to indicate no limits.
    """

    strict: bool
    """
    if strict=false, then the filter will return all records if no records match the
    filter
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DNSOutputRrset", "ResourceRecord", "Picker", "Warning"]


class ResourceRecord(BaseModel):
    content: List[object]
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

    id: Optional[int] = None

    enabled: Optional[bool] = None

    meta: Optional[Dict[str, object]] = None
    """
    Meta information for record Map with string key and any valid json as value,
    with valid keys

    1. `asn` (array of int)
    2. `continents` (array of string)
    3. `countries` (array of string)
    4. `latlong` (array of float64, latitude and longitude)
    5. `fallback` (bool)
    6. `backup` (bool)
    7. `notes` (string)
    8. `weight` (float)
    9. `ip` (string)

    Some keys are reserved for balancing, @see
    https://api.gcore.com/dns/v2/info/meta

    This meta will be used to decide which resource record should pass through
    filters from the filter set
    """


class Picker(BaseModel):
    type: Literal[
        "geodns", "asn", "country", "continent", "region", "ip", "geodistance", "weighted_shuffle", "default", "first_n"
    ]
    """Filter type"""

    limit: Optional[int] = None
    """
    Limits the number of records returned by the filter Can be a positive value for
    a specific limit. Use zero or leave it blank to indicate no limits.
    """

    strict: Optional[bool] = None
    """
    if strict=false, then the filter will return all records if no records match the
    filter
    """


class Warning(BaseModel):
    key: Optional[str] = None

    message: Optional[str] = None


class DNSOutputRrset(BaseModel):
    name: str

    resource_records: List[ResourceRecord]
    """List of resource record from rrset"""

    type: Literal["A", "AAAA", "NS", "CNAME", "MX", "TXT", "SRV", "SOA"]
    """RRSet type"""

    filter_set_id: Optional[int] = None

    meta: Optional[Dict[str, object]] = None
    """Meta information for rrset.

    Map with string key and any valid json as value, with valid keys

    1. `failover` (object, beta feature, might be changed in the future) can have
       fields 1.1. `protocol` (string, required, HTTP, TCP, UDP, ICMP) 1.2. `port`
       (int, required, 1-65535) 1.3. `frequency` (int, required, in seconds 10-3600)
       1.4. `timeout` (int, required, in seconds 1-10), 1.5. `method` (string, only
       for protocol=HTTP) 1.6. `command` (string, bytes to be sent only for
       protocol=TCP/UDP) 1.7. `url` (string, only for protocol=HTTP) 1.8. `tls`
       (bool, only for protocol=HTTP) 1.9. `regexp` (string regex to match, only for
       non-ICMP) 1.10. `http_status_code` (int, only for protocol=HTTP) 1.11. `host`
       (string, only for protocol=HTTP)
    2. `geodns_link` (string) - name of the geodns link to use, if previously set,
       must re-send when updating or CDN integration will be removed for this RRSet
    """

    pickers: Optional[List[Picker]] = None
    """Set of pickers"""

    ttl: Optional[int] = None

    updated_at: Optional[datetime] = None
    """Timestamp marshals/unmarshals date and time as timestamp in json"""

    warning: Optional[str] = None
    """
    Warning about some possible side effects without strictly disallowing operations
    on rrset readonly Deprecated: use Warnings instead
    """

    warnings: Optional[List[Warning]] = None
    """
    Warning about some possible side effects without strictly disallowing operations
    on rrset readonly
    """

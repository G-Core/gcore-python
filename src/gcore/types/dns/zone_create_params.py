# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ZoneCreateParams"]


class ZoneCreateParams(TypedDict, total=False):
    name: Required[str]
    """name of DNS zone"""

    contact: str
    """email address of the administrator responsible for this zone"""

    enabled: bool
    """If a zone is disabled, then its records will not be resolved on dns servers"""

    expiry: int
    """
    number of seconds after which secondary name servers should stop answering
    request for this zone
    """

    meta: Dict[str, object]
    """
    arbitrarily data of zone in json format you can specify `webhook` url and
    `webhook_method` here webhook will get a map with three arrays: for created,
    updated and deleted rrsets `webhook_method` can be omitted, POST will be used by
    default
    """

    nx_ttl: int
    """Time To Live of cache"""

    primary_server: str
    """primary master name server for zone"""

    refresh: int
    """
    number of seconds after which secondary name servers should query the master for
    the SOA record, to detect zone changes.
    """

    retry: int
    """
    number of seconds after which secondary name servers should retry to request the
    serial number
    """

    serial: int
    """
    Serial number for this zone or Timestamp of zone modification moment. If a
    secondary name server slaved to this one observes an increase in this number,
    the slave will assume that the zone has been updated and initiate a zone
    transfer.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["ZoneGetResponse", "Record", "RrsetsAmount", "RrsetsAmountDynamic"]


class Record(BaseModel):
    """Record - readonly short version of rrset"""

    name: Optional[str] = None

    short_answers: Optional[List[str]] = None

    ttl: Optional[int] = None

    type: Optional[str] = None


class RrsetsAmountDynamic(BaseModel):
    """Amount of dynamic RRsets in zone"""

    healthcheck: Optional[int] = None
    """Amount of RRsets with enabled healthchecks"""

    total: Optional[int] = None
    """Total amount of dynamic RRsets in zone"""


class RrsetsAmount(BaseModel):
    dynamic: Optional[RrsetsAmountDynamic] = None
    """Amount of dynamic RRsets in zone"""

    static: Optional[int] = None
    """Amount of static RRsets in zone"""

    total: Optional[int] = None
    """Total amount of RRsets in zone"""


class ZoneGetResponse(BaseModel):
    """Complete zone info with all records included"""

    id: Optional[int] = None
    """
    ID of zone. This field usually is omitted in response and available only in case
    of getting deleted zones by admin.
    """

    contact: Optional[str] = None
    """email address of the administrator responsible for this zone"""

    dnssec_enabled: Optional[bool] = None
    """
    describe dnssec status true means dnssec is enabled for the zone false means
    dnssec is disabled for the zone
    """

    enabled: Optional[bool] = None

    expiry: Optional[int] = None
    """
    number of seconds after which secondary name servers should stop answering
    request for this zone
    """

    meta: Optional[Dict[str, object]] = None
    """arbitrarily data of zone in json format"""

    name: Optional[str] = None
    """name of DNS zone"""

    nx_ttl: Optional[int] = None
    """Time To Live of cache"""

    primary_server: Optional[str] = None
    """primary master name server for zone"""

    records: Optional[List[Record]] = None

    refresh: Optional[int] = None
    """
    number of seconds after which secondary name servers should query the master for
    the SOA record, to detect zone changes.
    """

    retry: Optional[int] = None
    """
    number of seconds after which secondary name servers should retry to request the
    serial number
    """

    rrsets_amount: Optional[RrsetsAmount] = None

    serial: Optional[int] = None
    """
    Serial number for this zone or Timestamp of zone modification moment. If a
    secondary name server slaved to this one observes an increase in this number,
    the slave will assume that the zone has been updated and initiate a zone
    transfer.
    """

    status: Optional[str] = None

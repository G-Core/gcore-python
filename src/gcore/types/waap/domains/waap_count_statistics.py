# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from ...._models import BaseModel

__all__ = ["WaapCountStatistics"]


class WaapCountStatistics(BaseModel):
    """A collection of total numbers of events per criteria"""

    action: List[List[Union[str, int]]]
    """A collection of event counts per action.

    The first item is the action's abbreviation/full action name, and the second
    item is the number of events
    """

    country: List[List[Union[str, int]]]
    """A collection of event counts per country of origin.

    The first item is the country's ISO 3166-1 alpha-2, and the second item is the
    number of events
    """

    org: List[List[Union[str, int]]]
    """A collection of event counts per organization that owns the event's client IP.

    The first item is the organization's name, and the second item is the number of
    events
    """

    rule_name: List[List[Union[str, int]]]
    """A collection of event counts per rule that triggered the event.

    The first item is the rule's name, and the second item is the number of events
    """

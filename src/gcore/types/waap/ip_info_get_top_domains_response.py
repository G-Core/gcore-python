# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .waap_top_domain_detail import WaapTopDomainDetail

__all__ = ["IPInfoGetTopDomainsResponse"]

IPInfoGetTopDomainsResponse: TypeAlias = List[WaapTopDomainDetail]

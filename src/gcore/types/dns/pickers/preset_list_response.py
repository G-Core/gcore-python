# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import TypeAlias

from ..dns_label_name import DNSLabelName

__all__ = ["PresetListResponse"]

PresetListResponse: TypeAlias = Dict[str, List[DNSLabelName]]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .dns_label_name import DNSLabelName

__all__ = ["PickerListResponse"]

PickerListResponse: TypeAlias = List[DNSLabelName]

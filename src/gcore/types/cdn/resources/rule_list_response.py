# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .cdn_resource_rule import CDNResourceRule

__all__ = ["RuleListResponse"]

RuleListResponse: TypeAlias = List[CDNResourceRule]

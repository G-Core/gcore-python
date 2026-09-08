# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .logs_uploader_policy_field import LogsUploaderPolicyField

__all__ = ["PolicyListFieldsAllowedConversionsResponse"]

PolicyListFieldsAllowedConversionsResponse: TypeAlias = List[LogsUploaderPolicyField]

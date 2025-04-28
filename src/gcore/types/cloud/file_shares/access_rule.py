# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AccessRule"]


class AccessRule(BaseModel):
    id: str
    """
    '#/components/schemas/AccessRuleSerializer/properties/id'
    "$.components.schemas.AccessRuleSerializer.properties.id"
    """

    access_level: Literal["ro", "rw"]
    """
    '#/components/schemas/AccessRuleSerializer/properties/access_level'
    "$.components.schemas.AccessRuleSerializer.properties.access_level"
    """

    access_to: str
    """
    '#/components/schemas/AccessRuleSerializer/properties/access_to/anyOf/0'
    "$.components.schemas.AccessRuleSerializer.properties.access_to.anyOf[0]"
    """

    state: Literal["active", "applying", "denying", "error", "new", "queued_to_apply", "queued_to_deny"]
    """
    '#/components/schemas/AccessRuleSerializer/properties/state'
    "$.components.schemas.AccessRuleSerializer.properties.state"
    """

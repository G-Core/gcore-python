# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .session_persistence_type import SessionPersistenceType

__all__ = ["LbSessionPersistence"]


class LbSessionPersistence(BaseModel):
    type: SessionPersistenceType
    """
    '#/components/schemas/LbSessionPersistence/properties/type'
    "$.components.schemas.LbSessionPersistence.properties.type"
    """

    cookie_name: Optional[str] = None
    """
    '#/components/schemas/LbSessionPersistence/properties/cookie_name/anyOf/0'
    "$.components.schemas.LbSessionPersistence.properties.cookie_name.anyOf[0]"
    """

    persistence_granularity: Optional[str] = None
    """
    '#/components/schemas/LbSessionPersistence/properties/persistence_granularity/anyOf/0'
    "$.components.schemas.LbSessionPersistence.properties.persistence_granularity.anyOf[0]"
    """

    persistence_timeout: Optional[int] = None
    """
    '#/components/schemas/LbSessionPersistence/properties/persistence_timeout/anyOf/0'
    "$.components.schemas.LbSessionPersistence.properties.persistence_timeout.anyOf[0]"
    """

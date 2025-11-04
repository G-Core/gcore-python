# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel

__all__ = ["PostgresConfiguration", "Flavor", "StorageClass"]


class Flavor(BaseModel):
    cpu: int
    """Maximum available cores for instance"""

    memory_gib: int
    """Maximum available RAM for instance"""

    pg_conf: str


class StorageClass(BaseModel):
    name: str
    """Storage type"""


class PostgresConfiguration(BaseModel):
    flavors: List[Flavor]

    storage_classes: List[StorageClass]

    versions: List[str]
    """Available versions"""

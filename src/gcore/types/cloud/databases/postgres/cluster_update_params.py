# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ....._types import SequenceNotStr

__all__ = [
    "ClusterUpdateParams",
    "Database",
    "Flavor",
    "HighAvailability",
    "Network",
    "PgServerConfiguration",
    "PgServerConfigurationPooler",
    "Storage",
    "User",
]


class ClusterUpdateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    databases: Iterable[Database]

    flavor: Optional[Flavor]
    """New instance RAM and CPU"""

    high_availability: Optional[HighAvailability]
    """New High Availability settings"""

    network: Optional[Network]

    pg_server_configuration: Optional[PgServerConfiguration]
    """New PosgtreSQL cluster configuration"""

    storage: Optional[Storage]
    """New storage configuration"""

    users: Iterable[User]


class Database(TypedDict, total=False):
    name: Required[str]
    """Database name"""

    owner: Required[str]
    """Database owner from users list"""


class Flavor(TypedDict, total=False):
    """New instance RAM and CPU"""

    cpu: Required[int]
    """Maximum available cores for instance"""

    memory_gib: Required[int]
    """Maximum available RAM for instance"""


class HighAvailability(TypedDict, total=False):
    """New High Availability settings"""

    replication_mode: Required[Literal["async", "sync"]]
    """Type of replication"""


class Network(TypedDict, total=False):
    acl: Required[SequenceNotStr[str]]
    """Allowed IPs and subnets for incoming traffic"""

    network_type: Required[Literal["public"]]
    """Network Type"""


class PgServerConfigurationPooler(TypedDict, total=False):
    mode: Required[Literal["session", "statement", "transaction"]]

    type: Literal["pgbouncer"]


class PgServerConfiguration(TypedDict, total=False):
    """New PosgtreSQL cluster configuration"""

    pg_conf: Optional[str]
    """New pg.conf file settings"""

    pooler: Optional[PgServerConfigurationPooler]

    version: Optional[str]
    """New cluster version"""


class Storage(TypedDict, total=False):
    """New storage configuration"""

    size_gib: Required[int]
    """Total available storage for database"""


class User(TypedDict, total=False):
    name: Required[str]
    """User name"""

    role_attributes: Required[List[Literal["BYPASSRLS", "CREATEDB", "CREATEROLE", "INHERIT", "LOGIN", "NOLOGIN"]]]
    """User's attributes"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ....._types import SequenceNotStr

__all__ = [
    "ClusterCreateParams",
    "Flavor",
    "HighAvailability",
    "Network",
    "PgServerConfiguration",
    "PgServerConfigurationPooler",
    "Storage",
    "Database",
    "User",
]


class ClusterCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    cluster_name: Required[str]
    """PostgreSQL cluster name"""

    flavor: Required[Flavor]
    """Instance RAM and CPU"""

    high_availability: Required[Optional[HighAvailability]]
    """High Availability settings"""

    network: Required[Network]

    pg_server_configuration: Required[PgServerConfiguration]
    """PosgtreSQL cluster configuration"""

    storage: Required[Storage]
    """Cluster's storage configuration"""

    databases: Iterable[Database]

    users: Iterable[User]


class Flavor(TypedDict, total=False):
    """Instance RAM and CPU"""

    cpu: Required[int]
    """Maximum available cores for instance"""

    memory_gib: Required[int]
    """Maximum available RAM for instance"""


class HighAvailability(TypedDict, total=False):
    """High Availability settings"""

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
    """PosgtreSQL cluster configuration"""

    pg_conf: Required[str]
    """pg.conf settings"""

    version: Required[str]
    """Cluster version"""

    pooler: Optional[PgServerConfigurationPooler]


class Storage(TypedDict, total=False):
    """Cluster's storage configuration"""

    size_gib: Required[int]
    """Total available storage for database"""

    type: Required[str]
    """Storage type"""


class Database(TypedDict, total=False):
    name: Required[str]
    """Database name"""

    owner: Required[str]
    """Database owner from users list"""


class User(TypedDict, total=False):
    name: Required[str]
    """User name"""

    role_attributes: Required[List[Literal["BYPASSRLS", "CREATEDB", "CREATEROLE", "INHERIT", "LOGIN", "NOLOGIN"]]]
    """User's attributes"""

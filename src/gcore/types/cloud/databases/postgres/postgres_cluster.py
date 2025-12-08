# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = [
    "PostgresCluster",
    "Database",
    "Flavor",
    "HighAvailability",
    "Network",
    "PgServerConfiguration",
    "PgServerConfigurationPooler",
    "Storage",
    "User",
]


class Database(BaseModel):
    name: str
    """Database name"""

    owner: str
    """Database owner from users list"""

    size: int
    """Size in bytes"""


class Flavor(BaseModel):
    """Instance RAM and CPU"""

    cpu: int
    """Maximum available cores for instance"""

    memory_gib: int
    """Maximum available RAM for instance"""


class HighAvailability(BaseModel):
    replication_mode: Literal["async", "sync"]
    """Type of replication"""


class Network(BaseModel):
    acl: List[str]
    """Allowed IPs and subnets for incoming traffic"""

    connection_string: str
    """Connection string to main database"""

    host: str
    """database hostname"""

    network_type: Literal["public"]
    """Network Type"""


class PgServerConfigurationPooler(BaseModel):
    mode: Literal["session", "statement", "transaction"]

    type: Optional[Literal["pgbouncer"]] = None


class PgServerConfiguration(BaseModel):
    """Main PG configuration"""

    pg_conf: str
    """pg.conf settings"""

    version: str
    """Cluster version"""

    pooler: Optional[PgServerConfigurationPooler] = None


class Storage(BaseModel):
    """PG's storage configuration"""

    size_gib: int
    """Total available storage for database"""

    type: str
    """Storage type"""


class User(BaseModel):
    is_secret_revealed: bool
    """Display was secret revealed or not"""

    name: str
    """User name"""

    role_attributes: List[Literal["BYPASSRLS", "CREATEDB", "CREATEROLE", "INHERIT", "LOGIN", "NOLOGIN"]]
    """User's attributes"""


class PostgresCluster(BaseModel):
    cluster_name: str

    created_at: datetime

    databases: List[Database]

    flavor: Flavor
    """Instance RAM and CPU"""

    high_availability: Optional[HighAvailability] = None

    network: Network

    pg_server_configuration: PgServerConfiguration
    """Main PG configuration"""

    status: Literal["DELETING", "FAILED", "PREPARING", "READY", "UNHEALTHY", "UNKNOWN", "UPDATING"]
    """Current cluster status"""

    storage: Storage
    """PG's storage configuration"""

    users: List[User]

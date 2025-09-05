# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Storage", "Credentials", "CredentialsKey", "CredentialsS3"]


class CredentialsKey(BaseModel):
    id: Optional[int] = None

    created_at: Optional[str] = None

    name: Optional[str] = None


class CredentialsS3(BaseModel):
    access_key: Optional[str] = None

    secret_key: Optional[str] = None


class Credentials(BaseModel):
    keys: Optional[List[CredentialsKey]] = None

    s3: Optional[CredentialsS3] = None

    sftp_password: Optional[str] = None


class Storage(BaseModel):
    id: Optional[int] = None

    address: Optional[str] = None

    can_restore: Optional[bool] = None

    client_id: Optional[int] = None

    created_at: Optional[str] = None

    credentials: Optional[Credentials] = None

    custom_config_file: Optional[bool] = None

    deleted_at: Optional[str] = None

    disable_http: Optional[bool] = None

    expires: Optional[str] = None

    location: Optional[
        Literal["s-ed1", "s-drc2", "s-sgc1", "s-nhn2", "s-darz", "s-ws1", "ams", "sin", "fra", "mia"]
    ] = None

    name: Optional[str] = None

    provisioning_status: Optional[str] = None

    reseller_id: Optional[int] = None

    rewrite_rules: Optional[Dict[str, str]] = None

    server_alias: Optional[str] = None

    type: Optional[Literal["sftp", "s3"]] = None

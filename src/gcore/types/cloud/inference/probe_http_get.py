# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProbeHTTPGet"]


class ProbeHTTPGet(BaseModel):
    headers: Dict[str, str]
    """HTTP headers to be sent with the request."""

    host: Optional[str] = None
    """Host name to send HTTP request to."""

    path: str
    """The endpoint to send the HTTP request to."""

    port: int
    """Port number the probe should connect to."""

    schema_: str = FieldInfo(alias="schema")
    """Schema to use for the HTTP request."""

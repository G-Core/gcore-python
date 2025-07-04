# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["ProbeExec"]


class ProbeExec(BaseModel):
    command: List[str]
    """Command to be executed inside the running container."""

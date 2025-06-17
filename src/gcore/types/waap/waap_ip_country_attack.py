# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapIPCountryAttack"]


class WaapIPCountryAttack(BaseModel):
    count: int
    """The number of attacks from the specified IP address to the country"""

    country: str
    """
    An ISO 3166-1 alpha-2 formatted string representing the country that was
    attacked
    """

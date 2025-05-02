# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .fixed_address import FixedAddress
from .floating_address import FloatingAddress
from .fixed_address_short import FixedAddressShort

__all__ = ["FloatingIPDetailedAddressUnion"]

FloatingIPDetailedAddressUnion: TypeAlias = Union[FloatingAddress, FixedAddressShort, FixedAddress]

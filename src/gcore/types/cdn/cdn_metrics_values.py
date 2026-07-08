# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CDNMetricsValues", "CDNMetricsValueItem"]


class CDNMetricsValueItem(BaseModel):
    timestamp: Optional[int] = None
    """Start timestamp of interval."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Union[float, Dict[str, str]]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Union[float, Dict[str, str]]: ...
    else:
        __pydantic_extra__: Dict[str, Union[float, Dict[str, str]]]


CDNMetricsValues: TypeAlias = List[CDNMetricsValueItem]

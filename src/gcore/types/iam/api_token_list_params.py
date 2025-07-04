# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["APITokenListParams"]


class APITokenListParams(TypedDict, total=False):
    deleted: bool
    """The state of API tokens included in the response.
     Two possible values:

    - True - API token was not deleted.\\** False - API token was deleted.

    Example, _&deleted=True_
    """

    issued_by: int
    """User's ID.

    Use to get API tokens issued by a particular user.
     Example, _&`issued_by`=1234_
    """

    not_issued_by: int
    """User's ID.

    Use to get API tokens issued by anyone except a particular user.
     Example, _¬_issued_by=1234_
    """

    role: str
    """Group's ID. Possible values are:

    - 1 - Administrators* 2 - Users* 5 - Engineers* 3009 - Purge and Prefetch only
      (API+Web)* 3022 - Purge and Prefetch only (API)

    Example, _&role=Engineers_
    """

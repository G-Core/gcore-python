# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SecretReplaceParams", "SecretSlot"]


class SecretReplaceParams(TypedDict, total=False):
    name: Required[str]
    """The unique name of the secret."""

    comment: str
    """A description or comment about the secret."""

    secret_slots: Iterable[SecretSlot]
    """A list of secret slots associated with this secret."""


class SecretSlot(TypedDict, total=False):
    slot: Required[int]
    """
    Unix timestamp (seconds since epoch) indicating when this secret version becomes
    active. Use for time-based secret rotation.
    """

    value: str
    """The plaintext secret value. Will be encrypted with AES-256-GCM before storage."""

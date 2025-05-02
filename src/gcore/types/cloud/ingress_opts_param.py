# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IngressOptsParam"]


class IngressOptsParam(TypedDict, total=False):
    disable_response_buffering: bool
    """Disable response buffering if true.

    A client usually has a much slower connection and can not consume the response
    data as fast as it is produced by an upstream application. Ingress tries to
    buffer the whole response in order to release the upstream application as soon
    as possible.By default, the response buffering is enabled.
    """

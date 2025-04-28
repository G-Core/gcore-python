# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccessRuleCreateParams"]


class AccessRuleCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ffile_shares%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bfile_share_id%7D%2Faccess_rule/post/parameters/0/schema'
    "$.paths['/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/access_rule'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ffile_shares%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bfile_share_id%7D%2Faccess_rule/post/parameters/1/schema'
    "$.paths['/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/access_rule'].post.parameters[1].schema"
    """

    access_mode: Required[Literal["ro", "rw"]]
    """
    '#/components/schemas/CreateAccessRuleSerializer/properties/access_mode'
    "$.components.schemas.CreateAccessRuleSerializer.properties.access_mode"
    """

    ip_address: Required[str]
    """
    '#/components/schemas/CreateAccessRuleSerializer/properties/ip_address/anyOf/0'
    "$.components.schemas.CreateAccessRuleSerializer.properties.ip_address.anyOf[0]"
    """

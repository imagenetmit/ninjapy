"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateNodeRolePolicyAssignmentForOrganizationRequestBodyTypedDict(TypedDict):
    r"""Node role policy assignments"""

    node_role_id: NotRequired[int]
    r"""Node Role Identifier"""
    policy_id: NotRequired[int]
    r"""Policy Identifier"""


class UpdateNodeRolePolicyAssignmentForOrganizationRequestBody(BaseModel):
    r"""Node role policy assignments"""

    node_role_id: Annotated[Optional[int], pydantic.Field(alias="nodeRoleId")] = None
    r"""Node Role Identifier"""

    policy_id: Annotated[Optional[int], pydantic.Field(alias="policyId")] = None
    r"""Policy Identifier"""


class UpdateNodeRolePolicyAssignmentForOrganizationRequestTypedDict(TypedDict):
    id: int
    request_body: NotRequired[
        List[UpdateNodeRolePolicyAssignmentForOrganizationRequestBodyTypedDict]
    ]


class UpdateNodeRolePolicyAssignmentForOrganizationRequest(BaseModel):
    id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        Optional[List[UpdateNodeRolePolicyAssignmentForOrganizationRequestBody]],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None

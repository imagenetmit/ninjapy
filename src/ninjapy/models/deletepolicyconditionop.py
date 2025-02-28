"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class DeletePolicyConditionRequestTypedDict(TypedDict):
    policy_id: int
    condition_id: str


class DeletePolicyConditionRequest(BaseModel):
    policy_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    condition_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class GetClientChecklistSignedUrlsRequestTypedDict(TypedDict):
    checklist_id: int


class GetClientChecklistSignedUrlsRequest(BaseModel):
    checklist_id: Annotated[
        int,
        pydantic.Field(alias="checklistId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

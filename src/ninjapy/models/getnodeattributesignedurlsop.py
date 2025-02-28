"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class PathParamEntityType(str, Enum):
    NODE = "NODE"
    LOCATION = "LOCATION"
    ORGANIZATION = "ORGANIZATION"


class GetNodeAttributeSignedUrlsRequestTypedDict(TypedDict):
    entity_type: PathParamEntityType
    entity_id: int


class GetNodeAttributeSignedUrlsRequest(BaseModel):
    entity_type: Annotated[
        PathParamEntityType,
        pydantic.Field(alias="entityType"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    entity_id: Annotated[
        int,
        pydantic.Field(alias="entityId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

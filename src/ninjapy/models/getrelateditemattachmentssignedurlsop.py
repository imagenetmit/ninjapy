"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class GetRelatedItemAttachmentsSignedUrlsPathParamEntityType(str, Enum):
    ORGANIZATION = "ORGANIZATION"
    DOCUMENT = "DOCUMENT"
    LOCATION = "LOCATION"
    NODE = "NODE"
    CHECKLIST = "CHECKLIST"
    KB_DOCUMENT = "KB_DOCUMENT"


class GetRelatedItemAttachmentsSignedUrlsRequestTypedDict(TypedDict):
    entity_type: GetRelatedItemAttachmentsSignedUrlsPathParamEntityType
    entity_id: int


class GetRelatedItemAttachmentsSignedUrlsRequest(BaseModel):
    entity_type: Annotated[
        GetRelatedItemAttachmentsSignedUrlsPathParamEntityType,
        pydantic.Field(alias="entityType"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    entity_id: Annotated[
        int,
        pydantic.Field(alias="entityId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

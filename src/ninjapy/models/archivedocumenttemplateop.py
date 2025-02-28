"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class ArchiveDocumentTemplateRequestTypedDict(TypedDict):
    document_template_id: int


class ArchiveDocumentTemplateRequest(BaseModel):
    document_template_id: Annotated[
        int,
        pydantic.Field(alias="documentTemplateId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

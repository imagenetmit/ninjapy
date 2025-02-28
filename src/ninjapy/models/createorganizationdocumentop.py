"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateOrganizationDocumentFieldsTypedDict(TypedDict):
    r"""Fields"""


class CreateOrganizationDocumentFields(BaseModel):
    r"""Fields"""


class CreateOrganizationDocumentRequestBodyTypedDict(TypedDict):
    document_name: NotRequired[str]
    r"""Document Name"""
    document_description: NotRequired[str]
    r"""Document Description"""
    fields: NotRequired[Dict[str, CreateOrganizationDocumentFieldsTypedDict]]
    r"""Fields"""


class CreateOrganizationDocumentRequestBody(BaseModel):
    document_name: Annotated[Optional[str], pydantic.Field(alias="documentName")] = None
    r"""Document Name"""

    document_description: Annotated[
        Optional[str], pydantic.Field(alias="documentDescription")
    ] = None
    r"""Document Description"""

    fields: Optional[Dict[str, CreateOrganizationDocumentFields]] = None
    r"""Fields"""


class CreateOrganizationDocumentRequestTypedDict(TypedDict):
    organization_id: int
    r"""Organization identifier"""
    document_template_id: int
    r"""Document template identifier"""
    request_body: NotRequired[CreateOrganizationDocumentRequestBodyTypedDict]


class CreateOrganizationDocumentRequest(BaseModel):
    organization_id: Annotated[
        int,
        pydantic.Field(alias="organizationId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Organization identifier"""

    document_template_id: Annotated[
        int,
        pydantic.Field(alias="documentTemplateId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Document template identifier"""

    request_body: Annotated[
        Optional[CreateOrganizationDocumentRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class CreateOrganizationDocumentValueTypedDict(TypedDict):
    r"""Value"""


class CreateOrganizationDocumentValue(BaseModel):
    r"""Value"""


class CreateOrganizationDocumentOrganizationDocumentsFieldsTypedDict(TypedDict):
    r"""Updated Fields"""

    name: NotRequired[str]
    r"""Name"""
    value: NotRequired[CreateOrganizationDocumentValueTypedDict]
    r"""Value"""
    value_update_time: NotRequired[float]
    r"""Value Last Updated"""


class CreateOrganizationDocumentOrganizationDocumentsFields(BaseModel):
    r"""Updated Fields"""

    name: Optional[str] = None
    r"""Name"""

    value: Optional[CreateOrganizationDocumentValue] = None
    r"""Value"""

    value_update_time: Annotated[
        Optional[float], pydantic.Field(alias="valueUpdateTime")
    ] = None
    r"""Value Last Updated"""


class CreateOrganizationDocumentResponseBodyTypedDict(TypedDict):
    r"""Returns the organization document created"""

    document_id: NotRequired[int]
    r"""Document Identifier"""
    document_name: NotRequired[str]
    r"""Document Name"""
    document_description: NotRequired[str]
    r"""Document Description"""
    document_update_time: NotRequired[float]
    r"""Document Last Updated"""
    fields: NotRequired[
        List[CreateOrganizationDocumentOrganizationDocumentsFieldsTypedDict]
    ]
    r"""Fields"""
    document_template_id: NotRequired[int]
    r"""Document Template Identifier"""
    document_template_name: NotRequired[str]
    r"""Document Template Name"""
    organization_id: NotRequired[int]
    r"""Organization Identifier"""


class CreateOrganizationDocumentResponseBody(BaseModel):
    r"""Returns the organization document created"""

    document_id: Annotated[Optional[int], pydantic.Field(alias="documentId")] = None
    r"""Document Identifier"""

    document_name: Annotated[Optional[str], pydantic.Field(alias="documentName")] = None
    r"""Document Name"""

    document_description: Annotated[
        Optional[str], pydantic.Field(alias="documentDescription")
    ] = None
    r"""Document Description"""

    document_update_time: Annotated[
        Optional[float], pydantic.Field(alias="documentUpdateTime")
    ] = None
    r"""Document Last Updated"""

    fields: Optional[List[CreateOrganizationDocumentOrganizationDocumentsFields]] = None
    r"""Fields"""

    document_template_id: Annotated[
        Optional[int], pydantic.Field(alias="documentTemplateId")
    ] = None
    r"""Document Template Identifier"""

    document_template_name: Annotated[
        Optional[str], pydantic.Field(alias="documentTemplateName")
    ] = None
    r"""Document Template Name"""

    organization_id: Annotated[
        Optional[int], pydantic.Field(alias="organizationId")
    ] = None
    r"""Organization Identifier"""

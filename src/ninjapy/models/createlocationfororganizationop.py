"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateLocationForOrganizationFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class CreateLocationForOrganizationFields(BaseModel):
    r"""Custom Fields"""


class CreateLocationForOrganizationRequestBodyTypedDict(TypedDict):
    name: NotRequired[str]
    r"""Location name"""
    address: NotRequired[str]
    r"""Address"""
    description: NotRequired[str]
    r"""Description"""
    user_data: NotRequired[Dict[str, Any]]
    r"""Custom attributes"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[Dict[str, CreateLocationForOrganizationFieldsTypedDict]]
    r"""Custom Fields"""


class CreateLocationForOrganizationRequestBody(BaseModel):
    name: Optional[str] = None
    r"""Location name"""

    address: Optional[str] = None
    r"""Address"""

    description: Optional[str] = None
    r"""Description"""

    user_data: Annotated[Optional[Dict[str, Any]], pydantic.Field(alias="userData")] = (
        None
    )
    r"""Custom attributes"""

    tags: Optional[List[str]] = None
    r"""Tags"""

    fields: Optional[Dict[str, CreateLocationForOrganizationFields]] = None
    r"""Custom Fields"""


class CreateLocationForOrganizationRequestTypedDict(TypedDict):
    id: int
    request_body: NotRequired[CreateLocationForOrganizationRequestBodyTypedDict]


class CreateLocationForOrganizationRequest(BaseModel):
    id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        Optional[CreateLocationForOrganizationRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class CreateLocationForOrganizationManagementFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class CreateLocationForOrganizationManagementFields(BaseModel):
    r"""Custom Fields"""


class CreateLocationForOrganizationResponseBodyTypedDict(TypedDict):
    r"""Location"""

    name: NotRequired[str]
    r"""Location name"""
    address: NotRequired[str]
    r"""Address"""
    description: NotRequired[str]
    r"""Description"""
    user_data: NotRequired[Dict[str, Any]]
    r"""Custom attributes"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[
        Dict[str, CreateLocationForOrganizationManagementFieldsTypedDict]
    ]
    r"""Custom Fields"""
    id: NotRequired[int]
    r"""Location identifier"""


class CreateLocationForOrganizationResponseBody(BaseModel):
    r"""Location"""

    name: Optional[str] = None
    r"""Location name"""

    address: Optional[str] = None
    r"""Address"""

    description: Optional[str] = None
    r"""Description"""

    user_data: Annotated[Optional[Dict[str, Any]], pydantic.Field(alias="userData")] = (
        None
    )
    r"""Custom attributes"""

    tags: Optional[List[str]] = None
    r"""Tags"""

    fields: Optional[Dict[str, CreateLocationForOrganizationManagementFields]] = None
    r"""Custom Fields"""

    id: Optional[int] = None
    r"""Location identifier"""

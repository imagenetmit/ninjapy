"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetOrganizationsRequestTypedDict(TypedDict):
    page_size: NotRequired[int]
    r"""Limit number of organizations to return"""
    after: NotRequired[int]
    r"""Last Organization Identifier from previous page"""
    of: NotRequired[str]
    r"""Organization filter"""


class GetOrganizationsRequest(BaseModel):
    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Limit number of organizations to return"""

    after: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Last Organization Identifier from previous page"""

    of: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Organization filter"""


class GetOrganizationsNodeApprovalMode(str, Enum):
    r"""Device Approval Mode"""

    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"
    REJECT = "REJECT"


class GetOrganizationsFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class GetOrganizationsFields(BaseModel):
    r"""Custom Fields"""


class GetOrganizationsResponseBodyTypedDict(TypedDict):
    r"""Organization"""

    name: NotRequired[str]
    r"""Organization full name"""
    description: NotRequired[str]
    r"""Organization Description"""
    user_data: NotRequired[Dict[str, Any]]
    r"""Custom attributes"""
    node_approval_mode: NotRequired[GetOrganizationsNodeApprovalMode]
    r"""Device Approval Mode"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[Dict[str, GetOrganizationsFieldsTypedDict]]
    r"""Custom Fields"""
    id: NotRequired[int]
    r"""Organization identifier"""


class GetOrganizationsResponseBody(BaseModel):
    r"""Organization"""

    name: Optional[str] = None
    r"""Organization full name"""

    description: Optional[str] = None
    r"""Organization Description"""

    user_data: Annotated[Optional[Dict[str, Any]], pydantic.Field(alias="userData")] = (
        None
    )
    r"""Custom attributes"""

    node_approval_mode: Annotated[
        Optional[GetOrganizationsNodeApprovalMode],
        pydantic.Field(alias="nodeApprovalMode"),
    ] = None
    r"""Device Approval Mode"""

    tags: Optional[List[str]] = None
    r"""Tags"""

    fields: Optional[Dict[str, GetOrganizationsFields]] = None
    r"""Custom Fields"""

    id: Optional[int] = None
    r"""Organization identifier"""

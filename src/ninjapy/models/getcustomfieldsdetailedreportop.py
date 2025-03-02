"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetCustomFieldsDetailedReportRequestTypedDict(TypedDict):
    df: NotRequired[str]
    r"""Device filter"""
    cursor: NotRequired[str]
    r"""Cursor name"""
    page_size: NotRequired[int]
    r"""Limit number of records per page"""
    updated_after: NotRequired[str]
    r"""Custom fields updated after specified date"""
    fields: NotRequired[str]
    r"""Comma-separated list of fields"""
    show_secure_values: NotRequired[bool]
    r"""Flag to indicate if secure values should be returned as plain text without encryption"""


class GetCustomFieldsDetailedReportRequest(BaseModel):
    df: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Device filter"""

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Cursor name"""

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1000
    r"""Limit number of records per page"""

    updated_after: Annotated[
        Optional[str],
        pydantic.Field(alias="updatedAfter"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Custom fields updated after specified date"""

    fields: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-separated list of fields"""

    show_secure_values: Annotated[
        Optional[bool],
        pydantic.Field(alias="showSecureValues"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Flag to indicate if secure values should be returned as plain text without encryption"""


class GetCustomFieldsDetailedReportCursorTypedDict(TypedDict):
    name: NotRequired[str]
    offset: NotRequired[int]
    count: NotRequired[int]
    expires: NotRequired[float]


class GetCustomFieldsDetailedReportCursor(BaseModel):
    name: Optional[str] = None

    offset: Optional[int] = None

    count: Optional[int] = None

    expires: Optional[float] = None


class GetCustomFieldsDetailedReportEntityType(str, Enum):
    r"""Entity type"""

    NODE = "NODE"
    LOCATION = "LOCATION"
    ORGANIZATION = "ORGANIZATION"


class GetCustomFieldsDetailedReportValueTypedDict(TypedDict):
    r"""Field Value"""


class GetCustomFieldsDetailedReportValue(BaseModel):
    r"""Field Value"""


class GetCustomFieldsDetailedReportSource(str, Enum):
    API = "API"
    USER = "USER"
    SCRIPT = "SCRIPT"


class UserTypedDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]


class User(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class UpdatedByTypedDict(TypedDict):
    r"""Value source (who/what updated the value)"""

    source: NotRequired[GetCustomFieldsDetailedReportSource]
    user: NotRequired[UserTypedDict]


class UpdatedBy(BaseModel):
    r"""Value source (who/what updated the value)"""

    source: Optional[GetCustomFieldsDetailedReportSource] = None

    user: Optional[User] = None


class GetCustomFieldsDetailedReportFieldsTypedDict(TypedDict):
    r"""Field values"""

    name: NotRequired[str]
    r"""Field name"""
    value: NotRequired[GetCustomFieldsDetailedReportValueTypedDict]
    r"""Field Value"""
    updated_by: NotRequired[UpdatedByTypedDict]
    r"""Value source (who/what updated the value)"""
    update_time: NotRequired[float]


class GetCustomFieldsDetailedReportFields(BaseModel):
    r"""Field values"""

    name: Optional[str] = None
    r"""Field name"""

    value: Optional[GetCustomFieldsDetailedReportValue] = None
    r"""Field Value"""

    updated_by: Annotated[Optional[UpdatedBy], pydantic.Field(alias="updatedBy")] = None
    r"""Value source (who/what updated the value)"""

    update_time: Annotated[Optional[float], pydantic.Field(alias="updateTime")] = None


class GetCustomFieldsDetailedReportResultsTypedDict(TypedDict):
    entity_type: NotRequired[GetCustomFieldsDetailedReportEntityType]
    r"""Entity type"""
    fields: NotRequired[List[GetCustomFieldsDetailedReportFieldsTypedDict]]
    r"""Field values"""
    entity_id: NotRequired[int]


class GetCustomFieldsDetailedReportResults(BaseModel):
    entity_type: Annotated[
        Optional[GetCustomFieldsDetailedReportEntityType],
        pydantic.Field(alias="entityType"),
    ] = None
    r"""Entity type"""

    fields: Optional[List[GetCustomFieldsDetailedReportFields]] = None
    r"""Field values"""

    entity_id: Annotated[Optional[int], pydantic.Field(alias="entityId")] = None


class GetCustomFieldsDetailedReportResponseBodyTypedDict(TypedDict):
    r"""default response"""

    cursor: NotRequired[GetCustomFieldsDetailedReportCursorTypedDict]
    results: NotRequired[List[GetCustomFieldsDetailedReportResultsTypedDict]]


class GetCustomFieldsDetailedReportResponseBody(BaseModel):
    r"""default response"""

    cursor: Optional[GetCustomFieldsDetailedReportCursor] = None

    results: Optional[List[GetCustomFieldsDetailedReportResults]] = None

"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetCustomFieldsReportRequestTypedDict(TypedDict):
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


class GetCustomFieldsReportRequest(BaseModel):
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


class GetCustomFieldsReportCursorTypedDict(TypedDict):
    name: NotRequired[str]
    offset: NotRequired[int]
    count: NotRequired[int]
    expires: NotRequired[float]


class GetCustomFieldsReportCursor(BaseModel):
    name: Optional[str] = None

    offset: Optional[int] = None

    count: Optional[int] = None

    expires: Optional[float] = None


class GetCustomFieldsReportFieldsTypedDict(TypedDict):
    r"""Field values"""


class GetCustomFieldsReportFields(BaseModel):
    r"""Field values"""


class GetCustomFieldsReportResultsTypedDict(TypedDict):
    device_id: NotRequired[int]
    r"""Device identifier"""
    fields: NotRequired[Dict[str, GetCustomFieldsReportFieldsTypedDict]]
    r"""Field values"""


class GetCustomFieldsReportResults(BaseModel):
    device_id: Annotated[Optional[int], pydantic.Field(alias="deviceId")] = None
    r"""Device identifier"""

    fields: Optional[Dict[str, GetCustomFieldsReportFields]] = None
    r"""Field values"""


class GetCustomFieldsReportResponseBodyTypedDict(TypedDict):
    r"""default response"""

    cursor: NotRequired[GetCustomFieldsReportCursorTypedDict]
    results: NotRequired[List[GetCustomFieldsReportResultsTypedDict]]


class GetCustomFieldsReportResponseBody(BaseModel):
    r"""default response"""

    cursor: Optional[GetCustomFieldsReportCursor] = None

    results: Optional[List[GetCustomFieldsReportResults]] = None

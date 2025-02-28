"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetInstalledSoftwarePatchesRequestTypedDict(TypedDict):
    df: NotRequired[str]
    r"""Device filter"""
    type: NotRequired[str]
    r"""Patch Type filter"""
    impact: NotRequired[str]
    r"""Patch Impact filter"""
    status: NotRequired[str]
    r"""Patch Status filter"""
    product_identifier: NotRequired[str]
    r"""Product Identifier"""
    installed_before: NotRequired[str]
    r"""Include patches installed before specified date"""
    installed_after: NotRequired[str]
    r"""Include patches installed after specified date"""
    cursor: NotRequired[str]
    r"""Cursor name"""
    page_size: NotRequired[int]
    r"""Limit number of records per page"""


class GetInstalledSoftwarePatchesRequest(BaseModel):
    df: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Device filter"""

    type: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Patch Type filter"""

    impact: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Patch Impact filter"""

    status: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Patch Status filter"""

    product_identifier: Annotated[
        Optional[str],
        pydantic.Field(alias="productIdentifier"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Product Identifier"""

    installed_before: Annotated[
        Optional[str],
        pydantic.Field(alias="installedBefore"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Include patches installed before specified date"""

    installed_after: Annotated[
        Optional[str],
        pydantic.Field(alias="installedAfter"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Include patches installed after specified date"""

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Cursor name"""

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Limit number of records per page"""


class GetInstalledSoftwarePatchesCursorTypedDict(TypedDict):
    name: NotRequired[str]
    offset: NotRequired[int]
    count: NotRequired[int]
    expires: NotRequired[float]


class GetInstalledSoftwarePatchesCursor(BaseModel):
    name: Optional[str] = None

    offset: Optional[int] = None

    count: Optional[int] = None

    expires: Optional[float] = None


class GetInstalledSoftwarePatchesResultsTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Identifier"""
    product_identifier: NotRequired[str]
    r"""Software product identifier"""
    title: NotRequired[str]
    r"""Patch title"""
    impact: NotRequired[str]
    r"""Impact"""
    status: NotRequired[str]
    r"""Status"""
    type: NotRequired[str]
    r"""Patch type"""
    installed_at: NotRequired[float]
    r"""Installation attempt timestamp"""
    device_id: NotRequired[int]
    r"""Device identifier"""
    timestamp: NotRequired[float]
    r"""Date/Time when data was collected/updated"""


class GetInstalledSoftwarePatchesResults(BaseModel):
    id: Optional[str] = None
    r"""Identifier"""

    product_identifier: Annotated[
        Optional[str], pydantic.Field(alias="productIdentifier")
    ] = None
    r"""Software product identifier"""

    title: Optional[str] = None
    r"""Patch title"""

    impact: Optional[str] = None
    r"""Impact"""

    status: Optional[str] = None
    r"""Status"""

    type: Optional[str] = None
    r"""Patch type"""

    installed_at: Annotated[Optional[float], pydantic.Field(alias="installedAt")] = None
    r"""Installation attempt timestamp"""

    device_id: Annotated[Optional[int], pydantic.Field(alias="deviceId")] = None
    r"""Device identifier"""

    timestamp: Optional[float] = None
    r"""Date/Time when data was collected/updated"""


class GetInstalledSoftwarePatchesResponseBodyTypedDict(TypedDict):
    r"""default response"""

    cursor: NotRequired[GetInstalledSoftwarePatchesCursorTypedDict]
    results: NotRequired[List[GetInstalledSoftwarePatchesResultsTypedDict]]


class GetInstalledSoftwarePatchesResponseBody(BaseModel):
    r"""default response"""

    cursor: Optional[GetInstalledSoftwarePatchesCursor] = None

    results: Optional[List[GetInstalledSoftwarePatchesResults]] = None

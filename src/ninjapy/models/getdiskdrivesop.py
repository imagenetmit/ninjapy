"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetDiskDrivesRequestTypedDict(TypedDict):
    df: NotRequired[str]
    r"""Device filter"""
    ts: NotRequired[str]
    r"""Monitoring timestamp filter"""
    cursor: NotRequired[str]
    r"""Cursor name"""
    page_size: NotRequired[int]
    r"""Limit number of records per page"""


class GetDiskDrivesRequest(BaseModel):
    df: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Device filter"""

    ts: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Monitoring timestamp filter"""

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


class GetDiskDrivesCursorTypedDict(TypedDict):
    name: NotRequired[str]
    offset: NotRequired[int]
    count: NotRequired[int]
    expires: NotRequired[float]


class GetDiskDrivesCursor(BaseModel):
    name: Optional[str] = None

    offset: Optional[int] = None

    count: Optional[int] = None

    expires: Optional[float] = None


class GetDiskDrivesResultsTypedDict(TypedDict):
    bytes_per_sector: NotRequired[int]
    r"""Number of bytes per sector"""
    description: NotRequired[str]
    r"""Description"""
    interface_type: NotRequired[str]
    r"""Interface type"""
    manufacturer: NotRequired[str]
    r"""Manufacturer"""
    media_type: NotRequired[str]
    r"""Media Type"""
    model: NotRequired[str]
    r"""Model"""
    name: NotRequired[str]
    r"""Name"""
    partition_count: NotRequired[int]
    r"""Number of partitions"""
    serial_number: NotRequired[str]
    r"""Serial number"""
    size: NotRequired[int]
    r"""Size (Bytes)"""
    smart_capable: NotRequired[bool]
    r"""Is S.M.A.R.T. capable?"""
    status: NotRequired[str]
    r"""Status"""
    device_id: NotRequired[int]
    r"""Device identifier"""
    timestamp: NotRequired[float]
    r"""Date/Time when data was collected/updated"""


class GetDiskDrivesResults(BaseModel):
    bytes_per_sector: Annotated[
        Optional[int], pydantic.Field(alias="bytesPerSector")
    ] = None
    r"""Number of bytes per sector"""

    description: Optional[str] = None
    r"""Description"""

    interface_type: Annotated[Optional[str], pydantic.Field(alias="interfaceType")] = (
        None
    )
    r"""Interface type"""

    manufacturer: Optional[str] = None
    r"""Manufacturer"""

    media_type: Annotated[Optional[str], pydantic.Field(alias="mediaType")] = None
    r"""Media Type"""

    model: Optional[str] = None
    r"""Model"""

    name: Optional[str] = None
    r"""Name"""

    partition_count: Annotated[
        Optional[int], pydantic.Field(alias="partitionCount")
    ] = None
    r"""Number of partitions"""

    serial_number: Annotated[Optional[str], pydantic.Field(alias="serialNumber")] = None
    r"""Serial number"""

    size: Optional[int] = None
    r"""Size (Bytes)"""

    smart_capable: Annotated[Optional[bool], pydantic.Field(alias="smartCapable")] = (
        None
    )
    r"""Is S.M.A.R.T. capable?"""

    status: Optional[str] = None
    r"""Status"""

    device_id: Annotated[Optional[int], pydantic.Field(alias="deviceId")] = None
    r"""Device identifier"""

    timestamp: Optional[float] = None
    r"""Date/Time when data was collected/updated"""


class GetDiskDrivesResponseBodyTypedDict(TypedDict):
    r"""default response"""

    cursor: NotRequired[GetDiskDrivesCursorTypedDict]
    results: NotRequired[List[GetDiskDrivesResultsTypedDict]]


class GetDiskDrivesResponseBody(BaseModel):
    r"""default response"""

    cursor: Optional[GetDiskDrivesCursor] = None

    results: Optional[List[GetDiskDrivesResults]] = None

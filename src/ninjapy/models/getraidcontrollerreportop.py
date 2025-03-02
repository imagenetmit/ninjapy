"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetRAIDControllerReportRequestTypedDict(TypedDict):
    df: NotRequired[str]
    r"""Device filter"""
    ts: NotRequired[str]
    r"""Monitoring timestamp filter"""
    cursor: NotRequired[str]
    r"""Cursor name"""
    page_size: NotRequired[int]
    r"""Limit number of records per page"""


class GetRAIDControllerReportRequest(BaseModel):
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


class GetRAIDControllerReportCursorTypedDict(TypedDict):
    name: NotRequired[str]
    offset: NotRequired[int]
    count: NotRequired[int]
    expires: NotRequired[float]


class GetRAIDControllerReportCursor(BaseModel):
    name: Optional[str] = None

    offset: Optional[int] = None

    count: Optional[int] = None

    expires: Optional[float] = None


class GetRAIDControllerReportResultsTypedDict(TypedDict):
    backup_battery_status: NotRequired[str]
    r"""Backup Battery Status"""
    battery_temperature: NotRequired[int]
    r"""Battery Temperature"""
    bios_version: NotRequired[str]
    r"""BIOS Version"""
    cache_size: NotRequired[int]
    r"""Cache size (bytes)"""
    controller_index: NotRequired[int]
    r"""Controller Index"""
    driver_name: NotRequired[str]
    r"""Device Driver Name"""
    driver_version: NotRequired[str]
    r"""Driver Version"""
    family: NotRequired[str]
    r"""Family"""
    firmware_version: NotRequired[str]
    r"""Firmware Version"""
    hardware_revision: NotRequired[str]
    r"""Hardware Revision"""
    manufacturer: NotRequired[str]
    r"""Manufacturer"""
    manufacturing_date: NotRequired[float]
    r"""Manufacturing date"""
    model: NotRequired[str]
    r"""Model"""
    physical_drive_count: NotRequired[int]
    r"""Physical drive count"""
    slot: NotRequired[str]
    r"""Slot"""
    system_health_status: NotRequired[str]
    r"""System Health Status"""
    virtual_drive_count: NotRequired[int]
    r"""Virtual drive count"""
    device_id: NotRequired[int]
    r"""Device identifier"""
    timestamp: NotRequired[float]
    r"""Date/Time when data was collected/updated"""


class GetRAIDControllerReportResults(BaseModel):
    backup_battery_status: Annotated[
        Optional[str], pydantic.Field(alias="backupBatteryStatus")
    ] = None
    r"""Backup Battery Status"""

    battery_temperature: Annotated[
        Optional[int], pydantic.Field(alias="batteryTemperature")
    ] = None
    r"""Battery Temperature"""

    bios_version: Annotated[Optional[str], pydantic.Field(alias="biosVersion")] = None
    r"""BIOS Version"""

    cache_size: Annotated[Optional[int], pydantic.Field(alias="cacheSize")] = None
    r"""Cache size (bytes)"""

    controller_index: Annotated[
        Optional[int], pydantic.Field(alias="controllerIndex")
    ] = None
    r"""Controller Index"""

    driver_name: Annotated[Optional[str], pydantic.Field(alias="driverName")] = None
    r"""Device Driver Name"""

    driver_version: Annotated[Optional[str], pydantic.Field(alias="driverVersion")] = (
        None
    )
    r"""Driver Version"""

    family: Optional[str] = None
    r"""Family"""

    firmware_version: Annotated[
        Optional[str], pydantic.Field(alias="firmwareVersion")
    ] = None
    r"""Firmware Version"""

    hardware_revision: Annotated[
        Optional[str], pydantic.Field(alias="hardwareRevision")
    ] = None
    r"""Hardware Revision"""

    manufacturer: Optional[str] = None
    r"""Manufacturer"""

    manufacturing_date: Annotated[
        Optional[float], pydantic.Field(alias="manufacturingDate")
    ] = None
    r"""Manufacturing date"""

    model: Optional[str] = None
    r"""Model"""

    physical_drive_count: Annotated[
        Optional[int], pydantic.Field(alias="physicalDriveCount")
    ] = None
    r"""Physical drive count"""

    slot: Optional[str] = None
    r"""Slot"""

    system_health_status: Annotated[
        Optional[str], pydantic.Field(alias="systemHealthStatus")
    ] = None
    r"""System Health Status"""

    virtual_drive_count: Annotated[
        Optional[int], pydantic.Field(alias="virtualDriveCount")
    ] = None
    r"""Virtual drive count"""

    device_id: Annotated[Optional[int], pydantic.Field(alias="deviceId")] = None
    r"""Device identifier"""

    timestamp: Optional[float] = None
    r"""Date/Time when data was collected/updated"""


class GetRAIDControllerReportResponseBodyTypedDict(TypedDict):
    r"""default response"""

    cursor: NotRequired[GetRAIDControllerReportCursorTypedDict]
    results: NotRequired[List[GetRAIDControllerReportResultsTypedDict]]


class GetRAIDControllerReportResponseBody(BaseModel):
    r"""default response"""

    cursor: Optional[GetRAIDControllerReportCursor] = None

    results: Optional[List[GetRAIDControllerReportResults]] = None

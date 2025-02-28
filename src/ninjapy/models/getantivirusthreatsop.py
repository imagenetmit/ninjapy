"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetAntivirusThreatsRequestTypedDict(TypedDict):
    df: NotRequired[str]
    r"""Device filter"""
    ts: NotRequired[str]
    r"""Monitoring timestamp filter"""
    cursor: NotRequired[str]
    r"""Cursor name"""
    page_size: NotRequired[int]
    r"""Limit number of records per page"""


class GetAntivirusThreatsRequest(BaseModel):
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


class GetAntivirusThreatsCursorTypedDict(TypedDict):
    name: NotRequired[str]
    offset: NotRequired[int]
    count: NotRequired[int]
    expires: NotRequired[float]


class GetAntivirusThreatsCursor(BaseModel):
    name: Optional[str] = None

    offset: Optional[int] = None

    count: Optional[int] = None

    expires: Optional[float] = None


class GetAntivirusThreatsResultsTypedDict(TypedDict):
    name: NotRequired[str]
    r"""Threat name"""
    product_code: NotRequired[str]
    r"""AntiVirus vendor product code"""
    quarantine_id: NotRequired[str]
    r"""Threat Quarantine ID"""
    status: NotRequired[str]
    r"""Threat Status (vendor specific)"""
    type: NotRequired[str]
    r"""Type of Threat"""
    threat_id: NotRequired[int]
    r"""Threat ID"""
    category: NotRequired[str]
    r"""Threat Category"""
    level: NotRequired[str]
    r"""Threat Level"""
    detection_source: NotRequired[str]
    r"""Detection source"""
    trace_list: NotRequired[str]
    r"""Trace list (Files, Cookies, etc. Vendor specific)"""
    device_id: NotRequired[int]
    r"""Device identifier"""
    timestamp: NotRequired[float]
    r"""Date/Time when data was collected/updated"""


class GetAntivirusThreatsResults(BaseModel):
    name: Optional[str] = None
    r"""Threat name"""

    product_code: Annotated[Optional[str], pydantic.Field(alias="productCode")] = None
    r"""AntiVirus vendor product code"""

    quarantine_id: Annotated[Optional[str], pydantic.Field(alias="quarantineId")] = None
    r"""Threat Quarantine ID"""

    status: Optional[str] = None
    r"""Threat Status (vendor specific)"""

    type: Optional[str] = None
    r"""Type of Threat"""

    threat_id: Annotated[Optional[int], pydantic.Field(alias="threatId")] = None
    r"""Threat ID"""

    category: Optional[str] = None
    r"""Threat Category"""

    level: Optional[str] = None
    r"""Threat Level"""

    detection_source: Annotated[
        Optional[str], pydantic.Field(alias="detectionSource")
    ] = None
    r"""Detection source"""

    trace_list: Annotated[Optional[str], pydantic.Field(alias="traceList")] = None
    r"""Trace list (Files, Cookies, etc. Vendor specific)"""

    device_id: Annotated[Optional[int], pydantic.Field(alias="deviceId")] = None
    r"""Device identifier"""

    timestamp: Optional[float] = None
    r"""Date/Time when data was collected/updated"""


class GetAntivirusThreatsResponseBodyTypedDict(TypedDict):
    r"""default response"""

    cursor: NotRequired[GetAntivirusThreatsCursorTypedDict]
    results: NotRequired[List[GetAntivirusThreatsResultsTypedDict]]


class GetAntivirusThreatsResponseBody(BaseModel):
    r"""default response"""

    cursor: Optional[GetAntivirusThreatsCursor] = None

    results: Optional[List[GetAntivirusThreatsResults]] = None

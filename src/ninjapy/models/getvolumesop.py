"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetVolumesRequestTypedDict(TypedDict):
    df: NotRequired[str]
    r"""Device filter"""
    ts: NotRequired[str]
    r"""Monitoring timestamp filter"""
    cursor: NotRequired[str]
    r"""Cursor name"""
    page_size: NotRequired[int]
    r"""Limit number of records per page"""
    include: NotRequired[str]
    r"""Additional information to include (bl - BitLocker status)"""


class GetVolumesRequest(BaseModel):
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

    include: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Additional information to include (bl - BitLocker status)"""


class GetVolumesCursorTypedDict(TypedDict):
    name: NotRequired[str]
    offset: NotRequired[int]
    count: NotRequired[int]
    expires: NotRequired[float]


class GetVolumesCursor(BaseModel):
    name: Optional[str] = None

    offset: Optional[int] = None

    count: Optional[int] = None

    expires: Optional[float] = None


class GetVolumesConversionStatus(str, Enum):
    r"""Volume encryption or decryption status."""

    FULLY_DECRYPTED = "FULLY_DECRYPTED"
    FULLY_ENCRYPTED = "FULLY_ENCRYPTED"
    ENCRYPTION_IN_PROGRESS = "ENCRYPTION_IN_PROGRESS"
    DECRYPTION_IN_PROGRESS = "DECRYPTION_IN_PROGRESS"
    ENCRYPTION_PAUSED = "ENCRYPTION_PAUSED"
    DECRYPTION_PAUSED = "DECRYPTION_PAUSED"
    UNKNOWN = "UNKNOWN"


class GetVolumesEncryptionMethod(str, Enum):
    r"""Indicated the encryption algorithm and key size used on the volume"""

    NONE = "NONE"
    AES_128_WITH_DIFFUSER = "AES_128_WITH_DIFFUSER"
    AES_256_WITH_DIFFUSER = "AES_256_WITH_DIFFUSER"
    AES_128 = "AES_128"
    AES_256 = "AES_256"
    HARDWARE_ENCRYPTION = "HARDWARE_ENCRYPTION"
    XTS_AES_128 = "XTS_AES_128"
    XTS_AES_256 = "XTS_AES_256"
    UNKNOWN = "UNKNOWN"


class GetVolumesProtectionStatus(str, Enum):
    r"""indicates whether the volume and its encryption key (if any) are secured."""

    UNPROTECTED = "UNPROTECTED"
    PROTECTED = "PROTECTED"
    UNKNOWN = "UNKNOWN"
    PENDING = "PENDING"


class GetVolumesLockStatus(str, Enum):
    r"""Indicates whether the contents of the volume are accessible from Windows"""

    UNKNOWN = "UNKNOWN"
    UNLOCKED = "UNLOCKED"
    LOCKED = "LOCKED"


class GetVolumesBitLockerStatusTypedDict(TypedDict):
    r"""BitLocker Status"""

    conversion_status: NotRequired[GetVolumesConversionStatus]
    r"""Volume encryption or decryption status."""
    encryption_method: NotRequired[GetVolumesEncryptionMethod]
    r"""Indicated the encryption algorithm and key size used on the volume"""
    protection_status: NotRequired[GetVolumesProtectionStatus]
    r"""indicates whether the volume and its encryption key (if any) are secured."""
    lock_status: NotRequired[GetVolumesLockStatus]
    r"""Indicates whether the contents of the volume are accessible from Windows"""
    initialized_for_protection: NotRequired[bool]
    r"""Is initialized for protection"""


class GetVolumesBitLockerStatus(BaseModel):
    r"""BitLocker Status"""

    conversion_status: Annotated[
        Optional[GetVolumesConversionStatus], pydantic.Field(alias="conversionStatus")
    ] = None
    r"""Volume encryption or decryption status."""

    encryption_method: Annotated[
        Optional[GetVolumesEncryptionMethod], pydantic.Field(alias="encryptionMethod")
    ] = None
    r"""Indicated the encryption algorithm and key size used on the volume"""

    protection_status: Annotated[
        Optional[GetVolumesProtectionStatus], pydantic.Field(alias="protectionStatus")
    ] = None
    r"""indicates whether the volume and its encryption key (if any) are secured."""

    lock_status: Annotated[
        Optional[GetVolumesLockStatus], pydantic.Field(alias="lockStatus")
    ] = None
    r"""Indicates whether the contents of the volume are accessible from Windows"""

    initialized_for_protection: Annotated[
        Optional[bool], pydantic.Field(alias="initializedForProtection")
    ] = None
    r"""Is initialized for protection"""


class GetVolumesResultsTypedDict(TypedDict):
    name: NotRequired[str]
    r"""Name"""
    drive_letter: NotRequired[str]
    r"""Drive Letter"""
    label: NotRequired[str]
    r"""Volume Label"""
    device_type: NotRequired[str]
    r"""Device Type"""
    file_system: NotRequired[str]
    r"""File System Type"""
    auto_mount: NotRequired[bool]
    r"""Automatically Mounted"""
    compressed: NotRequired[bool]
    r"""Compressed"""
    capacity: NotRequired[int]
    r"""Capacity (bytes)"""
    free_space: NotRequired[int]
    r"""Free Space (bytes)"""
    serial_number: NotRequired[str]
    r"""Serial Number"""
    bit_locker_status: NotRequired[GetVolumesBitLockerStatusTypedDict]
    r"""BitLocker Status"""
    device_id: NotRequired[int]
    r"""Device identifier"""
    timestamp: NotRequired[float]
    r"""Date/Time when data was collected/updated"""


class GetVolumesResults(BaseModel):
    name: Optional[str] = None
    r"""Name"""

    drive_letter: Annotated[Optional[str], pydantic.Field(alias="driveLetter")] = None
    r"""Drive Letter"""

    label: Optional[str] = None
    r"""Volume Label"""

    device_type: Annotated[Optional[str], pydantic.Field(alias="deviceType")] = None
    r"""Device Type"""

    file_system: Annotated[Optional[str], pydantic.Field(alias="fileSystem")] = None
    r"""File System Type"""

    auto_mount: Annotated[Optional[bool], pydantic.Field(alias="autoMount")] = None
    r"""Automatically Mounted"""

    compressed: Optional[bool] = None
    r"""Compressed"""

    capacity: Optional[int] = None
    r"""Capacity (bytes)"""

    free_space: Annotated[Optional[int], pydantic.Field(alias="freeSpace")] = None
    r"""Free Space (bytes)"""

    serial_number: Annotated[Optional[str], pydantic.Field(alias="serialNumber")] = None
    r"""Serial Number"""

    bit_locker_status: Annotated[
        Optional[GetVolumesBitLockerStatus], pydantic.Field(alias="bitLockerStatus")
    ] = None
    r"""BitLocker Status"""

    device_id: Annotated[Optional[int], pydantic.Field(alias="deviceId")] = None
    r"""Device identifier"""

    timestamp: Optional[float] = None
    r"""Date/Time when data was collected/updated"""


class GetVolumesResponseBodyTypedDict(TypedDict):
    r"""default response"""

    cursor: NotRequired[GetVolumesCursorTypedDict]
    results: NotRequired[List[GetVolumesResultsTypedDict]]


class GetVolumesResponseBody(BaseModel):
    r"""default response"""

    cursor: Optional[GetVolumesCursor] = None

    results: Optional[List[GetVolumesResults]] = None

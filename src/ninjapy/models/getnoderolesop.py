"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetNodeRolesNodeClass(str, Enum):
    r"""Node Class"""

    WINDOWS_SERVER = "WINDOWS_SERVER"
    WINDOWS_WORKSTATION = "WINDOWS_WORKSTATION"
    LINUX_WORKSTATION = "LINUX_WORKSTATION"
    MAC = "MAC"
    ANDROID = "ANDROID"
    APPLE_IOS = "APPLE_IOS"
    APPLE_IPADOS = "APPLE_IPADOS"
    VMWARE_VM_HOST = "VMWARE_VM_HOST"
    VMWARE_VM_GUEST = "VMWARE_VM_GUEST"
    HYPERV_VMM_HOST = "HYPERV_VMM_HOST"
    HYPERV_VMM_GUEST = "HYPERV_VMM_GUEST"
    LINUX_SERVER = "LINUX_SERVER"
    MAC_SERVER = "MAC_SERVER"
    CLOUD_MONITOR_TARGET = "CLOUD_MONITOR_TARGET"
    NMS_SWITCH = "NMS_SWITCH"
    NMS_ROUTER = "NMS_ROUTER"
    NMS_FIREWALL = "NMS_FIREWALL"
    NMS_PRIVATE_NETWORK_GATEWAY = "NMS_PRIVATE_NETWORK_GATEWAY"
    NMS_PRINTER = "NMS_PRINTER"
    NMS_SCANNER = "NMS_SCANNER"
    NMS_DIAL_MANAGER = "NMS_DIAL_MANAGER"
    NMS_WAP = "NMS_WAP"
    NMS_IPSLA = "NMS_IPSLA"
    NMS_COMPUTER = "NMS_COMPUTER"
    NMS_VM_HOST = "NMS_VM_HOST"
    NMS_APPLIANCE = "NMS_APPLIANCE"
    NMS_OTHER = "NMS_OTHER"
    NMS_SERVER = "NMS_SERVER"
    NMS_PHONE = "NMS_PHONE"
    NMS_VIRTUAL_MACHINE = "NMS_VIRTUAL_MACHINE"
    NMS_NETWORK_MANAGEMENT_AGENT = "NMS_NETWORK_MANAGEMENT_AGENT"


class ChassisType(str, Enum):
    r"""Chassis Type"""

    UNKNOWN = "UNKNOWN"
    DESKTOP = "DESKTOP"
    LAPTOP = "LAPTOP"
    MOBILE = "MOBILE"


class GetNodeRolesFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class GetNodeRolesFields(BaseModel):
    r"""Custom Fields"""


class GetNodeRolesResponseBodyTypedDict(TypedDict):
    r"""Device Role"""

    id: NotRequired[int]
    r"""Device Role identifier"""
    name: NotRequired[str]
    r"""Name"""
    description: NotRequired[str]
    r"""Description"""
    node_class: NotRequired[GetNodeRolesNodeClass]
    r"""Node Class"""
    custom: NotRequired[bool]
    r"""Is custom node role?"""
    chassis_type: NotRequired[ChassisType]
    r"""Chassis Type"""
    created: NotRequired[float]
    r"""Date created"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[Dict[str, GetNodeRolesFieldsTypedDict]]
    r"""Custom Fields"""


class GetNodeRolesResponseBody(BaseModel):
    r"""Device Role"""

    id: Optional[int] = None
    r"""Device Role identifier"""

    name: Optional[str] = None
    r"""Name"""

    description: Optional[str] = None
    r"""Description"""

    node_class: Annotated[
        Optional[GetNodeRolesNodeClass], pydantic.Field(alias="nodeClass")
    ] = None
    r"""Node Class"""

    custom: Optional[bool] = None
    r"""Is custom node role?"""

    chassis_type: Annotated[
        Optional[ChassisType], pydantic.Field(alias="chassisType")
    ] = None
    r"""Chassis Type"""

    created: Optional[float] = None
    r"""Date created"""

    tags: Optional[List[str]] = None
    r"""Tags"""

    fields: Optional[Dict[str, GetNodeRolesFields]] = None
    r"""Custom Fields"""

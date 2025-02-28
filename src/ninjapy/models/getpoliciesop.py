"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetPoliciesNodeClass(str, Enum):
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


class GetPoliciesFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class GetPoliciesFields(BaseModel):
    r"""Custom Fields"""


class GetPoliciesResponseBodyTypedDict(TypedDict):
    r"""Assigned policy (overrides organization and location policy mapping)"""

    id: NotRequired[int]
    r"""Policy identifier"""
    parent_policy_id: NotRequired[int]
    r"""Parent Policy identifier"""
    name: NotRequired[str]
    r"""Name"""
    description: NotRequired[str]
    r"""Description"""
    node_class: NotRequired[GetPoliciesNodeClass]
    r"""Node Class"""
    updated: NotRequired[float]
    r"""Last update timestamp"""
    node_class_default: NotRequired[bool]
    r"""Is Default Policy for Node Class"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[Dict[str, GetPoliciesFieldsTypedDict]]
    r"""Custom Fields"""


class GetPoliciesResponseBody(BaseModel):
    r"""Assigned policy (overrides organization and location policy mapping)"""

    id: Optional[int] = None
    r"""Policy identifier"""

    parent_policy_id: Annotated[
        Optional[int], pydantic.Field(alias="parentPolicyId")
    ] = None
    r"""Parent Policy identifier"""

    name: Optional[str] = None
    r"""Name"""

    description: Optional[str] = None
    r"""Description"""

    node_class: Annotated[
        Optional[GetPoliciesNodeClass], pydantic.Field(alias="nodeClass")
    ] = None
    r"""Node Class"""

    updated: Optional[float] = None
    r"""Last update timestamp"""

    node_class_default: Annotated[
        Optional[bool], pydantic.Field(alias="nodeClassDefault")
    ] = None
    r"""Is Default Policy for Node Class"""

    tags: Optional[List[str]] = None
    r"""Tags"""

    fields: Optional[Dict[str, GetPoliciesFields]] = None
    r"""Custom Fields"""

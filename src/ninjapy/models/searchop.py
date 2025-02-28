"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SearchRequestTypedDict(TypedDict):
    q: NotRequired[str]
    r"""Search query (name, logged on user name, IP address, etc.)"""
    limit: NotRequired[int]
    r"""Limit number of devices to return"""


class SearchRequest(BaseModel):
    q: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Search query (name, logged on user name, IP address, etc.)"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Limit number of devices to return"""


class SearchNodeClass(str, Enum):
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


class SearchApprovalStatus(str, Enum):
    r"""Approval Status"""

    PENDING = "PENDING"
    APPROVED = "APPROVED"


class SearchFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class SearchFields(BaseModel):
    r"""Custom Fields"""


class SearchStatus(str, Enum):
    r"""Maintenance mode status"""

    PENDING = "PENDING"
    IN_MAINTENANCE = "IN_MAINTENANCE"
    FAILED = "FAILED"


class SearchMaintenanceTypedDict(TypedDict):
    r"""Maintenance mode status"""

    status: NotRequired[SearchStatus]
    r"""Maintenance mode status"""
    start: NotRequired[float]
    r"""Maintenance mode start time"""
    end: NotRequired[float]
    r"""Maintenance mode end time"""


class SearchMaintenance(BaseModel):
    r"""Maintenance mode status"""

    status: Optional[SearchStatus] = None
    r"""Maintenance mode status"""

    start: Optional[float] = None
    r"""Maintenance mode start time"""

    end: Optional[float] = None
    r"""Maintenance mode end time"""


class SearchNodeApprovalMode(str, Enum):
    r"""Device Approval Mode"""

    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"
    REJECT = "REJECT"


class SearchSystemFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class SearchSystemFields(BaseModel):
    r"""Custom Fields"""


class SearchOrganizationTypedDict(TypedDict):
    r"""Organization"""

    name: NotRequired[str]
    r"""Organization full name"""
    description: NotRequired[str]
    r"""Organization Description"""
    user_data: NotRequired[Dict[str, Any]]
    r"""Custom attributes"""
    node_approval_mode: NotRequired[SearchNodeApprovalMode]
    r"""Device Approval Mode"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[Dict[str, SearchSystemFieldsTypedDict]]
    r"""Custom Fields"""
    id: NotRequired[int]
    r"""Organization identifier"""


class SearchOrganization(BaseModel):
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
        Optional[SearchNodeApprovalMode], pydantic.Field(alias="nodeApprovalMode")
    ] = None
    r"""Device Approval Mode"""

    tags: Optional[List[str]] = None
    r"""Tags"""

    fields: Optional[Dict[str, SearchSystemFields]] = None
    r"""Custom Fields"""

    id: Optional[int] = None
    r"""Organization identifier"""


class SearchSystemResponseFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class SearchSystemResponseFields(BaseModel):
    r"""Custom Fields"""


class SearchLocationTypedDict(TypedDict):
    r"""Location"""

    name: NotRequired[str]
    r"""Location name"""
    address: NotRequired[str]
    r"""Address"""
    description: NotRequired[str]
    r"""Description"""
    user_data: NotRequired[Dict[str, Any]]
    r"""Custom attributes"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[Dict[str, SearchSystemResponseFieldsTypedDict]]
    r"""Custom Fields"""
    id: NotRequired[int]
    r"""Location identifier"""


class SearchLocation(BaseModel):
    r"""Location"""

    name: Optional[str] = None
    r"""Location name"""

    address: Optional[str] = None
    r"""Address"""

    description: Optional[str] = None
    r"""Description"""

    user_data: Annotated[Optional[Dict[str, Any]], pydantic.Field(alias="userData")] = (
        None
    )
    r"""Custom attributes"""

    tags: Optional[List[str]] = None
    r"""Tags"""

    fields: Optional[Dict[str, SearchSystemResponseFields]] = None
    r"""Custom Fields"""

    id: Optional[int] = None
    r"""Location identifier"""


class SearchSystemNodeClass(str, Enum):
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


class SearchSystemResponseDefaultFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class SearchSystemResponseDefaultFields(BaseModel):
    r"""Custom Fields"""


class SearchRolePolicyTypedDict(TypedDict):
    r"""Assigned policy (overrides organization and location policy mapping)"""

    id: NotRequired[int]
    r"""Policy identifier"""
    parent_policy_id: NotRequired[int]
    r"""Parent Policy identifier"""
    name: NotRequired[str]
    r"""Name"""
    description: NotRequired[str]
    r"""Description"""
    node_class: NotRequired[SearchSystemNodeClass]
    r"""Node Class"""
    updated: NotRequired[float]
    r"""Last update timestamp"""
    node_class_default: NotRequired[bool]
    r"""Is Default Policy for Node Class"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[Dict[str, SearchSystemResponseDefaultFieldsTypedDict]]
    r"""Custom Fields"""


class SearchRolePolicy(BaseModel):
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
        Optional[SearchSystemNodeClass], pydantic.Field(alias="nodeClass")
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

    fields: Optional[Dict[str, SearchSystemResponseDefaultFields]] = None
    r"""Custom Fields"""


class SearchSystemResponseNodeClass(str, Enum):
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


class SearchSystemResponseDefaultApplicationJSONFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class SearchSystemResponseDefaultApplicationJSONFields(BaseModel):
    r"""Custom Fields"""


class SearchPolicyTypedDict(TypedDict):
    r"""Assigned policy (overrides organization and location policy mapping)"""

    id: NotRequired[int]
    r"""Policy identifier"""
    parent_policy_id: NotRequired[int]
    r"""Parent Policy identifier"""
    name: NotRequired[str]
    r"""Name"""
    description: NotRequired[str]
    r"""Description"""
    node_class: NotRequired[SearchSystemResponseNodeClass]
    r"""Node Class"""
    updated: NotRequired[float]
    r"""Last update timestamp"""
    node_class_default: NotRequired[bool]
    r"""Is Default Policy for Node Class"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[
        Dict[str, SearchSystemResponseDefaultApplicationJSONFieldsTypedDict]
    ]
    r"""Custom Fields"""


class SearchPolicy(BaseModel):
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
        Optional[SearchSystemResponseNodeClass], pydantic.Field(alias="nodeClass")
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

    fields: Optional[Dict[str, SearchSystemResponseDefaultApplicationJSONFields]] = None
    r"""Custom Fields"""


class SearchSystemResponseDefaultNodeClass(str, Enum):
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


class SearchChassisType(str, Enum):
    r"""Chassis Type"""

    UNKNOWN = "UNKNOWN"
    DESKTOP = "DESKTOP"
    LAPTOP = "LAPTOP"
    MOBILE = "MOBILE"


class SearchSystemResponseDefaultApplicationJSONResponseBodyFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class SearchSystemResponseDefaultApplicationJSONResponseBodyFields(BaseModel):
    r"""Custom Fields"""


class SearchRoleTypedDict(TypedDict):
    r"""Device Role"""

    id: NotRequired[int]
    r"""Device Role identifier"""
    name: NotRequired[str]
    r"""Name"""
    description: NotRequired[str]
    r"""Description"""
    node_class: NotRequired[SearchSystemResponseDefaultNodeClass]
    r"""Node Class"""
    custom: NotRequired[bool]
    r"""Is custom node role?"""
    chassis_type: NotRequired[SearchChassisType]
    r"""Chassis Type"""
    created: NotRequired[float]
    r"""Date created"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[
        Dict[str, SearchSystemResponseDefaultApplicationJSONResponseBodyFieldsTypedDict]
    ]
    r"""Custom Fields"""


class SearchRole(BaseModel):
    r"""Device Role"""

    id: Optional[int] = None
    r"""Device Role identifier"""

    name: Optional[str] = None
    r"""Name"""

    description: Optional[str] = None
    r"""Description"""

    node_class: Annotated[
        Optional[SearchSystemResponseDefaultNodeClass],
        pydantic.Field(alias="nodeClass"),
    ] = None
    r"""Node Class"""

    custom: Optional[bool] = None
    r"""Is custom node role?"""

    chassis_type: Annotated[
        Optional[SearchChassisType], pydantic.Field(alias="chassisType")
    ] = None
    r"""Chassis Type"""

    created: Optional[float] = None
    r"""Date created"""

    tags: Optional[List[str]] = None
    r"""Tags"""

    fields: Optional[
        Dict[str, SearchSystemResponseDefaultApplicationJSONResponseBodyFields]
    ] = None
    r"""Custom Fields"""


class SearchBackupUsageTypedDict(TypedDict):
    r"""Device Backup Usage"""

    revisions_current_size: NotRequired[int]
    r"""Revisions current size"""
    revisions_previous_size: NotRequired[int]
    r"""Revisions previous size"""
    revisions_deleted_size: NotRequired[int]
    r"""Revisions deleted size"""
    local_file_folder_size: NotRequired[int]
    r"""Revisions local file folder size"""
    local_image_size: NotRequired[int]
    r"""Revisions local image size"""
    local_image_v2_size: NotRequired[int]
    r"""Revisions local image v2 size"""
    cloud_file_folder_size: NotRequired[int]
    r"""Revisions cloud file folder size"""
    cloud_image_size: NotRequired[int]
    r"""Revisions cloud image size"""
    cloud_image_v2_size: NotRequired[int]
    r"""Revisions cloud image v2 size"""
    last_successful_backup_job: NotRequired[float]
    r"""Last successful job. This is provided when the 'includeLastBackupJobTimes' query parameter is set to 'true'"""
    last_failed_backup_job: NotRequired[float]
    r"""Last failed job. This is provided when the 'includeLastBackupJobTimes' query parameter is set to 'true'"""
    revisions_total_size: NotRequired[int]
    r"""Revisions total size"""
    cloud_total_size: NotRequired[int]
    r"""Revisions cloud total size"""
    local_total_size: NotRequired[int]
    r"""Revisions local total size"""


class SearchBackupUsage(BaseModel):
    r"""Device Backup Usage"""

    revisions_current_size: Annotated[
        Optional[int], pydantic.Field(alias="revisionsCurrentSize")
    ] = None
    r"""Revisions current size"""

    revisions_previous_size: Annotated[
        Optional[int], pydantic.Field(alias="revisionsPreviousSize")
    ] = None
    r"""Revisions previous size"""

    revisions_deleted_size: Annotated[
        Optional[int], pydantic.Field(alias="revisionsDeletedSize")
    ] = None
    r"""Revisions deleted size"""

    local_file_folder_size: Annotated[
        Optional[int], pydantic.Field(alias="localFileFolderSize")
    ] = None
    r"""Revisions local file folder size"""

    local_image_size: Annotated[
        Optional[int], pydantic.Field(alias="localImageSize")
    ] = None
    r"""Revisions local image size"""

    local_image_v2_size: Annotated[
        Optional[int], pydantic.Field(alias="localImageV2Size")
    ] = None
    r"""Revisions local image v2 size"""

    cloud_file_folder_size: Annotated[
        Optional[int], pydantic.Field(alias="cloudFileFolderSize")
    ] = None
    r"""Revisions cloud file folder size"""

    cloud_image_size: Annotated[
        Optional[int], pydantic.Field(alias="cloudImageSize")
    ] = None
    r"""Revisions cloud image size"""

    cloud_image_v2_size: Annotated[
        Optional[int], pydantic.Field(alias="cloudImageV2Size")
    ] = None
    r"""Revisions cloud image v2 size"""

    last_successful_backup_job: Annotated[
        Optional[float], pydantic.Field(alias="lastSuccessfulBackupJob")
    ] = None
    r"""Last successful job. This is provided when the 'includeLastBackupJobTimes' query parameter is set to 'true'"""

    last_failed_backup_job: Annotated[
        Optional[float], pydantic.Field(alias="lastFailedBackupJob")
    ] = None
    r"""Last failed job. This is provided when the 'includeLastBackupJobTimes' query parameter is set to 'true'"""

    revisions_total_size: Annotated[
        Optional[int], pydantic.Field(alias="revisionsTotalSize")
    ] = None
    r"""Revisions total size"""

    cloud_total_size: Annotated[
        Optional[int], pydantic.Field(alias="cloudTotalSize")
    ] = None
    r"""Revisions cloud total size"""

    local_total_size: Annotated[
        Optional[int], pydantic.Field(alias="localTotalSize")
    ] = None
    r"""Revisions local total size"""


class SearchWarrantyTypedDict(TypedDict):
    r"""Warranty Info"""

    start_date: NotRequired[float]
    r"""Warranty Start Date (Seconds)"""
    end_date: NotRequired[float]
    r"""Warranty End Date (Seconds)"""
    manufacturer_fulfillment_date: NotRequired[float]
    r"""Manufacturer Fulfillment Date"""


class SearchWarranty(BaseModel):
    r"""Warranty Info"""

    start_date: Annotated[Optional[float], pydantic.Field(alias="startDate")] = None
    r"""Warranty Start Date (Seconds)"""

    end_date: Annotated[Optional[float], pydantic.Field(alias="endDate")] = None
    r"""Warranty End Date (Seconds)"""

    manufacturer_fulfillment_date: Annotated[
        Optional[float], pydantic.Field(alias="manufacturerFulfillmentDate")
    ] = None
    r"""Manufacturer Fulfillment Date"""


class SearchReferencesTypedDict(TypedDict):
    r"""Expanded entity references"""

    organization: NotRequired[SearchOrganizationTypedDict]
    r"""Organization"""
    location: NotRequired[SearchLocationTypedDict]
    r"""Location"""
    role_policy: NotRequired[SearchRolePolicyTypedDict]
    r"""Assigned policy (overrides organization and location policy mapping)"""
    policy: NotRequired[SearchPolicyTypedDict]
    r"""Assigned policy (overrides organization and location policy mapping)"""
    role: NotRequired[SearchRoleTypedDict]
    r"""Device Role"""
    backup_usage: NotRequired[SearchBackupUsageTypedDict]
    r"""Device Backup Usage"""
    warranty: NotRequired[SearchWarrantyTypedDict]
    r"""Warranty Info"""


class SearchReferences(BaseModel):
    r"""Expanded entity references"""

    organization: Optional[SearchOrganization] = None
    r"""Organization"""

    location: Optional[SearchLocation] = None
    r"""Location"""

    role_policy: Annotated[
        Optional[SearchRolePolicy], pydantic.Field(alias="rolePolicy")
    ] = None
    r"""Assigned policy (overrides organization and location policy mapping)"""

    policy: Optional[SearchPolicy] = None
    r"""Assigned policy (overrides organization and location policy mapping)"""

    role: Optional[SearchRole] = None
    r"""Device Role"""

    backup_usage: Annotated[
        Optional[SearchBackupUsage], pydantic.Field(alias="backupUsage")
    ] = None
    r"""Device Backup Usage"""

    warranty: Optional[SearchWarranty] = None
    r"""Warranty Info"""


class SearchDevicesTypedDict(TypedDict):
    r"""Devices matching search query"""

    id: NotRequired[int]
    r"""Node (Device) identifier"""
    parent_device_id: NotRequired[int]
    r"""Parent Node identifier"""
    organization_id: NotRequired[int]
    r"""Organization identifier"""
    location_id: NotRequired[int]
    r"""Location identifier"""
    node_class: NotRequired[SearchNodeClass]
    r"""Node Class"""
    node_role_id: NotRequired[int]
    r"""Node Role identifier"""
    role_policy_id: NotRequired[int]
    r"""Node Role policy ID based on organization and location Policy Mapping"""
    policy_id: NotRequired[int]
    r"""Assigned policy ID (overrides organization and location policy mapping)"""
    approval_status: NotRequired[SearchApprovalStatus]
    r"""Approval Status"""
    offline: NotRequired[bool]
    r"""Is Offline?"""
    display_name: NotRequired[str]
    r"""Display Name"""
    system_name: NotRequired[str]
    r"""System Name"""
    dns_name: NotRequired[str]
    r"""DNS Name"""
    netbios_name: NotRequired[str]
    r"""NETBIOS Name"""
    created: NotRequired[float]
    r"""Created"""
    last_contact: NotRequired[float]
    r"""Last Contact"""
    last_update: NotRequired[float]
    r"""Last data submission timestamp"""
    user_data: NotRequired[Dict[str, Any]]
    r"""Custom attributes"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[Dict[str, SearchFieldsTypedDict]]
    r"""Custom Fields"""
    maintenance: NotRequired[SearchMaintenanceTypedDict]
    r"""Maintenance mode status"""
    references: NotRequired[SearchReferencesTypedDict]
    r"""Expanded entity references"""
    score: NotRequired[int]
    r"""Match score"""
    match_attr: NotRequired[str]
    r"""Name of the attribute that matched the query"""
    match_attr_value: NotRequired[str]
    r"""Value of that attribute that matched"""


class SearchDevices(BaseModel):
    r"""Devices matching search query"""

    id: Optional[int] = None
    r"""Node (Device) identifier"""

    parent_device_id: Annotated[
        Optional[int], pydantic.Field(alias="parentDeviceId")
    ] = None
    r"""Parent Node identifier"""

    organization_id: Annotated[
        Optional[int], pydantic.Field(alias="organizationId")
    ] = None
    r"""Organization identifier"""

    location_id: Annotated[Optional[int], pydantic.Field(alias="locationId")] = None
    r"""Location identifier"""

    node_class: Annotated[
        Optional[SearchNodeClass], pydantic.Field(alias="nodeClass")
    ] = None
    r"""Node Class"""

    node_role_id: Annotated[Optional[int], pydantic.Field(alias="nodeRoleId")] = None
    r"""Node Role identifier"""

    role_policy_id: Annotated[Optional[int], pydantic.Field(alias="rolePolicyId")] = (
        None
    )
    r"""Node Role policy ID based on organization and location Policy Mapping"""

    policy_id: Annotated[Optional[int], pydantic.Field(alias="policyId")] = None
    r"""Assigned policy ID (overrides organization and location policy mapping)"""

    approval_status: Annotated[
        Optional[SearchApprovalStatus], pydantic.Field(alias="approvalStatus")
    ] = None
    r"""Approval Status"""

    offline: Optional[bool] = None
    r"""Is Offline?"""

    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""Display Name"""

    system_name: Annotated[Optional[str], pydantic.Field(alias="systemName")] = None
    r"""System Name"""

    dns_name: Annotated[Optional[str], pydantic.Field(alias="dnsName")] = None
    r"""DNS Name"""

    netbios_name: Annotated[Optional[str], pydantic.Field(alias="netbiosName")] = None
    r"""NETBIOS Name"""

    created: Optional[float] = None
    r"""Created"""

    last_contact: Annotated[Optional[float], pydantic.Field(alias="lastContact")] = None
    r"""Last Contact"""

    last_update: Annotated[Optional[float], pydantic.Field(alias="lastUpdate")] = None
    r"""Last data submission timestamp"""

    user_data: Annotated[Optional[Dict[str, Any]], pydantic.Field(alias="userData")] = (
        None
    )
    r"""Custom attributes"""

    tags: Optional[List[str]] = None
    r"""Tags"""

    fields: Optional[Dict[str, SearchFields]] = None
    r"""Custom Fields"""

    maintenance: Optional[SearchMaintenance] = None
    r"""Maintenance mode status"""

    references: Optional[SearchReferences] = None
    r"""Expanded entity references"""

    score: Optional[int] = None
    r"""Match score"""

    match_attr: Annotated[Optional[str], pydantic.Field(alias="matchAttr")] = None
    r"""Name of the attribute that matched the query"""

    match_attr_value: Annotated[
        Optional[str], pydantic.Field(alias="matchAttrValue")
    ] = None
    r"""Value of that attribute that matched"""


class SearchResponseBodyTypedDict(TypedDict):
    r"""default response"""

    query: NotRequired[str]
    r"""Search query"""
    devices: NotRequired[List[SearchDevicesTypedDict]]
    r"""Devices matching search query"""


class SearchResponseBody(BaseModel):
    r"""default response"""

    query: Optional[str] = None
    r"""Search query"""

    devices: Optional[List[SearchDevices]] = None
    r"""Devices matching search query"""

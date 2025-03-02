"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetDeviceAlertsRequestTypedDict(TypedDict):
    id: int
    r"""Device identifier"""
    lang: NotRequired[str]
    tz: NotRequired[str]
    r"""Time Zone"""


class GetDeviceAlertsRequest(BaseModel):
    id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Device identifier"""

    lang: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    tz: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Time Zone"""


class GetDeviceAlertsSourceType(str, Enum):
    r"""Alert origin"""

    AGENT_OFFLINE = "AGENT_OFFLINE"
    CONDITION_AGENT_CPU = "CONDITION_AGENT_CPU"
    CONDITION_AGENT_MEMORY = "CONDITION_AGENT_MEMORY"
    CONDITION_AGENT_NETWORK = "CONDITION_AGENT_NETWORK"
    CONDITION_AGENT_DISK_IO = "CONDITION_AGENT_DISK_IO"
    CONDITION_AGENT_DISK_FREE_SPACE = "CONDITION_AGENT_DISK_FREE_SPACE"
    CONDITION_AGENT_DISK_USAGE = "CONDITION_AGENT_DISK_USAGE"
    CONDITION_AGENT_CVSS_SCORE = "CONDITION_AGENT_CVSS_SCORE"
    CONDITION_AGENT_PATCH_LAST_INSTALLED = "CONDITION_AGENT_PATCH_LAST_INSTALLED"
    CONDITION_NMS_CPU = "CONDITION_NMS_CPU"
    CONDITION_NMS_MEMORY = "CONDITION_NMS_MEMORY"
    CONDITION_NMS_NETWORK_TRAFFIC_BITS = "CONDITION_NMS_NETWORK_TRAFFIC_BITS"
    CONDITION_NMS_NETWORK_TRAFFIC_PERCENT = "CONDITION_NMS_NETWORK_TRAFFIC_PERCENT"
    CONDITION_NMS_NETWORK_STATUS = "CONDITION_NMS_NETWORK_STATUS"
    CONDITION_NMS_NETWORK_STATUS_CHANGE = "CONDITION_NMS_NETWORK_STATUS_CHANGE"
    CONDITION_NMS_SYSTEM_UPTIME = "CONDITION_NMS_SYSTEM_UPTIME"
    CONDITION_PING = "CONDITION_PING"
    CONDITION_PING_LATENCY = "CONDITION_PING_LATENCY"
    CONDITION_PING_PACKET_LOSS = "CONDITION_PING_PACKET_LOSS"
    CONDITION_PING_RESPONSE = "CONDITION_PING_RESPONSE"
    CONDITION_SYSTEM_UPTIME = "CONDITION_SYSTEM_UPTIME"
    CONDITION_SMART_STATUS_DEGRATED = "CONDITION_SMART_STATUS_DEGRATED"
    CONDITION_RAID_HEALTH_STATUS = "CONDITION_RAID_HEALTH_STATUS"
    CONDITION_SCRIPT_RESULT = "CONDITION_SCRIPT_RESULT"
    CONDITION_HTTP = "CONDITION_HTTP"
    CONDITION_HTTP_RESPONSE = "CONDITION_HTTP_RESPONSE"
    CONDITION_PORT = "CONDITION_PORT"
    CONDITION_PORT_SCAN = "CONDITION_PORT_SCAN"
    CONDITION_SYSLOG = "CONDITION_SYSLOG"
    CONDITION_CONFIGURATION_FILE = "CONDITION_CONFIGURATION_FILE"
    CONDITION_SNMPTRAP = "CONDITION_SNMPTRAP"
    CONDITION_CRITICAL_EVENT = "CONDITION_CRITICAL_EVENT"
    CONDITION_DNS = "CONDITION_DNS"
    CONDITION_EMAIL = "CONDITION_EMAIL"
    CONDITION_CUSTOM_SNMP = "CONDITION_CUSTOM_SNMP"
    CONDITION_COMPOUND = "CONDITION_COMPOUND"
    SHADOWPROTECT_BACKUPJOB_CREATE = "SHADOWPROTECT_BACKUPJOB_CREATE"
    SHADOWPROTECT_BACKUPJOB_UPDATE = "SHADOWPROTECT_BACKUPJOB_UPDATE"
    SHADOWPROTECT_BACKUPJOB_DELETE = "SHADOWPROTECT_BACKUPJOB_DELETE"
    SHADOWPROTECT_BACKUPJOB_EXECUTE = "SHADOWPROTECT_BACKUPJOB_EXECUTE"
    IMAGEMANAGER_MANAGEDFOLDER_CREATE = "IMAGEMANAGER_MANAGEDFOLDER_CREATE"
    IMAGEMANAGER_MANAGEDFOLDER_UPDATE = "IMAGEMANAGER_MANAGEDFOLDER_UPDATE"
    IMAGEMANAGER_MANAGEDFOLDER_DELETE = "IMAGEMANAGER_MANAGEDFOLDER_DELETE"
    IMAGEMANAGER_MANAGEDFOLDER_EXECUTE = "IMAGEMANAGER_MANAGEDFOLDER_EXECUTE"
    TEAMVIEWER_CONNECTION = "TEAMVIEWER_CONNECTION"
    RETRIEVE_AGENT_LOGS = "RETRIEVE_AGENT_LOGS"
    SCHEDULED_TASK = "SCHEDULED_TASK"
    CONDITION_WINDOWS_EVENT_LOG_TRIGGERED = "CONDITION_WINDOWS_EVENT_LOG_TRIGGERED"
    CONDITION_WINDOWS_SERVICE_STATE_CHANGED = "CONDITION_WINDOWS_SERVICE_STATE_CHANGED"
    UI_MESSAGE_ACTION_REBOOT = "UI_MESSAGE_ACTION_REBOOT"
    UI_MESSAGE_BD_INSTALLATION_ISSUES = "UI_MESSAGE_BD_INSTALLATION_ISSUES"
    GRAVITYZONE_UI_MESSAGE_INSTALLATION_ISSUES = (
        "GRAVITYZONE_UI_MESSAGE_INSTALLATION_ISSUES"
    )
    AV_QUARANTINE_THREAT = "AV_QUARANTINE_THREAT"
    AV_RESTORE_THREAT = "AV_RESTORE_THREAT"
    AV_DELETE_THREAT = "AV_DELETE_THREAT"
    AV_REMOVE_THREAT = "AV_REMOVE_THREAT"
    BITDEFENDER_RESTORE_THREAT = "BITDEFENDER_RESTORE_THREAT"
    BITDEFENDER_DELETE_THREAT = "BITDEFENDER_DELETE_THREAT"
    CONDITION_BITLOCKER_STATUS = "CONDITION_BITLOCKER_STATUS"
    CONDITION_FILEVAULT_STATUS = "CONDITION_FILEVAULT_STATUS"
    CONDITION_LINUX_PROCESS = "CONDITION_LINUX_PROCESS"
    CONDITION_LINUX_DAEMON = "CONDITION_LINUX_Daemon"
    CONDITION_LINUX_PROCESS_RESOURCE = "CONDITION_LINUX_PROCESS_RESOURCE"
    CONDITION_LINUX_PROCESS_RESOURCE_CPU = "CONDITION_LINUX_PROCESS_RESOURCE_CPU"
    CONDITION_LINUX_PROCESS_RESOURCE_MEMORY = "CONDITION_LINUX_PROCESS_RESOURCE_MEMORY"
    CONDITION_LINUX_DISK_FREE_SPACE = "CONDITION_LINUX_DISK_FREE_SPACE"
    CONDITION_LINUX_DISK_USAGE = "CONDITION_LINUX_DISK_USAGE"
    CONDITION_VM_AGGREGATE_CPU_USAGE = "CONDITION_VM_AGGREGATE_CPU_USAGE"
    CONDITION_VM_DISK_USAGE = "CONDITION_VM_DISK_USAGE"
    CONDITION_VM_HOST_DATASTORE = "CONDITION_VM_HOST_DATASTORE"
    CONDITION_VM_HOST_UPTIME = "CONDITION_VM_HOST_UPTIME"
    CONDITION_VM_HOST_DEVICE_DOWN = "CONDITION_VM_HOST_DEVICE_DOWN"
    CONDITION_VM_HOST_BAD_SENSORS = "CONDITION_VM_HOST_BAD_SENSORS"
    CONDITION_VM_HOST_SENSOR_HEALTH = "CONDITION_VM_HOST_SENSOR_HEALTH"
    CONDITION_VM_GUEST_GUEST_OPERATIONAL_MODE = (
        "CONDITION_VM_GUEST_GUEST_OPERATIONAL_MODE"
    )
    CONDITION_VM_GUEST_SNAPSHOT_SIZE = "CONDITION_VM_GUEST_SNAPSHOT_SIZE"
    CONDITION_VM_GUEST_SNAPSHOT_LIFESPAN = "CONDITION_VM_GUEST_SNAPSHOT_LIFESPAN"
    CONDITION_VM_GUEST_TOOLS_NOT_RUNNING = "CONDITION_VM_GUEST_TOOLS_NOT_RUNNING"
    CONDITION_HV_GUEST_CHECKPOINT_SIZE = "CONDITION_HV_GUEST_CHECKPOINT_SIZE"
    CONDITION_HV_GUEST_CHECKPOINT_LIFESPAN = "CONDITION_HV_GUEST_CHECKPOINT_LIFESPAN"
    CONDITION_SOFTWARE = "CONDITION_SOFTWARE"
    CONDITION_WINDOWS_PROCESS_STATE = "CONDITION_WINDOWS_PROCESS_STATE"
    CONDITION_WINDOWS_PROCESS_RESOURCE_CPU = "CONDITION_WINDOWS_PROCESS_RESOURCE_CPU"
    CONDITION_WINDOWS_PROCESS_RESOURCE_MEMORY = (
        "CONDITION_WINDOWS_PROCESS_RESOURCE_MEMORY"
    )
    CONDITION_MAC_PROCESS_STATE = "CONDITION_MAC_PROCESS_STATE"
    CONDITION_MAC_PROCESS_RESOURCE_CPU = "CONDITION_MAC_PROCESS_RESOURCE_CPU"
    CONDITION_MAC_PROCESS_RESOURCE_MEMORY = "CONDITION_MAC_PROCESS_RESOURCE_MEMORY"
    CONDITION_MAC_DEAMON = "CONDITION_MAC_DEAMON"
    CONDITION_CUSTOM_FIELD = "CONDITION_CUSTOM_FIELD"
    CONDITION_PENDING_REBOOT = "CONDITION_PENDING_REBOOT"


class GetDeviceAlertsPsaTicketIDTypedDict(TypedDict):
    r"""Related PSA ticket ID"""


class GetDeviceAlertsPsaTicketID(BaseModel):
    r"""Related PSA ticket ID"""


class GetDeviceAlertsNodeClass(str, Enum):
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


class GetDeviceAlertsApprovalStatus(str, Enum):
    r"""Approval Status"""

    PENDING = "PENDING"
    APPROVED = "APPROVED"


class GetDeviceAlertsFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class GetDeviceAlertsFields(BaseModel):
    r"""Custom Fields"""


class GetDeviceAlertsStatus(str, Enum):
    r"""Maintenance mode status"""

    PENDING = "PENDING"
    IN_MAINTENANCE = "IN_MAINTENANCE"
    FAILED = "FAILED"


class GetDeviceAlertsMaintenanceTypedDict(TypedDict):
    r"""Maintenance mode status"""

    status: NotRequired[GetDeviceAlertsStatus]
    r"""Maintenance mode status"""
    start: NotRequired[float]
    r"""Maintenance mode start time"""
    end: NotRequired[float]
    r"""Maintenance mode end time"""


class GetDeviceAlertsMaintenance(BaseModel):
    r"""Maintenance mode status"""

    status: Optional[GetDeviceAlertsStatus] = None
    r"""Maintenance mode status"""

    start: Optional[float] = None
    r"""Maintenance mode start time"""

    end: Optional[float] = None
    r"""Maintenance mode end time"""


class GetDeviceAlertsNodeApprovalMode(str, Enum):
    r"""Device Approval Mode"""

    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"
    REJECT = "REJECT"


class GetDeviceAlertsDevicesFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class GetDeviceAlertsDevicesFields(BaseModel):
    r"""Custom Fields"""


class GetDeviceAlertsOrganizationTypedDict(TypedDict):
    r"""Organization"""

    name: NotRequired[str]
    r"""Organization full name"""
    description: NotRequired[str]
    r"""Organization Description"""
    user_data: NotRequired[Dict[str, Any]]
    r"""Custom attributes"""
    node_approval_mode: NotRequired[GetDeviceAlertsNodeApprovalMode]
    r"""Device Approval Mode"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[Dict[str, GetDeviceAlertsDevicesFieldsTypedDict]]
    r"""Custom Fields"""
    id: NotRequired[int]
    r"""Organization identifier"""


class GetDeviceAlertsOrganization(BaseModel):
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
        Optional[GetDeviceAlertsNodeApprovalMode],
        pydantic.Field(alias="nodeApprovalMode"),
    ] = None
    r"""Device Approval Mode"""

    tags: Optional[List[str]] = None
    r"""Tags"""

    fields: Optional[Dict[str, GetDeviceAlertsDevicesFields]] = None
    r"""Custom Fields"""

    id: Optional[int] = None
    r"""Organization identifier"""


class GetDeviceAlertsDevicesResponseFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class GetDeviceAlertsDevicesResponseFields(BaseModel):
    r"""Custom Fields"""


class GetDeviceAlertsLocationTypedDict(TypedDict):
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
    fields: NotRequired[Dict[str, GetDeviceAlertsDevicesResponseFieldsTypedDict]]
    r"""Custom Fields"""
    id: NotRequired[int]
    r"""Location identifier"""


class GetDeviceAlertsLocation(BaseModel):
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

    fields: Optional[Dict[str, GetDeviceAlertsDevicesResponseFields]] = None
    r"""Custom Fields"""

    id: Optional[int] = None
    r"""Location identifier"""


class GetDeviceAlertsDevicesNodeClass(str, Enum):
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


class GetDeviceAlertsDevicesResponseDefaultFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class GetDeviceAlertsDevicesResponseDefaultFields(BaseModel):
    r"""Custom Fields"""


class GetDeviceAlertsRolePolicyTypedDict(TypedDict):
    r"""Assigned policy (overrides organization and location policy mapping)"""

    id: NotRequired[int]
    r"""Policy identifier"""
    parent_policy_id: NotRequired[int]
    r"""Parent Policy identifier"""
    name: NotRequired[str]
    r"""Name"""
    description: NotRequired[str]
    r"""Description"""
    node_class: NotRequired[GetDeviceAlertsDevicesNodeClass]
    r"""Node Class"""
    updated: NotRequired[float]
    r"""Last update timestamp"""
    node_class_default: NotRequired[bool]
    r"""Is Default Policy for Node Class"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[Dict[str, GetDeviceAlertsDevicesResponseDefaultFieldsTypedDict]]
    r"""Custom Fields"""


class GetDeviceAlertsRolePolicy(BaseModel):
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
        Optional[GetDeviceAlertsDevicesNodeClass], pydantic.Field(alias="nodeClass")
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

    fields: Optional[Dict[str, GetDeviceAlertsDevicesResponseDefaultFields]] = None
    r"""Custom Fields"""


class GetDeviceAlertsDevicesResponseNodeClass(str, Enum):
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


class GetDeviceAlertsDevicesResponseDefaultApplicationJSONFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class GetDeviceAlertsDevicesResponseDefaultApplicationJSONFields(BaseModel):
    r"""Custom Fields"""


class GetDeviceAlertsPolicyTypedDict(TypedDict):
    r"""Assigned policy (overrides organization and location policy mapping)"""

    id: NotRequired[int]
    r"""Policy identifier"""
    parent_policy_id: NotRequired[int]
    r"""Parent Policy identifier"""
    name: NotRequired[str]
    r"""Name"""
    description: NotRequired[str]
    r"""Description"""
    node_class: NotRequired[GetDeviceAlertsDevicesResponseNodeClass]
    r"""Node Class"""
    updated: NotRequired[float]
    r"""Last update timestamp"""
    node_class_default: NotRequired[bool]
    r"""Is Default Policy for Node Class"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[
        Dict[str, GetDeviceAlertsDevicesResponseDefaultApplicationJSONFieldsTypedDict]
    ]
    r"""Custom Fields"""


class GetDeviceAlertsPolicy(BaseModel):
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
        Optional[GetDeviceAlertsDevicesResponseNodeClass],
        pydantic.Field(alias="nodeClass"),
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

    fields: Optional[
        Dict[str, GetDeviceAlertsDevicesResponseDefaultApplicationJSONFields]
    ] = None
    r"""Custom Fields"""


class GetDeviceAlertsDevicesResponseDefaultNodeClass(str, Enum):
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


class GetDeviceAlertsChassisType(str, Enum):
    r"""Chassis Type"""

    UNKNOWN = "UNKNOWN"
    DESKTOP = "DESKTOP"
    LAPTOP = "LAPTOP"
    MOBILE = "MOBILE"


class GetDeviceAlertsDevicesResponseDefaultApplicationJSONResponseBodyFieldsTypedDict(
    TypedDict
):
    r"""Custom Fields"""


class GetDeviceAlertsDevicesResponseDefaultApplicationJSONResponseBodyFields(BaseModel):
    r"""Custom Fields"""


class GetDeviceAlertsRoleTypedDict(TypedDict):
    r"""Device Role"""

    id: NotRequired[int]
    r"""Device Role identifier"""
    name: NotRequired[str]
    r"""Name"""
    description: NotRequired[str]
    r"""Description"""
    node_class: NotRequired[GetDeviceAlertsDevicesResponseDefaultNodeClass]
    r"""Node Class"""
    custom: NotRequired[bool]
    r"""Is custom node role?"""
    chassis_type: NotRequired[GetDeviceAlertsChassisType]
    r"""Chassis Type"""
    created: NotRequired[float]
    r"""Date created"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[
        Dict[
            str,
            GetDeviceAlertsDevicesResponseDefaultApplicationJSONResponseBodyFieldsTypedDict,
        ]
    ]
    r"""Custom Fields"""


class GetDeviceAlertsRole(BaseModel):
    r"""Device Role"""

    id: Optional[int] = None
    r"""Device Role identifier"""

    name: Optional[str] = None
    r"""Name"""

    description: Optional[str] = None
    r"""Description"""

    node_class: Annotated[
        Optional[GetDeviceAlertsDevicesResponseDefaultNodeClass],
        pydantic.Field(alias="nodeClass"),
    ] = None
    r"""Node Class"""

    custom: Optional[bool] = None
    r"""Is custom node role?"""

    chassis_type: Annotated[
        Optional[GetDeviceAlertsChassisType], pydantic.Field(alias="chassisType")
    ] = None
    r"""Chassis Type"""

    created: Optional[float] = None
    r"""Date created"""

    tags: Optional[List[str]] = None
    r"""Tags"""

    fields: Optional[
        Dict[
            str, GetDeviceAlertsDevicesResponseDefaultApplicationJSONResponseBodyFields
        ]
    ] = None
    r"""Custom Fields"""


class GetDeviceAlertsBackupUsageTypedDict(TypedDict):
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


class GetDeviceAlertsBackupUsage(BaseModel):
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


class GetDeviceAlertsWarrantyTypedDict(TypedDict):
    r"""Warranty Info"""

    start_date: NotRequired[float]
    r"""Warranty Start Date (Seconds)"""
    end_date: NotRequired[float]
    r"""Warranty End Date (Seconds)"""
    manufacturer_fulfillment_date: NotRequired[float]
    r"""Manufacturer Fulfillment Date"""


class GetDeviceAlertsWarranty(BaseModel):
    r"""Warranty Info"""

    start_date: Annotated[Optional[float], pydantic.Field(alias="startDate")] = None
    r"""Warranty Start Date (Seconds)"""

    end_date: Annotated[Optional[float], pydantic.Field(alias="endDate")] = None
    r"""Warranty End Date (Seconds)"""

    manufacturer_fulfillment_date: Annotated[
        Optional[float], pydantic.Field(alias="manufacturerFulfillmentDate")
    ] = None
    r"""Manufacturer Fulfillment Date"""


class GetDeviceAlertsReferencesTypedDict(TypedDict):
    r"""Expanded entity references"""

    organization: NotRequired[GetDeviceAlertsOrganizationTypedDict]
    r"""Organization"""
    location: NotRequired[GetDeviceAlertsLocationTypedDict]
    r"""Location"""
    role_policy: NotRequired[GetDeviceAlertsRolePolicyTypedDict]
    r"""Assigned policy (overrides organization and location policy mapping)"""
    policy: NotRequired[GetDeviceAlertsPolicyTypedDict]
    r"""Assigned policy (overrides organization and location policy mapping)"""
    role: NotRequired[GetDeviceAlertsRoleTypedDict]
    r"""Device Role"""
    backup_usage: NotRequired[GetDeviceAlertsBackupUsageTypedDict]
    r"""Device Backup Usage"""
    warranty: NotRequired[GetDeviceAlertsWarrantyTypedDict]
    r"""Warranty Info"""


class GetDeviceAlertsReferences(BaseModel):
    r"""Expanded entity references"""

    organization: Optional[GetDeviceAlertsOrganization] = None
    r"""Organization"""

    location: Optional[GetDeviceAlertsLocation] = None
    r"""Location"""

    role_policy: Annotated[
        Optional[GetDeviceAlertsRolePolicy], pydantic.Field(alias="rolePolicy")
    ] = None
    r"""Assigned policy (overrides organization and location policy mapping)"""

    policy: Optional[GetDeviceAlertsPolicy] = None
    r"""Assigned policy (overrides organization and location policy mapping)"""

    role: Optional[GetDeviceAlertsRole] = None
    r"""Device Role"""

    backup_usage: Annotated[
        Optional[GetDeviceAlertsBackupUsage], pydantic.Field(alias="backupUsage")
    ] = None
    r"""Device Backup Usage"""

    warranty: Optional[GetDeviceAlertsWarranty] = None
    r"""Warranty Info"""


class GetDeviceAlertsDeviceTypedDict(TypedDict):
    r"""Device information."""

    id: NotRequired[int]
    r"""Node (Device) identifier"""
    parent_device_id: NotRequired[int]
    r"""Parent Node identifier"""
    organization_id: NotRequired[int]
    r"""Organization identifier"""
    location_id: NotRequired[int]
    r"""Location identifier"""
    node_class: NotRequired[GetDeviceAlertsNodeClass]
    r"""Node Class"""
    node_role_id: NotRequired[int]
    r"""Node Role identifier"""
    role_policy_id: NotRequired[int]
    r"""Node Role policy ID based on organization and location Policy Mapping"""
    policy_id: NotRequired[int]
    r"""Assigned policy ID (overrides organization and location policy mapping)"""
    approval_status: NotRequired[GetDeviceAlertsApprovalStatus]
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
    fields: NotRequired[Dict[str, GetDeviceAlertsFieldsTypedDict]]
    r"""Custom Fields"""
    maintenance: NotRequired[GetDeviceAlertsMaintenanceTypedDict]
    r"""Maintenance mode status"""
    references: NotRequired[GetDeviceAlertsReferencesTypedDict]
    r"""Expanded entity references"""


class GetDeviceAlertsDevice(BaseModel):
    r"""Device information."""

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
        Optional[GetDeviceAlertsNodeClass], pydantic.Field(alias="nodeClass")
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
        Optional[GetDeviceAlertsApprovalStatus], pydantic.Field(alias="approvalStatus")
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

    fields: Optional[Dict[str, GetDeviceAlertsFields]] = None
    r"""Custom Fields"""

    maintenance: Optional[GetDeviceAlertsMaintenance] = None
    r"""Maintenance mode status"""

    references: Optional[GetDeviceAlertsReferences] = None
    r"""Expanded entity references"""


class GetDeviceAlertsResponseBodyTypedDict(TypedDict):
    uid: NotRequired[str]
    r"""Alert UID (activity series UID)"""
    device_id: NotRequired[int]
    r"""Device identifier"""
    message: NotRequired[str]
    r"""Alert message"""
    create_time: NotRequired[float]
    r"""Alert creation timestamp"""
    update_time: NotRequired[float]
    r"""Alert last updated"""
    source_type: NotRequired[GetDeviceAlertsSourceType]
    r"""Alert origin"""
    source_config_uid: NotRequired[str]
    r"""Source configuration/policy element reference"""
    source_name: NotRequired[str]
    r"""Source configuration/policy element name"""
    subject: NotRequired[str]
    r"""Alert subject"""
    user_id: NotRequired[int]
    r"""User identifier"""
    psa_ticket_id: NotRequired[GetDeviceAlertsPsaTicketIDTypedDict]
    r"""Related PSA ticket ID"""
    ticket_template_id: NotRequired[int]
    r"""PSA ticket template"""
    data: NotRequired[Dict[str, Any]]
    r"""Alert data"""
    device: NotRequired[GetDeviceAlertsDeviceTypedDict]
    r"""Device information."""


class GetDeviceAlertsResponseBody(BaseModel):
    uid: Optional[str] = None
    r"""Alert UID (activity series UID)"""

    device_id: Annotated[Optional[int], pydantic.Field(alias="deviceId")] = None
    r"""Device identifier"""

    message: Optional[str] = None
    r"""Alert message"""

    create_time: Annotated[Optional[float], pydantic.Field(alias="createTime")] = None
    r"""Alert creation timestamp"""

    update_time: Annotated[Optional[float], pydantic.Field(alias="updateTime")] = None
    r"""Alert last updated"""

    source_type: Annotated[
        Optional[GetDeviceAlertsSourceType], pydantic.Field(alias="sourceType")
    ] = None
    r"""Alert origin"""

    source_config_uid: Annotated[
        Optional[str], pydantic.Field(alias="sourceConfigUid")
    ] = None
    r"""Source configuration/policy element reference"""

    source_name: Annotated[Optional[str], pydantic.Field(alias="sourceName")] = None
    r"""Source configuration/policy element name"""

    subject: Optional[str] = None
    r"""Alert subject"""

    user_id: Annotated[Optional[int], pydantic.Field(alias="userId")] = None
    r"""User identifier"""

    psa_ticket_id: Annotated[
        Optional[GetDeviceAlertsPsaTicketID], pydantic.Field(alias="psaTicketId")
    ] = None
    r"""Related PSA ticket ID"""

    ticket_template_id: Annotated[
        Optional[int], pydantic.Field(alias="ticketTemplateId")
    ] = None
    r"""PSA ticket template"""

    data: Optional[Dict[str, Any]] = None
    r"""Alert data"""

    device: Optional[GetDeviceAlertsDevice] = None
    r"""Device information."""

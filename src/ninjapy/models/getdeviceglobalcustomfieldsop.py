"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class Scopes(str, Enum):
    r"""Comma-separated list of scopes"""

    ALL_NODE_LOCATION_ORGANIZATION = "all,node,location,organization"


class GetDeviceGlobalCustomFieldsRequestTypedDict(TypedDict):
    scopes: NotRequired[Scopes]
    r"""Comma-separated list of scopes"""


class GetDeviceGlobalCustomFieldsRequest(BaseModel):
    scopes: Annotated[
        Optional[Scopes],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-separated list of scopes"""


class GetDeviceGlobalCustomFieldsEntityType(str, Enum):
    r"""Entity Type"""

    USER = "USER"
    NODE = "NODE"
    TICKET = "TICKET"
    DOCUMENT = "DOCUMENT"


class GetDeviceGlobalCustomFieldsScope(str, Enum):
    r"""Scope"""

    NODE_GLOBAL = "NODE_GLOBAL"
    NODE_ROLE = "NODE_ROLE"
    NODE_CLASS = "NODE_CLASS"


class DefinitionScope(str, Enum):
    r"""Definition Scope"""

    NODE = "NODE"
    LOCATION = "LOCATION"
    ORGANIZATION = "ORGANIZATION"


class GetDeviceGlobalCustomFieldsType(str, Enum):
    r"""Type"""

    DROPDOWN = "DROPDOWN"
    MULTI_SELECT = "MULTI_SELECT"
    CHECKBOX = "CHECKBOX"
    TEXT = "TEXT"
    TEXT_MULTILINE = "TEXT_MULTILINE"
    TEXT_ENCRYPTED = "TEXT_ENCRYPTED"
    NUMERIC = "NUMERIC"
    DECIMAL = "DECIMAL"
    DATE = "DATE"
    DATE_TIME = "DATE_TIME"
    TIME = "TIME"
    ATTACHMENT = "ATTACHMENT"
    NODE_DROPDOWN = "NODE_DROPDOWN"
    NODE_MULTI_SELECT = "NODE_MULTI_SELECT"
    CLIENT_DROPDOWN = "CLIENT_DROPDOWN"
    CLIENT_MULTI_SELECT = "CLIENT_MULTI_SELECT"
    CLIENT_LOCATION_DROPDOWN = "CLIENT_LOCATION_DROPDOWN"
    CLIENT_LOCATION_MULTI_SELECT = "CLIENT_LOCATION_MULTI_SELECT"
    CLIENT_DOCUMENT_DROPDOWN = "CLIENT_DOCUMENT_DROPDOWN"
    CLIENT_DOCUMENT_MULTI_SELECT = "CLIENT_DOCUMENT_MULTI_SELECT"
    EMAIL = "EMAIL"
    PHONE = "PHONE"
    IP_ADDRESS = "IP_ADDRESS"
    WYSIWYG = "WYSIWYG"
    URL = "URL"


class EndUserPermission(str, Enum):
    r"""End User Permission"""

    HIDDEN = "HIDDEN"
    EDITABLE_OPTIONAL = "EDITABLE_OPTIONAL"
    EDITABLE_REQUIRED = "EDITABLE_REQUIRED"
    READ_ONLY = "READ_ONLY"


class TechnicianPermission(str, Enum):
    r"""Technician Permission"""

    NONE = "NONE"
    EDITABLE = "EDITABLE"
    READ_ONLY = "READ_ONLY"


class ScriptPermission(str, Enum):
    r"""Script Permission"""

    NONE = "NONE"
    READ_ONLY = "READ_ONLY"
    WRITE_ONLY = "WRITE_ONLY"
    READ_WRITE = "READ_WRITE"


class APIPermission(str, Enum):
    r"""Public API Permission"""

    NONE = "NONE"
    READ_ONLY = "READ_ONLY"
    WRITE_ONLY = "WRITE_ONLY"
    READ_WRITE = "READ_WRITE"


class EndUserCustomizationTypedDict(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]
    label: NotRequired[str]


class EndUserCustomization(BaseModel):
    name: Optional[str] = None

    description: Optional[str] = None

    label: Optional[str] = None


class GetDeviceGlobalCustomFieldsValuesTypedDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    active: NotRequired[bool]
    system: NotRequired[bool]


class GetDeviceGlobalCustomFieldsValues(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    active: Optional[bool] = None

    system: Optional[bool] = None


class GetDeviceGlobalCustomFieldsSystemType(str, Enum):
    NONE = "NONE"
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"
    PAST_DATES_ONLY = "PAST_DATES_ONLY"
    FUTURE_DATES_ONLY = "FUTURE_DATES_ONLY"
    RANGE = "RANGE"


class GetDeviceGlobalCustomFieldsDateFiltersTypedDict(TypedDict):
    type: NotRequired[GetDeviceGlobalCustomFieldsSystemType]
    selected: NotRequired[List[str]]


class GetDeviceGlobalCustomFieldsDateFilters(BaseModel):
    type: Optional[GetDeviceGlobalCustomFieldsSystemType] = None

    selected: Optional[List[str]] = None


class GetDeviceGlobalCustomFieldsComplexityRulesTypedDict(TypedDict):
    must_contain_one_integer: NotRequired[bool]
    must_contain_one_lowercase_letter: NotRequired[bool]
    must_contain_one_uppercase_letter: NotRequired[bool]
    greater_or_equal_than_six_characters: NotRequired[bool]


class GetDeviceGlobalCustomFieldsComplexityRules(BaseModel):
    must_contain_one_integer: Annotated[
        Optional[bool], pydantic.Field(alias="mustContainOneInteger")
    ] = None

    must_contain_one_lowercase_letter: Annotated[
        Optional[bool], pydantic.Field(alias="mustContainOneLowercaseLetter")
    ] = None

    must_contain_one_uppercase_letter: Annotated[
        Optional[bool], pydantic.Field(alias="mustContainOneUppercaseLetter")
    ] = None

    greater_or_equal_than_six_characters: Annotated[
        Optional[bool], pydantic.Field(alias="greaterOrEqualThanSixCharacters")
    ] = None


class GetDeviceGlobalCustomFieldsNumericRangeTypedDict(TypedDict):
    min: NotRequired[float]
    max: NotRequired[float]


class GetDeviceGlobalCustomFieldsNumericRange(BaseModel):
    min: Optional[float] = None

    max: Optional[float] = None


class GetDeviceGlobalCustomFieldsNodeClass(str, Enum):
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


class GetDeviceGlobalCustomFieldsIPAddressType(str, Enum):
    ALL = "ALL"
    IPV4 = "IPV4"
    IPV6 = "IPV6"


class GetDeviceGlobalCustomFieldsAdvancedSettingsTypedDict(TypedDict):
    file_max_size: NotRequired[int]
    file_extensions: NotRequired[List[str]]
    date_filters: NotRequired[GetDeviceGlobalCustomFieldsDateFiltersTypedDict]
    max_characters: NotRequired[int]
    complexity_rules: NotRequired[GetDeviceGlobalCustomFieldsComplexityRulesTypedDict]
    numeric_range: NotRequired[GetDeviceGlobalCustomFieldsNumericRangeTypedDict]
    org: NotRequired[List[int]]
    node_class: NotRequired[List[GetDeviceGlobalCustomFieldsNodeClass]]
    ip_address_type: NotRequired[GetDeviceGlobalCustomFieldsIPAddressType]
    expand_large_value_on_render: NotRequired[bool]


class GetDeviceGlobalCustomFieldsAdvancedSettings(BaseModel):
    file_max_size: Annotated[Optional[int], pydantic.Field(alias="fileMaxSize")] = None

    file_extensions: Annotated[
        Optional[List[str]], pydantic.Field(alias="fileExtensions")
    ] = None

    date_filters: Annotated[
        Optional[GetDeviceGlobalCustomFieldsDateFilters],
        pydantic.Field(alias="dateFilters"),
    ] = None

    max_characters: Annotated[Optional[int], pydantic.Field(alias="maxCharacters")] = (
        None
    )

    complexity_rules: Annotated[
        Optional[GetDeviceGlobalCustomFieldsComplexityRules],
        pydantic.Field(alias="complexityRules"),
    ] = None

    numeric_range: Annotated[
        Optional[GetDeviceGlobalCustomFieldsNumericRange],
        pydantic.Field(alias="numericRange"),
    ] = None

    org: Optional[List[int]] = None

    node_class: Annotated[
        Optional[List[GetDeviceGlobalCustomFieldsNodeClass]],
        pydantic.Field(alias="nodeClass"),
    ] = None

    ip_address_type: Annotated[
        Optional[GetDeviceGlobalCustomFieldsIPAddressType],
        pydantic.Field(alias="ipAddressType"),
    ] = None

    expand_large_value_on_render: Annotated[
        Optional[bool], pydantic.Field(alias="expandLargeValueOnRender")
    ] = None


class GetDeviceGlobalCustomFieldsContentTypedDict(TypedDict):
    customize_for_end_user: NotRequired[bool]
    end_user_customization: NotRequired[EndUserCustomizationTypedDict]
    values: NotRequired[List[GetDeviceGlobalCustomFieldsValuesTypedDict]]
    required: NotRequired[bool]
    footer_text: NotRequired[str]
    tooltip_text: NotRequired[str]
    advanced_settings: NotRequired[GetDeviceGlobalCustomFieldsAdvancedSettingsTypedDict]


class GetDeviceGlobalCustomFieldsContent(BaseModel):
    customize_for_end_user: Annotated[
        Optional[bool], pydantic.Field(alias="customizeForEndUser")
    ] = None

    end_user_customization: Annotated[
        Optional[EndUserCustomization], pydantic.Field(alias="endUserCustomization")
    ] = None

    values: Optional[List[GetDeviceGlobalCustomFieldsValues]] = None

    required: Optional[bool] = None

    footer_text: Annotated[Optional[str], pydantic.Field(alias="footerText")] = None

    tooltip_text: Annotated[Optional[str], pydantic.Field(alias="tooltipText")] = None

    advanced_settings: Annotated[
        Optional[GetDeviceGlobalCustomFieldsAdvancedSettings],
        pydantic.Field(alias="advancedSettings"),
    ] = None


class GetDeviceGlobalCustomFieldsResponseBodyTypedDict(TypedDict):
    entity_type: NotRequired[GetDeviceGlobalCustomFieldsEntityType]
    r"""Entity Type"""
    scope: NotRequired[GetDeviceGlobalCustomFieldsScope]
    r"""Scope"""
    definition_scope: NotRequired[List[DefinitionScope]]
    r"""Definition Scope"""
    type: NotRequired[GetDeviceGlobalCustomFieldsType]
    r"""Type"""
    label: NotRequired[str]
    r"""Label"""
    description: NotRequired[str]
    r"""Description"""
    name: NotRequired[str]
    r"""Name"""
    default_value: NotRequired[str]
    r"""Default Value"""
    end_user_permission: NotRequired[EndUserPermission]
    r"""End User Permission"""
    technician_permission: NotRequired[TechnicianPermission]
    r"""Technician Permission"""
    script_permission: NotRequired[ScriptPermission]
    r"""Script Permission"""
    api_permission: NotRequired[APIPermission]
    r"""Public API Permission"""
    content: NotRequired[GetDeviceGlobalCustomFieldsContentTypedDict]
    system: NotRequired[bool]
    r"""System"""
    active: NotRequired[bool]
    r"""Active"""
    create_time: NotRequired[float]
    r"""Create Time"""
    update_time: NotRequired[float]
    r"""Update Time"""


class GetDeviceGlobalCustomFieldsResponseBody(BaseModel):
    entity_type: Annotated[
        Optional[GetDeviceGlobalCustomFieldsEntityType],
        pydantic.Field(alias="entityType"),
    ] = None
    r"""Entity Type"""

    scope: Optional[GetDeviceGlobalCustomFieldsScope] = None
    r"""Scope"""

    definition_scope: Annotated[
        Optional[List[DefinitionScope]], pydantic.Field(alias="definitionScope")
    ] = None
    r"""Definition Scope"""

    type: Optional[GetDeviceGlobalCustomFieldsType] = None
    r"""Type"""

    label: Optional[str] = None
    r"""Label"""

    description: Optional[str] = None
    r"""Description"""

    name: Optional[str] = None
    r"""Name"""

    default_value: Annotated[Optional[str], pydantic.Field(alias="defaultValue")] = None
    r"""Default Value"""

    end_user_permission: Annotated[
        Optional[EndUserPermission], pydantic.Field(alias="endUserPermission")
    ] = None
    r"""End User Permission"""

    technician_permission: Annotated[
        Optional[TechnicianPermission], pydantic.Field(alias="technicianPermission")
    ] = None
    r"""Technician Permission"""

    script_permission: Annotated[
        Optional[ScriptPermission], pydantic.Field(alias="scriptPermission")
    ] = None
    r"""Script Permission"""

    api_permission: Annotated[
        Optional[APIPermission], pydantic.Field(alias="apiPermission")
    ] = None
    r"""Public API Permission"""

    content: Optional[GetDeviceGlobalCustomFieldsContent] = None

    system: Optional[bool] = None
    r"""System"""

    active: Optional[bool] = None
    r"""Active"""

    create_time: Annotated[Optional[float], pydantic.Field(alias="createTime")] = None
    r"""Create Time"""

    update_time: Annotated[Optional[float], pydantic.Field(alias="updateTime")] = None
    r"""Update Time"""

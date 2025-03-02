"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetTicketFormsMode(str, Enum):
    MANUAL = "MANUAL"
    AUTO_START = "AUTO_START"


class GetTicketFormsTimerSettingsTypedDict(TypedDict):
    enabled: NotRequired[bool]
    mode: NotRequired[GetTicketFormsMode]


class GetTicketFormsTimerSettings(BaseModel):
    enabled: Optional[bool] = None

    mode: Optional[GetTicketFormsMode] = None


class GetTicketFormsContentTypedDict(TypedDict):
    fields: NotRequired[List[int]]
    timer_settings: NotRequired[GetTicketFormsTimerSettingsTypedDict]


class GetTicketFormsContent(BaseModel):
    fields: Optional[List[int]] = None

    timer_settings: Annotated[
        Optional[GetTicketFormsTimerSettings], pydantic.Field(alias="timerSettings")
    ] = None


class GetTicketFormsEndUserCustomizationTypedDict(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]
    label: NotRequired[str]


class GetTicketFormsEndUserCustomization(BaseModel):
    name: Optional[str] = None

    description: Optional[str] = None

    label: Optional[str] = None


class GetTicketFormsValuesTypedDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    active: NotRequired[bool]
    system: NotRequired[bool]


class GetTicketFormsValues(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    active: Optional[bool] = None

    system: Optional[bool] = None


class GetTicketFormsType(str, Enum):
    NONE = "NONE"
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"
    PAST_DATES_ONLY = "PAST_DATES_ONLY"
    FUTURE_DATES_ONLY = "FUTURE_DATES_ONLY"
    RANGE = "RANGE"


class GetTicketFormsDateFiltersTypedDict(TypedDict):
    type: NotRequired[GetTicketFormsType]
    selected: NotRequired[List[str]]


class GetTicketFormsDateFilters(BaseModel):
    type: Optional[GetTicketFormsType] = None

    selected: Optional[List[str]] = None


class GetTicketFormsComplexityRulesTypedDict(TypedDict):
    must_contain_one_integer: NotRequired[bool]
    must_contain_one_lowercase_letter: NotRequired[bool]
    must_contain_one_uppercase_letter: NotRequired[bool]
    greater_or_equal_than_six_characters: NotRequired[bool]


class GetTicketFormsComplexityRules(BaseModel):
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


class GetTicketFormsNumericRangeTypedDict(TypedDict):
    min: NotRequired[float]
    max: NotRequired[float]


class GetTicketFormsNumericRange(BaseModel):
    min: Optional[float] = None

    max: Optional[float] = None


class GetTicketFormsNodeClass(str, Enum):
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


class GetTicketFormsIPAddressType(str, Enum):
    ALL = "ALL"
    IPV4 = "IPV4"
    IPV6 = "IPV6"


class GetTicketFormsAdvancedSettingsTypedDict(TypedDict):
    file_max_size: NotRequired[int]
    file_extensions: NotRequired[List[str]]
    date_filters: NotRequired[GetTicketFormsDateFiltersTypedDict]
    max_characters: NotRequired[int]
    complexity_rules: NotRequired[GetTicketFormsComplexityRulesTypedDict]
    numeric_range: NotRequired[GetTicketFormsNumericRangeTypedDict]
    org: NotRequired[List[int]]
    node_class: NotRequired[List[GetTicketFormsNodeClass]]
    ip_address_type: NotRequired[GetTicketFormsIPAddressType]
    expand_large_value_on_render: NotRequired[bool]


class GetTicketFormsAdvancedSettings(BaseModel):
    file_max_size: Annotated[Optional[int], pydantic.Field(alias="fileMaxSize")] = None

    file_extensions: Annotated[
        Optional[List[str]], pydantic.Field(alias="fileExtensions")
    ] = None

    date_filters: Annotated[
        Optional[GetTicketFormsDateFilters], pydantic.Field(alias="dateFilters")
    ] = None

    max_characters: Annotated[Optional[int], pydantic.Field(alias="maxCharacters")] = (
        None
    )

    complexity_rules: Annotated[
        Optional[GetTicketFormsComplexityRules], pydantic.Field(alias="complexityRules")
    ] = None

    numeric_range: Annotated[
        Optional[GetTicketFormsNumericRange], pydantic.Field(alias="numericRange")
    ] = None

    org: Optional[List[int]] = None

    node_class: Annotated[
        Optional[List[GetTicketFormsNodeClass]], pydantic.Field(alias="nodeClass")
    ] = None

    ip_address_type: Annotated[
        Optional[GetTicketFormsIPAddressType], pydantic.Field(alias="ipAddressType")
    ] = None

    expand_large_value_on_render: Annotated[
        Optional[bool], pydantic.Field(alias="expandLargeValueOnRender")
    ] = None


class GetTicketFormsTicketingContentTypedDict(TypedDict):
    customize_for_end_user: NotRequired[bool]
    end_user_customization: NotRequired[GetTicketFormsEndUserCustomizationTypedDict]
    values: NotRequired[List[GetTicketFormsValuesTypedDict]]
    required: NotRequired[bool]
    footer_text: NotRequired[str]
    tooltip_text: NotRequired[str]
    advanced_settings: NotRequired[GetTicketFormsAdvancedSettingsTypedDict]


class GetTicketFormsTicketingContent(BaseModel):
    customize_for_end_user: Annotated[
        Optional[bool], pydantic.Field(alias="customizeForEndUser")
    ] = None

    end_user_customization: Annotated[
        Optional[GetTicketFormsEndUserCustomization],
        pydantic.Field(alias="endUserCustomization"),
    ] = None

    values: Optional[List[GetTicketFormsValues]] = None

    required: Optional[bool] = None

    footer_text: Annotated[Optional[str], pydantic.Field(alias="footerText")] = None

    tooltip_text: Annotated[Optional[str], pydantic.Field(alias="tooltipText")] = None

    advanced_settings: Annotated[
        Optional[GetTicketFormsAdvancedSettings],
        pydantic.Field(alias="advancedSettings"),
    ] = None


class GetTicketFormsFieldsTypedDict(TypedDict):
    id: NotRequired[int]
    attribute_type: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    customize_for_end_user: NotRequired[bool]
    name_for_end_user: NotRequired[str]
    description_for_end_user: NotRequired[str]
    end_user_option: NotRequired[str]
    technician_option: NotRequired[str]
    content: NotRequired[GetTicketFormsTicketingContentTypedDict]
    system: NotRequired[bool]
    active: NotRequired[bool]
    create_time: NotRequired[float]
    update_time: NotRequired[float]


class GetTicketFormsFields(BaseModel):
    id: Optional[int] = None

    attribute_type: Annotated[Optional[str], pydantic.Field(alias="attributeType")] = (
        None
    )

    name: Optional[str] = None

    description: Optional[str] = None

    customize_for_end_user: Annotated[
        Optional[bool], pydantic.Field(alias="customizeForEndUser")
    ] = None

    name_for_end_user: Annotated[
        Optional[str], pydantic.Field(alias="nameForEndUser")
    ] = None

    description_for_end_user: Annotated[
        Optional[str], pydantic.Field(alias="descriptionForEndUser")
    ] = None

    end_user_option: Annotated[Optional[str], pydantic.Field(alias="endUserOption")] = (
        None
    )

    technician_option: Annotated[
        Optional[str], pydantic.Field(alias="technicianOption")
    ] = None

    content: Optional[GetTicketFormsTicketingContent] = None

    system: Optional[bool] = None

    active: Optional[bool] = None

    create_time: Annotated[Optional[float], pydantic.Field(alias="createTime")] = None

    update_time: Annotated[Optional[float], pydantic.Field(alias="updateTime")] = None


class GetTicketFormsResponseBodyTypedDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    description: NotRequired[str]
    end_user_title: NotRequired[str]
    content: NotRequired[GetTicketFormsContentTypedDict]
    active: NotRequired[bool]
    create_time: NotRequired[float]
    update_time: NotRequired[float]
    fields: NotRequired[List[GetTicketFormsFieldsTypedDict]]
    default: NotRequired[bool]


class GetTicketFormsResponseBody(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    description: Optional[str] = None

    end_user_title: Annotated[Optional[str], pydantic.Field(alias="endUserTitle")] = (
        None
    )

    content: Optional[GetTicketFormsContent] = None

    active: Optional[bool] = None

    create_time: Annotated[Optional[float], pydantic.Field(alias="createTime")] = None

    update_time: Annotated[Optional[float], pydantic.Field(alias="updateTime")] = None

    fields: Optional[List[GetTicketFormsFields]] = None

    default: Optional[bool] = None

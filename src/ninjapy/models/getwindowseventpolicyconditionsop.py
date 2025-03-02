"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetWindowsEventPolicyConditionsRequestTypedDict(TypedDict):
    policy_id: int


class GetWindowsEventPolicyConditionsRequest(BaseModel):
    policy_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetWindowsEventPolicyConditionsSeverity(str, Enum):
    r"""Policy condition severity"""

    NONE = "NONE"
    MINOR = "MINOR"
    MODERATE = "MODERATE"
    MAJOR = "MAJOR"
    CRITICAL = "CRITICAL"


class GetWindowsEventPolicyConditionsPriority(str, Enum):
    r"""Policy condition priority"""

    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class GetWindowsEventPolicyConditionsRunAs(str, Enum):
    r"""Policy condition script runAs"""

    SYSTEM = "SYSTEM"
    LOGGED_ON_USER = "LOGGED_ON_USER"
    LOCAL_ADMIN = "LOCAL_ADMIN"
    DOMAIN_ADMIN = "DOMAIN_ADMIN"
    PREFERRED_CREDENTIAL_MAC = "PREFERRED_CREDENTIAL_MAC"
    PREFERRED_CREDENTIAL_LINUX = "PREFERRED_CREDENTIAL_LINUX"


class GetWindowsEventPolicyConditionsScriptVariablesTypedDict(TypedDict):
    r"""Policy condition script variable"""

    id: NotRequired[str]
    r"""Policy condition script variable Id"""
    value: NotRequired[str]
    r"""Policy condition script variable value"""


class GetWindowsEventPolicyConditionsScriptVariables(BaseModel):
    r"""Policy condition script variable"""

    id: Optional[str] = None
    r"""Policy condition script variable Id"""

    value: Optional[str] = None
    r"""Policy condition script variable value"""


class GetWindowsEventPolicyConditionsScriptsTypedDict(TypedDict):
    r"""Policy condition script"""

    script_id: NotRequired[int]
    r"""Policy condition script id"""
    run_as: NotRequired[GetWindowsEventPolicyConditionsRunAs]
    r"""Policy condition script runAs"""
    script_param: NotRequired[str]
    r"""Policy condition script parameter"""
    script_variables: NotRequired[
        List[GetWindowsEventPolicyConditionsScriptVariablesTypedDict]
    ]
    r"""Policy condition script variables"""


class GetWindowsEventPolicyConditionsScripts(BaseModel):
    r"""Policy condition script"""

    script_id: Annotated[Optional[int], pydantic.Field(alias="scriptId")] = None
    r"""Policy condition script id"""

    run_as: Annotated[
        Optional[GetWindowsEventPolicyConditionsRunAs], pydantic.Field(alias="runAs")
    ] = GetWindowsEventPolicyConditionsRunAs.SYSTEM
    r"""Policy condition script runAs"""

    script_param: Annotated[Optional[str], pydantic.Field(alias="scriptParam")] = None
    r"""Policy condition script parameter"""

    script_variables: Annotated[
        Optional[List[GetWindowsEventPolicyConditionsScriptVariables]],
        pydantic.Field(alias="scriptVariables"),
    ] = None
    r"""Policy condition script variables"""


class GetWindowsEventPolicyConditionsNotificationAction(str, Enum):
    r"""Policy condition notification action"""

    NONE = "NONE"
    SEND = "SEND"


class GetWindowsEventPolicyConditionsInheritanceTypedDict(TypedDict):
    r"""Policy condition inheritance status"""

    inherited: NotRequired[bool]
    r"""Is policy condition inherited"""
    overridden: NotRequired[bool]
    r"""Is policy condition overridden"""
    source_policy_id: NotRequired[int]
    r"""Parent policy Id"""


class GetWindowsEventPolicyConditionsInheritance(BaseModel):
    r"""Policy condition inheritance status"""

    inherited: Optional[bool] = None
    r"""Is policy condition inherited"""

    overridden: Optional[bool] = None
    r"""Is policy condition overridden"""

    source_policy_id: Annotated[
        Optional[int], pydantic.Field(alias="sourcePolicyId")
    ] = None
    r"""Parent policy Id"""


class GetWindowsEventPolicyConditionsCondition(str, Enum):
    r"""Text condition"""

    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"


class GetWindowsEventPolicyConditionsInclude(str, Enum):
    r"""Text include"""

    ALL = "ALL"
    ANY = "ANY"


class GetWindowsEventPolicyConditionsTextTypedDict(TypedDict):
    r"""Windows event policy condition text"""

    values: NotRequired[List[str]]
    r"""Text values"""
    condition: NotRequired[GetWindowsEventPolicyConditionsCondition]
    r"""Text condition"""
    include: NotRequired[GetWindowsEventPolicyConditionsInclude]
    r"""Text include"""


class GetWindowsEventPolicyConditionsText(BaseModel):
    r"""Windows event policy condition text"""

    values: Optional[List[str]] = None
    r"""Text values"""

    condition: Optional[GetWindowsEventPolicyConditionsCondition] = (
        GetWindowsEventPolicyConditionsCondition.CONTAINS
    )
    r"""Text condition"""

    include: Optional[GetWindowsEventPolicyConditionsInclude] = (
        GetWindowsEventPolicyConditionsInclude.ALL
    )
    r"""Text include"""


class GetWindowsEventPolicyConditionsOccurrenceTypedDict(TypedDict):
    r"""Windows event policy condition occurrence"""

    enabled: NotRequired[bool]
    r"""Occurrence enabled"""
    threshold: NotRequired[int]
    r"""Occurrence threshold"""
    duration: NotRequired[int]
    r"""Occurrence duration"""


class GetWindowsEventPolicyConditionsOccurrence(BaseModel):
    r"""Windows event policy condition occurrence"""

    enabled: Optional[bool] = False
    r"""Occurrence enabled"""

    threshold: Optional[int] = 2
    r"""Occurrence threshold"""

    duration: Optional[int] = 5
    r"""Occurrence duration"""


class GetWindowsEventPolicyConditionsResponseBodyTypedDict(TypedDict):
    r"""Windows event policy condition response payload"""

    id: NotRequired[str]
    r"""Policy condition id"""
    condition_name: NotRequired[str]
    r"""Policy condition name"""
    display_name: NotRequired[str]
    r"""Policy condition display name"""
    enabled: NotRequired[bool]
    r"""Policy condition enabled"""
    severity: NotRequired[GetWindowsEventPolicyConditionsSeverity]
    r"""Policy condition severity"""
    priority: NotRequired[GetWindowsEventPolicyConditionsPriority]
    r"""Policy condition priority"""
    channels: NotRequired[List[int]]
    r"""Policy condition notification channels"""
    scripts: NotRequired[List[GetWindowsEventPolicyConditionsScriptsTypedDict]]
    r"""Policy condition scripts"""
    notification_action: NotRequired[GetWindowsEventPolicyConditionsNotificationAction]
    r"""Policy condition notification action"""
    notify_on_reset: NotRequired[bool]
    r"""Policy condition notify on reset"""
    reset_threshold: NotRequired[int]
    r"""Policy condition reset threshold (seconds)"""
    inheritance: NotRequired[GetWindowsEventPolicyConditionsInheritanceTypedDict]
    r"""Policy condition inheritance status"""
    source: NotRequired[str]
    r"""Event Source"""
    event_ids: NotRequired[List[int]]
    r"""Event IDs"""
    text: NotRequired[GetWindowsEventPolicyConditionsTextTypedDict]
    r"""Windows event policy condition text"""
    occurrence: NotRequired[GetWindowsEventPolicyConditionsOccurrenceTypedDict]
    r"""Windows event policy condition occurrence"""


class GetWindowsEventPolicyConditionsResponseBody(BaseModel):
    r"""Windows event policy condition response payload"""

    id: Optional[str] = None
    r"""Policy condition id"""

    condition_name: Annotated[Optional[str], pydantic.Field(alias="conditionName")] = (
        None
    )
    r"""Policy condition name"""

    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""Policy condition display name"""

    enabled: Optional[bool] = None
    r"""Policy condition enabled"""

    severity: Optional[GetWindowsEventPolicyConditionsSeverity] = None
    r"""Policy condition severity"""

    priority: Optional[GetWindowsEventPolicyConditionsPriority] = None
    r"""Policy condition priority"""

    channels: Optional[List[int]] = None
    r"""Policy condition notification channels"""

    scripts: Optional[List[GetWindowsEventPolicyConditionsScripts]] = None
    r"""Policy condition scripts"""

    notification_action: Annotated[
        Optional[GetWindowsEventPolicyConditionsNotificationAction],
        pydantic.Field(alias="notificationAction"),
    ] = None
    r"""Policy condition notification action"""

    notify_on_reset: Annotated[
        Optional[bool], pydantic.Field(alias="notifyOnReset")
    ] = None
    r"""Policy condition notify on reset"""

    reset_threshold: Annotated[
        Optional[int], pydantic.Field(alias="resetThreshold")
    ] = None
    r"""Policy condition reset threshold (seconds)"""

    inheritance: Optional[GetWindowsEventPolicyConditionsInheritance] = None
    r"""Policy condition inheritance status"""

    source: Optional[str] = None
    r"""Event Source"""

    event_ids: Annotated[Optional[List[int]], pydantic.Field(alias="eventIds")] = None
    r"""Event IDs"""

    text: Optional[GetWindowsEventPolicyConditionsText] = None
    r"""Windows event policy condition text"""

    occurrence: Optional[GetWindowsEventPolicyConditionsOccurrence] = None
    r"""Windows event policy condition occurrence"""

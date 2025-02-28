"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class Severity(str, Enum):
    r"""Policy condition severity"""

    NONE = "NONE"
    MINOR = "MINOR"
    MODERATE = "MODERATE"
    MAJOR = "MAJOR"
    CRITICAL = "CRITICAL"


class Priority(str, Enum):
    r"""Policy condition priority"""

    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class RunAs(str, Enum):
    r"""Policy condition script runAs"""

    SYSTEM = "SYSTEM"
    LOGGED_ON_USER = "LOGGED_ON_USER"
    LOCAL_ADMIN = "LOCAL_ADMIN"
    DOMAIN_ADMIN = "DOMAIN_ADMIN"
    PREFERRED_CREDENTIAL_MAC = "PREFERRED_CREDENTIAL_MAC"
    PREFERRED_CREDENTIAL_LINUX = "PREFERRED_CREDENTIAL_LINUX"


class ScriptVariablesTypedDict(TypedDict):
    r"""Policy condition script variable"""

    id: NotRequired[str]
    r"""Policy condition script variable Id"""
    value: NotRequired[str]
    r"""Policy condition script variable value"""


class ScriptVariables(BaseModel):
    r"""Policy condition script variable"""

    id: Optional[str] = None
    r"""Policy condition script variable Id"""

    value: Optional[str] = None
    r"""Policy condition script variable value"""


class ScriptsTypedDict(TypedDict):
    r"""Policy condition script"""

    script_id: NotRequired[int]
    r"""Policy condition script id"""
    run_as: NotRequired[RunAs]
    r"""Policy condition script runAs"""
    script_param: NotRequired[str]
    r"""Policy condition script parameter"""
    script_variables: NotRequired[List[ScriptVariablesTypedDict]]
    r"""Policy condition script variables"""


class Scripts(BaseModel):
    r"""Policy condition script"""

    script_id: Annotated[Optional[int], pydantic.Field(alias="scriptId")] = None
    r"""Policy condition script id"""

    run_as: Annotated[Optional[RunAs], pydantic.Field(alias="runAs")] = RunAs.SYSTEM
    r"""Policy condition script runAs"""

    script_param: Annotated[Optional[str], pydantic.Field(alias="scriptParam")] = None
    r"""Policy condition script parameter"""

    script_variables: Annotated[
        Optional[List[ScriptVariables]], pydantic.Field(alias="scriptVariables")
    ] = None
    r"""Policy condition script variables"""


class NotificationAction(str, Enum):
    r"""Policy condition notification action"""

    NONE = "NONE"
    SEND = "SEND"


class Operator(str, Enum):
    r"""Custom field operator"""

    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    LESS_THAN = "LESS_THAN"
    LESS_OR_EQUAL_THAN = "LESS_OR_EQUAL_THAN"
    GREATER_THAN = "GREATER_THAN"
    GREATER_OR_EQUAL_THAN = "GREATER_OR_EQUAL_THAN"
    IS_NOT_NULL = "IS_NOT_NULL"
    CONTAINS = "CONTAINS"
    CONTAINS_NONE = "CONTAINS_NONE"
    CONTAINS_ANY = "CONTAINS_ANY"


class MatchAllTypedDict(TypedDict):
    r"""Policy condition custom field"""

    field_name: str
    r"""Custom field name"""
    operator: Operator
    r"""Custom field operator"""
    value: str
    r"""Custom field value"""


class MatchAll(BaseModel):
    r"""Policy condition custom field"""

    field_name: Annotated[str, pydantic.Field(alias="fieldName")]
    r"""Custom field name"""

    operator: Operator
    r"""Custom field operator"""

    value: str
    r"""Custom field value"""


class CreateCustomFieldsPolicyConditionOperator(str, Enum):
    r"""Custom field operator"""

    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    LESS_THAN = "LESS_THAN"
    LESS_OR_EQUAL_THAN = "LESS_OR_EQUAL_THAN"
    GREATER_THAN = "GREATER_THAN"
    GREATER_OR_EQUAL_THAN = "GREATER_OR_EQUAL_THAN"
    IS_NOT_NULL = "IS_NOT_NULL"
    CONTAINS = "CONTAINS"
    CONTAINS_NONE = "CONTAINS_NONE"
    CONTAINS_ANY = "CONTAINS_ANY"


class MatchAnyTypedDict(TypedDict):
    r"""Policy condition custom field"""

    field_name: str
    r"""Custom field name"""
    operator: CreateCustomFieldsPolicyConditionOperator
    r"""Custom field operator"""
    value: str
    r"""Custom field value"""


class MatchAny(BaseModel):
    r"""Policy condition custom field"""

    field_name: Annotated[str, pydantic.Field(alias="fieldName")]
    r"""Custom field name"""

    operator: CreateCustomFieldsPolicyConditionOperator
    r"""Custom field operator"""

    value: str
    r"""Custom field value"""


class CreateCustomFieldsPolicyConditionRequestBodyTypedDict(TypedDict):
    r"""Custom fields policy condition create request payload"""

    enabled: NotRequired[bool]
    r"""Policy condition enabled"""
    display_name: NotRequired[str]
    r"""Policy condition display name"""
    severity: NotRequired[Severity]
    r"""Policy condition severity"""
    priority: NotRequired[Priority]
    r"""Policy condition priority"""
    channels: NotRequired[List[int]]
    r"""Policy condition notification channels"""
    scripts: NotRequired[List[ScriptsTypedDict]]
    r"""Policy condition scripts"""
    notification_action: NotRequired[NotificationAction]
    r"""Policy condition notification action"""
    notify_on_reset: NotRequired[bool]
    r"""Policy condition notify on reset"""
    reset_threshold: NotRequired[int]
    r"""Policy condition reset threshold (seconds)"""
    match_all: NotRequired[List[MatchAllTypedDict]]
    r"""Custom field value must meet all conditions"""
    match_any: NotRequired[List[MatchAnyTypedDict]]
    r"""Custom field value must meet any conditions"""


class CreateCustomFieldsPolicyConditionRequestBody(BaseModel):
    r"""Custom fields policy condition create request payload"""

    enabled: Optional[bool] = True
    r"""Policy condition enabled"""

    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""Policy condition display name"""

    severity: Optional[Severity] = Severity.NONE
    r"""Policy condition severity"""

    priority: Optional[Priority] = Priority.NONE
    r"""Policy condition priority"""

    channels: Optional[List[int]] = None
    r"""Policy condition notification channels"""

    scripts: Optional[List[Scripts]] = None
    r"""Policy condition scripts"""

    notification_action: Annotated[
        Optional[NotificationAction], pydantic.Field(alias="notificationAction")
    ] = NotificationAction.NONE
    r"""Policy condition notification action"""

    notify_on_reset: Annotated[
        Optional[bool], pydantic.Field(alias="notifyOnReset")
    ] = False
    r"""Policy condition notify on reset"""

    reset_threshold: Annotated[
        Optional[int], pydantic.Field(alias="resetThreshold")
    ] = 14400
    r"""Policy condition reset threshold (seconds)"""

    match_all: Annotated[Optional[List[MatchAll]], pydantic.Field(alias="matchAll")] = (
        None
    )
    r"""Custom field value must meet all conditions"""

    match_any: Annotated[Optional[List[MatchAny]], pydantic.Field(alias="matchAny")] = (
        None
    )
    r"""Custom field value must meet any conditions"""


class CreateCustomFieldsPolicyConditionRequestTypedDict(TypedDict):
    policy_id: int
    request_body: NotRequired[CreateCustomFieldsPolicyConditionRequestBodyTypedDict]


class CreateCustomFieldsPolicyConditionRequest(BaseModel):
    policy_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        Optional[CreateCustomFieldsPolicyConditionRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class CreateCustomFieldsPolicyConditionSeverity(str, Enum):
    r"""Policy condition severity"""

    NONE = "NONE"
    MINOR = "MINOR"
    MODERATE = "MODERATE"
    MAJOR = "MAJOR"
    CRITICAL = "CRITICAL"


class CreateCustomFieldsPolicyConditionPriority(str, Enum):
    r"""Policy condition priority"""

    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class CreateCustomFieldsPolicyConditionRunAs(str, Enum):
    r"""Policy condition script runAs"""

    SYSTEM = "SYSTEM"
    LOGGED_ON_USER = "LOGGED_ON_USER"
    LOCAL_ADMIN = "LOCAL_ADMIN"
    DOMAIN_ADMIN = "DOMAIN_ADMIN"
    PREFERRED_CREDENTIAL_MAC = "PREFERRED_CREDENTIAL_MAC"
    PREFERRED_CREDENTIAL_LINUX = "PREFERRED_CREDENTIAL_LINUX"


class CreateCustomFieldsPolicyConditionScriptVariablesTypedDict(TypedDict):
    r"""Policy condition script variable"""

    id: NotRequired[str]
    r"""Policy condition script variable Id"""
    value: NotRequired[str]
    r"""Policy condition script variable value"""


class CreateCustomFieldsPolicyConditionScriptVariables(BaseModel):
    r"""Policy condition script variable"""

    id: Optional[str] = None
    r"""Policy condition script variable Id"""

    value: Optional[str] = None
    r"""Policy condition script variable value"""


class CreateCustomFieldsPolicyConditionScriptsTypedDict(TypedDict):
    r"""Policy condition script"""

    script_id: NotRequired[int]
    r"""Policy condition script id"""
    run_as: NotRequired[CreateCustomFieldsPolicyConditionRunAs]
    r"""Policy condition script runAs"""
    script_param: NotRequired[str]
    r"""Policy condition script parameter"""
    script_variables: NotRequired[
        List[CreateCustomFieldsPolicyConditionScriptVariablesTypedDict]
    ]
    r"""Policy condition script variables"""


class CreateCustomFieldsPolicyConditionScripts(BaseModel):
    r"""Policy condition script"""

    script_id: Annotated[Optional[int], pydantic.Field(alias="scriptId")] = None
    r"""Policy condition script id"""

    run_as: Annotated[
        Optional[CreateCustomFieldsPolicyConditionRunAs], pydantic.Field(alias="runAs")
    ] = CreateCustomFieldsPolicyConditionRunAs.SYSTEM
    r"""Policy condition script runAs"""

    script_param: Annotated[Optional[str], pydantic.Field(alias="scriptParam")] = None
    r"""Policy condition script parameter"""

    script_variables: Annotated[
        Optional[List[CreateCustomFieldsPolicyConditionScriptVariables]],
        pydantic.Field(alias="scriptVariables"),
    ] = None
    r"""Policy condition script variables"""


class CreateCustomFieldsPolicyConditionNotificationAction(str, Enum):
    r"""Policy condition notification action"""

    NONE = "NONE"
    SEND = "SEND"


class CreateCustomFieldsPolicyConditionInheritanceTypedDict(TypedDict):
    r"""Policy condition inheritance status"""

    inherited: NotRequired[bool]
    r"""Is policy condition inherited"""
    overridden: NotRequired[bool]
    r"""Is policy condition overridden"""
    source_policy_id: NotRequired[int]
    r"""Parent policy Id"""


class CreateCustomFieldsPolicyConditionInheritance(BaseModel):
    r"""Policy condition inheritance status"""

    inherited: Optional[bool] = None
    r"""Is policy condition inherited"""

    overridden: Optional[bool] = None
    r"""Is policy condition overridden"""

    source_policy_id: Annotated[
        Optional[int], pydantic.Field(alias="sourcePolicyId")
    ] = None
    r"""Parent policy Id"""


class CreateCustomFieldsPolicyConditionManagementOperator(str, Enum):
    r"""Custom field operator"""

    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    LESS_THAN = "LESS_THAN"
    LESS_OR_EQUAL_THAN = "LESS_OR_EQUAL_THAN"
    GREATER_THAN = "GREATER_THAN"
    GREATER_OR_EQUAL_THAN = "GREATER_OR_EQUAL_THAN"
    IS_NOT_NULL = "IS_NOT_NULL"
    CONTAINS = "CONTAINS"
    CONTAINS_NONE = "CONTAINS_NONE"
    CONTAINS_ANY = "CONTAINS_ANY"


class CreateCustomFieldsPolicyConditionMatchAllTypedDict(TypedDict):
    r"""Policy condition custom field"""

    field_name: str
    r"""Custom field name"""
    operator: CreateCustomFieldsPolicyConditionManagementOperator
    r"""Custom field operator"""
    value: str
    r"""Custom field value"""


class CreateCustomFieldsPolicyConditionMatchAll(BaseModel):
    r"""Policy condition custom field"""

    field_name: Annotated[str, pydantic.Field(alias="fieldName")]
    r"""Custom field name"""

    operator: CreateCustomFieldsPolicyConditionManagementOperator
    r"""Custom field operator"""

    value: str
    r"""Custom field value"""


class CreateCustomFieldsPolicyConditionManagementResponseOperator(str, Enum):
    r"""Custom field operator"""

    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    LESS_THAN = "LESS_THAN"
    LESS_OR_EQUAL_THAN = "LESS_OR_EQUAL_THAN"
    GREATER_THAN = "GREATER_THAN"
    GREATER_OR_EQUAL_THAN = "GREATER_OR_EQUAL_THAN"
    IS_NOT_NULL = "IS_NOT_NULL"
    CONTAINS = "CONTAINS"
    CONTAINS_NONE = "CONTAINS_NONE"
    CONTAINS_ANY = "CONTAINS_ANY"


class CreateCustomFieldsPolicyConditionMatchAnyTypedDict(TypedDict):
    r"""Policy condition custom field"""

    field_name: str
    r"""Custom field name"""
    operator: CreateCustomFieldsPolicyConditionManagementResponseOperator
    r"""Custom field operator"""
    value: str
    r"""Custom field value"""


class CreateCustomFieldsPolicyConditionMatchAny(BaseModel):
    r"""Policy condition custom field"""

    field_name: Annotated[str, pydantic.Field(alias="fieldName")]
    r"""Custom field name"""

    operator: CreateCustomFieldsPolicyConditionManagementResponseOperator
    r"""Custom field operator"""

    value: str
    r"""Custom field value"""


class CreateCustomFieldsPolicyConditionResponseBodyTypedDict(TypedDict):
    r"""Custom fields policy condition response payload"""

    id: NotRequired[str]
    r"""Policy condition id"""
    condition_name: NotRequired[str]
    r"""Policy condition name"""
    display_name: NotRequired[str]
    r"""Policy condition display name"""
    enabled: NotRequired[bool]
    r"""Policy condition enabled"""
    severity: NotRequired[CreateCustomFieldsPolicyConditionSeverity]
    r"""Policy condition severity"""
    priority: NotRequired[CreateCustomFieldsPolicyConditionPriority]
    r"""Policy condition priority"""
    channels: NotRequired[List[int]]
    r"""Policy condition notification channels"""
    scripts: NotRequired[List[CreateCustomFieldsPolicyConditionScriptsTypedDict]]
    r"""Policy condition scripts"""
    notification_action: NotRequired[
        CreateCustomFieldsPolicyConditionNotificationAction
    ]
    r"""Policy condition notification action"""
    notify_on_reset: NotRequired[bool]
    r"""Policy condition notify on reset"""
    reset_threshold: NotRequired[int]
    r"""Policy condition reset threshold (seconds)"""
    inheritance: NotRequired[CreateCustomFieldsPolicyConditionInheritanceTypedDict]
    r"""Policy condition inheritance status"""
    match_all: NotRequired[List[CreateCustomFieldsPolicyConditionMatchAllTypedDict]]
    r"""Custom field value must meet all conditions"""
    match_any: NotRequired[List[CreateCustomFieldsPolicyConditionMatchAnyTypedDict]]
    r"""Custom field value must meet any conditions"""


class CreateCustomFieldsPolicyConditionResponseBody(BaseModel):
    r"""Custom fields policy condition response payload"""

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

    severity: Optional[CreateCustomFieldsPolicyConditionSeverity] = None
    r"""Policy condition severity"""

    priority: Optional[CreateCustomFieldsPolicyConditionPriority] = None
    r"""Policy condition priority"""

    channels: Optional[List[int]] = None
    r"""Policy condition notification channels"""

    scripts: Optional[List[CreateCustomFieldsPolicyConditionScripts]] = None
    r"""Policy condition scripts"""

    notification_action: Annotated[
        Optional[CreateCustomFieldsPolicyConditionNotificationAction],
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

    inheritance: Optional[CreateCustomFieldsPolicyConditionInheritance] = None
    r"""Policy condition inheritance status"""

    match_all: Annotated[
        Optional[List[CreateCustomFieldsPolicyConditionMatchAll]],
        pydantic.Field(alias="matchAll"),
    ] = None
    r"""Custom field value must meet all conditions"""

    match_any: Annotated[
        Optional[List[CreateCustomFieldsPolicyConditionMatchAny]],
        pydantic.Field(alias="matchAny"),
    ] = None
    r"""Custom field value must meet any conditions"""

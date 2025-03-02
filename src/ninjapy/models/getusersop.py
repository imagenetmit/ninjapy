"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UserType(str, Enum):
    r"""User type filter"""

    TECHNICIAN = "TECHNICIAN"
    END_USER = "END_USER"


class GetUsersRequestTypedDict(TypedDict):
    user_type: NotRequired[UserType]
    r"""User type filter"""
    include_roles: NotRequired[bool]
    r"""Includes user role information"""


class GetUsersRequest(BaseModel):
    user_type: Annotated[
        Optional[UserType],
        pydantic.Field(alias="userType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""User type filter"""

    include_roles: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeRoles"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Includes user role information"""


class GetUsersUserType(str, Enum):
    TECHNICIAN = "TECHNICIAN"
    END_USER = "END_USER"


class GetUsersInvitationStatus(str, Enum):
    REGISTERED = "REGISTERED"
    PENDING = "PENDING"
    EXPIRED = "EXPIRED"


class GetUsersFieldsTypedDict(TypedDict):
    r"""Custom Fields"""


class GetUsersFields(BaseModel):
    r"""Custom Fields"""


class GetUsersResponseBodyTypedDict(TypedDict):
    id: NotRequired[int]
    r"""User identifier"""
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    phone: NotRequired[str]
    enabled: NotRequired[bool]
    administrator: NotRequired[bool]
    permit_all_clients: NotRequired[bool]
    notify_all_clients: NotRequired[bool]
    must_change_pw: NotRequired[bool]
    mfa_configured: NotRequired[bool]
    user_type: NotRequired[GetUsersUserType]
    invitation_status: NotRequired[GetUsersInvitationStatus]
    organization_id: NotRequired[int]
    r"""Identifier of organization for end-users"""
    device_ids: NotRequired[List[int]]
    r"""Device IDs which end-user is authorized to access"""
    tags: NotRequired[List[str]]
    r"""Tags"""
    fields: NotRequired[Dict[str, GetUsersFieldsTypedDict]]
    r"""Custom Fields"""
    roles: NotRequired[List[str]]
    r"""A list of role names assigned to the user. This is provided when the 'includeRoles' query parameter is set to 'true'"""


class GetUsersResponseBody(BaseModel):
    id: Optional[int] = None
    r"""User identifier"""

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    email: Optional[str] = None

    phone: Optional[str] = None

    enabled: Optional[bool] = None

    administrator: Optional[bool] = None

    permit_all_clients: Annotated[
        Optional[bool], pydantic.Field(alias="permitAllClients")
    ] = None

    notify_all_clients: Annotated[
        Optional[bool], pydantic.Field(alias="notifyAllClients")
    ] = None

    must_change_pw: Annotated[Optional[bool], pydantic.Field(alias="mustChangePw")] = (
        None
    )

    mfa_configured: Annotated[Optional[bool], pydantic.Field(alias="mfaConfigured")] = (
        None
    )

    user_type: Annotated[
        Optional[GetUsersUserType], pydantic.Field(alias="userType")
    ] = None

    invitation_status: Annotated[
        Optional[GetUsersInvitationStatus], pydantic.Field(alias="invitationStatus")
    ] = None

    organization_id: Annotated[
        Optional[int], pydantic.Field(alias="organizationId")
    ] = None
    r"""Identifier of organization for end-users"""

    device_ids: Annotated[Optional[List[int]], pydantic.Field(alias="deviceIds")] = None
    r"""Device IDs which end-user is authorized to access"""

    tags: Optional[List[str]] = None
    r"""Tags"""

    fields: Optional[Dict[str, GetUsersFields]] = None
    r"""Custom Fields"""

    roles: Optional[List[str]] = None
    r"""A list of role names assigned to the user. This is provided when the 'includeRoles' query parameter is set to 'true'"""

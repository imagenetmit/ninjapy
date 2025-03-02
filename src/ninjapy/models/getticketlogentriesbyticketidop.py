"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class QueryParamType(str, Enum):
    DESCRIPTION = "DESCRIPTION"
    COMMENT = "COMMENT"
    CONDITION = "CONDITION"
    SAVE = "SAVE"
    DELETE = "DELETE"


class GetTicketLogEntriesByTicketIDRequestTypedDict(TypedDict):
    ticket_id: int
    type: NotRequired[QueryParamType]
    create_time: NotRequired[str]
    anchor_id: NotRequired[int]
    page_size: NotRequired[int]


class GetTicketLogEntriesByTicketIDRequest(BaseModel):
    ticket_id: Annotated[
        int,
        pydantic.Field(alias="ticketId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    type: Annotated[
        Optional[QueryParamType],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    create_time: Annotated[
        Optional[str],
        pydantic.Field(alias="createTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    anchor_id: Annotated[
        Optional[int],
        pydantic.Field(alias="anchorId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 500


class AppUserContactType(str, Enum):
    TECHNICIAN = "TECHNICIAN"
    END_USER = "END_USER"
    CONTACT = "CONTACT"


class GetTicketLogEntriesByTicketIDType(str, Enum):
    DESCRIPTION = "DESCRIPTION"
    COMMENT = "COMMENT"
    CONDITION = "CONDITION"
    SAVE = "SAVE"
    DELETE = "DELETE"


class ChangeDiffTypedDict(TypedDict):
    pass


class ChangeDiff(BaseModel):
    pass


class TechniciansTaggedMetadataTypedDict(TypedDict):
    id: NotRequired[int]
    email: NotRequired[str]
    display_name: NotRequired[str]
    deleted: NotRequired[bool]
    permitted: NotRequired[bool]


class TechniciansTaggedMetadata(BaseModel):
    id: Optional[int] = None

    email: Optional[str] = None

    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None

    deleted: Optional[bool] = None

    permitted: Optional[bool] = None


class AutomationTypedDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    system: NotRequired[bool]
    type: NotRequired[str]


class Automation(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    system: Optional[bool] = None

    type: Optional[str] = None


class GetTicketLogEntriesByTicketIDResponseBodyTypedDict(TypedDict):
    id: NotRequired[int]
    app_user_contact_uid: NotRequired[str]
    app_user_contact_id: NotRequired[int]
    app_user_contact_type: NotRequired[AppUserContactType]
    type: NotRequired[GetTicketLogEntriesByTicketIDType]
    body: NotRequired[str]
    html_body: NotRequired[str]
    full_email_body: NotRequired[str]
    public_entry: NotRequired[bool]
    system: NotRequired[bool]
    create_time: NotRequired[float]
    change_diff: NotRequired[ChangeDiffTypedDict]
    activity_id: NotRequired[int]
    time_tracked: NotRequired[int]
    technician_tagged: NotRequired[List[int]]
    technicians_tagged_metadata: NotRequired[List[TechniciansTaggedMetadataTypedDict]]
    automation: NotRequired[AutomationTypedDict]
    blocked_by_invoice: NotRequired[bool]
    email_response: NotRequired[bool]


class GetTicketLogEntriesByTicketIDResponseBody(BaseModel):
    id: Optional[int] = None

    app_user_contact_uid: Annotated[
        Optional[str], pydantic.Field(alias="appUserContactUid")
    ] = None

    app_user_contact_id: Annotated[
        Optional[int], pydantic.Field(alias="appUserContactId")
    ] = None

    app_user_contact_type: Annotated[
        Optional[AppUserContactType], pydantic.Field(alias="appUserContactType")
    ] = None

    type: Optional[GetTicketLogEntriesByTicketIDType] = None

    body: Optional[str] = None

    html_body: Annotated[Optional[str], pydantic.Field(alias="htmlBody")] = None

    full_email_body: Annotated[Optional[str], pydantic.Field(alias="fullEmailBody")] = (
        None
    )

    public_entry: Annotated[Optional[bool], pydantic.Field(alias="publicEntry")] = None

    system: Optional[bool] = None

    create_time: Annotated[Optional[float], pydantic.Field(alias="createTime")] = None

    change_diff: Annotated[Optional[ChangeDiff], pydantic.Field(alias="changeDiff")] = (
        None
    )

    activity_id: Annotated[Optional[int], pydantic.Field(alias="activityId")] = None

    time_tracked: Annotated[Optional[int], pydantic.Field(alias="timeTracked")] = None

    technician_tagged: Annotated[
        Optional[List[int]], pydantic.Field(alias="technicianTagged")
    ] = None

    technicians_tagged_metadata: Annotated[
        Optional[List[TechniciansTaggedMetadata]],
        pydantic.Field(alias="techniciansTaggedMetadata"),
    ] = None

    automation: Optional[Automation] = None

    blocked_by_invoice: Annotated[
        Optional[bool], pydantic.Field(alias="blockedByInvoice")
    ] = None

    email_response: Annotated[Optional[bool], pydantic.Field(alias="emailResponse")] = (
        None
    )

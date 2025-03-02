"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateOrganizationChecklistsFromTemplatesRequestTypedDict(TypedDict):
    organization_id: int
    request_body: NotRequired[List[int]]


class CreateOrganizationChecklistsFromTemplatesRequest(BaseModel):
    organization_id: Annotated[
        int,
        pydantic.Field(alias="organizationId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    request_body: Annotated[
        Optional[List[int]],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class CreateOrganizationChecklistsFromTemplatesDescriptionTypedDict(TypedDict):
    r"""Task description"""

    text: NotRequired[str]
    html: NotRequired[str]


class CreateOrganizationChecklistsFromTemplatesDescription(BaseModel):
    r"""Task description"""

    text: Optional[str] = None

    html: Optional[str] = None


class CreateOrganizationChecklistsFromTemplatesAssignedToTypedDict(TypedDict):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class CreateOrganizationChecklistsFromTemplatesAssignedTo(BaseModel):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class CreateOrganizationChecklistsFromTemplatesLastUpdatedByTypedDict(TypedDict):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class CreateOrganizationChecklistsFromTemplatesLastUpdatedBy(BaseModel):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class CreateOrganizationChecklistsFromTemplatesOrganizationChecklistsDescriptionTypedDict(
    TypedDict
):
    r"""Task description"""

    text: NotRequired[str]
    html: NotRequired[str]


class CreateOrganizationChecklistsFromTemplatesOrganizationChecklistsDescription(
    BaseModel
):
    r"""Task description"""

    text: Optional[str] = None

    html: Optional[str] = None


class CreateOrganizationChecklistsFromTemplatesOrganizationChecklistsAssignedToTypedDict(
    TypedDict
):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class CreateOrganizationChecklistsFromTemplatesOrganizationChecklistsAssignedTo(
    BaseModel
):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class CreateOrganizationChecklistsFromTemplatesCompletedByTypedDict(TypedDict):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class CreateOrganizationChecklistsFromTemplatesCompletedBy(BaseModel):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class CreateOrganizationChecklistsFromTemplatesTasksTypedDict(TypedDict):
    r"""Checklist's tasks"""

    id: NotRequired[int]
    r"""Identifier"""
    position: NotRequired[int]
    r"""Position of the task"""
    name: NotRequired[str]
    r"""Task name"""
    description: NotRequired[
        CreateOrganizationChecklistsFromTemplatesOrganizationChecklistsDescriptionTypedDict
    ]
    r"""Task description"""
    assigned_to: NotRequired[
        CreateOrganizationChecklistsFromTemplatesOrganizationChecklistsAssignedToTypedDict
    ]
    r"""Archive by user"""
    due_date: NotRequired[float]
    r"""Due date"""
    completed: NotRequired[bool]
    r"""Indicates if the checklist is completed"""
    completed_on: NotRequired[float]
    r"""Date of completion"""
    completed_by: NotRequired[
        CreateOrganizationChecklistsFromTemplatesCompletedByTypedDict
    ]
    r"""Archive by user"""


class CreateOrganizationChecklistsFromTemplatesTasks(BaseModel):
    r"""Checklist's tasks"""

    id: Optional[int] = None
    r"""Identifier"""

    position: Optional[int] = None
    r"""Position of the task"""

    name: Optional[str] = None
    r"""Task name"""

    description: Optional[
        CreateOrganizationChecklistsFromTemplatesOrganizationChecklistsDescription
    ] = None
    r"""Task description"""

    assigned_to: Annotated[
        Optional[
            CreateOrganizationChecklistsFromTemplatesOrganizationChecklistsAssignedTo
        ],
        pydantic.Field(alias="assignedTo"),
    ] = None
    r"""Archive by user"""

    due_date: Annotated[Optional[float], pydantic.Field(alias="dueDate")] = None
    r"""Due date"""

    completed: Optional[bool] = None
    r"""Indicates if the checklist is completed"""

    completed_on: Annotated[Optional[float], pydantic.Field(alias="completedOn")] = None
    r"""Date of completion"""

    completed_by: Annotated[
        Optional[CreateOrganizationChecklistsFromTemplatesCompletedBy],
        pydantic.Field(alias="completedBy"),
    ] = None
    r"""Archive by user"""


class CreateOrganizationChecklistsFromTemplatesArchivedByTypedDict(TypedDict):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class CreateOrganizationChecklistsFromTemplatesArchivedBy(BaseModel):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class CreateOrganizationChecklistsFromTemplatesResponseBodyTypedDict(TypedDict):
    id: NotRequired[int]
    r"""Identifier"""
    name: NotRequired[str]
    r"""Checklist name (must be unique)"""
    description: NotRequired[
        CreateOrganizationChecklistsFromTemplatesDescriptionTypedDict
    ]
    r"""Task description"""
    required: NotRequired[bool]
    r"""Indicates if the checklist completion is required"""
    due_date: NotRequired[float]
    r"""Due date"""
    completed: NotRequired[bool]
    r"""Indicates if the checklist is completed"""
    completed_on: NotRequired[float]
    r"""Date of completion"""
    assigned_to: NotRequired[
        CreateOrganizationChecklistsFromTemplatesAssignedToTypedDict
    ]
    r"""Archive by user"""
    last_updated_on: NotRequired[float]
    r"""Last updated on"""
    last_updated_by: NotRequired[
        CreateOrganizationChecklistsFromTemplatesLastUpdatedByTypedDict
    ]
    r"""Archive by user"""
    completed_task_count: NotRequired[int]
    r"""Last updated by user"""
    total_task_count: NotRequired[int]
    r"""Checklist's total tasks count"""
    tasks: NotRequired[List[CreateOrganizationChecklistsFromTemplatesTasksTypedDict]]
    r"""Checklist's tasks"""
    organization_id: NotRequired[int]
    r"""Organization identifier"""
    client_name: NotRequired[str]
    r"""Client name"""
    archived: NotRequired[bool]
    r"""Indicates if the checklist is archived"""
    archived_by: NotRequired[
        CreateOrganizationChecklistsFromTemplatesArchivedByTypedDict
    ]
    r"""Archive by user"""
    archive_time: NotRequired[float]
    r"""Archive time"""


class CreateOrganizationChecklistsFromTemplatesResponseBody(BaseModel):
    id: Optional[int] = None
    r"""Identifier"""

    name: Optional[str] = None
    r"""Checklist name (must be unique)"""

    description: Optional[CreateOrganizationChecklistsFromTemplatesDescription] = None
    r"""Task description"""

    required: Optional[bool] = None
    r"""Indicates if the checklist completion is required"""

    due_date: Annotated[Optional[float], pydantic.Field(alias="dueDate")] = None
    r"""Due date"""

    completed: Optional[bool] = None
    r"""Indicates if the checklist is completed"""

    completed_on: Annotated[Optional[float], pydantic.Field(alias="completedOn")] = None
    r"""Date of completion"""

    assigned_to: Annotated[
        Optional[CreateOrganizationChecklistsFromTemplatesAssignedTo],
        pydantic.Field(alias="assignedTo"),
    ] = None
    r"""Archive by user"""

    last_updated_on: Annotated[
        Optional[float], pydantic.Field(alias="lastUpdatedOn")
    ] = None
    r"""Last updated on"""

    last_updated_by: Annotated[
        Optional[CreateOrganizationChecklistsFromTemplatesLastUpdatedBy],
        pydantic.Field(alias="lastUpdatedBy"),
    ] = None
    r"""Archive by user"""

    completed_task_count: Annotated[
        Optional[int], pydantic.Field(alias="completedTaskCount")
    ] = None
    r"""Last updated by user"""

    total_task_count: Annotated[
        Optional[int], pydantic.Field(alias="totalTaskCount")
    ] = None
    r"""Checklist's total tasks count"""

    tasks: Optional[List[CreateOrganizationChecklistsFromTemplatesTasks]] = None
    r"""Checklist's tasks"""

    organization_id: Annotated[
        Optional[int], pydantic.Field(alias="organizationId")
    ] = None
    r"""Organization identifier"""

    client_name: Annotated[Optional[str], pydantic.Field(alias="clientName")] = None
    r"""Client name"""

    archived: Optional[bool] = None
    r"""Indicates if the checklist is archived"""

    archived_by: Annotated[
        Optional[CreateOrganizationChecklistsFromTemplatesArchivedBy],
        pydantic.Field(alias="archivedBy"),
    ] = None
    r"""Archive by user"""

    archive_time: Annotated[Optional[float], pydantic.Field(alias="archiveTime")] = None
    r"""Archive time"""

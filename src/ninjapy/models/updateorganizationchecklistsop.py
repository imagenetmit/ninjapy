"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateOrganizationChecklistsDescriptionTypedDict(TypedDict):
    r"""Task description"""

    text: NotRequired[str]
    html: NotRequired[str]


class UpdateOrganizationChecklistsDescription(BaseModel):
    r"""Task description"""

    text: Optional[str] = None

    html: Optional[str] = None


class UpdateOrganizationChecklistsOrganizationChecklistsDescriptionTypedDict(TypedDict):
    r"""Task description"""

    text: NotRequired[str]
    html: NotRequired[str]


class UpdateOrganizationChecklistsOrganizationChecklistsDescription(BaseModel):
    r"""Task description"""

    text: Optional[str] = None

    html: Optional[str] = None


class UpdateOrganizationChecklistsTasksTypedDict(TypedDict):
    r"""Checklist tasks"""

    id: NotRequired[int]
    r"""Identifier"""
    position: NotRequired[int]
    r"""Position of the task"""
    name: NotRequired[str]
    r"""Task name"""
    description: NotRequired[
        UpdateOrganizationChecklistsOrganizationChecklistsDescriptionTypedDict
    ]
    r"""Task description"""
    assigned_to_user_id: NotRequired[int]
    r"""User identifier assigned to the checklist task"""
    due_date: NotRequired[float]
    r"""Due date"""
    completed: NotRequired[bool]
    r"""Indicates if the checklist is completed"""


class UpdateOrganizationChecklistsTasks(BaseModel):
    r"""Checklist tasks"""

    id: Optional[int] = None
    r"""Identifier"""

    position: Optional[int] = None
    r"""Position of the task"""

    name: Optional[str] = None
    r"""Task name"""

    description: Optional[
        UpdateOrganizationChecklistsOrganizationChecklistsDescription
    ] = None
    r"""Task description"""

    assigned_to_user_id: Annotated[
        Optional[int], pydantic.Field(alias="assignedToUserId")
    ] = None
    r"""User identifier assigned to the checklist task"""

    due_date: Annotated[Optional[float], pydantic.Field(alias="dueDate")] = None
    r"""Due date"""

    completed: Optional[bool] = None
    r"""Indicates if the checklist is completed"""


class UpdateOrganizationChecklistsRequestBodyTypedDict(TypedDict):
    checklist_id: NotRequired[int]
    r"""Checklist identifier"""
    name: NotRequired[str]
    r"""Checklist name"""
    description: NotRequired[UpdateOrganizationChecklistsDescriptionTypedDict]
    r"""Task description"""
    required: NotRequired[bool]
    r"""Indicates if the checklist completion is required"""
    due_date: NotRequired[float]
    r"""Due date"""
    assigned_to_user_id: NotRequired[int]
    r"""User identifier assigned to the checklist"""
    tasks: NotRequired[List[UpdateOrganizationChecklistsTasksTypedDict]]
    r"""Checklist tasks"""


class UpdateOrganizationChecklistsRequestBody(BaseModel):
    checklist_id: Annotated[Optional[int], pydantic.Field(alias="checklistId")] = None
    r"""Checklist identifier"""

    name: Optional[str] = None
    r"""Checklist name"""

    description: Optional[UpdateOrganizationChecklistsDescription] = None
    r"""Task description"""

    required: Optional[bool] = None
    r"""Indicates if the checklist completion is required"""

    due_date: Annotated[Optional[float], pydantic.Field(alias="dueDate")] = None
    r"""Due date"""

    assigned_to_user_id: Annotated[
        Optional[int], pydantic.Field(alias="assignedToUserId")
    ] = None
    r"""User identifier assigned to the checklist"""

    tasks: Optional[List[UpdateOrganizationChecklistsTasks]] = None
    r"""Checklist tasks"""


class UpdateOrganizationChecklistsOrganizationChecklistsResponseDescriptionTypedDict(
    TypedDict
):
    r"""Task description"""

    text: NotRequired[str]
    html: NotRequired[str]


class UpdateOrganizationChecklistsOrganizationChecklistsResponseDescription(BaseModel):
    r"""Task description"""

    text: Optional[str] = None

    html: Optional[str] = None


class UpdateOrganizationChecklistsAssignedToTypedDict(TypedDict):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class UpdateOrganizationChecklistsAssignedTo(BaseModel):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class UpdateOrganizationChecklistsLastUpdatedByTypedDict(TypedDict):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class UpdateOrganizationChecklistsLastUpdatedBy(BaseModel):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class UpdateOrganizationChecklistsOrganizationChecklistsResponse200DescriptionTypedDict(
    TypedDict
):
    r"""Task description"""

    text: NotRequired[str]
    html: NotRequired[str]


class UpdateOrganizationChecklistsOrganizationChecklistsResponse200Description(
    BaseModel
):
    r"""Task description"""

    text: Optional[str] = None

    html: Optional[str] = None


class UpdateOrganizationChecklistsOrganizationChecklistsAssignedToTypedDict(TypedDict):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class UpdateOrganizationChecklistsOrganizationChecklistsAssignedTo(BaseModel):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class UpdateOrganizationChecklistsCompletedByTypedDict(TypedDict):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class UpdateOrganizationChecklistsCompletedBy(BaseModel):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class UpdateOrganizationChecklistsOrganizationChecklistsTasksTypedDict(TypedDict):
    r"""Checklist's tasks"""

    id: NotRequired[int]
    r"""Identifier"""
    position: NotRequired[int]
    r"""Position of the task"""
    name: NotRequired[str]
    r"""Task name"""
    description: NotRequired[
        UpdateOrganizationChecklistsOrganizationChecklistsResponse200DescriptionTypedDict
    ]
    r"""Task description"""
    assigned_to: NotRequired[
        UpdateOrganizationChecklistsOrganizationChecklistsAssignedToTypedDict
    ]
    r"""Archive by user"""
    due_date: NotRequired[float]
    r"""Due date"""
    completed: NotRequired[bool]
    r"""Indicates if the checklist is completed"""
    completed_on: NotRequired[float]
    r"""Date of completion"""
    completed_by: NotRequired[UpdateOrganizationChecklistsCompletedByTypedDict]
    r"""Archive by user"""


class UpdateOrganizationChecklistsOrganizationChecklistsTasks(BaseModel):
    r"""Checklist's tasks"""

    id: Optional[int] = None
    r"""Identifier"""

    position: Optional[int] = None
    r"""Position of the task"""

    name: Optional[str] = None
    r"""Task name"""

    description: Optional[
        UpdateOrganizationChecklistsOrganizationChecklistsResponse200Description
    ] = None
    r"""Task description"""

    assigned_to: Annotated[
        Optional[UpdateOrganizationChecklistsOrganizationChecklistsAssignedTo],
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
        Optional[UpdateOrganizationChecklistsCompletedBy],
        pydantic.Field(alias="completedBy"),
    ] = None
    r"""Archive by user"""


class UpdateOrganizationChecklistsArchivedByTypedDict(TypedDict):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class UpdateOrganizationChecklistsArchivedBy(BaseModel):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class UpdateOrganizationChecklistsResponseBodyTypedDict(TypedDict):
    id: NotRequired[int]
    r"""Identifier"""
    name: NotRequired[str]
    r"""Checklist name (must be unique)"""
    description: NotRequired[
        UpdateOrganizationChecklistsOrganizationChecklistsResponseDescriptionTypedDict
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
    assigned_to: NotRequired[UpdateOrganizationChecklistsAssignedToTypedDict]
    r"""Archive by user"""
    last_updated_on: NotRequired[float]
    r"""Last updated on"""
    last_updated_by: NotRequired[UpdateOrganizationChecklistsLastUpdatedByTypedDict]
    r"""Archive by user"""
    completed_task_count: NotRequired[int]
    r"""Last updated by user"""
    total_task_count: NotRequired[int]
    r"""Checklist's total tasks count"""
    tasks: NotRequired[
        List[UpdateOrganizationChecklistsOrganizationChecklistsTasksTypedDict]
    ]
    r"""Checklist's tasks"""
    organization_id: NotRequired[int]
    r"""Organization identifier"""
    client_name: NotRequired[str]
    r"""Client name"""
    archived: NotRequired[bool]
    r"""Indicates if the checklist is archived"""
    archived_by: NotRequired[UpdateOrganizationChecklistsArchivedByTypedDict]
    r"""Archive by user"""
    archive_time: NotRequired[float]
    r"""Archive time"""


class UpdateOrganizationChecklistsResponseBody(BaseModel):
    id: Optional[int] = None
    r"""Identifier"""

    name: Optional[str] = None
    r"""Checklist name (must be unique)"""

    description: Optional[
        UpdateOrganizationChecklistsOrganizationChecklistsResponseDescription
    ] = None
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
        Optional[UpdateOrganizationChecklistsAssignedTo],
        pydantic.Field(alias="assignedTo"),
    ] = None
    r"""Archive by user"""

    last_updated_on: Annotated[
        Optional[float], pydantic.Field(alias="lastUpdatedOn")
    ] = None
    r"""Last updated on"""

    last_updated_by: Annotated[
        Optional[UpdateOrganizationChecklistsLastUpdatedBy],
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

    tasks: Optional[List[UpdateOrganizationChecklistsOrganizationChecklistsTasks]] = (
        None
    )
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
        Optional[UpdateOrganizationChecklistsArchivedBy],
        pydantic.Field(alias="archivedBy"),
    ] = None
    r"""Archive by user"""

    archive_time: Annotated[Optional[float], pydantic.Field(alias="archiveTime")] = None
    r"""Archive time"""

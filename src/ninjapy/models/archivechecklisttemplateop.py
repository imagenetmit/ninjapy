"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ArchiveChecklistTemplateDescriptionTypedDict(TypedDict):
    r"""Task description"""

    text: NotRequired[str]
    html: NotRequired[str]


class ArchiveChecklistTemplateDescription(BaseModel):
    r"""Task description"""

    text: Optional[str] = None

    html: Optional[str] = None


class ArchiveChecklistTemplateChecklistTemplatesDescriptionTypedDict(TypedDict):
    r"""Task description"""

    text: NotRequired[str]
    html: NotRequired[str]


class ArchiveChecklistTemplateChecklistTemplatesDescription(BaseModel):
    r"""Task description"""

    text: Optional[str] = None

    html: Optional[str] = None


class ArchiveChecklistTemplateTasksTypedDict(TypedDict):
    r"""Checklist template tasks"""

    position: NotRequired[int]
    r"""Position of the task"""
    name: NotRequired[str]
    r"""Task name"""
    description: NotRequired[
        ArchiveChecklistTemplateChecklistTemplatesDescriptionTypedDict
    ]
    r"""Task description"""


class ArchiveChecklistTemplateTasks(BaseModel):
    r"""Checklist template tasks"""

    position: Optional[int] = None
    r"""Position of the task"""

    name: Optional[str] = None
    r"""Task name"""

    description: Optional[ArchiveChecklistTemplateChecklistTemplatesDescription] = None
    r"""Task description"""


class LastUpdatedByTypedDict(TypedDict):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class LastUpdatedBy(BaseModel):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class ArchivedByTypedDict(TypedDict):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class ArchivedBy(BaseModel):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class ArchiveChecklistTemplateResponseBodyTypedDict(TypedDict):
    id: NotRequired[int]
    r"""Identifier"""
    name: NotRequired[str]
    r"""Checklist template name (must be unique)"""
    description: NotRequired[ArchiveChecklistTemplateDescriptionTypedDict]
    r"""Task description"""
    tasks: NotRequired[List[ArchiveChecklistTemplateTasksTypedDict]]
    r"""Checklist template tasks"""
    required: NotRequired[bool]
    r"""Indicates if the checklist completion is required"""
    last_updated_on: NotRequired[float]
    r"""Last updated on"""
    last_updated_by: NotRequired[LastUpdatedByTypedDict]
    r"""Archive by user"""
    archived: NotRequired[bool]
    r"""Indicates if the checklist template is archived"""
    archived_by: NotRequired[ArchivedByTypedDict]
    r"""Archive by user"""
    archive_time: NotRequired[float]
    r"""Archive time"""


class ArchiveChecklistTemplateResponseBody(BaseModel):
    id: Optional[int] = None
    r"""Identifier"""

    name: Optional[str] = None
    r"""Checklist template name (must be unique)"""

    description: Optional[ArchiveChecklistTemplateDescription] = None
    r"""Task description"""

    tasks: Optional[List[ArchiveChecklistTemplateTasks]] = None
    r"""Checklist template tasks"""

    required: Optional[bool] = None
    r"""Indicates if the checklist completion is required"""

    last_updated_on: Annotated[
        Optional[float], pydantic.Field(alias="lastUpdatedOn")
    ] = None
    r"""Last updated on"""

    last_updated_by: Annotated[
        Optional[LastUpdatedBy], pydantic.Field(alias="lastUpdatedBy")
    ] = None
    r"""Archive by user"""

    archived: Optional[bool] = None
    r"""Indicates if the checklist template is archived"""

    archived_by: Annotated[Optional[ArchivedBy], pydantic.Field(alias="archivedBy")] = (
        None
    )
    r"""Archive by user"""

    archive_time: Annotated[Optional[float], pydantic.Field(alias="archiveTime")] = None
    r"""Archive time"""

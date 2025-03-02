"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetChecklistTemplatesRequestTypedDict(TypedDict):
    checklist_template_ids: NotRequired[str]
    checklist_template_name: NotRequired[str]
    required: NotRequired[bool]
    include_archived: NotRequired[bool]


class GetChecklistTemplatesRequest(BaseModel):
    checklist_template_ids: Annotated[
        Optional[str],
        pydantic.Field(alias="checklistTemplateIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    checklist_template_name: Annotated[
        Optional[str],
        pydantic.Field(alias="checklistTemplateName"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    required: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    include_archived: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeArchived"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class GetChecklistTemplatesDescriptionTypedDict(TypedDict):
    r"""Task description"""

    text: NotRequired[str]
    html: NotRequired[str]


class GetChecklistTemplatesDescription(BaseModel):
    r"""Task description"""

    text: Optional[str] = None

    html: Optional[str] = None


class GetChecklistTemplatesChecklistTemplatesDescriptionTypedDict(TypedDict):
    r"""Task description"""

    text: NotRequired[str]
    html: NotRequired[str]


class GetChecklistTemplatesChecklistTemplatesDescription(BaseModel):
    r"""Task description"""

    text: Optional[str] = None

    html: Optional[str] = None


class GetChecklistTemplatesTasksTypedDict(TypedDict):
    r"""Checklist template tasks"""

    position: NotRequired[int]
    r"""Position of the task"""
    name: NotRequired[str]
    r"""Task name"""
    description: NotRequired[
        GetChecklistTemplatesChecklistTemplatesDescriptionTypedDict
    ]
    r"""Task description"""


class GetChecklistTemplatesTasks(BaseModel):
    r"""Checklist template tasks"""

    position: Optional[int] = None
    r"""Position of the task"""

    name: Optional[str] = None
    r"""Task name"""

    description: Optional[GetChecklistTemplatesChecklistTemplatesDescription] = None
    r"""Task description"""


class GetChecklistTemplatesLastUpdatedByTypedDict(TypedDict):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class GetChecklistTemplatesLastUpdatedBy(BaseModel):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class GetChecklistTemplatesArchivedByTypedDict(TypedDict):
    r"""Archive by user"""

    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    deleted: NotRequired[bool]


class GetChecklistTemplatesArchivedBy(BaseModel):
    r"""Archive by user"""

    id: Optional[int] = None

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None

    deleted: Optional[bool] = None


class GetChecklistTemplatesResponseBodyTypedDict(TypedDict):
    id: NotRequired[int]
    r"""Identifier"""
    name: NotRequired[str]
    r"""Checklist template name (must be unique)"""
    description: NotRequired[GetChecklistTemplatesDescriptionTypedDict]
    r"""Task description"""
    tasks: NotRequired[List[GetChecklistTemplatesTasksTypedDict]]
    r"""Checklist template tasks"""
    required: NotRequired[bool]
    r"""Indicates if the checklist completion is required"""
    last_updated_on: NotRequired[float]
    r"""Last updated on"""
    last_updated_by: NotRequired[GetChecklistTemplatesLastUpdatedByTypedDict]
    r"""Archive by user"""
    archived: NotRequired[bool]
    r"""Indicates if the checklist template is archived"""
    archived_by: NotRequired[GetChecklistTemplatesArchivedByTypedDict]
    r"""Archive by user"""
    archive_time: NotRequired[float]
    r"""Archive time"""


class GetChecklistTemplatesResponseBody(BaseModel):
    id: Optional[int] = None
    r"""Identifier"""

    name: Optional[str] = None
    r"""Checklist template name (must be unique)"""

    description: Optional[GetChecklistTemplatesDescription] = None
    r"""Task description"""

    tasks: Optional[List[GetChecklistTemplatesTasks]] = None
    r"""Checklist template tasks"""

    required: Optional[bool] = None
    r"""Indicates if the checklist completion is required"""

    last_updated_on: Annotated[
        Optional[float], pydantic.Field(alias="lastUpdatedOn")
    ] = None
    r"""Last updated on"""

    last_updated_by: Annotated[
        Optional[GetChecklistTemplatesLastUpdatedBy],
        pydantic.Field(alias="lastUpdatedBy"),
    ] = None
    r"""Archive by user"""

    archived: Optional[bool] = None
    r"""Indicates if the checklist template is archived"""

    archived_by: Annotated[
        Optional[GetChecklistTemplatesArchivedBy], pydantic.Field(alias="archivedBy")
    ] = None
    r"""Archive by user"""

    archive_time: Annotated[Optional[float], pydantic.Field(alias="archiveTime")] = None
    r"""Archive time"""

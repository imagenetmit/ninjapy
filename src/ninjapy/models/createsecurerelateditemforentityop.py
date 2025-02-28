"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import io
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import IO, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateSecureRelatedItemForEntityPathParamEntityType(str, Enum):
    ORGANIZATION = "ORGANIZATION"
    DOCUMENT = "DOCUMENT"
    LOCATION = "LOCATION"
    NODE = "NODE"
    CHECKLIST = "CHECKLIST"
    KB_DOCUMENT = "KB_DOCUMENT"


class CreateSecureRelatedItemForEntityRequestTypedDict(TypedDict):
    entity_type: CreateSecureRelatedItemForEntityPathParamEntityType
    entity_id: int
    request_body: NotRequired[Union[bytes, IO[bytes], io.BufferedReader]]


class CreateSecureRelatedItemForEntityRequest(BaseModel):
    entity_type: Annotated[
        CreateSecureRelatedItemForEntityPathParamEntityType,
        pydantic.Field(alias="entityType"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    entity_id: Annotated[
        int,
        pydantic.Field(alias="entityId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    request_body: Annotated[
        Optional[Union[bytes, IO[bytes], io.BufferedReader]],
        FieldMetadata(request=RequestMetadata(media_type="*/*")),
    ] = None


class CreateSecureRelatedItemForEntityType(str, Enum):
    r"""Type of Relation"""

    VALUE = "VALUE"
    ENTITY = "ENTITY"


class CreateSecureRelatedItemForEntityEntityTypedDict(TypedDict):
    r"""Entity"""


class CreateSecureRelatedItemForEntityEntity(BaseModel):
    r"""Entity"""


class CreateSecureRelatedItemForEntityEntityType(str, Enum):
    r"""Entity Type"""

    ORGANIZATION = "ORGANIZATION"
    DOCUMENT = "DOCUMENT"
    LOCATION = "LOCATION"
    NODE = "NODE"
    CHECKLIST = "CHECKLIST"
    KB_DOCUMENT = "KB_DOCUMENT"


class CreateSecureRelatedItemForEntityRelEntityTypedDict(TypedDict):
    r"""Related Entity"""


class CreateSecureRelatedItemForEntityRelEntity(BaseModel):
    r"""Related Entity"""


class CreateSecureRelatedItemForEntityRelEntityType(str, Enum):
    r"""Related Entity Type"""

    ORGANIZATION = "ORGANIZATION"
    DOCUMENT = "DOCUMENT"
    LOCATION = "LOCATION"
    NODE = "NODE"
    ATTACHMENT = "ATTACHMENT"
    TECHNICIAN = "TECHNICIAN"
    CREDENTIAL = "CREDENTIAL"
    CHECKLIST = "CHECKLIST"
    END_USER = "END_USER"
    CONTACT = "CONTACT"
    KB_DOCUMENT = "KB_DOCUMENT"
    SECURE = "SECURE"


class CreateSecureRelatedItemForEntityValueTypedDict(TypedDict):
    r"""Related item value (Attachment meta data / Secure information)"""


class CreateSecureRelatedItemForEntityValue(BaseModel):
    r"""Related item value (Attachment meta data / Secure information)"""


class CreateSecureRelatedItemForEntityResponseBodyTypedDict(TypedDict):
    r"""Returns the secure related item created for an entity"""

    id: NotRequired[int]
    r"""Identifier"""
    type: NotRequired[CreateSecureRelatedItemForEntityType]
    r"""Type of Relation"""
    entity: NotRequired[CreateSecureRelatedItemForEntityEntityTypedDict]
    r"""Entity"""
    entity_id: NotRequired[int]
    r"""Entity Identifier"""
    entity_type: NotRequired[CreateSecureRelatedItemForEntityEntityType]
    r"""Entity Type"""
    rel_entity: NotRequired[CreateSecureRelatedItemForEntityRelEntityTypedDict]
    r"""Related Entity"""
    rel_entity_id: NotRequired[int]
    r"""Related Entity Identifier"""
    rel_entity_type: NotRequired[CreateSecureRelatedItemForEntityRelEntityType]
    r"""Related Entity Type"""
    value: NotRequired[CreateSecureRelatedItemForEntityValueTypedDict]
    r"""Related item value (Attachment meta data / Secure information)"""
    create_time: NotRequired[float]
    r"""Creation time"""
    update_time: NotRequired[float]
    r"""Last update time"""
    created_by_app_user_id: NotRequired[int]
    r"""The identifier of the user who created the related item"""
    updated_by_app_user_id: NotRequired[int]
    r"""The identifier of the last user to update the related item"""


class CreateSecureRelatedItemForEntityResponseBody(BaseModel):
    r"""Returns the secure related item created for an entity"""

    id: Optional[int] = None
    r"""Identifier"""

    type: Optional[CreateSecureRelatedItemForEntityType] = None
    r"""Type of Relation"""

    entity: Optional[CreateSecureRelatedItemForEntityEntity] = None
    r"""Entity"""

    entity_id: Annotated[Optional[int], pydantic.Field(alias="entityId")] = None
    r"""Entity Identifier"""

    entity_type: Annotated[
        Optional[CreateSecureRelatedItemForEntityEntityType],
        pydantic.Field(alias="entityType"),
    ] = None
    r"""Entity Type"""

    rel_entity: Annotated[
        Optional[CreateSecureRelatedItemForEntityRelEntity],
        pydantic.Field(alias="relEntity"),
    ] = None
    r"""Related Entity"""

    rel_entity_id: Annotated[Optional[int], pydantic.Field(alias="relEntityId")] = None
    r"""Related Entity Identifier"""

    rel_entity_type: Annotated[
        Optional[CreateSecureRelatedItemForEntityRelEntityType],
        pydantic.Field(alias="relEntityType"),
    ] = None
    r"""Related Entity Type"""

    value: Optional[CreateSecureRelatedItemForEntityValue] = None
    r"""Related item value (Attachment meta data / Secure information)"""

    create_time: Annotated[Optional[float], pydantic.Field(alias="createTime")] = None
    r"""Creation time"""

    update_time: Annotated[Optional[float], pydantic.Field(alias="updateTime")] = None
    r"""Last update time"""

    created_by_app_user_id: Annotated[
        Optional[int], pydantic.Field(alias="createdByAppUserId")
    ] = None
    r"""The identifier of the user who created the related item"""

    updated_by_app_user_id: Annotated[
        Optional[int], pydantic.Field(alias="updatedByAppUserId")
    ] = None
    r"""The identifier of the last user to update the related item"""

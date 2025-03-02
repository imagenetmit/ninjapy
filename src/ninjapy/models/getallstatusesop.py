"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetAllStatusesResponseBodyTypedDict(TypedDict):
    name: NotRequired[str]
    display_name: NotRequired[str]
    parent_id: NotRequired[int]
    status_id: NotRequired[int]


class GetAllStatusesResponseBody(BaseModel):
    name: Optional[str] = None

    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None

    parent_id: Annotated[Optional[int], pydantic.Field(alias="parentId")] = None

    status_id: Annotated[Optional[int], pydantic.Field(alias="statusId")] = None

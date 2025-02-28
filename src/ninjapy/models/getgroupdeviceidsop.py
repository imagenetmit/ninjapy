"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class GetGroupDeviceIdsRequestTypedDict(TypedDict):
    id: int
    r"""Group identifier"""


class GetGroupDeviceIdsRequest(BaseModel):
    id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Group identifier"""

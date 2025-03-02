"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetDeviceLinkRequestTypedDict(TypedDict):
    id: int
    r"""Device identifier"""
    redirect: NotRequired[bool]
    r"""Return redirect response"""


class GetDeviceLinkRequest(BaseModel):
    id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Device identifier"""

    redirect: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Return redirect response"""


class GetDeviceLinkResponseBodyTypedDict(TypedDict):
    r"""default response"""

    url: NotRequired[str]
    r"""URL"""
    expires: NotRequired[float]
    r"""Link expiration time"""


class GetDeviceLinkResponseBody(BaseModel):
    r"""default response"""

    url: Optional[str] = None
    r"""URL"""

    expires: Optional[float] = None
    r"""Link expiration time"""

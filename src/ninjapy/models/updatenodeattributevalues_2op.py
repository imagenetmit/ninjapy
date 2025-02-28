"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateNodeAttributeValues2RequestBodyTypedDict(TypedDict):
    pass


class UpdateNodeAttributeValues2RequestBody(BaseModel):
    pass


class UpdateNodeAttributeValues2RequestTypedDict(TypedDict):
    id: int
    location_id: int
    request_body: NotRequired[Dict[str, UpdateNodeAttributeValues2RequestBodyTypedDict]]


class UpdateNodeAttributeValues2Request(BaseModel):
    id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    location_id: Annotated[
        int,
        pydantic.Field(alias="locationId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    request_body: Annotated[
        Optional[Dict[str, UpdateNodeAttributeValues2RequestBody]],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None

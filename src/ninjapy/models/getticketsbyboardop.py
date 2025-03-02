"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from ninjapy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class Direction(str, Enum):
    ASC = "ASC"
    DESC = "DESC"


class SortByTypedDict(TypedDict):
    field: NotRequired[str]
    direction: NotRequired[Direction]


class SortBy(BaseModel):
    field: Optional[str] = None

    direction: Optional[Direction] = None


class FiltersTypedDict(TypedDict):
    field: NotRequired[str]
    operator: NotRequired[str]
    value: NotRequired[str]


class Filters(BaseModel):
    field: Optional[str] = None

    operator: Optional[str] = None

    value: Optional[str] = None


class GetTicketsByBoardRequestBodyTypedDict(TypedDict):
    sort_by: NotRequired[List[SortByTypedDict]]
    filters: NotRequired[List[FiltersTypedDict]]
    page_size: NotRequired[int]
    search_criteria: NotRequired[str]
    include_columns: NotRequired[List[str]]
    last_cursor_id: NotRequired[int]


class GetTicketsByBoardRequestBody(BaseModel):
    sort_by: Annotated[Optional[List[SortBy]], pydantic.Field(alias="sortBy")] = None

    filters: Optional[List[Filters]] = None

    page_size: Annotated[Optional[int], pydantic.Field(alias="pageSize")] = None

    search_criteria: Annotated[
        Optional[str], pydantic.Field(alias="searchCriteria")
    ] = None

    include_columns: Annotated[
        Optional[List[str]], pydantic.Field(alias="includeColumns")
    ] = None

    last_cursor_id: Annotated[Optional[int], pydantic.Field(alias="lastCursorId")] = (
        None
    )


class GetTicketsByBoardRequestTypedDict(TypedDict):
    board_id: int
    request_body: NotRequired[GetTicketsByBoardRequestBodyTypedDict]


class GetTicketsByBoardRequest(BaseModel):
    board_id: Annotated[
        int,
        pydantic.Field(alias="boardId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    request_body: Annotated[
        Optional[GetTicketsByBoardRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class DataTypedDict(TypedDict):
    pass


class Data(BaseModel):
    pass


class GetTicketsByBoardDirection(str, Enum):
    ASC = "ASC"
    DESC = "DESC"


class GetTicketsByBoardSortByTypedDict(TypedDict):
    field: NotRequired[str]
    direction: NotRequired[GetTicketsByBoardDirection]


class GetTicketsByBoardSortBy(BaseModel):
    field: Optional[str] = None

    direction: Optional[GetTicketsByBoardDirection] = None


class GetTicketsByBoardType(str, Enum):
    DROPDOWN = "DROPDOWN"
    MULTI_SELECT = "MULTI_SELECT"
    CHECKBOX = "CHECKBOX"
    TEXT = "TEXT"
    TEXT_MULTILINE = "TEXT_MULTILINE"
    TEXT_ENCRYPTED = "TEXT_ENCRYPTED"
    NUMERIC = "NUMERIC"
    DECIMAL = "DECIMAL"
    DATE = "DATE"
    DATE_TIME = "DATE_TIME"
    TIME = "TIME"
    ATTACHMENT = "ATTACHMENT"
    NODE_DROPDOWN = "NODE_DROPDOWN"
    NODE_MULTI_SELECT = "NODE_MULTI_SELECT"
    CLIENT_DROPDOWN = "CLIENT_DROPDOWN"
    CLIENT_MULTI_SELECT = "CLIENT_MULTI_SELECT"
    CLIENT_LOCATION_DROPDOWN = "CLIENT_LOCATION_DROPDOWN"
    CLIENT_LOCATION_MULTI_SELECT = "CLIENT_LOCATION_MULTI_SELECT"
    CLIENT_DOCUMENT_DROPDOWN = "CLIENT_DOCUMENT_DROPDOWN"
    CLIENT_DOCUMENT_MULTI_SELECT = "CLIENT_DOCUMENT_MULTI_SELECT"
    EMAIL = "EMAIL"
    PHONE = "PHONE"
    IP_ADDRESS = "IP_ADDRESS"
    WYSIWYG = "WYSIWYG"
    URL = "URL"


class GetTicketsByBoardAttributesTypedDict(TypedDict):
    name: NotRequired[str]
    type: NotRequired[GetTicketsByBoardType]


class GetTicketsByBoardAttributes(BaseModel):
    name: Optional[str] = None

    type: Optional[GetTicketsByBoardType] = None


class GetTicketsByBoardFiltersTypedDict(TypedDict):
    field: NotRequired[str]
    operator: NotRequired[str]
    value: NotRequired[str]


class GetTicketsByBoardFilters(BaseModel):
    field: Optional[str] = None

    operator: Optional[str] = None

    value: Optional[str] = None


class MetadataTypedDict(TypedDict):
    columns: NotRequired[List[str]]
    sort_by: NotRequired[List[GetTicketsByBoardSortByTypedDict]]
    attributes: NotRequired[Dict[str, GetTicketsByBoardAttributesTypedDict]]
    filters: NotRequired[List[GetTicketsByBoardFiltersTypedDict]]
    last_cursor_id: NotRequired[int]
    all_columns: NotRequired[List[str]]
    column_names_for_exporting: NotRequired[List[str]]
    all_required_columns: NotRequired[List[str]]


class Metadata(BaseModel):
    columns: Optional[List[str]] = None

    sort_by: Annotated[
        Optional[List[GetTicketsByBoardSortBy]], pydantic.Field(alias="sortBy")
    ] = None

    attributes: Optional[Dict[str, GetTicketsByBoardAttributes]] = None

    filters: Optional[List[GetTicketsByBoardFilters]] = None

    last_cursor_id: Annotated[Optional[int], pydantic.Field(alias="lastCursorId")] = (
        None
    )

    all_columns: Annotated[Optional[List[str]], pydantic.Field(alias="allColumns")] = (
        None
    )

    column_names_for_exporting: Annotated[
        Optional[List[str]], pydantic.Field(alias="columnNamesForExporting")
    ] = None

    all_required_columns: Annotated[
        Optional[List[str]], pydantic.Field(alias="allRequiredColumns")
    ] = None


class GetTicketsByBoardResponseBodyTypedDict(TypedDict):
    r"""default response"""

    data: NotRequired[List[Dict[str, DataTypedDict]]]
    metadata: NotRequired[MetadataTypedDict]


class GetTicketsByBoardResponseBody(BaseModel):
    r"""default response"""

    data: Optional[List[Dict[str, Data]]] = None

    metadata: Optional[Metadata] = None

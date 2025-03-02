"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ninjapy.types import BaseModel
from typing import Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class HeadersTypedDict(TypedDict):
    r"""Custom HTTP Headers (i.e. Authorization)"""

    name: NotRequired[str]
    r"""Header name"""
    value: NotRequired[str]
    r"""Header value"""


class Headers(BaseModel):
    r"""Custom HTTP Headers (i.e. Authorization)"""

    name: Optional[str] = None
    r"""Header name"""

    value: Optional[str] = None
    r"""Header value"""


class ConfigureWebhookRequestBodyTypedDict(TypedDict):
    url: NotRequired[str]
    r"""Callback (WebHook) URL for activity notifications"""
    activities: NotRequired[Dict[str, List[str]]]
    r"""Activity filter"""
    expand: NotRequired[List[str]]
    r"""Which references to expand in payloads"""
    headers: NotRequired[List[HeadersTypedDict]]
    r"""Custom HTTP Headers (i.e. Authorization)"""


class ConfigureWebhookRequestBody(BaseModel):
    url: Optional[str] = None
    r"""Callback (WebHook) URL for activity notifications"""

    activities: Optional[Dict[str, List[str]]] = None
    r"""Activity filter"""

    expand: Optional[List[str]] = None
    r"""Which references to expand in payloads"""

    headers: Optional[List[Headers]] = None
    r"""Custom HTTP Headers (i.e. Authorization)"""

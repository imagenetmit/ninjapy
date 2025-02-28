"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ninjapy.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class GetNotificationChannelsType(str, Enum):
    r"""Notification Channel Type"""

    EMAIL = "EMAIL"
    META_CHANNEL = "META_CHANNEL"
    PAGER_DUTY = "PAGER_DUTY"
    SLACK = "SLACK"
    SMS = "SMS"
    MICROSOFT_TEAMS = "MICROSOFT_TEAMS"
    WEBHOOK = "WEBHOOK"
    OTHER = "OTHER"


class GetNotificationChannelsResponseBodyTypedDict(TypedDict):
    id: NotRequired[int]
    r"""Notification Channel ID"""
    name: NotRequired[str]
    r"""Notification Channel Name"""
    description: NotRequired[str]
    r"""Notification Channel Description"""
    enabled: NotRequired[bool]
    r"""Notification Channel Enabled"""
    type: NotRequired[GetNotificationChannelsType]
    r"""Notification Channel Type"""


class GetNotificationChannelsResponseBody(BaseModel):
    id: Optional[int] = None
    r"""Notification Channel ID"""

    name: Optional[str] = None
    r"""Notification Channel Name"""

    description: Optional[str] = None
    r"""Notification Channel Description"""

    enabled: Optional[bool] = None
    r"""Notification Channel Enabled"""

    type: Optional[GetNotificationChannelsType] = None
    r"""Notification Channel Type"""

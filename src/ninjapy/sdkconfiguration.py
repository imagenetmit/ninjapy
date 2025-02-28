"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from ._hooks import SDKHooks
from ._version import (
    __gen_version__,
    __openapi_doc_version__,
    __user_agent__,
    __version__,
)
from .httpclient import AsyncHttpClient, HttpClient
from .utils import Logger, RetryConfig, remove_suffix
from dataclasses import dataclass
from ninjapy import models
from ninjapy.types import OptionalNullable, UNSET
from pydantic import Field
from typing import Callable, Dict, Optional, Tuple, Union


@dataclass
class SDKConfiguration:
    client: Union[HttpClient, None]
    client_supplied: bool
    async_client: Union[AsyncHttpClient, None]
    async_client_supplied: bool
    debug_logger: Logger
    server_url: str
    security: Optional[Union[models.Security, Callable[[], models.Security]]] = None
    language: str = "python"
    openapi_doc_version: str = __openapi_doc_version__
    sdk_version: str = __version__
    gen_version: str = __gen_version__
    user_agent: str = __user_agent__
    retry_config: OptionalNullable[RetryConfig] = Field(default_factory=lambda: UNSET)
    timeout_ms: Optional[int] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        return remove_suffix(self.server_url, "/"), {}

    def get_hooks(self) -> SDKHooks:
        return self._hooks

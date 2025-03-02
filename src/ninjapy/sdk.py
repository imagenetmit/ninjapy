"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from .utils.oauth import OAuth2ClientCredentials
import httpx
from ninjapy import models
from ninjapy._hooks import SDKHooks
from ninjapy.backup import Backup
from ninjapy.checklist_templates import ChecklistTemplates
from ninjapy.custom_fields import CustomFields
from ninjapy.devices import Devices
from ninjapy.document_templates import DocumentTemplates
from ninjapy.groups import Groups
from ninjapy.knowledge_base_articles import KnowledgeBaseArticles
from ninjapy.location import Location
from ninjapy.management import Management
from ninjapy.organization import Organization
from ninjapy.organization_checklists import OrganizationChecklists
from ninjapy.organization_documents import OrganizationDocuments
from ninjapy.queries import Queries
from ninjapy.related_items import RelatedItems
from ninjapy.system import System
from ninjapy.ticketing import Ticketing
from ninjapy.types import OptionalNullable, UNSET
from ninjapy.webhooks import Webhooks
from typing import Callable, Optional, Union, cast
import weakref


class Ninjapy(BaseSDK):
    r"""NinjaOne Public API 2.0: Ninja One Public API documentation. <br><br>
    See also: <br>
    <a href=\"https://resources.ninjarmm.com/API/Ninja+RMM+Public+API+v2.0.5+Device+Filter+Syntax.pdf\">Device Filter syntax</a><br>
    <a href=\"https://resources.ninjarmm.com/API/Ninja+RMM+Public+API+v2.0.5+Webhooks.pdf\">Webhooks</a>
    """

    management: Management
    r"""Management"""
    webhooks: Webhooks
    r"""Webhook Endpoints"""
    system: System
    r"""Core system Entities and Resources"""
    knowledge_base_articles: KnowledgeBaseArticles
    r"""Knowledge Base Articles"""
    checklist_templates: ChecklistTemplates
    r"""Checklist Templates"""
    organization_checklists: OrganizationChecklists
    r"""Organization Checklists"""
    organization_documents: OrganizationDocuments
    r"""Organization Documents"""
    document_templates: DocumentTemplates
    r"""Document Templates"""
    custom_fields: CustomFields
    r"""Custom Fields"""
    related_items: RelatedItems
    r"""Related Items"""
    backup: Backup
    r"""Backup"""
    ticketing: Ticketing
    r"""ticketing"""
    devices: Devices
    r"""Devices"""
    groups: Groups
    r"""Groups/Search"""
    organization: Organization
    r"""Organizations"""
    location: Location
    r"""Location"""
    queries: Queries
    r"""Queries"""

    def __init__(
        self,
        server_url: str,
        security: Optional[
            Union[models.Security, Callable[[], models.Security]]
        ] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param security: The security details required for authentication
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if security and isinstance(security, models.Security) and security.client_credentials:
            # Initialize OAuth2 client
            oauth2_client = OAuth2ClientCredentials(
                token_url=security.client_credentials.token_url,
                client_id=security.client_credentials.client_id,
                client_secret=security.client_credentials.client_secret,
                scope=security.client_credentials.scope,
            )
            
            # Create a security provider that fetches tokens as needed
            async def get_security():
                token = await oauth2_client.get_token()
                return models.Security(oauth2=token)
            
            security = get_security

        client_supplied = True
        if client is None:
            client = httpx.Client()
            client_supplied = False

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        async_client_supplied = True
        if async_client is None:
            async_client = httpx.AsyncClient()
            async_client_supplied = False

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                client_supplied=client_supplied,
                async_client=async_client,
                async_client_supplied=async_client_supplied,
                security=security,
                server_url=server_url,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        weakref.finalize(
            self,
            close_clients,
            cast(ClientOwner, self.sdk_configuration),
            self.sdk_configuration.client,
            self.sdk_configuration.client_supplied,
            self.sdk_configuration.async_client,
            self.sdk_configuration.async_client_supplied,
        )

        self._init_sdks()

    def _init_sdks(self):
        self.management = Management(self.sdk_configuration)
        self.webhooks = Webhooks(self.sdk_configuration)
        self.system = System(self.sdk_configuration)
        self.knowledge_base_articles = KnowledgeBaseArticles(self.sdk_configuration)
        self.checklist_templates = ChecklistTemplates(self.sdk_configuration)
        self.organization_checklists = OrganizationChecklists(self.sdk_configuration)
        self.organization_documents = OrganizationDocuments(self.sdk_configuration)
        self.document_templates = DocumentTemplates(self.sdk_configuration)
        self.custom_fields = CustomFields(self.sdk_configuration)
        self.related_items = RelatedItems(self.sdk_configuration)
        self.backup = Backup(self.sdk_configuration)
        self.ticketing = Ticketing(self.sdk_configuration)
        self.devices = Devices(self.sdk_configuration)
        self.groups = Groups(self.sdk_configuration)
        self.organization = Organization(self.sdk_configuration)
        self.location = Location(self.sdk_configuration)
        self.queries = Queries(self.sdk_configuration)

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.client is not None
            and not self.sdk_configuration.client_supplied
        ):
            self.sdk_configuration.client.close()
        self.sdk_configuration.client = None

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.async_client is not None
            and not self.sdk_configuration.async_client_supplied
        ):
            await self.sdk_configuration.async_client.aclose()
        self.sdk_configuration.async_client = None

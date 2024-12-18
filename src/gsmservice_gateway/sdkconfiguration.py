"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from ._hooks import SDKHooks
from .httpclient import AsyncHttpClient, HttpClient
from .utils import Logger, RetryConfig, remove_suffix
from dataclasses import dataclass
from gsmservice_gateway import models
from gsmservice_gateway.types import OptionalNullable, UNSET
from pydantic import Field
from typing import Callable, Dict, Optional, Tuple, Union


SERVER_PROD = "prod"
r"""Production system"""
SERVER_SANDBOX = "sandbox"
r"""Test system (SANDBOX)"""
SERVERS = {
    SERVER_PROD: "https://api.gsmservice.pl/rest",
    SERVER_SANDBOX: "https://api.gsmservice.pl/rest-sandbox",
}
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: HttpClient
    async_client: AsyncHttpClient
    debug_logger: Logger
    security: Optional[Union[models.Security, Callable[[], models.Security]]] = None
    server_url: Optional[str] = ""
    server: Optional[str] = ""
    language: str = "python"
    openapi_doc_version: str = "1.1.2"
    sdk_version: str = "2.1.5"
    gen_version: str = "2.438.15"
    user_agent: str = "speakeasy-sdk/python 2.1.5 2.438.15 1.1.2 gsmservice-gateway"
    retry_config: OptionalNullable[RetryConfig] = Field(default_factory=lambda: UNSET)
    timeout_ms: Optional[int] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url:
            return remove_suffix(self.server_url, "/"), {}
        if not self.server:
            self.server = SERVER_PROD

        if self.server not in SERVERS:
            raise ValueError(f'Invalid server "{self.server}"')

        return SERVERS[self.server], {}

    def get_hooks(self) -> SDKHooks:
        return self._hooks

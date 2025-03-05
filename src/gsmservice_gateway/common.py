"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from gsmservice_gateway import models, utils
from gsmservice_gateway._hooks import HookContext
from gsmservice_gateway.types import OptionalNullable, UNSET
from typing import Any, Mapping, Optional


class Common(BaseSDK):
    def ping(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PingResponse:
        r"""Checks API availability and version

        Check the API connection and the current API availability status. Also you will get the current API version number.

        As a successful result a `PingResponse` object will be returned.

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)
        req = self._build_request(
            method="GET",
            path="/ping",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=False,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="ping",
                oauth2_scopes=[],
                security_source=None,
            ),
            request=req,
            error_status_codes=["400", "4XX", "503", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.PingResponse)
        if utils.match_response(http_res, ["400", "4XX"], "application/problem+json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ErrorResponseErrorData
            )
            raise models.ErrorResponseError(data=response_data)
        if utils.match_response(http_res, ["503", "5XX"], "application/problem+json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ErrorResponseErrorData
            )
            raise models.ErrorResponseError(data=response_data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def ping_async(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PingResponse:
        r"""Checks API availability and version

        Check the API connection and the current API availability status. Also you will get the current API version number.

        As a successful result a `PingResponse` object will be returned.

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)
        req = self._build_request_async(
            method="GET",
            path="/ping",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=False,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="ping",
                oauth2_scopes=[],
                security_source=None,
            ),
            request=req,
            error_status_codes=["400", "4XX", "503", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.PingResponse)
        if utils.match_response(http_res, ["400", "4XX"], "application/problem+json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ErrorResponseErrorData
            )
            raise models.ErrorResponseError(data=response_data)
        if utils.match_response(http_res, ["503", "5XX"], "application/problem+json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ErrorResponseErrorData
            )
            raise models.ErrorResponseError(data=response_data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

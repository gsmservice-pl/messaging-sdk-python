"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from gsmservice_gateway import models, utils
from gsmservice_gateway._hooks import HookContext
from gsmservice_gateway.mms import Mms
from gsmservice_gateway.sms import Sms
from gsmservice_gateway.types import OptionalNullable, UNSET
from gsmservice_gateway.utils import get_security_from_env
from typing import Any, List, Optional


class Outgoing(BaseSDK):
    mms: Mms
    sms: Sms

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.mms = Mms(self.sdk_configuration)
        self.sms = Sms(self.sdk_configuration)

    def get_by_ids(
        self,
        *,
        ids: List[int],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.GetMessagesResponse:
        r"""Get the messages details and status by IDs

        Check the current status and details of one or more messages using their `ids`. You have to pass a `List[int]` as a `ids` named parameter containing unique message *IDs* which details you want to fetch. This method will accept maximum 50 identifiers in one call.

        As a successful result a `GetMessagesResponse` object will be returned containing `result` property of type `List[Message]` with `Message` objects, each object per single found message. `GetMessagesResponse` object will also contain `headers` property where you can find `X-Success-Count` (a count of messages which were found and returned correctly) and `X-Error-Count` (count of messages which were not found) elements.

        :param ids: List[str] with Message IDs assigned by the system. The system will accept a maximum of 50 identifiers in one call.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.GetMessagesRequest(
            ids=ids,
        )

        req = self.build_request(
            method="GET",
            path="/messages/{ids}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
                operation_id="getMessages",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.GetMessagesResponse(
                result=utils.unmarshal_json(http_res.text, List[models.Message]),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "4XX", "5XX"],
            "application/problem+json",
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseErrorData)
            raise models.ErrorResponseError(data=data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_by_ids_async(
        self,
        *,
        ids: List[int],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.GetMessagesResponse:
        r"""Get the messages details and status by IDs

        Check the current status and details of one or more messages using their `ids`. You have to pass a `List[int]` as a `ids` named parameter containing unique message *IDs* which details you want to fetch. This method will accept maximum 50 identifiers in one call.

        As a successful result a `GetMessagesResponse` object will be returned containing `result` property of type `List[Message]` with `Message` objects, each object per single found message. `GetMessagesResponse` object will also contain `headers` property where you can find `X-Success-Count` (a count of messages which were found and returned correctly) and `X-Error-Count` (count of messages which were not found) elements.

        :param ids: List[str] with Message IDs assigned by the system. The system will accept a maximum of 50 identifiers in one call.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.GetMessagesRequest(
            ids=ids,
        )

        req = self.build_request_async(
            method="GET",
            path="/messages/{ids}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
                operation_id="getMessages",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.GetMessagesResponse(
                result=utils.unmarshal_json(http_res.text, List[models.Message]),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "4XX", "5XX"],
            "application/problem+json",
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseErrorData)
            raise models.ErrorResponseError(data=data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def cancel_scheduled(
        self,
        *,
        ids: List[int],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.CancelMessagesResponse:
        r"""Cancel a scheduled messages

        Cancel messages using their `ids` which were scheduled to be sent at a specific time. You have to pass a `List[int]` as a `ids` named parameter containing the unique message IDs, which were returned after sending a message. This method will accept maximum 50 identifiers in one call. You can cancel only messages with *SCHEDULED* status.

        As a successful result a `CancelMessagesResponse` object will be returned, with `result` property of type `List[CancelledMessage]` containing `CancelledMessage` objects. The `status` property of each `CancelledMessage` object will contain a status code of operation - `204` if a particular message was cancelled successfully and other code if an error occured.

        `CancelMessagesResponse` object will also contain `headers` property where you can find `X-Success-Count` (a count of messages which were cancelled successfully), `X-Error-Count` (count of messages which were not cancelled) and `X-Sandbox` (if a request was made in Sandbox or Production system) elements.

        :param ids: List[str] with Message IDs assigned by the system. The system will accept a maximum of 50 identifiers in one call.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.CancelMessagesRequest(
            ids=ids,
        )

        req = self.build_request(
            method="DELETE",
            path="/messages/{ids}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
                operation_id="cancelMessages",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.CancelMessagesResponse(
                result=utils.unmarshal_json(
                    http_res.text, List[models.CancelledMessage]
                ),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "4XX", "5XX"],
            "application/problem+json",
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseErrorData)
            raise models.ErrorResponseError(data=data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def cancel_scheduled_async(
        self,
        *,
        ids: List[int],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.CancelMessagesResponse:
        r"""Cancel a scheduled messages

        Cancel messages using their `ids` which were scheduled to be sent at a specific time. You have to pass a `List[int]` as a `ids` named parameter containing the unique message IDs, which were returned after sending a message. This method will accept maximum 50 identifiers in one call. You can cancel only messages with *SCHEDULED* status.

        As a successful result a `CancelMessagesResponse` object will be returned, with `result` property of type `List[CancelledMessage]` containing `CancelledMessage` objects. The `status` property of each `CancelledMessage` object will contain a status code of operation - `204` if a particular message was cancelled successfully and other code if an error occured.

        `CancelMessagesResponse` object will also contain `headers` property where you can find `X-Success-Count` (a count of messages which were cancelled successfully), `X-Error-Count` (count of messages which were not cancelled) and `X-Sandbox` (if a request was made in Sandbox or Production system) elements.

        :param ids: List[str] with Message IDs assigned by the system. The system will accept a maximum of 50 identifiers in one call.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.CancelMessagesRequest(
            ids=ids,
        )

        req = self.build_request_async(
            method="DELETE",
            path="/messages/{ids}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
                operation_id="cancelMessages",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.CancelMessagesResponse(
                result=utils.unmarshal_json(
                    http_res.text, List[models.CancelledMessage]
                ),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "4XX", "5XX"],
            "application/problem+json",
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseErrorData)
            raise models.ErrorResponseError(data=data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def list(
        self,
        *,
        page: Optional[int] = 1,
        limit: Optional[int] = 10,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.ListMessagesResponse:
        r"""Lists the history of sent messages

        Get the details and current status of all of sent messages from your account message history. This method supports pagination so you have to pass a `page` (number of page with messages which you want to access) and a `limit` (max of messages per page) named parameters. Messages are fetched from the latest one. This method will accept maximum value of **50** as `limit` parameter value.

        As a successful result a `ListMessagesResponse` object will be returned containing `result` property of type `List[Message]` with a `Message` objects, each object per single message. `ListMessagesResponse` will also contain `headers` property where you can find `X-Total-Results` (a total count of all messages which are available in history on your account), `X-Total-Pages` (a total number of all pages with results), `X-Current-Page` (A current page number) and `X-Limit` (messages count per single page) elements.

        :param page: Page number of results
        :param limit: Number of results on one page
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.ListMessagesRequest(
            page=page,
            limit=limit,
        )

        req = self.build_request(
            method="GET",
            path="/messages",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
                operation_id="listMessages",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.ListMessagesResponse(
                result=utils.unmarshal_json(http_res.text, List[models.Message]),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "4XX", "5XX"],
            "application/problem+json",
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseErrorData)
            raise models.ErrorResponseError(data=data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def list_async(
        self,
        *,
        page: Optional[int] = 1,
        limit: Optional[int] = 10,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.ListMessagesResponse:
        r"""Lists the history of sent messages

        Get the details and current status of all of sent messages from your account message history. This method supports pagination so you have to pass a `page` (number of page with messages which you want to access) and a `limit` (max of messages per page) named parameters. Messages are fetched from the latest one. This method will accept maximum value of **50** as `limit` parameter value.

        As a successful result a `ListMessagesResponse` object will be returned containing `result` property of type `List[Message]` with a `Message` objects, each object per single message. `ListMessagesResponse` will also contain `headers` property where you can find `X-Total-Results` (a total count of all messages which are available in history on your account), `X-Total-Pages` (a total number of all pages with results), `X-Current-Page` (A current page number) and `X-Limit` (messages count per single page) elements.

        :param page: Page number of results
        :param limit: Number of results on one page
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.ListMessagesRequest(
            page=page,
            limit=limit,
        )

        req = self.build_request_async(
            method="GET",
            path="/messages",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
                operation_id="listMessages",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.ListMessagesResponse(
                result=utils.unmarshal_json(http_res.text, List[models.Message]),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(
            http_res,
            ["400", "401", "403", "404", "4XX", "5XX"],
            "application/problem+json",
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseErrorData)
            raise models.ErrorResponseError(data=data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .configs import (
    ConfigsResource,
    AsyncConfigsResource,
    ConfigsResourceWithRawResponse,
    AsyncConfigsResourceWithRawResponse,
    ConfigsResourceWithStreamingResponse,
    AsyncConfigsResourceWithStreamingResponse,
)
from .targets import (
    TargetsResource,
    AsyncTargetsResource,
    TargetsResourceWithRawResponse,
    AsyncTargetsResourceWithRawResponse,
    TargetsResourceWithStreamingResponse,
    AsyncTargetsResourceWithStreamingResponse,
)
from .policies import (
    PoliciesResource,
    AsyncPoliciesResource,
    PoliciesResourceWithRawResponse,
    AsyncPoliciesResourceWithRawResponse,
    PoliciesResourceWithStreamingResponse,
    AsyncPoliciesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["LogsUploaderResource", "AsyncLogsUploaderResource"]


class LogsUploaderResource(SyncAPIResource):
    @cached_property
    def policies(self) -> PoliciesResource:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return PoliciesResource(self._client)

    @cached_property
    def targets(self) -> TargetsResource:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return TargetsResource(self._client)

    @cached_property
    def configs(self) -> ConfigsResource:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return ConfigsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LogsUploaderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return LogsUploaderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsUploaderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return LogsUploaderResourceWithStreamingResponse(self)


class AsyncLogsUploaderResource(AsyncAPIResource):
    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return AsyncPoliciesResource(self._client)

    @cached_property
    def targets(self) -> AsyncTargetsResource:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return AsyncTargetsResource(self._client)

    @cached_property
    def configs(self) -> AsyncConfigsResource:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return AsyncConfigsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLogsUploaderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsUploaderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsUploaderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncLogsUploaderResourceWithStreamingResponse(self)


class LogsUploaderResourceWithRawResponse:
    def __init__(self, logs_uploader: LogsUploaderResource) -> None:
        self._logs_uploader = logs_uploader

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return PoliciesResourceWithRawResponse(self._logs_uploader.policies)

    @cached_property
    def targets(self) -> TargetsResourceWithRawResponse:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return TargetsResourceWithRawResponse(self._logs_uploader.targets)

    @cached_property
    def configs(self) -> ConfigsResourceWithRawResponse:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return ConfigsResourceWithRawResponse(self._logs_uploader.configs)


class AsyncLogsUploaderResourceWithRawResponse:
    def __init__(self, logs_uploader: AsyncLogsUploaderResource) -> None:
        self._logs_uploader = logs_uploader

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return AsyncPoliciesResourceWithRawResponse(self._logs_uploader.policies)

    @cached_property
    def targets(self) -> AsyncTargetsResourceWithRawResponse:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return AsyncTargetsResourceWithRawResponse(self._logs_uploader.targets)

    @cached_property
    def configs(self) -> AsyncConfigsResourceWithRawResponse:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return AsyncConfigsResourceWithRawResponse(self._logs_uploader.configs)


class LogsUploaderResourceWithStreamingResponse:
    def __init__(self, logs_uploader: LogsUploaderResource) -> None:
        self._logs_uploader = logs_uploader

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return PoliciesResourceWithStreamingResponse(self._logs_uploader.policies)

    @cached_property
    def targets(self) -> TargetsResourceWithStreamingResponse:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return TargetsResourceWithStreamingResponse(self._logs_uploader.targets)

    @cached_property
    def configs(self) -> ConfigsResourceWithStreamingResponse:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return ConfigsResourceWithStreamingResponse(self._logs_uploader.configs)


class AsyncLogsUploaderResourceWithStreamingResponse:
    def __init__(self, logs_uploader: AsyncLogsUploaderResource) -> None:
        self._logs_uploader = logs_uploader

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return AsyncPoliciesResourceWithStreamingResponse(self._logs_uploader.policies)

    @cached_property
    def targets(self) -> AsyncTargetsResourceWithStreamingResponse:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return AsyncTargetsResourceWithStreamingResponse(self._logs_uploader.targets)

    @cached_property
    def configs(self) -> AsyncConfigsResourceWithStreamingResponse:
        """Logs uploader allows you to upload logs with desired format to desired storages.

        Consists of three main parts:
        - **Policies** - rules that define which logs are uploaded and how they are uploaded.
        - **Targets** - destinations where logs are uploaded.
        - **Configs** - combinations of logs uploader policies, targets and resources to which they are applied.
        """
        return AsyncConfigsResourceWithStreamingResponse(self._logs_uploader.configs)

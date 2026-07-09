# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, cast
from datetime import datetime

from ..._types import Body, Omit, Query, Headers, omit
from ...types.cloud import secret_upload_tls_certificate_params
from ...types.cloud.secret import Secret

if TYPE_CHECKING:
    from ..._client import Gcore, AsyncGcore


class SecretsResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def upload_tls_certificate_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        payload: secret_upload_tls_certificate_params.Payload,
        expiration: Union[str, datetime, None] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Secret:
        response = self.upload_tls_certificate(
            project_id=project_id,
            region_id=region_id,
            name=name,
            payload=payload,
            expiration=expiration,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError("Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.secrets or len(task.created_resources.secrets) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            Secret,
            self.get(
                secret_id=task.created_resources.secrets[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )


class AsyncSecretsResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def upload_tls_certificate_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        payload: secret_upload_tls_certificate_params.Payload,
        expiration: Union[str, datetime, None] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Secret:
        response = await self.upload_tls_certificate(
            project_id=project_id,
            region_id=region_id,
            name=name,
            payload=payload,
            expiration=expiration,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError("Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.secrets or len(task.created_resources.secrets) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            Secret,
            await self.get(
                secret_id=task.created_resources.secrets[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )

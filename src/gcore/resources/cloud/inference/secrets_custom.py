# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any, cast

import httpx

from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, omit
from ...._utils import is_given
from ...._exceptions import APIError, NotFoundError

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore


def _polling_window(client: Any, interval: int | Omit, timeout: int | Omit) -> tuple[int, int]:
    if not is_given(interval):
        interval = cast(int, client.polling_interval_seconds)
    interval = max(1, interval)
    if not is_given(timeout):
        timeout = cast(int, client.polling_timeout_seconds)
    if timeout <= interval:
        raise ValueError(f"`polling_timeout_seconds` must be greater than `polling_interval_seconds` ({interval})")
    return interval, timeout


def _still_reported(secret_name: str, last_error: APIError | None) -> TimeoutError:
    message = f"Inference secret {secret_name} is still reported after delete"
    if last_error is not None:
        message += f" (last error: {last_error})"
    return TimeoutError(message)


class SecretsResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def delete_and_poll(
        self,
        secret_name: str,
        *,
        project_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete an inference secret and poll until the API stops reporting it.

        The DELETE creates no task and answers 204 while the secret is still reported for a few seconds.
        Polling stops on the first 404 and keeps going through other API errors, since the DELETE already
        succeeded; the last such error is attached when the polling timeout runs out.

        A 404 does not mean the API has finished: a secret created with the same name within a few seconds
        of it can still be removed by the earlier delete.
        """
        interval, polling_timeout = _polling_window(self._client, polling_interval_seconds, polling_timeout_seconds)
        self.delete(
            secret_name=secret_name,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        end_time = time.time() + polling_timeout
        last_error: APIError | None = None
        while True:
            try:
                self.get(secret_name=secret_name, project_id=project_id, extra_headers=extra_headers, timeout=timeout)
            except NotFoundError:
                return
            except APIError as err:
                last_error = err
            remaining = end_time - time.time()
            if remaining <= 0:
                raise _still_reported(secret_name, last_error)
            # Cut the last wait short so the final check lands on the deadline.
            self._sleep(min(interval, remaining))


class AsyncSecretsResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def delete_and_poll(
        self,
        secret_name: str,
        *,
        project_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete an inference secret and poll until the API stops reporting it.

        The DELETE creates no task and answers 204 while the secret is still reported for a few seconds.
        Polling stops on the first 404 and keeps going through other API errors, since the DELETE already
        succeeded; the last such error is attached when the polling timeout runs out.

        A 404 does not mean the API has finished: a secret created with the same name within a few seconds
        of it can still be removed by the earlier delete.
        """
        interval, polling_timeout = _polling_window(self._client, polling_interval_seconds, polling_timeout_seconds)
        await self.delete(
            secret_name=secret_name,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        end_time = time.time() + polling_timeout
        last_error: APIError | None = None
        while True:
            try:
                await self.get(
                    secret_name=secret_name, project_id=project_id, extra_headers=extra_headers, timeout=timeout
                )
            except NotFoundError:
                return
            except APIError as err:
                last_error = err
            remaining = end_time - time.time()
            if remaining <= 0:
                raise _still_reported(secret_name, last_error)
            # Cut the last wait short so the final check lands on the deadline.
            await self._sleep(min(interval, remaining))

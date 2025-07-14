# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncOffsetPage",
    "AsyncOffsetPage",
    "SyncOffsetPageIam",
    "AsyncOffsetPageIam",
    "SyncOffsetPageFastedgeApps",
    "AsyncOffsetPageFastedgeApps",
    "SyncOffsetPageFastedgeTemplates",
    "AsyncOffsetPageFastedgeTemplates",
    "SyncOffsetPageFastedgeAppLogs",
    "AsyncOffsetPageFastedgeAppLogs",
]

_T = TypeVar("_T")


class SyncOffsetPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        count = self.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        count = self.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageIam(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    result: List[_T]
    count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        result = self.result
        if not result:
            return []
        return result

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        count = self.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageIam(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    result: List[_T]
    count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        result = self.result
        if not result:
            return []
        return result

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        count = self.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageFastedgeApps(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    apps: List[_T]
    count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        apps = self.apps
        if not apps:
            return []
        return apps

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        count = self.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageFastedgeApps(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    apps: List[_T]
    count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        apps = self.apps
        if not apps:
            return []
        return apps

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        count = self.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageFastedgeTemplates(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    templates: List[_T]
    count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        templates = self.templates
        if not templates:
            return []
        return templates

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        count = self.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageFastedgeTemplates(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    templates: List[_T]
    count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        templates = self.templates
        if not templates:
            return []
        return templates

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        count = self.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageFastedgeAppLogs(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    logs: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        logs = self.logs
        if not logs:
            return []
        return logs

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageFastedgeAppLogs(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    logs: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        logs = self.logs
        if not logs:
            return []
        return logs

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None

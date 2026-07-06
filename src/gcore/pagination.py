# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast
from typing_extensions import override

from httpx import Response

from ._utils import is_mapping
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncOffsetPage",
    "AsyncOffsetPage",
    "SyncOffsetPageFastedgeApps",
    "AsyncOffsetPageFastedgeApps",
    "SyncOffsetPageFastedgeTemplates",
    "AsyncOffsetPageFastedgeTemplates",
    "SyncOffsetPageFastedgeAppLogs",
    "AsyncOffsetPageFastedgeAppLogs",
    "SyncPageStreamingAI",
    "AsyncPageStreamingAI",
    "SyncPageStreaming",
    "AsyncPageStreaming",
    "SyncOffsetPageCDN",
    "AsyncOffsetPageCDN",
    "OffsetPageCDNLogsMeta",
    "SyncOffsetPageCDNLogs",
    "AsyncOffsetPageCDNLogs",
    "SyncOffsetPageDNSZones",
    "AsyncOffsetPageDNSZones",
    "SyncOffsetPageDNSRrsets",
    "AsyncOffsetPageDNSRrsets",
    "SyncOffsetPageDNSNetworkMappings",
    "AsyncOffsetPageDNSNetworkMappings",
    "SyncOffsetPageFastedgeKvStores",
    "AsyncOffsetPageFastedgeKvStores",
]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)

_T = TypeVar("_T")


class SyncOffsetPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    count: int

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

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    count: int

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

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageFastedgeApps(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    apps: List[_T]
    count: int

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

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageFastedgeApps(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    apps: List[_T]
    count: int

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

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageFastedgeTemplates(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    templates: List[_T]
    count: int

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

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageFastedgeTemplates(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    templates: List[_T]
    count: int

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

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageFastedgeAppLogs(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    logs: List[_T]
    total_count: int

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

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageFastedgeAppLogs(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    logs: List[_T]
    total_count: int

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

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncPageStreamingAI(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class AsyncPageStreamingAI(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class SyncPageStreaming(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class AsyncPageStreaming(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class SyncOffsetPageCDN(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"offset": current_count})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class AsyncOffsetPageCDN(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"offset": current_count})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class OffsetPageCDNLogsMeta(BaseModel):
    count: Optional[int] = None


class SyncOffsetPageCDNLogs(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    meta: Optional[OffsetPageCDNLogsMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        count = None
        if self.meta is not None:
            if self.meta.count is not None:
                count = self.meta.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageCDNLogs(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    meta: Optional[OffsetPageCDNLogsMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        count = None
        if self.meta is not None:
            if self.meta.count is not None:
                count = self.meta.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageDNSZones(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    zones: List[_T]
    total_amount: int

    @override
    def _get_page_items(self) -> List[_T]:
        zones = self.zones
        if not zones:
            return []
        return zones

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_amount = self.total_amount

        if current_count < total_amount:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageDNSZones(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    zones: List[_T]
    total_amount: int

    @override
    def _get_page_items(self) -> List[_T]:
        zones = self.zones
        if not zones:
            return []
        return zones

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_amount = self.total_amount

        if current_count < total_amount:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageDNSRrsets(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    rrsets: List[_T]
    total_amount: int

    @override
    def _get_page_items(self) -> List[_T]:
        rrsets = self.rrsets
        if not rrsets:
            return []
        return rrsets

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_amount = self.total_amount

        if current_count < total_amount:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageDNSRrsets(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    rrsets: List[_T]
    total_amount: int

    @override
    def _get_page_items(self) -> List[_T]:
        rrsets = self.rrsets
        if not rrsets:
            return []
        return rrsets

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_amount = self.total_amount

        if current_count < total_amount:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageDNSNetworkMappings(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    network_mappings: List[_T]
    total_amount: int

    @override
    def _get_page_items(self) -> List[_T]:
        network_mappings = self.network_mappings
        if not network_mappings:
            return []
        return network_mappings

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_amount = self.total_amount

        if current_count < total_amount:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageDNSNetworkMappings(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    network_mappings: List[_T]
    total_amount: int

    @override
    def _get_page_items(self) -> List[_T]:
        network_mappings = self.network_mappings
        if not network_mappings:
            return []
        return network_mappings

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_amount = self.total_amount

        if current_count < total_amount:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageFastedgeKvStores(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    stores: List[_T]
    count: int

    @override
    def _get_page_items(self) -> List[_T]:
        stores = self.stores
        if not stores:
            return []
        return stores

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        count = self.count

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageFastedgeKvStores(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    stores: List[_T]
    count: int

    @override
    def _get_page_items(self) -> List[_T]:
        stores = self.stores
        if not stores:
            return []
        return stores

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        count = self.count

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None

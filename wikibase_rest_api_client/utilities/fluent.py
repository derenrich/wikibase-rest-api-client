import logging
import re
import typing
from dataclasses import dataclass
from functools import lru_cache
from typing import Any, List, Mapping, Optional, TypeVar, Union

from wikibase_rest_api_client import Client
from wikibase_rest_api_client.api.items import get_item
from wikibase_rest_api_client.api.labels import get_item_label, get_property_label
from wikibase_rest_api_client.models import Error
from wikibase_rest_api_client.models.value import Value
from wikibase_rest_api_client.types import Response

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class FluentProperty:
    pid: str
    label: Optional[str]
    datatype: str


@dataclass(frozen=True)
class FluentValue:
    value: Optional[str]
    qid: Optional[str] = None
    pid: Optional[str] = None


@dataclass(frozen=True)
class FluentWikibaseItem:
    qid: str
    label: Optional[str]
    description: Optional[str]
    aliases: Optional[List[str]]
    statements: Mapping[FluentProperty, List[FluentValue]]


WIKIDATA_TIME_REGEX = re.compile(r"^\+?(\d+)?-?(\d{1,2})-(\d{1,2})T\d{1,2}:\d{1,2}:\d{1,2}Z?$")

EMPTY_STRING_DICT: Mapping[str, Any] = {}

T = TypeVar("T")


class FluentWikibaseClient:
    lang: str
    _client: Client
    _supported_props: Optional[List[str]] = None

    def __init__(self, client: Client, *, lang="en", supported_props=None) -> None:
        self._client = client
        self.lang = lang
        self._supported_props = supported_props

    @staticmethod
    def _check_response(response: Response[Union[T, Error]]) -> Optional[T]:
        """Check if the response is valid."""

        if isinstance(response.parsed, Error):
            logging.warning(f"Error response when hitting Wikibase: {response.parsed}")
            return None
        else:
            return response.parsed

    @lru_cache(2048)
    def _get_property_label(self, pid: str) -> Optional[str]:
        label_response = get_property_label.sync_detailed(pid, self.lang, client=self._client)
        if label := self._check_response(label_response):
            return label
        else:
            return None

    @lru_cache(8192)
    def _get_item_label(self, qid: str) -> Optional[str]:
        label_response = get_item_label.sync_detailed(qid, self.lang, client=self._client)
        if label := self._check_response(label_response):
            return label
        else:
            return None

    # the content of the values are not well typed
    @typing.no_type_check
    def _value_to_string(self, value: Optional[Value], data_type: str) -> Optional[FluentValue]:
        if value:
            if data_type == "wikibase-item":
                if label := self._get_item_label(value.content):
                    return FluentValue(label, qid=value.content)
            elif data_type == "string":
                return FluentValue(value.content)
            elif data_type == "monolingualtext":
                return FluentValue(value.content["text"])
            elif data_type == "url":
                return FluentValue(value.content)
            elif data_type == "external-id":
                return FluentValue(value.content)
            elif data_type == "commonsMedia":
                return FluentValue(value.content)
            elif data_type == "wikibase-property":
                if label := self._get_property_label(value.content):
                    return FluentValue(label, pid=value.content)
            elif data_type == "quantity":
                return FluentValue(value.content["amount"])
            elif data_type == "time" and value.content:
                time_string = value.content["time"]
                precision = value.content["precision"]
                if match := WIKIDATA_TIME_REGEX.match(time_string):
                    y, m, d = match.groups()
                    if precision >= 11:
                        return FluentValue(f"{y}-{m}-{d}")
                    elif precision >= 10:
                        return FluentValue(f"{y}-{m}")
                    elif precision >= 9:
                        return FluentValue(f"{y}")
            elif data_type == "globe-coordinate":
                latitude = value.content["latitude"]
                longitude = value.content["longitude"]
                return FluentValue(f"{latitude}, {longitude}")
            elif data_type == "wikibase-lexeme":
                # explicitly not supported here
                return None
        return None

    def get_item(self, qid: str) -> Optional[FluentWikibaseItem]:
        item_response = get_item.sync_detailed(qid, client=self._client)
        if item := self._check_response(item_response):
            label = (item.labels or EMPTY_STRING_DICT).get(self.lang)
            description = (item.descriptions or EMPTY_STRING_DICT).get(self.lang)
            aliases = (item.aliases or EMPTY_STRING_DICT).get(self.lang)
            statements = dict()
            if item.statements:
                pids = self._supported_props or item.statements.additional_properties.keys()
                for pid in pids:
                    if pid not in item.statements:
                        continue
                    values = item.statements[pid]
                    if property_label := self._get_property_label(pid):
                        datatype: Optional[str] = None

                        fluent_values = []
                        for value in values:
                            if value.property_:
                                datatype = value.property_.data_type or None
                                value_string = self._value_to_string(value.value, value.property_.data_type)
                                if value_string:
                                    fluent_values.append(value_string)
                        if fluent_values and datatype:
                            fluent_property = FluentProperty(pid=pid, label=property_label, datatype=datatype)
                            statements[fluent_property] = fluent_values

            return FluentWikibaseItem(
                qid=qid,
                label=label,
                description=description,
                aliases=aliases,
                statements=statements,
            )
        return None

from enum import Enum


class GetItemFieldsItem(str, Enum):
    ALIASES = "aliases"
    DESCRIPTIONS = "descriptions"
    LABELS = "labels"
    SITELINKS = "sitelinks"
    STATEMENTS = "statements"
    TYPE = "type"

    def __str__(self) -> str:
        return str(self.value)

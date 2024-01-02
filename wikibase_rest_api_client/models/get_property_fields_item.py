from enum import Enum


class GetPropertyFieldsItem(str, Enum):
    ALIASES = "aliases"
    DATA_TYPE = "data-type"
    DESCRIPTIONS = "descriptions"
    LABELS = "labels"
    STATEMENTS = "statements"
    TYPE = "type"

    def __str__(self) -> str:
        return str(self.value)

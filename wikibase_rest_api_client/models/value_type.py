from enum import Enum


class ValueType(str, Enum):
    NOVALUE = "novalue"
    SOMEVALUE = "somevalue"
    VALUE = "value"

    def __str__(self) -> str:
        return str(self.value)

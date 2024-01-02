from enum import Enum


class StatementRank(str, Enum):
    DEPRECATED = "deprecated"
    NORMAL = "normal"
    PREFERRED = "preferred"

    def __str__(self) -> str:
        return str(self.value)

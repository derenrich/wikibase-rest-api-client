from enum import Enum


class PatchDocumentPatchItemOp(str, Enum):
    ADD = "add"
    COPY = "copy"
    MOVE = "move"
    REMOVE = "remove"
    REPLACE = "replace"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)

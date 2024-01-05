from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_document_patch_item_op import PatchDocumentPatchItemOp
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchDocumentPatchItem")


@_attrs_define
class PatchDocumentPatchItem:
    """
    Attributes:
        op (PatchDocumentPatchItemOp): The operation to perform Example: replace.
        path (str): A JSON Pointer for the property to manipulate
        value (Union[Unset, Any]): The value to be used within the operation
    """

    op: PatchDocumentPatchItemOp
    path: str
    value: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        op = self.op.value

        path = self.path

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "op": op,
                "path": path,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        op = PatchDocumentPatchItemOp(d.pop("op"))

        path = d.pop("path")

        value = d.pop("value", UNSET)

        patch_document_patch_item = cls(
            op=op,
            path=path,
            value=value,
        )

        patch_document_patch_item.additional_properties = d
        return patch_document_patch_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

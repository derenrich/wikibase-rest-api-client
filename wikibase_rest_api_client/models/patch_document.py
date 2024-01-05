from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_document_patch_item import PatchDocumentPatchItem


T = TypeVar("T", bound="PatchDocument")


@_attrs_define
class PatchDocument:
    """
    Attributes:
        patch (List['PatchDocumentPatchItem']): A JSON Patch document as defined by RFC 6902
    """

    patch: List["PatchDocumentPatchItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patch = []
        for patch_item_data in self.patch:
            patch_item = patch_item_data.to_dict()
            patch.append(patch_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "patch": patch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_document_patch_item import PatchDocumentPatchItem

        d = src_dict.copy()
        patch = []
        _patch = d.pop("patch")
        for patch_item_data in _patch:
            patch_item = PatchDocumentPatchItem.from_dict(patch_item_data)

            patch.append(patch_item)

        patch_document = cls(
            patch=patch,
        )

        patch_document.additional_properties = d
        return patch_document

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

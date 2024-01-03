from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from .value_type import ValueType

T = TypeVar("T", bound="Value")


@_attrs_define
class Value:
    """
    Attributes:
        content (Union[Unset, Any]): The value, if type == "value", otherwise omitted Example: I am a goat.
        type (Union[Unset, ValueType]): The value type
    """

    content: Union[Unset, Any] = UNSET
    type: Union[Unset, ValueType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ValueType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ValueType(_type)

        qualifier_value = cls(
            content=content,
            type=type,
        )

        qualifier_value.additional_properties = d
        return qualifier_value

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

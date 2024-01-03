from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from .property_info import PropertyInfo
    from .value import Value


T = TypeVar("T", bound="Qualifier")


@_attrs_define
class Qualifier:
    """
    Attributes:
        property_ (Union[Unset, PropertyInfo]):
        value (Union[Unset, Value]):
    """

    property_: Union[Unset, "PropertyInfo"] = UNSET
    value: Union[Unset, "Value"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.to_dict()

        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_ is not UNSET:
            field_dict["property"] = property_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from .property_info import PropertyInfo
        from .value import Value

        d = src_dict.copy()
        _property_ = d.pop("property", UNSET)
        property_: Union[Unset, PropertyInfo]
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = PropertyInfo.from_dict(_property_)

        _value = d.pop("value", UNSET)
        value: Union[Unset, Value]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = Value.from_dict(_value)

        qualifier = cls(
            property_=property_,
            value=value,
        )

        qualifier.additional_properties = d
        return qualifier

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

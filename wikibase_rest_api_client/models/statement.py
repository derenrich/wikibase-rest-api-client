from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.statement_rank import StatementRank
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualifier import Qualifier
    from ..models.reference import Reference
    from .property_info import PropertyInfo
    from .value import Value


T = TypeVar("T", bound="Statement")


@_attrs_define
class Statement:
    """
    Attributes:
        property_ (Union[Unset, PropertyInfo]):
        value (Union[Unset, Value]):
        id (Union[Unset, str]): The globally unique identifier for this Statement Example:
            Q11$6403c562-401a-2b26-85cc-8327801145e1.
        rank (Union[Unset, StatementRank]): The rank of the Statement Default: StatementRank.NORMAL.
        qualifiers (Union[Unset, List['Qualifier']]):
        references (Union[Unset, List['Reference']]):
    """

    property_: Union[Unset, "PropertyInfo"] = UNSET
    value: Union[Unset, "Value"] = UNSET
    id: Union[Unset, str] = UNSET
    rank: Union[Unset, StatementRank] = StatementRank.NORMAL
    qualifiers: Union[Unset, List["Qualifier"]] = UNSET
    references: Union[Unset, List["Reference"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.to_dict()

        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        id = self.id

        rank: Union[Unset, str] = UNSET
        if not isinstance(self.rank, Unset):
            rank = self.rank.value

        qualifiers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.qualifiers, Unset):
            qualifiers = []
            for qualifiers_item_data in self.qualifiers:
                qualifiers_item = qualifiers_item_data.to_dict()
                qualifiers.append(qualifiers_item)

        references: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_ is not UNSET:
            field_dict["property"] = property_
        if value is not UNSET:
            field_dict["value"] = value
        if id is not UNSET:
            field_dict["id"] = id
        if rank is not UNSET:
            field_dict["rank"] = rank
        if qualifiers is not UNSET:
            field_dict["qualifiers"] = qualifiers
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.qualifier import Qualifier
        from ..models.reference import Reference
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

        id = d.pop("id", UNSET)

        _rank = d.pop("rank", UNSET)
        rank: Union[Unset, StatementRank]
        if isinstance(_rank, Unset):
            rank = UNSET
        else:
            rank = StatementRank(_rank)

        qualifiers = []
        _qualifiers = d.pop("qualifiers", UNSET)
        for qualifiers_item_data in _qualifiers or []:
            qualifiers_item = Qualifier.from_dict(qualifiers_item_data)

            qualifiers.append(qualifiers_item)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = Reference.from_dict(references_item_data)

            references.append(references_item)

        statement = cls(
            property_=property_,
            value=value,
            id=id,
            rank=rank,
            qualifiers=qualifiers,
            references=references,
        )

        statement.additional_properties = d
        return statement

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

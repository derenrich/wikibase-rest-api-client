from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_aliases import PropertyAliases
    from ..models.property_descriptions import PropertyDescriptions
    from ..models.property_labels import PropertyLabels
    from ..models.property_statements import PropertyStatements


T = TypeVar("T", bound="Property")


@_attrs_define
class Property:
    """
    Attributes:
        id (Union[Unset, str]):  Example: P31.
        type (Union[Unset, str]):  Example: property.
        data_type (Union[Unset, str]):  Example: wikibase-item.
        labels (Union[Unset, PropertyLabels]):
        descriptions (Union[Unset, PropertyDescriptions]):
        aliases (Union[Unset, PropertyAliases]):
        statements (Union[Unset, PropertyStatements]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    data_type: Union[Unset, str] = UNSET
    labels: Union[Unset, "PropertyLabels"] = UNSET
    descriptions: Union[Unset, "PropertyDescriptions"] = UNSET
    aliases: Union[Unset, "PropertyAliases"] = UNSET
    statements: Union[Unset, "PropertyStatements"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        data_type = self.data_type

        labels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        descriptions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descriptions, Unset):
            descriptions = self.descriptions.to_dict()

        aliases: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases.to_dict()

        statements: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statements, Unset):
            statements = self.statements.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if data_type is not UNSET:
            field_dict["data-type"] = data_type
        if labels is not UNSET:
            field_dict["labels"] = labels
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if statements is not UNSET:
            field_dict["statements"] = statements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_aliases import PropertyAliases
        from ..models.property_descriptions import PropertyDescriptions
        from ..models.property_labels import PropertyLabels
        from ..models.property_statements import PropertyStatements

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        data_type = d.pop("data-type", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, PropertyLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = PropertyLabels.from_dict(_labels)

        _descriptions = d.pop("descriptions", UNSET)
        descriptions: Union[Unset, PropertyDescriptions]
        if isinstance(_descriptions, Unset):
            descriptions = UNSET
        else:
            descriptions = PropertyDescriptions.from_dict(_descriptions)

        _aliases = d.pop("aliases", UNSET)
        aliases: Union[Unset, PropertyAliases]
        if isinstance(_aliases, Unset):
            aliases = UNSET
        else:
            aliases = PropertyAliases.from_dict(_aliases)

        _statements = d.pop("statements", UNSET)
        statements: Union[Unset, PropertyStatements]
        if isinstance(_statements, Unset):
            statements = UNSET
        else:
            statements = PropertyStatements.from_dict(_statements)

        property_ = cls(
            id=id,
            type=type,
            data_type=data_type,
            labels=labels,
            descriptions=descriptions,
            aliases=aliases,
            statements=statements,
        )

        property_.additional_properties = d
        return property_

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

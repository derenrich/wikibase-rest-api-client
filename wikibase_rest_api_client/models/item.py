from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_aliases import ItemAliases
    from ..models.item_descriptions import ItemDescriptions
    from ..models.item_labels import ItemLabels
    from ..models.item_sitelinks import ItemSitelinks
    from ..models.item_statements import ItemStatements


T = TypeVar("T", bound="Item")


@_attrs_define
class Item:
    """
    Attributes:
        id (Union[Unset, str]):  Example: Q42.
        type (Union[Unset, str]):  Example: item.
        labels (Union[Unset, ItemLabels]):
        descriptions (Union[Unset, ItemDescriptions]):
        aliases (Union[Unset, ItemAliases]):
        sitelinks (Union[Unset, ItemSitelinks]):  Example: {'afwiki': {'title': 'Douglas Adams', 'badges':
            ['Q17437798'], 'url': 'https://af.wikipedia.org/wiki/Douglas_Adams'}, 'arwiki': {'title': 'دوغلاس آدمز',
            'badges': [], 'url':
            'https://ar.wikipedia.org/wiki/%D8%AF%D9%88%D8%BA%D9%84%D8%A7%D8%B3_%D8%A2%D8%AF%D9%85%D8%B2'}}.
        statements (Union[Unset, ItemStatements]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    labels: Union[Unset, "ItemLabels"] = UNSET
    descriptions: Union[Unset, "ItemDescriptions"] = UNSET
    aliases: Union[Unset, "ItemAliases"] = UNSET
    sitelinks: Union[Unset, "ItemSitelinks"] = UNSET
    statements: Union[Unset, "ItemStatements"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        labels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        descriptions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descriptions, Unset):
            descriptions = self.descriptions.to_dict()

        aliases: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases.to_dict()

        sitelinks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sitelinks, Unset):
            sitelinks = self.sitelinks.to_dict()

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
        if labels is not UNSET:
            field_dict["labels"] = labels
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if sitelinks is not UNSET:
            field_dict["sitelinks"] = sitelinks
        if statements is not UNSET:
            field_dict["statements"] = statements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_aliases import ItemAliases
        from ..models.item_descriptions import ItemDescriptions
        from ..models.item_labels import ItemLabels
        from ..models.item_sitelinks import ItemSitelinks
        from ..models.item_statements import ItemStatements

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, ItemLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ItemLabels.from_dict(_labels)

        _descriptions = d.pop("descriptions", UNSET)
        descriptions: Union[Unset, ItemDescriptions]
        if isinstance(_descriptions, Unset):
            descriptions = UNSET
        else:
            descriptions = ItemDescriptions.from_dict(_descriptions)

        _aliases = d.pop("aliases", UNSET)
        aliases: Union[Unset, ItemAliases]
        if isinstance(_aliases, Unset):
            aliases = UNSET
        else:
            aliases = ItemAliases.from_dict(_aliases)

        _sitelinks = d.pop("sitelinks", UNSET)
        sitelinks: Union[Unset, ItemSitelinks]
        if isinstance(_sitelinks, Unset):
            sitelinks = UNSET
        else:
            sitelinks = ItemSitelinks.from_dict(_sitelinks)

        _statements = d.pop("statements", UNSET)
        statements: Union[Unset, ItemStatements]
        if isinstance(_statements, Unset):
            statements = UNSET
        else:
            statements = ItemStatements.from_dict(_statements)

        item = cls(
            id=id,
            type=type,
            labels=labels,
            descriptions=descriptions,
            aliases=aliases,
            sitelinks=sitelinks,
            statements=statements,
        )

        item.additional_properties = d
        return item

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

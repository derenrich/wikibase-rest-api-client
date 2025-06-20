from typing import Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .search_match import SearchMatch
from .language_value import LanguageValue

T = TypeVar("T", bound="SearchItemResult")


@_attrs_define
class SearchItemResult:
    """A single search result item
    
    Attributes:
        id (str): The item ID (e.g., "Q123")
        display_label (LanguageValue): The display label for the item
        description (Optional[LanguageValue]): The description of the item
        match (SearchMatch): Information about what matched in the search
    """

    id: str
    display_label: LanguageValue
    match: SearchMatch
    description: Optional[LanguageValue] = None

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        display_label = self.display_label.to_dict()

        match = self.match.to_dict()

        description = self.description.to_dict() if self.description else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "display-label": display_label,
                "match": match,
            }
        )
        if description is not None:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from .search_match import SearchMatch
        from .language_value import LanguageValue

        d = src_dict.copy()
        id = d.pop("id")

        display_label = LanguageValue.from_dict(d.pop("display-label"))

        match = SearchMatch.from_dict(d.pop("match"))

        _description = d.pop("description", None)
        description: Optional[LanguageValue]
        if _description is None:
            description = None
        else:
            description = LanguageValue.from_dict(_description)

        search_item_result = cls(
            id=id,
            display_label=display_label,
            match=match,
            description=description,
        )

        search_item_result.additional_properties = d
        return search_item_result

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

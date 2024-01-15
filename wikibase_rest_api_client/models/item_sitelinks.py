from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from wikibase_rest_api_client.models.utils import GettableModel

if TYPE_CHECKING:
    from ..models.sitelink import Sitelink


T = TypeVar("T", bound="ItemSitelinks")


@_attrs_define
class ItemSitelinks(GettableModel):
    """
    Example:
        {'afwiki': {'title': 'Douglas Adams', 'badges': ['Q17437798'], 'url':
            'https://af.wikipedia.org/wiki/Douglas_Adams'}, 'arwiki': {'title': 'دوغلاس آدمز', 'badges': [], 'url':
            'https://ar.wikipedia.org/wiki/%D8%AF%D9%88%D8%BA%D9%84%D8%A7%D8%B3_%D8%A2%D8%AF%D9%85%D8%B2'}}

    """

    additional_properties: Dict[str, "Sitelink"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sitelink import Sitelink

        d = src_dict.copy()
        item_sitelinks = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = Sitelink.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        item_sitelinks.additional_properties = additional_properties
        return item_sitelinks

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "Sitelink":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "Sitelink") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Sitelink")


@_attrs_define
class Sitelink:
    """
    Attributes:
        title (Union[Unset, str]):
        badges (Union[Unset, List[str]]):
        url (Union[Unset, str]):
    """

    title: Union[Unset, str] = UNSET
    badges: Union[Unset, List[str]] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        badges: Union[Unset, List[str]] = UNSET
        if not isinstance(self.badges, Unset):
            badges = self.badges

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if badges is not UNSET:
            field_dict["badges"] = badges
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        badges = cast(List[str], d.pop("badges", UNSET))

        url = d.pop("url", UNSET)

        sitelink = cls(
            title=title,
            badges=badges,
            url=url,
        )

        sitelink.additional_properties = d
        return sitelink

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

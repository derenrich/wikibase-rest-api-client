from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AliasesAddRequest")


@_attrs_define
class AliasesAddRequest:
    """
    Attributes:
        aliases (List[str]): The label to be set for the entity.
        tags (Union[Unset, List[str]]):  Example: ['mobile edit', 'external tool edit'].
        bot (Union[Unset, bool]):  Default: False.
        comment (Union[Unset, str]):  Example: API edit fixing the modelling as discussed in ....
    """

    aliases: List[str]
    tags: Union[Unset, List[str]] = UNSET
    bot: Union[Unset, bool] = False
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        bot = self.bot

        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aliases": self.aliases,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if bot is not UNSET:
            field_dict["bot"] = bot
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        aliases = cast(List[str], d.pop("aliases"))

        tags = cast(List[str], d.pop("tags", UNSET))

        bot = d.pop("bot", UNSET)

        comment = d.pop("comment", UNSET)

        label_request = cls(
            aliases=aliases,
            tags=tags,
            bot=bot,
            comment=comment,
        )

        label_request.additional_properties = d
        return label_request

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

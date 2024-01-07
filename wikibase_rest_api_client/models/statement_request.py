from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.statement import Statement


T = TypeVar("T", bound="StatementRequest")


@_attrs_define
class StatementRequest:
    """
    Attributes:
        statement (Statement):
        tags (Union[Unset, List[str]]):  Example: ['mobile edit', 'external tool edit'].
        bot (Union[Unset, bool]):  Default: False.
        comment (Union[Unset, str]):  Example: API edit fixing the modelling as discussed in ....
    """

    statement: "Statement"
    tags: Union[Unset, List[str]] = UNSET
    bot: Union[Unset, bool] = False
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        statement = self.statement.to_dict()

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        bot = self.bot

        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statement": statement,
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
        from ..models.statement import Statement

        d = src_dict.copy()
        statement = Statement.from_dict(d.pop("statement"))

        tags = cast(List[str], d.pop("tags", UNSET))

        bot = d.pop("bot", UNSET)

        comment = d.pop("comment", UNSET)

        statement_request = cls(
            statement=statement,
            tags=tags,
            bot=bot,
            comment=comment,
        )

        statement_request.additional_properties = d
        return statement_request

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

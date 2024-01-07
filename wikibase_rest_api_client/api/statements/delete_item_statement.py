from typing import Any, Union

from ...client import AuthenticatedClient, Client
from ...models import MediawikiEdit
from ...types import UNSET, Response, Unset
from .delete_statement import asyncio_detailed as generic_asyncio_detailed
from .delete_statement import sync_detailed as generic_sync_detailed


def sync_detailed(
    item_id: str,
    statement_id: str,
    edit: Union[Unset, MediawikiEdit] = UNSET,
    *,
    client: Union[AuthenticatedClient, Client],
    if_unmodified_since: Union[Unset, str] = UNSET,
) -> Response[Any]:
    if not statement_id.startswith(item_id):
        raise ValueError("statement_id must match the passed item_id")
    return generic_sync_detailed(
        statement_id=statement_id,
        edit=edit,
        client=client,
        if_unmodified_since=if_unmodified_since,
    )


async def asyncio_detailed(
    item_id: str,
    statement_id: str,
    edit: Union[Unset, MediawikiEdit] = UNSET,
    *,
    client: Union[AuthenticatedClient, Client],
    if_unmodified_since: Union[Unset, str] = UNSET,
) -> Response[Any]:
    if not statement_id.startswith(item_id):
        raise ValueError("statement_id must match the passed item_id")
    return generic_asyncio_detailed(
        statement_id=statement_id,
        edit=edit,
        client=client,
        if_unmodified_since=if_unmodified_since,
    )

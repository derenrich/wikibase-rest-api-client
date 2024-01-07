from typing import Any, Union

from ...client import AuthenticatedClient, Client
from ...models import StatementRequest
from ...types import UNSET, Response, Unset
from .replace_statement import asyncio_detailed as generic_asyncio_detailed
from .replace_statement import sync_detailed as generic_sync_detailed


def sync_detailed(
    property_id: str,
    statement_id: str,
    statement_request: StatementRequest,
    *,
    client: Union[AuthenticatedClient, Client],
    if_unmodified_since: Union[Unset, str] = UNSET,
) -> Response[Any]:
    if not statement_id.startswith(property_id):
        raise ValueError("statement_id must match the passed property_id")

    return generic_sync_detailed(
        statement_id=statement_id,
        statement_request=statement_request,
        client=client,
        if_unmodified_since=if_unmodified_since,
    )


def assyncio_detailed(
    property_id: str,
    statement_id: str,
    statement_request: StatementRequest,
    *,
    client: Union[AuthenticatedClient, Client],
    if_unmodified_since: Union[Unset, str] = UNSET,
) -> Response[Any]:
    if not statement_id.startswith(property_id):
        raise ValueError("statement_id must match the passed property_id")

    return generic_asyncio_detailed(
        statement_id=statement_id,
        statement_request=statement_request,
        client=client,
        if_unmodified_since=if_unmodified_since,
    )

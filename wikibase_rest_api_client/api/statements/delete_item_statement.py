from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    statement_id: str,
    *,
    if_unmodified_since: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(if_unmodified_since, Unset):
        headers["If-Unmodified-Since"] = if_unmodified_since

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/entities/items/{item_id}/statements/{statement_id}".format(
            item_id=item_id,
            statement_id=statement_id,
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.PRECONDITION_FAILED:
        return None
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    statement_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    if_unmodified_since: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Delete a single Statement from an Item

     This endpoint is also accessible through `/statements/{statement_id}`

    Args:
        item_id (str):
        statement_id (str):
        if_unmodified_since (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        statement_id=statement_id,
        if_unmodified_since=if_unmodified_since,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    item_id: str,
    statement_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    if_unmodified_since: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Delete a single Statement from an Item

     This endpoint is also accessible through `/statements/{statement_id}`

    Args:
        item_id (str):
        statement_id (str):
        if_unmodified_since (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        statement_id=statement_id,
        if_unmodified_since=if_unmodified_since,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

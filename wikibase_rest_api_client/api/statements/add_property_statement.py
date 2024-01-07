from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import Statement, StatementRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    property_id: str,
    add_statement_request: StatementRequest,
    *,
    if_unmodified_since: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(if_unmodified_since, Unset):
        headers["If-Unmodified-Since"] = if_unmodified_since

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/entities/properties/{property_id}/statements".format(
            property_id=property_id,
        ),
        "json": add_statement_request.to_dict(),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.CREATED:
        return Statement.from_dict(response.json())
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
    property_id: str,
    add_statement_request: StatementRequest,
    *,
    client: Union[AuthenticatedClient, Client],
    if_unmodified_since: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Add a new Statement to a Property

    Args:
        property_id (str):
        add_statement_request (StatementRequest):
        if_unmodified_since (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        property_id=property_id,
        add_statement_request=add_statement_request,
        if_unmodified_since=if_unmodified_since,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    property_id: str,
    add_statement_request: StatementRequest,
    *,
    client: Union[AuthenticatedClient, Client],
    if_unmodified_since: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Add a new Statement to a Property

    Args:
        property_id (str):
        add_statement_request (StatementRequest):
        if_unmodified_since (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        property_id=property_id,
        add_statement_request=add_statement_request,
        if_unmodified_since=if_unmodified_since,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    language_code: str,
    *,
    if_modified_since: Union[Unset, str] = UNSET,
    if_unmodified_since: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(if_modified_since, Unset):
        headers["If-Modified-Since"] = if_modified_since

    if not isinstance(if_unmodified_since, Unset):
        headers["If-Unmodified-Since"] = if_unmodified_since

    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/entities/items/{item_id}/descriptions/{language_code}".format(
            item_id=item_id,
            language_code=language_code,
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[List[str], Error]]:
    if response.status_code == HTTPStatus.OK:
        return response.json()
    if response.status_code == HTTPStatus.NOT_MODIFIED:
        return None
    if response.status_code == HTTPStatus.PERMANENT_REDIRECT:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return Error.from_dict(response.json())
    if response.status_code == HTTPStatus.NOT_FOUND:
        return Error.from_dict(response.json())
    if response.status_code == HTTPStatus.PRECONDITION_FAILED:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return Error.from_dict(response.json())
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[List[str], Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    language_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    if_modified_since: Union[Unset, str] = UNSET,
    if_unmodified_since: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[List[str], Error]]:
    """Retrieve an Item's description in a specific language

    Args:
        item_id (str):
        language_code (str):
        if_modified_since (Union[Unset, str]):
        if_unmodified_since (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        language_code=language_code,
        if_modified_since=if_modified_since,
        if_unmodified_since=if_unmodified_since,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    item_id: str,
    language_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    if_modified_since: Union[Unset, str] = UNSET,
    if_unmodified_since: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[List[str], Error]]:
    """Retrieve an Item's description in a specific language

    Args:
        item_id (str):
        language_code (str):
        if_modified_since (Union[Unset, str]):
        if_unmodified_since (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        language_code=language_code,
        if_modified_since=if_modified_since,
        if_unmodified_since=if_unmodified_since,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

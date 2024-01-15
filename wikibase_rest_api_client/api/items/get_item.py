from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import Error
from ...models.get_item_fields_item import GetItemFieldsItem
from ...models.item import Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    *,
    field_fields: Union[Unset, List[GetItemFieldsItem]] = UNSET,
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

    params: Dict[str, Any] = {}

    json_field_fields: Union[Unset, List[str]] = UNSET
    if not isinstance(field_fields, Unset):
        json_field_fields = []
        for field_fields_item_data in field_fields:
            field_fields_item = field_fields_item_data.value
            json_field_fields.append(field_fields_item)

    params["_fields"] = json_field_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/entities/items/{item_id}".format(
            item_id=item_id,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Item, Error]]:
    if response.status_code == HTTPStatus.OK:
        return Item.from_dict(response.json())
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
) -> Response[Union[Item, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    field_fields: Union[Unset, List[GetItemFieldsItem]] = UNSET,
    if_modified_since: Union[Unset, str] = UNSET,
    if_unmodified_since: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Item, Error]]:
    """Retrieve a single Wikibase Item by ID

    Args:
        item_id (str):
        field_fields (Union[Unset, List[GetItemFieldsItem]]):
        if_modified_since (Union[Unset, str]):
        if_unmodified_since (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Item, Error]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        field_fields=field_fields,
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
    *,
    client: Union[AuthenticatedClient, Client],
    field_fields: Union[Unset, List[GetItemFieldsItem]] = UNSET,
    if_modified_since: Union[Unset, str] = UNSET,
    if_unmodified_since: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Item, Error]]:
    """Retrieve a single Wikibase Item by ID

    Args:
        item_id (str):
        field_fields (Union[Unset, List[GetItemFieldsItem]]):
        if_modified_since (Union[Unset, str]):
        if_unmodified_since (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Item, Error]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        field_fields=field_fields,
        if_modified_since=if_modified_since,
        if_unmodified_since=if_unmodified_since,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

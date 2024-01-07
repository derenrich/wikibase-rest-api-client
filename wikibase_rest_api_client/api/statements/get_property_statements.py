from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import Error, PropertyStatements
from ...types import UNSET, Response, Unset


def _get_kwargs(
    property_id: str,
    *,
    property_: Union[Unset, str] = UNSET,
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

    params["property"] = property_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/entities/properties/{property_id}/statements".format(
            property_id=property_id,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return PropertyStatements.from_dict(response.json())
    if response.status_code == HTTPStatus.NOT_MODIFIED:
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    property_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    property_: Union[Unset, str] = UNSET,
    if_modified_since: Union[Unset, str] = UNSET,
    if_unmodified_since: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Retrieve Statements from a Property

    Args:
        property_id (str):
        property_ (Union[Unset, str]):
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
        property_id=property_id,
        property_=property_,
        if_modified_since=if_modified_since,
        if_unmodified_since=if_unmodified_since,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    property_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    property_: Union[Unset, str] = UNSET,
    if_modified_since: Union[Unset, str] = UNSET,
    if_unmodified_since: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Retrieve Statements from a Property

    Args:
        property_id (str):
        property_ (Union[Unset, str]):
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
        property_id=property_id,
        property_=property_,
        if_modified_since=if_modified_since,
        if_unmodified_since=if_unmodified_since,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

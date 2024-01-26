from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import LabelReplaceRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    language_code: str,
    replace_request: Union[LabelReplaceRequest, str],
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

    if not isinstance(replace_request, LabelReplaceRequest):
        replace_request = LabelReplaceRequest(label=replace_request)

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/entities/items/{item_id}/labels/{language_code}".format(
            item_id=item_id,
            language_code=language_code,
        ),
        "json": replace_request.to_dict(),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.CREATED:
        return None
    if response.status_code == HTTPStatus.NOT_MODIFIED:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.CONFLICT:
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
    language_code: str,
    replace_request: LabelReplaceRequest,
    *,
    client: Union[AuthenticatedClient, Client],
    if_modified_since: Union[Unset, str] = UNSET,
    if_unmodified_since: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Add / Replace an Item's label in a specific language

    Args:
        item_id (str):
        language_code (str):
        replace_request (Union[LabelReplaceRequest, str]):
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
        replace_request=replace_request,
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
    replace_request: LabelReplaceRequest,
    *,
    client: Union[AuthenticatedClient, Client],
    if_modified_since: Union[Unset, str] = UNSET,
    if_unmodified_since: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Add / Replace an Item's label in a specific language

    Args:
        item_id (str):
        language_code (str):
        replace_request (Union[LabelReplaceRequest, str]):
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
        replace_request=replace_request,
        if_modified_since=if_modified_since,
        if_unmodified_since=if_unmodified_since,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

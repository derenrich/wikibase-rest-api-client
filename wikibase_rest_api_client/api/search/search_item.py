from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx
import urllib.parse

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import Error
from ...models.search_item_results import SearchItemResults
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    language: str,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 0,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    
    params["q"] = q
    params["language"] = language
    
    if not isinstance(limit, Unset):
        params["limit"] = limit
        
    if not isinstance(offset, Unset):
        params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/search/items",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[SearchItemResults, Error]]:
    if response.status_code == HTTPStatus.OK:
        return SearchItemResults.from_dict(response.json())
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return Error.from_dict(response.json())
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[SearchItemResults, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,
    language: str,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 0,
) -> Response[Union[SearchItemResults, Error]]:
    """Simple Item search by label and aliases

    Args:
        q (str): The term to search labels by
        language (str): The language to search labels in (pattern: ^[a-z]{2}[a-z0-9-]*$)
        limit (Union[Unset, int]): The maximum number of results to return (1-500, default: 10)
        offset (Union[Unset, int]): The index to start showing results from (min: 0, default: 0)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SearchItemResults, Error]]
    """

    kwargs = _get_kwargs(
        q=q,
        language=language,
        limit=limit,
        offset=offset,
    )


    # for now this only works on v0 endpoints
    base_url = str(client.get_httpx_client().base_url)
    if "/v1/" in base_url:
        base_url = base_url.replace("/v1/", "/v0/")
        kwargs['url'] = urllib.parse.urljoin(base_url, "." + kwargs['url'])

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,
    language: str,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 0,
) -> Response[Union[SearchItemResults, Error]]:
    """Simple Item search by label and aliases

    Args:
        q (str): The term to search labels by
        language (str): The language to search labels in (pattern: ^[a-z]{2}[a-z0-9-]*$)
        limit (Union[Unset, int]): The maximum number of results to return (1-500, default: 10)
        offset (Union[Unset, int]): The index to start showing results from (min: 0, default: 0)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SearchItemResults, Error]]
    """

    kwargs = _get_kwargs(
        q=q,
        language=language,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,
    language: str,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[SearchItemResults, Error]]:
    """Simple Item search by label and aliases

    Args:
        q (str): The term to search labels by
        language (str): The language to search labels in (pattern: ^[a-z]{2}[a-z0-9-]*$)
        limit (Union[Unset, int]): The maximum number of results to return (1-500, default: 10)
        offset (Union[Unset, int]): The index to start showing results from (min: 0, default: 0)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SearchItemResults, Error]
    """
    return sync_detailed(
        client=client,
        q=q,
        language=language,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,
    language: str,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[SearchItemResults, Error]]:
    """Simple Item search by label and aliases

    Args:
        q (str): The term to search labels by
        language (str): The language to search labels in (pattern: ^[a-z]{2}[a-z0-9-]*$)
        limit (Union[Unset, int]): The maximum number of results to return (1-500, default: 10)
        offset (Union[Unset, int]): The index to start showing results from (min: 0, default: 0)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SearchItemResults, Error]
    """
    return (
        await asyncio_detailed(
            client=client,
            q=q,
            language=language,
            limit=limit,
            offset=offset,
        )
    ).parsed

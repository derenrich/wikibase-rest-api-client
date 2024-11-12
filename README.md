# wikibase-rest-api-client
A client library for accessing Wikibase REST API. See [the swagger UI](https://doc.wikimedia.org/Wikibase/master/js/rest-api/) for details of the API. Docs for the REST API can be found at [doc.wikimedia.org](https://doc.wikimedia.org/Wikibase/master/php/repo_rest-api_README.html#autotoc_md670).


## Installation
[![PyPI version](https://badge.fury.io/py/wikibase-rest-api-client.svg)](https://badge.fury.io/py/wikibase-rest-api-client)

    sudo pip3 install wikibase-rest-api-client

## Usage
See the tests for detailed examples of usage. For basic usage read on.

First, create a client:

```python
from wikibase_rest_api_client import Client

# by default will connect to Wikidata at https://www.wikidata.org/w/rest.php/wikibase/v0/
client = Client()
# specify some other url to connect to
other_client = Client(base_url="https://api.example.com")
```

You probably should specify a User-Agent when constructing the client

```python
from wikibase_rest_api_client import Client
client = Client(headers={"User-Agent": "my-agent/1.0.0"})

```

And you probably want to also have the client follow redirects (which will follow redirects between items when reading data)


```python
from wikibase_rest_api_client import Client
client = Client(headers={"User-Agent": "my-agent/1.0.0"}, follow_redirects=True)

```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead. See [the OAuth docs](https://www.wikidata.org/wiki/Wikidata:REST_API/Authentication#Setting_up_OAuth_2.0) for how to get a token.

```python
from wikibase_rest_api_client import AuthenticatedClient

client = AuthenticatedClient(token="SuperSecretToken")
```

Now call your endpoint and use your models:

```python
from wikibase_rest_api_client.models import Item
from wikibase_rest_api_client.api.items import get_item
from wikibase_rest_api_client.types import Response

with client as client:
    # it's detailed because it responds with need more info than just the Item (e.g. status_code / headers)
    response: Response[Item] = get_item.sync_detailed('Q5', client=client)
```

Or do the same thing with an async version:

```python
from wikibase_rest_api_client.models import Item
from wikibase_rest_api_client.api.items import get_item
from wikibase_rest_api_client.types import Response

async with client as client:
    response: Response[Item] = await get_item.asyncio_detailed('Q5', client=client)
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken", 
    verify_ssl=False
)
```


## Fluent usage

The library also offers a "fluent" API that is useful for many common operations. To use it you will first need to create a client as above.

```python
from wikibase_rest_api_client.utilities.fluent import FluentWikibaseClient
from wikibase_rest_api_client import Client

inner_client = Client()
# defaults to English values
c = FluentWikibaseClient(inner_client)
item = c.get_item("Q5")
assert item.label == "human"
description = item.description
aliases = item.aliases

# see source for the format of item.statements
```

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from wikibase_rest_api_client import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://api.example.com",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from wikibase_rest_api_client import Client

client = Client(
    base_url="https://api.example.com",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://api.example.com", proxies="http://localhost:8030"))
```

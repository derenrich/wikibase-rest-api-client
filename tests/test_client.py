from wikibase_rest_api_client import Client
from wikibase_rest_api_client.models import Item
from wikibase_rest_api_client.api.items import get_item
from wikibase_rest_api_client.types import Response


def test_foo():
    client = Client()
    with client as client:
        response: Response[Item] = get_item.sync_detailed('Q5', client=client)
        assert response.status_code == 200
        assert response.parsed is not None

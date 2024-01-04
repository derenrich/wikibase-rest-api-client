import pytest

from wikibase_rest_api_client import Client
from wikibase_rest_api_client.api.items import get_item
from wikibase_rest_api_client.api.labels import delete_item_label
from wikibase_rest_api_client.api.properties import get_property
from wikibase_rest_api_client.types import Response

TEST_ITEM = "Q233445"
TEST_STRING_PROP = "P95180"
PROPS = [TEST_STRING_PROP]


@pytest.fixture
def client():
    client = Client(
        "https://test.wikidata.org/w/rest.php/wikibase/v0/", headers={"User-Agent": "wikibase-rest-api-client/1.0.0"}
    )
    return client


# just confirm the item we are going to test with still exists
def test_get_test_item(client):
    with client as client:
        response = get_item.sync_detailed(TEST_ITEM, client=client)
        assert type(response) == Response
        assert response.status_code == 200


# just confirm the item we are going to test with still exists


def test_get_test_props(client):
    for prop in PROPS:
        with client as client:
            response = get_property.sync_detailed(prop, client=client)
            assert type(response) == Response
            assert response.status_code == 200


def test_delete_item_label(client):
    with client as client:
        # Delete the label
        response = delete_item_label.sync_detailed(TEST_ITEM, "en", client=client)

        # Check the response
        assert type(response) == Response
        assert response.status_code == 200
        assert response.content == b"Label deleted"

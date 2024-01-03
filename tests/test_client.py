from typing import Any

from wikibase_rest_api_client import Client
from wikibase_rest_api_client.api.labels import get_item_label, get_property_label
from wikibase_rest_api_client.api.descriptions import get_item_description, get_property_description

from wikibase_rest_api_client.api.items import get_item
from wikibase_rest_api_client.api.properties import get_property
from wikibase_rest_api_client.models import Item, Property
from wikibase_rest_api_client.types import Response


def test_get_item():
    client = Client(headers={"User-Agent": "wikibase-rest-api-client/1.0.0"})
    with client as client:
        response: Response[Any] = get_item.sync_detailed("Q5", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert type(response.parsed) == Item
        parsed = response.parsed

        assert len(parsed.statements.additional_properties) > 0
        assert "P31" in parsed.statements
        assert parsed.statements["P31"][0].value.type == "value"
        assert parsed.statements["P31"][0].value.content == "Q55983715"

        assert parsed.labels["en"] == "human"
        assert len(parsed.aliases["en"]) > 1
        assert parsed.descriptions is not None


def test_get_property():
    client = Client(headers={"User-Agent": "wikibase-rest-api-client/1.0.0"})
    with client as client:
        response: Response[Any] = get_property.sync_detailed("P31", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert type(response.parsed) == Property
        parsed = response.parsed
        assert len(parsed.statements.additional_properties) > 0
        assert "P31" in parsed.statements
        assert parsed.statements["P31"][0].value.type == "value"

        assert parsed.labels["en"] == "instance of"
        assert len(parsed.aliases["en"]) > 1
        assert parsed.descriptions is not None


def test_get_property_label():
    client = Client(headers={"User-Agent": "wikibase-rest-api-client/1.0.0"})
    with client as client:
        response: Response[Any] = get_property_label.sync_detailed("P31", "en", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert type(response.parsed) == str
        parsed = response.parsed
        assert parsed == "instance of"


def test_get_item_label():
    client = Client(headers={"User-Agent": "wikibase-rest-api-client/1.0.0"})
    with client as client:
        response: Response[Any] = get_item_label.sync_detailed("Q5", "en", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert type(response.parsed) == str
        parsed = response.parsed
        assert parsed == "human"


def test_get_item_description():
    client = Client(headers={"User-Agent": "wikibase-rest-api-client/1.0.0"})
    with client as client:
        response: Response[Any] = get_item_description.sync_detailed("Q5", "en", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert type(response.parsed) == str
        parsed = response.parsed
        assert "Homo sapiens" in parsed


def test_get_property_description():
    client = Client(headers={"User-Agent": "wikibase-rest-api-client/1.0.0"})
    with client as client:
        response: Response[Any] = get_property_description.sync_detailed("P31", "en", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert type(response.parsed) == str
        parsed = response.parsed
        assert "class" in parsed

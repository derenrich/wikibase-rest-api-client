from typing import Any

from wikibase_rest_api_client import Client
from wikibase_rest_api_client.api.aliases import (
    get_item_aliases,
    get_item_aliases_in_language,
    get_property_aliases,
    get_property_aliases_in_language,
)
from wikibase_rest_api_client.api.descriptions import (
    get_item_description,
    get_item_descriptions,
    get_property_description,
    get_property_descriptions,
)
from wikibase_rest_api_client.api.items import get_item
from wikibase_rest_api_client.api.labels import get_item_label, get_item_labels, get_property_label, get_property_labels
from wikibase_rest_api_client.api.properties import get_property
from wikibase_rest_api_client.api.statements import (
    get_item_statement,
    get_item_statements,
    get_property_statement,
    get_property_statements,
    get_statement,
)
from wikibase_rest_api_client.models import Error, Item, Property
from wikibase_rest_api_client.models.statement_rank import StatementRank
from wikibase_rest_api_client.types import Response


def test_get_item(client):
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


def test_get_item_error(client):
    with client as client:
        response: Response[Any] = get_item.sync_detailed("Q-1", client=client)
        assert response.status_code == 400
        assert type(response.parsed) == Error

        # Q123456789 was famously deleted
        response: Response[Any] = get_item.sync_detailed("Q123456789", client=client)
        assert response.status_code == 404
        assert type(response.parsed) == Error


def test_get_property(client):
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


def test_get_property_error(client):
    with client as client:
        response: Response[Any] = get_property.sync_detailed("P-1", client=client)
        assert response.status_code == 400
        assert type(response.parsed) == Error

        response: Response[Any] = get_property.sync_detailed("P1", client=client)
        assert response.status_code == 404
        assert type(response.parsed) == Error


def test_get_property_label(client):
    with client as client:
        response: Response[Any] = get_property_label.sync_detailed("P31", "en", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert type(response.parsed) == str
        parsed = response.parsed
        assert parsed == "instance of"


def test_get_item_label(client):
    with client as client:
        response: Response[Any] = get_item_label.sync_detailed("Q5", "en", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert type(response.parsed) == str
        parsed = response.parsed
        assert parsed == "human"


def test_get_item_labels(client):
    with client as client:
        response: Response[Any] = get_item_labels.sync_detailed("Q5", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert "en" in response.parsed
        assert "fr" in response.parsed
        response.parsed["en"] == "human"


def test_get_property_labels(client):
    with client as client:
        response: Response[Any] = get_property_labels.sync_detailed("P31", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert "en" in response.parsed
        assert "fr" in response.parsed
        response.parsed["en"] == "instance of"


def test_get_item_description(client):
    with client as client:
        response: Response[Any] = get_item_description.sync_detailed("Q5", "en", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert type(response.parsed) == str
        parsed = response.parsed
        assert "Homo sapiens" in parsed


def test_get_item_descriptions(client):
    with client as client:
        response: Response[Any] = get_item_descriptions.sync_detailed("Q5", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        parsed = response.parsed
        assert "Homo sapiens" in parsed["en"]
        assert "Homo sapiens" in parsed["fr"]


def test_get_property_description(client):
    with client as client:
        response: Response[Any] = get_property_description.sync_detailed("P31", "en", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert type(response.parsed) == str
        parsed = response.parsed
        assert "class" in parsed


def test_get_property_descriptions(client):
    with client as client:
        response: Response[Any] = get_property_descriptions.sync_detailed("P31", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        parsed = response.parsed
        assert "class" in parsed["en"]
        assert "classe" in parsed["fr"]


def test_get_item_aliases_in_language(client):
    with client as client:
        response: Response[Any] = get_item_aliases_in_language.sync_detailed("Q5", "en", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert type(response.parsed) == list
        parsed = response.parsed
        assert len(parsed) > 0
        assert all(isinstance(alias, str) for alias in parsed)


def test_get_item_aliases_in_language_error(client):
    with client as client:
        response: Response[Any] = get_item_aliases_in_language.sync_detailed("Q5", "zzt", client=client)
        assert type(response) == Response
        assert response.status_code == 400
        assert response.parsed is not None
        assert type(response.parsed) == Error

        response: Response[Any] = get_item_aliases_in_language.sync_detailed("Q123456789", "en", client=client)
        assert type(response) == Response
        assert response.status_code == 404
        assert response.parsed is not None
        assert type(response.parsed) == Error


def test_get_item_aliases(client):
    with client as client:
        response: Response[Any] = get_item_aliases.sync_detailed("Q5", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        parsed = response.parsed
        assert type(parsed["en"]) == list
        assert len(parsed.to_dict()) > 0
        assert len(parsed["en"]) > 0
        assert all(isinstance(alias, str) for alias in parsed["en"])


def test_get_property_aliases_in_language(client):
    with client as client:
        response: Response[Any] = get_property_aliases_in_language.sync_detailed("P31", "en", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        assert type(response.parsed) == list
        parsed = response.parsed
        assert len(parsed) > 0
        assert all(isinstance(alias, str) for alias in parsed)


def test_get_property_aliases(client):
    with client as client:
        response: Response[Any] = get_property_aliases.sync_detailed("P31", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        parsed = response.parsed
        assert type(parsed["en"]) == list
        assert len(parsed["en"]) > 0
        assert all(isinstance(alias, str) for alias in parsed["en"])


def test_get_statement(client):
    with client as client:
        response: Response[Any] = get_statement.sync_detailed("Q5$82b80d5f-4353-c7cb-1a3c-c0c8f4f5f237", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        parsed = response.parsed
        assert parsed.id == "Q5$82b80d5f-4353-c7cb-1a3c-c0c8f4f5f237"
        assert parsed.rank == StatementRank.NORMAL
        assert parsed.property_.id == "P31"


def test_get_statement_error(client):
    with client as client:
        response: Response[Any] = get_statement.sync_detailed("Q1$82b80d5f-4353-c7cb-1a3c-c0c8f4f5f237", client=client)
        assert type(response) == Response
        assert response.status_code == 404
        assert response.parsed is not None
        assert type(response.parsed) == Error


def test_get_item_statement(client):
    with client as client:
        response: Response[Any] = get_item_statement.sync_detailed(
            "Q5", "Q5$82b80d5f-4353-c7cb-1a3c-c0c8f4f5f237", client=client
        )
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        parsed = response.parsed
        assert parsed.id == "Q5$82b80d5f-4353-c7cb-1a3c-c0c8f4f5f237"
        assert parsed.rank == StatementRank.NORMAL
        assert parsed.property_.id == "P31"


def test_get_property_statement(client):
    with client as client:
        response: Response[Any] = get_property_statement.sync_detailed(
            "P31", "P31$9d042001-4a7e-2432-a7e1-233360062379", client=client
        )
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        parsed = response.parsed
        assert parsed.id == "P31$9d042001-4a7e-2432-a7e1-233360062379"
        assert parsed.rank == StatementRank.NORMAL
        assert parsed.property_.id == "P31"


def test_get_item_statements(client):
    with client as client:
        response: Response[Any] = get_item_statements.sync_detailed("Q5", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        parsed = response.parsed
        assert "P31" in parsed
        assert len(parsed["P31"]) > 0


def test_get_item_statements_redirect(client):
    with client as client:
        response: Response[Any] = get_item_statements.sync_detailed("Q121879077", client=client)
        assert type(response) == Response
        assert response.status_code == 308
        assert response.parsed is None
        # location field should tell us where to request next
        assert "location" in response.headers.keys()

    follow_redirect_client = Client(headers={"User-Agent": "wikibase-rest-api-client/1.0.0"}, follow_redirects=True)
    with follow_redirect_client as client:
        response: Response[Any] = get_item_statements.sync_detailed("Q121879077", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        parsed = response.parsed
        assert "P31" in parsed
        assert len(parsed["P31"]) > 0


def test_get_property_statements(client):
    with client as client:
        response: Response[Any] = get_property_statements.sync_detailed("P31", client=client)
        assert type(response) == Response
        assert response.status_code == 200
        assert response.parsed is not None
        parsed = response.parsed
        assert "P31" in parsed
        assert len(parsed["P31"]) > 0

import pytest

from wikibase_rest_api_client import Client
from wikibase_rest_api_client.utilities.fluent import FluentWikibaseClient


@pytest.fixture(scope="module")
def fluent_client():
    client = Client(httpx_args={"timeout": 200}, headers={"User-Agent": "wikibase-rest-api-client/1.0.0"})
    return FluentWikibaseClient(client)


def test_basic_fluent(fluent_client):
    fluent_item = fluent_client.get_item("Q5")
    assert fluent_item.qid == "Q5"
    assert fluent_item.label == "human"
    assert "human being" in fluent_item.aliases
    assert "instance of" in [p.label for p in fluent_item.statements.keys()]


def test_human_fluent(fluent_client):
    fluent_item = fluent_client.get_item("Q23")
    assert fluent_item.qid == "Q23"
    assert fluent_item.label == "George Washington"

    # did we format the date correctly?
    assert (
        "1732-02-22"
        in [d for (p, d) in fluent_item.statements.items() if p.label == "date of birth" and p.datatype == "time"][0]
    )


def test_lake_fluent(fluent_client):
    fluent_item = fluent_client.get_item("Q1066")
    assert fluent_item.qid == "Q1066"
    assert fluent_item.label == "Lake Superior"

    assert (
        len(
            [
                d
                for (p, d) in fluent_item.statements.items()
                if p.label == "coordinate location" and p.datatype == "globe-coordinate"
            ][0]
        )
        > 0
    )


def test_only_interesting_fluent(fluent_client):
    fluent_item = fluent_client.get_item("Q1066")
    fluent_item.statements.keys() == ["P31", "P17"]


def test_error_fluent(fluent_client):
    fluent_item = fluent_client.get_item("Q123456789")
    assert fluent_item is None

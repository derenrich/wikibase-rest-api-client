import pytest

from wikibase_rest_api_client import Client
from wikibase_rest_api_client.utilities.fluent import FluentWikibaseClient


@pytest.fixture(scope="module")
def fluent_client():
    client = Client(timeout=200, follow_redirects=True, headers={"User-Agent": "wikibase-rest-api-client/1.0.0"})
    return FluentWikibaseClient(client, supported_props=["P31", "P17", "P569", "P625"])


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
        in [
            [d.value for d in ds]
            for (p, ds) in fluent_item.statements.items()
            if p.label == "date of birth" and p.datatype == "time"
        ][0]
    )

    assert "Q5" in [[d.qid for d in ds] for (p, ds) in fluent_item.statements.items() if p.pid == "P31"][0]


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
    client = Client(timeout=200, follow_redirects=True, headers={"User-Agent": "wikibase-rest-api-client/1.0.0"})
    fluent_client = FluentWikibaseClient(client, supported_props=["P31", "P17"])

    fluent_item = fluent_client.get_item("Q1066")
    assert [p.pid for p in fluent_item.statements.keys()] == ["P31", "P17"]

    for p, vs in fluent_item.statements.items():
        if p.pid == "P31":
            values = [v.value for v in vs]
            assert "lake" in values
        elif p.pid == "P17":
            values = [v.value for v in vs]
            assert "Canada" in values


def test_error_fluent(fluent_client):
    fluent_item = fluent_client.get_item("Q123456789")
    assert fluent_item is None

from wikibase_rest_api_client.api.items import get_item
from wikibase_rest_api_client.api.properties import get_property


def assert_item_label(client, item: str, lang: str, target: str):
    response = get_item.sync_detailed(item, client=client)
    assert response.status_code == 200
    assert response.parsed is not None
    assert response.parsed.labels is not None
    assert lang in response.parsed.labels
    assert response.parsed.labels[lang] == target


def assert_item_description(client, item: str, lang: str, target: str):
    response = get_item.sync_detailed(item, client=client)
    assert response.status_code == 200
    assert response.parsed is not None
    assert response.parsed.descriptions is not None
    assert lang in response.parsed.descriptions
    assert response.parsed.descriptions[lang] == target


def assert_property_label(client, prop: str, lang: str, target: str):
    response = get_property.sync_detailed(prop, client=client)
    assert response.status_code == 200
    assert response.parsed is not None
    assert response.parsed.labels is not None
    assert lang in response.parsed.labels
    assert response.parsed.labels[lang] == target

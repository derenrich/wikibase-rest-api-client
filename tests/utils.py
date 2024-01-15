from wikibase_rest_api_client.api.items import get_item
from wikibase_rest_api_client.api.properties import get_property
from wikibase_rest_api_client.models.item import Item
from wikibase_rest_api_client.models.item_aliases import ItemAliases
from wikibase_rest_api_client.models.item_descriptions import ItemDescriptions
from wikibase_rest_api_client.models.item_labels import ItemLabels
from wikibase_rest_api_client.models.property_ import Property
from wikibase_rest_api_client.models.property_aliases import PropertyAliases
from wikibase_rest_api_client.models.property_descriptions import PropertyDescriptions
from wikibase_rest_api_client.models.property_labels import PropertyLabels


def assert_item_label(client, item: str, lang: str, target: str):
    response = get_item.sync_detailed(item, client=client)
    assert response.status_code == 200
    assert response.parsed is not None
    assert isinstance(response.parsed, Item)
    assert response.parsed.labels is not None
    assert isinstance(response.parsed.labels, ItemLabels)
    assert lang in response.parsed.labels
    assert response.parsed.labels[lang] == target


def assert_item_description(client, item: str, lang: str, target: str):
    response = get_item.sync_detailed(item, client=client)
    assert response.status_code == 200
    assert response.parsed is not None
    assert isinstance(response.parsed, Item)
    assert isinstance(response.parsed.descriptions, ItemDescriptions)
    assert response.parsed.descriptions is not None
    assert lang in response.parsed.descriptions
    assert response.parsed.descriptions[lang] == target


def assert_item_alias(client, item: str, lang: str, target: str):
    response = get_item.sync_detailed(item, client=client)
    assert response.status_code == 200
    assert response.parsed is not None
    assert isinstance(response.parsed, Item)
    assert isinstance(response.parsed.aliases, ItemAliases)
    assert response.parsed.aliases is not None
    assert lang in response.parsed.aliases
    assert target in response.parsed.aliases[lang]


def assert_property_label(client, prop: str, lang: str, target: str):
    response = get_property.sync_detailed(prop, client=client)
    assert response.status_code == 200
    assert isinstance(response.parsed, Property)
    assert response.parsed is not None
    assert isinstance(response.parsed.labels, PropertyLabels)
    assert response.parsed.labels is not None
    assert lang in response.parsed.labels
    assert response.parsed.labels[lang] == target


def assert_property_description(client, item: str, lang: str, target: str):
    response = get_property.sync_detailed(item, client=client)
    assert response.status_code == 200
    assert isinstance(response.parsed, Property)
    assert response.parsed.aliases is not None
    assert isinstance(response.parsed.descriptions, PropertyDescriptions)
    assert response.parsed.descriptions is not None
    assert lang in response.parsed.descriptions
    assert response.parsed.descriptions[lang] == target


def assert_property_alias(client, item: str, lang: str, target: str):
    response = get_property.sync_detailed(item, client=client)
    assert response.status_code == 200
    assert response.parsed is not None
    assert isinstance(response.parsed, Property)
    assert response.parsed.aliases is not None
    assert isinstance(response.parsed.aliases, PropertyAliases)
    assert lang in response.parsed.aliases
    assert target in response.parsed.aliases[lang]

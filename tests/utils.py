from wikibase_rest_api_client.api.items import get_item


def assert_item_label(client, item: str, lang: str, target: str):
    response = get_item.sync_detailed(item, client=client)
    assert response.status_code == 200
    assert response.parsed is not None
    assert response.parsed.labels is not None
    assert lang in response.parsed.labels
    assert response.parsed.labels[lang] == target

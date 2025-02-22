import os

import pytest

from wikibase_rest_api_client import AuthenticatedClient
from wikibase_rest_api_client.client import Client


@pytest.fixture
def rw_client():
    token = os.environ.get("WIKIDATA_TEST_TOKEN")

    if token:
        return AuthenticatedClient(
            base_url="https://test.wikidata.org/w/rest.php/wikibase/v1/",
            token=token,
            headers={"User-Agent": "wikibase-rest-api-client/1.0.0"},
        )
    else:
        raise Exception("No wikidata test token found so cannot do write tests")


@pytest.fixture
def client():
    return Client(headers={"User-Agent": "wikibase-rest-api-client/1.0.0"})

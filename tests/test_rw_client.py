import json
import os

import pytest

from wikibase_rest_api_client import AuthenticatedClient
from wikibase_rest_api_client.api.aliases import (
    patch_item_aliases,
    patch_property_aliases,
)
from wikibase_rest_api_client.api.descriptions import (
    delete_item_description,
    patch_item_descriptions,
    patch_property_descriptions,
    replace_item_description,
    replace_property_description,
)
from wikibase_rest_api_client.api.labels import (
    delete_item_label,
    delete_property_label,
    patch_item_labels,
    patch_property_labels,
    replace_item_label,
    replace_property_label,
)
from wikibase_rest_api_client.api.properties import get_property
from wikibase_rest_api_client.models import (
    DescriptionReplaceRequest,
    DescriptionsPatchRequest,
    LabelReplaceRequest,
    LabelsPatchRequest,
    PatchDocumentPatchItem,
    PatchDocumentPatchItemOp,
)
from wikibase_rest_api_client.types import Response

from .utils import (
    assert_item_alias,
    assert_item_description,
    assert_item_label,
    assert_property_alias,
    assert_property_description,
    assert_property_label,
)

TEST_ITEM = "Q233445"
TEST_STRING_PROP = "P95180"
TEST_PROP = "P98080"
PROPS = [TEST_STRING_PROP, TEST_PROP]

IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"

if IN_GITHUB_ACTIONS:
    pytest.skip("Skipping write tests in github actions", allow_module_level=True)


@pytest.fixture
def client():
    token = os.environ.get("WIKIDATA_TEST_TOKEN")

    if token:
        return AuthenticatedClient(
            base_url="https://test.wikidata.org/w/rest.php/wikibase/v0/",
            token=token,
            headers={"User-Agent": "wikibase-rest-api-client/1.0.0"},
        )
    else:
        raise Exception("No wikidata test token found so cannot do write tests")


# just confirm the item we are going to test with still exists
def test_get_test_props(client):
    for prop in PROPS:
        with client as client:
            response = get_property.sync_detailed(prop, client=client)
            assert type(response) == Response
            assert response.status_code == 200


def test_delete_item_label(client):
    with client as client:
        # set the label
        test_label = "Test label " + str(os.urandom(10))
        response = replace_item_label.sync_detailed(TEST_ITEM, "en", LabelReplaceRequest(test_label), client=client)
        assert response.status_code == 200 or response.status_code == 201
        assert response.content == json.dumps(test_label).encode()

        assert_item_label(client, TEST_ITEM, "en", test_label)

        # delete the label
        response = delete_item_label.sync_detailed(TEST_ITEM, "en", client=client)

        # Check the response
        assert type(response) == Response
        assert response.status_code == 200
        assert response.content == b'"Label deleted"'


def test_patch_item_label(client):
    with client as client:
        test_label = "Test label" + str(os.urandom(10))
        patch = LabelsPatchRequest(
            [PatchDocumentPatchItem(PatchDocumentPatchItemOp.ADD, "/en", test_label)], comment="do a test patch"
        )
        response = patch_item_labels.sync_detailed(TEST_ITEM, patch, client=client)
        assert type(response) == Response
        assert response.status_code == 200

        assert_item_label(client, TEST_ITEM, "en", test_label)


def test_delete_property_label(client):
    with client as client:
        # set the label
        test_label = "Test label"
        response = replace_property_label.sync_detailed(
            TEST_PROP, "en", LabelReplaceRequest(test_label, comment="test label set"), client=client
        )
        assert response.status_code == 200 or response.status_code == 201
        assert response.content == b'"' + test_label.encode() + b'"'

        assert_property_label(client, TEST_PROP, "en", test_label)

        # delete the label
        response = delete_property_label.sync_detailed(TEST_PROP, "en", client=client)

        # Check the response
        assert type(response) == Response
        assert response.status_code == 200
        assert response.content == b'"Label deleted"'


def test_patch_property_label(client):
    with client as client:
        test_label = "Test label" + str(os.urandom(10))
        patch = LabelsPatchRequest(
            [PatchDocumentPatchItem(PatchDocumentPatchItemOp.ADD, "/en", test_label)], comment="do a test patch"
        )
        response = patch_property_labels.sync_detailed(TEST_PROP, patch, client=client)
        assert type(response) == Response
        assert response.status_code == 200

        assert_property_label(client, TEST_PROP, "en", test_label)


def test_patch_item_description(client):
    with client as client:
        test_desc = "Test desc " + str(os.urandom(10))
        patch = DescriptionsPatchRequest(
            [PatchDocumentPatchItem(PatchDocumentPatchItemOp.ADD, "/en", test_desc)], comment="do a test patch"
        )
        response = patch_item_descriptions.sync_detailed(TEST_ITEM, patch, client=client)
        assert type(response) == Response
        assert response.status_code == 200

        assert_item_description(client, TEST_ITEM, "en", test_desc)


def test_patch_property_description(client):
    with client as client:
        test_desc = "Test desc " + str(os.urandom(10))
        patch = DescriptionsPatchRequest(
            [PatchDocumentPatchItem(PatchDocumentPatchItemOp.ADD, "/en", test_desc)], comment="do a test patch"
        )
        response = patch_property_descriptions.sync_detailed(TEST_PROP, patch, client=client)
        assert type(response) == Response
        assert response.status_code == 200

        assert_property_description(client, TEST_PROP, "en", test_desc)


def test_delete_item_description(client):
    with client as client:
        test_description = "Test description " + str(os.urandom(10))
        response = replace_item_description.sync_detailed(
            TEST_ITEM, "en", DescriptionReplaceRequest(test_description), client=client
        )
        assert response.status_code == 200 or response.status_code == 201
        assert response.content == json.dumps(test_description).encode()
        assert_item_description(client, TEST_ITEM, "en", test_description)

        response = delete_item_description.sync_detailed(TEST_ITEM, "en", client=client)

        # Check the response
        assert type(response) == Response
        assert response.status_code == 200
        assert response.content == b'"Description deleted"'


def test_delete_property_description(client):
    with client as client:
        test_description = "Test description " + str(os.urandom(10))
        response = replace_property_description.sync_detailed(
            TEST_PROP, "en", DescriptionReplaceRequest(test_description), client=client
        )
        assert response.status_code == 200 or response.status_code == 201
        assert response.content == json.dumps(test_description).encode()
        assert_property_description(client, TEST_PROP, "en", test_description)

        # Not working yet? Marked as "in development" in the API docs
        # response = delete_property_description.sync_detailed(TEST_PROP, "en", client=client)
        # assert type(response) == Response
        # assert response.status_code == 200
        # assert response.content == b'"Description deleted"'


def test_patch_item_aliases(client):
    with client as client:
        # set alias to some value
        test_alias = "Test alias " + str(os.urandom(10))
        patch = DescriptionsPatchRequest(
            [PatchDocumentPatchItem(PatchDocumentPatchItemOp.ADD, "/en/0", test_alias)], comment="add alias"
        )
        response = patch_item_aliases.sync_detailed(TEST_ITEM, patch, client=client)
        assert type(response) == Response
        assert response.status_code == 200

        assert_item_alias(client, TEST_ITEM, "en", test_alias)

        # now blank the aliases
        patch = DescriptionsPatchRequest(
            [PatchDocumentPatchItem(PatchDocumentPatchItemOp.REMOVE, "/en", "")], comment="blank aliases"
        )
        response = patch_item_aliases.sync_detailed(TEST_ITEM, patch, client=client)
        assert type(response) == Response
        assert response.status_code == 200


def test_patch_property_aliases(client):
    with client as client:
        # set alias to some value
        test_alias = "Test alias " + str(os.urandom(10))
        patch = DescriptionsPatchRequest(
            [PatchDocumentPatchItem(PatchDocumentPatchItemOp.ADD, "/en/0", test_alias)], comment="add alias"
        )
        response = patch_property_aliases.sync_detailed(TEST_PROP, patch, client=client)
        assert type(response) == Response
        assert response.status_code == 200

        assert_property_alias(client, TEST_PROP, "en", test_alias)

        # now blank the aliases
        patch = DescriptionsPatchRequest(
            [PatchDocumentPatchItem(PatchDocumentPatchItemOp.REMOVE, "/en", "")], comment="blank aliases"
        )
        response = patch_property_aliases.sync_detailed(TEST_PROP, patch, client=client)
        assert type(response) == Response
        assert response.status_code == 200

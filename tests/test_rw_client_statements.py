import os

import pytest

from wikibase_rest_api_client.api.statements import (
    add_item_statement,
    add_property_statement,
    delete_statement,
    patch_statement,
    replace_statement,
)
from wikibase_rest_api_client.models import (
    PatchDocumentPatchItem,
    PatchDocumentPatchItemOp,
    PropertyInfo,
    Statement,
    StatementPatchRequest,
    StatementRequest,
    Value,
    ValueType,
)

TEST_ITEM = "Q233445"
TEST_STRING_PROP = "P95180"
TEST_PROP = "P98080"

IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"

if IN_GITHUB_ACTIONS:
    pytest.skip("Skipping write tests in github actions", allow_module_level=True)


def test_add_remove_item_statement(client):
    response = add_item_statement.sync_detailed(
        TEST_ITEM,
        StatementRequest(
            Statement(
                property_=PropertyInfo(id=TEST_STRING_PROP),
                value=Value(
                    content="test string",
                    type=ValueType.VALUE,
                ),
            ),
            comment="test add statement",
        ),
        client=client,
    )
    assert response.status_code == 201
    assert response.parsed is not None
    assert type(response.parsed) == Statement
    assert response.parsed.id.startswith(TEST_ITEM + "$")
    statement_id = response.parsed.id

    response = delete_statement.sync_detailed(statement_id, client=client)
    assert response.status_code == 200
    assert response.content == b'"Statement deleted"'


def test_add_remove_property_statement(client):
    response = add_property_statement.sync_detailed(
        TEST_PROP,
        StatementRequest(
            Statement(
                property_=PropertyInfo(id=TEST_STRING_PROP),
                value=Value(
                    content="test string",
                    type=ValueType.VALUE,
                ),
            ),
            comment="test add statement",
        ),
        client=client,
    )

    assert response.status_code == 201
    assert response.parsed is not None
    assert type(response.parsed) == Statement
    assert response.parsed.id.startswith(TEST_PROP + "$")
    assert response.parsed.value.content == "test string"
    statement_id = response.parsed.id

    response = replace_statement.sync_detailed(
        statement_id,
        StatementRequest(
            Statement(
                property_=PropertyInfo(id=TEST_STRING_PROP),
                value=Value(
                    content="test string 2",
                    type=ValueType.VALUE,
                ),
            ),
            comment="test replace statement",
        ),
        client=client,
    )
    assert response.status_code == 200
    assert response.parsed is not None
    assert type(response.parsed) == Statement
    assert response.parsed.id == statement_id
    assert response.parsed.value.content == "test string 2"

    response = patch_statement.sync_detailed(
        statement_id,
        StatementPatchRequest(
            [PatchDocumentPatchItem(PatchDocumentPatchItemOp.REPLACE, "/value/content", "test string 3")],
            comment="test patch statement",
        ),
        client=client,
    )
    assert response.status_code == 200
    assert response.parsed is not None
    assert type(response.parsed) == Statement
    assert response.parsed.id == statement_id
    assert response.parsed.value.content == "test string 3"

    response = delete_statement.sync_detailed(statement_id, client=client)
    assert response.status_code == 200
    assert response.content == b'"Statement deleted"'

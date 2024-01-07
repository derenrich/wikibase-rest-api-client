import os

import pytest

from wikibase_rest_api_client.api.statements import add_item_statement, delete_statement
from wikibase_rest_api_client.models import PropertyInfo, Statement, StatementRequest, Value, ValueType

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

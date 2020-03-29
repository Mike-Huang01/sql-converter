import pytest
from unittest import mock

from sql_export.export import SQLExport


@pytest.fixture
def query():
    return "SELECT * FROM users LIMIT 1"


@pytest.fixture
def data():
    return (51, 'John Doe', "john.doe@example.com"),


@mock.patch.object(SQLExport, "make_query")
def test_sql_export_should_print_data(mock_sql_response, query, capsys):
    data = ((51, 'John Doe', "john.doe@example.com"), )
    mock_sql_response.return_value = data
    SQLExport(
        query=query,
        headers=["id", "username", "email"],
        output_filename=None,
        pprint=True,
    ).make()
    expected = "{'id': 51, 'username': 'John Doe', 'email': 'john.doe@example.com'}\n"
    captured = capsys.readouterr()
    assert captured.out == expected


@mock.patch.object(SQLExport, "make_query")
def test_sql_export_none_headers_shoult_raise_exception(mock_sql_response, query, data):
    mock_sql_response.return_value = data
    with pytest.raises(AttributeError):
        SQLExport(query=query, headers=None).make()

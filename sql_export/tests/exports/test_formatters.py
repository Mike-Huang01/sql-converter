import os

import pytest

from sql_export.exports.formatters import ConsoleFormatter
from sql_export.exports.manager import ExportManager


@pytest.fixture
def headers():
    return ["id", "users"]


@pytest.fixture
def data():
    return (1, "John Doe"), (2, "John Smith"),


def test_json_formatter_should_return_json_seialized_data_in_file(headers, data, capsys):
    ExportManager(headers=headers, data=data, filename="test_json.json").run()
    captured = capsys.readouterr()
    assert captured.out == "test_json.json has been created successfully.\n"
    assert os.path.exists("test_json.json") is True
    os.remove("test_json.json")


def test_should_print_json_output(headers, data, capsys):
    ExportManager(headers=headers, data=data, filename="test_json.json").run(pprint=True)
    captured = capsys.readouterr()
    expected = '[\n  {\n    "id": 1,\n    "users": "John Doe"\n  }' \
               ',\n  {\n    "id": 2,\n    "users": "John Smith"\n  }\n]\n'
    assert captured.out == expected


def test_csv_formatter_should_return_csv_file(headers, data, capsys):
    ExportManager(headers=headers, data=data, filename="test_csv.csv").run()
    captured = capsys.readouterr()
    assert captured.out == "test_csv.csv has been created successfully.\n"
    assert os.path.exists("test_csv.csv") is True
    os.remove("test_csv.csv")


def test_csv_formatter_should_print_result_on_console(headers, data, capsys):
    ExportManager(headers=headers, data=data, filename="test_csv.csv").run(pprint=True)
    captured = capsys.readouterr()
    expected = "test_csv.csv has been created successfully.\n" \
               "['id', 'users']\n['1', 'John Doe']\n['2', 'John Smith']\n"
    assert captured.out == expected
    assert os.path.exists("test_csv.csv") is True
    os.remove("test_csv.csv")


def test_should_print_formatted_data_on_console(headers, data, capsys):
    ConsoleFormatter(headers=["id", "user"], data=data, filename=None).print()
    captured = capsys.readouterr()
    assert captured.out == "{'id': 1, 'user': 'John Doe'}\n{'id': 2, 'user': 'John Smith'}\n"


def test_export_console_output_should_return_error():
    data = ((1, "John Doe"), (2, "John Smith"),)
    with pytest.raises(ValueError):
        ConsoleFormatter(headers=["id", "user"], data=data, filename=None).export()

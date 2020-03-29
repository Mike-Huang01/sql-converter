# Readme

Export SQL extract in dedicated format.

## Presentation

This tool can be used by developers who want to print or dump SQL data in CSV or JSON to analyze tables or make tests 
fixtures.

## Installation

### Configuration

#### File

Setup the config file in `settings/files/config.yaml`

#### Environment Variables

    'SQL_EXPORT_DB_HOST': 'test_localhost',
    'SQL_EXPORT_DB_PORT': "1234",
    'SQL_EXPORT_DB_USER': 'root',
    'SQL_EXPORT_DB_NAME': 'mysql database name',
    'SQL_EXPORT_DB_PASSWORD': 'psswd'
    
### Virtualenv

    $ python3 -m venv venv
    $ source venv/bin/activate

## Usage:

### Query Builder

```python
from query.builder import Query
from query.database import Table


authors = Table(
    name="author",
    fields=["id", "name", "first_name", "nationality"],
    alias="aut"
)
books = Table(
    name="books",
    fields=["id", "author_id", "title", "isbn"],
    alias="boo",
)

query = Query(prettify=True) \
    .add(authors) \
    .add(books) \
    .join(authors, "id", books, "author_id") \
    .order_by(authors, "-id") \
    .limit(5) \

query.build()
```
## Export Data

### With Query Builder

```python
from export.sql_export import SQLExport

export = SQLExport(
    query=query.build(),
    headers=query.headers,
    output_filename=f"authors.json",
    pprint=True,
)

data = export.make()
```

### With Raw SQL

```python
from export.sql_export import SQLExport

query = """SELECT aut.id, aut.name, aut.first_name, aut.nationality, boo.id, boo.author_id, boo.title, boo.isbn 
FROM author AS aut 
    INNER JOIN books AS boo 
        ON boo.author_id = aut.id 
ORDER BY aut.id DESC 
LIMIT 5;"""

headers = ["id", "name", "first_name", "nationality", "id", "author_id", "title", "isbn"]

export = SQLExport(
    query=query,
    headers=headers,
    output_filename=f"authors.json",
    pprint=True,
)

data = export.make()
```

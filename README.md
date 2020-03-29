# Readme

[![pipeline status](https://gitlab.com/p2m3ng/sql-export/badges/master/pipeline.svg)](https://gitlab.com/p2m3ng/sql-export/-/commits/master)
[![coverage report](https://gitlab.com/p2m3ng/sql-export/badges/master/coverage.svg)](https://gitlab.com/p2m3ng/sql-export/-/commits/master)

Export SQL extract in dedicated format.

## Presentation

This tool can be used by developers in order to dump SQL data to console, CSV or JSON and make fixtures.  

## Installation

Clone repository: 

    $ git@gitlab.com:p2m3ng/sql-export.git

Or install with pip:

    $ pip install git+ssh://git@gitlab.com/p2m3ng/sql-export

### Configuration

Use package configuration file or environment variables. 

#### File

Setup the config file in `settings/files/config.yaml`

#### Environment Variables

    SQL_EXPORT_DB_HOST="localhost"
    SQL_EXPORT_DB_PORT=1234
    SQL_EXPORT_DB_USER="root"
    SQL_EXPORT_DB_NAME="my_database"
    SQL_EXPORT_DB_PASSWORD="password"

## Usage:

### Query Builder

```python
from sql_export.query import Query
from sql_export.queries.database import Table


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
from sql_export.export import SQLExport

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
from sql_export.export import SQLExport

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

# Readme

Export SQL extract in dedicated format.

## Presentation

This tool can be used by developers who want to dump SQL data in CSV or JSON to analyze tables or make tests fixtures.
Joins are not possible in this first POC version. 

## Usage:

First, setup the config file in `settings/environment/config.yaml`

```python
from main import SQLExport

export = SQLExport(
    tablename="set the table name here",
    headers="set the headers separated by spaces in a string, None for '*'",
    order="`field` for ASC, `-field` for DESC",
    limit="Data limit, default = None",
    output_filename="File extensions choices: csv, json. If no extension, console is the default",
    pprint="True: Print output to console, False export to a file silently",
    raw_query="Raw SQL query has to be used with appropriate headers"
)

data = export.run()
```

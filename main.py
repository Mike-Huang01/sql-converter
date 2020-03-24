import sys

from sql_export.connector import MySQLConnector
from sql_export.manager import Manager
from sql_export.query import QueryBuilder


class SQLExport:
    def __init__(
            self,
            tablename,
            headers=None,
            order=None,
            limit=None,
            output_filename=None,
            pprint=True,
            raw_query=None
    ):
        self.tablename = tablename
        self._headers = headers
        self.order = order
        self.limit = limit
        self.output_filename = output_filename
        self.pprint = pprint
        self.raw_query = raw_query

    @property
    def headers(self):
        if self.raw_query and not self._headers:
            print("ERROR: You used a raw SQL query. In this case, headers are mandatory.")
            sys.exit(1)
        if not self._headers:
            self._headers = self.query.headers
        return self.query.headers

    @property
    def query(self):
        return QueryBuilder(tablename=self.tablename, headers=self._headers, order=self.order, limit=self.limit)

    def make_query(self):
        if self.raw_query:
            return MySQLConnector.execute(self.raw_query)
        return MySQLConnector.execute(self.query.make())

    def run(self):
        return Manager(
            data=self.make_query(), headers=self.headers, filename=self.output_filename
        ).run(self.pprint)

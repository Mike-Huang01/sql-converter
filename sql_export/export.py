from typing import List, Optional

from sql_export.exports.connector import MySQLConnector
from sql_export.exports.manager import ExportManager
from sql_export.query import Query


class SQLExport:
    def __init__(
            self,
            query: (Query, str),
            headers: List[str],
            output_filename: Optional[str] = None,
            pprint: Optional[bool] = True,
    ):
        self.query = query
        self._headers = headers
        self.output_filename = output_filename
        self.pprint = pprint

    @property
    def headers(self):
        if self._headers is None:
            raise AttributeError("`headers` attribute should contain data.")
        return self._headers

    def make_query(self):
        return MySQLConnector.execute(self.query)

    def make(self):
        return ExportManager(
            data=self.make_query(), headers=self.headers, filename=self.output_filename
        ).run(self.pprint)

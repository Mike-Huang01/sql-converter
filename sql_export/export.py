from typing import List, Optional

from sql_export.exports.connector import MySQLConnector
from sql_export.exports.manager import ExportManager
from sql_export.query import Query


class SQLExport:
    def __init__(
            self,
            query: (Query, str),
            headers: List[str],
            export_to: Optional[str] = None,
    ):
        self.query = query
        self._headers = headers
        self.export_to = export_to

    @property
    def headers(self):
        if self._headers is None:
            raise AttributeError("`headers` attribute should contain data.")
        return self._headers

    def make_query(self):
        return MySQLConnector.execute(self.query)

    def make(self, pprint: Optional[bool] = False, json: Optional[bool] = False):
        return ExportManager(
            data=self.make_query(), headers=self.headers, export_to=self.export_to
        ).run(pprint=pprint, json=json)

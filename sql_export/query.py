from sql_export.connector import MySQLConnector


class QueryBuilder:
    connector = MySQLConnector

    def __init__(self, tablename, headers=None, order=None, limit=None):
        self.tablename = tablename
        self._headers = headers
        self.order = order
        self.limit = limit

    def make(self):
        headers = [f"`{header}`" for header in self.headers]
        return f"SELECT {', '.join(headers)} FROM {self.tablename} {self.get_order()}{self.get_limit()};"

    @property
    def headers(self):
        if self._headers is None:
            describe = self.connector.execute(f"DESCRIBE {self.tablename};")
            return [header[0] for header in describe]
        else:
            try:
                return [header for header in self._headers.split(" ")]
            except AttributeError:
                return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value

    def get_limit(self):
        if self.limit is None:
            return ""
        else:
            return f"LIMIT {self.limit}"

    def get_order(self):
        if self.order is None:
            return ""
        elif self.order.startswith("-"):
            return f"ORDER BY {self.order[1:]} DESC "
        elif not self.order.startswith("-"):
            return f"ORDER BY {self.order} ASC "

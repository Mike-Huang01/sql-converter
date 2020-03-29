from sql_export.settings.settings import get_config
from sql_export.exports.formatters import CSVFormatter, JsonFormatter, ConsoleFormatter

config = get_config()


class File:
    def __init__(self, filename):
        self.filename = filename

    def get_extension(self):
        try:
            return self.filename.split(".")[1]
        except (IndexError, AttributeError):
            return None

    def get_filename(self):
        if self.filename is None:
            return ""
        return self.filename


class ExportManager:
    formats = {"csv": "csv", "json": "json", "console": "console"}

    def __init__(self, data, headers, filename):
        self._filename = File(filename=filename)
        self.headers = headers
        self.data = data

    @property
    def filename(self):
        return self._filename.get_filename()

    def run(self, pprint):
        extension = self._filename.get_extension()
        formatter = self.formats.get(extension, "console")
        if formatter == "csv":
            return self.__to_csv(pprint=pprint)
        elif formatter == "json":
            return self.__to_json(pprint=pprint)
        elif formatter == "console":
            return self.__to_console()

    def __to_console(self):
        formatter = ConsoleFormatter(headers=self.headers, data=self.data, filename=self.filename)
        formatter.print()

    def __to_csv(self, pprint=False):
        formatter = CSVFormatter(headers=self.headers, data=self.data, filename=self.filename)
        if pprint:
            return formatter.print()
        return formatter.export()

    def __to_json(self, pprint=False):
        formatter = JsonFormatter(headers=self.headers, data=self.data, filename=self.filename)
        if pprint:
            return formatter.print()
        formatter.export()
        return formatter.use()

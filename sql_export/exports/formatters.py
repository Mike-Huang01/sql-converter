import csv
import json
from abc import ABC, abstractmethod


class BaseFormatter(ABC):
    def __init__(self, headers, data, filename):
        self.headers = headers
        self.data = data
        self.filename = filename

    @abstractmethod
    def export(self):
        """"""

    @abstractmethod
    def print(self):
        """"""


class CSVFormatter(BaseFormatter):

    def export(self):
        with open(f"{self.filename}", 'w') as file:
            writer = csv.writer(file, delimiter="|")
            writer.writerow(self.headers)
            writer.writerows(self.data)
        print(f"{self.filename} has been created successfully.")
        return ""

    def print(self):
        self.export()
        with open(f"{self.filename}", 'r') as file:
            reader = csv.reader(file, delimiter="|")
            for line in reader:
                print(line)
        return ""


class DictFormatter(BaseFormatter, ABC):
    def _dict_formatter(self):
        result = []
        for data in self.data:
            result.append(dict(zip(self.headers, data)))
        return result

    @abstractmethod
    def export(self):
        """"""

    @abstractmethod
    def print(self):
        """"""


class JsonFormatter(DictFormatter):

    def export(self):
        with open(f"{self.filename}", "w") as file:
            json.dump(self._dict_formatter(), file, indent=2, ensure_ascii=False, default=str)
        print(f"{self.filename} has been created successfully.")
        return self.use()

    def use(self):
        return json.dumps(self._dict_formatter(), ensure_ascii=False, default=str)

    def print(self):
        return print(json.dumps(self._dict_formatter(), indent=2, ensure_ascii=False, default=str))


class ConsoleFormatter(DictFormatter):
    def export(self):
        raise ValueError("Unusable method.")

    def print(self):
        for data in self._dict_formatter():
            print(data)
        return ""

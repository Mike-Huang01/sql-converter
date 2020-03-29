import random
import string


class BaseMapper:

    def __init__(self, name, alias=None):
        self.name = name
        self._alias = alias

    @property
    def alias(self):
        if self._alias is None:
            self.alias = self._get_alias()
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value

    @staticmethod
    def _get_alias():
        return "".join([random.choice(string.ascii_letters) for _ in range(3)])


class Database(BaseMapper):
    pass


class Table(BaseMapper):
    def __init__(self, name, alias=None, fields=None):
        super(Table, self).__init__(name=name, alias=alias)
        self._fields = fields

    @property
    def fields(self):
        if self._fields is None:
            return None
        return ", ".join([f"`{self.alias}`.`{field}`" for field in self._fields])


class Field(BaseMapper):
    def __init__(self, name):
        super(Field, self).__init__(name=name)

    @property
    def alias(self):
        raise AttributeError("'Field' object has no attribute 'alias'")

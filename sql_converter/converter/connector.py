import pymysql

from sql_converter.settings.settings import get_config


class MySQLConnector:
    config = get_config()

    @classmethod
    def connect(cls):
        return pymysql.connect(
            host=cls.config.get['db']['host'],
            user=cls.config.get['db']['user'],
            password=cls.config.get['db']['password'],
            db=cls.config.get['db']['name'],
            port=cls.config.get['db']['port'],
        )

    @classmethod
    def execute(cls, request):
        connect = cls.connect()
        try:
            with connect.cursor() as cursor:
                cursor.execute(request)
                return cursor.fetchall()
        finally:
            connect.close()

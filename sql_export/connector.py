import pymysql

from settings.settings import get_config


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
        try:
            connect = cls.connect()
            with connect.cursor() as cursor:
                cursor.execute(request)
                return cursor.fetchall()
        finally:
            connect.close()

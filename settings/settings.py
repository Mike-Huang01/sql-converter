import os

import yaml


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config:
    def __init__(self, file="config.yaml"):
        self.file = file

    @property
    def get(self):
        return self.get_file_content()

    def get_file_content(self):
        with open(self.get_file_path()) as file:
            return yaml.load(file, Loader=yaml.FullLoader)

    def get_file_path(self):
        return os.path.join(BASE_DIR, "files", self.file)

    def __repr__(self):
        return f"<Configuration: {self.file}>"


def get_config(file="config.yaml"):
    return Config(file=file)

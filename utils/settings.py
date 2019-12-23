import json
from typing import List


class Settings:
    settings_filename = "utils/settings.json"
    settings: dict = {}

    def __init__(self):
        self.settings = json.loads(open(self.settings_filename).read())

    def add_to_list(self, list_name: str, string: str):
        if self.settings.get(list_name):
            list_to_edit: List = self.settings[list_name]
            list_to_edit.append(string)
        else:
            self.settings[list_name] = [string]
        self.write()

    def write(self):
        json_to_write = json.dumps(self.settings)
        with open(self.settings_filename, "w") as settings_file:
            settings_file.write(json_to_write)

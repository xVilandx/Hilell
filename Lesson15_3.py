import json


class JsonReader:
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def read_json(self):
        with open(self.filename, 'r') as json_file:
            self.data = json.load(json_file)


class JsonWorkerList(JsonReader):
    def __init__(self, filename, limit):
        super().__init__(filename)
        self.data = self.data[:limit]

    def sort(self):
        self.data.sort()


class JsonWorkerDict(JsonReader):
    def sort(self):
        keys = self.data.keys()
        keys = sorted(keys)
        self.data = {key: self.data[key] for key in keys}

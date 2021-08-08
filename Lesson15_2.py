import csv


class ReadCSV:
    def __init__(self, filename, mode='reader'):
        self.filename = filename
        if mode == 'dict_reader':
            self._csv_mode = csv.DictReader
        else:
            self._csv_mode = csv.reader

    def read_from_csv(self):
        with open(self.filename, 'r') as csv_file:
            reader = self._csv_mode(csv_file, deliniter=',')
            data = []
            for row in reader:
                data.append(row)
            return data

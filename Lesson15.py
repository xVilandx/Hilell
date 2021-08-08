import os
import string


class WorkWithFiles:
    def __init__(self, dirname='alphabet'):
        self.dirname = dirname
        self.create_dir()

    def create_dir(self):
        os.makedirs(self.dirname, exist_ok=True)

    def create_file(self, symbol):
        filename = f'{self.dirname}/{symbol}.txt'
        with open(filename, 'w') as txt_file:
            txt_file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))

    def create_files_in_dir(self):
        for letter in string.ascii_lowercase:
            self.create_file(letter)

    def get_tanos_click(self):
        files = os.listdir(self.dirname)
        files = list(set(files))[:len(files) // 2]
        for file in files:
            os.remove(os.path.join(self.dirname, file))
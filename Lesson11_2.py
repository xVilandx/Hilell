import csv


def write_to_csv(filename, data, delimiter=','):
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=delimiter)
        writer.writerows(data)


def read_from_csv(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = []
        for row in reader:
            data.append(row)
        return data


file_name = 'data.csv'
data_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
write_to_csv(data=data_2, filename=file_name)

new_data = read_from_csv(file_name)

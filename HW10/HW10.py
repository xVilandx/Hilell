#1 task
def create_list_domains(file_name):
    with open(file_name, 'r') as txt_file:
        return txt_file.read().replace('.', '').split('\n')


#2 task
def create_list_surname(file_name):
    with open(file_name, 'r') as txt_file:
        return txt_file.read().split('\t')[1::3]


#3 task
def create_list_date(file_name):
    with open(file_name, 'r') as txt_file:
        list_date = [date for date in txt_file.read().split('\n') if date.count('-') > 0]
        list_date = [date.split(' - ')[0] for date in list_date if len(date[0:date.find('-')].split()) == 3]
        return list_date


def modified_date(date_line):
    month_dict = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
                  'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
    day, months, year = date_line.split()
    day = day.rstrip('ndrsth')
    day = day if len(day) == 2 else f'0{day}'
    months = month_dict[months]
    new_date = f'{day}/{months}/{year}'
    return new_date


def create_dict(file_name):
    full_list = []
    for value in range(len(create_list_date(file_name))):
        date = create_list_date(file_name)[value]
        date_dict = dict(date_original=date, date_modified=modified_date(date))
        full_list.append(date_dict)
    return full_list

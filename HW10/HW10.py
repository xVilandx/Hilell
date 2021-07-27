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
        list_date = [my_str[0:my_str.find('-')-1] for my_str in txt_file.read().split('\n') if my_str.count('-') > 0]
        return list_date


def modified_date(file_name):
    modified_list_date = []
    month_dict = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
                  'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
    for date in create_list_date(file_name):
        my_string = ''
        for value in date.split():
            if value[0].isdigit() and not value[2].isdigit():
                if len(value) == 3:
                    my_string += '0' + value[0] + '/'
                else:
                    my_string += value[:2] + '/'
            if month_dict.get(value):
                my_string += month_dict[value]
            if value.isdigit():
                my_string += '/' + value
        modified_list_date.append(my_string)
    return modified_list_date


def create_dict(file_name):
    full_list_date = []
    for value in range(len(create_list_date(file_name))):
        my_dict = dict(date_original=create_list_date(file_name)[value], date_modified=modified_date(file_name)[value])
        full_list_date.append(my_dict)
    return full_list_date

my_str = 'Это "как буд-то" ну ооооочень длииииинаааая строка'
l_symbol = 'н'
r_symbol = 'о'
sub_str = my_str[my_str.find(l_symbol)+1:my_str.rfind(r_symbol)]
print(sub_str)
# class MyFirstClass:
#     some_string = 'TEST'
#
#
# MyFirstClass.some_string = 'new test'
# test_value = MyFirstClass.some_string
#
# print(test_value)

# class Person:
#     name = 'John'
#     surname = 'Wick'
#     age = 23
#     sex = 'Male'
#
#
# if Person.age < 50:
#     print(f'Ты молодой человек, {Person.name} {Person.surname}')
#
# person1 = Person()
# person2 = Person()
# print(person1.name)
# print(person2.name)

class Person:
    def __init__(self, name, surname, age, sex):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.switch_sex()

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.age}'

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def increase_age(self):
        self.age += 1

    def switch_sex(self):
        sex_dict = {'Male': 'Female', 'Female': 'Male'}
        self.sex = sex_dict[self.sex]


person_1 = Person('John', 'Wick', 23, "male")
print(person_1)
person_1.increase_age()
person_1.switch_sex()
print(person_1)
person_2 = Person('Jane', 'Fri', 32, 'Female')
list_persons = [person_1, person_2]
print(person_1.name)
print(person_2.name)

print(list_persons)
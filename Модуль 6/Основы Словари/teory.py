# phonebook_dict = {'Ваня': 8800,
#                   'Петя': 5424,
#                   'Лена': 5345
#                   }
# name = input('Введите имя: ')
# if name in phonebook_dict:
#     print(phonebook_dict[name])
# else:
#     print('Человек с именем {0} не найден'.format(name))

student = input(
    'Введите информацию о студент через пробел\n'
    '(имя, фамилия, город, место учебы, оценки):'
)

student_info = student.split()
student = dict()
student['Имя'] = student_info[0]
student['Фамилия'] = student_info[1]
student['Город'] = student_info[2]
student['Место учебы'] = student_info[3]
student['Оценки'] = []

for i_grade in student_info[4:]:
    student['Оценки'].append(int(i_grade))

for i in student:
    print(i, '-', student[i])
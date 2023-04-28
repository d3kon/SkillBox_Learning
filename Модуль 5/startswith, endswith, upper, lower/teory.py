# user_name = input('Введите пользователя: ')
# file_name = input('Введите имя файла: ')
#
# path = 'C:/{user}/docs/folder/{new_file}'.format(
#     user=user_name,
#     new_file=file_name
# )
#
# if path.endswith('.txt'):
#     print(path)
# else:
#     print('Ошибка!')



word_list = []

for i_num in range(3):
    print(f'Введите {i_num + 1} слово: ')
    # word = input().lower()
    word = input().upper()
    word_list.append(word)

# text = input('Введите текст: ').lower().split()
text = input('Введите текст: ').upper().split()

print('\n Подсчет слов в тексте')
for index in range(3):
    print(word_list[index], ':', text.count(word_list[index]))
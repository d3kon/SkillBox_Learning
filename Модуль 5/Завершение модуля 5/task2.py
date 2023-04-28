text = input('Введите строку: ').split(' ')
max_len = len(text[0])
max_word = ''
for i in text:
    if len(i) >= max_len:
        max_len = len(i)
        max_word = i

print(f'Самое длинное слово: "{max_word}"')
print(f'Длина этого слова: {max_len}')
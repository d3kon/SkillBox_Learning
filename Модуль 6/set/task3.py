text = input('Введите строку: ')

new_text = set(text)
result = new_text & set('0123456789')
print(''.join(result))
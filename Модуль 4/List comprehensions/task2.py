word = input('Введите строку: ')
symbol = input('Ввведите дополнительный символ: ')

print([x * 2 for x in word])
print([x * 2 + symbol for x in word])
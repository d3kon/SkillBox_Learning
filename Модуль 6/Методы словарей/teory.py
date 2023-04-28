text = input("Введите текст: ")

frequency = {}
for symbol in text:
    if symbol in frequency:
        frequency[symbol] += 1
    else:
        frequency[symbol] = 1

for letter, freq in frequency.items():
    print(letter, ':', freq)

print("Максимальная частота: ", max(frequency.values()))


# phonebook = {
#     'Ваня': 100,
#     'Петя': 200,
#     'Алиса': 300,
# }
#
# other_phonebook = {
#     'Игорь': 1000,
#     'Петя': 800,
#     'Алена': 2000,
# }
#
# phonebook.update(other_phonebook)
# print(phonebook)
#
# phonebook['Гоша'] = phonebook.pop('Игорь')
# print(phonebook)
#
# print(phonebook.get('Степан'))
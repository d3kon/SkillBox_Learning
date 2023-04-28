text = input("Введите текст: ")

frequency = {}
for symbol in text:
    if symbol in frequency:
        frequency[symbol] += 1
    else:
        frequency[symbol] = 1

for letter, freq in frequency.items():
    print(letter, ':', freq)

invent_dict = {}
for symbol, count in frequency.items():
    invent_dict.setdefault(count, []).append(symbol)  # сортировка и запись значений по определенному количеству
for i in invent_dict:
    print(i, ':', invent_dict[i])

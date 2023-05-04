count_pare = int(input('Введите количество пар слов: '))
pare_dict = {}

for i in range(count_pare):
    pare = input(f'{i + 1}-я пара: ').title().split(' - ')
    pare_dict[pare[0]] = pare[1]
    pare_dict[pare[1]] = pare[0]

while True:
    word = input('Введите слово: ').title()
    if word in pare_dict:
        print(f'Синоним {pare_dict[word]}')
    else:
        print(f'Синоним к слову {word} не обнаружен')


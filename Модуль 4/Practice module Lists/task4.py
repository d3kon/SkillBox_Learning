guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

count = 5
while True:
    print(f'Сейчас на вечеринке {count} человек: {guests}')
    answer = input('Гость пришел или ушел? ')
    if answer == 'пришел':
        name_guest = input('Введите имя гостя: ')
        if count < 6:
            guests.append(name_guest)
            print(f'Привет {name_guest}!')
            count += 1
        else:
            print(f'Прости, {name_guest},но мест нет.')

    elif answer == 'ушел':
        name_guest = input('Введите имя гостя: ')
        if name_guest in guests:
            guests.remove(name_guest)
            print(f'Пока {name_guest}')
            count -= 1
        else:
            print('Такого гостя и не было!')
    elif answer == 'Пора спать':
        break


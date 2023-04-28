# Контейнеры на складе лежат в ряд в порядке невозрастания (меньше либо равно) массы в килограммах.
# На склад привезли ещё один контейнер, который тоже нужно положить на определённое место.
#
# Напишите программу, которая получает на вход невозрастающую последовательность натуральных чисел.
# Они означают массу каждого контейнера в ряду. После этого вводится число X — масса нового контейнера.
# Программа выводит номер, под которым будет лежать новый контейнер. Если в ряду есть контейнеры с массой, как у нового, то его нужно положить после них.
#
# Обеспечьте контроль ввода: все числа не превышают 200.

def Containers(count):
    list_container = []
    k = 0
    for i in range(count):
        try:
            weight = int(input('Введите вес контейнера: '))
            if weight <= 200:
                list_container.append(weight)
            else:
                while weight > 200:
                    weight = int(input('Повторите ввод: '))
                else:
                    list_container.append(weight)
        except ValueError:
            print('Введено не число!')
            return
    new_container = int(input('Введите вес нового контейнера: '))
    if new_container <= 200:
        list_container.append(new_container)
    else:
        while new_container > 200:
            new_container = int(input('Повторите ввод: '))
        else:
            list_container.append(new_container)

    list_container.sort(reverse=True)
    return f'Место для нового контейнера: {list_container.index(new_container) + 1}'


if __name__ == "__main__":
    try:
        print(Containers(int(input('Введите количество контейнеров: '))))
    except ValueError:
        print('Введено не число!')

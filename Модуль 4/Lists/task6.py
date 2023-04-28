def Shift(count, K):
    list_start = []
    for i in range(count):
        number = int(input(f'Введите {i + 1}й элемент списка из {count}: '))
        list_start.append(number)
    print(f'Изначальный список: {list_start}')

    lst_shift = list_start[-K:] + list_start[:-K]
    print(f'Список со двигом: {lst_shift}')


if __name__ == '__main__':
    Shift(int(input('Введите количество элементов массива: ')), int(input('Введите сдвиг: ')))

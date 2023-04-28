def Sort(N):
    num_list = []
    for i in range(N):
        try:
            number = int(input(f'Введите {i + 1}e число списка: '))
            num_list.append(number)
        except ValueError:
            print('Вы ввели не число!')
            return

    num_list.sort()
    return num_list


if __name__ == "__main__":
    try:
        print(Sort(int(input('Введите количество чисел в списке: '))))
    except ValueError:
        print('Вы ввели не число!')

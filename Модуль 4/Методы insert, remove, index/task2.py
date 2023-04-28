def Cut(N):
    person_list = []
    count_zero = 0
    for i in range(N):
        person = int(input(f'Зарплата {i+1} сотрудника: '))
        person_list.append(person)
    for i in person_list:
        if i == 0:
            person_list.remove(i)
            count_zero += 1
    print(f'Осталось сотрудников {N - count_zero}')
    return person_list


if __name__ == "__main__":
    try:
        print(Cut(int(input('Введите количество сотрудников: '))))
    except ValueError:
        print('Вы ввели не число!')
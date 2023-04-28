def generator(N):
    return [(1 if i % 2 == 0 else i % 5) for i in range(N)]


if __name__ == '__main__':
    print(generator(int(input('Введите длину списка: '))))
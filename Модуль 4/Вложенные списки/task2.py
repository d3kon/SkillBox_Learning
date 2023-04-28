N = int(input('Кол-во участников: '))
count = int(input('Кол-во человек в команде: '))
members = []
num = 1
if N % count == 0:
    for _ in range(N // count):
        members.append(list(range(num, num + 4)))
        num += 4
    print(members)
else:
    print(f'{N} участников невозможно поделить на команды по {count} человек!')
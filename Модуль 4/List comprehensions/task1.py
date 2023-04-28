left = int(input('Левая граница: '))
right = int(input('Правая граница: '))

print([x ** 3 for x in range(left, right + 1)])
print([x ** 2 for x in range(left, right + 1)])
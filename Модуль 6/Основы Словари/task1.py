# def f(x): return x, x ** 2
#
#
# N = int(input('Ввведите число итераций:'))
# print(dict(f(x) for x in range(1, N + 1)))

number = int(input("Введите целое число: "))
result = {}
for i in range(1, number + 1):
    result[i] = i ** 2
print("Результат:", result)
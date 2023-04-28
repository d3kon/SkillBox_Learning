import random

A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))

mass = [number for number in range(A,B) if number % 2 == 0]
print(mass)
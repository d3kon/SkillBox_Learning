import random

numbers_list = [random.randint(1, 4) for _ in range(10)]
unique = set(numbers_list) #Выводит только уникальные значения, создает множество
print(unique)


# unioun
# intersection
# difference
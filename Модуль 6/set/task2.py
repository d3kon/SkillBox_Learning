import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

nums__1 = set(nums_1)
nums__2 = set(nums_2)

print(f'Удаляем число {min(nums__1)}')
nums__1.discard(min(nums__1))
print(f'Удаляем число {min(nums__2)}')
nums__2.discard(min(nums__2))

nums__1.add(random.randint(100, 200))
nums__2.add(random.randint(100, 200))
print(f'Множество 1 с новым числом и без минимального: {nums__1}')
print(f'Множество 2 с новым числом и без минимального: {nums__2}')

print(nums__1.union(nums__2))
print(nums__1.intersection(nums__2))
print(nums__2.difference(nums__1))

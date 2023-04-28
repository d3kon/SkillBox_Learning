import random

squad1 = [random.randint(50, 80) for _ in range(10)]
squad2 = [random.randint(30, 60) for _ in range(10)]
squad3_condition = [('Погиб' if squad1[i_damage] + squad2[i_damage] > 100
                     else 'Выжил')
                    for i_damage in range(10)]

print(f'Урон первого отряда: {squad1}')
print(f'Урон второго отряда: {squad2}')
print(f'Результат боя: {squad3_condition}')
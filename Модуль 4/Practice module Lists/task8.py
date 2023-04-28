number = int(input('Количество чисел: '))
mass_num = []
for i in range(number):
    num = int(input('Число: '))
    mass_num.append(num)

print(f'Последовательность: {mass_num}')
i = 0

while mass_num != mass_num[::-1]:
    mass_num.insert(number, mass_num[i])
    i += 1

print(i)
print(*mass_num[:i][::-1])
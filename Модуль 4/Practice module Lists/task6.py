n_count = int(input('Количество коньков: '))
pare = []
count = 0
for i in range(1, n_count + 1):
    pare.append(int(input(f'Размер пары {i}: ')))

people_count = int(input('Количество людей: '))
legs = []
for b in range(1, people_count + 1):
    legs.append(int(input(f'Размер ноги человека {b}: ')))

for num in legs:
    for j in range(len(pare)):
        if pare[j] >= num:
            pare.remove(pare[j])
            count += 1
            break

print(count)

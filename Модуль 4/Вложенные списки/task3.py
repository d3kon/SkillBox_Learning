goods = [
    ["яблоки", 50],  # 0
    ["апельсины", 190],  # 1
    ["груши", 100],  # 2
    ["нектарины", 200],  # 3
    ["бананы", 77]  # 4
]
print(f'Текущий ассортимент: {goods}')
new_fruit = input('Наименование нового фрукта: ')
price = int(input('Цена нового фрукта: '))

goods.append([new_fruit, price])
print(goods)

for fruit in goods:
    fruit[1] = round(fruit[1] * 1.08, 2)

print(goods)

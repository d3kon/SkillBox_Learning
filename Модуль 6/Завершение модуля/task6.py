count_orders = int(input('Введите количество заказов: '))

orders_dict = {}

for i in range(1, count_orders + 1):
    product = input(f'{i}-й заказ: ').title().split()
    if product[0] in orders_dict:
        if product[1] in orders_dict[product[0]]:
            orders_dict[product[0]][product[1]] += product[2]
        else:
            orders_dict[product[0]][product[1]] = product[2]
    else:
        orders_dict[product[0]] = dict({product[1]: int(product[2])})

for elem1 in sorted(orders_dict):
    print(f'\n{elem1}: ')
    for elem2 in sorted(orders_dict[elem1]):
        print(f'\t{elem2}: {orders_dict[elem1][elem2]}')

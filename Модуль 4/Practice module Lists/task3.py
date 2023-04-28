shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
count_detail = 0
summ = 0
name_detail = input('Название детали: ')
for i in shop:
    if i[0] == name_detail:
        count_detail += 1
        summ += i[1]


print(f'Количество деталей: {count_detail}')
print(f'Общая стоимость: {summ}')

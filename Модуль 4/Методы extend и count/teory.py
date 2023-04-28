# my_list = ['Игра', 'Изгой', 'Таксист']
# your_list = ['Начало', 'Отступники', 'Король Лев']
#
# my_list.extend(your_list)
#
# print(my_list)


pack = []
decode = []
bad_packs = 0

packs_amt = int(input('Кол-во пакетов: '))
for i_pack_num in range(packs_amt):
    print(f'\nПакет номер {i_pack_num + 1}')
    for i_bit in range(4):
        print(f'{i_bit + 1} бит: ')
        num = int(input())
        pack.append(num)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('Много ошибок в пакете.')
        bad_packs += 1
    pack = []

print(f'Полученное сообщение: {decode}')
print(f'Кол-во ошибок в сообщении: {decode.count(-1)}')
print(f'Кол-во потерянных пакетов: {bad_packs}')
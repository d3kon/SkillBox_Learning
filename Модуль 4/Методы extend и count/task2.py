first_messege = input('Первое сообщение: ')
second_messege = input('Второе сообщение: ')
count_one = first_messege.count('!') + first_messege.count('?')
count_too = second_messege.count('!') + second_messege.count('?')
if count_one > count_too:
    print('Третье сообщение:', first_messege, second_messege)
elif count_too > count_one:
    print('Третье сообщение:', second_messege, first_messege)
else:
    print('Ой')

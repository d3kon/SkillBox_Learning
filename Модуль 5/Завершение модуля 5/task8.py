s1 = input('Первая строка: ')
s2 = input('Вторая строка: ')

if s1 == s2:
    print('Строки идентичны!')

elif len(s2) != len(s1):
    print('В во торой строке больше или меньше символов чем в первой.')

else:
    k = 1
    mozhno = False
    for i in range(len(s2) - 1):
        s2 = s2[-1] + s2[:-1]
        print(s2)
        if s2 == s1:
            mozhno = True
            print(f'Первая строка получается из второй со двигом {k}')
            break
        else:
            k += 1
    if not mozhno:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
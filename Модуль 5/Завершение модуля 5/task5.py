# При регистрации на сайте, помимо логина, нужно придумать пароль.
# Этот пароль должен состоять минимум из восьми символов, содержать хотя бы одну большую букву и не менее трёх цифр.
# Тогда он будет считаться надёжным.
#
# Напишите программу, которая просит пользователя придумать пароль до тех пор, пока этот пароль не станет надёжным. Должна использоваться латиница.



while True:
    password = input('Придумайте пароль: ')
    if len(password) < 8 or sum(i.isupper() for i in password) < 1 or sum(i.isdigit() for i in password) < 3:
        print('Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль.')
        break
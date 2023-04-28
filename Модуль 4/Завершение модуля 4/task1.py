def search_vowel(text):
    mass = [i for i in text if i in ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'е')]
    print(mass)
    print(len(mass))


if __name__ == '__main__':
    search_vowel(input('Введите строку: '))

def Pallindrom(word):
    return_word = word[::-1]
    if return_word == word:
        return 'Слово является палиндромом!'
    else:
        return 'Слово не является палиндромом'


if __name__ == "__main__":
    print(Pallindrom(input('Введите слово: ')))

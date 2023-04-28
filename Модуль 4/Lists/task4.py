def Film(N, count):
    my_film_list = []
    for _ in range(count):
        film = input('Введите название фильма: ')
        if film in N:
            my_film_list.append(film)
        else:
            print(f'Ошибка фильма {film} у нас нет :(')
    print(*my_film_list, sep=', ')


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
         'Отступники', 'Деревня']
if __name__ == '__main__':
    Film(films, int(input('Сколько фильмов добавить? ')))

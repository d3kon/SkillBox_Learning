violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
summ_time = 0
N = int(input('Сколько песен выбрать? '))
for i in range(1, N + 1):
    song = input(f'Ввведите название {i}-й песни: ')
    for p in violator_songs:
        if song == p[0]:
            summ_time += p[1]

print(f'Общее время звучания песен: {summ_time}')

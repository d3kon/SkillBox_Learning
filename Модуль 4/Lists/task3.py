N = int(input('Введите количество видекарт: '))
video_card = []

for i in range(N ):
    V = int(input(f'Видеокарта {i + 1}: '))
    video_card.append(V)

print(video_card)

m = max(video_card)
video_card = [i for i in video_card if i != m]
print(video_card)
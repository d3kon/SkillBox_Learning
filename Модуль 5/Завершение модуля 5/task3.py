word = input('Введите название файла: ')
if set(word) & set('@№$%^&*()'):
  print('Ошибка: в названии файла запрещенный символ!')
elif word.endswith('.txt' and '.docx'):
  print('Все хорошо!')
else:
  print('Ошибка: формат файла не txt или не docx')

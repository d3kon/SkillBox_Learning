# text = input('Введите строку: ')
# s2 = ''
# n = 1
#
# for i in range(len(text) - 1):
#     if text[i] == text[i + 1]:
#         n += 1
#     if text[i] != text[i + 1] or i == len(text) - 2:
#         s2 += text[i] + str(n)
#         n = 1
# if text[-2] != text[-1]:
#     s2 += text[-1] + '1'
# print(s2)

message = str(input())
cnt = 1
x = 1
j = message[x:x+1]
for i in message:
    if i in j:
        cnt += 1
    else:
        print(i, end='')
        print(cnt, end='')
        cnt = 1
    x += 1
    j = message[x:x+1]
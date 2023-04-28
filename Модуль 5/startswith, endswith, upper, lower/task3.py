string = input()
low_summ = 0
up_summ = 0

for i in string:
    if i.islower():
        low_summ += 1
    elif i.isupper():
        up_summ += 1

if low_summ > up_summ:
    print(string.lower())
else:
    print(string.upper())
# number = int(input('Количество чисел: '))
def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i_num])
    if num_list == reverse_list:
        return True
    else:
        return False


nums = [1, 2, 3, 4, 3, 2]
mass_num = []
answer = []

for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        mass_num.append(nums[j])
    if is_palindrome(mass_num):
        for i_answer in range(0, i):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    mass_num = []

print(f'Исходный список: {nums}')
print(f'Нужно чисел: {len(answer)}')
print(f'Список этих чисел {answer}')

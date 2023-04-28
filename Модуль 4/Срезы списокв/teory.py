# nums = [x for x in range(1, 101) if x % 10 == 0]
# new_nums = nums[:] #делаем копию
# new_nums[3] = 0
#
# print(new_nums[2:8])


def is_palindrome(num_list):
    reverse_list = num_list[::-1]
    if num_list == reverse_list:
        return True
    else:
        return False


nums = [1, 2, 3, 2, 1]
answer = []

for i in range(0, len(nums)):
    if is_palindrome(nums[i:len(nums)]):
        answer = nums[:i]
        answer.reverse()
        break

print(f'Исходный список: {nums}')
print(f'Нужно чисел: {len(answer)}')
print(f'Список этих чисел {answer}')

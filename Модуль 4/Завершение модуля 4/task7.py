nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [j for j in nice_list for p in j for j in p]
print(new_list)

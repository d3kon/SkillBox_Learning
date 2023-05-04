def union_with_dict(list1, list2, list3):
    return set(list1).intersection(set(list2).intersection(set(list3)))


def difference_array1(list1, list2, list3):
    return set(list1) - set(list2 + list3)


def intersection_without_dict(list1, list2, list3):
    array__4 = [value for value in list1 if value in list2 and value in list3]
    return array__4


def difference_without_dict(list1, list2, list3):
    return [value for value in list1 if value not in (list2 or list3)]


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

if __name__ == '__main__':
    print(intersection_without_dict(array_1, array_2, array_3))
    print(union_with_dict(array_1, array_2, array_3))
    print(difference_array1(array_1, array_2, array_3))
    print(difference_without_dict(array_1, array_2, array_3))

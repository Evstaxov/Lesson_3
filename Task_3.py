def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return "enter only a numbers!"

print(my_func(2, 11, -30))
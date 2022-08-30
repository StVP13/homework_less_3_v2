def my_func(num_1, num_2, num_3):
    try:
        my_list = list(map(float, [num_1, num_2, num_3]))
        my_list.remove(min(my_list))
        return sum(my_list)
    except (TypeError, ValueError):
        return 'Enter only a number!'

    print(my_func(input(), input(), input()))

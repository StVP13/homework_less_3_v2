def my_pow_func(x, y):
    try:
        res = x ** y
    except TypeError:
        return 'enter a float number and a negative power'
    return res

print(my_pow_func(1.2, -2))
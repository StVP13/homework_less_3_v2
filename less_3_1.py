def div(n_1, n_2):
    try:
        n_1, n_2 = int(n_1), int(n_2)
        div_num = n_1 / n_2
    except ValueError:
        return 'ValueError'
    except ZeroDivisionError:
        return 'Division by zero forbidden!'
    return round(div_num, 4)
print(div(input('введите первое число - '), input('введите второе число - ')))

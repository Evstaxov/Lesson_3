def my_pow_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Enter a float number and a negative power"
    return res

print(my_pow_fun(4.5, -2))
# name - constant, function, class names
# Built-in names:
# built-in functions (print, min, max, len)
# built-in data types (int, float, list, dict)
# built-in exceptions (Exception, IndexError, ValueError)

GLOBAL_VAR = 100


def func(a):
    x = 1
    # global GLOBAL_VAR
    # GLOBAL_VAR = 0

    def inner(b):
        y = 2
        # nonlocal x
        # x = 10000

        print(' --- Local level (inside inner()) --- ')
        print('Built-in names are visible:', type, list, NameError)
        print('Global names are visible:', GLOBAL_VAR, func)
        print('Enclosing names are visible:', a, x)
        print('Local names are visible:', b, y)

    inner('X')

    print(' --- Enclosing level (inside func()) --- ')
    print('Built-in names are visible:', type, list, NameError)
    print('Global names are visible:', GLOBAL_VAR, func)
    print('Local names are visible:', a, x, inner)


func('Ana')
print(' --- Global level --- ')
print('Built-in names are visible:', type, list, NameError)
print('Global names are visible:', GLOBAL_VAR, func)

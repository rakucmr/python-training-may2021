import functools


def make_pretty(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("I got decorated")
        return func(*args, **kwargs)
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


@make_pretty
def greet(name):
    print(f'Hello, {name}!')


@make_pretty
def add(a, b):
    """Adds two numbers"""
    return a + b


ordinary()
greet('Ana')
result = add(10, 20)
print('Result', result)

# ordinary = make_pretty(ordinary)  # decoration
# ordinary()
# make_pretty(ordinary)()
# make_pretty.<locals>.inner()

import functools
from time import time, sleep


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


def running_time(function):
    def inner(*params, **kwargs):
        start_time = time()
        ret = function(*params, **kwargs)
        print("Run time:", time() - start_time)
        return ret
    return inner


@running_time
def filter_short_words(word_list, max_length):
    sleep(2)  # mock a slow function
    return filter(lambda word: len(word) < max_length, word_list)


# filter_short_words = running_time(filter_short_words)


@running_time
def sort_words(*words):
    return sorted(set(words), key=words.count, reverse=True)


if __name__ == '__main__':
    ordinary()
    greet('Ana')
    result = add(10, 20)
    print('Result', result)

    # ordinary = make_pretty(ordinary)  # decoration
    # ordinary()
    # make_pretty(ordinary)()
    # make_pretty.<locals>.inner()

    word_list = ["aaa", "bbbbb", "ccccccc", "ddddd"]
    print(list(filter_short_words(word_list, max_length=4)))

    print(sort_words("aaa", "aaa", "aaa", "bb", "bb", "bb", "bb", "c"))

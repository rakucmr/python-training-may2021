import functools
import time


def timeit(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        time_before = time.time()
        return_value = func(*args, **kwargs)
        print(f'Execution time for {func.__name__} with args={args} and kwargs={kwargs}:',
              time.time() - time_before)
        return return_value
    return inner


@timeit
def long_exec_time(lim1, lim2):
    s = 0
    for i in range(lim1):
        for j in range(lim2):
            s += i * j
    return s


if __name__ == '__main__':
    s1 = long_exec_time(2000, 2000)
    s2 = long_exec_time(5000, 5000)
    print(s1, s2)

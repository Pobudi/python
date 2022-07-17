import time


def speed_calc_decorator(function):
    def wrapper():
        time_before = time.time()
        function()
        time_after = time.time()
        print(time_after - time_before)
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


slow_function()

import time

def function_details(function):
    def wrapper(*args):
        time_zero = time.time()
        print(f"{function.__name__}{args}\nIt returned: {function(*args)}\nTime it took: {time.time() - time_zero}")
    return wrapper


@function_details
def random_function(*args):
    i = 1
    for number in args:
        i *= number
    # Zeby opoznic
    for j in range(100000):
        j * j
    return i


random_function(2, 5, 6, 5, 5, 5, 9, 9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9)

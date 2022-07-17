import time


def delay(function):
    def wrapper():
        time.sleep(5)
        function()
    return wrapper


# Teraz jak wywolam say_hello to bedzie opoznienie 2 sek
# @delay
def say_hello():
    print("Hello")


## Alternatywa do @
# wer = delay(say_hello)
# wer()
say_hello()

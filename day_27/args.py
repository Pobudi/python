def add(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


suma = add(2, 3, 4, 6, 7, 3)
print(suma)
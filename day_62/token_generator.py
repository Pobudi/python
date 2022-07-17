import random


class TokenGenerator:

    def __init__(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        list1 = [random.choice(letters) for _ in range(random.randint(10, 12))]
        list2 = [random.choice(numbers) for _ in range(random.randint(4, 6))]
        list3 = [random.choice(symbols) for _ in range(random.randint(4, 6))]

        password = list1 + list2 + list3
        random.shuffle(password)
        self.password = "".join(password)

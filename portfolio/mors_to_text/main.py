import winsound
import time

mors_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "0": "-----"}

frequency = 1000
duration_dot = 200
duration_dash = 600

text = input("Insert your text to translate: ")
for letter in text:
    if letter == " ":
        # daje dlugosc 4 kropek bo przed spacja zawsze jestkoniec litery wiec tez przerwa 3 kropek
        time.sleep(4*duration_dot/1000)
    else:
        for sign in mors_dict[letter.capitalize()]:
            if sign == ".":
                winsound.Beep(frequency, duration_dot)
                time.sleep(duration_dot/1000)
            else:
                winsound.Beep(frequency, duration_dash)
                time.sleep(duration_dot/1000)
    time.sleep(2*duration_dot/1000)



import pandas

data_frame = pandas.read_csv("./nato_phonetic_alphabet.csv")
#itterows do pandas DataFrame
formatted_dictionary = {row.letter: row.code for (index, row) in data_frame.iterrows()}

while True:
    word = input("Insert a word to be translated: ")
    try:
        list_translated = [formatted_dictionary[letter.upper()] for letter in word]
    except KeyError:
        print("Use only letters")
    else:
        print(list_translated)

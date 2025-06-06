import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    name = input("What is your name? ").upper()
    try:
        name_list = [data_dict[letter] for letter in name]
    except KeyError:
        print("Sorry only English alphabet letters are accepted.")
        generate_phonetic()
    else:
        print(name_list)


generate_phonetic()

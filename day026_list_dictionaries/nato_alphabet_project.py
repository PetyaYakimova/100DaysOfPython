import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("What is your name? ").upper()
name_list = [data_dict[letter] for letter in name]
print(name_list)

import pandas

df_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_phonetic = {row.letter: row.code for (index, row) in df_phonetic.iterrows()}

def generate_phonetic():
    user_input = [char for char in input("Enter a word: ")]
    try:
        phonetic_list_from_input = [dict_phonetic[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list_from_input)

generate_phonetic()

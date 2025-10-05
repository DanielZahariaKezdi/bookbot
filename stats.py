from collections import Counter

def get_num_words(book_to_string):
    words = book_to_string.split()
    return words

def letter_counter(words):

    letter_dict = {}

    for word in words:
        for letter in word:

            if letter.isalpha():

                letter = letter.lower()
                letter_dict[letter] = letter_dict.get(letter, 0) + 1
                
    letter_dict_list = list(letter_dict.items())

    return  letter_dict_list
    
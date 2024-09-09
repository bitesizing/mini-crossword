# %%
import numpy as np

""" File from which to run the project (runs with f8) """

"""
- Import the text
- Generate the 130 sets of 5-letter words
- Generate the starting set of letters
"""

def letter_to_number(letter: str):
    return ord(letter.lower()) - ord('a')

with open("5-letter-words.txt", "r") as f:
    flws = [line.strip() for line in f.readlines()]

sets = [[set() for _ in range(26)] for _ in range(5)]
full_set = set(flws[:-1])

for word in flws:
    for letter_idx, letter in enumerate(word):
        sets[letter_idx][letter_to_number(letter)].add(word)

# Down first, then across
starting_words = [
    "",
    "",
    "",
    "",
    "",

    "",
    "",
    "",
    "",
    "",
]

def find_legal_words(word: str):
    legal_words = full_set.copy()
    for letter_idx, letter in enumerate(word):
        if letter != "":
            legal_words = legal_words & sets[letter_idx][letter_to_number(letter)]
    return legal_words

matrix = np.full((5, 5), "")

for column_idx in range(5):
    down_word = matrix[:, column_idx]
    legal_words = find_legal_words(down_word)

for row_idx in range(5):
    across_word = matrix[row_idx, :]
    legal_words = find_legal_words(across_word)

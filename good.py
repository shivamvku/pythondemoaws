#!/usr/bin/env python

"""This script prompts a user to enter a message to encode or decode
using a classic Caeser shift substitution (3 letter shift)
from https://docs.pylint.org/en/1.9/tutorial.html"""

import string

shift = 3
choice = input("would you like to encode or decode?")
word = (input("Please enter text"))
letters = string.ascii_letters + string.punctuation + string.digits
encoded = ''
if choice == "encode":
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) + shift
            encoded = encoded + letters[x]
if choice == "decode":
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
    else:
        x = letters.index(letter) - shift
        encoded = encoded + letters[x]
print(encoded)
